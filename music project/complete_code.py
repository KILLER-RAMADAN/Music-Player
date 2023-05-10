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
class MediaPlayer:
    def __init__(self, window):

        style = ttk.Style()
        style.theme_use("breeze")

        background = "grey"

        style.configure("TScale",background = background)

        self.root = window

        self.root.configure(bg="black")
        
        self.back =tk.PhotoImage(file='images/music-intro.png')
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

        self.multiple_song_icon = Image.open('images/song2.png')
        self.multiple_song_icon = self.multiple_song_icon.resize((30, 30), Image.ANTIALIAS)
        self.multiple_song_icon = ImageTk.PhotoImage(self.multiple_song_icon)

        self.shuffle_icon = Image.open('images/shuffle.png')
        self.shuffle_icon = self.shuffle_icon.resize((40, 40), Image.ANTIALIAS)
        self.shuffle_icon = ImageTk.PhotoImage(self.shuffle_icon)

        self.auto_play_icon = Image.open('images/auto_play.png')
        self.auto_play_icon = self.auto_play_icon.resize((40, 50), Image.ANTIALIAS)
        self.auto_play_icon = ImageTk.PhotoImage(self.auto_play_icon)

        self.auto_play_not_icon = Image.open('images/auto_play_not.png')
        self.auto_play_not_icon = self.auto_play_not_icon.resize((40, 40), Image.ANTIALIAS)
        self.auto_play_not_icon = ImageTk.PhotoImage(self.auto_play_not_icon)
        
        self.heading_icon=tk.PhotoImage(file='images/house.png')
        self.head_image=tk.Button(self.root,bg="white",image=self.heading_icon,bd=0,command=self.add_songs)
        self.head_image.place(x=5,y=2)

        tk.Label(self.root, text="",background=background,height=7,width=120).place(x=0,y=404)

        self.songs_list = tk.Listbox(self.root, width=60, height=5, bg="white", fg="black", relief="flat",
                                     selectbackground="grey")
        self.songs_list.place(x=100 ,y=4)

        self.time_elapsed_label = tk.Label(self.root,text="00:00", fg="black",background=background,
                                           activebackground=background,padx=5)
        self.time_elapsed_label.place(x=10,y=404)

        self.music_duration_label = tk.Label(self.root,text="00:00",fg="black",background=background,
                                             activebackground=background,padx=15)
        self.music_duration_label.place(x=460,y=404)

        self.progress_scale = ttk.Scale(self.root,orient="horizontal",style='TScale',from_=0,length=380,
                                        command=self.progress_scale_moved,cursor='hand2')
        self.progress_scale.place(x=80,y=404)

        self.play_button = tk.Button(self.root,image=self.play_icon,command=self.check_play_pause,cursor='hand2',bd=0,
                                     background=background,activebackground=background)
        self.play_button.place(x=150,y=430)

        self.next_button = tk.Button(self.root, image=self.next_icon, command=self.next_song, cursor='hand2', bd=0,
                                     background=background, activebackground=background)
        self.next_button.place(x=328, y=435)

        self.previous_button = tk.Button(self.root, image=self.previous_icon, command=self.previous_song, cursor='hand2', bd=0,
                                     background=background, activebackground=background)
        self.previous_button.place(x=73, y=435)

        self.stop_button = tk.Button(self.root, image=self.stop_icon, command=self.stop_song, cursor='hand2', bd=0,
                                     background=background, activebackground=background)
        self.stop_button.place(x=236, y=425)

        self.shuffle_button = tk.Button(self.root, image=self.shuffle_icon, command=self.shuffle_songs, cursor='hand2', bd=0,
                                     background=background, activebackground=background)
        self.shuffle_button.place(x=10, y=425)

        self.speaker_button = tk.Button(self.root, image=self.speaker_icon, command="command", cursor='hand2', bd=0,
                                     background=background, activebackground=background)
        self.speaker_button.place(x=390, y=420)

        self.repeat_button = tk.Button(self.root, image=self.repeat_icon, command=self.repeat_song, cursor='hand2', bd=0,
                                     background=background, activebackground=background)
        self.repeat_button.place(x=10, y=470)

        self.auto_play_button = tk.Button(self.root, image=self.auto_play_not_icon, command=self.auto_play_song, cursor='hand2', bd=0,
                                     background=background, activebackground=background)
        self.auto_play_button.place(x=420, y=453)

        self.vol_scale = ttk.Scale(self.root, from_=0,to=100,orient="horizontal",command=self.volume,cursor="hand2")
        self.vol_scale.place(x=420,y=425)

        self.status = tk.Label(self.root,text="Ready To Run : ---------- Song : 0 of 0",width=0,fg="black",anchor="w",background="cyan",
                               font="arial 9 bold",bd=5,relief="ridge")
        self.status.place(x=0,y=520,relwidth=1)

        self.menu = tk.Menu(self.root)
        self.root.configure(menu=self.menu)
        
        # add songs #
        m1 = tk.Menu(self.menu,background="grey",tearoff=False,bd=0,activebackground="black")
        self.menu.add_cascade(label="Add Playlist",menu=m1)
        m1.add_command(label="developed by",command=self.devlope,image=self.developer_icon,compound="left")
        m1.add_command(label="Add Songs",command=self.add_songs,image=self.add_song_icon,compound="left")
        # add songs #
        
        self.directory_list = []
        self.pause=False
        self.repeat_condition=False
        self.scale_pause=False

        self.autoplay = False

        self.songs_to_play=[]
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
        songs = filedialog.askdirectory(title="Select Music Folder")
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

            elif self.songs_to_play[length-1]!=self.songs_to_play[length-2]:
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
            self.status.config(text=f"Paused : {self.songs_list.get('active')} {self.songs_list.index('active')} of {self.songs_list.size()}")
            pygame.mixer.music.pause()
            self.scale_pause=True
        else:
            self.pause=False
            self.play_button.config(image=self.pause_icon)
            self.status.config(text=f"Playing : {self.songs_list.get('active')} {self.songs_list.index('active')} of {self.songs_list.size()}")
            pygame.mixer.music.unpause()
            self.scale_update()
   # puase song #         
###################
###############
######
   # when changes your song #
    def play_song(self):
        self.progress_scale['value'] = 0
        self.time_elapsed_label['text'] = "00:00"
        song_name = self.songs_list.get('active')
        self.status.config(text=f"Playing : {song_name} Song : {self.songs_list.index('active')} of "
                                f"{self.songs_list.size()}")
        directory_path=os.path.join(songs)
        
        # get song lenthe #
        song_with_path = f'{directory_path}/{song_name}'
        music_data = MP3(song_with_path)
        self.music_length = int(music_data.info.length)
        self.music_duration_label['text'] = time.strftime('%M:%S', time.gmtime(self.music_length))
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
            self.time_elapsed_label['text'] = "00:00"
            self.music_duration_label['text'] = "00:00"
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
            self.time_elapsed_label['text'] = time.strftime('%M:%S', time.gmtime(self.progress_scale.get()))
            self.updater = self.root.after(1000, self.scale_update)
        elif self.repeat_condition:
            self.play_song()

        elif self.autoplay:
            self.next_song()
        else:
            self.progress_scale['value'] = 0
            self.time_elapsed_label['text'] = "00:00"
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
if __name__ == '__main__':
    window = themed_tk.ThemedTk()
    window.title("Music Player")
    window.wm_iconbitmap('images/music.ico')
    window.geometry("770x570+400+150")
    window.resizable(0,0)
    window.attributes("-topmost",True)
    x = MediaPlayer(window)
    pygame.init()
    window.mainloop()
