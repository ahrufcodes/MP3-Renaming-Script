from mutagen.easyid3 import EasyID3
import os

# Navigating to the folder containing the audio files
folder_path = r"C:\Users\ahmad\Desktop\Ayub\MUHAMMAD"

# Iterating over all the audio files in the folder
for file_name in os.listdir(folder_path):
    
    # Just chekcking if all the files are in MP3 format 
    if file_name.endswith(".mp3") or file_name.endswith(".MP3"):
        # Set the full file path
        file_path = os.path.join(folder_path, file_name)
        
        # Load the metadata for the audio file
        audio = EasyID3(file_path)
        
        # Get the title from the metadata
        title = audio['title'][0]
        
        # Rename the file using the title
        new_file_path = os.path.join(folder_path, f"{title}.mp3")
        os.rename(file_path, new_file_path)
