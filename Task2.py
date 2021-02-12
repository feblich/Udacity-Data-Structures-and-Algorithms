"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
from collections import defaultdict
from operator import itemgetter
d = defaultdict(int)
for record in calls:
    d[record[0]] += (int(record[3]))
    d[record[1]] += (int(record[3]))

# convert d from defaultdict to d to use operator.itemgetter module
d = dict(d)
maxNumber = max(d.items(), key=itemgetter(1))[0]
maxDuration = max(d.items(), key=itemgetter(1))[1]

print('{} spent the longest time, {} seconds, on the phone during September 2016.'.format(maxNumber, maxDuration))
