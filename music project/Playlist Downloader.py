import yt_dlp

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
           'preferredcodec': 'mp3',
           'preferredquality': '192',
           'playlist': True,
        #    'video-multistreams ':True,
            }
               

           with yt_dlp.YoutubeDL(playlist_opts) as ydl:
            playlist_info = yt_dlp.YoutubeDL().extract_info(f'{self.get_playlist_link.get()}', download=False)
            playlist_title = playlist_info.get('title', None)
            # self.status.config(text=f"Please Wait We Processing Your List......")
            ydl.download([f'{self.get_playlist_link.get()}']) 
            self.status.config(text=f"Successfully Downloading {playlist_title} ......")
            messagebox.showinfo("Congratulations","Successfully Downloaded Playlist...")
            self.file_download_playlist_button.config(state="normal")
        except:
             messagebox.showerror("Eroor",'An error occurred while searching for Playlist Quality!\n'
                'Below might be the causes\n->Unstable internet connection\n->Invalid link\n->closing program')
             self.status.config(text=f"Error")
             self.get_playlist_link.delete(0,1000)
            
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
         self.file_download_playlist_button.config(state="disabled")
   # download Playlist #