import os

directory  = "D:\code\Cafe management"


def check_name(filename):
    if filename in os.listdir(directory):
        return "yes"
    else:
        return "no"  

