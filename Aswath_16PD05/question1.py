# -*- coding: utf-8 -*-
"""question1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x-BmzNri1HEjYAHO5z9jXdh3tDcmiSzB
"""

from google.colab import files
s =files.upload()

import pandas as pd
df=pd.read_csv('question1.csv')

df.describe() #No null values
datasetHasNan = False
if df.count().min() == df.shape[0]:
    print('NO null values') 
else:
    datasetHasNan = True
    print('Null is present')

df.describe() #No null values

# main libraries
import pandas as pd
import numpy as np
import time
# visual libraries
from matplotlib import pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D 
plt.style.use('ggplot')
# sklearn libraries
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize
from sklearn.metrics import confusion_matrix,accuracy_score,precision_score,recall_score,f1_score,matthews_corrcoef,classification_report,roc_curve
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

df.isnull().any().sum()

f1 = [df['Angle'].values]
sns.distplot(f1)

f2 = [df['Chord_Length'].values]
sns.distplot(f2)

f2 = [df['velocity'].values]
sns.distplot(f2)

f4 = [df['Pressure_level'].values]
sns.distplot(f4)

f3 = [df['Displacement'].values]
sns.distplot(f3)

f5 = [df['Frquency(Hz)'].values]
sns.distplot(f5)

correlation_matrix = df.corr()
fig = plt.figure(figsize=(6,3))
sns.heatmap(correlation_matrix,vmax=0.8,square = True)
plt.show()

plt.scatter(df['Frquency(Hz)'],df['Pressure_level'])

plt.title('Frequency vs Pressure level')

plt.xlabel('Frequency')

plt.ylabel('Pressure_level')

plt.show()

plt.scatter(df['Angle'],df['Pressure_level'])

plt.title('Angle vs Pressure level')

plt.xlabel('Angle')

plt.ylabel('Pressure_level')

plt.show()

plt.scatter(df['Chord_Length'],df['Pressure_level'])

plt.title('Chord_Length vs Pressure level')

plt.xlabel('Chord_Length')

plt.ylabel('Pressure_level')

plt.show()

plt.scatter(df['velocity'],df['Pressure_level'])

plt.title('velocity vs Pressure level')

plt.xlabel('velocity')

plt.ylabel('Pressure_level')

plt.show()

plt.scatter(df['Displacement'],df['Pressure_level'])

plt.title('displacement vs Pressure level')

plt.xlabel('displacement')

plt.ylabel('Pressure_level')

plt.show()

par(mfrow = c(1, 2))
# Boxplot for X
boxplot(df['Displacement'], main='X', sub=paste('Outliers: ', boxplot.stats(df['Displacement'])))

cor(df['Displacement'], df['Pressure_level'])

from scipy.stats.stats import pearsonr    
print(pearsonr(df['Displacement'], df['Pressure_level']))

import numpy
print(numpy.corrcoef(df['Displacement'], df['Pressure_level']))
df.corr()

from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split

dfName.select_dtypes(exclude=['int', 'float']).columns

df.plot(kind='box', subplots=True, layout=(6, 6), figsize=(12, 50))
plt.show()

x = df.iloc[:,:5]
y = df.iloc[:,-1]

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state=12345)

# Scale the data to be between -1 and 1
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

print("Coefficient ", regressor.coef_)
print("Intercept ",regressor.intercept_)

y_pred = regressor.predict(X_test)





sum(abs(list(y_test)-y_pred))/len(y_pred)



regressor.score(X_train,y_train)

# Import the model we are using
from sklearn.ensemble import RandomForestRegressor
# Instantiate model with 1000 decision trees
rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
# Train the model on training data
rf.fit(X_train,y_train);

# Use the forest's predict method on the test data
predictions = rf.predict(X_test)
# Calculate the absolute errors
errors = abs(predictions - y_test)
# Print out the mean absolute error (mae)
print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')

# Calculate mean absolute percentage error (MAPE)
mape = 100 * (errors / y_test)
# Calculate and display accuracy
accuracy = 100 - np.mean(mape)
print('Accuracy:', round(accuracy, 2), '%.')



from sklearn.model_selection import cross_val_predict, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
gsc = GridSearchCV(
        estimator=RandomForestRegressor(),
        param_grid={
            'max_depth': range(3,7),
            'n_estimators': (10, 50, 100, 1000),
        },
        cv=5, scoring='neg_mean_squared_error', verbose=0,                         n_jobs=-1)

grid_result = gsc.fit(X_train, y_train)

best_params = grid_result.best_params_

rfr = RandomForestRegressor(max_depth=best_params["max_depth"], n_estimators=best_params["n_estimators"],                               random_state=False, verbose=False)

scores = cross_val_predict(rfr, X_train, y_train, cv=10)

predictions = cross_val_predict(rfr, X_test, y_test, cv=10)
predictions

errors = abs(predictions - y_test)
# Print out the mean absolute error (mae)
print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')

# Calculate mean absolute percentage error (MAPE)
mape = 100 * (errors / y_test)
# Calculate and display accuracy
accuracy = 100 - np.mean(mape)
print('Accuracy:', round(accuracy, 2), '%.')