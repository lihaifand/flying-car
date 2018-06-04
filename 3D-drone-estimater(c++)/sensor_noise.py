import pandas as pd
import numpy as np
pos = pd.read_csv('config/log/Graph1.txt').iloc[:,1]
accel = pd.read_csv('config/log/Graph2.txt').iloc[:,1]
pos_std, accel_std = np.std(pos), np.std(accel)
print('Set MeasuredStdDev_GPSPosXY to {0:.1f} and MeasuredStdDev_AccelXY to {1:.1f}'.format(pos_std, 0.5))