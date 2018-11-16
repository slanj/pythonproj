import numpy as np
import pandas as pd
data = pd.read_csv('president_heights.csv')
heights = np.array(data['height(cm)'])
print(heights)

print("Mean height:       ", heights.mean())
print("Standard deviation:", heights.std())
print("Minimum height:    ", heights.min())
print("Maximum height:    ", heights.max())

print("25th percentile:   ", np.percentile(heights, 25))
print("Median:            ", np.median(heights))
print("75th percentile:   ", np.percentile(heights, 75))

import matplotlib.pyplot as plt
import seaborn; seaborn.set()  # set plot style

plt.hist(heights)
plt.title('Height Distribution of US Presidents')
plt.xlabel('height (cm)')
plt.ylabel('number')

plt.show()

# [189 170 189 163 183 171 185 168 173 183 173 173 175 178 183 193 178 173
#  174 183 183 168 170 178 182 180 183 178 182 188 175 179 183 193 182 183
#  177 185 188 188 182 185]
# Mean height:        179.73809523809524
# Standard deviation: 6.931843442745892
# Minimum height:     163
# Maximum height:     193
# 25th percentile:    174.25
# Median:             182.0
# 75th percentile:    183.0