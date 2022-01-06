import os


os.chdir(r'C:\Users\Nicol\OneDrive\Bureau\travail\sistemas digitais')

for f in os.listdir():
    print(os.path.splitext(f))
    