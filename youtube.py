import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import filedialog, messagebox


def createWidgets():
    link=Label(root, text="Youtube URL:", bg="grey")
    link.grid(row=1, column=0, pady=5, padx=5)
    #creating input for inserting the link
    root.link_text=Entry(root, width=60, textvariable=video_url)
    #locating the entry
    root.link_text.grid(row=1, column=1, pady=5, padx=5)
    #destination path
    des_label= Label(root, text="Destination:", bg="grey")
    des_label.grid(row=2, column=0,pady=5, padx=5)

    root.des_text =Entry(root, width=45, textvariable=download_path)
    root.des_text.grid(row=2, column=1, pady=3, padx=3)

    browse_but=Button(root, text="Browse", command=browse, width=10, bg="red")
    browse_but.grid(row=2, column=2, pady=1, padx=1)

    download_but=Button(root, text="Download Video", command=download_video, width=25, bg="red")
    download_but.grid(row=3, column=1, pady=3, padx=3)
def browse():
    download_dir= filedialog.askdirectory(initialdir="your Directory path")
    download_path.set(download_dir)
def download_video():
    url= video_url.get()
    folder= download_path.get()

    get_video= YouTube(url)
    get_stream=get_video.streams.filter(file_extension='mp4', progressive='True').get_by_itag(22)
    get_stream.download(folder)

    messagebox.showinfo("video downloaded! video located at\n"+folder)
root =tk.Tk()


root.geometry("600x300")
root.resizable(False, False)
root.title("Video downloader")
root.config(background="black")

video_url=StringVar()
download_path=StringVar()
createWidgets()
root.mainloop() 