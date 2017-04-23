import numpy as np
import matplotlib.pyplot as plt

# 1(a) dB to Linear
Power_dB = np.array([0, -3, -6, -8])
Power = 10**(Power_dB/10)

# 1(b) Max excess delay
# 120 ns

# 1(c) Mean excess delay
Delay = np.array([0, 20, 80, 120])*(1e-9)
Power_Normalize = Power/sum(Power)
Delay_Mean = Delay.dot(Power_Normalize)

# 1(d) RMS excess delay
Delay_RMS = np.sqrt(((Delay-Delay_Mean)**2).dot(Power_Normalize))

# 2(a) h
X = np.loadtxt("Gaussian_RV_X.txt", dtype=float)
Y = np.loadtxt("Gaussian_RV_Y.txt", dtype=float)
variance_test_X = np.var(X,ddof=1) # Degrees of Freedom = 1
variance_test_Y = np.var(Y,ddof=1) # Degrees of Freedom = 1
Z = X+1j*Y
a = np.sqrt(Power)
g = a*Z
g_abs = abs(g)
k = g_abs**2
K = 1/np.sqrt(sum(k))
h = K*g
h_test = sum(abs(h)**2)

# 2(b) Fourier transform equation

# 2(c) Channel Frequency response
fs = 50e6
f = (np.linspace(-1, 1, 401))*fs
HH = np.zeros(np.size(f), dtype=complex)

for ff in range(0, np.size(f), 1):
    temp = h*np.exp(-1j*2*np.pi*f[ff]*Delay)
    HH[ff] = sum(temp)

plt.style.use('dark_background')
fig, P1 = plt.subplots()
P1.plot(f, abs(HH), '-', color='palevioletred',linewidth=4.0)
P1.set_xlabel('f')
P1.set_ylabel('Amplitude')
P1.set_title("Frequency domin-Magnitude")

plt.style.use('dark_background')
fig, P2 = plt.subplots()
P2.plot(f, np.angle(HH), '-', color='palevioletred',linewidth=4.0)
P2.set_xlabel('f')
P2.set_ylabel('Amplitude')
P2.set_title("Frequency domin-Phase")

plt.show()