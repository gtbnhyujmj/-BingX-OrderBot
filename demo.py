# 各類 demo = 功能主體
# 從BingX API文件貼過來的
# 真正的"虛擬信件"的內容擺在這邊

from .endpoints import SWAP_POSITION_DUAL
from .requester import send_request

# 24小時行情價格變動統計
def 24hr_Ticker_Price_Change_Statistics():
    paramsMap = {
        "symbol": "SFP-USDT",  # 交易對符號，需包含連字號，如 SFP-USDT
        "timestamp": "1702719836770"  # 請求時間戳，單位：毫秒
    }
    
# K線 = 蠟燭圖資料
def Candlestick_Data():
    paramsMap = {
        "symbol": "KNC-USDT",  # 交易對，需包含連字號，如 KNC-USDT
        "interval": "1h",  # K 線時間間隔，例：1 小時
        "limit": "1000",  # 限制回傳資料數量，例：1000 筆
        "startTime": "1702717199998"  # 起始時間戳，單位：毫秒
    }

# 取得資金費率歷史紀錄
def Get_Funding_Rate_History():
    paramsMap = {
        "symbol": "QNT-USDT",  # 交易對，需包含連字號，例如 QNT-USDT
        "limit": 2  # 限制回傳資料筆數，這裡設定為 2 筆
    }

# "標記價格" K線 = 蠟燭圖資料
def Mark_Price_Kline_Candlestick_Data():
    paramsMap = {
        "symbol": "KNC-USDT",  # 交易對，需包含連字號，如 KNC-USDT
        "interval": "1h",  # K 線時間間隔，例：1 小時
        "limit": "1000",  # 限制回傳資料筆數，例：1000 筆
        "startTime": "1702717199998"  # 起始時間戳，單位：毫秒
    }

# "標記價格"與資金費率
def Mark_Price_and_Funding_Rate():
    paramsMap = {
        "symbol": "BTC-USDT"  # 交易對符號，必須包含連字號，如 BTC-USDT
    }
    
# 未平倉合約統計
def Open_Interest_Statistics():
    paramsMap = {
        "symbol": "EOS-USDT"  # 交易對，需包含連字號，如 EOS-USDT
    }

# 訂單簿 (Order Book)
def Order_Book():
    paramsMap = {
        "symbol": "SHIB-USDT",  # 交易對，範例為 SHIB 對 USDT
        "limit": "5"  # 限制返回的訂單數量，這裡取 5 條
    }

# 查詢歷史交易訂單
def Query_historical_transaction_orders():
    paramsMap = {
        "fromId": "412551",  # 從此交易 ID 開始返回資料
        "limit": "500",  # 回傳最大結果數，最大為 100
        "symbol": "ETH-USDT",  # 交易對，需包含連字號，如 ETH-USDT
        "timestamp": "1702731995838",  # 請求時間戳，單位：毫秒
        "recvWindow": "60000"  # 請求有效時間窗，單位：毫秒
    }

# 近期成交列表 (Recent Trades List)
def Recent_Trades_List():
    paramsMap = {
        "symbol": "BTC-USDT",  # 交易對符號，必須包含連字號，如 BTC-USDT
        "limit": 10  # 查詢限制，回傳最近 10 筆成交
    }

# 交易對訂單薄行情 (Symbol Order Book Ticker)
def Symbol_Order_Book_Ticker():
    paramsMap = {
        "symbol": "BTC-USDT",  # 交易對，必須包含連字號，如 BTC-USDT
        "timestamp": "1702719942130"  # 請求時間戳，單位：毫秒
    }

# 交易對價格行情 (Symbol Price Ticker)
def Symbol_Price_Ticker():
    paramsMap = {
        "timestamp": "1702718923479",  # 請求時間戳，單位：毫秒
        "symbol": "TIA-USDT"  # 交易對，需包含連字號，如 TIA-USDT
    }

# USDT-M 永續合約交易對
def USDT_M_Perp_Futures_symbols():
    paramsMap = {}  # URL 參數字典，目前沒有額外參數










































































































































































def set_dual_side_position(dual_side=True):
    params = {
        "dualSidePosition": str(dual_side).lower(),
        "timestamp": "1702731530753"  # 需動態生成
    }
    return send_request("POST", SWAP_POSITION_DUAL, params)
