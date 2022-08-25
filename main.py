import pandas as pd
data_car = pd.read_csv(r"cars-data.csv")
print(data_car)

#Data cleaning
print(data_car.isnull().sum())
data_car.dropna(how='all', inplace=True)
print(data_car.isnull().sum())

#Fill null values with the mean of the column
data_car['Cylinders'].fillna(data_car['Cylinders'].mean(), inplace=True)
print(data_car.isnull().sum())

#Show Makes and ocurrences of each
print(data_car['Make'].value_counts())

#Show all records where Origin is Asia or Europe
data_car_a_e = data_car[data_car['Origin'].isin(['Asia', 'Europe'])]
print(data_car_a_e)

#remove all records where weight is > 4000
data_car_weight = data_car.loc[data_car['Weight'] <= 4000]
print(data_car_weight)

#Increase all values from MPG_City by 3
data_car['MPG_City'] = data_car['MPG_City'].apply(lambda x:x+3)
print(data_car)
