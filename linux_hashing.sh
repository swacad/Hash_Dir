find / -type f -size +1 -exec md5sum -b {} \; > hashes.txt
# For SHA1 format hashes use line below by commenting out top line and uncommenting bottom line.
# find / -type f -size +1 -exec md5sum -b {} \; > hashes.txt
