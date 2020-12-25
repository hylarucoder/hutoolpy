from functools import lru_cache

from pydantic import BaseSettings, PostgresDsn


class PvSettings(BaseSettings):
    TITLE: str = "Pv"

    class Config:
        case_sensitive = True
        env_prefix = "PV_"


@lru_cache()
def get_settings() -> PvSettings:
    # override if required
    return PvSettings(_env_file=".env")
