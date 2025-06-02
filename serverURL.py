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
Apply_VST = "/openApi/swap/v1/trade/getVst"

# 延遲全部撤單（Cancel All After） / POST
# 倒數計時結束後，系統會撤銷目前所有掛單。
# 此請求可以持續發送，以不斷延長“懲罰”倒數時間。
Cancel_All_After = "/openApi/swap/v2/trade/cancelAllAfter"

# Cancel All Open Orders / DELETE
# 全部取消未成交掛單
# 取消當前帳戶下所有處於委託（掛單）狀態的訂單。
Cancel_All_Open_Orders = "/openApi/swap/v2/trade/allOpenOrders"

# 取消訂單 / DELETE
# 取消當前帳戶中處於委託狀態的訂單。
Cancel_Order = "DELETE /openApi/swap/v2/trade/order"

# 取消 TWAP 訂單（Cancel TWAP Order） / POST
Cancel_TWAP_Order = "/openApi/swap/v1/twap/cancelOrder"

# 撤銷現有訂單並發送新訂單 / POST
Cancel_an_Existing_Order_and_Send_a_New_Order = "/openApi/swap/v1/trade/cancelReplace"

# 批量取消訂單 / DELETE
Cancel_multiple_orders = "/openApi/swap/v2/trade/batchOrders"

# 批次撤單與批次下單 / POST
Cancel_orders_in_batches_and_place_orders_in_batches = "/openApi/swap/v1/trade/batchCancelReplace"

# 切換保證金模式 / POST
# 更改用戶在指定合約品種下的保證金模式：逐倉、全倉或獨立逐倉。
Change_Margin_Type = "/openApi/swap/v2/trade/marginType"

# 全部平倉 / POST
Close_All_Positions = "/openApi/swap/v2/trade/closeAllPositions"

# 根據持倉ID平倉（Close position by position ID） / POST
Close_position_by_position_ID = "/openApi/swap/v1/trade/closePosition"

# 查詢目前全部掛單 / GET
# 查詢用戶目前所有處於委託（掛單）狀態的訂單。
Current_All_Open_Orders = "/openApi/swap/v2/trade/openOrders"

# 對沖模式持倉 - 自動追加保證金 / POST
# Hedge mode Position - Automatic Margin Addition
# 在對沖模式下，支持設置和取消「自動追加保證金」功能。
Hedge_mode_Position = "/openApi/swap/v1/trade/autoAddMargin"

# 逐倉保證金調整歷史（Isolated Margin Change History） / GET
Isolated_Margin_Change_History = "/openApi/swap/v1/positionMargin/history"

# 調整逐倉持倉保證金 / POST
Modify_Isolated_Position_Margin = "/openApi/swap/v2/trade/positionMargin"

# 一鍵反向持倉（One-Click Reverse Position） / POST
One_Click_Reverse_Position = "/openApi/swap/v1/trade/reverse"

# 下達 TWAP 訂單（Place TWAP Order） / POST
# 建立一個時間加權平均價格（TWAP）訂單。
Place_TWAP_Order = "/openApi/swap/v1/twap/order"

# 批量下單 / POST
Place_multiple_orders = "/openApi/swap/v2/trade/batchOrders"

# 模擬交易下單 / POST
Place_order_in_demo_trading = "/openApi/swap/v2/trade/order"

# 開倉 / POST
Place_order = "/openApi/swap/v2/trade/order"

# 倉位與維持保證金率（Position and Maintenance Margin Ratio） / GET
# 獲取倉位及維持保證金率的相關資訊
Position_and_Maintenance_Margin_Ratio = "/openApi/swap/v1/maintMarginRatio"

# 查詢槓桿與可開倉數量 / GET
# 查詢用戶在指定合約品種下的開倉槓桿倍數與可開倉數量。
Query_Leverage_and_Available_Positions = "/openApi/swap/v2/trade/leverage"

# 查詢保證金模式 / GET
# 查詢用戶在指定合約品種下的保證金模式：逐倉、全倉或獨立逐倉。
Query_Margin_Type = "/openApi/swap/v2/trade/marginType"

# 查詢多資產保證金（Query Multi-Assets Margin） / GET
# 查詢多資產模式下的保證金
Query_Multi_Assets_Margin = "/openApi/swap/v1/user/marginAssets"

# 查詢多資產模式（Query Multi-Assets Mode） / GET
# 查詢帳戶多資產模式
Query_Multi_Assets_Mode = "/openApi/swap/v1/trade/assetMode"

# 查詢多資產規則（Query Multi-Assets Rules） / GET
# 查詢平台定義的多資產規則
Query_Multi_Assets_Rules = "/openApi/swap/v1/trade/multiAssetsRules"

# 查詢訂單歷史紀錄 / GET
# 查詢用戶的歷史訂單（訂單狀態為已完成或已取消）。
Query_Order_history = "/openApi/swap/v2/trade/allOrders"

# 查詢持倉歷史（Query Position History） / GET
# 查詢當前帳戶下永續合約的持倉歷史記錄。
Query_Position_History = "/openApi/swap/v1/trade/positionHistory"

# 查詢 TWAP 委託單（Query TWAP Entrusted Order） / GET
Query_TWAP_Entrusted_Order = "/openApi/swap/v1/twap/openOrders"

# 查詢 TWAP 歷史訂單（Query TWAP Historical Orders） / GET
Query_TWAP_Historical_Orders = "/openApi/swap/v1/twap/historyOrders"

# 查詢歷史成交明細 / GET
# 獲取某一交易對的歷史成交記錄明細
Query_historical_transaction_details = "/openApi/swap/v2/trade/fillHistory"

# 查詢歷史成交訂單 / GET
# 查詢某個交易對的成交歷史紀錄
Query_historical_transaction_orders = "/openApi/swap/v2/trade/allFillOrders"

# 查詢掛單狀態 / GET
Query_pending_order_status = "/openApi/swap/v2/trade/openOrder"

# 查詢持倉模式 / GET
Query_position_mode = "/openApi/swap/v1/positionSide/dual"

# 查詢訂單詳情 / GET
Query_Order_details = "/openApi/swap/v2/trade/order"

# 設定槓桿倍數 / POST
# 調整用戶在指定合約品種下的開倉槓桿倍數。
Set_Leverage = "/openApi/swap/v2/trade/leverage"

# 設定持倉模式 / POST
# 用於設定永續合約的持倉模式，支援雙向持倉模式與單向持倉模式
Set_Position_Mode = "/openApi/swap/v1/positionSide/dual"

# 切換多資產模式（Switch Multi-Assets Mode） / POST
# 切換帳戶多資產模式
Switch_Multi_Assets_Mode = "/openApi/swap/v1/trade/assetMode"

# 用於查詢 TWAP 委託訂單的詳細資訊 / GET
TWAP_Order_Details = "/openApi/swap/v1/twap/orderDetail"

# 測試下單 / POST
Test_Order = "/openApi/swap/v2/trade/order/test"

# 用戶強制平倉訂單。 / GET
# 查詢用戶的強制平倉訂單。
User's_Force_Orders = "/openApi/swap/v2/trade/forceOrders"


"""-END-"""
