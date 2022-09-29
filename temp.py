import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('Residents vs non-residents 2015-20.csv')
plt.plot(data.Years, data.IndianResidents, marker='o')
plt.plot(data.Years, data.NonResident, marker='o')
plt.xlabel("Years")
plt.ylabel("Number of patents filed")
plt.legend(["Residents","Non-Residents"])
plt.show()