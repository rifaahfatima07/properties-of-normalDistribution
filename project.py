import pandas as pd
import statistics
import plotly.figure_factory as ff

df = pd.read_csv("Data.csv")
data = df["Weight(Pounds)"].tolist()

average = statistics.mean(data)
deviation = statistics.stdev(data)


range1_start, range1_end = average-1*deviation, average+1*deviation
range2_start, range2_end = average-2*deviation, average+2*deviation
range3_start, range3_end = average-3*deviation, average+3*deviation

BellCurve = ff.create_distplot([data], ["Weights"], show_hist=False)
BellCurve.show()

range1_array = []
for x in data:
    if x > range1_start and x < range1_end:
        range1_array.append(x)


range2_array =[]
for y in data:
    if y > range2_start and y < range2_end:
        range2_array.append(y)


range3_array = []
for z in data:
    if z > range3_start and z < range3_end:
        range3_array.append(z)



range1_percentage = len(range1_array)*100/len(data)
range2_percentage = len(range2_array)*100/len(data)
range3_percentage = len(range3_array)*100/len(data)

print(range1_percentage)
print(range2_percentage)
print(range3_percentage)