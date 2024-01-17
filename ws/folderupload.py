from cgi import FieldStorage
import os
import requests

folder = r'C:\Users\laboratorio\Desktop\Fotos2019' 

for filename in os.listdir(folder):
  if filename.lower().endswith('.jpg') or filename.lower().endswith('.png')  :
    
    file_path = os.path.join(folder, filename)
    
    files = {'file': open(file_path, 'rb')} 
    response = requests.post('http://localhost:5000/upload', files=files)
    
    if response.status_code == 200:
       print(f'{filename} uploaded!') 
    else:
       print(f'Error uploading {filename}')