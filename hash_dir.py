import sys
import datetime
import socket
from os import walk, stat
from os.path import join
from hash_file import hash_file, get_bad_hash


def hash_dir(dir_path, algo, max_file_size=100, display_current_file=False):
    """
    Description:  hash_dir creates a dictionary of hashes where the key is the
    full file path and the value is the associated hash object which is created
    by calling hash_file.  All files in the directory and subdirectories are
    operated upon.

    :param dir_path: str path to directory in which to recursively hash files
    :param algo: str of hashing algorithm to be used.
        Allowed values are 'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512'
    :param max_file_size: Maximum file size in MB.
    :param display_current_file: Display current file to screen switch
    :return:
    :param hash_dict: dictionary containing file:hash pairs
    """
    hash_dict = {}
    file_list = get_file_paths(dir_path)
    for f in file_list:
        if stat(f).st_size <= max_file_size:
            if display_current_file:
                print(f)
            hash_dict[f] = hash_file(f, algo).hexdigest()

    return hash_dict


def get_file_paths(dir_path):
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
    for root, directories, files in walk(dir_path):
        for filename in files:
            # Join the two strings in order to form the full file_path.
            file_path = join(root, filename)
            file_paths.append(file_path)  # Add it to the list.

            # Comment out if you don't want to print file_path to screen during list build
            # print(file_path)
    return file_paths


def main():
    """
    This will allow for execution from the command line using two arguments.
    args should follow hash_dir.py preceded with a space.
    arg1 is the path to the directory as a strings
    arg2 is the hashing algorithm to be used

    The text file containing the file paths and associated hash values will
    written to the directory in which hash_file.py is executed from.
    """
    # Command line arguments
    dir_path = sys.argv[1]
    hash_algo = sys.argv[2]
    max_file_size = sys.argv[3]
    display_current_file = sys.argv[4] # should be True or False
    if display_current_file.lower() == 'true':
        display_current_file = True
    else:
        display_current_file = False

    max_file_size = int(max_file_size)
    max_file_size *= 2**(10*2)

    hash_dict = hash_dir(dir_path, hash_algo, max_file_size, display_current_file)

    # Generate file name
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H%M.%Ss")
    hostname = socket.gethostname()
    file_name = 'hashes_' + hash_algo + '_' + hostname + '_' + timestamp + '.csv'
    bad_hash = get_bad_hash(hash_algo).hexdigest()

    f = open(file_name, 'a')
    f.write('FILE_PATH,Hashing Algorithm: ' + hash_algo + '\n')
    f.write('BAD_FILE_HASH,' + bad_hash + '\n')
    for key in hash_dict:
        f.write(key + ',' + hash_dict[key] + '\n')
    f.close()


if __name__ == '__main__':
    main()
