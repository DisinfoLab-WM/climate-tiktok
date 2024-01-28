from tiktokapipy.api import TikTokAPI
from tiktokapipy.models.video import Video
from tiktokapipy.models.challenge import Challenge
from pprint import pprint

# TikTokApiPy: https://tiktokpy.readthedocs.io/en/latest/reference/api_reference.html

tag_name: str = "climatechange"
limit: int = 10

def get_tiktok_test():
    tiktok_collection = []

    with TikTokAPI() as api:
        # Challenge is the TikTok internal name for a hashtag
        challenge: Challenge = api.challenge(tag_name, video_limit=10)

        for video in challenge.videos: 
            assert isinstance(video, Video) 
            data = {
                "desc": video.desc,
                "plays": video.stats.play_count,
                "comments": video.stats.comment_count,
                "url": video.url
            }
            tiktok_collection.append(data)

    return tiktok_collection


def main():
    results = get_tiktok_test()
    pprint(results)


if __name__ == '__main__':
    main()