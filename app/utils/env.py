from os import getenv

def getvar(var) -> str:
    env_var = getenv(var)
    if env_var:
        return env_var
    else:
        raise Exception("Environment Variable not set: {}".format(var))
