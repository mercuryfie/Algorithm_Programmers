def solution(arr):
    anser = []
    for i in range(len(arr)):
        if i == 0:
            anser.append(arr[i])
        elif arr[i] != arr[i-1]:
            anser.append(arr[i])

    return anser