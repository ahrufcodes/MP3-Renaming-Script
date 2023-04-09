# from mutagen.easyid3 import EasyID3

# # Set the path to the audio file
# file_path = r"C:\Users\ahmad\Desktop\Ayub\MUHAMMAD\127162161.MP3"

# # Load the metadata for the audio file
# audio = EasyID3(file_path)

# # Print the metadata for the audio file
# print(audio.pprint())


from mutagen.easyid3 import EasyID3
import os

# Set the path to the audio file
file_path = r"C:\Users\ahmad\Desktop\Ayub\MUHAMMAD\127162161.MP3"

# Load the metadata for the audio file
audio = EasyID3(file_path)

# Get the title from the metadata
title = audio['title'][0]

# Rename the file using the title
file_name, extension = os.path.splitext(file_path)
new_file_path = f"{os.path.dirname(file_path)}\\{title}{extension}"
os.rename(file_path, new_file_path)
