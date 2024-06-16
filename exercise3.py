def count_word(file_path):
    counter = {}
    a_file = open(file_path, 'r')
    data = a_file.read()
    data1 = data.lower()
    data2 = data1.split()
    a_file.close()
    for i in range(len(data2)):
        counter.update({data2[i]: data2.count(data2[i])})
    return counter


file_path = 'C:/Users/Hanh/Downloads/P1_data.txt'
print(count_word(file_path))
