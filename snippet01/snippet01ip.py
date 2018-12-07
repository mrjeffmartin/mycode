#!/usr/bin/env python3

def add_ten (user_beginning_ip):
    ##print(user_beginning_ip.split('.'))
    octets = user_beginning_ip.split('.')
    for last_octet in octets[3:]:
        ##print (last_octet)
        plus_ten = int(last_octet) + 10
        ##print (plus_ten)
        if (plus_ten > 255):
            print ('Unable to add a block of 10 more IPs to this block because last octet would be greater than 255.')
            break
        elif (plus_ten >= 0):
            print ('Added IP addresses ' + user_beginning_ip + ' through ' + octets[0] + '.' + octets[1] + '.' + octets[2] + '.' + str(plus_ten))
            break
        else:
            break

print ("This program will reserve a block of 10 IP addresses at a time.")
user_beginning_ip = input('Please enter the starting IP address of the block you would like to add: ')

add_ten (user_beginning_ip)
