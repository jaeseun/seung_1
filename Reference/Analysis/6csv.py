#### 다른지역과 인구비교
### csv comma separated values [separated.세퍼레이드.분리]
#인코딩과 디코딩 : ★문자를 코드로(encoding) / ★코드를 문자로 (decoding) 'euc-kr' = 한글코드표
##### 인구(ingu_code)데이터 읽어들이기-------------------------------------------------------------------------------------------
import csv
f = open('ingu_code.csv',encoding='euc-kr')        # 1.파일열기 _ 변수 f 에 open cad.csv / 형식은 encoding='euc-kr'/ 'cp949' / 'utf8'  
data = csv.reader(f)                               # 2.파일읽기 _ reader(f) 읽는자 변수f
next(data)                                         # 3.헤더제거하기 첫줄 next 하고 다음줄부터(첫줄 헤더제거) 
data = list(data)                                  # 4. list 변환하기 [[,,,],[,,,],[,,,]]
#### 동(dong_code)데이터 읽어들이기-------------------------------------------------------------------------------------------
f2 = open('dong_code.csv',encoding='euc-kr')       # 1.파일열기 _ 변수 f 에 open cad.csv / 형식은 encoding='euc-kr'/ 'cp949' / 'utf8'  
data1 = csv.reader(f2)                             # 2.파일읽기 _ reader(f) 읽는자 변수f
next(data1)                                        # 3.헤더제거하기 첫줄 next 하고 다음줄부터(첫줄 헤더제거) 
next(data1)
data1 = list(data1)                                # 4. list 변환하기 [[,,,],[,,,],[,,,]]★★★
##### 인구 data --> 숫자형으로
for row in data:                                   # data[[0,r,o,w],[1,r,o,w],[2,r,o,w]] 이차원리스트★★★
    for i in range(1, 32):          
        if i <= 2:
            row[i] = int(row[i])
        else:
            row[i] = float(row[i])
# #### 동 data1 --> 숫자형으로
for row in data1:
    row[1] = int(row[1])
# #### data1 row[-1]열과 같다면 d_code에 row[1]을 참조 
name = '압구정동' # 에 행정코드 찾기
for row in data1:
    if row[-1] == name:  
        d_code = row[1]
name1 = '역삼2동' # 에 행정코드 찾기
for row in data1:
    if row[-1] == name1:  
        d_code1 = row[1]

apg = [0 for i in range(24)]                    # [0,0,0....23개] 1차원리스트 생성 ★★★ list 를 만듬과 동시에 초기화 [리스트내포 라함]
uks = [0 for i in range(24)]                    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for row in data:
    if row[2] == d_code:
        apg[row[1]] += row[3]                  # 압구정동인구 총합
    elif row[2] == d_code1:
        uks[row[1]] += row[3]                  # 역삼2동인구  총합
apg = [a/31 for a in apg] 
uks = [u/31 for u in uks]
# #### 그래프 그리기
from matplotlib import pyplot as plt                  # 명령어줄여쓰기 as 란 : pyplot.plot(a, b) --> plt.plot(a, b)
plt.figure(figsize = (7, 4))                          # 그래프크기조정(가로x세로)
plt.rc('font', family ='malgun gothic')               # 한글 글꼴설정
plt.title(name + name1 +'시간대별평균인구')   
plt.plot(range(24), apg, color = 'y', label = '압구정동')    # ★꺽은선★ color r.g.b 형 색넣기 /  label(범래)
plt.plot(range(24), uks, color = 'r', label = '역삼2동')     # ★꺽은선★ color r.g.b 형 색넣기 /  label(범래)
plt.xticks(range(24),range(24))                             # x축 눈금간격
plt.legend(loc = 'upper left')                              # label위치 /center.lower.upper/center.right.left/   
plt.xlabel('[시간대]')                                      # X축 이름   
plt.ylabel('[평균인구]')                                    # y축 이름   
plt.show()                                                  # pip 출력