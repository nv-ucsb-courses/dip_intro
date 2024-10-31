#let bold(content) = {
  text(weight: "bold", content)
}

= ECE-178 Homework \#4 
#bold[Due on Wednesday, November 6, 2024, 11:59 PM]

#bold[Name:]

== 2D Fourier Transform Intuition (8 points)

1. Compute the (Discrete) Fourier Transform for each of the following signals, assuming that each signal has a length of 8 samples. Sketch a plot of the resulting Fourier Transform including axis labels.

  a. $p[n] = n mod 2$

  b. $c[n] = 1$

  c. $c[n] = 0$

2. Sketch the 2D Fourier Transform of each of the following 8x8 images. For your convenience, you may report each pixel as being "dark" or "light" (white/black). #emph[Hint: you shouldn't have to do any computations if you use the result from the previous question!]

  a. 
 
  #box(stroke:black, image("images/2a.png", width:25%))

  b. 
  
  #box(stroke: black, image("images/2b.png", width:25%))

  c. 
  
  #box(stroke: black, image("images/2c.png", width:25%))

3. Explain the intuition behind the light pixels for 2a. What does a lit-up pixel represent? Create a general rule which applies to larger images.

== [PROGRAMMING] Fast Convolution (7 points)

#bold[Unless otherwise stated, you may not use any library functions which compute convolution for this problem.]

1. Implement a function called `conv(x[n], y[n])` which returns the convolution of two 1D signals of identical length `x[n]` and `y[n]` using the formula from class.

2. Recall the relationship between convolution and the FFT. Use any `np.fft` to implement a faster `fastconv(x[n], y[n])` in numpy. Briefly explain why this implementation is faster.

#bold[Bonus (not graded)] Convolution should work for signals of arbitrary length - not just signals of identical length. Implement `fastconv2(x[n], y[m])` using an FFT to improve your runtime where `x[n]` and `y[m]` don't necessarily have the same length.
