import argparse
import hashlib
import os
import time


def get_bad_hash(algo):
    bad_hash = 'bad_hash'
    if algo == 'md5':
        bad_hash = hashlib.md5(b'bad_hash')
    elif algo == 'sha1':
        bad_hash = hashlib.sha1(b'bad_hash')
    elif algo == 'sha224':
        bad_hash = hashlib.sha224(b'bad_hash')
    elif algo == 'sha256':
        bad_hash = hashlib.sha256(b'bad_hash')
    elif algo == 'sha384':
        bad_hash = hashlib.sha384(b'bad_hash')
    elif algo == 'sha512':
        bad_hash = hashlib.sha512(b'bad_hash')

    return bad_hash


def hash_file(file_name, algo):
    """
    Description:  This function will hash a file and return the hash object.
    The hash algorithm can be modified by changing the hashlib algorithm.
    This function should be able to hash objects of indefinite size.

    References:
    https://docs.python.org/2/library/hashlib.html
    http://www.pythoncentral.io/hashing-files-with-python/

    input args:
    file_name is the path and name of the file to be hashed in string format.

    algo is the hashing algorithm in string format.  Allowed algorithms are:
    'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512'

    output:
    hasher is the HASH object created by the hashlib function
    """

    file_hash = None
    block_size = 2 ** 16
    if algo == 'md5':
        file_hash = hashlib.md5()
    elif algo == 'sha1':
        file_hash = hashlib.sha1()
    elif algo == 'sha224':
        file_hash = hashlib.sha224()
    elif algo == 'sha256':
        file_hash = hashlib.sha256()
    elif algo == 'sha384':
        file_hash = hashlib.sha384()
    elif algo == 'sha512':
        file_hash = hashlib.sha512()
    try:
        with open(file_name, 'rb') as f:
            _buffer = f.read(block_size)
            while len(_buffer) > 0:
                file_hash.update(_buffer)
                _buffer = f.read(block_size)
        f.close()
        return file_hash
    except IOError:
        return get_bad_hash(algo)


def hash_dir(top, algo):
    # f = open('test.csv', 'w')
    # f.write('path,' + algo + '\n')
    for root, dirs, files in os.walk(top):
        for name in files:
            file_path = (os.path.join(root, name))
            file_hash = hash_file(file_path, algo=algo).hexdigest()
            # print(hash_file(file_path, algo='md5').hexdigest())
            # f.write(file_path + ',' + hash_file(file_path, algo='md5').hexdigest() + '\n')
    # f.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('top', help='Top directory to start hashing from')
    parser.add_argument('algo', help='Hashing algorithm to use')
    args = parser.parse_args()
    start = time.time()
    hash_dir(args.top, args.algo)
    print('Run time:', time.time() - start)
