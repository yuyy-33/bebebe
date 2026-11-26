from pathlib import Path

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication, QAbstractItemView, QComboBox, QFileDialog, QHBoxLayout,
    QLabel, QLineEdit, QMessageBox, QPushButton, QScrollArea, QSplitter,
    QTableWidget, QTableWidgetItem, QTabWidget, QTextEdit, QVBoxLayout,
    QWidget,
)


class ZoomPreview(QScrollArea):
    def __init__(self):
        super().__init__()
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.setWidget(self.label)
        self.setWidgetResizable(False)
        self.scale = 1.0
        self.pixmap = None
        self.drag_start = None

    def show_image(self, path):
        self.pixmap = QPixmap(str(path))
        self._update_pixmap()

    def _update_pixmap(self):
        if self.pixmap:
            size = self.pixmap.size()
            scaled = self.pixmap.scaled(
                int(size.width() * self.scale),
                int(size.height() * self.scale),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation,
            )
            self.label.setPixmap(scaled)
            self.label.resize(scaled.size())

    def wheelEvent(self, event):
        delta = event.angleDelta().y()
        if delta == 0:
            return
        cursor = event.position().toPoint()
        old = self.scale
        self.scale *= 1.1 if delta > 0 else 1 / 1.1
        self.scale = max(0.2, min(5.0, self.scale))
        self._update_pixmap()
        if self.scale != old:
            event.accept()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start = event.pos()

    def mouseMoveEvent(self, event):
        if self.drag_start is not None:
            delta = event.pos() - self.drag_start
            self.horizontalScrollBar().setValue(
                self.horizontalScrollBar().value() - delta.x()
            )
            self.verticalScrollBar().setValue(
                self.verticalScrollBar().value() - delta.y()
            )
            self.drag_start = event.pos()

    def mouseReleaseEvent(self, event):
        self.drag_start = None

    def mouseDoubleClickEvent(self, event):
        self.scale = 1.0
        self._update_pixmap()
        self.horizontalScrollBar().setValue(0)
        self.verticalScrollBar().setValue(0)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.controller = None
        self.setWindowTitle("顧客資料分析與 K-means 分群")
        self.resize(1250, 760)

        layout = QVBoxLayout(self)
        common = QHBoxLayout()
        common.addWidget(QLabel("共用資料檔"))
        self.path_edit = QLineEdit(str(Path(__file__).resolve().parents[1] / "customers.csv"))
        self.path_edit.setToolTip("欲分析的 CSV；預設會讀本作業目錄的 customers.csv")
        common.addWidget(self.path_edit)
        open_button = QPushButton("選擇檔案")
        open_button.setToolTip("選擇 UTF-8 或 UTF-8 BOM 的 customers.csv")
        open_button.clicked.connect(self.choose_file)
        common.addWidget(open_button)
        common.addWidget(QLabel("亂數種子"))
        self.seed_edit = QLineEdit("42")
        self.seed_edit.setToolTip("固定種子讓分群結果可重現，預設 42")
        common.addWidget(self.seed_edit)
        layout.addLayout(common)

        splitter = QSplitter(Qt.Horizontal)
        self.preview = ZoomPreview()
        splitter.addWidget(self.preview)

        right = QWidget()
        right_layout = QVBoxLayout(right)
        self.tabs = QTabWidget()
        self.tabs.setToolTip("依序進行資料、清理、分析、視覺化與分群")
        right_layout.addWidget(self.tabs)
        splitter.addWidget(right)
        splitter.setSizes([780, 470])
        layout.addWidget(splitter)

        self.status = QTextEdit()
        self.status.setReadOnly(True)
        self.status.setMaximumHeight(100)
        layout.addWidget(self.status)

        self.build_tabs()

    def set_controller(self, controller):
        self.controller = controller

    def choose_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "選擇 CSV", "", "CSV (*.csv)")
        if path:
            self.path_edit.setText(path)

    def build_tabs(self):
        data_tab = QWidget()
        data_layout = QVBoxLayout(data_tab)
        button = QPushButton("讀取並檢查資料")
        button.setToolTip("讀入 CSV，顯示 shape、dtypes、缺值、重複列與異常值")
        button.clicked.connect(self.load_data)
        data_layout.addWidget(button)
        self.data_table = QTableWidget()
        self.data_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        data_layout.addWidget(self.data_table)
        self.tabs.addTab(data_tab, "資料")

        clean_tab = QWidget()
        clean_layout = QVBoxLayout(clean_tab)
        button = QPushButton("執行清理")
        button.setToolTip("刪除重複 customer_id，異常值改缺值後以中位數補值")
        button.clicked.connect(self.clean_data)
        clean_layout.addWidget(button)
        save_button = QPushButton("另存清理後 CSV")
        save_button.setToolTip("將 customers_clean.csv 儲存到指定位置")
        save_button.clicked.connect(self.save_clean)
        clean_layout.addWidget(save_button)
        self.clean_text = QTextEdit()
        self.clean_text.setReadOnly(True)
        clean_layout.addWidget(self.clean_text)
        self.tabs.addTab(clean_tab, "清理")

        analysis_tab = QWidget()
        analysis_layout = QVBoxLayout(analysis_tab)
        button = QPushButton("執行敘述統計與相關分析")
        button.setToolTip("顯示敘述統計、地區分組平均與相關係數")
        button.clicked.connect(self.analyze)
        analysis_layout.addWidget(button)
        self.analysis_text = QTextEdit()
        self.analysis_text.setReadOnly(True)
        analysis_layout.addWidget(self.analysis_text)
        self.tabs.addTab(analysis_tab, "分析")

        visual_tab = QWidget()
        visual_layout = QVBoxLayout(visual_tab)
        self.chart_combo = QComboBox()
        self.chart_combo.addItems(["直方圖", "盒鬚圖", "散佈圖", "相關係數熱圖"])
        self.chart_combo.setToolTip("選擇要產生的圖；預設直方圖為 age")
        visual_layout.addWidget(self.chart_combo)
        self.x_edit = QLineEdit("age")
        self.x_edit.setToolTip("X 軸欄位；散佈圖與直方圖或盒鬚圖使用此欄")
        visual_layout.addWidget(self.x_edit)
        self.y_edit = QLineEdit("monthly_spend")
        self.y_edit.setToolTip("散佈圖的 Y 軸欄位")
        visual_layout.addWidget(self.y_edit)
        button = QPushButton("繪製並預覽")
        button.setToolTip("產生 PNG 並在左側預覽")
        button.clicked.connect(self.visualize)
        visual_layout.addWidget(button)
        save_button = QPushButton("另存 PNG")
        save_button.setToolTip("開啟檔案對話框儲存目前圖表")
        save_button.clicked.connect(self.save_image)
        visual_layout.addWidget(save_button)
        visual_layout.addStretch()
        self.tabs.addTab(visual_tab, "視覺化")

        cluster_tab = QWidget()
        cluster_layout = QVBoxLayout(cluster_tab)
        k_layout = QHBoxLayout()
        k_layout.addWidget(QLabel("k"))
        self.k_edit = QLineEdit("3")
        self.k_edit.setToolTip("分群數量，預設 3")
        k_layout.addWidget(self.k_edit)
        cluster_layout.addLayout(k_layout)
        evaluate_button = QPushButton("背景執行 k＝2～10 評估")
        evaluate_button.setToolTip("在 QThread 中計算手肘法與輪廓係數，不凍結畫面")
        evaluate_button.clicked.connect(self.evaluate)
        cluster_layout.addWidget(evaluate_button)
        stop_button = QPushButton("停止")
        stop_button.setToolTip("安全停止正在執行的 K-means 評估")
        stop_button.clicked.connect(self.stop)
        cluster_layout.addWidget(stop_button)
        run_button = QPushButton("執行分群")
        run_button.setToolTip("使用選定 k 執行分群並顯示群輪廓")
        run_button.clicked.connect(self.run_kmeans)
        cluster_layout.addWidget(run_button)
        save_button = QPushButton("另存含 cluster 的 CSV")
        save_button.setToolTip("儲存 customers_clustered.csv")
        save_button.clicked.connect(self.save_clustered)
        cluster_layout.addWidget(save_button)
        self.cluster_text = QTextEdit()
        self.cluster_text.setReadOnly(True)
        cluster_layout.addWidget(self.cluster_text)
        self.tabs.addTab(cluster_tab, "K-means")

    def load_data(self):
        path = self.path_edit.text()
        try:
            self.controller.open_csv(path)
        except Exception as error:
            self.show_error(str(error))

    def clean_data(self):
        try:
            self.controller.clean()
        except Exception as error:
            self.show_error(str(error))

    def save_clean(self):
        path, _ = QFileDialog.getSaveFileName(self, "另存清理資料", "customers_clean.csv", "CSV (*.csv)")
        if path:
            self.controller.model.clean_data(path)
            self.show_status(f"已儲存：{path}")

    def analyze(self):
        try:
            self.controller.analyze()
        except Exception as error:
            self.show_error(str(error))

    def visualize(self):
        kind = self.chart_combo.currentText()
        path = str(Path(__file__).resolve().parents[1] / "output" / f"gui_{kind}.png")
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        try:
            self.controller.visualize(kind, self.x_edit.text(), self.y_edit.text(), path)
        except Exception as error:
            self.show_error(str(error))

    def save_image(self):
        path, _ = QFileDialog.getSaveFileName(self, "另存圖片", "figure.png", "PNG (*.png)")
        if path and hasattr(self.preview, "pixmap") and self.preview.pixmap:
            self.preview.pixmap.save(path)

    def evaluate(self):
        output = str(Path(__file__).resolve().parents[1] / "output")
        self.show_status("正在背景執行 k=2～10...")
        self.controller.start_evaluation(output)

    def stop(self):
        self.controller.stop_evaluation()

    def run_kmeans(self):
        try:
            k = int(self.k_edit.text())
            output = str(Path(__file__).resolve().parents[1] / "output")
            self.controller.run_kmeans(k, output)
        except Exception as error:
            self.show_error(str(error))

    def save_clustered(self):
        if self.controller.model.clustered is None:
            self.show_error("請先執行分群")
            return
        path, _ = QFileDialog.getSaveFileName(self, "另存分群資料", "customers_clustered.csv", "CSV (*.csv)")
        if path:
            self.controller.model.save_clustered(path)
            self.show_status(f"已儲存：{path}")

    def show_dataframe(self, df):
        self.data_table.setRowCount(len(df))
        self.data_table.setColumnCount(len(df.columns))
        self.data_table.setHorizontalHeaderLabels(list(df.columns))
        for i, row in enumerate(df.head(200).itertuples(index=False, name=None)):
            for j, value in enumerate(row):
                self.data_table.setItem(i, j, QTableWidgetItem("" if value is None else str(value)))

    def show_inspection(self, inspection):
        text = [
            f"shape: {tuple(inspection['shape'])}",
            f"缺值總數（原始資料）：{inspection['missing_total']}",
            "各欄缺值：",
            str(inspection["missing"]),
            "重複列索引：",
            str(inspection["duplicate_rows"]),
            "異常值：",
            str(inspection["anomalies"]),
            "dtypes：",
            str(inspection["dtypes"]),
        ]
        self.status.setPlainText("\n".join(text))

    def show_clean_report(self, report):
        self.clean_text.setPlainText(
            "\n".join([
                f"清理前列數：{report['rows_before']}",
                f"清理後列數：{report['rows_after']}",
                f"清理前缺值總數：{report['missing_before']}",
                f"清理後缺值總數：{report['missing_after']}",
                "處理方式：",
                *report["actions"],
            ])
        )

    def show_analysis(self, stats, regional, corr, spread):
        self.analysis_text.setPlainText(
            "敘述統計\n" + stats.to_string()
            + f"\n\n標準差最大欄位：{spread}"
            + "\n\n依地區分組\n" + regional.to_string()
            + "\n\n相關係數\n" + corr.to_string()
        )

    def show_evaluations(self, values):
        self.cluster_text.setPlainText(
            "k / inertia / silhouette\n"
            + "\n".join(
                f"{x['k']} / {x['inertia']:.3f} / {x['silhouette']:.3f}"
                for x in values
            )
        )

    def show_profiles(self, profiles):
        self.cluster_text.setPlainText(profiles.to_string())

    def show_image(self, path):
        self.preview.show_image(str(path))

    def show_status(self, text):
        self.status.setPlainText(text)

    def show_error(self, text):
        QMessageBox.critical(self, "錯誤", text)

    def closeEvent(self, event):
        worker_running = (
            getattr(self.controller, "worker", None) is not None
            and self.controller.worker.isRunning()
        )
        message = "工作仍在執行中，確定要安全停止並離開？" if worker_running else "確定要離開嗎？"
        answer = QMessageBox.question(
            self, "離開確認", message,
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No,
        )
        if answer == QMessageBox.Yes:
            if worker_running:
                self.controller.stop_evaluation()
            event.accept()
        else:
            event.ignore()
