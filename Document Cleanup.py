import os
import time
from datetime import datetime
from datetime import timedelta

import pprint

docPath = str(os.environ['HOMEDRIVE']) + str(os.environ['HOMEPATH']) + '\Documents'
docArchive = str(os.environ['HOMEDRIVE']) + str(os.environ['HOMEPATH']) + '\Documents' + '\Archive'
downPath = str(os.environ['HOMEDRIVE']) + str(os.environ['HOMEPATH']) + '\Downloads'
downArchive = str(os.environ['HOMEDRIVE']) + str(os.environ['HOMEPATH']) + '\Downloads' + '\Archive'
daysBack = 5
currentDate = datetime.date(datetime.now())
dateBack = datetime.date(datetime.now() - timedelta(days=daysBack))

#pprint.pprint(dict(os.environ), width=1)
print(docPath)
os.chdir(docPath)

print(str(currentDate))
print(str(dateBack))
print(str(docArchive))

# check for existence of archive folder
#def ensure_dir(file_path):
directory = os.path.dirname(docArchive)
if not os.path.exists(docArchive):
    print('No archive ' + str(docArchive))
    os.makedirs(docArchive)




for file in os.listdir(docPath):
    # Archive CSV files

    if file.endswith(".csv"):
        if datetime.fromtimestamp(os.path.getmtime(file)).date() < dateBack:

            print(datetime.fromtimestamp(os.path.getmtime(file)).strftime('%Y-%m-%d'))
            print(type(datetime.fromtimestamp(os.path.getmtime(file))))
            print(dateBack)
            print(type(dateBack))
         #if datetime.date(os.path.getmtime(file)) < dateBack:
         #   print(os.path.join(docPath, file) + ' -- ' + datetime.fromtimestamp(os.path.getmtime(file)).strftime('%Y-%m-%d %H:%M:%S'))



