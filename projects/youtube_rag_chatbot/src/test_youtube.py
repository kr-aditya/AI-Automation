from youtube import extract_video_id


urls = [
    "https://www.youtube.com/watch?v=abc123",
    "https://youtu.be/abc123",
]


for url in urls:
    print(
        url,
        "→",
        extract_video_id(url),
    )