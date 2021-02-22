#!/usr/bin/python2
#
# Credits to: 
#https://gist.github.com/sgk/1286682#file-trac2down-py-L42 for the regular expressions and the general idea for such a python script
#
# This script assumes that you have already exported the trac wiki pages with trac-admin into some dump files.
# The first argument of the script is the folder with all wiki pages
# Afterwards the folder export, which must be created before, will contain the markdown translation
#
import io
import sys
import datetime
import re
import os

for subdir, dirs, files in os.walk(sys.argv[1]):
    for File in files:
        filept = open(os.path.join(subdir, File))
        fp = open('export/%s.md' % File, 'w')

        for text in filept.readlines():
            print (text)
            text = re.sub('\r\n', '\n', text)
            text = re.sub(r'{{{(.*?)}}}', r'`\1`', text)
            def indent4(m):
                return '\n ' + m.group(1).replace('\n', '\n ')
            text = re.sub(r'(?sm){{{\n(.*?)\n}}}', indent4, text)
            text = re.sub(r'(?m)^====\s+(.*?)\s+====$', r'#### \1', text)
            text = re.sub(r'(?m)^===\s+(.*?)\s+===$', r'### \1', text)
            text = re.sub(r'(?m)^==\s+(.*?)\s+==$', r'## \1', text)
            text = re.sub(r'(?m)^=\s+(.*?)\s+=$', r'# \1', text)
            text = re.sub(r'^ \d+. ', r'1.', text)

            line = text
            line = re.sub(r'\[(https?://[^\s\[\]]+)\s([^\[\]]+)\]', r'[\2](\1)', line)
            line = re.sub(r'\[(wiki:[^\s\[\]]+)\s([^\[\]]+)\]', r'[\2](/\1/)', line)
            line = re.sub(r'\!(([A-Z][a-z0-9]+){2,})', r'\1', line)
            line = re.sub(r'\'\'\'(.*?)\'\'\'', r'*\1*', line)
            line = re.sub(r'\'\'(.*?)\'\'', r'_\1_', line)

            fp.write(line)#.encode('utf-8'))
    
        filept.close()
        fp.close() 