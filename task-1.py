import pandas 
import matplotlib.pyplot as plt
re=pandas.read_excel('C:\\Users\\91740\\Desktop\\tasks\\data.xlsx.xls')
# Read the Excel file
data = pandas.read_excel('C:\\Users\\91740\\Desktop\\tasks\\data.xlsx.xls', skiprows=4)
data.columns = data.columns.str.strip()

print("Columns:", list(data.columns))
print(data.head(10))

# Use actual column names
categories = data.iloc[:, 0].fillna("Unknown").astype(str) # representing using index values
values = pandas.to_numeric(data.iloc[:, 60], errors='coerce')  # representing using index values

# Remove invalid or missing values
valid = ~values.isna()
categories = categories[valid]
values = values[valid]

plt.figure(figsize=(16, 7))
plt.bar(categories, values, color='skyblue')
plt.xlabel('Country Name')
plt.ylabel('Population in 2020')
plt.title('Population by Country (2020)')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 4))
plt.hist(categories, bins=10, color='lightgreen', edgecolor='black')
plt.xlabel('Country Name')
plt.ylabel('Population in 2020')
plt.title('Histogram of Values')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

