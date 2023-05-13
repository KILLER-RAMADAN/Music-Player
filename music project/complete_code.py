import tkinter as tk
from ttkthemes import themed_tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog
from mutagen.mp3 import MP3
import os
import time
import pygame
from tkinter import messagebox
import customtkinter
from customtkinter import *
import yt_dlp
import os
import threading
import sys
class MediaPlayer:
    def __init__(self, window):

        style =ttk.Style()
        
        
        self.home_directory = os.path.expanduser( '~' )

        background = "grey"

        style.configure("TScale", background="#FFFFFF")
        self.root = window

        self.root.configure(bg="dark")
        
        self.back =tk.PhotoImage(file='images/back.png')
        self.img_lable=tk.Label(image=self.back,bg="white")
        self.img_lable.place(x=0,y=0)

        
        
        self.repeat_icon = Image.open('images/repeat.png')
        self.repeat_icon = self.repeat_icon.resize((40, 40), Image.ANTIALIAS)
        self.repeat_icon = ImageTk.PhotoImage(self.repeat_icon)

        self.repeat1_icon = Image.open('images/repeat1.png')
        self.repeat1_icon = self.repeat1_icon.resize((40, 40), Image.ANTIALIAS)
        self.repeat1_icon = ImageTk.PhotoImage(self.repeat1_icon)

        self.play_icon = Image.open('images/play.png')
        self.play_icon = self.play_icon.resize((80, 80), Image.ANTIALIAS)
        self.play_icon = ImageTk.PhotoImage(self.play_icon)

        self.pause_icon = Image.open('images/pause.png')
        self.pause_icon = self.pause_icon.resize((80, 80), Image.ANTIALIAS)
        self.pause_icon = ImageTk.PhotoImage(self.pause_icon)

        self.next_icon = Image.open('images/next.png')
        self.next_icon = self.next_icon.resize((70, 70), Image.ANTIALIAS)
        self.next_icon = ImageTk.PhotoImage(self.next_icon)

        self.previous_icon = Image.open('images/previous.png')
        self.previous_icon = self.previous_icon.resize((70, 70), Image.ANTIALIAS)
        self.previous_icon = ImageTk.PhotoImage(self.previous_icon)

        self.stop_icon = Image.open('images/stop.png')
        self.stop_icon = self.stop_icon.resize((90, 90), Image.ANTIALIAS)
        self.stop_icon = ImageTk.PhotoImage(self.stop_icon)

        self.speaker_icon = Image.open('images/speaker.png')
        self.speaker_icon = self.speaker_icon.resize((30, 30), Image.ANTIALIAS)
        self.speaker_icon = ImageTk.PhotoImage(self.speaker_icon)

        self.mute_icon = Image.open('images/mute.png')
        self.mute_icon = self.mute_icon.resize((30, 30), Image.ANTIALIAS)
        self.mute_icon = ImageTk.PhotoImage(self.mute_icon)

        
        self.add_song_icon = Image.open('images/song.png')
        self.add_song_icon = self.add_song_icon.resize((30, 30), Image.ANTIALIAS)
        self.add_song_icon = ImageTk.PhotoImage(self.add_song_icon)
        
        self.developer_icon = Image.open('images/code.png')
        self.developer_icon = self.developer_icon.resize((30, 30), Image.ANTIALIAS)
        self.developer_icon = ImageTk.PhotoImage(self.developer_icon)


        self.shuffle_icon = Image.open('images/shuffle.png')
        self.shuffle_icon = self.shuffle_icon.resize((40, 40), Image.ANTIALIAS)
        self.shuffle_icon = ImageTk.PhotoImage(self.shuffle_icon)

        self.auto_play_icon = Image.open('images/auto_play.png')
        self.auto_play_icon = self.auto_play_icon.resize((40, 50), Image.ANTIALIAS)
        self.auto_play_icon = ImageTk.PhotoImage(self.auto_play_icon)

        self.auto_play_not_icon = Image.open('images/auto_play_not.png')
        self.auto_play_not_icon = self.auto_play_not_icon.resize((40, 50), Image.ANTIALIAS)
        self.auto_play_not_icon = ImageTk.PhotoImage(self.auto_play_not_icon)
        
        self.heading_icon=tk.PhotoImage(file='images/death.png')
        self.head_image=tk.Button(self.root,bg="white",image=self.heading_icon,bd=0,command=self.add_songs)
        self.head_image.place(x=5,y=2)
        
        
        # Downloading Icons #
        self.download_sound_icon=tk.PhotoImage(file='images/download.png')
        self.download_video_icon=tk.PhotoImage(file='images/download.png')
        # Downloading Icons #
        
        

        self.songs_list = tk.Listbox(self.root, width=50, height=24, bg="white",font=("arial,bold"), fg="black", relief="flat",
                                     selectbackground="grey")
        self.songs_list.place(x=773 ,y=0)
        
        
        # White Frame #
        customtkinter.CTkLabel(self.root, text="",bg_color="white",height=300,width=900).place(x=0,y=450)
        # White Frame #
        
        # Social Icons #
        self.youtube_icon=tk.PhotoImage(file='images/youtube.png')
        self.facebook_icon=tk.PhotoImage(file='images/facebook.png')
        self.instegram_icon=tk.PhotoImage(file='images/instagram.png')
        self.twitter_icon=tk.PhotoImage(file='images/twitter.png')
        self.dropbox_icon=tk.PhotoImage(file='images/dropbox.png')
        self.gdrive_icon=tk.PhotoImage(file='images/google-drive.png')
        self.soundc_icon=tk.PhotoImage(file='images/sound cloud.png')
        self.tik_icon=tk.PhotoImage(file='images/tik-tok.png')
        # Social Icons #
        self.youtube_button_icon=tk.Button(self.root,text="youtube",font=("arial,10"),image=self.youtube_icon,background="white",bd=0,command=self.youtube_down)
        self.youtube_button_icon.place(x=670,y=570)
        self.facebook_button_icon=tk.Button(self.root,text="youtube",font=("arial,10"),image=self.facebook_icon,background="white",bd=0,command=self.facebook_down)
        self.facebook_button_icon.place(x=730,y=570)
        self.instagram_button_icon=tk.Button(self.root,text="youtube",font=("arial,10"),image=self.instegram_icon,background="white",bd=0,command=self.instagram_down)
        self.instagram_button_icon.place(x=790,y=570)
        self.twitter_button_icon=tk.Button(self.root,text="youtube",font=("arial,10"),image=self.twitter_icon,background="white",bd=0,command=self.twitter_down)
        self.twitter_button_icon.place(x=850,y=570)
        self.dropbox_button_icon=tk.Button(self.root,text="youtube",font=("arial,10"),image=self.dropbox_icon,background="white",bd=0,command=self.dropbox_down)
        self.dropbox_button_icon.place(x=670,y=625)
        self.google_button_icon=tk.Button(self.root,text="youtube",font=("arial,10"),image=self.gdrive_icon,background="white",bd=0,command=self.google_down)
        self.google_button_icon.place(x=730,y=625)
        self.scloud_button_icon=tk.Button(self.root,text="youtube",font=("arial,10"),image=self.soundc_icon,background="white",bd=0,command=self.sound_cloud_down)
        self.scloud_button_icon.place(x=790,y=625)
        self.tik_button_icon=tk.Button(self.root,text="youtube",font=("arial,10"),image=self.tik_icon,background="white",bd=0,command=self.tik_down)
        self.tik_button_icon.place(x=850,y=625)
        # Social Icons Buttons #
        
        # Stop Icons #
        self.stop_download_icon=tk.PhotoImage(file='images/loss.png')
        self.Stop_icon=tk.Button(self.root,text="Stop Download",font=("arial,10"),image=self.stop_download_icon,background="white",bd=0,command=self.cancel_down)
        self.Stop_icon.place(x=590,y=595)
        # Stop Icons #
        
        self.header_lable=tk.Label(self.root,text="Music Player With Full Downloader Access",font=("arial,20"),background="white")
        self.header_lable.place(x=110,y=10)
        self.header_lable_icon=tk.PhotoImage(file='images/cloud.png')
        self.cloud_button=tk.Button(self.root,text="Download",font=("arial,10"),image=self.header_lable_icon,background="white",bd=0,command=self.songs_location)
        self.cloud_button.place(x=500,y=10)
        
        self.get_link=customtkinter.CTkEntry(self.root,bg_color="white",width=300,font=("arial",15))
        self.get_link.place(x=90,y=55)
        
        self.link_lable=tk.Label(self.root,text="Sound Link",font=("arial,10"),background="white")
        self.link_lable.place(x=0,y=70)
        
        self.file_download_sound_button=tk.Button(self.root,text="Download",font=("arial,10"),image=self.download_sound_icon,background="white",bd=0,command=self.thread)
        self.file_download_sound_button.place(x=490,y=65)
        
        self.get_video_link=customtkinter.CTkEntry(self.root,bg_color="white",width=250,font=("arial",15))
        self.get_video_link.place(x=90,y=100)
        
        self.file_download_video_button=tk.Button(self.root,text="Download",font=("arial,10"),image=self.download_sound_icon,background="white",bd=0,command=self.thread2)
        self.file_download_video_button.place(x=430,y=120)
        
        self.file_name_lable=tk.Label(self.root,text="Video Link",font=("arial,10"),background="white")
        self.file_name_lable.place(x=0,y=130)
        
        
        
        self.time_elapsed_label = tk.Label(self.root,text="00:00:00", fg="black",background="white",
                                           activebackground=background,padx=5,font=("arial,5"),relief="ridge")
        self.time_elapsed_label.place(x=10,y=563)

        self.music_duration_label = tk.Label(self.root,text="00:00:00",fg="black",background="white",
                                             activebackground=background,padx=15,font=("arial,5"))
        self.music_duration_label.place(x=490,y=563)

        self.progress_scale = ttk.Scale(self.root,orient="horizontal",from_=0,length=380,
                                        command=self.progress_scale_moved,cursor='hand2')
        self.progress_scale.place(x=120,y=565)

        self.play_button = tk.Button(self.root,image=self.play_icon,command=self.check_play_pause,cursor='hand2',bd=0,
                                     background="white",activebackground="white")
        self.play_button.place(x=150,y=595)

        self.next_button = tk.Button(self.root, image=self.next_icon, command=self.next_song, cursor='hand2', bd=0,
                                     background="white", activebackground="white")
        self.next_button.place(x=328, y=595)

        self.previous_button = tk.Button(self.root, image=self.previous_icon, command=self.previous_song, cursor='hand2', bd=0,
                                     background="white", activebackground="white")
        self.previous_button.place(x=73, y=595)

        self.stop_button = tk.Button(self.root, image=self.stop_icon, command=self.stop_song, cursor='hand2', bd=0,
                                     background="white", activebackground="white")
        self.stop_button.place(x=236, y=590)

        self.shuffle_button = tk.Button(self.root, image=self.shuffle_icon, command=self.shuffle_songs, cursor='hand2', bd=0,
                                     background="white", activebackground="white")
        self.shuffle_button.place(x=10, y=595)

        self.speaker_button = tk.Button(self.root, image=self.speaker_icon, command="command", cursor='hand2', bd=0,
                                     background="white", activebackground="white")
        self.speaker_button.place(x=395, y=595)

        self.repeat_button = tk.Button(self.root, image=self.repeat_icon, command=self.repeat_song, cursor='hand2', bd=0,
                                     background="white", activebackground="white")
        self.repeat_button.place(x=10, y=640)

        self.auto_play_button = tk.Button(self.root, image=self.auto_play_not_icon, command=self.auto_play_song, cursor='hand2', bd=0,
                                     background="white", activebackground="white")
        self.auto_play_button.place(x=540, y=595)
    

        self.vol_scale = ttk.Scale(self.root, from_=0,to=100,orient="horizontal",style="TScale",command=self.volume,cursor="hand2")
        self.vol_scale.place(x=430,y=597)

        self.status = tk.Label(self.root,text="Ready To Run : ---------- Song : 0 of 0",width=0,fg="black",anchor="w",background="white",
                               font="arial 12 bold",bd=1,relief="ridge")
        self.status.place(x=0,y=684,relwidth=1)

        self.menu = tk.Menu(self.root)
        self.root.configure(menu=self.menu)
        
        # Menue #
        m1 = tk.Menu(self.menu,background="white",tearoff=True,bd=0,activebackground="black")
        self.menu.add_cascade(label="Help",menu=m1)
        m1.add_command(label="developed by",command=self.devlope,image=self.developer_icon,compound="left")
        m1.add_command(label="Add Songs",command=self.add_songs,image=self.add_song_icon,compound="left")
        # Menue #
        
        # Functions #
        self.directory_list = []
        self.pause=False
        self.repeat_condition=False
        self.scale_pause=False
        self.stop_download=False
        self.autoplay = False

        self.songs_to_play=[]
        # Functions #
        
###################
###############
######    
    # Songs To Cloud Button #
    def songs_location(self):
        global songs
        self.songs_list.delete(0,1000)
        self.directory_list.clear()
        songs = filedialog.askdirectory(title="Select Music Folder",initialdir=f"{self.home_directory}\\Desktop\\DownoadedSongs")
        for song in os.listdir(songs):
            name,ext=os.path.splitext(song)
            if ext==".mp3":
             self.directory_list.append(song.upper())
        for song in self.directory_list:
            self.songs_list.insert('end',song)
            self.songs_list.select_set(0)
    # Songs To Cloud Button #
###################
###############
######    
     
   # add songs to listbox #
    def devlope(self):
        messagebox.showinfo("Ahmed Ramadan Abd Elnaser","Contact Me On\nAhmed-Ramadan-Abd-Elnaser@protonmail.com")
    def add_songs(self):
        global songs
        self.songs_list.delete(0,1000)
        self.directory_list.clear()
        songs = filedialog.askdirectory(initialdir=f"{self.home_directory}\\Desktop\\DownoadedSongs",title="Select Music Folder")
        for song in os.listdir(songs):
            name,ext=os.path.splitext(song)
            if ext==".mp3":
             self.directory_list.append(song.upper())
        for song in self.directory_list:
            self.songs_list.insert('end',song)
            self.songs_list.select_set(0)
   # add songs to listbox #
###################
###############
######   
   # to cheack if you have songs or not # 
    def check_play_pause(self):
        if self.songs_list.size() >= 1:
            self.songs_to_play.append(self.songs_list.get('active'))

            length=len(self.songs_to_play)

            if len(self.songs_to_play)==1:
                self.play_song()

            elif self.songs_to_play[length-2]!=self.songs_to_play[length-1]:
                self.root.after_cancel(self.updater)
                self.play_song()

            else:
                self.pause_unpause()
   # to cheack if you have songs or not # 
###################
###############
######
   # puase song #
    def pause_unpause(self):
        if not self.pause:
            self.root.after_cancel(self.updater)
            self.play_button.config(image=self.play_icon)
            self.pause=True
            self.scale_pause=True
            self.status.config(text=f"Paused : {self.songs_list.get('active')} song: {self.songs_list.index('active')} of {self.songs_list.size()} songs")
            self.root.after_cancel(self.updater)
            pygame.mixer.music.pause()
            self.scale_pause=True
        else:
            self.pause=False
            self.scale_pause=False
            self.play_button.config(image=self.pause_icon)
            self.status.config(text=f"Playing : {self.songs_list.get('active')} song: {self.songs_list.index('active')} of {self.songs_list.size()} songs")
            self.root.after_cancel(self.updater)
            pygame.mixer.music.unpause()
            self.scale_update()
   # puase song #         
###################
###############
######
   # when changes your song #
    def play_song(self):
        self.progress_scale['value'] = 0
        self.time_elapsed_label['text'] = "00:00:00"
        song_name = self.songs_list.get('active')
        self.status.config(text=f"Playing : {song_name} Song: {self.songs_list.index('active')} of "
                                f"{self.songs_list.size()} songs")
        directory_path=os.path.join(songs)
        
        # get song lenthe #
        song_with_path = f'{directory_path}/{song_name}'
        music_data = MP3(song_with_path)
        self.music_length = int(music_data.info.length)
        self.music_duration_label['text'] = f"- {time.strftime('%M:%S', time.gmtime(self.music_length))}"
        # get song lenthe # 
        
        self.progress_scale['to'] = self.music_length
        self.play_button.config(image=self.pause_icon)
        pygame.mixer.music.load(os.path.join(song_with_path))
        pygame.mixer.music.play()
        self.scale_update()
   # when changes your song #
###################
###############
######  
   # stop song #
    def stop_song(self):
        if self.songs_list.size() >= 1:
            self.root.after_cancel(self.updater)
            self.status.config(text=f"Music Player Stoped")
            pygame.mixer.music.stop()
            self.progress_scale['value'] = 0
            self.time_elapsed_label['text'] = "00:00:00"
            self.music_duration_label['text'] = "00:00:00"
            self.play_button['image'] = self.play_icon
   # stop song #
###################
###############
######
   # when you mpoved progress scale #
    def progress_scale_moved(self,x):
        self.root.after_cancel(self.updater)
        scale_at=self.progress_scale.get()
        song_name=self.songs_list.get('active')
        directory_path=os.path.join(songs)
        pygame.mixer.music.load(f"{directory_path}/{song_name}")
        pygame.mixer.music.play(0,scale_at)
        self.scale_update()
   # when you mpoved progress scale #
###################
###############
######
   # scale progress ubdate #
    def scale_update(self):
        if self.progress_scale['value'] < self.music_length:
            self.progress_scale['value'] += 1
            self.time_elapsed_label['text']= time.strftime('%H:%M:%S', time.gmtime(self.progress_scale.get()))
            self.music_duration_label['text']= f"- {time.strftime('%H:%M:%S', time.gmtime(self.music_length-self.progress_scale.get() ))}"
            self.updater = self.root.after(1000, self.scale_update)
        elif self.repeat_condition:
            self.play_song()

        elif self.autoplay:
            self.next_song()
        else:
            self.progress_scale['value'] = 0
            self.time_elapsed_label['text'] = "00:00:00"
            self.music_duration_label['text']="00:00:00"
            self.play_button.config(image=self.play_icon)
            self.songs_to_play=[]
   # scale progress ubdate # 
###################
###############
######
   # reapet #
    def repeat_song(self):
        if self.songs_list.size() >= 1:
            if not self.repeat_condition:
                self.repeat_condition=True
                self.repeat_button.config(image=self.repeat1_icon)
            else:
                self.repeat_condition=False
                self.repeat_button.config(image=self.repeat_icon)
   # reapet #
###################
###############
######
   # auto_play #
    def auto_play_song(self):
        if self.songs_list.size() >= 1:
            if not self.autoplay:
                self.autoplay=True
                self.auto_play_button.config(image=self.auto_play_icon)
            else:
                self.autoplay=False
                self.auto_play_button.config(image=self.auto_play_not_icon)
   # auto_play #
###################
###############
######
   # shuffle #
    def shuffle_songs(self):
        if self.songs_list.size() >= 1:
            song_name=self.songs_list.get('active')

            songs_list=list(self.songs_list.get('0','end'))
            self.songs_list.delete("0","end")

            import random
            random.shuffle(songs_list)

            for i,song in enumerate(songs_list):
                self.songs_list.insert(i,song)

                if song==song_name:
                    self.songs_list.selection_set(i)
                    self.songs_list.activate(i)
            self.songs_list.update()
   # shuffle #
###################
###############
######
   # next #
    def next_song(self):
        if self.songs_list.size() >= 1:
            self.root.after_cancel(self.updater)
            song_index=self.songs_list.index('active')
            self.songs_list.selection_clear(song_index)
            self.songs_list.selection_set(song_index+1)
            self.songs_list.activate(song_index+1)
            self.check_play_pause()
   # next #
###################
###############
######
   # previos #
    def previous_song(self):
        if self.songs_list.size() >= 1:
            self.root.after_cancel(self.updater)
            song_index = self.songs_list.index('active')
            self.songs_list.selection_clear(song_index)
            self.songs_list.selection_set(song_index-1)
            self.songs_list.activate(song_index-1)
            self.check_play_pause()
   # previos # 
###################
###############
######        
   # volume #
    def volume(self, p):
        scale_at = self.vol_scale.get()/100
        pygame.mixer.music.set_volume(scale_at)
        if scale_at == 0:
            self.speaker_button.config(image=self.mute_icon)
        else:
            self.speaker_button.config(image=self.speaker_icon)
   # volume #
###################
###############
######
   # download sound #
   
    def count_down(self):
     for i in range(0,100):
         self.count=f"{i}%"
         return self.count  
   
   
    def down_sound(self):
        try:
          URLS =f'{self.get_link.get()}'
          info_dict = yt_dlp.YoutubeDL().extract_info(url=self.get_link.get(), download=False)
          info_dict.get("title")
         
          ydl_opts = {
          'format': 'bestaudio/best',
          # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
          'postprocessors': [{  # Extract audio using ffmpeg
          'key': 'FFmpegExtractAudio',
          'preferredcodec': 'mp3',
          'preferredquality': '192',
           }],
           'outtmpl':f'{self.home_directory}\\Desktop\\DownoadedSongs\\{info_dict.get("title")}',
           }  
    
          with yt_dlp.YoutubeDL(ydl_opts) as ydl:
           error_code = ydl.download(URLS)
           messagebox.showinfo("Congratulations","Successfully Downloaded...")
           self.status.config(text=f"Successfully Downloading Sound......")
           self.get_link.delete(0,1000)
        except:
          messagebox.showerror("Eroor",'An error occurred while searching for Sound Quality!\n'
                'Below might be the causes\n->Unstable internet connection\n->Using Spotify Link\n->Invalid link\n->Invalid File Name\n->closing program')
          self.status.config(text=f"Error")
          self.get_link.delete(0,1000)
    def thread(self):
        if self.get_link.get()=="":
         messagebox.showinfo("Error","Plaese Enter Music Link...")
        else:
          info_dict = yt_dlp.YoutubeDL().extract_info(url=self.get_link.get(), download=False)
          info_dict.get('title')
          self.status.configure(text=f"Please Wait We Processing Your Sound {info_dict.get('title')}.mp3......")
          self.stop_download=True
          Target=threading.Thread(target=self.down_sound)
          Target.start()
        # download sound #
###################
###############
######      
    # download Video #
    def down_video(self):
        try:
             video_url=self.get_video_link.get()
             video_info= yt_dlp.YoutubeDL().extract_info(url=video_url, download = False)
             file = f"{video_info['title']}.mp4"
             options={
             'format':'bestvideo+bestaudio',
             'format': 'WebM',
             'format':'mp4',
            #  'format':'all',
             'outtmpl':f'{self.home_directory}\\Desktop\\DownoadedSongs\\{video_info.get("title")}'
             }
             with yt_dlp.YoutubeDL(options) as ydl:
                 ydl.download([video_info['webpage_url']])
                 self.status.config(text=f"Successfully Downloading Video......")
                 messagebox.showinfo("Congratulations","Successfully Downloaded...")
                 self.get_video_link.delete(0,1000)
        except:
              messagebox.showerror("Eroor",'An error occurred while searching for Sound Quality!\n'
                'Below might be the causes\n->Unstable internet connection\n->Using Spotify Link\n->Invalid link\n->Invalid File Name\n->closing program')
              self.status.config(text=f"Error")
              self.get_video_link.delete(0,1000)
    def thread2(self):
        if self.get_video_link.get()=="":
         messagebox.showinfo("Error","Plaese Enter Video Link...")
        else:
         video_url=self.get_video_link.get()
         video_info= yt_dlp.YoutubeDL().extract_info(url=video_url, download = False)
         file = f"{video_info['title']}.mp4"
         self.status.config(text=f"Please Wait We Processing Your Video {video_info['title']}.mp4......")
         self.stop_download=True
         Target=threading.Thread(target=self.down_video)
         Target.start()
    # download Video #
###################
###############
######
    # Cancel download #
    def cancel_down(self):
        if self.stop_download :
         self.stop_download=False
         self.status.config(text=f"Downloading Stoped....")
         messagebox.showinfo("Downloading Manager","Downloading has been stopped...")
         os._exit(0)
    # Cancel download #
###################
###############
######
    # Social Icons Buttons functions #
    def youtube_down(self):
        messagebox.showinfo("Youtube","Enter Youtube Link Please... ")
    def facebook_down(self):
        messagebox.showinfo("Facebook","Enter Facebook Link Please... ")
    def instagram_down(self):
        messagebox.showinfo("Instagram","Enter Instagram Link Please... ")
    def twitter_down(self):
        messagebox.showinfo("Twitter","Enter Twitter Link Please... ")
    def dropbox_down(self):
        messagebox.showinfo("Drobpox","Enter Drobpox Link Please... ")
    def google_down(self):
        messagebox.showinfo("Google","Enter GoogleDrive Link Please... ")
    def sound_cloud_down(self):
        messagebox.showinfo("SoundCloud","Enter SoundCloud Link Please... ")
    def tik_down(self):
        messagebox.showinfo("Tiktok","Enter Tiktok Link Please... ")
    # Social Icons Buttons functions #
###################
###############
######
window = customtkinter.CTk()
window.title("Music Player")
window.wm_iconbitmap('images/music.ico')
window.geometry("770x565+510+200")
window.resizable(0,0)
window.attributes("-topmost",True)
x = MediaPlayer(window)
pygame.init()
window.mainloop()
###################
###############
######
