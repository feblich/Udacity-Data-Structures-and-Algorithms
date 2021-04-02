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

    path = r'C:\Files\Udacity\Data Structures and Algorithms\P0\P0\Project1_Show Me the Data Structures\testdir\testdir'
    find_files('.c', path)
    files = find_files('.c', path)