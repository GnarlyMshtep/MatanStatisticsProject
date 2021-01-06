from dataSet import dataSet
import utils

y = utils.stringToList("""
32	2
37	1
42	3
47	3
52	8
57	12
62	14
67	17
72	13
""")

x = dataSet(utils.frequencyToStandard(y))

print(x.getMeanMedianMode())
