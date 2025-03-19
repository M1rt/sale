def generate_drive_links(num_links=300):
    base_url = "https://drive.google.com/file/d/1TBa1zl3VnYuqA5dXGNCaIZiRhNgFA1hT/view?usp=sharing"
    links = [f"{i}. {base_url}" for i in range(1, num_links + 1)]

    with open("google_drive_links.txt", "w", encoding="utf-8") as f:
        for link in links:
            f.write(link + "\n")

    print(f"Сгенерил 300 ссылок, пиздец, и засунул их в google_drive_links.txt")
    print("Первые 5 для примера, сука:")
    for link in links[:700]:
        print(link)


if __name__ == "__main__":
    generate_drive_links()