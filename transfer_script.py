#!/usr/bin/env python3

#Import Libraries
import os,shutil, time, sys

#Global Variables
out_file = input("Enter which company you are generating this report for: ")

#Functions

def move() :
	os.system("mkdir temp")
	for f in os.listdir():
		if os.path.isfile(f):
			if f != "transfer_script.py":
				cmd = "mv " + f + " temp"
				os.system(cmd)
def zip():
	shutil.make_archive(out_file, 'zip', 'temp')
	os.system("rm temp/*")
	os.system("rmdir temp")
#Main Script
move()
zip()

cmd = "transfer " + out_file 
os.system(cmd)
