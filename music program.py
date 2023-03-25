import pygame
from tkinter import *
from tkinter import filedialog
import os
pygame.mixer.init()


root = Tk()
root.title("Music Player by[Ahmed Ramadan Abd Elnaser]")
root.geometry("500x430+400+100")
root.resizable(0,0)
root.attributes('-topmost', True)
root.iconbitmap("images/musical.ico")
img=PhotoImage(file="images/musical.png")
Label(root,image=img,bg="white").place(x=0,y=0)

songs=[]
current_song=""
paused=False
def load_music():
    global current_song
    root.directory=filedialog.askdirectory()# to select folder only...
    for song in os.listdir(root.directory):
        name,ext=os.path.splitext(song)
        if ext==".mp3":
            songs.append(song)
    for song in songs:
        song_list.insert("end",song)
    song_list.selection_set(0)
    current_song=songs[song_list.curselection()[0]]
Menubar=Menu(root)
root.config(menu=Menubar)
organise_menue=Menu(Menubar,tearoff=False)
Menubar.add_command(label="Select Music Folder",background="black",command=load_music)
        
def play():
    global current_song
    pygame.mixer.music.load(os.path.join(root.directory,current_song))
    pygame.mixer.music.play()
     
def pause():
    global paused
    pygame.mixer.music.pause()
    paused=True

def next():
    global current_song
    
    song_list.selection_clear(0,END)
    song_list.select_set(songs.index(current_song)+1)
    current_song=songs[song_list.curselection()[0]]
    play()
    
def prev():
   global current_song
   song_list.selection_clear(0,END)
   song_list.select_set(songs.index(current_song)-1)
   current_song=songs[song_list.curselection()[0]]
   play()
  
   
def loop_music():
    global current_song
    pygame.mixer.music.play(-1)
def no_loop():
    pygame.mixer.music.play(loops=0)
    play()

play_music=PhotoImage(file="images/play-buttton.png")
pause_music=PhotoImage(file="images/pause.png")
next_music=PhotoImage(file="images/arrowhead.png")
prev_music=PhotoImage(file="images/previous.png")



play_button = Button(root, text="Play",image=play_music, command=play,activebackground="green",width=60,bd=0,height=0)
stop_button = Button(root, text="Stop", image=pause_music,command=pause,pady=0,activebackground="red",width=60,bd=0)
next_button =Button(root, text="Next", image=next_music,command=next,pady=0,activebackground="green",width=60,bd=0)
prev_button = Button(root, text="Prev",image=prev_music ,command=prev,pady=0,activebackground="green",width=60,bd=0)
song_list=Listbox(root,bg="white",fg="black",width=82,height=10,font="times,9")
song_list.place(x=0,y=1)
button_mode=True
def loop():
    global button_mode
    if button_mode:
        loop_button.config(image=loop_repeat,activebackground="green",bd=0)
        loop_button.config(command=loop_music)
        button_mode=False    
    else:
        loop_button.config(image=repeat,activebackground="white",bd=0)
        loop_button.config(command=no_loop)
        button_mode=True
repeat=PhotoImage(file="images/repeat.png")
loop_repeat=PhotoImage(file="images/repeat-once.png")
loop_button = Button(root,image=repeat,command=loop,bd=0)
loop_button.place(x=430,y=370)
play_button.place(x=170,y=368)
stop_button.place(x=240,y=368)
next_button.place(x=320,y=368)
prev_button.place(x=90,y=368)
root.mainloop()



