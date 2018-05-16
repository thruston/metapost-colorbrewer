#! /usr/bin/env python3

import argparse
import csv
import sys

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--csv_file_name", default="cb.csv", help="The csv file from the Color Brewer project")
    args = parser.parse_args()

    with open(args.csv_file_name) as csv_file:
        cynthia = csv.DictReader(csv_file)

        # ColorName,NumOfColors,Type,CritVal,ColorNum,ColorLetter,C,M,Y,K,SchemeType
        colors = list()
        ranges = list()
        for row in cynthia:
            
            if row['ColorName']:
                current_range = get_rid_of_numbers(row['ColorName'])
                if current_range not in ranges:
                    ranges.append(current_range)

            if row['NumOfColors']:
                current_size = row['NumOfColors']

            colors.append('{}[{}][{}] = 1/100 ({},{},{},{});'.format(
                current_range, current_size, row['ColorNum'], row['C'], row['M'], row['Y'], row['K'])
                )


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
        ''')

        out = "cmykcolor "
        
        for r in ranges:
            out = out + "{}[][]".format(r) + ', '
            if len(out) > 64:
                print(out)
                out = '    '
        if len(out) > 4:
            print(out.rstrip().strip(',') + ';')

        print()
        for c in colors:
            print(c)
