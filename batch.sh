#!/bin/sh
curl https://data.nhi.gov.tw/resource/mask/maskdata.csv  > remain.csv
python data.py