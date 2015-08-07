import hashlib

def hash_file(FILE_NAME, algo):
    '''
    Description:  This function will hash a file and return the hash object.
    The hash algorithm can be modified by changing the hashlib algorithm.

    References:
    https://docs.python.org/2/library/hashlib.html
    http://www.pythoncentral.io/hashing-files-with-python/

    input args:
    FILE_NAME is the path and name of the file to be hashed in string format.

    algo is the hashing algorithm in string format.  Allows algorithms are:
    'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512'

    output:
    hasher is the HASH object created by the hashlib function
    '''
    blockSize = 2 ** 16
    if algo == 'md5':
        fileHash = hashlib.md5()
    elif algo == 'sha1':
        fileHash = hashlib.sha1()
    elif algo == 'sha224':
        fileHash = hashlib.sha224()
    elif algo == 'sha256':
        fileHash = hashlib.sha256()
    elif algo == 'sha384':
        fileHash = hashlib.sha384()
    elif algo == 'sha512':
        fileHash = hashlib.sha512()
    with open(FILE_NAME, 'rb') as afile:
        buf = afile.read(blockSize)
        while len(buf) > 0:
            fileHash.update(buf)
            buf = afile.read(blockSize)
    return fileHash
