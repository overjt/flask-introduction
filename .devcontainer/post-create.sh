#!/bin/bash
pip3 install -r requirements.txt
cd app && python -c '
from app import db
db.create_all()
exit()
'