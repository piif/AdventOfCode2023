#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DBG(code) //code
#define DBGI(code) //printf("\n%s", "||||||||||||||||||||||||||||||"+30-ind);code

int match(char *record, char *pattern, int len) {
    while(len--) {
        if (*pattern != '?' && *record != *pattern) {
            return 0;
        }
        record++;
        pattern++;
    }
    return 1;
}

int recordMatch(char *record, int *ranges, int nRanges, int len, int minLen, int ind) {
    int r0 = nRanges==0 ? -1 : ranges[0];
    int sum = 0;
    DBGI(printf("recordMatch(%s, %d)", record, r0));
    if (len < minLen) {
        DBG(printf("(l)"));
        return 0;
    }
    if (r0 == -1) {
        if (strchr(record, '#') == NULL) {
            DBG(printf("(..)"));
            return 1;
        }
    }
    while(*record == '.') {
        DBG(printf("<.>"));
        record++;
        len--;
    }
    while(*record) {
        DBG(printf("[%c]", *record));
        if (*record == '#') {
            if (r0 == 0) {
                DBG(printf("(!#)"));
                return sum;
            }
            r0--;
        } else if (*record == '.') {
            if (r0 != 0) {
                DBG(printf("(!.)"));
                return sum;
            }
            return sum + recordMatch(record+1, ranges+1, nRanges-1, len-1, minLen-1-ranges[0], ind+1);
        } else if (*record == '?') {
            if (r0 == 0) {
                return sum + recordMatch(record+1, ranges+1, nRanges-1, len-1, minLen-1-ranges[0], ind+1);
            } else if (r0 != ranges[0]) {
                DBG(printf("(?#)"));
                r0--;
            } else {
                DBG(printf("(?.)"));
                sum += recordMatch(record+1, ranges, nRanges, len-1, minLen, ind+1);
                DBGI(printf("-> %d", sum));
                DBGI(printf("(?#)"));
                r0--;
            }
        }
        record++;
        len--;
    }
    if  (nRanges == 0 || (nRanges == 1 && r0 == 0)) {
        return sum + 1;
    }
    return sum;
}

int main(int argc, char **argv) {
    FILE *f = fopen(argv[1], "r");
    char s[201];
    int perms = 0;
    int l = 0;
    while (fgets(s, 200, f)) {
        l++;
        char *c = strchr(s, ' ');
        char *record = s;
        *c = '\0';
        c++;
        int ranges[30] = { 0, };
        int nRanges = 0;
        int r;
        int minLen = -1;
        while(r = strtol(c, &c, 10)) {
            ranges[nRanges++] = r;
            minLen += r+1;
            c++;
        }

        printf("record = '%s' , ranges = ", record);
        for(int i = 0; i < nRanges; i++) {
            printf("%d ", ranges[i]);
        }
        putchar('\n');

        perms += recordMatch(record, ranges, nRanges, strlen(record), minLen, 0);
        printf("\n[%u] % 4d : => %d\n", time(), l, perms);
    }
    return 0;
}


//     # print('| '*ind, "match", record, ranges)
//     if len(ranges) == 0:
//         if record.count('#') != 0:
//             # print('| '*ind, "-> 0")
//             return 0
//         else:
//             # print('| '*ind, "-> 1")
//             return 1

//     s = 0

//     rg0 = ranges[0]
//     ranges = ranges[1:]
//     test = '#'*rg0 + ('' if len(ranges) == 0 else '.')
//     remaining = sum(ranges) + len(ranges)
//     for i in range(len(record) - (rg0 + remaining) + 1):
//         # print('| '*ind, "test", ('.'*i + test), record[:(i+len(test))])
//         suffix = '' if len(ranges) == 0 else '.'
//         if fnmatch.fnmatch('.'*i + test, record[:(i+len(test))]):
//             s += recordMatch(record[(i+len(test)):], ranges, ind+1)
//     return s


// f = open(file, 'r')
// s = 0
// for line in f.readlines():
//     print("read " + line)
//     (record, ranges) = line.split()
//     record = '?'.join([ record, record, record, record, record ])
//     ranges = ','.join([ ranges, ranges, ranges, ranges, ranges ])
//     ranges= [ int(i) for i in ranges.split(',') ]

//     s += recordMatch(record, ranges)

//     print(s)
