def remove_duplicates(sequence):
    result = []
    for i in range(len(sequence)):
        if sequence[i] not in result:
            result.append(sequence[i])
    return result

print remove_duplicates([1,3,3,4,1,5,8])
