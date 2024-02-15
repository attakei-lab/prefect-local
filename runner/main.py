"""Entrypoint for running as single local runner."""
import argparse
import importlib
import sys
import tomllib
from pathlib import Path
from typing import Any

from prefect import serve
from prefect.deployments import Deployment
from prefect.flows import Flow
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings


class DeploymentSettings(BaseModel):
    """Configuration for deployment unit."""

    flow: str
    cron: str | None = None
    parameters: dict[str, Any] | None = None


class Settings(BaseSettings):
    """Local worker settings."""

    deployments: dict[str, DeploymentSettings] = Field(default_factory=dict)

    @classmethod
    def load_from_tomlpath(cls, src: Path) -> "Settings":  # noqa: D102
        obj = tomllib.loads(src.read_text())
        return cls.parse_obj(obj)


def generate_deployments(settings: Settings) -> list[Deployment]:  # noqa: D103
    def _generate_deployment(name: str, settings: DeploymentSettings) -> Deployment:
        module, func = settings.flow.split(":")
        kwargs = settings.dict(exclude="flow")
        flow: Flow = getattr(importlib.import_module(module), func)
        return flow.to_deployment(name=name, **kwargs)

    return [_generate_deployment(name, ds) for name, ds in settings.deployments.items()]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--conf", type=Path, default=Path.cwd() / "settings.toml")
    # Append src directory into python-path
    here = Path(__file__).parent
    sys.path.insert(0, str(here))
    args = parser.parse_args()
    settings = Settings.load_from_tomlpath(args.conf)
    deployments = generate_deployments(settings)
    serve(*deployments)
