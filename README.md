# Jefferson-Papers
Repo for my work on the Jefferson Papers Research Project

Steps to merge the jeff and loc corpora:

1. run `python scraper.py` with a solid internet connection if you need to download the corpus off the library of congress

2. run `python jeff_cleanup.py` provided you have the jeff corpus in your directory

3. run `python xmlConvert.py "Jefferson Papers"`

4. run `python separator.py`

5. run `python merge.py`