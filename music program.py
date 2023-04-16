import pygame
from tkinter import *
from tkinter import filedialog
import os
from tkinter import messagebox
import os
from pygame import mixer
import customtkinter



pygame.mixer.init()


root = Tk()
root.title("Music")
root.geometry("500x430+550+200")
root.resizable(0,0)
root.attributes('-topmost', True)
root.iconbitmap(f"images\\musical.ico")
img=PhotoImage(file="images\\musical.png")
Label(root,image=img).place(x=0,y=0)
Frame(root,bg="black",width=1000,height=100).place(x=0,y=360)




songs=[]
current_song=""
paused=False
def load_music():
     global current_song
     global name
     global song
     song_list.delete(0,10000)
     root.directory=filedialog.askdirectory()# to select folder only...
     for song in os.listdir(root.directory):
        name,ext=os.path.splitext(song)
        if ext==".mp3":
            songs.append(song)
        if song not in root.directory:
            song_list.delete(0,10000)
     for song in songs:
        song_list.insert("end",song)
     song_list.selection_set(0)
     current_song=songs[song_list.curselection()[0]]
Menubar=Menu(root)
root.config(menu=Menubar)
organise_menue=Menu(Menubar,tearoff=False)
def develober():
    messagebox.showinfo("Ahmed Ramadan Abd Elnaser","Contact Me On\nAhmed-Ramadan-Abd-Elnaser@protonmail.com")
    
Menubar.add_command(label="Devoleped By",command=develober,font=('DS-DIGIB',18,"bold"))
Menubar.add_command(label="Select Music Folder",background="black",command=load_music,font=('DS-DIGIB',18,"bold"))

def delete():
    deleet=song_list.delete(0,END)
    return deleet

def select():
    select=song_list.get("anchor")
    mixer.music.load(os.path.join(root.directory,select))
    mixer.music.play()

def play():
    global current_song
    pygame.mixer.music.load(os.path.join(root.directory,current_song))
    pygame.mixer.music.play()
    
    
     
def pause():
    global paused
    pygame.mixer.music.pause()
   

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
    
    


play_music=PhotoImage(file="images\\play-buttton.png")
pause_music=PhotoImage(file="images\\pause.png")
next_music=PhotoImage(file="images\\next.png")
prev_music=PhotoImage(file="images\\previous.png")


play_button =customtkinter.CTkButton(root, text="Play",image=play_music, bg_color="black",command=select,width=60)
stop_button = customtkinter.CTkButton(root, text="Stop", image=pause_music,bg_color="black",command=pause,width=60)
next_button =customtkinter.CTkButton(root, text="Next", image=next_music,bg_color="black",command=next,width=60)
prev_button = customtkinter.CTkButton(root, text="Prev",image=prev_music ,bg_color="black",command=prev,width=60)

song_list=Listbox(root,bg="black",fg="green",width=20,height=20,font=('DS-DIGIB',10,"bold"))
song_list.place(x=0,y=7)

scrollbar = Scrollbar(root)
  
# Adding Scrollbar to the right
# side of root window
scrollbar.pack(side = RIGHT, fill = BOTH)

song_list.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = song_list.yview)



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
loop_button = customtkinter.CTkButton(root,text="",bg_color="black",image=repeat,command=loop,width=1)
loop_button.place(x=430,y=367)
play_button.place(x=140,y=368)
stop_button.place(x=235,y=368)
next_button.place(x=330,y=368)
prev_button.place(x=45,y=368)

root.mainloop()



