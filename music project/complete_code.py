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
from downloader import downloader
import webbrowser
class MediaPlayer:
    def __init__(self, window):
        # Scale Progress Theme #
        self.style =ttk.Style()
        self.style.configure("TScale", background="#28231D")
        # Scale Progress Theme #
        
        # To Access At Any Desktop #
        self.home_directory = os.path.expanduser( '~' )
        # To Access At Any Desktop #

        # Main Window #
        self.root = window
        # Main Window #
        
        # themes photo #
        self.theme =tk.PhotoImage(file='images/theme.png')
        # themes photo #
 
        self.contact_us = Image.open('images/contact.png')
        self.contact_us_icon = self.contact_us.resize((250, 100), Image.ANTIALIAS)
        self.contact_us_icon = ImageTk.PhotoImage(self.contact_us_icon)
        
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
        self.stop_icon = self.stop_icon.resize((80, 80), Image.ANTIALIAS)
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
        
        self.about_me_icon = Image.open('images/about.png')
        self.about_me_icon = self.about_me_icon.resize((30, 30), Image.ANTIALIAS)
        self.about_me_icon = ImageTk.PhotoImage(self.about_me_icon)
        
        self.developer_icon = Image.open('images/code.png')
        self.developer_icon = self.developer_icon.resize((30, 30), Image.ANTIALIAS)
        self.developer_icon = ImageTk.PhotoImage(self.developer_icon)


        self.shuffle_icon = Image.open('images/shuffle.png')
        self.shuffle_icon = self.shuffle_icon.resize((40, 40), Image.ANTIALIAS)
        self.shuffle_icon = ImageTk.PhotoImage(self.shuffle_icon)

        self.auto_play_icon = Image.open('images/auto_play.png')
        self.auto_play_icon = self.auto_play_icon.resize((30, 30), Image.ANTIALIAS)
        self.auto_play_icon = ImageTk.PhotoImage(self.auto_play_icon)

        self.auto_play_not_icon = Image.open('images/auto_play_not.png')
        self.auto_play_not_icon = self.auto_play_not_icon.resize((30, 30), Image.ANTIALIAS)
        self.auto_play_not_icon = ImageTk.PhotoImage(self.auto_play_not_icon)
        
        self.heading_icon=tk.PhotoImage(file='images/death.png')
        self.head_image=CTkButton(self.root,text="",width=610,image=self.heading_icon,command=self.add_songs)
        self.head_image.place(x=5,y=2)
        
        
        # Downloading Icons #
        self.download_sound_icon=tk.PhotoImage(file='images/download1.png')
        self.download_video_icon=tk.PhotoImage(file='images/download1.png')
        self.download_playlist_icon=tk.PhotoImage(file='images/download1.png')
        # Downloading Icons #
        
        
        # songs list #
        self.songs_list = tk.Listbox(self.root, width=30, height=14, bg="#28231D", fg="white", relief="flat",selectbackground="grey")
        self.songs_list.place(x=773 ,y=5)
        # songs list #
        
       
        
        # Social Icons #
        self.youtube_icon=tk.PhotoImage(file='images/youtube.png')
        self.facebook_icon=tk.PhotoImage(file='images/facebook.png')
        self.instegram_icon=tk.PhotoImage(file='images/instagram.png')
        self.twitter_icon=tk.PhotoImage(file='images/twitter.png')
        self.dropbox_icon=tk.PhotoImage(file='images/dropbox.png')
        self.gdrive_icon=tk.PhotoImage(file='images/google-drive.png')
        self.soundc_icon=tk.PhotoImage(file='images/sound cloud.png')
        self.cloud_icon=tk.PhotoImage(file='images/apple.png')
        self.linkid_icon=tk.PhotoImage(file='images/linkedin.png')
        self.gif_icon=tk.PhotoImage(file='images/gif.png')
        # Social Icons #
        
        # Social Icons Buttons #
        self.youtube_button_icon=CTkButton(self.root,text="",width=3,image=self.youtube_icon,command=self.youtube_down)
        self.youtube_button_icon.place(x=5,y=70)
        self.facebook_button_icon=CTkButton(self.root,text="",width=3,image=self.facebook_icon,command=self.facebook_down)
        self.facebook_button_icon.place(x=70,y=70)
        self.instagram_button_icon=CTkButton(self.root,text="",width=3,image=self.instegram_icon,command=self.instagram_down)
        self.instagram_button_icon.place(x=135,y=70)
        self.twitter_button_icon=CTkButton(self.root,text="",width=3,image=self.twitter_icon,command=self.twitter_down)
        self.twitter_button_icon.place(x=200,y=70)
        self.dropbox_button_icon=CTkButton(self.root,text="",width=3,image=self.dropbox_icon,command=self.dropbox_down)
        self.dropbox_button_icon.place(x=265,y=70)
        self.google_button_icon=CTkButton(self.root,text="",width=3,image=self.gdrive_icon,command=self.google_down)
        self.google_button_icon.place(x=5,y=130)
        self.scloud_button_icon=CTkButton(self.root,width=3,text="",image=self.soundc_icon,command=self.sound_cloud_down)
        self.scloud_button_icon.place(x=70,y=130)
        self.icloud_button_icon=CTkButton(self.root,width=3,text="",image=self.cloud_icon,command=self.icloud_down)
        self.icloud_button_icon.place(x=135,y=130)
        self.linkidin_button_icon=CTkButton(self.root,width=3,text="",image=self.linkid_icon,command=self.linkedin_down)
        self.linkidin_button_icon.place(x=200,y=130)
        self.giphy_button_icon=CTkButton(self.root,width=3,text="",image=self.gif_icon,command=self.gif_down)
        self.giphy_button_icon.place(x=265,y=130)
        # Social Icons Buttons #
        
        # Stop Icons #
        self.stop_download_icon=tk.PhotoImage(file='images/loss.png')
        self.Stop_icon=CTkButton(self.root,text="",width=0,image=self.stop_download_icon,command=self.cancel_down)
        self.Stop_icon.place(x=490,y=478)
        # Stop Icons #
        
        # Header Text #
        self.header_lable=CTkLabel(self.root,text="Music Player\nWith\nFull Downloader",font=("arial",30,"bold"))
        self.header_lable.place(x=349,y=65)
        # Header Text #
        
        # contact us #
        self.contact_button=CTkButton(self.root,text="",image=self.contact_us_icon,command=self.develop_contact_us)
        self.contact_button.place(x=550,y=478)
        # contact us #
        
        
        ########################## inputs and download buttons ###########################
        
        # Sound inputs and bUttons #
        self.get_link=customtkinter.CTkEntry(self.root,width=450,font=("arial",15))
        self.get_link.place(x=160,y=205)
        
        self.link_lable=CTkLabel(self.root,text="Sound Link",font=("arial",28,"bold"))
        self.link_lable.place(x=5,y=200)
        
        self.file_download_sound_button=CTkButton(self.root,text="",font=("arial",10),height=40,image=self.download_sound_icon,command=self.thread)
        self.file_download_sound_button.place(x=620,y=200)
        # Sound inputs and bUttons #
        
        
        # Video inputs and buttons #
        self.get_video_link=customtkinter.CTkEntry(self.root,width=450,font=("arial",15))
        self.get_video_link.place(x=160,y=250)
        
        self.file_download_video_button=CTkButton(self.root,text="",font=("arial",10),height=40,image=self.download_video_icon,command=self.thread2)
        self.file_download_video_button.place(x=620,y=245)
        
        self.file_name_lable=CTkLabel(self.root,text="Video  Link",font=("arial",28,"bold"))
        self.file_name_lable.place(x=5,y=245)
        # # Video inputs and buttons #
        
        
        # # playlist inputs and buttons #
        self.get_playlist_link=customtkinter.CTkEntry(self.root,width=450,font=("arial",15))
        self.get_playlist_link.place(x=160,y=295)
        
        self.playlist_lable=CTkLabel(self.root,text="PlaylistLink",font=("arial",28,"bold"))
        self.playlist_lable.place(x=5,y=290)
        
        self.file_download_playlist_button=CTkButton(self.root,text="",font=("arial",10),height=40,image=self.download_playlist_icon,command=self.thread3)
        self.file_download_playlist_button.place(x=620,y=290)
        
        self.combopox_lable=CTkLabel(self.root,text="PlaylistType:",font=("arial",28,"bold"))
        self.combopox_lable.place(x=5,y=340)
        self.combopox=CTkComboBox(self.root,values=["mp3","mp4"],state="normal",font=("arial",15),width=100)
        self.combopox.place(x=180,y=346)
        self.combopox.set("mp3")

        ########################## inputs and download buttons ###########################
        
        self.time_elapsed_label = CTkLabel(self.root,text="00:00:00",
                                           height=3,font=("arial",15))
        self.time_elapsed_label.place(x=10,y=453)

        self.music_duration_label =CTkLabel(self.root,text="00:00:00"
                                            ,height=3,font=("arial",15))
        self.music_duration_label.place(x=400,y=453)

        self.progress_scale = ttk.Scale(self.root,orient="horizontal",from_=0,length=380,
                                        command=self.progress_scale_moved,cursor='hand2')
        self.progress_scale.place(x=100,y=565)

        self.play_button = CTkButton(self.root,image=self.play_icon,width=3,text="",command=self.check_play_pause)
        self.play_button.place(x=150,y=478)

        self.next_button = CTkButton(self.root,width=3,text="", image=self.next_icon, command=self.next_song, cursor='hand2')
        self.next_button.place(x=323, y=478)

        self.previous_button = CTkButton(self.root,width=3,text="", image=self.previous_icon, command=self.previous_song, cursor='hand2')
        self.previous_button.place(x=73, y=478)

        self.stop_button = CTkButton(self.root,width=3,text="", image=self.stop_icon, command=self.stop_song, cursor='hand2')
        self.stop_button.place(x=236, y=478)

        self.shuffle_button = CTkButton(self.root,width=3,text="", image=self.shuffle_icon, command=self.shuffle_songs, cursor='hand2')
        self.shuffle_button.place(x=10, y=524)

        self.speaker_button = CTkButton(self.root,width=3,text="", image=self.speaker_icon, command=self.silent, cursor='hand2')
        self.speaker_button.place(x=400, y=478)

        self.repeat_button = CTkButton(self.root,width=3,text="", image=self.repeat_icon, command=self.repeat_song, cursor='hand2')
        self.repeat_button.place(x=10, y=478)

        self.auto_play_button = CTkButton(self.root,width=0,text="", image=self.auto_play_not_icon, command=self.auto_play_song, cursor='hand2')
        self.auto_play_button.place(x=445, y=478)
    

        self.vol_scale = ttk.Scale(self.root, from_=0,to=100,orient="horizontal",style="TScale",command=self.volume,cursor="hand2")
        self.vol_scale.place(x=505,y=650)

        self.status = tk.Label(self.root,text="Ready To Run : ---------- Song : 0 of 0",width=0,fg="black",anchor="w",background="white",
                               font="arial 12 bold",bd=1,relief="ridge")
        self.status.place(x=0,y=710,relwidth=1)

        self.menu = tk.Menu(self.root)
        self.root.configure(menu=self.menu)
        
        # Top Menue #
        m1 = tk.Menu(self.menu,background="white",tearoff=True,bd=0,activebackground="black")
        self.menu.add_cascade(label="Help",menu=m1)
        m1.add_command(label="developed by",command=self.devlope,image=self.developer_icon,compound="left")
        m1.add_command(label="Add Songs",command=self.add_songs,image=self.add_song_icon,compound="left")
        m1.add_command(label="About Me",command=self.about_me,image=self.about_me_icon,compound="left")
        m2 = tk.Menu(self.menu,background="white",tearoff=True,bd=0,activebackground="black")
        self.menu.add_cascade(label="Theme",menu=m2)
        m2.add_command(label="Light",command=self.changeTheme3,image=self.theme,compound="left")
        m2.add_command(label="System",command=self.changeTheme2,image=self.theme,compound="left")
        m2.add_command(label="Dark",command=self.changeTheme1,image=self.theme,compound="left")
        self.menu.add_cascade(label="Exit",command=self.destroy)
        # Top Menue #
        
        # Functions #
        self.directory_list = []
        self.pause=False
        self.repeat_condition=False
        self.scale_pause=False
        self.stop_download=False
        self.autoplay = False
        self.silentt=False
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
        songs = filedialog.askdirectory(title="Select Music Folder",initialdir=f"{self.home_directory}\\Desktop")
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
        songs = filedialog.askdirectory(initialdir=f"{self.home_directory}\\Desktop",title="Select Music Folder")
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
            self.play_button.configure(image=self.play_icon)
            self.pause=True
            # self.scale_pause=True 
            self.status.config(text=f"Paused : {self.songs_list.get('active')}                                                    song: {self.songs_list.index('active')} of {self.songs_list.size()} songs")
            self.root.after_cancel(self.updater)
            pygame.mixer.music.pause()
            # self.scale_pause=True
        else:
            self.pause=False
            # self.scale_pause=False
            self.play_button.configure(image=self.pause_icon)
            self.status.config(text=f"Playing : {self.songs_list.get('active')}                                                   song: {self.songs_list.index('active')} of {self.songs_list.size()} songs")
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
        self.time_elapsed_label.configure(text="00:00:00") 
        song_name = self.songs_list.get('active')
        self.status.config(text=f"Playing : {song_name}                                                                          Song: {self.songs_list.index('active')} of "
                                f"{self.songs_list.size()} songs")
        directory_path=os.path.join(songs)
        
        # get song lenthe #
        song_with_path = f'{directory_path}/{song_name}'
        music_data = MP3(song_with_path)
        self.music_length = int(music_data.info.length)
        self.music_duration_label.configure(text={time.strftime('%M:%S', time.gmtime(self.music_length))})
        # get song lenthe # 
        
        self.progress_scale['to'] = self.music_length
        self.play_button.configure(image=self.pause_icon)
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
            self.time_elapsed_label.configure(text="00:00:00") 
            self.music_duration_label.configure(text="00:00:00") 
            self.play_button['image'] = self.play_icon
   # stop song #
###################
###############
######
   # when you mpoved progress scale #
    def progress_scale_moved(self,d):
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
            self.time_elapsed_label.configure(text=time.strftime('%H:%M:%S', time.gmtime(self.progress_scale.get())))
            self.music_duration_label.configure(text=f"- {time.strftime('%H:%M:%S', time.gmtime(self.music_length-self.progress_scale.get() ))}")
            self.updater = self.root.after(1000, self.scale_update)
            
            
        elif self.repeat_condition:
            self.play_song()
            
            

        elif self.autoplay:
            self.next_song()
            
            
        else:
            self.progress_scale['value'] = 0
            self.time_elapsed_label.configure(text="00:00:00") 
            self.music_duration_label.configure(text="00:00:00") 
            self.play_button.configure(image=self.play_icon)
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
                self.repeat_button.configure(image=self.repeat1_icon)
            else:
                self.repeat_condition=False
                self.repeat_button.configure(image=self.repeat_icon)
   # reapet #
###################
###############
######
   # auto_play #
    def auto_play_song(self):
        if self.songs_list.size() >= 1:
            if not self.autoplay:
                self.autoplay=True
                self.auto_play_button.configure(image=self.auto_play_icon)
            else:
                self.autoplay=False
                self.auto_play_button.configure(image=self.auto_play_not_icon)
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
    def volume(self,d):
        scale_at = self.vol_scale.get()/100
        pygame.mixer.music.set_volume(scale_at)
        if scale_at == 0:
            self.speaker_button.configure(image=self.mute_icon)
        else:
            self.speaker_button.configure(image=self.speaker_icon)
    def silent(self):
        if not self.silentt:
         self.vol_scale.set(0)
         self.speaker_button.configure(image=self.mute_icon)
         self.silentt=True
        else:
         self.vol_scale.set(1000)
         self.speaker_button.configure(image=self.speaker_icon)
         self.silentt=False
   # volume #
###################
###############
######
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
        #   'audio-multistreams':True,
          'preferredcodec': 'mp3',
          'preferredquality': '192',
           }],
           'outtmpl':f'{self.home_directory}//Desktop//Songs//{"%(title)s.%(ext)s"}',
           }  
    
          with yt_dlp.YoutubeDL(ydl_opts) as ydl:
           error_code = ydl.download(URLS)
           messagebox.showinfo("Congratulations","Successfully Downloaded...")
           self.status.config(text=f"Successfully Downloading Sound {info_dict.get('title')}......")
           self.file_download_sound_button.configure(state="normal")
           self.get_link.delete(0,1000)
        except:
          messagebox.showerror("Eroor",'An error occurred while searching for Sound Quality!\n'
                'Below might be the causes\n->Unstable internet connection\n->Using Spotify Link\n->Invalid link\n->Invalid File Name\n->closing program')
          self.status.config(text=f"Error")
          self.get_link.delete(0,1000)
          self.file_download_sound_button.configure(state="normal")
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
          self.file_download_sound_button.configure(state="disabled")
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
             'format':f'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            #  'video-multistreams ':True,
             '--rm-cache-dir': True,
             'html5': '1',
             'c': 'TVHTML5',
             'cver': '6.20180913',
             'outtmpl':f'{self.home_directory}//Desktop//Videos//{"%(title)s.%(ext)s"}'
             }
             with yt_dlp.YoutubeDL(options) as ydl:
                 ydl.download([video_info['webpage_url']])
                 self.status.config(text=f"Successfully Downloading Video {video_info.get('title')}......")
                 messagebox.showinfo("Congratulations","Successfully Downloaded...")
                 self.get_video_link.delete(0,1000)
                 self.file_download_video_button.configure(state="normal")
        except:
              messagebox.showerror("Eroor",'An error occurred while searching for Video Quality!\n'
                'Below might be the causes\n->Unstable internet connection\n->Using Spotify Link\n->Invalid link\n->closing program')
              self.status.config(text=f"Error")
              self.get_video_link.delete(0,1000)
              self.file_download_video_button.configure(state="normal")
              
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
         self.file_download_video_button.configure(state="disabled")
    # download Video #
###################
###############
######
   # download Playlist #
    def down_playlist(self):
        playlist_info = yt_dlp.YoutubeDL().extract_info(f'{self.get_playlist_link.get()}', download=False)
        playlist_title = playlist_info.get('title', None)
        try:
           if self.combopox.get()=="mp4":
            playlist_opts = {
           'format': f'{"bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"}',
           'outtmpl': f'{self.home_directory}//Desktop//{playlist_title}//{"%(title)s.%(ext)s"}',
           'playlist': True,
           'video-multistreams ':True,
            }
           else:
            playlist_opts = {
           'format': f'{"bestaudio/best[ext=mp3]"}',
           'outtmpl': f'{self.home_directory}//Desktop//{playlist_title}//{"%(title)s"}.mp3',
           'playlist': True,
           'audio-multistreams ':True,
            }
               

           with yt_dlp.YoutubeDL(playlist_opts) as ydl:
            playlist_info = yt_dlp.YoutubeDL().extract_info(f'{self.get_playlist_link.get()}', download=False)
            playlist_title = playlist_info.get('title', None)        
            ydl.download([f'{self.get_playlist_link.get()}']) 
            self.status.config(text=f"Successfully Downloading {playlist_title} ......")
            messagebox.showinfo("Congratulations","Successfully Downloaded Playlist...")
            self.file_download_playlist_button.configure(state="normal")
            self.get_playlist_link.delete(0,1000)
        except:
             messagebox.showerror("Eroor",'An error occurred while searching for Playlist Quality!\n'
                'Below might be the causes\n->Unstable internet connection\n->Invalid link\n->closing program')
             self.status.config(text=f"Error")
             self.get_playlist_link.delete(0,1000)
             self.file_download_playlist_button.configure(state="normal")
            
    def thread3(self):
        if self.get_playlist_link.get()=="":
         messagebox.showinfo("Error","Plaese Enter Playlist Link...")
        elif self.combopox.get()=="":
         messagebox.showinfo("Error","Please Choose Your Playlist Format.....")
        else:
         Playlist_url=self.get_playlist_link.get()
         video_info= yt_dlp.YoutubeDL().extract_info(url=Playlist_url, download = False)
         self.status.config(text=f"Please Wait We Processing Your Playlist [{video_info['title']}]......")
         self.stop_download=True
         Target=threading.Thread(target=self.down_playlist)
         Target.start()
         self.file_download_playlist_button.configure(state="disabled")
   # download Playlist #
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
        webbrowser.open_new("https://www.youtube.com/")
        # messagebox.showinfo("Youtube","Enter Youtube Link Please... ")
    def facebook_down(self):
        webbrowser.open_new("https://ar-ar.facebook.com/")
        # messagebox.showinfo("Facebook","Enter Facebook Link Please... ")
    def instagram_down(self):
        webbrowser.open_new("https://www.instagram.com/")
        # messagebox.showinfo("Instagram","Enter Instagram Link Please... ")
    def twitter_down(self):
        webbrowser.open_new("https://twitter.com/")
        # messagebox.showinfo("Twitter","Enter Twitter Link Please... ")
    def dropbox_down(self):
        webbrowser.open_new("https://www.dropbox.com/official-teams-page?&_tk=paid_sem_goog_biz_b&_camp=2043311742&_kw=dropbox%7cp&_ad=650036337330%7c%7cc&gclid=CjwKCAjw9pGjBhB-EiwAa5jl3BUW9ZBrKewiVglsu8oxSECTGVWX1RrVkcozIrcQLv0GVnCAIYBwXxoCDuQQAvD_BwE&gclsrc=aw.ds")
        # messagebox.showinfo("Drobpox","Enter Drobpox Link Please... ")
    def google_down(self):
        webbrowser.open_new("https://drive.google.com/")
        # messagebox.showinfo("Google","Enter GoogleDrive Link Please... ")
    def sound_cloud_down(self):
        webbrowser.open_new("https://soundcloud.com/")
        # messagebox.showinfo("SoundCloud","Enter SoundCloud Link Please... ")
    def icloud_down(self):
        webbrowser.open_new("https://www.icloud.com/")
        # messagebox.showinfo("Tiktok","Enter Icloud Link Please... ")
    def linkedin_down(self):
        webbrowser.open_new("https://www.linkedin.com/")
        # messagebox.showinfo("Tiktok","Enter Linkedin Link Please... ")
    def gif_down(self):
        webbrowser.open_new("https://giphy.com/")
        # messagebox.showinfo("Tiktok","Enter Gif Link Please... ")
    def develop_contact_us(self):
        webbrowser.open_new("https://mail.proton.me/u/0/inbox")
    def about_me(self):
        webbrowser.open_new("https://github.com/KILLER-RAMADAN")
    # Social Icons Buttons functions #
###################
###############
######
# change themes #
    def changeTheme1(self):
         customtkinter.set_appearance_mode("dark")
         self.style.configure("TScale", background="#28231D")
         self.songs_list.configure(bg="#28231D")
         self.songs_list.configure(fg="white")
    def changeTheme2(self):
         customtkinter.set_appearance_mode("system")
         self.style.configure("TScale", background="#28231D")
         self.songs_list.configure(bg="#28231D")
         self.songs_list.configure(fg="white")
    def changeTheme3(self):
         customtkinter.set_appearance_mode("light")
         self.style.configure("TScale", background="#ebebeb")
         self.songs_list.configure(bg="#ebebeb")
         self.songs_list.configure(fg="black")
# change themes # 
###################
###############
######
    # Exit #
    def destroy(self):
        window.quit()
    # Exit #
###################
###############
######
window = customtkinter.CTk()
window.title("Music Player & Downloader")
window.wm_iconbitmap('images/music.ico')
window.geometry("770x585+510+200")
window.resizable(0,0)
customtkinter.set_appearance_mode("dark") 
window.attributes("-topmost",True)
x = MediaPlayer(window)
pygame.init()
window.mainloop()
###################
###############
######
