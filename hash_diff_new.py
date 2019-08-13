import argparse
from collections import defaultdict
import csv
from pprint import pprint


def main(reference, difference):
    hash_dict1 = defaultdict(set)
    hash_dict2 = defaultdict(set)

    path_dict1 = dict()
    path_dict2 = dict()

    with open(reference) as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            if row[0] == 'SHA1':
                # print(row)
                hash_val = row[1] # hash index
                hash_dict1[hash_val].add(row[2])
                path_dict1[row[2]] = row[1]

    with open(difference) as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            if row[0] == 'SHA1':
                hash_val = row[1] # hash index
                hash_dict2[hash_val].add(row[2])
                path_dict2[row[2]] = row[1]

    for k in hash_dict1:
        if k in hash_dict2:
            for p in hash_dict1[k]:
                if p in hash_dict2[k]:
                    # print('Match:', p)
                    continue
                else:
                    print(p + ' not in difference set')
        else:
            print('Difference set does not contain file hash: ' + k + ' ' + str(hash_dict1[k]))

    for k in path_dict1:
        if k in path_dict2:
            if path_dict1[k] != path_dict2[k]:
                print('Hashes do not match:', k)
        else:
            print('File not in difference set:', k)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('reference', help='Top directory to start hashing from')
    parser.add_argument('difference', help='Hashing algorithm to use')
    args = parser.parse_args()
    main(args.reference, args.difference)
