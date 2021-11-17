# Helper functions

import os
import socket

def find_dir_GI():
    cpu = socket.gethostname()
    if cpu == 'RT5362WL-GGB':
        print('On predator machine')
        di_dir = {'windows':'D:\\projects\\GIOrdinal', 'wsl':'/mnt/d/projects/Ordinal'}
        di_os = {'nt':'windows', 'posix':'wsl'}
        dir_GI = di_dir[di_os[os.name]]
    elif cpu == 'snowqueen':
        print('On snowqueen machine')
        dir_GI = '/data/GIOrdinal'
    elif cpu == 'cavansite':
        print('On cavansite')
        dir_GI = '/data/erik/GIOrdinal'
    elif cpu == 'malachite':
        print('On malachite')
        dir_GI = '/home/erik/projects/GIOrdinal'
    else:
        sys.exit('Where are we?!')
    return dir_GI
