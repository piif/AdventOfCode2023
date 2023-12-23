#include <stdio.h>

int main(int argc, char **argv) {
    int c;
    int sum = 0;
    int hash = 0;
    while((c=getchar())>=0) {
        if (c==',') {
            printf("%d\n", hash);
            sum += hash;
            hash = 0;
        } else if (c!='\n') {
            hash = ( (hash+c) * 17 ) & 255;
        }
    }
    sum += hash;
    printf("%d\n", sum);
}
