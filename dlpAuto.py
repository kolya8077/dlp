import yt_dlp


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
                print(" -> Готово.")
            except Exception as e:
                print(f" -> Помилка: {e}")

    print("\nУсі посилання опрацьовано.")


# ======================================================
# БЛОК ВВЕДЕННЯ URL З ТЕРМІНАЛУ
# ======================================================

if __name__ == "__main__":

    url_list = []

    print("Введіть посилання для завантаження (по одному):")
    print("Коли закінчите — напишіть 'end'\n")

    while True:
        user_input = input("URL: ").strip()

        if user_input.lower() == "end":
            break

        if user_input == "":
            break

        url_list.append(user_input)

    if not url_list:
        print("Не введено жодного посилання. Завершення.")
    else:
        print(
            f"\nОтримано {len(url_list)} посилань. Починаю завантаження...\n")
        download_videos(url_list)
