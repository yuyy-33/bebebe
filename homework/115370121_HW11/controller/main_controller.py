from pathlib import Path

from PyQt5.QtCore import QThread, pyqtSignal


class EvaluationWorker(QThread):
    finished_with_result = pyqtSignal(object)
    error = pyqtSignal(str)

    def __init__(self, model):
        super().__init__()
        self.model = model
        self.request_stop = False

    def run(self):
        try:
            result = self.model.evaluate_k(2, 10)
            if not self.request_stop:
                self.finished_with_result.emit(result)
        except Exception as error:
            self.error.emit(str(error))

    def stop(self):
        self.request_stop = True


class MainController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.worker = None

    def open_csv(self, path):
        self.model.load(path)
        inspection = self.model.inspect()
        self.view.show_dataframe(self.model.raw)
        self.view.show_inspection(inspection)
        return inspection

    def clean(self, output_path=None):
        result = self.model.clean_data(output_path)
        self.view.show_dataframe(self.model.clean)
        self.view.show_clean_report(result)
        return result

    def analyze(self):
        stats, spread = self.model.descriptive_stats()
        regional = self.model.regional_analysis()
        corr = self.model.correlation()
        self.view.show_analysis(stats, regional, corr, spread)

    def visualize(self, kind, x, y, output_path):
        if kind == "直方圖":
            self.model.plot_histogram(x, output_path)
        elif kind == "盒鬚圖":
            self.model.plot_box(x, output_path)
        elif kind == "散佈圖":
            self.model.plot_scatter(x, y, output_path)
        else:
            self.model.plot_heatmap(output_path)
        self.view.show_image(output_path)

    def start_evaluation(self, output_dir):
        self.worker = EvaluationWorker(self.model)
        self.worker.finished_with_result.connect(
            lambda values: self.evaluation_finished(values, output_dir)
        )
        self.worker.error.connect(self.view.show_error)
        self.worker.start()

    def evaluation_finished(self, values, output_dir):
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        self.model.plot_evaluation(output_dir)
        self.view.show_evaluations(values)
        self.view.show_image(Path(output_dir) / "fig_elbow.png")

    def stop_evaluation(self):
        if self.worker and self.worker.isRunning():
            self.worker.stop()
            self.worker.terminate()
            self.worker.wait()
            self.view.show_status("已停止背景分群工作")

    def run_kmeans(self, k, output_dir):
        profiles = self.model.choose_k(k)
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        self.model.plot_clusters("income", "monthly_spend", Path(output_dir) / "fig_kmeans_clusters.png")
        self.view.show_profiles(profiles)
        self.view.show_image(Path(output_dir) / "fig_kmeans_clusters.png")
