#!/usr/bin/env python3


text_file = open('/home/student/mycode/snippet01/internet_traveler.txt','r')
text_file_lines = text_file.readlines()

print ("\t".join(text_file_lines)) ###puts tab "\t" between every item on the list 
