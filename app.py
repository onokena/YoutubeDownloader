import customtkinter as ctk
from tkinter import ttk
from pytube import YouTube
import os

resolution_labels = {
    "2160p": "4k",
    "1440p": "2k",
    "1080p": "1080p",
    "720p": "720p",
    "480p": "480p"
}

def download_video():
    url = entry_url.get()
    resolution = resolutions_var.get()

    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        stream = yt.streams.filter(res=resolution).first()
        output_path = os.path.join("downloads", f"{yt.title}.mp4")
        stream.download(output_path=output_path)
        status.configure(text="Download complete", text_color="white", fg_color="green")
    except Exception as e:
        status.configure(text=f"Error: {str(e)}", text_color="white", fg_color="red")

def on_progress(stream, chunk, remaining):
    total_size = stream.filesize
    download_remain = total_size - remaining
    percentage_completed = download_remain / total_size * 100

    progress.configure(text=str(int(percentage_completed)) + "%")
    progress.update()

    progress_bar.set(float(percentage_completed / 100))

root = ctk.CTk()
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")
root.title("Youtube downloader")
root.geometry("720x480")
root.minsize(720, 480)
root.maxsize(1080, 720)

content_frame = ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH, expand=True, padx=5, pady=5)

url = ctk.CTkLabel(content_frame, text="Youtube link")
url.pack(pady=("10p"))
entry_url = ctk.CTkEntry(content_frame, width=400, height=40)
entry_url.pack(pady=("15p"))

download = ctk.CTkButton(content_frame, text="Download now", command=download_video)
download.pack(pady=("10p"))

resolutions = ["2160p", "1440p", "1080p", "720p", "480p"]
resolutions_var = ctk.StringVar()
resolutions_combinations = ttk.Combobox(content_frame, values=[resolution_labels[res] for res in resolutions], textvariable=resolutions_var)
resolutions_combinations.pack(pady=("10p"))
resolutions_combinations.set("1080p") 

progress = ctk.CTkLabel(content_frame, text="0%")
progress.pack(pady=("10p"))

progress_bar = ctk.CTkProgressBar(content_frame, width=400)
progress_bar.set(0.6)

status = ctk.CTkLabel(content_frame, text="Finished")

root.mainloop()