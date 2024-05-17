import numpy as np


def calculate(input):
    input_list = input.split(',')
    results = dict()

    try:
        if len(input_list) < 9 or len(input_list) > 9:
            raise ValueError
    except ValueError:
        print('Exception ocurred: List must contain nine numbers')
        return
    try:
        for i in input_list:
            int(i)
    except ValueError:
        print('Exception ocurred: All values must be numbers')
        return
    #I create my np matrix
    matrix = np.array(input_list, dtype='float').reshape((3,3))

    #Create the mean values
    results['mean'] = list()
    results['mean'].append(matrix.mean(axis=0).tolist())
    results['mean'].append(matrix.mean(axis=1).tolist())
    results['mean'].append(matrix.mean().tolist())

    # Create the variance values
    results['variance'] = list()
    results['variance'].append(matrix.var(axis=0).tolist())
    results['variance'].append(matrix.var(axis=1).tolist())
    results['variance'].append(matrix.var().tolist())

    # Create the standard deviation values
    results['standard deviation'] = list()
    results['standard deviation'].append(matrix.std(axis=0).tolist())
    results['standard deviation'].append(matrix.std(axis=1).tolist())
    results['standard deviation'].append(matrix.std().tolist())

    # Create the max values
    results['max'] = list()
    results['max'].append(matrix.max(axis=0).tolist())
    results['max'].append(matrix.max(axis=1).tolist())
    results['max'].append(matrix.max().tolist())

    # Create the min values
    results['min'] = list()
    results['min'].append(matrix.min(axis=0).tolist())
    results['min'].append(matrix.min(axis=1).tolist())
    results['min'].append(matrix.min().tolist())

    # Create the sum values
    results['sum'] = list()
    results['sum'].append(matrix.sum(axis=0).tolist())
    results['sum'].append(matrix.sum(axis=1).tolist())
    results['sum'].append(matrix.sum().tolist())

    #In order to better print the dictionary
    print("{" + "\n".join("{}: {},".format(k, v) for k, v in results.items()) + "}")

input = input('Pass 9 numbers separated by commas: ')
calculate(input)
