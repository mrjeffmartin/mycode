#!/usr/bin/env python3
import csv

### Make f a file object, by reading csv_users.txt
f = open('csv_users.txt', 'r')

### Set i equal to 0. We’re going to use this as a counter.
i = 0

### Now we want to use the csv.reader() This function will read each line of the file in row.
### Row becomes a list, where each comma seperated value becomes a new value in that list.
for row in csv.reader(f):
    i = i + 1
    filename = 'admin.rc%d'%(i,)
    rcfile = open(filename, 'w')
    print('export OS_AUTH_URL=' + row[0], file=rcfile)
    print('export OS_IDENTITY_API_VERSION=3', file=rcfile)
    print('export OS_PROJECT_NAME=' + row[1], file=rcfile)
    print('export OS_PROJECT_DOMAIN_NAME=' + row[2], file=rcfile)
    print('export OS_USERNAME=' + row[3], file=rcfile)
    print('export OS_USER_DOMAIN_NAME=' + row[4], file=rcfile)
    print('export OS_PASSWORD=' + row[5], file=rcfile)
    rcfile.close()