from pathlib import Path


def classify_size(petal_len: float) -> str:
    if petal_len < 2.0:
        return "Small"
    if petal_len < 5.0:
        return "Medium"
    return "Large"


def read_iris_data(path: Path):
    iris_list = []
    try:
        with path.open("r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                fields = line.split(",")
                if fields[0].strip().lower() == "sepal_len":
                    continue
                flower = {
                    "sepal_len": float(fields[0]),
                    "sepal_wid": float(fields[1]),
                    "petal_len": float(fields[2]),
                    "petal_wid": float(fields[3]),
                    "species": fields[4].strip().replace("Iris-", "").lower(),
                }
                iris_list.append(flower)
    except FileNotFoundError:
        print(f"找不到檔案：{path}")
        return []

    return iris_list


def write_report(path: Path, species_count: dict, size_count: dict, large_virginica: list):
    with path.open("w", encoding="utf-8") as file:
        file.write("各品種數量\n")
        for species in ("setosa", "versicolor", "virginica"):
            file.write(f"{species}: {species_count.get(species, 0)}\n")

        file.write("\n各等級數量\n")
        for size in ("Small", "Medium", "Large"):
            file.write(f"{size}: {size_count.get(size, 0)}\n")

        file.write(f"\nLarge 且 virginica 的朵數: {len(large_virginica)}\n")
        if large_virginica:
            file.write(f"sepal_len 最大值: {max(large_virginica):.1f}\n")
            file.write(f"sepal_len 最小值: {min(large_virginica):.1f}\n")
            file.write(f"sepal_len 平均值: {sum(large_virginica) / len(large_virginica):.2f}\n")


def main():
    data_path = Path(__file__).with_name("iris_data.csv")
    report_path = Path(__file__).with_name("iris_report.txt")

    iris_list = read_iris_data(data_path)
    if not iris_list:
        return

    species_count = {}
    size_count = {"Small": 0, "Medium": 0, "Large": 0}
    large_virginica = []

    for flower in iris_list:
        species = flower["species"]
        species_count[species] = species_count.get(species, 0) + 1

        size = classify_size(flower["petal_len"])
        size_count[size] = size_count.get(size, 0) + 1

        if size == "Large" and species == "virginica":
            large_virginica.append(flower["sepal_len"])

    print("各品種數量：")
    for species in ("setosa", "versicolor", "virginica"):
        print(f"{species}: {species_count.get(species, 0)}")

    print("\n各等級數量：")
    for size in ("Small", "Medium", "Large"):
        print(f"{size}: {size_count.get(size, 0)}")

    print(f"\nLarge 且 virginica 的朵數: {len(large_virginica)}")
    if large_virginica:
        print(f"sepal_len 最大值: {max(large_virginica):.1f}")
        print(f"sepal_len 最小值: {min(large_virginica):.1f}")
        print(f"sepal_len 平均值: {sum(large_virginica) / len(large_virginica):.2f}")

    write_report(report_path, species_count, size_count, large_virginica)
    print(f"\n報告已寫入: {report_path}")


if __name__ == "__main__":
    main()
