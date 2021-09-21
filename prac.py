test_dic = {'a': {'b': 'c'}, 'd': 'e'}

print(test_dic.keys()) 
# dict_keys(['a', 'd']) 최상위 key들만 표시됨
print(test_dic.values())


print('a' in test_dic.keys()) # 출력 : True
print('e' in test_dic.values()) # 출력 : True

# key,value 같이 출력하기
for key, value in test_dic.items():
    print(key, value)
    
 # 출력 : 'd', 'e' (nested dictionary는 출력 안됨)

print(isinstance(1,))