#!/usr/bin/env python3
# This script checks if input matches 
hostname = input('Please enter hostname: ')
if hostname is 'MTG' or 'mtg' or 'mTg' or 'MTg' or 'mTG' or 'MtG':
	print('The hostname was found to be '+ hostname)
	print ('hostname matches expected config')
print ('Exiting the script.')