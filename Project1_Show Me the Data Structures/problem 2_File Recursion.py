from os.path import isfile, isdir, join
from os import listdir

def find_files(suffix, path):
    files = []
    folder_content = listdir(path)
    for i in range(len(folder_content)):
        if isdir(path + '\\' + folder_content[i]):
            files = files + find_files(suffix, path + '\\' + folder_content[i])
        elif folder_content[i].endswith(suffix):
            files.append(folder_content[i])
    return files


if __name__ == '__main__':

    # test general functionality
    path = r'C:\Files\Udacity\Data Structures and Algorithms\P0\P0\Project1_Show Me the Data Structures\testdir\testdir'
    find_files('.c', path)
    files = find_files('.c', path)
    print(files)

    # test edge case 1 (invalid directory path)
    path = r'C:\Files\Udacity\Data Structures and Algorithms\P0\P0\Project1_Show Me the Data Structures\testdir\testdir2'
    try:
        files = find_files('.c', path) # must raise error FileNotFoundError: [WinError 3] The system cannot find the path specified:
    except FileNotFoundError as f:
        print(f)

    # test edge case 2 (empty directory)
    path = r'C:\Files\Udacity\Data Structures and Algorithms\P0\P0\Project1_Show Me the Data Structures\testdir\testdir\empty'
    find_files('.c', path)
    files = find_files('.c', path)
    print(files) # []