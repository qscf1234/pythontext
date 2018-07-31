import time
import pygame

# 音乐路径
filePath = r"D:\pythontext\day15\7-播放音乐\王心凌-第一次爱的人.flac"

# 初始化
pygame.mixer.init()
# 加载音乐
track = pygame.mixer.music.load(filePath)
# 播放
pygame.mixer.music.play()
#
time.sleep(4*60+20.41)
# 停止
pygame.mixer.music.stop()
