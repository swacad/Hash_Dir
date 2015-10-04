import sys
import datetime
import socket
from os import listdir, walk
from os.path import isfile, join
from hash_file_2_4 import hash_file

def get_filepaths(dirPath):
    """
    This function will generate the file names in a directory 
    tree by walking the tree either top-down or bottom-up. For each 
    directory in the tree rooted at directory top (including top itself), 
    it yields a 3-tuple (dirpath, dirnames, filenames).

    References:
    http://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory-in-python
    """
    file_paths = []  # List which will store all of the full filepaths.
    # Walk the tree.
    for root, directories, files in walk(dirPath):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = join(root, filename)
            file_paths.append(filepath)  # Add it to the list.
    return file_paths

if __name__ == '__main__':
    '''
    This will allow for execution from the command line using two arguments.
    args should follow hash_dir.py preceded with a space.
    arg1 is the path to the directory as a strings
    arg2 is the hashing algorithm to be used

    The text file containing the file paths and associated hash values will
    written to the directory in which hash_file.py is executed from.
    '''
    # Command line arguments
    dirPath = sys.argv[1]

    file_list = get_filepaths(dirPath)


    # Generate file name
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H%M.%Ss")
    hostname = socket.gethostname()
    fileName = 'hashes_' + hostname +  '_' + timestamp + ".txt"

    f = open(fileName, 'a')
    f.write('FILE_PATH - Hashing Algorithm: md5' + '\n')
    f.write('System Hostname: ' + hostname + '\n')
    f.write('Timestamp: ' + str(now) + '\n')
    f.write('###########################################################################\n')
    for i in range(0, len(file_list)):
        f.write(file_list[i] + ' - ' + hash_file(file_list[i].hexdigest() + '\n')
    f.write('#################### SUCCESSFULLY TERMINATED ###################')
    f.close()



