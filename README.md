# TinyTroupe 多角色團隊頭腦風暴

Microsoft TinyTroupe 是一個創新的開源專案，旨在模擬多智能體互動，利用大型語言模型（LLM）創建逼真的角色和環境。該專案允許用戶探索合成 agent 之間複雜的行為和互動，這些 agent 被稱為 TinyPersons，並在一個可自定義的環境中進行互動，稱為 TinyWorld。

## 主要特點

### 多智能體模擬
- **TinyPersons**：由 AI 驅動的 agent，具有獨特的人格、興趣和目標
- **TinyWorld**：TinyPersons 存在和互動的虛擬空間，提供靈活的框架來模擬多樣化場景

### 應用場景
- 廣告評估：模擬受眾對數位廣告的反應
- 軟體測試：為聊天機器人或搜尋引擎生成測試輸入
- 合成數據生成：創建逼真的合成數據集
- 產品反饋：模擬焦點小組討論
- 頭腦風暴會議：通過模擬不同角色討論促進創意過程

## 安裝步驟

1. 安裝 Anaconda
   - 從 https://www.anaconda.com/download/success 下載

2. 建立環境
```bash
conda create -n tinytroupes python=3.10
conda activate tinytroupes
conda install jupyter jupyterlab notebook nbconvert
```
或
```bash
python -m venv venv
# Windows 啟動虛擬環境
venv\Scripts\activate
# Linux/Mac 啟動虛擬環境
source venv/bin/activate
```
3. 設定 OpenAI API
```bash
export OPENAI_API_KEY=你的金鑰
```

4. 啟動 Jupyter
```bash
jupyter lab
```

5. 安裝專案
```bash
pip install -e .
```

## 配置文件

創建 `config.ini` 文件並填入以下內容：

```ini
[OpenAI]
API_TYPE=openai
AZURE_API_VERSION=2023-05-15

MODEL=gpt-4o
MAX_TOKENS=4000
TEMPERATURE=0.3
FREQ_PENALTY=0.0
PRESENCE_PENALTY=0.0
TIMEOUT=60
MAX_ATTEMPTS=5
WAITING_TIME=1
EXPONENTIAL_BACKOFF_FACTOR=5

EMBEDDING_MODEL=text-embedding-3-small 

CACHE_API_CALLS=False
CACHE_FILE_NAME=openai_api_cache.pickle

MAX_CONTENT_DISPLAY_LENGTH=1024

[Simulation]
RAI_HARMFUL_CONTENT_PREVENTION=True
RAI_COPYRIGHT_INFRINGEMENT_PREVENTION=True

[Logging]
LOGLEVEL=ERROR
```

## 範例使用場景

本專案包含一個完整的團隊討論模擬範例，模擬了以下角色：
- Kevin：全端開發者（後端為主）
- Samantha：產品經理
- Tina：UX 設計師
- Alex：工程經理
- Liam：前端開發者
- Max：數據分析師

每個角色都具有獨特的背景、專業知識和個性特徵，可以進行真實的團隊討論模擬。

## 技術細節

- 使用緩存機制優化性能
- 提供代理創建和管理工具
- 支援多輪討論模擬
- 包含結果提取和總結功能

## 注意事項

使用本專案需要有效的 OpenAI API 金鑰。如需充值 API 金鑰或 ChatGPT 會員，可使用 Wildcard 虛擬卡。