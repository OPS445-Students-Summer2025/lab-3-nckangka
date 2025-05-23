#!/usr/bin/env python3

# Author ID: kang-kang

import subprocess

def free_space():
    p = subprocess.Popen(["df -h | grep '/$' | awk '{print $4}'"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output = p.communicate()
    stdout = output[0].decode('UTF-8').strip()
    return stdout

free_space()

