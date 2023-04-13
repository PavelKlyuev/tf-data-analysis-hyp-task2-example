import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

chat_id = 240671999 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.08
    stat, pval = ks_2samp(x, y)
    return True if pval < alpha else False
