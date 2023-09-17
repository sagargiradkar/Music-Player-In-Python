import tkinter as tk
from tkinter import filedialog
import pygame
import os

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x200")

        # Initialize Pygame mixer
        pygame.mixer.init()

        # Create playlist
        self.playlist = []

        # Create current track variable
        self.current_track = tk.StringVar()
        self.status = tk.StringVar()

        # Create track label
        self.track_label = tk.Label(root, textvariable=self.current_track, font=("Helvetica", 12))
        self.track_label.pack(pady=10)

        # Create buttons
        self.play_button = tk.Button(root, text="Play", command=self.play)
        self.pause_button = tk.Button(root, text="Pause", command=self.pause)
        self.stop_button = tk.Button(root, text="Stop", command=self.stop)
        self.add_button = tk.Button(root, text="Add Song", command=self.add_song)
        self.play_button.pack()
        self.pause_button.pack()
        self.stop_button.pack()
        self.add_button.pack()
        
        # Create status label
        self.status_label = tk.Label(root, textvariable=self.status, font=("Helvetica", 10))
        self.status_label.pack(pady=10)

    def add_song(self):
        song = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
        if song:
            self.playlist.append(song)
            self.current_track.set(os.path.basename(song))
            self.status.set("Track added to playlist")

    def play(self):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[0])
            pygame.mixer.music.play()
            self.status.set("Playing a Music")

    def pause(self):
        pygame.mixer.music.pause()
        self.status.set("Paused a Music")

    def stop(self):
        pygame.mixer.music.stop()
        self.status.set("Stopped a Music")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('800x800')
    app = MusicPlayer(root)
    root.mainloop()
