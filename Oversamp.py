def oversamp(indata, sample):
    import numpy as np
    nsymb = np.size(indata)
    out = np.zeros(nsymb*sample, dtype=complex)
    for i in range(0, nsymb, 1):
        out[i*sample] = indata[i]
    return out