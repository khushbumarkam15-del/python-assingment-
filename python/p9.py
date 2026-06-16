if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    # 1. Convert to a set to remove duplicates
    unique_scores = set(arr)
    
    # 2. Remove the maximum score
    unique_scores.remove(max(unique_scores))
    
    # 3. The new maximum is the runner-up
    print(max(unique_scores))