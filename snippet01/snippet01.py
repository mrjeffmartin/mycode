#!/usr/bin/env python3


text_file = open('/home/student/mycode/snippet01/internet_traveler.txt','r')
text_file_lines = text_file.readlines()

print(\n".join(text_file_lines))

###my_list = [line.split(' , ')for line in open ("test")]
###print (my_list)

###for i in range(len(text_file_lines)):
###    if "- - - - -] Authorization failed" in keystone_file_lines[i]:
###        loginfail += 1 # this is the same as loginfail = loginfail + 1
###print('The number of failed log in attempts is ' + str(loginfail))