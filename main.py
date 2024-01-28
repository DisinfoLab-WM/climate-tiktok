import asyncio
from pprint import pprint

from tiktokapipy.async_api import AsyncTikTokAPI
from tiktokapipy.models.challenge import Challenge
from tiktokapipy.models.video import Video

# TikTokApiPy: https://tiktokpy.readthedocs.io/en/latest/reference/api_reference.html

tag_name: str = "climatechange"
limit: int = 10


async def get_tiktok_test():
    tiktok_collection = []

    async with AsyncTikTokAPI() as api:
        # Challenge is the TikTok internal name for a hashtag
        challenge: Challenge = await api.challenge(tag_name, video_limit=10)

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
    results = asyncio.run(get_tiktok_test())
    pprint(results)


if __name__ == "__main__":
    main()
