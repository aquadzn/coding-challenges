halvingSum(int n) {
    int s = 0;
    while (n) {
        s += n;
        n /= 2;
    }
    return s;
}