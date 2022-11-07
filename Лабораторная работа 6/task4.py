import json

INPUT_FILE = "input.csv"    # Использовал файл из task3, так как в оригинале непереводимая каша


def csv_to_list_dict(filename: str, delimiter: str = ',', new_line: str = '\n') -> list[dict]:
    with open(filename, 'rt') as f:
        list_dict = list()
        headers = f.readline().split(sep=delimiter)
        for line in f:
            line = line.split(sep=delimiter)
            dict_ = {headers[i].replace(new_line, ''): line[i].replace(new_line, '') for i in range(len(headers))}
            list_dict.append(dict_)
    return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4, ensure_ascii=False))
