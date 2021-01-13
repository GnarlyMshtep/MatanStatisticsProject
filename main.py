from dataSet import dataSet
import utils


x = dataSet(utils.stringToList("""
43.6
47.8
53.8
56.9
62.9
67.2
70.8
76.2
54.1
56.5
53.5
46
58.2
78.6
62
66.7
60
58
55.6
56
56.3
45
64.4
50.6
68
56
78.6
56.9
64
78.6
63.1
63.5
51.7
75
71.8

"""))
print(x.getStdDeviation())
print(x.getExtremas())
print(x.getMeanMedianMode())
