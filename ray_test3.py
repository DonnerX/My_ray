from ray.tune.registry import register_env
from ~.xiaoleiacrobot import AcrobotEnv

def env_creator(env_config):
    return AcrobotEnv()

register_env("my_env",env_creator)

