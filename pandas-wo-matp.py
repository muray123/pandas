import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
try:
    import matplotlib_fontja
except ImportError:
    pass

fig,axes = plt.subplots(1,1,figsize=(10,5))
data = {
    "数学": [60, 72, 68, 85, 90],
    "英語": [80, 78, 82, 80, 88],
    "国語": [70, 65, 75, 72, 80]
}
df = pd.DataFrame(data, index=["4月", "5月", "6月", "7月", "8月"])


df.plot(ax=axes,marker="o",grid=True)
axes.set_title("五教科の点数")
axes.set_ylim(50,100)
plt.show()