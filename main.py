class DataProcesser:
    def __init__(self, path_to_file):
        self.data = []

        # 파일 읽어오기
        with open(path_to_file, "r") as f:
            if "csv" in path_to_file:
                for line in f:
                    self.data.append(line.strip().split(","))
            elif "txt" in path_to_file:
                for line in f:
                    self.data.append(line.split())

        # 전체 판매량 데이터
        self.total_sales = {}
        for row in range(1, len(self.data[0])):
            self.total_sales[self.data[0][row]] = sum(
                int(self.data[sales_a_day][row])
                for sales_a_day in range(1, len(self.data))
            )

        # 하루평균 판매량 데이터
        self.avg_sales = {}
        for coffee, sales_value in self.total_sales.items():
            self.avg_sales[coffee] = round(float(sales_value / (len(self.data) - 1)), 1)

    # CSV 파일로 출력
    def export_file(self, path_to_file):
        with open(path_to_file, "w") as f:
            if "total" in path_to_file:
                data = [
                    [coffe for coffe in self.total_sales.keys()],
                    [str(sales) for sales in self.total_sales.values()],
                ]
            elif "avg" in path_to_file or "average" in path_to_file:
                data = [
                    [coffe for coffe in self.avg_sales.keys()],
                    [str(sales) for sales in self.avg_sales.values()],
                ]
            for line in data:
                f.write(",".join(line) + "\n")

    # 콘솔로 출력
    def show_tables(self):
        print("Daily sales data for coffee from the file is:")
        print("==================================================================")
        for line in self.data:
            print("| " + " | ".join("{:<10}".format(cell) for cell in line) + " |")
        print("==================================================================")
        print("")
        print("The total sales data for coffee from the file is:")
        print("=====================================================")
        print(
            "| "
            + " | ".join("{:<10}".format(key) for key in self.total_sales.keys())
            + " |"
        )
        print(
            "| "
            + " | ".join("{:<10}".format(value) for value in self.total_sales.values())
            + " |"
        )
        print("=====================================================")
        print("")
        print("The average sales data for coffee from the file is:")
        print("=====================================================")
        print(
            "| "
            + " | ".join("{:<10}".format(key) for key in self.avg_sales.keys())
            + " |"
        )
        print(
            "| "
            + " | ".join("{:<10}".format(value) for value in self.avg_sales.values())
            + " |"
        )
        print("=====================================================")


data_processer = DataProcesser("./data.txt")
data_processer.show_tables()
data_processer.export_file("./total_sales.csv")
data_processer.export_file("./avg_sales.csv")
