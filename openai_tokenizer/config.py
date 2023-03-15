import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="openai_tokenizer",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="openai_tokenizer_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from openai_tokenizer.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export openai_tokenizer_KEY=value
export openai_tokenizer_KEY="@int 42"
export openai_tokenizer_KEY="@jinja {{ this.db.uri }}"
export openai_tokenizer_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
openai_tokenizer_ENV=production openai_tokenizer run
```

Read more on https://dynaconf.com
"""
