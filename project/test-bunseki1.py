import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
#日本語対応、ないならスキップ
try:
    import matplotlib_fontja
except ImportError:
    pass

#点数、教科を"test-scores.csv"から読み込み、dfに落とす
df = pd.read_csv("test-scores.csv")
print(df)
