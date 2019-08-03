#!/bin/bash
source ../env/bin/activate
python3 --version

cd ../src
echo "NOW RUNNING JEFF_CLEANUP.PY"
python3 jeff_cleanup.py

echo "NOW RUNNING XMLCONVERT.PY"
python3 xmlConvert.py "../Jefferson Papers"

echo "NOW RUNNING SEPARATOR.PY"
python3 separator.py

echo "NOW RUNNING MERGE.PY"
python3 merge.py

echo "NOW RUNNING CSVCONVERT.py"
python3 csvConvert.py

echo "NOW RUNNING BOOKS.PY"
python3 books.py

echo "NOW RUNNING CORPORA.PY"
python3 corpora.py

echo "FINISHED"
