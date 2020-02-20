A, = numpy.r_[eval(dir()[0])]
A[A > 0] = sorted(A[A > 0])
return A
