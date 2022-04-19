
# from cProfile import label
# from random import randint
# from matplotlib import pyplot as plt                  # 명령어줄여쓰기 as 란 : pyplot.plot(a, b) --> plt.plot(a, b)
# from numpy import append

# plt.figure(dpi = 100)                                 # 그래프크기조정(해상도조정) [dot per inch] 도트 퍼 인치 (점 당 인치)
# # plt.figure(figsize = (8, 4))                          # 그래프크기조정(가로x세로)
# plt.rc('font', family ='malgun gothic')               # 한글 글꼴설정

##### 꺽은선그래프------------------------------------------------------------------------------------------------------------
# x = ['월','화','수','목','금','토','일']
# y1 , y2 = [1,5,7,8,6,2,4] , [2,4,6,9,5,1,5]                 # range()형적용검토 / 기타 for.if 가능할것같음
# plt.title('꺽은선그래프')   
# plt.plot(x, y1, color = 'y', label = '(첫째주)')           # ★꺽은선★ color r.g.b 형 색넣기 /  label(범래)
# plt.plot(x, y2, color = 'r', label = '(둘째주)')
# plt.legend(loc = 'upper left')                              # label위치 /center.lower.upper/center.right.left/   
# plt.xlabel('[요 일]')                                       # X축 이름   
# plt.ylabel('[매 출]')                                       # y축 이름   
# plt.show()                                                  # pip 출력        
##### 바차트횡 단일-------------------------------------------------------------------------------------------------------
# x = ['월','화','수','목','금','토','일']
# y = [1,5,7,8,6,2,4]
# plt.title('바차트횡')   
# plt.rcParams['axes.unicode_minus'] = False                  # 마이너스 표기설정  
# plt.barh(x, y, color = 'r', label = '(첫째주)')            # ★바차트횡방향★ - barh(횡방향 바)-h는horizontal로방향바꾸기
# plt.legend(loc = 'upper left')                              # label위치 /center.lower.upper/center.right.left/   
# plt.xlabel('[요 일]')                                       # X축 이름   
# plt.ylabel('[매 출]')                                       # y축 이름   
# plt.show()                                                  # pip 출력        
##### 바차트횡 이중  -------------------------------------------------------------------------------------------------------
# x = ['월','화','수','목','금','토','일']
# y1 , y2 = [1,5,7,8,6,2,4] , [-2,-4,-6,-9,-5,-1,-5]          # range()형적용검토 / 기타 for.if 가능할것같음
# plt.title('바차트횡')   
# plt.rcParams['axes.unicode_minus'] = False                  # 마이너스 표기설정  
# plt.barh(x, y1, color = 'y', label = '(첫째주)')            # ★바차트횡방향★ - barh(횡방향 바)-h는horizontal로방향바꾸기
# plt.barh(x, y2, color = 'r', label = '(둘째주)')
# plt.legend(loc = 'upper left')                              # label위치 /center.lower.upper/center.right.left/   
# plt.xlabel('[요 일]')                                       # X축 이름   
# plt.ylabel('[매 출]')                                       # y축 이름   
# plt.show()                                                  # pip 출력        
##### 바차트종 단일-------------------------------------------------------------------------------------------------------
# y = [1,5,7,8,6]
# plt.title('바차트횡')   
# plt.bar(range(1 , 6 ), y, label = '(첫째주)', color = 'r')
# plt.xticks(range(1 , 6) , ['첫째','둘째','셋째','넷째','다섯째'])
# plt.legend(loc = 'upper left')                              # label위치 /center.lower.upper/center.right.left/   
# plt.xlabel('[요 일]')                                       # X축 이름   
# plt.ylabel('[매 출]')                                       # y축 이름   
# plt.show()                                                  # pip 출력        
##### 바차트종 이중1-------------------------------------------------------------------------------------------------------
# y1 , y2 = [1,5,7,8,6] , [2,4,6,9,3]                 # range()형적용검토 / 기타 for.if 가능할것같음
# plt.title('바차트횡')   
# plt.bar(range(1 , 6 ), y1, label = '(첫째주)', color = 'y')            # ★바차트횡방향★ - barh(횡방향 바)-h는horizontal로방향바꾸기
# plt.bar(range(7 , 12), y2, label = '(둘째주)', color = 'r')
# plt.xticks(range(1 , 12) , ['첫째','둘째','셋째','넷째','다섯째','','첫째','둘째','셋째','넷째','다섯째'])
# plt.legend(loc = 'upper left')                              # label위치 /center.lower.upper/center.right.left/   
# plt.xlabel('[요 일]')                                       # X축 이름   
# plt.ylabel('[매 출]')                                       # y축 이름   
# plt.show()                                                  # pip 출력        
##### 바차트종 이중2-------------------------------------------------------------------------------------------------------
# y1 , y2 = [1,5,7,8,6] , [2,4,6,9,3]                 # range()형적용검토 / 기타 for.if 가능할것같음
# plt.title('바차트횡')   
# plt.bar(range(1 , 14 , 3 ), y1, label = '(첫째주)', color = 'y')            # ★바차트횡방향★ - barh(횡방향 바)-h는horizontal로방향바꾸기
# plt.bar(range(2 , 15 , 3 ), y2, label = '(둘째주)', color = 'r')
# plt.xticks(range(1 , 14 , 3) , ['첫째','둘째','셋째','넷째','다섯째'])
# plt.legend(loc = 'upper left')                              # label위치 /center.lower.upper/center.right.left/   
# plt.xlabel('[요 일]')                                       # X축 이름   
# plt.ylabel('[매 출]')                                       # y축 이름   
# plt.show()                                                  # pip 출력        
##### 히스토그램(빈도)--------------------------------------------------------------------------------------------------------
# a = [2,7,5,4,7,7,8,4,5,6,3,5,7,8,]
# plt.title('히스토그램 그래프')   
# plt.hist(a, color = 'r', label = '(단위: 수량)', bins=15)   # ★히스토그램_분포차트★ 데이터하나만 / bins(구간분포:2에서8까지를 10개로)
# plt.legend(loc = 'lower right')                            # [legend 레전드] label(범래)의 위치지정 
# plt.xlabel('[요일]')                                       # X축 이름   
# plt.ylabel('[빈도]')                                       # y축 이름   
# plt.show()
##### 파이차트(빈도)-----------------------------------------------------------------------------------------------------
# plt.title('파이차트')   
# a = [12,4,7,2]
# b = ['a형','b형','c형','o형']
# plt.pie(a, labels = b, autopct='%1.1f%%')
# plt.show()
##### 산점도-------------------------------------------------------------------------------------------------------------
# x , y = [], []
# for i in range(50):
#     x.append(randint(10,200))
#     y.append(randint(20,300))
# plt.title('산점도')
# plt.scatter(x, y, s=x, c = y, alpha=0.5, cmap='Spectral')   # c=사이즈 /  alpha.알파.투명도 / cmap.컬러맵      
# plt.colorbar(label = '키')                                     # 종방향 바 라벨 
# plt.xlabel('[키]')   
# plt.ylabel('[몸무게]')   
# plt.show()
##### 산점도 이중-------------------------------------------------------------------------------------------------------------
# x1 , x2 , y1 , y2 = [] , [] , [] ,[]
# for i in range(50):
#     x1.append(randint(10,200))
#     y1.append(randint(20,300))
#     x2.append(randint(10,200))
#     y2.append(randint(20,300))
# plt.title('산점도이중')
# plt.scatter(x1, y1, s=x1, color = 'crimson', alpha=0.5, label='그룹1')      
# plt.scatter(x2, y2, s=x2, color = 'indigo', alpha=0.5, label='그룹2')
# plt.colorbar(label = '키')                                     # 종방향 바 라벨 
# plt.legend(loc = 'upper left')                                # label위치 /center.lower.upper/center.right.left/ 
# plt.xlabel('[키]')   
# plt.ylabel('[몸무게]')   
# plt.show()
##### 캔들-(그래프에대한 공부필요)------------------------------------------------------------------------------------------
# t1 = [80,20,50,20,10,50,60,30,60]
# t2 = [70,10,40,60,30,70,20,20,50]
# t3 = [50,60,40,10,30,40,70,20,40]
# plt.boxplot([t1,t2,t3], labels = ['국어점수','영어점수','수학점수'])
# plt.show()