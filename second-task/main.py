def get_cats_info(path: str) -> list[dict]:
    """
    Читає файл, де кожен рядок має формат:
      <id>,<name>,<age>
    і повертає список словників з ключами: "id", "name", "age".
    Невалідні рядки акуратно пропускаються.
    Якщо файл не знайдено — повертає порожній список.
    """
    cats: list[dict] = []

    try:
        # utf-8-sig на випадок BOM
        with open(path, encoding="utf-8-sig") as f:
            for i, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue

                parts = line.split(",", 2)  
                if len(parts) != 3:
                    # рядок з неправильною кількістю полів — пропускаємо
                    continue

                cat_id, name, age = (p.strip() for p in parts)

                # базова валідація: всі три поля мають бути непорожні
                if not cat_id or not name or not age:
                    continue

                # За умовою прикладу "age" — рядок, тому не перетворюємо на int
                cats.append({"id": cat_id, "name": name, "age": age})

    except FileNotFoundError:
        # файл не існує — повертаємо []
        return []

    return cats

print(get_cats_info("cats_file.txt"))
