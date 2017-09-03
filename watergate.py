#!/usr/bin/env python3 
# -*- coding: utf-8 -*-

#░░░░░▄█▌▀▄▓▓▄▄▄▄▀▀▀▄▓▓▓▓▓▌█ 
#░░░▄█▀▀▄▓█▓▓▓▓▓▓▓▓▓▓▓▓▀░▓▌█ 
#░░█▀▄▓▓▓███▓▓▓███▓▓▓▄░░▄▓▐█▌ 
#░█▌▓▓▓▀▀▓▓▓▓███▓▓▓▓▓▓▓▄▀▓▓▐█ 
#▐█▐██▐░▄▓▓▓▓▓▀▄░▀▓▓▓▓▓▓▓▓▓▌█▌
#█▌███▓▓▓▓▓▓▓▓▐░░▄▓▓███▓▓▓▄▀▐█ 
#█▐█▓▀░░▀▓▓▓▓▓▓▓▓▓██████▓▓▓▓▐█ 
#▌▓▄▌▀░▀░▐▀█▄▓▓██████████▓▓▓▌█▌ 
#▌▓▓▓▄▄▀▀▓▓▓▀▓▓▓▓▓▓▓▓█▓█▓█▓▓▌█▌ 
#█▐▓▓▓▓▓▓▄▄▄▓▓▓▓▓▓█▓█▓█▓█▓▓▓▐█
#Picture : Doge, by Leonardo Doge Vinci
#
## The following script is written in python (3.5.2) by /u/Glorfindel212
# This work is distributed under the CC-BY-NC licence and can hence be modified and communicated as long as the original author is mentioned and the work is not destined for commercial use. (https://en.wikipedia.org/wiki/Creative_Commons_license)

# The following script is written in python (3.5.2) by /u/Glorfindel212


# Imports

import os
import sys  # Import console management module
import praw # Import reddit API
import csv # Import the CSV module to handle the manipulation of CSV documents. Deprecated : see, numpy, pandas.
import json #the json module
import re # Import the regular expression module to parse data
import array # Import the array module to force numeric arrays for one function
import numpy as np # Import the numpy module as part of the pandas module
import pandas as pd #Import the pandas module to handle CSV and data manipulation easily : http://pandas.pydata.org/
pd.options.display.max_rows = 999 #change the console monotiring limit for printing lines to get all results
from datetime import datetime # Import the date-time module 
from pprint import pprint # Pretty print module to visualize data printed in the console for debugging purposes
from pathlib import Path #file path management system module
from random import randint


# Constants

#The default subreddit against which the query will be run
SUBNAME="Politics+EnoughTrumpSpam"
#The string to search for in new posts
TRIGGER="!Watergate"
#final quote file
BOOK="quotes.json"
#temporary csv file
CSV="president.csv"

#elementary console interaction variables
YES = set(['yes','y', 'ye', ''])
NO = set(['no','n'])

#advanced console interaction variables for split decisions (several functions)
CUSTOM=set(['custom','cus','c'])
DEFAULT=set(['default','def','d',''])

#filter interaction variables for the subreddit sorting function (determine_function)
FILTERS=set(['hot','top','best','controversial','new'])


#function list

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

def file_exists(input_file):
    my_file=Path(input_file)
    #test file existence
    if my_file.is_file():
        return True
    else:
        return False

#creates the dataframe that will be used to store values

def create_dataframe(csv_file):
    if file_exists(csv_file):
        pprint('Starting reading of the file : ' + csv_file)
        #reading file
        df = pd.read_csv(csv_file, encoding="utf-8", skiprows=7)
        df.drop('suivi', axis=1, inplace=True)
        df['title'] = np.nan
        # Note = df.loc[df["Type d'annotation"] == 'Surlignement (Jaune)']
        # uprint(Note['Annotation'])
        for index, row in df.iterrows():
            if row["type"] == 'Note':
                df.loc[index-1, 'title'] = row["anno"]
        final = df[df.type == 'Surlignement (Jaune)']
        final.drop('type', axis=1, inplace=True)
        return final
    else:
       print('No quote file found')
       return False

#jsonify this dataframe and put it in a file

def make_json(dataframe, json_file):
    if file_exists(json_file):
        pprint("File found under : " + json_file + ". Replacing content")
        with open(json_file,'w' ) as json_file:
            dataframe.to_json(path_or_buf=json_file, orient="records", encoding='utf-8')
    else:
        pprint("File not already existing, creating it under : " + json_file + "in the current path")
        with open(json_file,'w', encoding='utf-8' ) as json_file:
            dataframe.to_json(path_or_buf=json_file, orient="records")

#read_json

def read_json(json_file):
    if file_exists(json_file):
        with open(json_file, 'r', encoding='utf-8') as file:
            #creates the list item from json
            wow = json.load(file)
        return wow
    pprint("The file doesn't exist")
    return False

def random_gen(max_range):
    return  randint(0,max_range-1)

def draft_quote():
    return True

#Formating variables

space = " "
spacer = "---"
line = "\n"
double_line = "\n\n"
comma=", "
quotation_mark = ">"
title = "**All the President's Men**"
title_mark = "# "
authors = "by *Woodward & Bernstein*"
editor = "[Simon & Schuster; Reissue edition (November 1, 2007) ISBN-13: 978-1476770512]"
endquote = "[Buy the book](https://www.amazon.com/All-Presidents-Men-Bob-Woodward/dp/1476770514/ref=pd_lpo_sbs_74_t_1?_encoding=UTF8&psc=1&refRID=EQMM2F6C7NR1243Y25CH) | [See the code](https://github.com/Glorfindel21/watergate-bot) | Draw me a sketch ^(please the sketch guy is gone) |  [Suggestions to my creator](https://www.reddit.com/user/Glorfindel212)"

# authentication

def main():

    quotes = read_json('quotes.json')

    # quotes = create_dataframe(CSV)

    # json = make_json(quotes, BOOK)

#identification intel found in another file : reddit.id.bots (for security)
#This is a test for commiting.

    subreddit = reddit.subreddit(SUBNAME)
    for comment in subreddit.stream.comments():
        if TRIGGER in comment.body:
            print("Found one !")
            number = random_gen(len(quotes))
            full_post=title_mark+quotes[number]['title']+double_line+spacer+double_line+quotation_mark+quotes[number]['anno']+double_line+spacer+double_line+quotes[number]['empla']+comma+title+comma+authors+comma+editor+double_line+endquote
            comment.reply(full_post)

if __name__ == '__main__':
    main()