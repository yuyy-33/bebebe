import argparse
import sys
from pathlib import Path

from model.customer_model import CustomerModel


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "customers.csv"


def run_auto(input_path=DATA, output_dir=ROOT / "output", k=None):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    model = CustomerModel(seed=42)
    model.load(input_path)
    inspection = model.inspect()
    clean_report = model.clean_data(output_dir / "customers_clean.csv")

    stats, spread = model.descriptive_stats()
    regional = model.regional_analysis()
    corr = model.correlation()

    model.plot_histogram("age", output_dir / "fig_histogram_age.png")
    model.plot_box("monthly_spend", output_dir / "fig_box_monthly_spend.png")
    model.plot_scatter("income", "monthly_spend", output_dir / "fig_scatter_income_spend.png")
    model.plot_heatmap(output_dir / "fig_correlation_heatmap.png")

    evaluations = model.evaluate_k(2, 10)
    model.plot_evaluation(output_dir)
    if k is None:
        k = max(evaluations, key=lambda x: x["silhouette"])["k"]
    profiles = model.choose_k(k)
    model.plot_clusters("income", "monthly_spend", output_dir / "fig_kmeans_clusters.png")
    model.save_clustered(output_dir / "customers_clustered.csv")
    model.export_summary(output_dir / "summary.json", clean_report)

    print("inspection:", inspection)
    print("cleaning:", clean_report)
    print("largest_std_column:", spread)
    print("regional:\n", regional)
    print("correlation:\n", corr)
    print("selected k:", k)
    print("cluster profiles:\n", profiles)
    print("output:", output_dir)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--auto", action="store_true", help="一行執行完整分析")
    parser.add_argument("--input", default=str(DATA))
    parser.add_argument("--output", default=str(ROOT / "output"))
    parser.add_argument("--k", type=int)
    args = parser.parse_args()

    if args.auto:
        run_auto(args.input, args.output, args.k)
        return

    from PyQt5.QtWidgets import QApplication
    from view.main_window import MainWindow
    from controller.main_controller import MainController

    app = QApplication(sys.argv)
    model = CustomerModel(seed=42)
    view = MainWindow()
    controller = MainController(model, view)
    view.set_controller(controller)
    view.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()