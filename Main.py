import numpy as np

# 1(a) dB to Linear
Power_dB = np.array([0, -3, -6, -8])
Power = 10**(Power_dB/10)

# 1(b) Max excess delay
# 120 ns

# 1(c) Mean excess delay
Delay = np.array([0, 20, 80, 120])*(10**-9)
Power_Normalize = Power/sum(Power)
Delay_Mean = Delay.dot(Power_Normalize)

# 1(d) RMS excess delay
Delay_RMS = (((Delay-Delay_Mean)**2).dot(Power_Normalize))**0.5

# 2(a) h
X = np.loadtxt("Gaussian_RV_X.txt", dtype=float)
Y = np.loadtxt("Gaussian_RV_Y.txt", dtype=float)
variance_test_X = np.var(X,ddof=1) # Degrees of Freedom = 1
variance_test_Y = np.var(Y,ddof=1) # Degrees of Freedom = 1
Z=X+1j*Y
a=Power**0.5
g=a*Z
g_abs=abs(g)
k=g_abs**2
K=1/(sum(k)**0.5)
h=K*g
h_test=sum(abs(h)**2)

# 2(b) Fourier transform equation