from rsserpent.models import Persona, Plugin

from . import comic


plugin = Plugin(
    name="rsserpent-plugin-manhuagui",
    author=Persona(
        name="wdssmq",
        link="https://github.com/wdssmq",
        email="wdssmq@qq.com",
    ),
    prefix="/manhuagui",
    repository="https://github.com/wdssmq/rsserpent-plugin-manhuagui",
    routers={comic.path: comic.provider},
)
