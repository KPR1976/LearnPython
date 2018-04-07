#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -DONE Extract all the text from the file and print it
 -DONE Find and extract the year and print it
 -DONE Extract the names and rank numbers and just print them
 -DONE Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  file = open(filename, mode='r')
  text = file.read() # read text of file
  #Find and extract the year and print it
  matchyear = re.search('(Popularity in) (\d\d\d\d)', text)
  #print(matchyear.group(2))
  #Extract the names and rank numbers and just print them
  #Get the names data into a dict and print it
  matchname = re.findall('(<tr align="right"><td>)(\d+)(</td><td>)(\w+)(</td><td>)(\w+)', text)
  #print(matchname)
  namedict = {}
  for match in matchname:
      print(match[1] + ' ' + match[3] + ' ' + match[5])
      namedict[match[3]] = match[1]
      namedict[match[5]] = match[1]
  print(namedict)
  #Build the [year, 'name rank', ... ] list and print it
  finallist = [matchyear.group(2)]
  for key, value in namedict.items():
      name = key
      number = value
      tolist = key + ' ' + value
      finallist.append(tolist)
  print(finallist)
  return


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  extract_names(args[0])

if __name__ == '__main__':
  main()
