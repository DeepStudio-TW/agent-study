# AI 聊天機器人團隊模擬系統

這個專案使用 Microsoft TinyTroupe 框架來模擬多智能體互動，特別是用於模擬團隊討論和產品開發過程。

## 專案特點

### 角色模擬
系統包含六個預定義的角色：
- **Ethan** (後端開發者): 專注於系統架構和效能優化
- **Samantha** (產品經理): 負責產品策略和用戶需求
- **Tina** (UX設計師): 專注於用戶體驗和介面設計
- **Alex** (工程經理): 協調團隊和技術決策
- **Liam** (前端開發者): 負責用戶界面實現
- **Max** (資料分析師): 負責數據分析和用戶行為研究

### 核心功能
- 多角色互動模擬
- 團隊討論流程模擬
- 自動化結果提取和總結
- 格式化輸出報告

## 安裝步驟

1. 設置 Python 環境
```bash
# 創建虛擬環境
python -m venv venv

# 啟動虛擬環境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

2. 安裝依賴
```bash
pip install -e .
```

3. 設置配置文件
```bash
# 在專案根目錄創建 config.ini
[OpenAI]
API_TYPE=openai
AZURE_API_VERSION=2023-05-15
MODEL=gpt-4
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

4. 設置環境變數
```bash
# Windows
set OPENAI_API_KEY=your-api-key

# macOS/Linux
export OPENAI_API_KEY=your-api-key
```

## 使用方法

1. 運行模擬
```bash
python app.py
```

2. 查看結果
程式將輸出格式化的討論總結，包含：
- 主要討論要點
- 創新功能提案
- 技術實現考量
- 潛在挑戰
- 團隊成員貢獻
- 建議事項
- 後續步驟

## 專案結構
```
project/
├── pyproject.toml          # 專案配置
├── config.ini             # 配置文件
├── README.md              # 說明文件
└── tinytroupe/           # 主要程式碼
    ├── __init__.py
    ├── app.py            # 主程式
    ├── agent.py          # 代理人定義
    ├── config.py         # 配置處理
    ├── environment.py    # 環境設定
    ├── extraction.py     # 結果提取
    ├── utils.py          # 工具函數
    └── prompts/          # 提示模板
      ....../
        ├── tinyperson.mustache
        └── interaction_results_extractor.mustache
```

## 輸出範例

```
====== AI聊天機器人創新功能討論總結 ======

📌 主要討論要點
------------------------------
  • 討論創新功能需求
  • 強調用戶體驗重要性
  • 平衡創新與實用性

💡 創新功能提案
------------------------------
  • 情感智能整合
  • 多模態互動系統
  • 個人化功能適配

[更多輸出內容...]
```

## 參考資料
- [Microsoft TinyTroupe 文件](https://github.com/microsoft/tinytroupe)
- [OpenAI API 文件](https://platform.openai.com/docs/api-reference)

## 注意事項
- 需要有效的 OpenAI API 金鑰
- Python 3.10 或以上版本
- 確保所有依賴包都正確安裝
- 配置文件中的參數可根據需要調整

## 貢獻指南
如果你想貢獻代碼：
1. Fork 本專案
2. 創建你的功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 開啟一個 Pull Request

## 授權
本專案使用 MIT 授權 - 查看 [LICENSE](LICENSE) 文件了解更多詳情
