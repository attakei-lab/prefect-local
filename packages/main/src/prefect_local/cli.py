"""CLI behaviors."""

import argparse
import importlib
import sys
from pathlib import Path

from prefect import serve
from prefect.deployments import Deployment
from prefect.flows import Flow

from .settings import DeploymentSettings, Settings

parser = argparse.ArgumentParser()
parser.add_argument("--conf", type=Path, default=Path.cwd() / "settings.toml")


def generate_deployments(settings: Settings) -> list[Deployment]:
    """Generate deployments definition from settings."""

    def _generate_deployment(name: str, settings: DeploymentSettings) -> Deployment:
        module, func = settings.flow.split(":")
        kwargs = settings.dict(exclude="flow")
        flow: Flow = getattr(importlib.import_module(module), func)
        return flow.to_deployment(name=name, **kwargs)

    return [_generate_deployment(name, ds) for name, ds in settings.deployments.items()]


def main():
    """Entrypoint of CLI."""
    args = parser.parse_args()
    settings = Settings.load_from_tomlpath(args.conf)
    sys.path.insert(0, str(settings.scripts_dir))
    deployments = generate_deployments(settings)
    serve(*deployments)
