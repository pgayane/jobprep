def sum_of_list(list):
    if len(list) == 0:
        return 0
    else: 
        return list[0] + sum_of_list(list[1:])


if __name__ == '__main__':

    print sum_of_list([0, 1, -2, 3])
