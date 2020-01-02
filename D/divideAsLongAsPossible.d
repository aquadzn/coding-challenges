int divideAsLongAsPossible(int n, int d) {
    while (n % d == 0)
        n /= d;
    return n;
}