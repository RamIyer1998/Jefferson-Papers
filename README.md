# Jefferson-Papers
Repo for my work on the Jefferson Papers Research Project

Steps to merge the jeff and loc corpora:

1. run `python scraper.py` with a solid internet connection if you need to download the corpus off the library of congress

2. run `bin/jeff.sh`, and it will run the python scripts necessary to build your corpora for model training and generate a csv file containing relevant data regarding the letters

NB: This repository is meant for researchers at the University of Pittsburgh who have access to the proper corpora. The bash script will not run for those who only have the corpus generated from `scraper.py`.


TODO:

1. In case of failure, have the scraper save the last document it downloaded (as well as other relevant information), and exit more gracefully in case of an exception.
