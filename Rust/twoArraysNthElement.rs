fn twoArraysNthElement(mut a: Vec<i32>, b: Vec<i32>, n: i32) -> i32 {
    a.extend(b);
    a.sort();
    a[n as usize]
}
// 92