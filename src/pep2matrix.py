import math
import re
from argparse import ArgumentParser

property_dic = {
    'property_chou': {
        'A': '0.62	-0.5	15.0	2.35	9.87	6.11',
        'C': '0.29	-1.0	47.0	1.71	10.78	5.02',
        'D': '-0.90	3.0	59.0	1.88	9.60	2.98',
        'E': '-0.74	3.0	73.0	2.19	9.67	3.08',
        'F': '1.19	-2.5	91.0	2.58	9.24	5.91',
        'G': '0.48	0.0	1.0	2.34	9.60	6.06',
        'H': '-0.40	-0.5	82.0	1.78	8.97	7.64',
        'I': '1.38	-1.8	57.0	2.32	9.76	6.04',
        'K': '-1.50	3.0	73.0	2.20	8.90	9.47',
        'L': '1.06	-1.8	57.0	2.36	9.60	6.04',
        'M': '0.64	-1.3	75.0	2.28	9.21	5.74',
        'N': '-0.78	0.2	58.0	2.18	9.09	10.76',
        'P': '0.12	0.0	42.0	1.99	10.60	6.30',
        'Q': '-0.85	0.2	72.0	2.17	9.13	5.65',
        'R': '-2.53	3.0	101.0	2.18	9.09	10.76',
        'S': '-0.18	0.3	31.0	2.21	9.15	5.68',
        'T': '-0.05	-0.4	45.0	2.15	9.12	5.60',
        'V': '1.08	-1.5	43.0	2.29	9.74	6.02',
        'W': '0.81	-0.34	130.0	2.38	9.39	5.88',
        'Y': '0.26	-2.3	107.0	2.20	9.11	5.63'
    },
    'property': {
        'G': '5.97	-0.4	1	0	0	0',
        'A': '6.02	-4.5	15	0	0	0',
        'V': '5.97	4.2	43	0	0	0',
        'L': '5.98	3.8	57	0	0	0',
        'I': '6.02	4.5	57	0	0	0',
        'M': '5.75	1.9	75	0	0	0',
        'P': '6.3	-1.6	42	0	1	0',
        'F': '5.48	2.8	91	0	0	0',
        'W': '5.89	-0.9	130	0	0	0',
        'S': '5.68	-0.8	31	0	1	0',
        'T': '6.53	-0.7	45	0	1	0',
        'N': '5.41	-3.5	58	0	1	0',
        'Q': '5.65	-3.5	72	0	1	0',
        'Y': '5.66	-1.3	107	0	0	0',
        'C': '5.02	2.5	47	0	1	0',
        'K': '9.74	-3.9	73	1	1	0',
        'R': '10.76	1.8	101	1	1	0',
        'H': '7.59	-3.2	82	1	1	0',
        'D': '2.97	-3.5	58	-1	1	1',
        'E': '3.22	-3.5	72	-1	1	1'
    },
    'binary': {
        'A': '1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0',
        'C': '0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0',
        'D': '0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0',
        'E': '0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0',
        'F': '0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0',
        'G': '0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0',
        'H': '0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0',
        'I': '0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0',
        'K': '0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0',
        'L': '0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0',
        'M': '0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0',
        'N': '0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0',
        'P': '0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0',
        'Q': '0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0',
        'R': '0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0',
        'S': '0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0',
        'T': '0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0',
        'V': '0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0',
        'W': '0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0',
        'Y': '0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1'
    },
    'index': {
        'A': '1',
        'C': '2',
        'D': '3',
        'E': '4',
        'F': '5',
        'G': '6',
        'H': '7',
        'I': '8',
        'K': '9',
        'L': '10',
        'M': '11',
        'N': '12',
        'P': '13',
        'Q': '14',
        'R': '15',
        'S': '16',
        'T': '17',
        'V': '18',
        'W': '19',
        'Y': '20'
    }
}


# convert an amino acid character to vector according to matrix_type
def convert(char, matrix_type):
    assert 65 <= ord(char) <= 90, 'unrecognized amino acid!'
    if char == 'G':
        rtn_str = property_dic[matrix_type]['G']
    elif char == 'A':
        rtn_str = property_dic[matrix_type]['A']
    elif char == 'V':
        rtn_str = property_dic[matrix_type]['V']
    elif char == 'L':
        rtn_str = property_dic[matrix_type]['L']
    elif char == 'I':
        rtn_str = property_dic[matrix_type]['I']
    elif char == 'M':
        rtn_str = property_dic[matrix_type]['M']
    elif char == 'P':
        rtn_str = property_dic[matrix_type]['P']
    elif char == 'F':
        rtn_str = property_dic[matrix_type]['F']
    elif char == 'W':
        rtn_str = property_dic[matrix_type]['W']
    elif char == 'S':
        rtn_str = property_dic[matrix_type]['S']
    elif char == 'T':
        rtn_str = property_dic[matrix_type]['T']
    elif char == 'N':
        rtn_str = property_dic[matrix_type]['N']
    elif char == 'Q':
        rtn_str = property_dic[matrix_type]['Q']
    elif char == 'Y':
        rtn_str = property_dic[matrix_type]['Y']
    elif char == 'C':
        rtn_str = property_dic[matrix_type]['C']
    elif char == 'K':
        rtn_str = property_dic[matrix_type]['K']
    elif char == 'R':
        rtn_str = property_dic[matrix_type]['R']
    elif char == 'H':
        rtn_str = property_dic[matrix_type]['H']
    elif char == 'D':
        rtn_str = property_dic[matrix_type]['D']
    elif char == 'E':
        rtn_str = property_dic[matrix_type]['E']
    else:
        print('[-]wrong character in file!')
        rtn_str = 'None'
    return rtn_str


def pep2matrix(peptide):
    def transpose(matrix):
        new_matrix = []
        for i in range(len(matrix[0])):
            matrix1 = []
            for j in range(len(matrix)):
                matrix1.append(matrix[j][i])
            new_matrix.append(matrix1)
        return new_matrix

    rtn_matrix = []
    for aa in peptide:
        tmp_vector = [convert(aa, 'index')]
        tmp = convert(aa, 'property')
        tmp_vector.extend(tmp.split('\t'))
        tmp = convert(aa, 'property_chou')
        tmp_vector.extend(tmp.split('\t'))
        rtn_matrix.append(tmp_vector)
        # rtn_materxi.append()
    return transpose(rtn_matrix)


def matrix_extend(matrix, dimensionX, dimensionY):
    X_matrix = len(matrix[0])
    Y_matrix = len(matrix)
    assert X_matrix <= dimensionX, 'target dimension X too small'
    assert Y_matrix <= dimensionY, 'target dimension Y too small'
    for row in matrix:
        for i in range(0, dimensionX - X_matrix):
            row.append('0')
    tmp_vec = ['0' for i in range(0, dimensionX)]
    for i in range(0, dimensionY - Y_matrix):
        matrix.append(tmp_vec)
    return matrix


def matrix_output_to_file(matrix, file_path):
    with open(file_path, 'w') as fp_out:
        for row in matrix:
            for col in row:
                fp_out.write(col + '\t')
            fp_out.write('\n')
        fp_out.write('\n')


def pep_input_from_file(file_in):
    pep_list = []
    with open(file_in, 'r') as fp_in:
        for line in fp_in:
            pep_list.append(line.replace('\n', ''))
    return pep_list


if __name__ == '__main__':
    # file_name = '/home/han/test_input'
    # pep_l = pep_input_from_file(file_name)
    # file_name_out = '/home/han/test_out'
    # with open(file_name_out, 'w') as f:
    #     for pep in pep_l:
    #         matrix = pep2matrix(pep)
    #         matrix = matrix_extend(matrix, 20, 20)
    #         matrix_output_to_file(matrix, f)
    matrix = pep2matrix('AADHW')
    print(len(matrix[0]))
    print(len(matrix))
    matrix = matrix_extend(matrix, 5, 13)
    for line in matrix:
        print(line)
    matrix_output_to_file(matrix, '/home/han/test')
