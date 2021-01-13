import bisect  # to insert in sorted list
import utils
from math import ceil, floor, sqrt

# for plotting
import matplotlib.pyplot as plt


"""
to implement list:
1) how many in certain class range (what's the frequencyt and cumalative frequency) (class range our set based on user specs)
2) leaf plot creator (dict returned)

"""
from typing import Iterable

# COULD MAKE ANY UNIT A SUBCLASS


class dataSet:  # allow initialization as frequency table?
    def __init__(self, dataSet: Iterable):
        if isinstance(dataSet, Iterable):
            # clean up empties and irregulerities

            self.data = sorted(dataSet)
            self.len = len(self.data)
            # figured I'll just sort it once and have that gurrentee
# UNIT 1:

    def stemPlot(self) -> dict:  # works!
        temp = {}
        for dataEntry in self.data:
            firstDigit = int(str(dataEntry)[0])
            if firstDigit not in temp.keys():
                # probably should be an array so dataEntry can sort
                temp[firstDigit] = []
            for digit in str(dataEntry)[1:]:
                utils.insort(temp[firstDigit], int(digit))

        return temp


# UNIT 2: DESCRIPTIVE STATICS
    # this is not fully functional, will give trouble when upper and lower messurments for the quartile vary (I belive)


    def getQuarrtiles(self) -> dict:
        temp = {'25th': self.getElementByPrecentile(25)['value'], 'Median': self.getElementByPrecentile(
            50)['value'], '75th': self.getElementByPrecentile(75)['value']}
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
        if (fPrec*(self.len)).is_integer():
            ret['locator'] = fPrec*(self.len)+.5

        else:
            ret['locator'] = ceil(
                fPrec*(self.len))

        ret['value'] = (self.data[floor(ret['locator']-1)] +
                        self.data[ceil(ret['locator']-1)])/2

        ret['note'] = "begining to count from element 0"
        return ret

    def getMeanMedianMode(self) -> float:
        temp = {}

        temp['Mean'] = round(sum(self.data)/len(self.data), 4)
        temp['Median'] = self.getQuarrtiles()['Median']
        temp['Mode'] = self.getMode()
        return temp

    def getFrequencyTable(self):
        temp = {}
        for el in self.data:
            if el not in temp.keys():
                temp[el] = 1
            else:
                temp[el] += 1
        return temp

    def getMode(self):  # this is pretty sub-par considerign the list is sorted
        max = -1
        modes = []
        table = self.getFrequencyTable()
        for key in table.keys():
            if table[key] > max:
                modes.clear()
                modes.append(key)
                max = table[key]
            elif table[key] == max:
                modes.append(key)

        return {'modes': modes, 'frequency': max}

    def getALotOfInfo(self) -> dict:
        pass
    # def displayalotofinfo

    def getOutliers(self) -> list:
        quartInfo = self.getQuarrtiles()
        x = 1.5*quartInfo['IQR']

        return [element for element in self.data if element < (quartInfo['25th']-x) or element > quartInfo['75th']+x]

    def getExtremas(self):  # and range
        return {'Min': self.data[0], 'Max': self.data[self.len-1], 'Range': self.data[self.len-1] - self.data[0]}

    def getBoxPlot(self) -> dict:
        quarts = self.getQuarrtiles()
        ext = self.getExtremas()
        return {'min': min(self.data), '25th': quarts['25th'], 'Median': quarts['Median'], '75th': quarts['75th'], 'max': max(self.data)}

    def getStdDeviation(self):
        x = self.getMeanMedianMode()["Mean"]
        temp = sqrt(sum(((element-x)**2 for element in self.data)))
        return {'Population': round(temp/sqrt(self.len), 5),
                'Sample': round(temp/sqrt(self.len-1), 5),
                'SampleVariance': round((sum(((element-x)**2 for element in self.data)) / (self.len-1)), 5),
                'PopulationVariance': round((sum(((element-x)**2 for element in self.data)) / self.len), 5)}

    # how many stds from mean?: sorry for unredability I'm a golfer 😎
    def getZScore(self, value, isSample=True) -> float:
        return round((value-self.getMeanMedianMode()["Mean"])/self.getStdDeviation()[('Sample' if isSample else 'Population')], 5)

    # add more initialization arguments like the range and stuff
    def createHistogramPlot(self, binNumber):
        i = 0
        bins = []
        while 10+5*i <= max(self.data):
            bins.append(10+5*i)
            i += 1

        plt.hist(self.data, bins=bins, range=(10, self.getExtremas()[
                 "Max"]),  facecolor='green', edgecolor='black', rwidth=5)
        #bins=binNumber or self.len
        plt.title('histogram of data')
        plt.xlabel('pinkie lengths in cm')
        plt.ylabel('number of pinkies messured of each category')
        plt.grid(axis='y', alpha=0.75)

        classWidth = round((max(self.data)-min(self.data)) /
                           (binNumber or self.len), 1)

        plt.xticks(
            bins)

        plt.show()

    def createLinePlot(self):
        """
        plt.plot(self.data, [0]*31, marker='x', linewidth=0,
                 markersize=5, markerfacecolor='blue')
        plt.title("plot on a number line")
        plt.show()
        """
        freqTable = self.getFrequencyTable()
        sizes = [freqTable[el]*10 + 2 for el in self.data]
        fig = plt.figure()
        ax = fig.gca()
        ax.scatter(self.data, [0]*self.len, s=sizes, color='red')
        plt.show()

# END OF UNIT 2 DESCRIPTIVE STATISTICS
