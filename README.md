# ButlerLabsMiniProject

What this program does:

Takes in a folder of resumes called "in_resume_samples" within the current working directory, splits them into readable strings, searches for info using regex and spaCy (their name, email, and what coding languages they likely know), and exports that data to a csv file named "resumeInfo" in the same current working directory.

Files in this program:
- pdfExtraction.py - Extracts information from pdf's and exports data to csv file.
- matchPatterns.py - Defines match patterns, utilizing spaCy tokens, in order to locate programming languages.
More information can be found about both of these files within the files themselves.

Important Notes to Run the Program:
- Written in Python 3.9, may not work as intended on earlier versions
- Requires packages os, spacy, csv, re, and pdfplumber
- the main file is pdfExtraction, to run the program run pdfExtraction.py
- the program grabs files from the provided folder "in_resume_samples" with some pdf's already present. If you wish to add   more resumes, please add them in that folder.

Additional Notes:

There are quite a few comments on what could be improved, as this is a work in progress. 
Could additionally add more data fields, or train a model to better predict what is and what isn't a name (in order to accept more resume templates). 
Could pursue training a model to determine what is or isn't a coding language. (I briefly looked into training models using the youtube video linked below but did not have time to implement it, nor time to collect the volume of data necessary)

Sources: 
regex review + basic spaCy:
- https://realpython.com/natural-language-processing-spacy-python/#visualization-using-displacy
- https://www.youtube.com/watch?v=KL4-Mpgbahw

exporting to CSV:
- https://www.youtube.com/watch?v=s1XiCh-mGCA

list of programming languages:
- https://www.whoishostingthis.com/resources/programming/
