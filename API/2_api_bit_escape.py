## bithumb key 는 메일에서 승인후 작동
import pybithumb                                               # 빗썸의 Public API 1초 20회, Private API 1초10회가능
import time                                                    # API는초당20회 호출가능 초과시 일정시간API 차단            
tickers = pybithumb.get_tickers()                              # tickers.티커.시세표시기
con_key ='0caf7146ad31562f84a5d2fe85718af6'
sec_key ='1b05df244296ee51adb774dc8f188a07'
bithumb = pybithumb.Bithumb(con_key, sec_key)

### 매도 던기기 =======================================================================================================
try:
    for i in range(5):
        name = 'XRP' 
        good_price =pybithumb.get_orderbook(name)['asks'][0]['price']
        good_cnt =pybithumb.get_orderbook(name)['asks'][0]['quantity']
        # from_sell = bithumb.sell_limit_order(name, good_price, good_cnt)
        time.sleep(0.2)        
        print('{}--> 호가 [{:,}원] --> [{:,}개 : {:,}원] 던지기 매도'.
        format(i, good_price, good_cnt, good_price* good_cnt))
        print('-'*120) 
        
except:
    print('자동매도 거래를 실패하였습니다!')