
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# 科目名稱
subjects = ["國文", "英文", "數學", "物理", "化學"]
labels = ["Chinese", "English", "Math", "Physics", "Chemistry"]


# 函式1：讀取 CSV
def read_csv_file(filename):
    return pd.read_csv(filename)


# 函式2：各科平均長條圖
def plot_subject_average(df, ax):
    averages = df[subjects].mean()

    ax.bar(labels, averages.values, color="skyblue")
    ax.set_title("Average Scores by Subject")
    ax.set_xlabel("Subjects")
    ax.set_ylabel("Average Score")
    ax.tick_params(axis="x", labelrotation=30)

    return averages


# 函式3：數學與物理散佈圖
def plot_scatter(df, ax):
    correlation = df["數學"].corr(df["物理"])

    ax.scatter(df["數學"], df["物理"], color="blue")
    ax.set_title(f"Math vs Physics (r = {correlation:.3f})")
    ax.set_xlabel("Math Score")
    ax.set_ylabel("Physics Score")
    ax.grid(True, alpha=0.3)

    return correlation


# 函式4：數學成績直方圖
def plot_histogram(df, ax):
    ax.hist(df["數學"], bins=10,
            color="orange", edgecolor="black")

    ax.set_title("Math Score Histogram")
    ax.set_xlabel("Math Score")
    ax.set_ylabel("Frequency")

    return ax


# 函式5：數學成績圓餅圖
def plot_piechart(df, ax):

    def get_grade(score):
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        elif score >= 60:
            return "D"
        else:
            return "F"

    grades = df["數學"].apply(get_grade)

    counts = grades.value_counts().reindex(
        ["A", "B", "C", "D", "F"], fill_value=0
    )

    counts = counts[counts > 0]

    ax.pie(counts.values,
           labels=counts.index,
           autopct="%1.1f%%",
           startangle=90)

    ax.set_title("Math Grade Distribution")

    return ax


# 函式6：各科成績箱型圖
def plot_boxplot(df, ax):
    data = [df[s].dropna() for s in subjects]

    ax.boxplot(data)
    ax.set_xticks(range(1, len(labels) + 1))
    ax.set_xticklabels(labels, rotation=30)

    ax.set_title("Score Distribution by Subject")
    ax.set_ylabel("Score")

    return ax


# 函式7：各科相關係數熱力圖
def plot_heatmap(df, ax):
    corr = df[subjects].corr()

    ax.imshow(corr, cmap="coolwarm", vmin=-1, vmax=1)

    ax.set_xticks(range(len(labels)))
    ax.set_yticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45, ha="right")
    ax.set_yticklabels(labels)

    for i in range(len(labels)):
        for j in range(len(labels)):
            ax.text(j, i, f"{corr.iloc[i, j]:.2f}",
                    ha="center", va="center", fontsize=9)

    ax.set_title("Correlation Heatmap")

    return corr


# 函式8：依序顯示六張圖
def plot_report(df):

    # 圖1：長條圖
    fig, ax = plt.subplots(figsize=(8, 5))
    averages = plot_subject_average(df, ax)
    plt.tight_layout()
    plt.show(block=True)
    plt.close(fig)

    # 圖2：散佈圖
    fig, ax = plt.subplots(figsize=(8, 5))
    correlation = plot_scatter(df, ax)
    plt.tight_layout()
    plt.show(block=True)
    plt.close(fig)

    # 圖3：直方圖
    fig, ax = plt.subplots(figsize=(8, 5))
    plot_histogram(df, ax)
    plt.tight_layout()
    plt.show(block=True)
    plt.close(fig)

    # 圖4：圓餅圖
    fig, ax = plt.subplots(figsize=(8, 5))
    plot_piechart(df, ax)
    plt.tight_layout()
    plt.show(block=True)
    plt.close(fig)

    # 圖5：箱型圖
    fig, ax = plt.subplots(figsize=(8, 5))
    plot_boxplot(df, ax)
    plt.tight_layout()
    plt.show(block=True)
    plt.close(fig)

    # 圖6：熱力圖
    fig, ax = plt.subplots(figsize=(8, 5))
    corr_matrix = plot_heatmap(df, ax)
    plt.tight_layout()
    plt.show(block=True)
    plt.close(fig)

    return averages, correlation, corr_matrix


# 函式9：主程式
def main():
    filename = Path(__file__).resolve().parent / "data" / "grades.csv"

    df = read_csv_file(filename)

    averages, correlation, corr_matrix = plot_report(df)

    print("\n各科平均成績：")
    print(averages)

    print(f"\n數學與物理相關係數：{correlation:.3f}")

    print("\n各科相關係數矩陣：")
    print(corr_matrix)


if __name__ == "__main__":
    main()
