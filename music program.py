import pygame
from tkinter import *
from tkinter import filedialog
import os
from tkinter import messagebox
import os
from pygame import mixer
import customtkinter
import tkinter as tk



pygame.mixer.init()


root = customtkinter.CTk()
root.title("Music Player")
root.geometry("500x430+700+200")
root.resizable(0,0)
root.attributes('-topmost', True)
root.iconbitmap(f"images\\musical.ico")
img=PhotoImage(file="images\\music-intro.png")
Label(root,image=img).place(x=0,y=100)
# Frame(root,bg="black",width=1000,height=100).place(x=0,y=360)




songs=[]
current_song=""
paused=False
def load_music():
     global current_song
     global name
     global song
     root.directory=filedialog.askdirectory()# to select folder only...
     song_list.delete(0,10000)
     songs.clear()
     for song in os.listdir(root.directory):
        name,ext=os.path.splitext(song)
        if ext==".mp3":
            songs.append(song)
     for song in songs:
        song_list.insert("end",song.upper())
     song_list.selection_set(0)
     current_song=songs[song_list.curselection()[0]]
     
# TOP MENUEBAR
Menubar=Menu(root)
root.config(menu=Menubar)
organise_menue=Menu(Menubar,tearoff=False)
def develober():
    messagebox.showinfo("Ahmed Ramadan Abd Elnaser","Contact Me On\nAhmed-Ramadan-Abd-Elnaser@protonmail.com")
Menubar.add_command(label="Devoleped By",command=develober,font=('DS-DIGIB',18,"bold"))
# TOP MENUEBAR



def play():
    global current_song
    select=song_list.get("anchor")
    mixer.music.load(os.path.join(root.directory,select))
    status.configure(text=f"Playing: {select}")
    pygame.mixer.music.load(os.path.join(root.directory,select))
    pygame.mixer.music.play(-1)

    
    
     
def pause():
    global paused
    pygame.mixer.music.pause()
   

def next():
    global current_song
    song_list.selection_clear(0,END)
    song_list.select_set(songs.index(current_song)+1)
    current_song=songs[song_list.curselection()[0]]
    status.configure(text=f"Playing: {current_song.upper()}")
    pygame.mixer.music.load(os.path.join(root.directory,current_song))
    pygame.mixer.music.play(-1)
    
def prev():
   global current_song
   song_list.selection_clear(0,END)
   song_list.select_set(songs.index(current_song)-1)
   current_song=songs[song_list.curselection()[0]]
   status.configure(text=f"Playing: {current_song.upper()}")
   pygame.mixer.music.load(os.path.join(root.directory,current_song))
   pygame.mixer.music.play(-1)
    
  
   
  
   
def loop_music():
    global current_song
    pygame.mixer.music.play(-1)
def no_loop():
    pygame.mixer.music.play(loops=0)
    play()
    
    


play_music=PhotoImage(file="images\\play-buttton.png")
pause_music=PhotoImage(file="images\\pause.png")
next_music=PhotoImage(file="images\\next.png")
prev_music=PhotoImage(file="images\\previous.png")


play_button =customtkinter.CTkButton(root, text="Play",image=play_music,command=play,width=60,height=30)
stop_button = customtkinter.CTkButton(root, text="Stop", image=pause_music,command=pause,width=60)
next_button =customtkinter.CTkButton(root, text="Next", image=next_music,command=next,width=60)
prev_button = customtkinter.CTkButton(root, text="Prev",image=prev_music ,command=prev,width=60)

status=tk.Label(root,text="Playing Music: Ready",font=("calibre" ,13,"bold"),anchor="w")
status.place(rely=1,anchor="sw",relwidth=1)


location = customtkinter.CTkButton(root,text="Music Playlist", width = 110, command = load_music, corner_radius = 15)
location.place(x = 2 , y = 5)


song_list=Listbox(root,width=100,height=5,bg="white",fg="black",font=("calibre",15,"bold"))
song_list.place(x=0,y=50)


scrollbar = Scrollbar(root)
  
# Adding Scrollbar to the right
# side of root window
scrollbar.pack(side = RIGHT, fill = BOTH)

song_list.configure(yscrollcommand = scrollbar.set)
scrollbar.configure(command = song_list.yview)



button_mode=True
def loop():
    global button_mode
    if button_mode:
        loop_button.configure(image=loop_repeat)
        loop_button.configure(command=loop_music)
        button_mode=False 
    else:
        loop_button.configure(image=repeat)
        loop_button.configure(command=no_loop)
        button_mode=True
repeat=PhotoImage(file="images\\loop.png")
loop_repeat=PhotoImage(file="images\\loop-once.png")
loop_button = customtkinter.CTkButton(root,text="",image=repeat,command=loop,width=1)
loop_button.place(x=430,y=367)
play_button.place(x=140,y=368)
stop_button.place(x=235,y=368)
next_button.place(x=330,y=368)
prev_button.place(x=45,y=368)


def changeTheme(color):
    color = color.lower()
    themes_list = ["system", "dark", "light"]
    if color in themes_list:
        customtkinter.set_appearance_mode(color) 
      

themes_menu = customtkinter.CTkOptionMenu(root, values = ["System", "Dark", "Light"], width = 110, command = changeTheme, corner_radius = 15)
themes_menu.place(x = 370 , y = 5)

root.mainloop()



