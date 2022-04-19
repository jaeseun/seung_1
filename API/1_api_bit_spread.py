## bithumb key 는 메일에서 승인후 작동
from logging import exception
import pybithumb                                               # 빗썸의 Public API 1초 20회, Private API 1초10회가능
import time                                                    # API는초당20회 호출가능 초과시 일정시간API 차단            
tickers = pybithumb.get_tickers()                              # tickers.티커.시세표시기
from random import randint
bithumb = pybithumb.Bithumb('0caf7146ad31562f84a5d2fe85718af6', '1b05df244296ee51adb774dc8f188a07')
### 매도 뿌리기 ====================================================================================================
turn = 5
order_list = []
try:
    for i in range(turn):
        name = 'XRP' 
        good_price =pybithumb.get_orderbook(name)['asks'][0]['price'] 
        good_cnt =pybithumb.get_orderbook(name)['asks'][0]['quantity']
        call_price = (good_price + randint(1, 5))                               # 주문가 : 호가 + 랜덤 선택 범위
        # call_cnt = (good_cnt + randint(10, 20))                               # 주문량 : 호가잔여수량 + 랜덤 선택범위
        call_cnt = (randint(10, 20))                                            # 주문량 : 테스트용
        order = bithumb.sell_limit_order(name, call_price, call_cnt)            # 주문
        order_list.append(order)                                                # [('ask', 'XRP', 'C0106000000375455064', 'KRW')]
        time.sleep(0.5)
        print('{}--> 호가 [{:,}원] 매도가 [{:,}원 ▲ {:,}원] / [{:,}원 {:,}개]뿌리기 매도 --> {}'
        .format(i, good_price , call_price, call_price-good_price, call_cnt*call_price, call_cnt, order))
        print('-'*120) 
except:
    print('자동매도 거래를 실패하였습니다!')

time.sleep(20)                                                                  # time sleep(10) 10초후 지정가 매도 취소
try:
    for i, t in enumerate(order_list):                                                       # [('ask', 'XRP', 'C0106000000375455064', 'KRW')]
        cancel = bithumb.cancel_order(t)                                       # 지정가매도 취
        print('{}--> {}--> 거래가 취소되었습니다!'.format(i, t))
        print('-'*120)
        time.sleep(10)
except:
    print('자동취소 거래를 실패하였습니다!')

