def solution(quiz):
    answer = []
    for i in quiz:
        x = i.split("=")
        if eval(x[0]) == int(x[1]):
            answer.append('O')
        else:
            answer.append('X')
    
    return answer