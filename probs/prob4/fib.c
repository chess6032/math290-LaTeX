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

    int odd_fd = STDOUT_FILENO;
    int even_fd = STDOUT_FILENO;
    FILE* odd_file;
    FILE* even_file;
    
    if (argc > 2) {
        const char *odd_path = argv[2];
        const char *even_path = argv[3];
        
        if ((odd_fd = open(odd_path, O_WRONLY | O_CREAT)) < 0) {
            fprintf(stderr, "Failed opening ODD file: %s\n", odd_path);
            perror("ERR");
            return 1;
        }
        if ((even_fd = open(even_path, O_WRONLY | O_CREAT)) < 0) {
            fprintf(stderr, "Failed opening EVEN file: %s\n", even_path);
            perror("ERR");
            return 1;
        }
    }

    if ((odd_file = fdopen(odd_fd, "w")) == NULL) {
        fprintf(stderr, "Failed converting ODD file to a stream\n");
        return 2;
    }
    if ((even_file = fdopen(even_fd, "w")) == NULL) {
        fprintf(stderr, "Failed converting EVEN file to a stream\n");
        return 2;
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
            fprintf(odd_file, "O(%d): %d    (%ld)\n", odd_idx, f_n, odd_sum);
            fprintf(stdout, "F(%d): %d    (%d: %ld)\n", i+1, f_n, odd_idx, odd_sum);
            ++odd_idx;
        } else {
            // EVEN IDX
            even_sum += f_n;
            fprintf(even_file, "E(%d): %d    [%ld]\n", even_idx, f_n, even_sum);
            fprintf(stdout, "F(%d): %d    [%d: %ld]\n", i+1, f_n, even_idx, even_sum);
            ++even_idx;
        }
    }

    free(cache);

    return 0;
}