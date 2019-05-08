import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df= pd.read_excel('Dataset Problem 3.xlsx',header=0)
#Question 1.............
df = df[df.Date >= pd.Timestamp(2017,1,1,0)]
df = df.set_index('Date',drop="True")
df['E2'].plot()
df['E1'].plot()


#Question 3...........................................
df.corr()
corr = df.corr()

#..........................
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(corr,cmap='coolwarm', vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0,len(df.columns),1)
ax.set_xticks(ticks)
plt.xticks(rotation=90)
ax.set_yticks(ticks)
ax.set_xticklabels(df.columns)
ax.set_yticklabels(df.columns)
plt.show()

#Question 2...........................................
s =[]
w =[]
y =[]
for i in range(1,13):
    s.append(np.mean(list(df[df.index.month == i]['Power Consumption'])))
    w.append(np.mean(list(df[df.index.month == i]['E2'])))
    y.append(np.mean(list(df[df.index.month == i]['E1'])))
    
a =[]
b =[]
c =[]

for i in range(int(len(s)/3)):
    a.append((np.mean(s[i:i+3])))
    b.append((np.mean(w[i:i+3])))
    c.append((np.mean(y[i:i+3])))
    
import seaborn as sns
l1 = ['Q1','Q2','Q3','Q4']
sns.pointplot(x=l1,y=b)
 
l2 = ['Q1','Q2','Q3','Q4']
sns.pointplot(x=Q,y=c)   
#
#d = ["Q1","Q2","Q3","Q4"]
##plt.plot(d,a)
#plt.plot(d,b)
#plt.plot(d,c)

#...................................................

