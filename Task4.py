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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def getTelemarketers(calls, texts):
    callers = list(set([record[0] for record in calls]))
    callReceivers = list(set([record[1] for record in calls]))
    texters = list(set([record[0] for record in texts]))
    textReceivers = list(set([record[1] for record in texts]))

    # create boolean vectors
    idx0 = [caller in callReceivers for caller in callers]
    idx1 = [caller in texters for caller in callers]
    idx2 = [caller in textReceivers for caller in callers]
    teleMarketers = []
    for i in range(len(callers)):
        if not any([idx0[i], idx1[i], idx2[i]]):
            teleMarketers.append(callers[i])

    return teleMarketers


if __name__ == '__main__':
    teleMarketers = getTelemarketers(calls, texts)
    teleMarketers.sort()

    print('\nThese numbers could be telemarketers: ')
    for t in teleMarketers:
        print(t)