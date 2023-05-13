import random
def delete_song(self,command):
        if self.songs_list.size() >= 1:
            current_song = self.songs_list.index('active')
            if command == 'selected':
                if self.songs_list.size()>1:
                    if current_song == self.songs_list.size()-1:
                        self.songs_list.selection_set(self.songs_list.size()-1)
                        self.songs_list.activate(self.songs_list.size()-1)
                    else:
                        self.songs_list.selection_set(current_song+1)
                        self.songs_list.activate(current_song+1)

                self.songs_list.delete(current_song)
            else:
                self.songs_list.delete(0,self.songs_list.size()-1)

            self.root.after_cancel(self.updater)
            pygame.mixer.music.stop()

            self.progress_scale['value']=0
            self.time_elapsed_label['text']="00:00"
            self.music_duration_label['text']="00:00"
            self.play_button['image']=self.play_icon
            
            
            m2 = tk.Menu(self.menu, background="grey", tearoff=False, bd=0, activebackground="black")
            self.menu.add_cascade(label="Delete", menu=m2)

            m2.add_command(label="Delete Selected", command=lambda: self.delete_song('selected'), image=self.delete_icon, compound="left")
            m2.add_command(label="Delete All", command=lambda: self.delete_song('all'), image=self.delete_all_icon, compound="left")
            
