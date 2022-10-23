def delete(list_, index=None):
    last_index = len(list_) - 1
    if index == 0:
        return list_[1:]
    elif index == last_index or not index:
        return list_[:-1]
    else:
        return list_[:index] + list_[index+1:]


print(delete([0, 0, 1, 2], index=0))
print(delete([0, 1, 1, 2, 3], index=1))
print(delete([0, 1, 2, 3, 4, 4]))
