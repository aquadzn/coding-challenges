fn runnersMeetings(p: Vec<i32>, s: Vec<i32>) -> i32 {
    let mut r = -1;
    let l = p.len();

    for i in 0..l {
        for j in 0..l {
            let mut c = 0;
            let d = p[j] - p[i];
            let f = s[i] - s[j];

            if d * f < 1 {
                continue;
            }

            for k in 0..l {
                if p[k] * f + s[k] * d == p[i] * f + s[i] * d {
                    c += 1;
                }
            }

            if c > r {
                r = c;
            }
        }
    }
    r // Return
}
