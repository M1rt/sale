import random
import time

def generate_windows_chrome_useragent():
    chrome_version = f"{random.randint(90, 123)}.0.{random.randint(1000, 9999)}.{random.randint(0, 99)}"

    windows_platforms = [
        "Windows NT 10.0; Win64; x64",
        "Windows NT 10.0; WOW64",
        "Windows NT 6.1; Win64; x64",
        "Windows NT 6.3; Win64; x64"
    ]

    platform = random.choice(windows_platforms)

    user_agent = f"Mozilla/5.0 ({platform}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version} Safari/537.36"

    return user_agent


def load_existing_agents(filename="useragents.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return set(line.strip() for line in f if line.strip())
    except FileNotFoundError:
        return set()  # Если файла нет, начинаем с пустого


def save_useragents_to_file(filename="useragents.txt", count=50000):
    while True:
        # Загружаем существующие юзер-агенты
        existing_agents = load_existing_agents(filename)
        new_agents = set()

        # Генерим новые уникальные агенты, пока не наберем 50k
        while len(new_agents) < count:
            ua = generate_windows_chrome_useragent()
            new_agents.add(ua)

        # Фильтруем только те, которых еще нет
        unique_new_agents = new_agents - existing_agents
        total_new = len(unique_new_agents)

        if total_new > 0:
            with open(filename, "a", encoding="utf-8") as f:  # "a" — добавляем, не перезаписываем
                for agent in unique_new_agents:
                    f.write(f"{agent}\n")
            print(f"Сгенерил и добавил {total_new} новых уникальных Windows Chrome юзер-агентов в {filename}, пиздец!")
            print(f"Всего в файле теперь: {len(existing_agents) + total_new} строк, сука!")
        else:
            print("Ни хуя нового, все юзер-агенты уже были, ебаный рандом!")

        print("Жду 120 минут, потом снова ебашу хаос!")
        time.sleep(7200)  # 120 минут = 7200 секунд


if __name__ == "__main__":
    print("Запускаю эту хуйню, 50k Windows Chrome агентов каждые 120 минут, держись, motherfucker!")
    save_useragents_to_file("useragents.txt", 50000)