# 放伺服器位址。
# 集中管理所有 API 路徑（V1/V2/V3）。

# 根網址
API_URL = "https://open-api.bingx.com"
API_URL_VST = "https://open-api-vst.bingx.com" #模擬倉專用

# ... 依需求加入其他API路徑
# Market-Data = 12個 => 2025/06/01

# 24小時行情價格變動統計 / GET
24hr_Ticker_Price_Change_Statistics = "/openApi/swap/v2/quote/ticker"

# K線 = 蠟燭圖資料 / GET
Candlestick_Data = "/openApi/swap/v3/quote/klines"

# 取得資金費率歷史紀錄 / GET
Get_Funding_Rate_History = "/openApi/swap/v2/quote/fundingRate"

# "標記價格" K線 = 蠟燭圖資料 / GET
Mark_Price_Kline_Candlestick_Data = "/openApi/swap/v1/market/markPriceKlines" 

# 標記價格與資金費率 / GET
Mark_Price_and_Funding_Rate = "openApi/swap/v2/quote/premiumIndex"

# 未平倉合約統計 / GET
Open_Interest_Statistics = "openApi/swap/v2/quote/openInterest"

# 訂單簿 / GET
Order_Book = "/openApi/swap/v2/quote/depth"

# 查詢歷史交易訂單 / GET
Query_historical_transaction_orders = "/openApi/swap/v1/market/historicalTrades"

# 近期成交列表 / GET
Recent_Trades_List = "/openApi/swap/v2/quote/trades"

# 交易對訂單薄行情 / GET
Symbol_Order_Book_Ticker = "/openApi/swap/v2/quote/bookTicker"

# 交易對價格行情 / GET
Symbol_Price_Ticker = "/openApi/swap/v1/ticker/price"

# USDT-M 永續合約交易對 / GET
USDT_M_Perp_Futures_symbols = "/openApi/swap/v2/quote/contracts"


# 
# Account-Endpoints = 5個 => 2025/06/01
# 跟帳戶操作有關的東西

# 匯出資金流向資料 / GET
Export_fund_flow = "/openApi/swap/v2/user/income/export"

# 取得帳戶盈虧資金流向 = 查詢當前帳戶下永續合約的資金流動情況 / GET
Get_Account_Profit_and_Loss_Fund_Flow = "/openApi/swap/v2/user/income"

# 查詢交易手續費率 = 取得當前使用者的交易費率 / GET
Query_Trading_Commission_Rate = "openApi/swap/v2/user/commissionRate"

# 查詢帳戶資料 = 取得使用者USDC和USDT永續合約帳戶的資產資訊 / GET
Query_account_data = "/openApi/swap/v3/user/balance"

# 查詢持倉資料 = 取得使用者永續合約持倉資訊 / GET
Query_position_data = "/openApi/swap/v2/user/positions"


# 
# Trades-Endpoints = 42個 => 2025/06/01
# 跟倉位操作有關的東西

# 所有訂單查詢（All Orders） / GET
# 查詢用戶的歷史訂單（訂單狀態包含：已完全成交、待成交、新建、部分成交、已取消）。
All_Orders_Query_the_user's_historical_orders = "/openApi/swap/v1/trade/fullOrder"

# 申請 VST 資產以進行模擬交易 / POST
Apply VST = "/openApi/swap/v1/trade/getVst"

# 延遲全部撤單（Cancel All After） / POST
# 倒數計時結束後，系統會撤銷目前所有掛單。
# 此請求可以持續發送，以不斷延長“懲罰”倒數時間。
Cancel_All_After = "/openApi/swap/v2/trade/cancelAllAfter"










































SWAP_POSITION_DUAL = '/openApi/swap/v1/positionSide/dual'
USER_COMMISSION_RATE = '/openApi/swap/v2/user/commissionRate'
