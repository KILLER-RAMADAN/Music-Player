import yt_dlp
from tkinter import filedialog
import tkinter
from tkinter import *
import os





def down():
 try:
  URLS =f'https://youtube.com/shorts/T2RoyZYii6w?feature=share'

  ydl_opts = {
    'format': 'bestaudio/best',
    # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    
    'outtmpl':f'Desktop\\DownoadedSongs\\{locate_entry.get()}.mp3',


  }  

  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    error_code = ydl.download(URLS)
 except:
     pass
    
def locate():
    locate_entry.delete(0,1000)
    global file_location
    file_location=filedialog.askdirectory(initialdir=os.getcwd(),title="select location")
    locate_entry.insert(END,file_location)
    
root=tkinter.Tk()
root.geometry("400x400")


locate_entry=Entry(root,width=20,font=("arial,15"))
locate_entry.place(x=0,y=0)

file_button=Button(root,text="directory",width=10,height=8,command=locate)
file_button.place(x=30,y=50)


download_button=Button(root,text="download",width=5,command=down)
download_button.place(x=100,y=0)

root.mainloop()