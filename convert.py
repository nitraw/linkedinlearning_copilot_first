from pathlib import Path

import yaml
from mutagen.easyid3 import EasyID3

def read_audio_files(audio_directory):
    audio_path = Path(audio_directory)
    audio_files = []

    for file_path in sorted(audio_path.glob('*.mp3')):
        tags = EasyID3(file_path)
        metadata = {
            key: values[0] if len(values) == 1 else values
            for key, values in tags.items()
        }
        metadata['file'] = f'/{audio_path.name}/{file_path.name}'
        audio_files.append(metadata)

    return audio_files

if __name__ == '__main__':
    print(yaml.safe_dump(read_audio_files('audio'), sort_keys=False))

