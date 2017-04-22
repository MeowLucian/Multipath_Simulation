import numpy as np

# 1(a) dB to Linear
Power_dB = np.array([0, -3, -6, -8])
Power = 10**(Power_dB/10)

# 1(b) Max excess delay
# 120 ns

# 1(c) Mean excess delay
Delay=np.array([0, 20, 80, 120])*(10**-9)
Power_Normalize=Power/sum(Power)
Delay_Mean=Delay.dot(Power_Normalize)

# 1(d) RMS excess delay
Delay_RMS=(((Delay-Delay_Mean)**2).dot(Power_Normalize))**0.5