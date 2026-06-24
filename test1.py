# 한글 형태소 분석기 사용 테스트1

# Hananum: KAIST 말뭉치를 이용해서 생성된 사전 분석기
from konlpy.tag import Hannanum

hannanum = Hannanum()

# 제공 메소드 : 레퍼런스.메소드명() 사용
# analyze(): 구(parse) 분석
# morphs(): 형태소 분석
# nouns(): 명사만 분석
# pos(): 형태소 분석 + 태깅

# 사용
print('Hannanum 분석기 이용 --------------------')
text = u'길동 마트의 흑마늘 양념 치킨이 논란이 되고 있다.'
print(hannanum.analyze(text))
print(hannanum.morphs(text))
print(hannanum.nouns(text))
print(hannanum.pos(text))

# KKma (꼬꼬마): 세종 말뭉치를 이용해 생성된 사전 분석기 (서울대 제작)
from konlpy.tag import Kkma

kkma = Kkma()

# 메소드 정리
# sentences(): 문장분석
# morphs(): 형태소 분석
# nouns(): 명사만 분석
# pos() : 형태소 분석 + 태깅

print('KKma 분석기 이용 ------------------------------------')

print(kkma.sentences(text))
print(kkma.morphs(text))
print(kkma.nouns(text))
print(kkma.pos(text))

# Komoran : Java로 만들어진 오픈소스 한글 형태소 분석기
from konlpy.tag import Komoran
kom = Komoran()

print('Komoran 분석기 이용 ---------------------------------')

print(kom.morphs(text))
print(kom.nouns(text))
print(kom.pos(text))

# Twitter (Okt) : 오픈소스 한글 형태소 분석기
from konlpy.tag import Okt
okt = Okt()

print('Okt 분석기 이용 -------------------------------------')

print(okt.phrases(text))
print(okt.morphs(text))
print(okt.nouns(text))
print(okt.pos(text))

# stem : 각 단어에서 어간 추출 처리 매개변수

print('Okt method : stem parameter using ---------------------')
print(okt.morphs(text, stem=True))