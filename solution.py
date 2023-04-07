import pandas as pd
import numpy as np


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    t = 93;
    a = 2 * np.median(x) / (t ** 2)
    return a # Ваш ответ
