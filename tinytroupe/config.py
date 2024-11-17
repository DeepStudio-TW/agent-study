# tinytroupe/config.py

import configparser
from pathlib import Path
from .constants import ROOT_DIR, DEFAULT_CONFIG

class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.load_config()

    def get_config_file_path(self):
        """Get the path to the config file."""
        possible_locations = [
            ROOT_DIR / "config.ini",  # 專案根目錄
            Path.cwd() / "config.ini",  # 當前目錄
            Path.home() / ".tinytroupe" / "config.ini",  # 使用者主目錄
        ]
        
        for path in possible_locations:
            if path.exists():
                return path
                
        return ROOT_DIR / "config.ini"

    def load_config(self):
        """Load configuration from config.ini file."""
        config_path = self.get_config_file_path()
        
        if config_path.exists():
            self.config.read(str(config_path))
        else:
            # 使用預設配置
            for section, values in DEFAULT_CONFIG.items():
                self.config[section] = values

    def get(self, section, option, fallback=None):
        return self.config.get(section, option, fallback=fallback)

    def getint(self, section, option, fallback=None):
        return self.config.getint(section, option, fallback=fallback)

    def getfloat(self, section, option, fallback=None):
        return self.config.getfloat(section, option, fallback=fallback)

    def getboolean(self, section, option, fallback=None):
        return self.config.getboolean(section, option, fallback=fallback)

# 創建全局配置實例
config = Config()

# 導出常用配置
API_TYPE = config.get("OpenAI", "API_TYPE")
MODEL = config.get("OpenAI", "MODEL")
MAX_TOKENS = config.getint("OpenAI", "MAX_TOKENS")
TEMPERATURE = config.getfloat("OpenAI", "TEMPERATURE")
FREQ_PENALTY = config.getfloat("OpenAI", "FREQ_PENALTY")
PRESENCE_PENALTY = config.getfloat("OpenAI", "PRESENCE_PENALTY")
RAI_HARMFUL_CONTENT_PREVENTION = config.getboolean("Simulation", "RAI_HARMFUL_CONTENT_PREVENTION")
RAI_COPYRIGHT_INFRINGEMENT_PREVENTION = config.getboolean("Simulation", "RAI_COPYRIGHT_INFRINGEMENT_PREVENTION")
LOGLEVEL = config.get("Logging", "LOGLEVEL")