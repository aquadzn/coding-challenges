// int countSumOfTwoRepresentations3(int n, int l, int r) {
//     return fmax(n / 2 - fmax(l, n-r) + 1, 0);
// }

#define countSumOfTwoRepresentations3(n, l, r) fmax(n / 2 - fmax(l, n-r) + 1, 0)