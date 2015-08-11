import sys
from os import listdir, walk
from os.path import isfile, join
from hash_file import hash_file

def hash_dir(dirPath, algo):
    '''
    Description:  hash_dir creates a dictionary of hashes where the key is the
    full file path and the value is the associated hash object which is created
    by calling hash_file.  All files in the directory and subdirectories are 
    operated upon.

    input args:
    dirName is the path to the directory in which to hash files
    algo is the type of hashing algorithm to be used.  Allowed algorithms are:
    'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512'

    output:
    hashDict is the dictionary containing the file:hash pairs.
    '''
    hashDict = {}
    fileList = get_filepaths(dirPath)
    for f in fileList:
        hashDict[f] = hash_file(f, algo).hexdigest()
    return hashDict

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
    dirPath = sys.argv[1]
    hashAlgo = sys.argv[2]
    hashDict = hash_dir(dirPath, hashAlgo)
    f = open('hashDict.txt', 'a')
    f.write('FILE PATH - Hashing Algorithm: ' + hashAlgo + '\n\n')
    for key in hashDict:
        f.write(key + ' - ' + hashDict[key] + '\n')
    f.close()



