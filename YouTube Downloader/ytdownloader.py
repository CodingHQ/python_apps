from pytube import YouTube

a = True

while a:
    link = input("Поставете линка на видеото, което искате да изтеглите: ")
    if link.lower() == "stop":
        break

    yt = YouTube(link)
    print("Title:",yt.title)
    print("Number of views: ", yt.views)
    print("Lenght of video: ", yt.length)
    print("Rating of video: ", yt.rating)

    ys = yt.streams.get_highest_resolution()
    vn = "videos/" + yt.title
    print("Downloading...")
    ys.download(vn)
    print("Download completed")