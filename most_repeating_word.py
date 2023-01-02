from operator import itemgetter
from collections import Counter
from collections import defaultdict


def most_repeating_word(words):
    dics = {}
    for word in words:
        dics[words] = Counter(word)

def wordlengthcount(filename):
    output = {}
    with open(filename) as fh:
        for line in fh:
            for word in line.split():
                if word.strip().isalnum():
                    output[len(word)] = output.get(len(word), 0) + 1
    for key, value in output.items():
        print(f'number of {key}-letter words is {value}')


def dictdiff(d1, d2):

    output = {}
    for k in (d1.keys() | d2.keys()):
         if k in (d1.keys() & d2.keys()):
             if d1[k] == d2[k]:
                 continue
             else:
                output[k] = [d1[k], d2[k]]
         else:
            output[k] = [d1.get(k, None), d2.get(k, None)]
    return output


d1 = {'a':1, 'b':2, 'c':3}
d2 = {'a':1, 'b':2, 'c':4}
print(dictdiff(d1, d1))
print(dictdiff(d1, d2))

d3 = {'a':1, 'b':2, 'd':3}
d4 = {'a':1, 'b':2, 'c':4}
print(dictdiff(d3, d4))
d5 = {'a':1, 'b':2, 'd':4}
print(dictdiff(d1, d5))

def mergedicts(*dicts):
    output = {}
    for eachdict in dicts:
        for key, value in eachdict.items():
            output[key] = eachdict[key]
    return output
print(mergedicts(d1,d2, d3,d4))

def multi_update(*args):
    output = {}

    for one_dict in args:
        output.update(one_dict)

    return output
print(multi_update(d1,d2, d3,d4))

def createdict(*args):
    output = {}
    return {k:v for k,v in zip(args[0::2], args[1::2])}
print(createdict('a',1,'b',2))

def fn(k, v):
    if k in "aeiou":
        return True
    return False
def splitdict(d, decidingfn):
    d1 = {}
    d2 = {}
    for k, v in d.items():
        if decidingfn(k,v):
            print(f'{k}')
            d1[k] = v
        else:
            d2[k] = v
    return d1, d2
print(splitdict({'a': 1, 'b': 2, 'c': 4, 'd': 3}, fn))

def sourceips(filename):
    ips = set()
    with open(filename) as fh:
        for line in fh:
            ips.add(line.strip().split()[0])
    return ips

import os
def fileext(directory):
    extnames = set()
    listoffilenames = os.listdir(directory)
    print(listoffilenames)
    for eachfile in os.listdir(directory):
        #print(eachfile)
        if os.path.isfile(os.path.join(directory,eachfile)):
            print(eachfile)
            print(os.path.splitext(eachfile)[-1])
            extnames.add(os.path.splitext(eachfile)[-1])
    print(extnames)



fileext("C:\\Users\\siddh\\Python")


#print(most_repeating_word(['this', 'is', 'an', 'elementary', 'test', 'example']))
#wordlengthcount("textfile.txt")