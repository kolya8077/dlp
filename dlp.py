import yt_dlp

# url = 'https://nl201.cdnsqu.com/s/FHYxZHhwqyLpJZMYer5M37e0FBQUFBSUFjS0VFUkZOTGhCZlFBQlFFPQ.2_vUkMjuopRxdjG3mRF8LUVB26lpxgmt48qPpw/hdr_018/Ant-Man.2015.BDRip.2160p.dub.ukr.ru_2160.mp4'
# yt_dlp.YoutubeDL().download([url])


# Тепер url_list — список посилань
url_list = [
''
]


def download_videos(urls):
    ydl_opts = {
        "outtmpl": "downloads/%(title)s.%(ext)s",
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
