import numpy as np
import pandas as pd
Number_of_courses= int(input("Number of courses:"))

def Points(x):
	if x<= 39:
		data['points'].append(0)
	elif x >=40 and x<=44:
		data['points'].append(1)
	elif x >=45 and x<=49:
		data['points'].append(2)
	elif x>=50 and x<=59:
		data['points'].append(3)
	elif x>=60 and x<=69:
		data['points'].append(4)
	elif x>=70 and x<=100:
		data['points'].append(5)
		
def Remark(x):
	if x <= 1:
		print("Fail")
	elif x >= 1 and x<= 1.49:
		print("Pass")
	elif x >= 1.5 and x <=2.39 :
		print ("3rd Class")
	elif x>= 2.40 and x <= 3.49:
		print("2nd Class Lower")
	elif x >= 3.50 and x <= 4.49:
		print ("2nd Class Upper")
	elif x >= 4.50 and x<= 5.00:
		print("First Class")
		
i= 0

data={
		'courses': [],
		'units':[],
		'scores':[],
		'points':[]
}
while Number_of_courses != i:
	course= input("Enter a course:")
	data['courses'].append(course)
	units=int(input("Enter the units of the course:"))
	data['units'].append(units)
	scores=int(input("Enter your score(/100):"))
	data['scores'].append(scores)
	i+=1
for number in data['scores']:
	Points(number)
df= pd.DataFrame(data)
print(df)
sum_of_units=df['units'].sum()
values_times_units = df['points']*df['units']
Sum= values_times_units.sum()
Average= Sum/sum_of_units
Average_2sf=float("{:.2f}".format(Average))
print("GPA=",Average_2sf)
Remark(Average_2sf)

		
		
		
		
		
		
from pandas.plotting import table
import matplotlib.pyplot as plt

ax=plt.subplot(111,frame_on=False)
ax.xaxis.set_visible(0)
ax.yaxis.set_visible(0)
table(ax,df,loc="upper center")
plt.savefig("Gpa.pdf")
		