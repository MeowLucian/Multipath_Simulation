import numpy as np
import matplotlib.pyplot as plt
import Oversamp as Os

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
P1.plot(f, abs(HH), '-', color='palevioletred', linewidth=4.0)
P1.set_xlabel("f")
P1.set_ylabel("Amplitude")
P1.set_title("Frequency domin-Magnitude")

plt.style.use('dark_background')
fig, P2 = plt.subplots()
P2.plot(f, np.angle(HH), '-', color='palevioletred', linewidth=4.0)
P2.set_xlabel("f")
P2.set_ylabel("Amplitude")
P2.set_title("Frequency domin-Phase")

# 2(d) Subcarrier
B_c = 1/(5*Delay_RMS)
N = np.ceil(50e6/B_c)

# 3(a) d_n
Binary_data = np.array([0, 1, 0, 1, 1, 1])
Binary_data_new = np.zeros(np.size(Binary_data), dtype=complex)

for p in range(0, np.size(Binary_data), 1):
    if Binary_data[p] == 0:
        Binary_data_new[p] = 1
    else:
        Binary_data_new[p] = -1

d_n = Os.oversamp(Binary_data_new, 8)
t = np.arange(np.size(d_n))*20e-9

plt.style.use('dark_background')
fig, P3 = plt.subplots()
markerline, stemlines, baseline = P3.stem(t, d_n)
plt.setp(markerline, color='springgreen', markersize=8.5)
plt.setp(stemlines, color='cornflowerblue', linewidth=4.0, linestyle='--')
plt.setp(baseline, color='palevioletred', linewidth=2.0)
P3.set_xlabel("t")
P3.set_ylabel("Amplitude")
P3.set_title("d_n")

# 3(b) z_n
h_new = np.array([h[0], h[1], 0, 0, h[2], 0, h[3]])
NN = np.size(h_new)
t = np.arange(NN)*20e-9

plt.style.use('dark_background')
fig, P4 = plt.subplots()
markerline, stemlines, baseline = P4.stem(t, abs(h_new))
plt.setp(markerline, color='springgreen', markersize=8.5)
plt.setp(stemlines, color='cornflowerblue', linewidth=4.0, linestyle='--')
plt.setp(baseline, color='palevioletred', linewidth=2.0)
P4.set_xlabel("t")
P4.set_ylabel("Amplitude")
P4.set_title("h_new")

z_n_temp = np.zeros((NN,np.size(d_n)), dtype=complex)
z_n_temp2 = np.zeros((NN,np.size(d_n)+NN-1), dtype=complex)

for o in range(0, NN, 1):
    offset_zero_front = np.zeros((o), dtype=complex)
    offset_zero_back = np.zeros((NN-1-o), dtype=complex)
    z_n_temp[o,:] = h_new[o]*d_n # [1x48]
    z_n_temp2[o,:] = np.concatenate((offset_zero_front, z_n_temp[o,:], offset_zero_back)) # [1x54]

z_n = sum(z_n_temp2) # [1x54]
t = np.arange(np.size(d_n)+6)*20e-9

plt.style.use('dark_background')
fig, P5 = plt.subplots()
P5.plot(t, np.real(z_n), '-', color='palevioletred', linewidth=4.0)
P5.set_xlabel("t")
P5.set_ylabel("Amplitude")
P5.set_title("real z_n")

plt.style.use('dark_background')
fig, P6 = plt.subplots()
P6.plot(t, np.imag(z_n), '-', color='palevioletred', linewidth=4.0)
P6.set_xlabel("t")
P6.set_ylabel("Amplitude")
P6.set_title("imag z_n")

plt.style.use('dark_background')
fig, P7 = plt.subplots()
P7.plot(t, abs(z_n), '--', color='palevioletred', linewidth=3.0, label='abs z_n')
t2 = np.arange(np.size(d_n))*20e-9
markerline, stemlines, baseline = P7.stem(t2, d_n, label='d_n')
plt.setp(markerline, color='springgreen', markersize=8.5)
plt.setp(stemlines, color='cornflowerblue', linewidth=4.0, linestyle='--')
plt.setp(baseline, color='palevioletred', linewidth=2.0)

P7.legend(loc='lower right')
P7.set_xlabel("t")
P7.set_ylabel("Amplitude")
P7.set_title("imag z_n")

plt.show()

# 3(c) ISI
# NO