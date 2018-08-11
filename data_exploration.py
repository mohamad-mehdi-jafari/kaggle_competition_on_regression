import numpy as np # linear algebra
import random



def normalizer(matrix):
    answer = matrix
    if len(matrix.shape)==2:
        colums = matrix.shape[1]
        for i in range(0, colums):
            mean = np.mean(matrix[:, i])
            std = np.std(matrix[:, i])
            answer[:, i] = (matrix[:, i] - mean) / std
    else:
        mean = np.mean(matrix)
        std = np.std(matrix)
        answer = (matrix - mean) / std


    return answer


def batch_generator(batch_size):
    matrix = np.loadtxt("matrix.out")
    labels = np.loadtxt("labels.out")
    labels = normalizer(labels)
    matrix = normalizer(matrix)
    counter = 0
    while True:
        Xmatrix = []
        Yvector = []
        for i in range(0, batch_size):
            Ynumber = []
            Xvector = []
            first = random.randint(0, matrix.shape[0]-1)
            second = random.randint(0, matrix.shape[0]-1)
            counter = counter+ 1
            Xvector = Xvector + list(matrix[first])
            Xvector = Xvector + list(matrix[second])
            Ynumber = Ynumber + [labels[first]-labels[second]]
            Xmatrix.append(Xvector)
            Yvector.append(Ynumber)
        yield Xmatrix, Yvector

if __name__ == '__main__':
    batch_generator = batch_generator(2)
    a , b = next(batch_generator)
    x = np.array(a)
    y = np.array(b)

    print(x.shape)
    print(y.shape)

    print(x.dtype)
    print(y.dtype)

    print(normalizer(np.array([[2.0, 2, 4], [3 ,5, 8]])))