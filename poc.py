import csv
import pandas as PD

#mylines = []                              # Declare an empty list
#with open ('/Users/ftucci/Downloads/todoist/testinput.txt', 'rt') as myfile:  # Open lorem.txt for reading text.
#    for line in myfile:                   # For each line of text,
#        mylines.append(line)              # add that line to the list.
#    for element in mylines:               # For each element in the list,
#        print(element)                    # print it.

df = PD.read_fwf('/Users/ftucci/Downloads/todoist/testinput.txt')
df.to_csv('/Users/ftucci/Downloads/todoist/testinput.csv')