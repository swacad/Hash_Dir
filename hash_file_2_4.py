import md5
import sys

'''
To run this program type the following in a command prompt or shell console:

python PATH/hash_file.py 'PATH/target_file'

Update 8/27/2015:  modified funciton to support older versions of Python,
specifically version 2.4
'''

def hash_file(FILE_NAME):
    '''
    Description:  This function will hash a file and return the hash object.
    The hash algorithm can be modified by changing the hashlib algorithm.
    This function should be able to hash objects of indefinite size.  

    References:
    https://docs.python.org/2/library/hashlib.html
    http://www.pythoncentral.io/hashing-files-with-python/

    input args:
    FILE_NAME is the path and name of the file to be hashed in string format.

    output:
    hasher is the HASH object created by the hashlib function
    '''
    blockSize = 2 ** 16
    fileHash = md5.new()
    try:
        f = open(FILE_NAME, 'rb')
        buf = f.read(blockSize)
        while len(buf) > 0:
            fileHash.update(buf)
            buf = f.read(blockSize)
        f.close()
        return fileHash
    except IOError:
        return md5.new('bad_hash')



if __name__ == '__main__':
    fileName = sys.argv[1]
    print hash_file(fileName).hexdigest()

    