import yt_dlp
import os

URL_FILE = "urls.txt"


def load_urls_from_file():
    if not os.path.exists(URL_FILE):
        return []

    with open(URL_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def save_urls_to_file(urls):
    with open(URL_FILE, "w", encoding="utf-8") as f:
        for url in urls:
            f.write(url + "\n")


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

    remaining_urls = urls.copy()

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for index, url in enumerate(urls, start=1):
            print(f"\n[{index}/{len(urls)}] Завантаження: {url}")
            try:
                ydl.download([url])
                print(" -> Готово.")
                remaining_urls.remove(url)
                save_urls_to_file(remaining_urls)
            except Exception as e:
                print(f" -> Помилка: {e}")

    print("\nУсі посилання опрацьовано.")


# ======================================================
# MAIN
# ======================================================

if __name__ == "__main__":

    urls = []

    if os.path.exists(URL_FILE):
        saved_urls = load_urls_from_file()
        if saved_urls:
            choice = input(
                f"Знайдено файл з {len(saved_urls)} посиланнями. Продовжити завантаження? (y/n): "
            ).strip().lower()

            if choice == "y":
                urls = saved_urls

    if not urls:
        print("\nВведіть посилання для завантаження (по одному):")
        print("Коли закінчите — напишіть 'end'\n")

        while True:
            user_input = input("URL: ").strip()

            if user_input.lower() == "end" or user_input == "":
                break

            urls.append(user_input)

        if urls:
            save_urls_to_file(urls)

    if not urls:
        print("Немає посилань для завантаження. Завершення.")
    else:
        print(f"\nПочинаю завантаження {len(urls)} посилань...\n")
        download_videos(urls)
