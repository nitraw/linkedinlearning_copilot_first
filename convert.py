import os

#create a function that read audio file in mp3 format
#the audio directory and return the list of audio files in the directory

def read_audio_files(audio_directory):

    audio_files = []

    # Iterate through the files in the directory
    for file_name in os.listdir(audio_directory):
        # Check if the file is an mp3 file
        if file_name.endswith('.mp3'):
            audio_files.append(file_name)

    return audio_files

print(read_audio_files('audio'))
    
