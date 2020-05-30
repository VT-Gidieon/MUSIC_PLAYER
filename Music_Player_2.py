from tkinter import *
import pygame
import os

class MusicPlayer:

  def __init__(self,root):
    self.root = root
    self.root.title("Music Player")
    self.root.geometry("1000x200+200+200")

    pygame.init()
    pygame.mixer.init()
    self.track = StringVar()
    self.status = StringVar()

    track_frame = LabelFrame(self.root,text="Song Track",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
    track_frame.place(x=0,y=0,width=600,height=100)

    song_track = Label(track_frame,textvariable=self.track,width=20,font=("times new roman",24,"bold"),bg="grey",fg="gold")
    song_track.grid(row=0,column=0,padx=10,pady=5)

    track_status = Label(track_frame,textvariable=self.status,font=("times new roman",24,"bold"),bg="grey",fg="gold")
    track_status.grid(row=0,column=1,padx=10,pady=5)

    button_frame = LabelFrame(self.root,text="Control Panel",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
    button_frame.place(x=0,y=100,width=600,height=100)

    play_btn1 = Button(button_frame,text="PLAY",command=self.play_song,width=6,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold")
    play_btn1.grid(row=0,column=0,padx=10,pady=5)
    play_btn2 = Button(button_frame,text="PAUSE",command=self.pause_song,width=8,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold")
    play_btn2.grid(row=0,column=1,padx=10,pady=5)
    play_btn3 = Button(button_frame,text="UNPAUSE",command=self.unpause_song,width=10,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold")
    play_btn3.grid(row=0,column=2,padx=10,pady=5)
    play_btn4 = Button(button_frame,text="STOP",command=self.stop_song,width=6,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold")
    play_btn4.grid(row=0,column=3,padx=10,pady=5)

    songs_frame = LabelFrame(self.root,text="Song Playlist",font=("times new roman",15,"bold"),bg="grey",fg="white",bd=5,relief=GROOVE)
    songs_frame.place(x=600,y=0,width=400,height=200)

    scrol_y = Scrollbar(songs_frame,orient=VERTICAL)

    self.playlist = Listbox(songs_frame,yscrollcommand=scrol_y.set,selectbackground="gold",selectmode=SINGLE,font=("times new roman",12,"bold"),bg="silver",fg="dark blue",bd=5,relief=GROOVE)

    scrol_y.pack(side=RIGHT,fill=Y)
    scrol_y.config(command=self.playlist.yview)
    self.playlist.pack(fill=BOTH)

    os.chdir("/Users/Lenovo/Desktop/g music")
    songtracks = os.listdir()

    for track in songtracks:
      self.playlist.insert(END,track)

  def play_song(self):
    self.track.set(self.playlist.get(ACTIVE))
    self.status.set("-Playing")
    pygame.mixer.music.load(self.playlist.get(ACTIVE))
    pygame.mixer.music.play()
  def stop_song(self):
    self.status.set("-Stopped")
    pygame.mixer.music.stop()
  def pause_song(self):
    self.status.set("-Paused")
    pygame.mixer.music.pause()
  def unpause_song(self):
    self.status.set("-Playing")
    pygame.mixer.music.unpause()

root = Tk()
MusicPlayer(root)
root.mainloop()