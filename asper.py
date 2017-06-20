from scipy.io.wavfile import write
from numpy import arange, pi, sin, int16
    
def f(t, f_c, f_m):
	# t    = time
	# f_c  = carrier frequency
	# f_m  = modulation frequency
	return (1 + sin(2*pi*f_m*t))*sin(2*f_c*pi*t)
    
def to_integer(signal):
	# Take samples in [-1, 1] and scale to 16-bit integers,
	# values between -2^15 and 2^15 - 1.
	return int16(signal*(2**15 - 1))
    
N = 48000 # samples per second
x = arange(1*N) # three seconds of audio
    
# 1 asper corresponds to a 1 kHz tone, 100% modulated at 70 Hz, at 60 dB
data = f(x/N, 2000, 500)
write("one_asper.wav", N, to_integer(data))