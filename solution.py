import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

chat_id = 240671999 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    stat, pval = ttest_ind(x, y, equal_var=False)
    return False if pval > 0.08 else True
