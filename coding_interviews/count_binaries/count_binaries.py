def count_binaries(binary_string, requests):
    result = []
    flipped = (''.join(['0' if el == '1' else '1' for el in binary_string]))

    for i in range(len(requests)):
        if 'count' in requests[i]:
            index = int(requests[i].split(':')[1])
            result.append(binary_string[:index].count('0'))
        elif 'flip' in requests[i]:
            binary_string = flipped
    return result


binaries = "1111010"
request_list = ["count:4", "count:6", "flip", "count:4", "flip", "count:2"]


print(count_binaries(binaries, request_list))  # Output: [1, 2, 4, 0]
