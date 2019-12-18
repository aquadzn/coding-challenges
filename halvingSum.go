func halvingSum(n int) int {
    s := 0
    for n != 0 {
        s += n
        n /= 2
    }
    return s
}