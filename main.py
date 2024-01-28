import asyncio
from pprint import pprint

from tiktokapipy.async_api import AsyncTikTokAPI
from tiktokapipy.models.challenge import Challenge
from tiktokapipy.models.video import Video

# TikTokApiPy: https://tiktokpy.readthedocs.io/en/latest/reference/api_reference.html

tags: list[str] = ["climatechange", "nuclear", "nuclearenergy"]
limit: int = 10


async def get_tiktoks_by_tag(tag: str):
    '''
    Gets the TikToks returned first on the platform for a given tag.
    '''
    tiktok_collection = []

    async with AsyncTikTokAPI() as api:
        # Challenge is the TikTok internal name for a hashtag
        challenge: Challenge = await api.challenge(tag, video_limit=10)

        async for video in challenge.videos:
            assert isinstance(video, Video)
            data = {
                "desc": video.desc,
                "plays": video.stats.play_count,
                "comments": video.stats.comment_count,
                "url": video.url,
            }
            tiktok_collection.append(data)

    return tiktok_collection


def main():
    for tag in tags:
        print(f"Getting TikToks for #{tag}")
        results = asyncio.run(get_tiktoks_by_tag(tag))
        pprint(results)


if __name__ == "__main__":
    main()
