runnersMeetings(arr_integer p, arr_integer s) {
    int r = -1;
    int l = p.size;

    for (int i = 0; i < l; i++) {
        for (int j = 0; j < l; j++) {
            int c = 0;
            int d = p.arr[j] - p.arr[i];
            int f = s.arr[i] - s.arr[j];

            if (d * f < 1)
                continue;

            for (int k = 0; k < l; k++)
                p.arr[k] * f + s.arr[k] * d == p.arr[i] * f + s.arr[i] * d ? c++ : 0;

            c > r ? r = c : 0;
        }
    }
    return r;
}
