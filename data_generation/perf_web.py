import os
import time

def output(i, j):
    return './' + str(i) + '/' + str(i) + '-' + str(j) + '.txt'

def create_close_dataset():
    with open('./alexa_50.txt') as f:    
        for i in range(1, 31):
            url = f.readline()
            os.mkdir('./' + str(i))
            for j in range(1, 101):
                os.system('timeout 6 perf stat -e \
                    cache-misses,node-loads,branch-misses,branch-load-misses,LLC-store-misses,branch-loads,L1-dcache-stores,L1-icache-load-misses,branch-instructions,iTLB-loads,iTLB-load-misses,dTLB-store-misses,dTLB-load-misses,dTLB-stores,node-stores,L1-dcache-load-misses \
                    -I 1000 -o ' + output(i, j) + ' google-chrome-stable ' + url)

def create_open_dataset():
    with open('./alexa_50.txt') as f:    
        for i in range(1, 51):
            url = f.readline()
            if i <= 30:
                continue
            # os.mkdir('./0')
            for j in range(1, 11):
                os.system('timeout 6 perf stat -e \
                    cache-misses,node-loads,branch-misses,branch-load-misses,LLC-store-misses,branch-loads,L1-dcache-stores,L1-icache-load-misses,branch-instructions,iTLB-loads,iTLB-load-misses,dTLB-store-misses,dTLB-load-misses,dTLB-stores,node-stores,L1-dcache-load-misses \
                    -I 1000 -o ' + output(0, (i - 31) * 10 + j) + ' google-chrome-stable ' + url)

create_open_dataset()