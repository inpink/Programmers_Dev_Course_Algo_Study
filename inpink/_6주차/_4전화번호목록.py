def solution(phone_book):
    answer = True
    d={}
    
    for i in phone_book:
        d[i]=True
    
    for i in phone_book:
        tmp=""
        for j in i:
            tmp+=j
            if tmp in d:
                if i!=tmp:
                    answer=False
    return answer
