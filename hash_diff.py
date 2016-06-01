import csv
import datetime
import sys

def main():
    csv1 = sys.argv[1]
    csv2 = sys.argv[2]

    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H%M.%Ss")
    report_name = 'hash_diff_report_' + timestamp + '.txt'
    f = open(report_name, 'a')

    csv1_list = []
    csv2_list = []
    new = []
    deleted = []
    changed = []
    unchanged = []

    with open(csv1, newline='') as csvfile:
        hash_reader = csv.reader(csvfile, delimiter=',')
        row_idx = 0
        for row in hash_reader:
            if row_idx > 1:
                csv1_list.append(row)
            row_idx += 1

    with open(csv2, newline='') as csvfile:
        hash_reader = csv.reader(csvfile, delimiter=',')
        row_idx = 0
        for row in hash_reader:
            if row_idx > 1:
                csv2_list.append(row)
            row_idx += 1

    csv2_dict = dict(csv2_list)

    for i in range(len(csv1_list)):
        file_path = csv1_list[i][0]
        hash_hex_digest = csv1_list[i][1]

        if file_path not in csv2_dict:
            deleted.append(file_path)
        elif file_path in csv2_dict and hash_hex_digest == csv2_dict[file_path]:
            unchanged.append(file_path)
            csv2_dict.pop(file_path)
        elif file_path in csv2_dict and hash_hex_digest != csv2_dict[file_path]:
            changed.append(file_path)
            csv2_dict.pop(file_path)

    for file_path in csv2_dict:
        new.append(file_path)

    print('DELETED FILES BELOW:')
    f.write('DELETED FILES BELOW:' + '\n')
    for file_path in deleted:
        print(file_path)
        f.write(file_path + '\n')
    print('\n')
    f.write('\n')

    print('CHANGED FILES BELOW:')
    f.write('CHANGED FILES BELOW:' + '\n')
    for file_path in changed:
        f.write(file_path + '\n')
        print(file_path)
    print('\n')
    f.write('\n')

    print('NEW FILES BELOW:')
    f.write('NEW FILES BELOW:' + '\n')
    for file_path in new:
        f.write(file_path + '\n')
        print(file_path)
    print('\n')
    f.write('\n')

    print('UNCHANGED FILES BELOW:')
    f.write('UNCHANGED FILES BELOW:' + '\n')
    for file_path in unchanged:
        f.write(file_path + '\n')
        print(file_path)
    print('\n')
    f.write('\n')

if __name__ == '__main__':
    main()

