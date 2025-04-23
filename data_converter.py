def string_to_txt(filename, data):
    files = []
    i = 0
    for item in data:
        writename = filename + str(i)
        with open(writename + ".txt", "w", encoding="utf-8") as file:
            file.write(item)
        files.append(writename + ".txt")
        i += 1
    return files
