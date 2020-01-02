func divideAsLongAsPossible(n int, d int) int {
    for n % d == 0 {
        n /= d
    }
    return n
}