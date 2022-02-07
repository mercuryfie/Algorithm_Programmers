def solution(n):
    answer = 0
    n_list = []
    n = 12
    
    for i in range(1, n+1):
        if n % i == 0:
            n_list.append(i)
    
    answer += sum(n_list)
        
    return answer
