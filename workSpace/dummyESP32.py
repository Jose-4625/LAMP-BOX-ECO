import random
def raw_temperature():
    return random.randint(1,100)
def hall_sensor():
    return random.randint(1,100)


if __name__ == "__main__":
    print(raw_temperature())
    print(hall_sensor())
