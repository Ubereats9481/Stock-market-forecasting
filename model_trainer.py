import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, CSVLogger

def train_lstm_model(model, train_data, val_split=0.2, patience=10, model_folder='models'):
    # 功能: 訓練 LSTM 模型。 實作模型訓練流程，包含 callbacks (EarlyStopping, ModelCheckpoint, CSVLogger)。
    # 輸入:  Keras LSTM 模型 model、訓練資料 train_data、驗證集比例 val_split、EarlyStopping 的耐心值 patience 和模型儲存路徑 model_folder。
    # 輸出:  訓練好的 LSTM 模型。
    pass