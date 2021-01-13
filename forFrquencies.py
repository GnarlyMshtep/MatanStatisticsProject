from dataSet import dataSet
import utils

y = utils.stringToList("""
50                       2

51                       4

52                       4

53                       6

54                       4
""")

x = dataSet(utils.frequencyToStandard(y))

print(x.getMeanMedianMode())
