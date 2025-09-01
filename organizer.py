import os
import shutil
import logging

# --- FILE PATH AND TYPE CONFIGURATION ---
DOWNLOADS_PATH = "/Users/oluwabunmijoseph/Downloads/test-messy-folder"

FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
    'Documents': ['.pdf', '.doc', 'docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx', '.pages'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac', '.m4a'],
    'Video': ['.mp4', '.mov', '.avi', '.mkv'],
    'Scripts': ['.py', '.js', '.html', '.css', '.sh'],
}

# --- LOGGING CONFIGURATION ---
LOG_FILE_PATH = os.path.join(os.path.dirname(__file__), 'organizer.log')
logging.basicConfig(filename=LOG_FILE_PATH, level=logging.INFO, 
                    format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
# ---------------------------

def organize_files(path):
    logging.info(f"Scanning the directory: {path}")
    
    try:
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    except FileNotFoundError:
        logging.error(f"Error: The directory '{path}' was not found.")
        return

    for file in files:
        file_extension = os.path.splitext(file)[1].lower()
        moved = False

        for folder_name, extensions in FILE_TYPES.items():
            if file_extension in extensions:
                dest_folder_path = os.path.join(path, folder_name)
                os.makedirs(dest_folder_path, exist_ok=True)
                shutil.move(os.path.join(path, file), os.path.join(dest_folder_path, file))
                logging.info(f"Moved: {file} -> {folder_name}/")
                moved = True
                break
        
        if not moved:
            other_folder_path = os.path.join(path, 'Other')
            os.makedirs(other_folder_path, exist_ok=True)
            shutil.move(os.path.join(path, file), os.path.join(other_folder_path, file))
            logging.info(f"Moved: {file} -> Other/")

    logging.info("Organization complete! 🎉\n")

if __name__ == "__main__":
    organize_files(DOWNLOADS_PATH)