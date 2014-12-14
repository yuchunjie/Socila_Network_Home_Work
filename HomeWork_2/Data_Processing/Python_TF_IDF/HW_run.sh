#!/bin/sh
echo "compute the TF"
python ./get_TF.py
echo "compute the IDF"
python ./get_IDF.py
echo "produce the TF-IDF"
python ./get_TF-IDF.py
echo "compute the words weight for hot issuess"
python ./get_words_weight.py
echo "produce the issues score"
python ./check_issue_score.py
