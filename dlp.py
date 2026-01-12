import yt_dlp

# url = 'https://nl201.cdnsqu.com/s/FHYxZHhwqyLpJZMYer5M37e0FBQUFBSUFjS0VFUkZOTGhCZlFBQlFFPQ.2_vUkMjuopRxdjG3mRF8LUVB26lpxgmt48qPpw/hdr_018/Ant-Man.2015.BDRip.2160p.dub.ukr.ru_2160.mp4'
# yt_dlp.YoutubeDL().download([url])


# Тепер url_list — список посилань
url_list = [
    "https://youtu.be/vR3CZ9kH2p0"
    # 'https://nl201.cdnsqu.com/s/FHBeE14c1xxFpEVn77lK2LDEFBQUFBSUFjS0VFUlJCS1JndlFBQlFFPQ.S1L1H1rryEMPlpzz0tondjk8iHW0R5xoD9cQ9g/hd_02/Spider.Man-Homecoming.2017.BDRip.1080p.UKR_1080.mp4'
]


def download_videos(urls):
    ydl_opts = {
        "outtmpl": "downloads_dlp/%(title)s.%(ext)s",
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "noplaylist": True,
        "quiet": False,
        "no_warnings": True,
        "ignoreerrors": True,
        "retries": 5,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for index, url in enumerate(urls, start=1):
            print(f"\n[{index}/{len(urls)}] Завантаження: {url}")
            try:
                ydl.download([url])
                print(f" -> Готово.")
            except Exception as e:
                print(f" -> Помилка: {e}")

    print("\nУсі посилання опрацьовано.")


# Виклик функції
download_videos(url_list)
