import tarfile
import time
from io import BytesIO

class TarOSFileSystem:
    def __init__(self, fs_path, hostname):
        self.hostname = hostname
        self.tarFS = tarfile.open(fs_path, 'w')
        self.mkdir('home')
        self.mkdir(f'home/{hostname}')
    
    def mkdir(self, dir_name):
        dinfo = tarfile.TarInfo(name=dir_name)
        dinfo.type = tarfile.DIRTYPE
        dinfo.mode = 0o755
        dinfo.mtime = time.time()
        self.tarFS.addfile(tarinfo=dinfo)
    
    def touch(self, file_name):
        finfo = tarfile.TarInfo(name=file_name)
        finfo.mtime = time.time()
        self.tarFS.addfile(tarinfo=finfo)