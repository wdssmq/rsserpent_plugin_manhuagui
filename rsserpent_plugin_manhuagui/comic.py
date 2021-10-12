from typing import Any, Dict

from pyquery import PyQuery
from rsserpent.utils import HTTPClient, cached


path = "/manhuagui/comic/{cid}"


@cached
async def provider(cid: int) -> Dict[str, Any]:
    """获取漫画章节."""
    link = f"https://www.manhuagui.com/comic/{cid}/"

    async with HTTPClient() as client:
        response = await client.get(link)

    dom = PyQuery(response.text)
    title = dom(".book-title h1").text()
    description = dom("#intro-cut").text()

    el_chapters = dom(".chapter-list > ul li").items()

    return {
        "title": title,
        "link": link,
        "description": description,
        "items": [
            {
                "title": item("a").attr("title"),
                "description": f"{item('a').attr('title')} - {item('i').text()}",
                "link": f"https://www.manhuagui.com{item('a').attr('href')}",
                "author": "manhuagui",
            }
            for item in el_chapters
        ],
    }
