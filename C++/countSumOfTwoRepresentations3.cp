int countSumOfTwoRepresentations3(int n, int l, int r) {
    return max(n / 2 - max(l, n-r) + 1, 0);
}