import os


os.chdir(r'C:\Users\Nicol\OneDrive\Bureau\travail\sistemas digitais')

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    print(file_name, file_ext)
    print( file_name.split('-'))
    
