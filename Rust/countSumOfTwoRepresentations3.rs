// use std::cmp::max;

fn countSumOfTwoRepresentations3(n: i32, l: i32, r: i32) -> i32 {
    // max(n / 2 - max(l, n-r) + 1, 0)
    0.max(n / 2 - l.max(n-r) + 1)
}

