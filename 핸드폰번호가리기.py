Algorithm_Programmers/Level_1/핸드폰 번호 가리기.py/

def solution(phone_number):

    phone_number_len = len(phone_number)

    answer = '*' * (phone_number_len - 4)

    answer += phone_number[-4:]

    return answer
