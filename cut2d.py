import math				# for ceil
import itertools	# for permutation iterator
import copy				# for deepcopying Bins
import sys				# for exit
from time import clock, time # for timing


# FORK FROM https://github.com/type/Bin-Packing/blob/master/binpacking.py

class Cut2D:

    def __init__(self):
        # Get the capacity for the bins from the user
        self.cap = 100
        self.allItems = [1, 2, 3]
        self.items = sorted(self.allItems)
        self.bigItem = self.items.pop()  # We can reduce time by a factor of 2 by always putting the same item in bin0
        self.maxBins = len(self.allItems)
        self.minBins = int(math.ceil(sum(self.allItems) / self.cap))
        self.curMin = self.maxBins + 1
        self.config = []

    def easyCase(self, aList):
        for item in aList:
            if item < self.cap / 2:
                return False
        return True

    def checkInput(self, aList):
        for item in aList:
            if item > self.cap:
                print
                "SOME ITEM WON'T EVEN FIT IN ITS OWN BIN! ABORTING"
                sys.exit()

    def permutations(self, itens):
        return itens

    def execute(self):
        # Begin timing
        t1 = clock()

        # Make sure no item is too large
        self.checkInput(self.allItems)

        # Check if we're in the case where all items need their own bins
        if self.easyCase(self.allItems):
            print("Easy case")
            self.curMin = len(self.allItems)
            for item in self.allItems:
                self.config.append([item])
        else: