def common_elements(set_1, set_2):
    common_list = []
    for i in set_1:
        if i in set_2:
            common_list.append(i)
    return common_list
