#! /usr/bin/env python3
from __future__ import print_function, division

import argparse
import csv
import os.path
import re
import textwrap

def get_rid_of_numbers(ss):
    ss = ss.replace('1', 'One')
    ss = ss.replace('2', 'Two')
    ss = ss.replace('3', 'Three')
    ss = ss.replace('4', 'Four')
    ss = ss.replace('5', 'Five')
    ss = ss.replace('6', 'Six')
    ss = ss.replace('7', 'Seven')
    ss = ss.replace('8', 'Eight')
    ss = ss.replace('9', 'Nine')
    return ss

def get_cmyk_values():
    csv_file_name = os.path.join(args.colorbrewer, 'cb.csv')
    with open(csv_file_name) as csv_file:
        cynthia = csv.DictReader(csv_file)

        # ColorName,NumOfColors,Type,CritVal,ColorNum,ColorLetter,C,M,Y,K,SchemeType
        colors = list()
        ranges = list()

        for row in cynthia:

            if row['ColorName']:
                this_range = get_rid_of_numbers(row['ColorName'])
                if this_range not in ranges:
                    ranges.append(this_range)

            if row['NumOfColors']:
                this_size = row['NumOfColors']

            colors.append('{}[{}][{}] = 1/100 ({},{},{},{});'.format(
                this_range, this_size, row['ColorNum'], row['C'], row['M'], row['Y'], row['K'])
                         )

    return colors, ranges

def is_int(n):
    "Is this a dagger?"
    try:
        a = int(n)
    except:
        return False
    return True

def get_rgb_values():
    js_file_name = os.path.join(args.colorbrewer, 'colorbrewer_schemes.js')

    colors = list()
    ranges = list()
    with open(js_file_name) as js:
        for line in js:
            m = re.match(r'^([A-Za-z0-9]+):\s*({.*})\s*,?$', line)
            if m is  None:
                continue
            this_range = get_rid_of_numbers(m.group(1))
            ranges.append(this_range)
            details = eval(m.group(2))

            for k in details:
                if is_int(k):
                    for i, v in enumerate(details[k]):
                        if v.startswith('rgb('):
                            colors.append('{}[{}][{}] = 1/256 {};'.format(this_range, k, i+1, v[3:]))

    return colors, ranges


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--colorbrewer",
                        help="Directory for local copy of the Axel Maps Colorbrewer project")
    parser.add_argument("-r", "--rgb", action="store_true", help="Create RGB colors, not CMYK")

    args = parser.parse_args()

    if args.rgb:
        colors, ranges = get_rgb_values()
    else:
        colors, ranges = get_cmyk_values()

    print('''% This package includes color specifications and designs
% developed by Cynthia Brewer (http://colorbrewer.org/).
% Metapost version adapted from cb.csv by Toby Thurston.
% Please see license at http://colorbrewer.org/export/LICENSE.txt

% This package defines all the colours from colorbrewer.org
% Visit the site to get an idea what you can do with them
% Each colour set is defined as a MP variable with two suffixes
% The first suffix defines the number of colours in the set,
% the second one defines the index of this colour in the set
% starting at 1, so this loop shows you all the shades of red
% in the six colour "Reds" set.
%
% for i=1 upto 6:
%   fill unitsquare scaled 1cm shifted (i*cm,0) withcolor Reds[6][i];
% endfor
%
% Six of the qualititative colour sets have numbers in their names at colorbrewer.org
% MP doesn't allow this, so they are renamed here as follows:
%
% Dark2   is called DarkTwo
% Pastel1 is called PastelOne
% Pastel2 is called PastelTwo
% Set1    is called SetOne
% Set2    is called SetTwo
% Set3    is called SetThree
%
% No sequence has fewer than three colours.
% All of the sequences are defined for upto eight colours.
% The sequential sequences are defined for 3 to 9 colours each.
% The divergent sequences are defined for 3 to 11 colours each.
% A few of the qualitative sequences have upto 12 colours.
%
% In general try not to use too many colours in one chart.
% The sequences were designed for cartography and may not suit all applications.

message "metapost-colorbrewer - Copyright (C) 2018 Toby Thurston. This program comes with ABSOLUTELY NO WARRANTY. " &
"This is free software, and you are welcome to redistribute it under certain conditions; read the LICENCE file for details. " &
"The colorbrewer colours are copyright (C) Cynthia Brewer, Mark Harrower and The Pennsylvania State University. " & 
"See http://colorbrewer2.org";

    ''')


    if args.rgb:
        out = "color "
    else:
        out = "cmykcolor "

    out = out + ', '.join('{}[][]'.format(x) for x in sorted(ranges)) + ';'

    rapper = textwrap.TextWrapper(subsequent_indent = '    ', width = 72)
    print('\n'.join(rapper.wrap(out)))

    print("")

    for c in sorted(colors):
        print(c)
