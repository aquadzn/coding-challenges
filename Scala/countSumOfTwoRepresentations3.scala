// def countSumOfTwoRepresentations3(n: Int, l: Int, r: Int): Int = {
//     (n / 2 - l.max(n-r) + 1).max(0)
// }

def countSumOfTwoRepresentations3(n: Int, l: Int, r: Int) =
    (n / 2 - (l max n-r) + 1) max 0