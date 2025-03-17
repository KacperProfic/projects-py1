def count_files_per_category(filename):
    category_counts = {}

    try:
        with open(filename, 'r') as file:
            for line in file:
                path = line.strip()
                if not path:
                    continue

                parts = path.split('/')
                if len(parts) >= 3:
                    category = parts[2]
                    if category:
                        category_counts[category] = category_counts.get(category, 0) + 1
        print("Number of files per category:")
        for category, count in category_counts.items():
            print(f"{category}:{count}")

    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"error {e}")

count_files_per_category("pliczek2.txt")