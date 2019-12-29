
def read_file(name:str):
    with open(name, "r") as file:
        data = file.read()

    result = set()
    for word in data.split():
        result.add(word.lower().replace(".", "").replace(",", ""))

    return result

def save_file(name:str):
    result = read_file(name)
    count = len(result)
    print("Всего уникальных слов: {}".format(count))
    for value in result:
        print(value)


if __name__ == '__main__':
    print(read_file("1.txt"))
    save_file("1.txt")

