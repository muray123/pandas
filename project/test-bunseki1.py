import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
#日本語対応、ないならスキップ
try:
    import matplotlib_fontja
except ImportError:
    pass

#点数、教科を"test-scores.csv"から読み込み、dfに落とす
df = pd.read_csv("test-scores-pre.csv")
df.set_index("times",inplace=True)
subject_df = df[["japanese","math","english","science","social"]]

fig,axes = plt.subplots(2,5,figsize=(14,8),sharey=False)
def set_opt(ax_kind,x,y,label_name,marker_s,color):
    ax_kind.plot(
                    x,
                    y,
                    label=label_name,
                    marker=marker_s,
                    color=color
                    )
    ax_kind.legend(loc="upper left")
    ax_kind.grid(True)
    ax_kind.set_yticks(np.arange(0,101,10))

subjects = ["japanese", "math", "english", "science", "social"]
labels = ["国", "数", "英", "理", "社"]
colors = ["red", "blue", "green", "orange", "purple"]

for i in range(5):
    set_opt(
        axes[0][i],
        subject_df.index,      # x軸：インデックス(times)
        subject_df.iloc[:, i], # y軸：各教科の列
        labels[i],
        "o",
        colors[i]              # カンマ忘れに注意！
    )

# ===== 円グラフ（2行目） =====
for i, (time_index, row) in enumerate(subject_df.iterrows()):
    axes[1][i].pie(
        row,
        labels=labels,
        counterclock=False,
        startangle=90,
        autopct='%1.1f%%',
        colors=colors
    )
    axes[1][i].set_title(f"第{time_index}")
    print(time_index),
    print(row)

plt.tight_layout()
plt.show()