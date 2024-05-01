// gcc main.c -o bin/hashme -lm -ggdb

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double hashme(double input) {
  return powl(input, 4) + logl(input + 3);
}

int main(int argc, char** argv) {
  if (argc != 2) {
    printf("Usage: %s N\n", argv[0]);
    return EXIT_FAILURE;
  }

  double N = (double)atoi(argv[1]);
  double hash = hashme(N);
  printf("%f\n", hash);

  return EXIT_SUCCESS;
}
