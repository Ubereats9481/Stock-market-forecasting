import pandas as pd
import numpy as np

def simulate_trading(predictions, test_data, top_k=10, slippage_cost=0.002):
    # 功能: 模擬交易策略 ("買入預測機率最高的 k 支股票，賣空預測機率最低的 k 支股票")，計算每日報酬率。包含交易成本 (slippage_cost)。
    # 輸入:  預測機率 predictions、測試資料 test_data、買賣股票數量 top_k 和滑價成本 slippage_cost。
    # 輸出:  Pandas DataFrame 格式的每日報酬率 (columns: 'Long', 'Short')。
    pass