#include <bits/stdc++.h>
using namespace std;

int T, N, K;

int main() {
    scanf("%d", &T);
    while (T--) {
        scanf("%d%d", &N, &K);
        int r, p;
        scanf("%d%d", &r, &p);
        if (K >= N) {
            long long sum = 0;
            for (int i = 0; i < N; i++) {
                printf("T %d\n", i + 1);
                fflush(stdout);
                int x;
                scanf("%d%d", &r, &x);
                if (x == -1) {
                    return 0;
                }
                sum += x;
            }
            printf("E %lld\n", sum/2);
            fflush(stdout);
        } else {
            long long sum = 0;
            map<int, int> M;
            for (int i = 0; i < K/2; i++) {
                int node = rand() % N + 1;
                printf("T %d\n", node);
                fflush(stdout);
                int x;
                scanf("%d%d", &r, &x);
                if (x == -1) {
                    return 0;
                }
                sum += x;
                M[r] = x;
                printf("W\n");
                fflush(stdout);
                scanf("%d%d", &r, &x);
                M[r] = x;
            }
            double est_deg = (double)sum/(K/2);
            double ans = 0;
            for (int i = 1; i <= N; i++) {
                if (M.find(i) == M.end()) ans += est_deg;
                else {
                    ans += M[i];
                }
            }
            printf("E %lld\n", (long long)(ans / 2 + 0.5));
            fflush(stdout);
        }
    }
}