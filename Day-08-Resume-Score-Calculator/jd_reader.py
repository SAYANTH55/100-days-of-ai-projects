def read_jd(file_path):
    with open(file_path, "r") as file:
        content = file.read().splitlines()
    return set(content)