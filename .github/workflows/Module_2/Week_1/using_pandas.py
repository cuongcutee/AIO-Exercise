import pandas as pd
import numpy as np
df = pd.read_csv(r'.github\workflows\Module_2\Week_1\advertising.csv')
data = df.to_numpy()

# max number and index in Sales
height, width = data.shape
max = data[0][3]
index = 0
for i in range(1, height):
    if data[i][3] > max:
        max = data[i][3]
        index = i
print(f"Max:{max} - Index:{index}")

print(sum(data[:, 0])/height)

print(np.sum(data[:, 3] >= 20))
sales_data = data[:, 3]
filtered_sales_data = sales_data[sales_data >= 15]
average_filtered_sales = np.mean(filtered_sales_data)
print(average_filtered_sales)
