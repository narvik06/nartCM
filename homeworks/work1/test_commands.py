import pytest
from commands import CommandDispatcher
from io import BytesIO

tarfs_path = "OSFileSystem.tar"

username = 'cmUser'
disp = CommandDispatcher(tarfs_path, username)

disp.fs_obj.mkdir(f'home/{username}/dir1')
disp.fs_obj.mkdir(f'home/{username}/dir2')
disp.fs_obj.touch(f'home/{username}/dir1/file11.txt')
disp.fs_obj.touch(f'home/{username}/dir1/file12.txt')
disp.fs_obj.touch(f'home/{username}/dir2/file21.txt')
disp.fs_obj.touch(f'home/{username}/file1.txt')
disp.fs_obj.mkdir(f'home/{username}/empty')

def test_ls_in_current_direcry():
    disp.current_path = f'/home/{username}'
    result = disp.execute("ls")
    assert 'dir1' in result
    assert 'dir2' in result
    assert 'file1.txt' in result
    assert 'file12.txt' not in result

def test_ls_empty_directory():
    disp.current_path = f'/home/{username}'
    result = disp.execute('ls empty')
    assert result == ''

def test_cd_to_directory():
    disp.current_path = f'/home'
    disp.execute(f"cd ../home///./{username}//")
    assert disp.current_path == f'/home/{username}'

def test_cd_non_existent_directory():
    result = disp.execute("cd non_existent_folder")
    assert result == '-shellEmulNV: cd: non_existent_folder: No such file or directory'

def test_uname_command():
    result = disp.execute("uname")
    assert result == "shellEmulNV"