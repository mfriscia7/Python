'''
input format:

first line (1 int): number of test cases

following is two lines per test case

first line (2 ints): n = length of list, k = weight that knapsack can hold
second line (n ints): weights of each object

SAMPLE INPUT:
 1
 3 12
 1 6 9
SAMPLE OUTPUT : 12
'''


test_cases = int(raw_input())

for i in range(0,test_cases):
    ta = [int(x) for x in raw_input().split(' ')]
    n = ta[0]
    k = ta[1]
    weights = [int(x) for x in raw_input().split(' ')]

    ## use set to remove duplicate weights
    weights = list(set(weights))
    n = len(weights)

    if 1 in weights:
        print k
    else:
        arr = [[0]*(k+1) for x in range(0,n)]

        # run knapsack alg
        for i in range(0,n):
            for curr_weight in range(1,k+1):

                ## first column does not have a column to the left to look at
                if i == 0:
                    arr[i][curr_weight] = arr[i][curr_weight-1]
                    if arr[i][curr_weight] + weights[i] <= curr_weight:
                        arr[i][curr_weight] += weights[i]

                ## for columns 2,...,n there are three options
                else:
                    ## first option: adding to or keeping what is in the same column
                    if curr_weight-weights[i] >= 0:
                        if arr[i][curr_weight-weights[i]] + weights[i] <= curr_weight:
                            try1 = arr[i][curr_weight-weights[i]] + weights[i]
                    else:
                        try1 = 0

                    ## second option: add current item to knapsack in last column
                    if curr_weight-weights[i] > 0:
                        try2 = arr[i-1][curr_weight-weights[i]] + weights[i]
                    else:
                        try2 = 0

                    ## third option: taking the curr_weight for the last column
                    try3 = arr[i-1][curr_weight]

                    arr[i][curr_weight] = max(try1, try2, try3)


        # prints the top right corner of the knapsack grid
        print arr[n-1][k]