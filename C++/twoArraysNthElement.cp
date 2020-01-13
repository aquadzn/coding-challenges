int twoArraysNthElement(auto a, auto b, auto n) {
    a.insert(end(a), begin(b), end(b));
    sort(begin(a), end(a));
    return a[n];
}
