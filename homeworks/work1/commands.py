import os
import sys
from TarOSFileSystem import TarOSFileSystem

uname = "shellEmulNV"

def handlePath(vfs, current_path, arg_path):

    if not arg_path:
        return current_path

    arg_path = arg_path.rstrip('/')
    while '//' in arg_path:
        arg_path = arg_path.replace('//', '/')
    chunks = arg_path.split('/')

    i = 0
    while i < len(chunks):
        if chunks[i] == '':
            current_path = '/'
            i += 1
        elif chunks[i] == '..':
            if current_path == '/':
                i += 1
                continue
            parts = current_path.split('/')
            parts.pop()
            if len(parts) < 2:
                parts.append('')
            current_path = '/'.join(parts)
            i += 1
        elif chunks[i] == ".":
            i += 1
            continue
        else:
            maxChunk = chunks[i]
            while i + 1 < len(chunks) and chunks[i + 1] not in ['..','.']:
                maxChunk += f'/{chunks[i + 1]}'
                i += 1

            expected_path = f"{current_path.rstrip('/')}/{maxChunk}"
            for dir_path in vfs.tarFS.getnames():
                dir_path = f"/{dir_path}"
                if dir_path == expected_path:
                    if vfs.tarFS.getmember(dir_path.lstrip('/')).isdir():
                        current_path = expected_path
                        i += 1
                        break
                    else:
                        return -1
            if (current_path != expected_path):
                return False
    return current_path



class LS:
    @staticmethod
    def run(vfs, current_path, dirs):

        if not dirs:
            dirs.append('.')
        for i in range(len(dirs)):
            ls_path = handlePath(vfs, current_path, dirs[i])
            if not ls_path:
                dirs[i] = f"ls: cannot access '{dirs[i]}': No such file or directory"
            elif ls_path == -1:
                continue

            files = list()
            for file_path in vfs.tarFS.getnames():
                file_path = f'/{file_path}'
                truncated = file_path[len(ls_path):].lstrip('/')
                if truncated and file_path.startswith(ls_path) and not '/' in truncated:

                    fname = truncated
                    if vfs.tarFS.getmember(file_path.lstrip('/')).isdir():
                        fname = f"\033[34m{fname}\033[0m"
                    
                    files.append(fname)

            dirs[i] = f'{dirs[i]}:{'\n' if files else ''}{'\t'.join(files)}' if len(dirs) > 1 else f'{'\t'.join(files)}'
        
        return '\n\n'.join(dirs)


class CD:
    @staticmethod
    def run(vfs, current_path, arg_path):

        if not arg_path:
            return current_path
        elif len(arg_path) > 1:
            return f"-{uname}: cd: too many arguments"
        
        result = handlePath(vfs, current_path, arg_path[0])
        if not result:
            result = f"-{uname}: cd: {arg_path[0]}: No such file or directory"
        elif result == -1:
            result = f"-{uname}: cd: {arg_path[0]}: Not a directory"
        
        return result
    

class Mkdir:
    @staticmethod
    def run(vfs, current_path, dirs):

        for dir in dirs:

            newdir_location = handlePath(vfs, current_path, dir)
            if newdir_location:
                return f"mkdir: cannot create directory ‘{dir}’: File exists"
            
            dir = dir.rstrip('/')
            dir = dir.replace('//', '/')

            parts = dir.split('/')
            newdir = parts.pop()
            parent = '/'.join(parts)

            newdir_location = handlePath(vfs, current_path, parent)
            if not newdir_location:
                return f"mkdir: cannot create directory ‘{dir}’: No such file or directory"
            
            newdir = f"{newdir_location}/{newdir}".lstrip('/')
            
            vfs.mkdir(newdir)
            

class Touch:

    def run(vfs, current_path, fpaths):

        for fpath in fpaths:

            fpath = fpath.rstrip('/')
            fpath  = fpath.replace('//', '/')

            parts = fpath.split('/')
            newfile = parts.pop()
            parts.append('')
            parent = '/'.join(parts)

            file_location = handlePath(vfs, current_path, parent)
            if not file_location:
                return f"-{uname}: {fpath}: No such file or directory"
            
            newfile = f"{file_location}/{newfile}".lstrip('/')
            
            vfs.touch(newfile)


class Exit:
    @staticmethod
    def run(vfs, current_path, args):
        print(f"Exiting {uname} shell emulator.")
        vfs.tarFS.close()
        sys.exit()

class Clear:
    @staticmethod
    def run(vfs, current_path, args):
        os.system('cls')

class Uname:
    @staticmethod
    def run(vfs, current_path, args):
        return f"{uname}"
    
class Pwd:
    @staticmethod
    def run(vfs, current_path, args):
        return current_path
    

class CommandDispatcher:
    def __init__(self, fs_path, username):
        self.username = username
        self.fs_obj = TarOSFileSystem(fs_path, username)
        self.current_path = f'/home/{username}'
        self.blue = ['\033[34m', '\033[0m']
        self.inputPrompt_path = f'{self.blue[0]}~{self.blue[1]}'
        self.commands = {
            'ls': LS,
            'cd': CD,
            'exit': Exit,
            'clear': Clear,
            'uname': Uname,
            'mkdir': Mkdir,
            'touch': Touch,
            'pwd' : Pwd
        }
        self.uname = "shellEmulNV"

    def execute(self, command: str) -> str:
        if not command:
            return ''
        parts = command.split()
        cmd = parts[0]
        args = parts[1:]

        cmd_class = self.commands.get(cmd)

        if not cmd_class:
            return f"{cmd}: command not found"
        
        result = cmd_class.run(self.fs_obj, self.current_path, args)
        if cmd == "cd" and not result.startswith('-'):
            self.current_path = result
            if self.current_path.startswith(f'/home/{self.username}'):
                self.inputPrompt_path = f'{self.blue[0]}{self.current_path.replace(f"/home/{self.username}", f'~', 1)}{self.blue[1]}'
            else:
                self.inputPrompt_path = f'{self.blue[0]}{self.current_path}{self.blue[1]}'
            result = ''
        
        return result