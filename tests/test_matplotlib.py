import matplotlib.pyplot as plt


# a = [0, 1, 2, 3, 4, 5]
# b = [12, 15, 13, 18, 8, 3]

dictionary = {1: 10, 2: 11, 3: 12, 4: 11, 5: 13}

# plt.plot(a, b, 'r+')

a = list(dictionary.keys())
b = []

for i in a:
    b.append(dictionary[i])

figure = plt.figure()

plt.plot(a, b, color='red', marker='o', linestyle='dashed')
plt.title('График зависимости ответов от задержки.')
plt.xlabel('Время задержки, с.')
plt.ylabel('Время ответа, с.')

plt.show()

figure.savefig('foo.png')



# import matplotlib
# import matplotlib.pyplot as plt
# import numpy as np
#
# y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# x = np.arange(10)
# fig = plt.figure()
# ax = plt.subplot(111)
# ax.plot(x, y, label='$y = numbers')
# plt.title('Legend inside')
# ax.legend()
# # plt.show()
# fig.savefig('plot.png')
