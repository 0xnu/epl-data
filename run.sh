#!/usr/bin/env bash
#chmod +x run.sh && ./run.sh

# Process Data
python3 epl.py && python3 convert.py

# Push to repository
git add .
git commit -s -m "epl data"
git push
echo "I am done processing data. Bye!"