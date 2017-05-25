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


import os
# Import console management module
import sys
# Import reddit API
import praw
# Import the CSV module to handle the manipulation of CSV documents. Deprecated : see, numpy, pandas.
import csv
# Import the regular expression module to parse data
import re
# Import the array module to force numeric arrays for one function
import array
# Import the numpy module as part of the pandas module
import numpy as np
#Import the pandas module to handle CSV and data manipulation easily : http://pandas.pydata.org/
import pandas as pd
#change the console monotiring limit for printing lines to get all results
pd.options.display.max_rows = 999
# Import the date-time module to handle date formats in a readable way (from timestamp to human-readable time)
from datetime import datetime
# Pretty print module to visualize data printed in the console for debugging purposes
from pprint import pprint
#file path management system module
from pathlib import Path