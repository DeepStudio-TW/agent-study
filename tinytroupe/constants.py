# tinytroupe/constants.py

import os
from pathlib import Path

# 基礎路徑配置
ROOT_DIR = Path(__file__).parent.parent
PROMPTS_DIR = Path(__file__).parent / "prompts"

# 預設配置值
DEFAULT_CONFIG = {
    "OpenAI": {
        "API_TYPE": "openai",
        "AZURE_API_VERSION": "2023-05-15",
        "MODEL": "gpt-4",
        "MAX_TOKENS": "4000",
        "TEMPERATURE": "0.3",
        "FREQ_PENALTY": "0.0",
        "PRESENCE_PENALTY": "0.0",
        "TIMEOUT": "60",
        "MAX_ATTEMPTS": "5",
        "WAITING_TIME": "1",
        "EXPONENTIAL_BACKOFF_FACTOR": "5",
        "EMBEDDING_MODEL": "text-embedding-3-small",
        "CACHE_API_CALLS": "False",
        "CACHE_FILE_NAME": "openai_api_cache.pickle",
        "MAX_CONTENT_DISPLAY_LENGTH": "1024"
    },
    "Simulation": {
        "RAI_HARMFUL_CONTENT_PREVENTION": "True",
        "RAI_COPYRIGHT_INFRINGEMENT_PREVENTION": "True"
    },
    "Logging": {
        "LOGLEVEL": "ERROR"
    }
}

# 環境變數
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")