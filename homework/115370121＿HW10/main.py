import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["Heiti TC", "Arial Unicode MS", "Hiragino Sans GB"]
plt.rcParams["axes.unicode_minus"] = False

from pathlib import Path
BASE = Path(__file__).parent
df = pd.read_csv(BASE / "data" / "grades.csv")
df["英文"] = df["英文"].fillna(df["英文"].mean())   # S07 的英文缺值先補平均

# 1. 數學最高分的學號與分數
i = df["數學"].idxmax()
print(df.loc[i, ["學號", "數學"]])

# 2. 新增「等第」欄
df["平均"] = df[["程式", "數學", "英文"]].mean(axis=1)
df["等第"] = np.select(
    [df["平均"] >= 80, df["平均"] >= 60],
    ["A", "B"],
    default="C",
)

# 3. 各等第人數的長條圖
counts = df["等第"].value_counts().reindex(["A", "B", "C"])
fig, ax = plt.subplots(figsize=(6, 3.6))
counts.plot(kind="bar", ax=ax, rot=0, title="各等第人數")
ax.set_xlabel("等第")
ax.set_ylabel("人數")
fig.tight_layout()
fig.savefig(BASE / "grade.png", dpi=150)
plt.show()