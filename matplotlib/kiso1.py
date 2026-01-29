import numpy as np
from matplotlib import pyplot as plt
try:
    import japanize_matplotlib
except ImportError:
    pass

fig,axes = plt.subplots(1,2,figsize=(10,5))

x1 = np.array([1,2,3,4,5,6,7,8])
x2 = np.array([1,2,3,4,5])

y1 = 3 * x1 + 3
y2 = x2 * x2 + 1

#グラフ1
axes[0].plot(x1,y1)
axes[0].set_xlabel("x")
axes[0].set_ylabel("y")
axes[1].plot(x2,y2)
fig.tight_layout()
for ax in axes:
    ax.gird(True)

plt.show()