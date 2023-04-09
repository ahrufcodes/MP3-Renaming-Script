# Mp3 Renaming Script

This script allows you to rename multiple MP3 files based on their metadata, specifically the title tag. (You can cahnge this as you seem fit) 

**Prerequisites**

Python 3.x
mutagen library
You can install the mutagen library using pip:

**Copy code**

pip install mutagen

**Usage**

*Clone this repository to your local machine.*

*Place your MP3 files that you want to rename in a folder.*

*Open the rename_mp3.py file in a code editor.*

*Modify the folder_path variable to the path of the folder containing your MP3 files.*

*Save the rename_mp3.py file.*

*In your terminal, navigate to the folder where the rename_mp3.py file is located.*

*Run the rename_mp3.py file using the following command: python rename_mp3.py.*

The script will loop through all the files in the specified folder, check if each file is an MP3 file, load the metadata for the MP3 file, retrieve the title from the metadata, and rename the file using the title. The new file names will be based on the title tag in the MP3 file's metadata.
