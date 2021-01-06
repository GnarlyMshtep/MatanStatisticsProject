from dataSet import dataSet
import utils

x = dataSet(utils.stringToList("""

2	5	9	14
"""))

print(x.getMeanMedianMode())
