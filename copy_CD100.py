#!/usr/bin/env python

import os
import subprocess

def run_cmd(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    return p.stdout.readlines()

def escape_illegal_chars(s):
    illegal_chars = [" ", "(", ")", "&"]

    for char in illegal_chars:
        s = s.replace(char, "\%s" %char)

    return s

def replace_dir_slash(s):
    return s.replace('/', '&')


src_dir = "/Users/minhdang/Dropbox (Advanced Microgrid)/AMS-Macquarie Data room"
dest_dir = "/Users/minhdang/OneDrive - Advanced Microgrid Solutions/Manager/MacCap_Software_Escrow/2018"

os.chdir(src_dir)

# Command to find files
cmd = 'find . -type f -name "*.pdf" | egrep -i "CD-100|CD100|CD 100"'
output = run_cmd(cmd)

for line in output:
    # Remove leading "./" and trialing "\n"
    file_name = line[2:].strip('\n')

    src_file_path = escape_illegal_chars(os.path.join(src_dir, file_name))
    dest_file_path = escape_illegal_chars(os.path.join(dest_dir, replace_dir_slash(file_name)))

    print "src : %s" % src_file_path
    print "dest: %s" % dest_file_path
    cmd = "cp %s %s" % (src_file_path, dest_file_path)
    run_cmd(cmd)
