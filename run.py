import pytest
import os
from datetime import datetime

# 1. 生成报告路径
report_time = datetime.now().strftime("%Y%m%d_%H%M%S")
# report_path = os.path.join("allure-results", report_time)

# 2. pytest 参数（你之前在终端敲的命令，全写这里）
args = [
    "testcases/",          # 用例目录
    "-v",                  # 详细输出
    # "--alluredir", report_path,  # 生成allure数据
    # "--clean-alluredir"    # 清空旧报告
]

# 3. 运行用例
pytest.main(args)