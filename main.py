# python3
import heapq
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    # TODO: create the function
    # TODO: print out the results, each pair in it's own line
def parallel_processing(n, k, data):
    output = []
    t = [(0, i) for i in range(n)]
    heapq.heapify(t)
    for i in range(k):
       start, ind = heapq.heappop(t)
        output.append((ind, start))
        finish = start + data[i]
        heapq.heappush(t, (finish, ind))
    return output

def main():
    try:
        n, k = map(int, input().split())
        if not (1 <=n <= 10**5) or not (1 <= k <= 10**5):
            raise ValueError("Invalid input, input must be from 1 to 10^5")
        
        data = list(map(int, input(). split()))
        if len(data) != k or not all(1 <= d <= 10**9 for d in data):
            raise ValueError("Invalid input: data must be a list of m integers between 1 and 10^9")
            
        result = parallel_processing(n, k, data)
        
        for i in range(k):
            print(result[i][0], result[i][1])
            
    except ValueError as e:
        print (e)

if __name__ == "__main__":
    main()
