# Hash_Dir Overview

This repository holds my hash_dir project.  There are currently two python programs in the repository.  One is hash_file which will hash a single file and print the hexdigest to the screen.  The second program is hash_dir which imports the hash_file function from hash_file and hashes all of the files in a directory to include hidden files and files in its subdirectories.  The results and printed to a text file which is timestamped and includes the hostname the program was run on.  The text file will be saved to the same directory where hash_dir.py is run from.

I do have a standalone executable version of both hash_dir and hash_file for Microsoft Windows.  You can use the executable to run the program without installing Python on the host machine.

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
python hash_dir.py / md5
(This will hash the entire contents of the root directory using MD5)

python hash_dir.py c:\ sha256
(This will hash the entire contents of the C drive)

python hash_dir.py "c:\program files" sha1
(This will hash the entire contents of the C:\Windows\System32\ directory using SHA1)
```

# Performance
Hashing small directories will be nearly instantaneous.  Hashing large directories such as the C:\Windows\System32\ will probably take between 10-20 seconds depending on how fast your machine is.  Hashing entire root directories can take 20 minutes or longer.

The text file outputs will be proportionate to the number of files hashed.  This is not a problem for small directories but hashing large directories will create large text files.  Make sure you have enough space for your files.

# Known Issues
Some files cannot be read because they protected.  This can occur even when running with administrator credentials.  These files will have a "bad hash" value of 6150626741db26913278948d5d32b779500a6eb03907732d9c28a1f74e86cfc02844d172eb22c0e1fb16230ef7084e0b24a7d27b639c1759c5ed10aec6cb1d5a.

# To Do
1.  Clean up execution portion of code by modularizing the code.
2.  Add the ability to compare a list of hashes from a text file and output all matching or non-matching files and hashes to another text file.
