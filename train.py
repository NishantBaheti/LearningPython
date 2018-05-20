#!/usr/bin/python3

# apple & orange -texture ,weight 
from sklearn import tree
import sys
import time



#inn=sys.argv
#w=int(inn[1])
#q=int(inn[2])
#	print(w,q)

features=[[110,0],[120,0],[130,1],[140,1]]
# smooth =0	, bumpy=1
output=["apple","apple","orange","orange"]

#now loading decision tree classifier	
while True:

	algo  =  tree.DecisionTreeClassifier()

#now training the feature and output set


	trained=algo.fit(features,output)	#recommended core 1 --
#testing trained model 

	resoutput=trained.predict([[121,1]])

#printing result
	print(resoutput)
	time.sleep(1)
