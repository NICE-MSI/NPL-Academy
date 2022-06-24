import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("C:/Users/ag12/PycharmProjects/NPL-Academy/spectra.csv", index_col=False)  # read data files
print(df)  #print data file

plt.plot(df["m/z"],df["A_APCKRAS"], color='blue', label='tissue A-APCKRAS')
plt.plot(df["m/z"],df["D_APCKRAS"], color='red', label='tissue D-APCKRAS')
plt.legend()
#plt.show()
plt.clf()

plt.plot(df["m/z"],df["A_APCKRAS"], color='blue', label='tissue A-APCKRAS')
plt.xlim((400,420))
#plt.show()
plt.clf()


print(np.std(df["A_APCKRAS"]), np.std(df["D_APCKRAS"]))

treshold = np.std(df["A_APCKRAS"])/20

plt.plot(df["m/z"],df["A_APCKRAS"].where(df["A_APCKRAS"]<treshold), color='blue', label='noise A-APCKRAS')
plt.plot(df["m/z"],df["A_APCKRAS"].where(df["A_APCKRAS"]>=treshold), color='red', label='signal A-APCKRAS')

# plt.plot(df["m/z"],df["D_APCKRAS"].where(df["D_APCKRAS"]<treshold), color='blue', label='tissue A-APCKRAS')
# plt.plot(df["m/z"],df["D_APCKRAS"].where(df["D_APCKRAS"]>=treshold), color='red', label='tissue A-APCKRAS')
plt.xlim((400,405))
plt.ylim((-2,14))
#plt.show()
plt.savefig("C:/Users/ag12/PycharmProjects/NPL-Academy/outputs/test.png")

