#!/usr/bin/python2
#
# Credits to: 
#https://gist.github.com/sgk/1286682#file-trac2down-py-L42 for the regular expressions and the general idea for such a python script
#
# This script assumes that you have already exported the trac wiki pages with trac-admin into some dump files.
# The first argument of the script is the folder with all wiki pages
# Afterwards the folder export, which must be created before, will contain the markdown translation
#
# BJS Added or Fixed
#
# (fixed) line ends with space after header symbol '= '
# (added) code spread across several lines {{{\n  !#python  <some code>\n }}}\n - NB. might have spaces after/before {}
# (fixed) found that some list converts did not have space, so MD did not interpret correctly.
#    - 1.bob   versus   1. bob
#
#
# (issue) Some FAQ q/a pairs were all in the first line (the header line), not separate lines
# (issue) Some embedded multi-line code blocks in a list ended up lined up at space 0, thus
#   causing the list to start over numbering for the next entry.  Simple solution is
#   to manually select and tab over the code block. 
#

import re
from pathlib import Path


def convert(fin, fout):

    filept = open(fin, encoding="utf-8", errors="ignore")
    fp = open(fout, 'w')

    print(fin)

    try:

        for i, text in enumerate(filept.readlines()):

            text = re.sub('\r\n', '\n', text)
            text = re.sub(r'{{{(.*?)}}}', r'`\1`', text)

            def indent4(m):
                return '\n ' + m.group(1).replace('\n', '\n ')

            text = re.sub(r'(?sm){{{\n(.*?)\n}}}', indent4, text)
            text = re.sub(r'(?m)^====\s*(.*?)\s*====\s*$', r'#### \1', text)
            text = re.sub(r'(?m)^===\s*(.*?)\s*===\s*$', r'### \1', text)
            text = re.sub(r'(?m)^==\s*(.*?)\s*==\s*$', r'## \1', text)
            text = re.sub(r'(?m)^=\s*(.*?)\s*=\s*$', r'# \1', text)
            text = re.sub(r'^ \d+. ', r'1. ', text)

            line = text
            line = re.sub(r'\[(https?://[^\s\[\]]+)\s([^\[\]]+)\]', r'[\2](\1)', line)
            line = re.sub(r'\[(wiki:[^\s\[\]]+)\s([^\[\]]+)\]', r'[\2](/\1/)', line)
            line = re.sub(r'\!(([A-Z][a-z0-9]+){2,})', r'\1', line)
            line = re.sub(r'\'\'\'(.*?)\'\'\'', r'*\1*', line)
            line = re.sub(r'\'\'(.*?)\'\'', r'_\1_', line)

            # bjs addins

            line = re.sub(r'\s*{{{\s*\n', r'```\n', line)
            line = re.sub(r'\s*}}}\s*\n', r'```\n', line)

            fp.write(line)  # .encode('utf-8'))

    except UnicodeEncodeError as e:
        # bjs - 2021 Feb 23
        # readlines() threw exception when it found odd >= sign in Trac export files
        # open(encoding=??, errors='ignore') did not fix this, so i did it the hard
        # way with this except. When stopped here, I go into File and change that
        # (or other) symbol by hand and save.  Only about 3 issues in all my Tracs
        bob = 10

    filept.close()
    fp.close()




#--------------------------------------------------------------------

def _convert_all():

    fbase = 'D:/Users/bsoher/code/repo_github/vespa.io/trac_files'

    # # debug code for testing just one file
    # ftrac = ['dump_hlsvdpro', ]
    # fname = 'HowToBuildWheelsLinuxSetup'
    # convert(Path(fbase, ftrac[0], fname), Path(fbase, ftrac[0], 'export', fname+'.md') )


    ftrac = ['dump_analysis', 'dump_gamma',   'dump_hlsvdpro', 'dump_ice_python', \
             'dump_priorset', 'dump_private', 'dump_project',  'dump_pulse', \
             'dump_sandbox',  'dump_siemens', 'dump_simulation' ]

    for fpath in ftrac:
        path_in = Path(fbase, fpath)
        path_out = Path(path_in, 'export')

        if not path_out.exists():
            os.mkdir(path_out)

        fnames = [p for p in Path(path_in).iterdir() if p.is_file()]

        for fname in fnames:
            convert(fname, Path(path_out, fname.name+'.md'))



if __name__ == '__main__':
    _convert_all()
