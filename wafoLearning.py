import wafo.spectrum.models as wsm
import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint

print("\n\n\n")


# creating Jonswap spectrum from wafo methods
S1 = wsm.Jonswap(Hm0=7, Tp=11, gamma=1)
S1_specData=S1.tospecdata()

# plot spectrum via wafo style
S1_specData.plot()
S1_specData.show()

# getting angular frequency and spectrum variables
freq = S1_specData.args    # w    [rad/s]
spec = S1_specData.data    # S(w) [m2.s/rad]

# matplotlib plot
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(freq, spec, label="direct from [wafo.tospecdata] method")
plt.xlabel(r'Frequency [rad/s]',fontsize=12)
plt.ylabel(r'$S(\omega)$ $[m^2.s/rad]$',fontsize=12)
plt.legend(loc="upper left")
plt.show()

# I can use directly the wave spectrum and define my own frequency range
w = np.linspace(0, 2, 400)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(freq, spec, label="direct from [wafo.tospecdata] method")
ax.plot(w, S1(w), label="user defined frequency range")
plt.xlabel(r'Frequency [rad/s]',fontsize=12)
plt.ylabel(r'$S(\omega)$ $[m^2.s/rad]$',fontsize=12)
plt.legend(loc="upper left")
plt.show()
