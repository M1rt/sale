import random
import time
from datetime import datetime

def generate_android_user_agent():
    android_versions = ["10", "11", "12", "13", "14"]
    devices = [
        "Pixel 7; Pixel 7", "SM-G998B; Galaxy S21 Ultra", "SM-A525F; Galaxy A52",
        "Redmi Note 10 Pro; Redmi Note 10 Pro", "POCO X5 Pro; POCO X5 Pro"
    ]
    instagram_versions = ["320.0.0.42.101", "319.0.9.40.102", "318.0.7.38.103", "317.0.4.36.104"]

    android_ver = random.choice(android_versions)
    device = random.choice(devices)
    ig_ver = random.choice(instagram_versions)

    return f"Instagram {ig_ver} Android ({android_ver}/5.{random.randint(0, 9)}; 480dpi; 1080x1920; {device}; samsung/google/xiaomi; en_US; {random.randint(400000000, 499999999)})"


def generate_ios_user_agent():
    ios_versions = ["15.6", "16.0", "16.1", "16.5", "17.0", "17.3"]
    devices = ["iPhone13,2", "iPhone14,5", "iPhone15,3", "iPad13,1"]
    instagram_versions = ["320.0.1", "319.1.2", "318.0.3", "317.0.4"]

    ios_ver = random.choice(ios_versions)
    device = random.choice(devices)
    ig_ver = random.choice(instagram_versions)

    return f"Instagram {ig_ver} iPhone ({device}; iOS {ios_ver}; en_US; en; scale=2.00; 1170x2532; {random.randint(400000000, 499999999)})"


def load_existing_agents(filename="user_agents.txt"):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return set(line.strip() for line in f if line.strip())
    except FileNotFoundError:
        return set()  # Если файла нет, начинаем с пустого множества


def save_to_file(num_agents=50000, filename="user_agents.txt"):
    while True:
        # Загружаем существующие агенты из файла
        existing_agents = load_existing_agents(filename)
        new_agents = set()

        # Генерим новые уникальные агенты, пока не наберем 50k
        while len(new_agents) < num_agents:
            # 50/50 шанс на Android или iOS
            if random.random() < 0.5:
                agent = generate_android_user_agent()
            else:
                agent = generate_ios_user_agent()
            new_agents.add(agent)

        # Добавляем только те, которых еще нет в файле
        unique_new_agents = new_agents - existing_agents
        total_new = len(unique_new_agents)

        if total_new > 0:
            with open(filename, "a", encoding="utf-8") as f:
                for agent in unique_new_agents:
                    f.write(agent + "\n")
            print(f"Долбанул {total_new} новых уникальных юзер-агентов в {filename}, пиздец!")
            print(f"Всего в файле теперь: {len(existing_agents) + total_new} строк, сука!")
        else:
            print("Ни хуя нового не добавил, все агенты уже были, ебаный случай!")

        print("Жду 120 минут, потом снова пиздец начинается!")
        time.sleep(7200)  # 120 минут = 7200 секунд


if __name__ == "__main__":
    print("Запускаю эту хуйню, один файл, никаких повторов, держись, motherfucker!")
    save_to_file(50000)