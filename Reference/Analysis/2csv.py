### csv comma separated values [separated.세퍼레이드.분리]
# 인코딩과 디코딩 : ★문자를 코드로(encoding) / ★코드를 문자로 (decoding) 'euc-kr' = 한글코드표

# from ast import operator
import csv
f = open('cad.csv',encoding='euc-kr')         # 1.파일열기 _ 변수 f 에 open cad.csv / 형식은 encoding='euc-kr'  
data = csv.reader(f)                          # 2.파일읽기 _ reader(f) 읽는자 변수f
# writer = csv.writer(f)                                                  # [writer.라이터.작가] 의해 파일을 쓸수있음
next(data)                                    # 3.헤더제거하기 첫줄 next 하고 다음줄부터(첫줄 헤더제거) 
data = list(data)                             # 4. list 변환하기
# print(data,end=' ')

##### 기본1 (row start = 0) -------------------------------------------------------------------------------------------
# for row in data:                              # range(0,len(data)):
#     if row[8] == '전매입':
#         date = row[0]
#         pay = int(row[6])
#         nam = row[5]
#         print('구매확정',date,'당시', nam ,'에서', pay,'원',row[8])
#     else:
#         date = row[0]
#         pay = int(row[6])
#         nam = row[5]
#         print('구매취소',date,'당시', nam ,'에서', pay,'원',row[8])
##### 월별지출내역분석------------------------------------------------------------------------------------------------
s_mon = [0]*3                                    # 10월,11월,12월
for row in data:
    if row[-1] == '전매입':                                       # 만약 row[-1]이 '전매입'과 같은데이터라면  
        mon , pay = row[0].split('-')[1] , int(row[6])          # 날짜 를 리스트로 나누어 리스트[1]을 획득함
        index1 = int(mon) - 10                                  # (10,11,12) - 10 =  0,1,2 획득
        s_mon[index1]+= pay                                     # pay를 누적 리스트 0,1,2 에 넣음    
        # s_mon[int(row[0].split('-')[1])-10] += int(row[6])     # 코드줄임 기본에서출발하면 s_mon[0]+=int(row[-3])
        print(s_mon[index1])

s_mon = [0]*3
print(s_mon)
##### 택시비내역분석------------------------------------------------------------------------------------------------
# taxi = [ 0 , 0 , 0 ]                                             # 월별합계
# for row in data:
#     if row[-1] == '전매입' and '우아한형제들' in row[5]:         # 만약 row[-1]이 '전매입'과 같고 row[5]에 '택시'데이터가 있다면                     
#         mon , pay = row[0].split('-')[1] , int(row[-3])         # 날짜 를 리스트로 나누어 리스트[1]을 획득함
#         index1 = int(mon) - 10                                  # 요놈이 0,1,2 로 반복변함
#         taxi[index1]+= pay                                      # pay를 누적 리스트 0,1,2 에 넣음    
#         taxi[int(row[0].split('-')[1])-10] += int(row[-3])      # ★★★ 코드줄임 기본에서출발하면 taxi[0]+=int(row[-3])

##### {}딕셔너리변환 {업체:지출액} 데이터 분석--------------------------------------------------------------------------------
# from operator import* #[operator 오퍼레이터(운영자)][import.들여오다] # 계산을 도와주는 라이브러리 
spending = {}
for row in data:
    if row[8] == '전매입':
        name , pay = row[5] , int(row[-3])
        if name not in spending.keys():
            spending[name] = pay
        else:
            spending[name] += pay
# top10 = sorted(spending.items(), key = itemgetter(1) , reverse = True) [:10] # 오름의 거꾸로 내림 [geter.겟터.획득.제거]
# x , y = [] , []
# for i in top10: # for m,v in manu.items(): 
#     x.append(i[0])
#     y.append(i[1])        
# plt.title('top 지출현황')     
# plt.barh(x, y, color = 'r', label = '(top10 지출)')                 # ★바차트횡방향★ - barh(횡방향 바)-h는horizontal로방향바꾸기
# plt.legend(loc = 'upper left')                                      # label위치 /center.lower.upper/center.right.left/   
# plt.xlabel('[목 록]')                                               # X축 이름   
# plt.ylabel('[금 액]')                                               # y축 이름   
# plt.show()                                                          # pip 출력   