# configs/config.py
import os
from pathlib import Path

# 项目根目录
BASE_DIR = Path(__file__).resolve().parent.parent

# 测试地址
BASE_URL = "https://www.saucedemo.com/"

# 测试账号
USERNAME = "admin"
PASSWORD = "123456"

# 浏览器
BROWSER = "chrome"
HEADLESS = False

# 等待时间
IMPLICITLY_WAIT = 10

# 目录
SCREENSHOT_DIR = BASE_DIR / "screenshots"
LOG_DIR = BASE_DIR / "logs"