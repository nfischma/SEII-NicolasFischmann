import os

print(os.getcwd())

os.chdir(r'C:\Users\Nicol\OneDrive\Bureau\travail\sistemas digitais')

print(os.getcwd())


os.mkdir("OS-demo-2")

print(os.listdir())
os.rename('OS-demo-2', 'OS-demo-1')
print(os.listdir())
os.rmdir('OS-demo-1')


from datetime import datetime
print("")
mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time))


print("")
for dirpath, dirnames, filenames in os.walk(r'C:\Users\Nicol\OneDrive\Bureau\travail\sistemas digitais'):
    print('Current Path:', dirpath)
    print('Directories', dirnames)
    print('Files', filenames)
    print()


print(os.environ.get('HOME'))
