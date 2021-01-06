import bisect  # to insert in sorted list
import utils
from math import ceil, floor


"""
to implement list:
1) how many in certain class range (what's the frequencyt and cumalative frequency) (class range our set based on user specs)
2) leaf plot creator (dict returned)

"""
from typing import Iterable


class dataSet:
    def __init__(self, dataSet: Iterable):
        if isinstance(dataSet, Iterable):
            # clean up empties and irregulerities

            self.data = sorted(dataSet)
            self.len = len(self.data)
            # figured I'll just sort it once and have that gurrentee

    def leafPlot(self) -> dict:  # works!
        temp = {}
        for dataEntry in self.data:
            firstDigit = int(str(dataEntry)[0])
            if firstDigit not in temp.keys():
                print(firstDigit)
                # probably should be an array so dataEntry can sort
                temp[firstDigit] = []
            for digit in str(dataEntry)[1:]:
                utils.insort(temp[firstDigit], int(digit))

        return temp

    # this is not fully functional, will give trouble when upper and lower messurments for the quartile vary (I belive)
    def getQuarrtiles(self) -> dict:
        temp = {'25th': self.data[int(.25*(
            self.len+1))], 'Mode': self.data[int(.5*(self.len+1))], '75th': self.data[int(.75*(self.len+1))]}
        temp['IQR'] = temp['75th'] - temp['25th']

        return temp

    def getPrecentileOfElement(self, item):
        below = 0
        equalTo = 0
        if item not in self.data:
            return False
        for el in self.data:
            if el < item:
                below += 1
            elif el == item:
                equalTo += 1
            else:
                break

        return {'bestApproximation': [round(100*((below+.5*equalTo)/self.len)), (100)*(below+.5*equalTo)/self.len], 'fromBelow': (below/self.len)*100, 'fromAboveAndEqual': 100-((equalTo + self.len-equalTo-below)/self.len)*100}

    def getElementByPrecentileDEPRACATED(self, precentile) -> dict:
        x = {'fromBelow': self.data[floor(.5*(self.len+1))],
             'fromAbove': self.data[ceil(.5*(self.len+1))]}
        x['Avrage'] = (x['fromBelow'] + x['fromAbove'])/2

        return x
    # the first element is #1 not 0
    # when we get an integer index we don't round up we avrage the above and below value

    def getElementByPrecentile(self, precentile):
        fPrec = precentile/100
        ret = {}
        print(fPrec*(self.len), isinstance(fPrec*(self.len), int))
        if (fPrec*(self.len)).is_integer():
            ret['locator'] = fPrec*(self.len)+.5

        else:
            ret['locator'] = ceil(
                fPrec*(self.len))

        if not isinstance(ret['locator'], int):
            ret['value'] = (self.data[floor(ret['locator']-1)] +
                            self.data[ceil(ret['locator']-1)])/2
        else:
            ret['value'] = self.data[ret['locator']-1]
        ret['note'] = "begining to count from element 0"
        return ret

    def getMean(self) -> float:
        sum(self.data)/len(self.data)

    def getALotOfInfo(self) -> dict:
        pass
    # def displayalotofinfo

    def getOutliers(self) -> list:
        quartInfo = self.getQuarrtiles()
        x = 1.5*quartInfo['IQR']
        lowerRange = quartInfo['']

        return [element for element in self.data if element < (quartInfo['25th']-x) or element > quartInfo['75th']+x]

    def getExtremas(self):
        return self.data[0], self.data[self.len]
