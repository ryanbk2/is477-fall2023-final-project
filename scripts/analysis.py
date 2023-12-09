import pandas as pd
import matplotlib.pyplot as plt

colnames=['buying','maint','doors','persons','lug_boot','safety','class'] 
df = pd.read_csv('data/car.csv', names=colnames, header=None)
df = df.dropna()
df.head()

df['doors'].hist()
plt.xlabel("Number of Doors")
plt.ylabel("Frequency")
plt.title('Number of Doors per Car')
plt.show()

df['persons'].hist()
plt.xlabel("Car Capacity")
plt.ylabel("Frequency")
plt.title('Number of People per Car')
plt.show()