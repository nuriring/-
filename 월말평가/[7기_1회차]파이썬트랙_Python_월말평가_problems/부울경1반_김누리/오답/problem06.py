# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# def caesar(word, n):

def caesar(word, n):
    # 함수에 입력되는 값은 문자열과, 숫자 두가지 인자이다
    # 여기에 코드를 작성하여 함수를 완성합니다.
    # 문자열 각각에 해당하는 아스키 코드 숫자값을 조회한다
    # 입력된 단어의 문자열을 순회한다
    result='' #변환된 문자열을 저장해줄 빈 result
    for words in word:
        
        
       
        number = ord(words) # 더해준 값을 new_number에 할당
        if 65 <= number <= 90: #대문자일경우
            number = (ord(words)+n-65)%26 #대문자 안에서 순회하도록
            new_number = number+65 
            result += chr(new_number)
                  
        elif 97<= number <= 122: #소문자일 경우
            number = (ord(words)+n-97)%26 #소문자안에서 순회
            new_number = number+97
            result += chr(new_number)
    return result
     

    #소문자는 소문자 내에서만 순회하고 대문자는 대문자내에서 순회하는 코드를 고려해줘야함!!!!!!!!!!!!
    



# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(caesar('apple', 5))
    # fuuqj
    print(caesar('ssafy', 1))
    # ttbgz
    print(caesar('Python', 10))
    # Zidryx