from matplotlib import pyplot as plt
import numpy as np
import matplotlib_fontja
import pandas as pd
fig,axes = plt.subplots(1,2,figsize=(10,5))

def set_opt(ax_kind,x,y,label_name,marker_s,color):
    ax_kind.plot(
                    x,
                    y,
                    label=label_name,
                    marker=marker_s,
                    color=color
                    )
    ax_kind.legend(loc="upper left")
list1 = np.array([1,2,3,4,5])
x = [1,2,3,4,5]
set_opt(axes[0],x,list1,"お試し","o","red")
set_opt(axes[0],)

plt.show()