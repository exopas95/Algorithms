"""
[문제: 1157] 
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
단, 대문자와 소문자를 구분하지 않는다.

[입력]
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

[출력]
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
"""
word = list(input().lower())
word_dict = {}
for char in word:
    if char in word_dict:
        word_dict[char] += 1
    else:
        word_dict[char] = 1

max_value = 0
max_list = []
for key in word_dict:
    if word_dict[key] >= max_value:
        max_value = word_dict[key]
        max_list.append(max_value)
        max_key = key.upper()

if max_list.count(max_value) > 1:
    print('?')
else:
    print(max_key)
