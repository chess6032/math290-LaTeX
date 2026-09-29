#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>

int *cache;

int fib(int n) {
    if (cache[n-1] != -1) {
        return cache[n-1];
    }
    int f = fib(n-2) + fib(n-1);
    cache[n-1] = f;
    return f;
}

int main(int argc, char *argv[]) {
    const int FIB_N = atoi(argv[1]);
    const int CACHE_SIZE = FIB_N + 1;
    
    // open files

    FILE* odd_file = stderr;
    FILE* even_file = stderr;
    
    if (argc > 2) {
        const char *odd_path = argv[2];
        const char *even_path = argv[3];
        
        if ((odd_file = fopen(odd_path, "w")) < 0) {
            fprintf(stderr, "Failed opening ODD file: %s\n", odd_path);
            perror("ERR");
            return 1;
        }
        if ((even_file = fopen(even_path, "w")) < 0) {
            fprintf(stderr, "Failed opening EVEN file: %s\n", even_path);
            perror("ERR");
            return 1;
        }
    }
    
    // initialize cache
    cache = malloc(FIB_N * sizeof(int));
    for (unsigned int i = 0; i < CACHE_SIZE; ++i) {
        cache[i] = -1;
    }
    cache[0] = 1; // F(1)
    cache[1] = 1; // F(2)

    // fill cache
    fib(FIB_N);

    // print out fib sequence
    int f_n;
    int odd_idx = 1;
    int even_idx = 1;
    long odd_sum = 0;
    long even_sum = 0;
    for (unsigned int i = 0; i < FIB_N; ++i) {
        f_n = cache[i];
        if ((i+1) & 1) {
            // ODD IDX
            odd_sum += f_n;
            fprintf(odd_file, "F(%d): %d    (%ld)\n", i+1, f_n, odd_sum);
            printf("F(%d): %d    (%ld)\n", i+1, f_n, odd_sum);
            ++odd_idx;
        } else {
            // EVEN IDX
            even_sum += f_n;
            fprintf(even_file, "F(%d): %d    [%ld]\n", i+1, f_n, even_sum);
            printf("F(%d): %d    [%ld]\n", i+1, f_n, even_sum);
            ++even_idx;
        }
        // printf("F(%d): %d\n", i+1, f_n);
    }

    free(cache);

    return 0;
}