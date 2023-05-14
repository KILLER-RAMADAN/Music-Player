import yt_dlp

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
           self.file_download_sound_button.config(state="normal")
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
          self.file_download_sound_button.config(state="disabled")
        # download sound #