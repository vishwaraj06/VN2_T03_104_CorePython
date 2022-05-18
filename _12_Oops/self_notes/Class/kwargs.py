def intro(**data):
    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="Sa", Lastname="Sha", Age=42, Phone=1234567890,address="salem")