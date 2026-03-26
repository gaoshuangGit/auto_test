# # logs/logger.py
# import sys
# from loguru import logger
#
# # 移除默认处理器
# logger.remove()
#
# # 控制台输出
# logger.add(
#     sys.stderr,
#     format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
#     level="INFO",
#     colorize=True
# )
#
# # 文件输出
# logger.add(
#     "logs/test.log",
#     format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
#     level="DEBUG",
#     rotation="1 day"
# )
#
# # 导出 logger 实例
# __all__ = ["logger"]