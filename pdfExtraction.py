"""
THIS IS THE MAIN FILE. IN ORDER TO RUN THE PROGRAM, PLEASE RUN THIS FILE.

Important Notes to Run the Program:
- Written in Python 3.9, may not work as intended on earlier versions
- Requires packages os, spacy, csv, re, and pdfplumber

What this file does:
Takes in a folder of resumes called "in_resume_samples" within the current working directory,
splits them into readable strings, searches for names and emails using regex, as well as programming languages using
spaCy with match patterns imported from matchPatterns.py.
Exports that data to a csv file named "resumeInfo" in the same current working directory.

Additional Notes:
- There are quite a few comments on what could be improved, as this is a work in progress.
- For more information, please refer to README.md and matchPatterns.py
"""

import os
import spacy
import csv
import re
import pdfplumber
from spacy.matcher import Matcher
import matchPatterns

# instance variables to store the string representation of the resumes,
# as well as the names, emails, and programming languages extracted from each resume
allResumeContent = []
names = []
emails = []
languagesLikelyKnown = []


# Opens every resume, pulls out text page by page, and adds each pdf's content to allResumeContent
for files in os.listdir("./in_resume_samples"):
    # using pdfplumber to extract data from pdf
    with pdfplumber.open('./in_resume_samples/' + files) as pdf:
        text = ""
        # iterating through pages and extracting text
        for p in pdf.pages:
            text += p.extract_text()
        # adding text to allResumeContent List
        allResumeContent.append(text)


# Finds the name of every applicant, since this template has the name on the first line,
# just split the text line by line and return the first value
# NOTES:
# - there is likely a more efficient way to do this that does not involve splitting every line,
#   rather only the first instance, but did not have time to find a faster way
# - Could run into errors with other templates as this only uses the first line to find the name
for resume in allResumeContent:
    # split by new line
    resume_line_by_line = re.split(r'\n', resume)
    # checks to see if PDF was blank
    if resume_line_by_line:
        # adds name to list of names
        names.append([resume_line_by_line[0]])
    else:
        # otherwise adds an empty name to the list
        names.append([])


# Finds the first email in each pdf document using regex
# NOTES:
# - there is also definitely a faster way to do this; you could stop the regex after finding the
#   first matching occurrence. Attempted to do this with matcher objects, but failed and ran out of time to debug
# - Could run into errors with other templates as this finds only the first email
for resume in allResumeContent:
    # finds emails in file using regex
    resume_emails = re.findall(r"\S*@\S*[.][a-z]{2,3}", resume)
    # if an email was found, adds email to list of emails. otherwise, adds empty array to list of emails
    if resume_emails:
        emails.append([resume_emails[0]])
    else:
        emails.append([])


# loads spacy english pipeline and generates a Matcher object
nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

# passes matcher into a function in the "matchPatterns" file that
# generates programming language patterns for spacy tokens
matchPatterns.generateProgrammingLanguageMatchPatterns(matcher)

# Iterates through every resume and matches with tokens. Stores these tokens in a set to avoid duplicates,
# then turns them into a list to store in the outer scope's 2-d array of languages known per applicant
for resume in allResumeContent:
    # processes the doc
    doc = nlp(resume)
    # creates a temporary set to store the languages known
    tempSetOfLanguages = set()
    # stores the languages known into the temp set
    for match_id, start, end in matcher(doc):
        string_id = nlp.vocab.strings[match_id]
        tempSetOfLanguages.add(string_id)
    # turns temp set into list and adds to outer scope's list of languagesLikelyKnown
    languagesLikelyKnown.append(list(tempSetOfLanguages))


# writing name, email, and programming language information to CSV file called "resumeInfo"
with open('resumeInfo.csv', 'w', newline='') as f:
    # creates csv writer object
    w = csv.writer(f)
    # writes column titles
    w.writerow(['Name', 'Email', 'Programming Languages Known'])
    # write to rows individually, iterating by index
    for index in range(len(allResumeContent)):
        if len(languagesLikelyKnown[index]):
            w.writerow([' '.join(names[index]), ' '.join(emails[index]), languagesLikelyKnown[index]])
        else:
            w.writerow([' '.join(names[index]), ' '.join(emails[index])])

