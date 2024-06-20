def find_common_elements(list_1, list_2):
    common = []
    for item in list_1:
        if item in list_2:
            common.append(item)
    return common
