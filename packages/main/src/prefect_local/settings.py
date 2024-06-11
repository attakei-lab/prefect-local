"""Settings for runner works."""

import tomllib
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings


class DeploymentSettings(BaseModel):
    """Configuration for deployment unit."""

    flow: str
    cron: str | None = None
    parameters: dict[str, Any] | None = None


class Settings(BaseSettings):
    """Local worker settings."""

    scripts_dir: Path
    deployments: dict[str, DeploymentSettings] = Field(default_factory=dict)

    @classmethod
    def load_from_tomlpath(cls, src: Path) -> "Settings":  # noqa: D102
        obj = tomllib.loads(src.read_text())
        return cls.parse_obj(obj)
