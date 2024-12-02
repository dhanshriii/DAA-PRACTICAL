from bisect import bisect_left

def maximumShops(opening, closing, n, k):
    a = [[0,0] for i in range(n)]

    for i in range(n):
        a[i][0] = opening[i]
        a[i][1] = closing[i]

    a = sorted(a, key = lambda x : x[1])

    count = 1

    st = {}
    for i in range(n):

        flag = False

        if ( len(st) == 0):
            ar = list(st.keys())
            it = bisect_left(ar,a[i][0])

         
            if (it !=0):
                it -= 1

                if (ar[it] <= a[i][0]):
                    del st[it]

                    st[a[i][1]] = 1

                    count +=1
                    flag = True

        if (len(st) < k and flag == False):
            st[a[i][1]] = 1
            count += 1
    return count

if __name__ == '__main__':
 
    # Given starting and ending time
    S = [1, 8, 3, 2, 6]
    E = [5, 10, 6, 5, 9]
 
    # Given K and N
    K,N = 2, len(S)
 
    # Function call
    print (maximumShops(S, E, N, K))
                    

