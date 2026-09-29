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
    }
    
    // initialize cache
    cache = malloc(FIB_N * sizeof(int));
    for (unsigned int i = 0; i < CACHE_SIZE; ++i) {
        cache[i] = -1;
    }
    cache[0] = 1; // F(1)
    cache[1] = 1; // F(2)

    fib(FIB_N);

    int f;
    int odd = 1;
    int even = 1;
    for (unsigned int i = 0; i < FIB_N; ++i) {
        f = cache[i];
        if ((i+1) & 1) {
            fprintf(odd_file, "O(%d): %d\n", odd++, f);
        } else {
            fprintf(even_file, "E(%d): %d\n", even++, f);
        }
        fprintf(stdout, "F(%d): %d\n", i+1, f);
    }

    free(cache);

    return 0;
}