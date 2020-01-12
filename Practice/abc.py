import json

diary = {
    'id' : 3,
    'title' : 'I\'m starving...',
    'body' : 'On nana On na On nanana deal car',
}

print(diary)
print(type(diary))

# dumps: json 형식의 문자열로 변환해주는 함수
diary_s = json.dumps(diary)

print(diary_s)
print(type(diary_s))

# loads: json 형식의 문자열을 원래 형식으로 역변환
diary_back = json.loads(diary_s)

print(diary_back)
print(type(diary_back))