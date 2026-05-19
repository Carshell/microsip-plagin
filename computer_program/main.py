import os
import time
import requests

PATH_FOLDER = "C:/Users/Loq/Documents/КПІ/КомпютернаГрафіка"
SERVER = "http://213.32.25.197" 

class File:
    def __init__(self, path):
        self.path = path

    def sent_to_server(self):
        filename = os.path.basename(self.path)
        mime_type = 'audio/wav' if self.path.endswith('.wav') else 'audio/mpeg'
        
        try:
            with open(self.path, 'rb') as f:
                files = {'file': (filename, f, mime_type)}
                
                response = requests.post(SERVER, files=files, timeout=30)
                
                if response.status_code == 200:
                    print(f"File {filename} is sent.")
                    return True  
                else:
                    print(f"Server error: {response.status_code}")
                    return False
                    
        except PermissionError:
            print(f"File {filename} blocked (file is holding). Waiting...")
            return False
            
        except requests.exceptions.RequestException as e:
            print(f"Помилка мережі при відправці файлу: {e}")
            return False

    def delete_file(self):
        try:
            os.remove(self.path)
            print("File deleted.")
        except Exception as e:
            print(f"File could not be sent: {e}")

def get_file(folder_path):
    if not os.path.exists(folder_path):
        print("Folder not found!")
        return None
    
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            return File(item_path)
            
    return None

print("Program started...")
while True:
    found_file = get_file(PATH_FOLDER)
    
    if found_file:
        success = found_file.sent_to_server()

        if success:
            found_file.delete_file()

    time.sleep(10)