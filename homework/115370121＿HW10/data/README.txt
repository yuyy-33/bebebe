本資料夾為 P2_W10_Numerical_Tools_Packages 教材的範例資料（程式中以 data/檔名 讀取）

grades.csv
  模擬成績資料，30 位學生（學號 S01–S30），欄位：學號、班級（A／B／C）、程式、數學、英文
  英文有 1 筆缺值（S07），供 fillna／dropna 練習；UTF-8 編碼
  由 build/make_data.py 以 NumPy 亂數（種子 10）產生，非真實學生資料

grades.xlsx
  與 grades.csv 內容相同的 Excel 版（工作表「成績」），供 pd.read_excel 練習（需安裝 openpyxl）

iris.csv
  Iris 鳶尾花資料集，150 筆、3 個品種各 50 筆
  欄位：sepal_length、sepal_width、petal_length、petal_width（單位 cm）、species（setosa／versicolor／virginica）
  來源：UCI Machine Learning Repository, Iris（R. A. Fisher, 1936），https://archive.ics.uci.edu/dataset/53/iris
  取自下載檔中的 bezdekIris.data（已修正 iris.data 第 35、38 筆與 Fisher 原文不符之處），並加上欄名、去掉品種名稱前的「Iris-」
  與 scikit-learn 的 load_iris() 數值完全相同
  DOI：10.24432/C56C76；授權：CC BY 4.0（UCI 頁面標示）

uci_iris/
  UCI 下載的原始檔：iris.data（原始版，第 35、38 筆有誤）、bezdekIris.data（修正版）、iris.names（資料說明）、Index
