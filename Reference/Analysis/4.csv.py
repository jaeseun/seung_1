#### 주중 주말 시간대별 평균인구
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

import datetime as dt
weekday = [0 for i in range(24)]                    # [0,0,0....23개] 1차원리스트 생성 ★★★ list 를 만듬과 동시에 초기화 [리스트내포 라함]
weekend = [0 for i in range(24)]                    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for row in data:
    if row[2] == d_code:
        y , m , d = int(row[0][:4]) , int(row[0][4:6]) , int(row[0][6:]) # 날짜 년.월.일 slicing
        num = dt.date( y , m , d ). weekday()        # ★★★★ 날짜를 요일 1에서7까지표기 / 5>i 주중 / 5<i 주말 
        if num < 5:
            weekday[row[1]] += row[3]                # row[1]시간int 0에서23까지 / row[3]인구int value     
        else:
            weekend[row[1]] += row[3]                # 최초값 0 에 +=row[3] 누적합
#### 주중주말 일수구하기
weekday_cnt , weekend_cnt = 0 , 0
for i in range(1, 32):
    if dt.date(2019,12,i).weekday() < 5:
        weekday_cnt += 1
    else:
        weekend_cnt += 1
weekday = [w/weekday_cnt for w in weekday] 
weekend = [w/weekend_cnt for w in weekend]