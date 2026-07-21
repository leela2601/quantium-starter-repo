import csv

input_files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv",
]

output_file = "formatted_sales_data.csv"

with open(output_file, "w", newline="") as out_csv:
    writer = csv.writer(out_csv)
    writer.writerow(["Sales", "Date", "Region"])

    for file_path in input_files:
        with open(file_path, "r", newline="") as in_csv:
            reader = csv.DictReader(in_csv)
            for row in reader:
                if row["product"].strip().lower() != "pink morsel":
                    continue
                price = float(row["price"].replace("$", ""))
                quantity = int(row["quantity"])
                sales = price * quantity
                writer.writerow([f"{sales:.2f}", row["date"], row["region"]])

print(f"Done. Wrote output to {output_file}")
