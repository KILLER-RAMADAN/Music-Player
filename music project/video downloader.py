import yt_dlp



    # download Video #
    def down_video(self):
        try:
             video_url=self.get_video_link.get()
             video_info= yt_dlp.YoutubeDL().extract_info(url=video_url, download = False)
             file = f"{video_info['title']}.mp4"
             options={
             'format':f'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
             'video-multistreams ':True,
             'outtmpl':f'{self.home_directory}//Desktop//Videos//{"%(title)s.%(ext)s"}'
             }
             with yt_dlp.YoutubeDL(options) as ydl:
                 ydl.download([video_info['webpage_url']])
                 self.status.config(text=f"Successfully Downloading Video {video_info.get('title')}......")
                 messagebox.showinfo("Congratulations","Successfully Downloaded...")
                 self.get_video_link.delete(0,1000)
                 self.file_download_video_button.config(state="normal")
        except:
              messagebox.showerror("Eroor",'An error occurred while searching for Video Quality!\n'
                'Below might be the causes\n->Unstable internet connection\n->Using Spotify Link\n->Invalid link\n->closing program')
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
         self.file_download_video_button.config(state="disabled")
    # download Video #