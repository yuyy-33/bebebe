import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler


NUMERIC_COLUMNS = ["age", "income", "monthly_spend", "visits", "tenure"]

plt.rcParams["font.sans-serif"] = [
    "PingFang TC",
    "PingFang HK",
    "Hiragino Sans GB",
    "Arial Unicode MS",
    "Noto Sans CJK TC",
    "DejaVu Sans",
]
plt.rcParams["axes.unicode_minus"] = False


class CustomerModel:
    def __init__(self, seed=42):
        self.seed = seed
        self.raw = None
        self.clean = None
        self.clustered = None
        self.scaler = None
        self.kmeans = None
        self.evaluations = []
        self.cluster_profiles = None
        self.selected_k = None

    def load(self, path):
        path = Path(path)
        self.raw = pd.read_csv(path, encoding="utf-8-sig")
        for column in NUMERIC_COLUMNS:
            self.raw[column] = pd.to_numeric(self.raw[column], errors="coerce")
        return self.raw

    def inspect(self):
        df = self.raw
        duplicate_mask = df.duplicated("customer_id", keep=False)
        duplicate_rows = df.index[duplicate_mask].tolist()

        rules = {
            "age": df["age"].notna() & ~df["age"].between(18, 100),
            "income": df["income"].notna() & ~df["income"].between(0, 500),
            "monthly_spend": df["monthly_spend"].notna() & ~df["monthly_spend"].between(0, 100),
            "visits": df["visits"].notna() & ~df["visits"].between(0, 30),
            "tenure": df["tenure"].notna() & ~df["tenure"].between(0, 50),
        }
        anomalies = {}
        for column, mask in rules.items():
            anomalies[column] = {
                "rows": df.index[mask].tolist(),
                "values": df.loc[mask, column].dropna().tolist(),
            }

        missing_before = int(df.isna().sum().sum())
        return {
            "shape": list(df.shape),
            "dtypes": {c: str(t) for c, t in df.dtypes.items()},
            "missing": df.isna().sum().astype(int).to_dict(),
            "missing_total": missing_before,
            "duplicate_rows": duplicate_rows,
            "duplicate_count": int(duplicate_mask.sum()),
            "anomalies": anomalies,
        }

    def clean_data(self, save_path=None):
        df = self.raw.copy()
        missing_before = int(df.isna().sum().sum())
        rows_before = len(df)

        df["region"] = df["region"].fillna("未知").astype(str).str.strip()

        age = df["age"].where(df["age"].between(18, 100))
        income = df["income"].where(df["income"].between(0, 500))
        monthly = df["monthly_spend"].where(df["monthly_spend"].between(0, 100))
        visits = df["visits"].where(df["visits"].between(0, 30))
        tenure = df["tenure"].where(df["tenure"].between(0, 50))
        df["age"] = age
        df["income"] = income
        df["monthly_spend"] = monthly
        df["visits"] = visits
        df["tenure"] = tenure

        for column in NUMERIC_COLUMNS:
            df[column] = df[column].fillna(df[column].median())

        df = df.drop_duplicates(subset="customer_id", keep="first")
        df = df.reset_index(drop=True)

        missing_after = int(df.isna().sum().sum())
        self.clean = df
        if save_path:
            Path(save_path).parent.mkdir(parents=True, exist_ok=True)
            df.to_csv(save_path, index=False, encoding="utf-8-sig")

        return {
            "rows_before": rows_before,
            "rows_after": len(df),
            "missing_before": missing_before,
            "missing_after": missing_after,
            "missing_after_by_column": df.isna().sum().astype(int).to_dict(),
            "actions": [
                "重複 customer_id：保留第一筆，刪除重複列",
                "年齡範圍：18～100，超出值先改為缺值",
                "年收入範圍：0～500 萬，超出值先改為缺值",
                "月消費範圍：0～100 千元，超出值先改為缺值",
                "月來店次數範圍：0～30 次，超出值先改為缺值",
                "會員年資範圍：0～50 年，超出值先改為缺值",
                "數值欄缺值：每欄各自以清理後的中位數補值",
                "缺失地區：補成「未知」",
            ],
        }

    def descriptive_stats(self):
        stats = self.clean[NUMERIC_COLUMNS].describe(
            percentiles=[0.5]
        ).loc[["mean", "std", "min", "50%", "max"]].T
        stats.index.name = "欄位"
        stats = stats.rename(columns={"50%": "median"})
        spread = stats["std"].idxmax()
        return stats, spread

    def regional_analysis(self):
        count = self.clean.groupby("region").size().rename("人數")
        means = self.clean.groupby("region")[NUMERIC_COLUMNS].mean()
        return pd.concat([count, means], axis=1)

    def correlation(self):
        return self.clean[NUMERIC_COLUMNS].corr()

    def plot_histogram(self, column, output):
        fig, ax = plt.subplots(figsize=(7, 5))
        ax.hist(self.clean[column], bins=20, edgecolor="black", alpha=0.8)
        ax.set_title(f"{column} 分佈")
        ax.set_xlabel(column)
        ax.set_ylabel("人數")
        fig.tight_layout()
        fig.savefig(output, dpi=150)
        plt.close(fig)

    def plot_box(self, column, output):
        regions = list(self.clean["region"].dropna().unique())
        data = [self.clean.loc[self.clean["region"] == r, column].dropna() for r in regions]
        fig, ax = plt.subplots(figsize=(8, 5))
        ax.boxplot(data)
        ax.set_xticklabels(regions)
        ax.set_title(f"各地區 {column} 盒鬚圖")
        ax.set_xlabel("地區")
        ax.set_ylabel(column)
        fig.tight_layout()
        fig.savefig(output, dpi=150)
        plt.close(fig)

    def plot_scatter(self, x, y, output):
        fig, ax = plt.subplots(figsize=(7, 5))
        ax.scatter(self.clean[x], self.clean[y], alpha=0.55)
        ax.set_title(f"{x} 與 {y} 散佈圖")
        ax.set_xlabel(x)
        ax.set_ylabel(y)
        fig.tight_layout()
        fig.savefig(output, dpi=150)
        plt.close(fig)

    def plot_heatmap(self, output):
        corr = self.correlation()
        fig, ax = plt.subplots(figsize=(8, 6))
        image = ax.imshow(corr, vmin=-1, vmax=1)
        ax.set_xticks(range(len(corr.columns)))
        ax.set_yticks(range(len(corr.index)))
        ax.set_xticklabels(corr.columns, rotation=45, ha="right")
        ax.set_yticklabels(corr.index)
        for i in range(len(corr.index)):
            for j in range(len(corr.columns)):
                ax.text(j, i, f"{corr.iloc[i, j]:.2f}", ha="center", va="center")
        ax.set_title("數值欄相關係數熱圖")
        fig.colorbar(image, ax=ax)
        fig.tight_layout()
        fig.savefig(output, dpi=150)
        plt.close(fig)

    def evaluate_k(self, k_min=2, k_max=10):
        features = self.clean[NUMERIC_COLUMNS].astype(float)
        self.scaler = StandardScaler()
        scaled = self.scaler.fit_transform(features)
        evaluations = []
        for k in range(k_min, k_max + 1):
            model = KMeans(n_clusters=k, random_state=self.seed, n_init=20)
            labels = model.fit_predict(scaled)
            silhouette = silhouette_score(scaled, labels)
            evaluations.append({
                "k": k,
                "inertia": float(model.inertia_),
                "silhouette": float(silhouette),
            })
        self.evaluations = evaluations
        return evaluations

    def plot_evaluation(self, output_dir):
        output_dir = Path(output_dir)
        ks = [item["k"] for item in self.evaluations]
        inertia = [item["inertia"] for item in self.evaluations]
        silhouette = [item["silhouette"] for item in self.evaluations]

        fig, ax = plt.subplots(figsize=(7, 5))
        ax.plot(ks, inertia, marker="o")
        ax.set_title("K-means 手肘法")
        ax.set_xlabel("k")
        ax.set_ylabel("Inertia")
        fig.tight_layout()
        fig.savefig(output_dir / "fig_elbow.png", dpi=150)
        plt.close(fig)

        fig, ax = plt.subplots(figsize=(7, 5))
        ax.plot(ks, silhouette, marker="o")
        ax.set_title("K-means 輪廓係數")
        ax.set_xlabel("k")
        ax.set_ylabel("輪廓係數")
        fig.tight_layout()
        fig.savefig(output_dir / "fig_silhouette.png", dpi=150)
        plt.close(fig)

    def choose_k(self, k):
        k = int(k)
        features = self.clean[NUMERIC_COLUMNS].astype(float)
        scaled = self.scaler.transform(features)
        self.kmeans = KMeans(n_clusters=k, random_state=self.seed, n_init=20)
        labels = self.kmeans.fit_predict(scaled)
        self.clustered = self.clean.copy()
        self.clustered["cluster"] = labels
        self.selected_k = k
        self.cluster_profiles = self.clustered.groupby("cluster")[NUMERIC_COLUMNS].mean()
        self.cluster_profiles["人數"] = self.clustered.groupby("cluster").size()
        self.cluster_profiles = self.cluster_profiles[
            ["人數"] + NUMERIC_COLUMNS
        ]
        return self.cluster_profiles

    def plot_clusters(self, x, y, output):
        fig, ax = plt.subplots(figsize=(8, 6))
        for cluster in sorted(self.clustered["cluster"].unique()):
            part = self.clustered[self.clustered["cluster"] == cluster]
            ax.scatter(part[x], part[y], alpha=0.65, label=f"群 {cluster}")
        ax.set_title("K-means 顧客分群")
        ax.set_xlabel(x)
        ax.set_ylabel(y)
        ax.legend(title="群")
        fig.tight_layout()
        fig.savefig(output, dpi=150)
        plt.close(fig)

    def save_clustered(self, path):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        self.clustered.to_csv(path, index=False, encoding="utf-8-sig")

    def predict_cluster(self, values):
        row = np.array([[values[c] for c in NUMERIC_COLUMNS]], dtype=float)
        return int(self.kmeans.predict(self.scaler.transform(row))[0])

    def export_summary(self, path, clean_report):
        def rounded(value):
            return round(float(value), 3)

        stats, spread = self.descriptive_stats()
        summary = {
            "cleaning": clean_report,
            "descriptive_spread_largest": spread,
            "descriptive_stats": {
                c: {k: rounded(v) for k, v in row.items()}
                for c, row in stats.to_dict("index").items()
            },
            "regional": {
                str(region): {c: rounded(v) for c, v in row.items()}
                for region, row in self.regional_analysis().to_dict("index").items()
            },
            "correlation": {
                c: {r: rounded(v) for r, v in row.items()}
                for c, row in self.correlation().to_dict().items()
            },
            "selected_k": self.selected_k,
            "evaluations": [
                {
                    "k": int(x["k"]),
                    "inertia": rounded(x["inertia"]),
                    "silhouette": rounded(x["silhouette"]),
                }
                for x in self.evaluations
            ],
            "cluster_profiles": {
                str(int(cluster)): {
                    c: rounded(v) for c, v in row.items()
                }
                for cluster, row in self.cluster_profiles.to_dict("index").items()
            },
        }
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as file:
            json.dump(summary, file, ensure_ascii=False, indent=2)
