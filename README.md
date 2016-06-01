# Hash_Dir Overview

This repository holds my hash_dir project.  There are currently three python programs in the repository.  

1. hash_file will hash a single file and print the hexdigest to the screen.
2. hash_dir imports the hash_file function from hash_file and recursively hashes all of the files in a directory to include hidden files and files in its subdirectories.  The results and printed to a csv file which will include a timestamp and the hostname the program was run on as part of the file name.  The csv file will be saved to the same directory where hash_dir.py is run from.
3. hash_diff will take two csv files generated from the hash_dir program and output a diff report as a text file.  The diff file will report which files are new, modified, deleted, and unchanged.

This repositor contains a standalone executable version of both hash_dir and hash_file for Microsoft Windows.  You can use the executable to run the program without installing Python on the host machine.

# Usage
To run directly from command line use the following format:
```
python hash_file.py FILE_PATH ALGORITHM
python hash_dir.py DIR_PATH ALGORITHM

FILE_PATH is the path to the file.
DIR_PATH is the directory path.  
ALGORITHM is the the hashing algorithm to be used and must be one of the following:
'md5'
'sha1'
'sha224'
'sha256'
'sha384'
'sha512'

EXAMPLES:
python hash_dir.py / md5 1
(Hash all files less 1MB or less in the root directory using MD5)

python hash_dir.py c:\ sha256 100 True
(Hash all files less 100MB or less in the root directory using SHA256 and output hashed files to console)

python hash_dir.py "c:\program files" sha1 1000
(Hash all files less 1000MB or less in the root directory using SHA1)

python hash_diff.py <CSV_FILE1> <CSV_FILE2>
```

# Performance
Hashing small directories will be nearly instantaneous.  Hashing large directories such as the C:\Windows\System32\ will probably take between 10-20 seconds depending on how fast your machine is.  Hashing entire root directories can take 20 minutes or longer.

The csv file outputs will be proportionate to the number of files hashed.  This is not a problem for small directories but hashing large directories will create large csv files.  Make sure you have enough space for your files.

# Known Issues
Some files cannot be read because they protected.  This can occur even when running with administrator credentials.  These files will have a "bad hash" value of the string "bad_hash" hashed with the chosen algorithm.

