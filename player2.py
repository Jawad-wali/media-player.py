import tkinter as tk #Python's standard GUI library
from tkinter import filedialog # helps open a file picker dialog so the user can select audio files.
import pygame  #A multimedia library used here for audio playback.

# Initialize pygame mixer
pygame.mixer.init()  #Initializes the Pygame mixer, which handles loading and playing sound files.

# Create the main window
MP3= tk.Tk() 
MP3.title("Jawad Play - Audio Player") #Creates the main application window named mp3
MP3.geometry("500x350")        #Sets  size.

# Set default volume
current_volume = 0.5   # Set initial volume to 50%
pygame.mixer.music.set_volume(current_volume) # Apply the volume to pygame's mixer

# Load and play function
def load_and_play():  
    filepath = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
    if filepath: # Open file dialog to select an audio file
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play()                    # Load and play the selected audio file

# Pause function
def pause():
    pygame.mixer.music.pause()  # ⏸️  Pause audio playback

# Resume function
def resume():
    pygame.mixer.music.unpause()

# Stop function
def stop():    # ⏹️ Stop audio playback
    pygame.mixer.music.stop()

# Volume Up function
def volume_up():
    global current_volume  # Use global to modify the volume variable
    if current_volume < 1.0: # 🔊 Increase volume by 10%
        current_volume = min(current_volume + 0.01, 1.0)
        pygame.mixer.music.set_volume(current_volume)  # Apply new volume
        volume_label.config(text=f"Volume: {int(current_volume * 100)}%")  # Update label

# Volume Down function
def volume_down():
    global current_volume    # Use global to modify the volume variable
    if current_volume > 0.0:
        current_volume = max(current_volume - 0.01, 0.0)
        pygame.mixer.music.set_volume(current_volume)
        volume_label.config(text=f"Volume: {int(current_volume * 100)}%")

# Buttons    Create and place control buttons on the window
tk.Button(MP3, text="Load & Play", command=load_and_play).pack(pady=10)
tk.Button(MP3, text="Pause", command=pause).pack(pady=5)      
tk.Button(MP3, text="Resume", command=resume).pack(pady=5)
tk.Button(MP3, text="Stop", command=stop).pack(pady=5)
tk.Button(MP3, text="Volume Up", command=volume_up).pack(pady=5)
tk.Button(MP3, text="Volume Down", command=volume_down).pack(pady=5)

# Volume label  Create a label to show the current volume percentage
volume_label = tk.Label(MP3, text=f"Volume: {int(current_volume * 100)}%")
volume_label.pack(pady=10) 

# Run the GUI loop
MP3.mainloop()    # Run the Tkinter event loop to keep the window open
 