mySubstring(char * i, int l, int r) {
    char *s = &i[l];
    char *e = &i[r+1];
    return memcpy((char *)calloc(1, e - s + 1), s, e - s);
}
