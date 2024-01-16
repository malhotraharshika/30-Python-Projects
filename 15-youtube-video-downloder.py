from pytube import YouTube

def download_youtube_video(video_link, output_path=None):
    try:
        yt = YouTube(video_link)
        stream = yt.streams.get_highest_resolution()

        if output_path is None:
            output_path = "./" + yt.title + ".mp4"

        print("Downloading:", yt.title)
        print(".....")
        stream.download(output_path)
        print("Download completed!")

    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    youtube_video_link = input("Enter url here: ")

    output_path = "D:"

    download_youtube_video(youtube_video_link, output_path)
# https://www.youtube.com/watch?v=AcVaF1w34SU
