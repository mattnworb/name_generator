#!/usr/bin/env python
import csv
import random
import argparse

class WeightedName:
    def __init__(self, name, weight):
        self.name = name
        self.weight = float(weight)

class NameCollection:
    def __init__(self, names):
        self.names = names
        self.count = len(names)
        self.sum_weights = sum((name.weight for name in names))

    
    def choose(self):
        """Chooses a name from the collection at random, based on the weights"""
        remaining = self.sum_weights
        for wname in self.names:
            r = random.random()
            this_prob = wname.weight / remaining
            #print "Weight %0.02f, remaining %0.02f, this_prob %0.02f, r %0.02f" % (wname.weight, remaining, this_prob, r)
            if r <= this_prob:
                return wname.name
            remaining = remaining - wname.weight


def read_file(filename):
    """
    Reads CSV file at filename and returns a NameCollection where each row is one WeightedName.

    The first column in the CSV must be the names, and the second column must be the weights (in any format/range). Any other columns in the CSV are ignored.
    """
    with open(filename, 'rb') as f:
        reader = csv.reader(f)
        return NameCollection([WeightedName(row[0], row[1]) for row in reader if len(row) >= 2])


def normalize(name):
    return name[0].upper() + name[1:].lower()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generates random names.', epilog='The CSV files must contain a name in the first column and a weight in the second column. The weights can be in any format/range as long as they are positive numbers; the math works out the same if a weight of 10% is expressed as "10" or "0.10".')

    parser.add_argument('firstnames', help='Path to CSV file of first names')
    parser.add_argument('lastnames', help='Path CSV file of last names')
    parser.add_argument('num', help='Optional, number of names to generate (default=1)', type=int, metavar='N', nargs='?', default=1)

    args = parser.parse_args()

    fnames = read_file(args.firstnames)
    lnames = read_file(args.lastnames)

    for i in xrange(args.num):
        first = normalize(fnames.choose())
        last = normalize(lnames.choose())
        print "%s %s" % (first, last)
