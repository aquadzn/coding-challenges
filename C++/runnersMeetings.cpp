int runnersMeetings(auto p, auto s) {
    int r = -1;
    int l = p.size();

    for (int i = 0; i < l; i++) {
        for (int j = 0; j < l; j++) {
            int c = 0;
            int d = p[j] - p[i];
            int f = s[i] - s[j];

            if (d * f < 1)
                continue;

            for (int k = 0; k < l; k++)
                p[k] * f + s[k] * d == p[i] * f + s[i] * d ? c++ : 0;

            c > r ? r = c : 0;
        }
    }
    return r;
}
