"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def getUniqueNums(texts, calls):
    allPhones = [*[num[0] for num in texts], *[num[1] for num in texts], *[num[0] for num in calls], *[num[1] for num in calls]]
    return len(set(allPhones))

if __name__ == "__main__":
    print('There are {} different telephone numbers in the records.'.format(getUniqueNums(texts, calls)))