from urllib.parse import parse_qs, urlparse


def extract_video_id(url: str) -> str:
    parsed_url = urlparse(url)

    if parsed_url.hostname in {
        "www.youtube.com",
        "youtube.com",
        "m.youtube.com",
    }:
        video_id = parse_qs(
            parsed_url.query
        ).get("v")

        if video_id:
            return video_id[0]

    if parsed_url.hostname == "youtu.be":
        return parsed_url.path.lstrip("/")

    raise ValueError("Invalid YouTube URL.")