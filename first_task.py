def total_salary(path: str) -> tuple[int, float]:
    """
    Читає файл зі строками 'Ім’я Прізвище,сума' і повертає (total, average).
    Якщо файл відсутній або немає валідних рядків — повертає (0, 0).
    """
    total = 0.0
    count = 0

    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    _, salary_str = line.split(",", 1)
                    salary = float(salary_str)
                except ValueError:
                    # Рядок з помилкою формату — пропускаємо
                    continue

                total += salary
                count += 1
    except FileNotFoundError:
        return (0, 0)

    if count == 0:
        return (0, 0)

    average = total / count

    # Повернемо акуратно: якщо без дробної частини — як int
    def tidy(x):
        return int(x) if isinstance(x, float) and x.is_integer() else x

    return tidy(total), tidy(average)

total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

