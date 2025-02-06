import pandas as pd
import numpy as np
from sklearn.preprocessing import RobustScaler

def load_data(data_path):
    # 功能: 讀取您的資料集。data_path 為資料集檔案路徑。
    # 輸出: Pandas DataFrame 或 NumPy array 格式的原始資料。您需要根據您的資料集格式調整讀取方式 (例如 pd.read_csv, pd.read_excel 等)。
    pass

def preprocess_data(df):
    # 功能: 進行資料預處理，例如處理缺失值、異常值等。 根據您的資料集特性決定是否需要此步驟和具體處理方法。
    # 輸入: 原始資料 DataFrame。
    # 輸出:  預處理後的 DataFrame。
    pass

def feature_engineering(df, history_window=240):
    # 功能:  根據論文方法建立 LSTM 模型所需的特徵 (Intraday returns, Returns with respect to last closing price, Returns with respect to opening price)。使用過去 history_window 天的資料。
    # 輸入: 預處理後的 DataFrame 和歷史回溯窗口大小 history_window。
    # 輸出:  包含特徵的 DataFrame。
    pass

def create_labels(feature_df, label_type='intraday_return', quantiles=[0.5, 0.5]):
    # 功能: 根據股價報酬率 (label_type)，將股票分為兩個類別 (Class 0 和 Class 1)，使用分位數 quantiles 劃分。
    # 輸入: 包含特徵的 DataFrame、標籤類型 label_type 和分位數 quantiles。
    # 輸出:  包含標籤的 DataFrame。
    pass

def prepare_data_for_lstm(feature_label_df, stock_list, test_year, history_window=240, ):
    # 功能: 將特徵和標籤資料整理成 LSTM 模型輸入格式，並劃分訓練集和測試集 (以 test_year 年份劃分)。
    # 輸入: 包含特徵和標籤的 DataFrame、股票列表 stock_list、歷史回溯窗口大小 history_window 和測試年份 test_year。
    # 輸出:  NumPy array 格式的訓練資料 (train_data) 和測試資料 (test_data)。
    pass

def normalize_data(train_data, test_data):
    # 功能: 使用 RobustScaler 對特徵資料進行標準化。
    # 輸入: 訓練資料 train_data 和測試資料 test_data。
    # 輸出:  標準化後的訓練資料和測試資料。
    pass