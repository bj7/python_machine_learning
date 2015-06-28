#adapted from Machine Learning in Python: Essential Techniques for Predictive Analysis
__author__ = 'josh_bernitt'
import urllib.request
import sys

#read data from uci data repository
target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
"databases/undocumented/connectionist-bench/sonar/sonar.all-data")

#pull data and convert to ascii characters
data = urllib.request.urlopen(target_url)
bytes = data.read()
datastr = bytes.decode("utf8")
data.close()

#write data to text file
text_file = open("output.txt", "w")
text_file.write(datastr)
text_file.close()

#read text file in as seperate lines 
text_file = open("output.txt", "rt")
datatxt = text_file.read().splitlines()
text_file.close()

#arrange data into list for labels and list of list for attributes
xList = []
labels = []
for line in datatxt:
    #split on comma
    row = line.strip().split(",")
    xList.append(row)

sys.stdout.write("Number of Rows of Data = " + str(len(xList)) + '\n')
sys.stdout.write("Number of Columns of Data = " + str(len(xList[1])) + '\n')
