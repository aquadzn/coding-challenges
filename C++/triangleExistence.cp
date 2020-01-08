bool triangleExistence(auto t) {
    sort(begin(t), end(t));
    return t[0] + t[1] > t[2];
}

