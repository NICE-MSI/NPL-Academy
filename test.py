import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import ttest_ind
# df = pd.read_csv("C:/Users/ag12/PycharmProjects/NPL-Academy/spectra.csv", index_col=False)  # read data files
# print(df)  #print data file
# #
# plt.plot(df["m/z"],df["A_APCKRAS"], color='blue', label='tissue A-APCKRAS')
# plt.plot(df["m/z"],df["D_APCKRAS"], color='red', label='tissue D-APCKRAS')
# plt.legend()
# plt.show()
# plt.clf()
#
# plt.plot(df["m/z"],df["A_APCKRAS"], color='blue', label='tissue A-APCKRAS')
# plt.xlim((300,320))
# plt.show()
# plt.clf()
#
#
# print('standard deviation for tissue A', np.std(df["A_APCKRAS"]))
# print('standard deviation for tissue D',np.std(df["D_APCKRAS"]))
#
# treshold = np.std(df["A_APCKRAS"])
#
# plt.plot(df["m/z"],df["A_APCKRAS"].where(df["A_APCKRAS"]<treshold), color='blue', label='noise A-APCKRAS')
# plt.plot(df["m/z"],df["A_APCKRAS"].where(df["A_APCKRAS"]>=treshold), color='red', label='signal A-APCKRAS')
#
# # plt.plot(df["m/z"],df["D_APCKRAS"].where(df["D_APCKRAS"]<treshold), color='blue', label='tissue A-APCKRAS')
# # plt.plot(df["m/z"],df["D_APCKRAS"].where(df["D_APCKRAS"]>=treshold), color='red', label='tissue A-APCKRAS')
# plt.xlim((300,320))
# #plt.ylim((-2,14))
# plt.show()
# #plt.savefig("C:/Users/ag12/PycharmProjects/NPL-Academy/outputs/test.png")
# plt.clf()
#
#
# plt.plot(df["m/z"],df["A_APCKRAS"].where(df["A_APCKRAS"]<treshold), color='blue', label='noise A-APCKRAS')
# plt.plot(df["m/z"],df["A_APCKRAS"].where(df["A_APCKRAS"]>=treshold), color='red', label='signal A-APCKRAS')
#
# # plt.plot(df["m/z"],df["D_APCKRAS"].where(df["D_APCKRAS"]<treshold), color='blue', label='tissue A-APCKRAS')
# # plt.plot(df["m/z"],df["D_APCKRAS"].where(df["D_APCKRAS"]>=treshold), color='red', label='tissue A-APCKRAS')
# plt.xlim((310,320))
# plt.ylim((-1E5,6E5))
# plt.show()


# peaks = pd.read_csv("C:/Users/ag12/PycharmProjects/NPL-Academy/top70_peaks.csv")  # read data files
# #print(peaks)  #print data file
#
# print(peaks.columns)
# peaks['mean APCKRAS'] = peaks.iloc[:, [1,5,6]].mean(axis=1)
# peaks['mean APC'] = peaks.iloc[:, [2,3,4]].mean(axis=1)
#
# peaks['ratio'] = peaks['mean APCKRAS']/peaks['mean APC']
#
# peaks.sort_values(by=['ratio'])
# #print(peaks.sort_values(by=['ratio'], ascending=False))
#
#print(peaks.nlargest(10,'ratio'))

ttest = pd.read_csv("C:/Users/ag12/PycharmProjects/NPL-Academy/t_test_tumours.csv")  # read data files
print(ttest)
print(ttest.nsmallest(10,'t_value'))