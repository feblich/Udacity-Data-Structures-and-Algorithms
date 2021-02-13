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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.


Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

# part A
# get all numbers called by Bangalore
def getNumbersCalledByBangalore():
    # create a dictionary keyed on calling numbers and valued on receiving numbers
    from collections import defaultdict
    d = defaultdict(list)
    for record in calls:
        d[record[0]].append(record[1])

    # extract numbers called by Bangalore
    d = dict(d)
    numbersCalledByBangalore = []
    for k, v in d.items():
        if k.startswith('(080)'):
            numbersCalledByBangalore.append(v)

    # flatten the list
    return [number for listOfNums in numbersCalledByBangalore for number in listOfNums]

numbersCalledByBangalore = getNumbersCalledByBangalore()

# get codes of numbers called by Bangalore:
def areaCodeExtractor(num):
    # check fixed number:
    if num.startswith("("):
        areaCode = num[num.find("("):num.find(")") + 1]

    # check mobile number:
    if num.startswith(("7", "8", "9")) and ' ' in num:
        areaCode = num[0:5]

    # check telemarketers number:
    if all(x not in num for x in ["(", ")", " "]) and num.startswith('140'):
        areaCode = num[0:3]

    return areaCode


# extract area codes:
areaCodes = []
for num in numbersCalledByBangalore:
    areaCodes.append(areaCodeExtractor(num))

areaCodes = set(areaCodes)

print('The numbers called by people in Bangalore have codes: \n {}'.format(areaCodes))
