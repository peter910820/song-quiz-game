import os

directory = "E:\Code\song-quiz-game\static"

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    
    if os.path.isfile(file_path) and not filename.endswith('.txt'):
        try:
            os.remove(file_path)
            print(f'Removed file: {file_path}')
        except Exception as e:
            print(f'Error removing file: {file_path}, {e}')