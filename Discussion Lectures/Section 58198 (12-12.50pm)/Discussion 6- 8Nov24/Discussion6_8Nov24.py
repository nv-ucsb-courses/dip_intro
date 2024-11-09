import numpy as np

def convolve_1d(signal, kernel):
    signal_len = len(signal) # get the length of the signal
    kernel_len = len(kernel) # get the length of the kernel
    output_len = signal_len + kernel_len - 1 # get the length of the output
    output = np.zeros(output_len)

    for i in range(output_len): # loop through the output
        for j in range(kernel_len): # loop through the kernel
            if i - j >= 0 and i - j < signal_len: # check if the index is within the signal range
                output[i] += signal[i - j] * kernel[j] # compute the convolution
    
    return output

def convolve_1d_fft(signal, kernel):
    signal_len = len(signal)
    kernel_len = len(kernel)
    output_len = signal_len + kernel_len - 1

    # Compute the FFT of the input signals
    signal_fft = np.fft.fft(signal, output_len)
    kernel_fft = np.fft.fft(kernel, output_len)

    # Element-wise multiplication in the frequency domain
    output_fft = signal_fft * kernel_fft

    # Compute the inverse FFT to get the convolution result
    output = np.fft.ifft(output_fft)

    # Return the real part of the output
    return np.real(output)


if __name__ == "__main__":
    signal = np.array([1, 2, 3, 4, 5])
    kernel = np.array([1, 2, 3])

    conv1 = convolve_1d(signal, kernel)
    conv2 = convolve_1d_fft(signal, kernel)

    print(conv1)
    print(conv2)