import sys
import time
from tkinter import *
from tkinter import ttk
from pytube import YouTube


def startDownload(urlVar):
    try:
        yt = YouTube(urlVar, on_progress_callback=progressBar)

        if yt.age_restricted == True:
            print("This video is age restricted")
            raise Exception("Age restricted video")

        video = yt.streams.get_highest_resolution()

        print("Downloading: ", yt.title)
        video.download()
        finishLabel.configure(text="Download complete", foreground="green")

    except KeyboardInterrupt:
        finishLabel.configure(text="Download cancelled... Exiting!", foreground="red")
        time.sleep(1)
        sys.exit(0)

    except Exception as e:
        finishLabel.configure(text=e.args[0], foreground="red")

    return


def progressBar(stream, chunks, bytes_remaining):
    total_bytes = stream.filesize
    bytes_downloaded = total_bytes - bytes_remaining
    percentCompletion = bytes_downloaded / total_bytes * 100
    progress["value"] = percentCompletion
    app.update_idletasks()
    percentageLabel.configure(text=str(int(percentCompletion)) + "%")
    return


# App based settings

app = Tk()
app.geometry("720x480")
app.title("Youtube Downloader")

## Adding UI elements

### Label text
title = ttk.Label(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

### Text input
urlVar = StringVar()
link = ttk.Entry(app, width=350, textvariable=urlVar)
link.pack(padx=15, pady=15)

## Add a finish label
finishLabel = ttk.Label(app, text="")
finishLabel.pack(padx=10, pady=10)

## Add a progress bar
percentageLabel = ttk.Label(app, text="0%")
percentageLabel.pack(padx=20, pady=20)
progress = ttk.Progressbar(
    app,
    length=400,
    mode="indeterminate",
)
progress.pack(padx=10, pady=10)

### Button
action = ttk.Button(
    app,
    command=lambda: startDownload(urlVar.get()),
    text="Start Download",
)
action.pack(padx=20, pady=20)

## Run the app
app.mainloop()
