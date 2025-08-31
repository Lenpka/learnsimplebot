from dataclasses import dataclass
from environs import Env
@dataclass
class LogSetting:
    level:str
    format:str

@dataclass
class TgBot:
    token:str

@dataclass
class Config:
    bot:TgBot
    log:LogSetting

def load_config(path:str| None=None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        bot = TgBot(
            env("BOT_TOKEN")

        ),
        log=LogSetting(
            level = env("LOG_LEVEL"),
            format= env("LOG_FORMAT")
        )
    )
