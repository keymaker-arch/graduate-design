import math
import re
from optparse import OptionParser, OptionGroup


# new function:support custom data set input in txt format
# set color message output, detect platform by
# sys.platform and check win or linux in the return value using re

# binary matrix output in vertical and horizontal form

class data_set():
    dic = {
        'chrt_chou': {
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
        'chrt': {
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
            'E': '3.22	-3.5	72	-1	1	1'},

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
            'Y': '0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1'},

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
            'Y': '20'}
    }

    # take in a matrix type and return a dictionary of a list of standarized property, add the dic in data_set with key 'matrix_type_std'
    def std_convert(self, matrix_type):
        unstd_dic = {}
        std_dic = {}
        list_sum_in_numerator = []
        list_denominator = []

        # convert char to float, store in a dictionary of a series of list ordered by aa
        for key, value in data_set.dic[matrix_type].items():
            tmp_list = value.split('\t')
            unstd_dic[key] = []
            for i in tmp_list:
                unstd_dic[key].append(float(i))

        # calc the sum in numerator, store in a list ordered by property
        for value in unstd_dic.values():
            if list_sum_in_numerator == []:
                for i in range(0, len(value)):
                    list_sum_in_numerator.append(0)
            else:
                for i in range(0, len(value)):
                    list_sum_in_numerator[i] += value[i] / 20.0

        # calc the denominator, store in a list ordered by property
        for i in range(0, len(list_sum_in_numerator)):
            tmp_list = []
            for value in unstd_dic.values():
                tmp_list.append(value[i])

            tmp_sum = 0
            for j in range(0, 20):
                tmp_sum += (tmp_list[j] - list_sum_in_numerator[i]) * (tmp_list[j] - list_sum_in_numerator[i])

            list_denominator.append(math.sqrt((tmp_sum / 20)))

        for key, value in unstd_dic.items():
            std_dic[key] = []
            for i in range(0, len(value)):
                std_dic[key].append((unstd_dic[key][i] - list_sum_in_numerator[i]) / list_denominator[i])

        data_set.dic[str(matrix_type) + '_std'] = std_dic

    def cus_in(self, f_cus, matrix_type):
        pattern_line = '^(.*?)\t(.*?)$'
        tmp_dic = {}
        for line in f_cus:
            match = re.search(pattern_line, line)
            if match:
                pep = match.group(1)
                prop = match.group(2)

                if pep in tmp_dic.keys():
                    print('[-]warning:multi peptide property detect, check matrix file input!')
                tmp_dic[pep] = prop
        if matrix_type != 'new':
            for key in data_set.dic[matrix_type].keys():
                if key in tmp_dic.keys():
                    data_set.dic[matrix_type][key] = tmp_dic[key]
        else:
            data_set.dic['cus'] = tmp_dic


# conver single letter peptide to matrix, char is one aa, matrix_type is the name of one of the three classes above, file_out is the pointer of result file
# this func can be called in the function below to convert a aa file
def convert(char, matrix_type):
    if char == 'G':
        rtn_str = data_set.dic[matrix_type]['G']
    elif char == 'A':
        rtn_str = data_set.dic[matrix_type]['A']
    elif char == 'V':
        rtn_str = data_set.dic[matrix_type]['V']
    elif char == 'L':
        rtn_str = data_set.dic[matrix_type]['L']
    elif char == 'I':
        rtn_str = data_set.dic[matrix_type]['I']
    elif char == 'M':
        rtn_str = data_set.dic[matrix_type]['M']
    elif char == 'P':
        rtn_str = data_set.dic[matrix_type]['P']
    elif char == 'F':
        rtn_str = data_set.dic[matrix_type]['F']
    elif char == 'W':
        rtn_str = data_set.dic[matrix_type]['W']
    elif char == 'S':
        rtn_str = data_set.dic[matrix_type]['S']
    elif char == 'T':
        rtn_str = data_set.dic[matrix_type]['T']
    elif char == 'N':
        rtn_str = data_set.dic[matrix_type]['N']
    elif char == 'Q':
        rtn_str = data_set.dic[matrix_type]['Q']
    elif char == 'Y':
        rtn_str = data_set.dic[matrix_type]['Y']
    elif char == 'C':
        rtn_str = data_set.dic[matrix_type]['C']
    elif char == 'K':
        rtn_str = data_set.dic[matrix_type]['K']
    elif char == 'R':
        rtn_str = data_set.dic[matrix_type]['R']
    elif char == 'H':
        rtn_str = data_set.dic[matrix_type]['H']
    elif char == 'D':
        rtn_str = data_set.dic[matrix_type]['D']
    elif char == 'E':
        rtn_str = data_set.dic[matrix_type]['E']
    else:
        print('[-]wrong charactor in file!')
        rtn_str = 'None'

    return rtn_str


# take one line of peptide, return each aa count in array fx_i, total aa count in aa_num and aa rate in array Vx_i
def count_aa(line):
    fx_i = [x * 0.0 for x in range(0, 20)]
    Vx_i = [x * 0.0 for x in range(0, 20)]
    aa_num = 0.0

    for char in line:

        if char == 'A':
            fx_i[0] += 1
        elif char == 'C':
            fx_i[1] += 1
        elif char == 'D':
            fx_i[2] += 1
        elif char == 'E':
            fx_i[3] += 1
        elif char == 'F':
            fx_i[4] += 1
        elif char == 'G':
            fx_i[5] += 1
        elif char == 'H':
            fx_i[6] += 1
        elif char == 'I':
            fx_i[7] += 1
        elif char == 'K':
            fx_i[8] += 1
        elif char == 'L':
            fx_i[9] += 1
        elif char == 'M':
            fx_i[10] += 1
        elif char == 'N':
            fx_i[11] += 1
        elif char == 'P':
            fx_i[12] += 1
        elif char == 'Q':
            fx_i[13] += 1
        elif char == 'R':
            fx_i[14] += 1
        elif char == 'S':
            fx_i[15] += 1
        elif char == 'T':
            fx_i[16] += 1
        elif char == 'V':
            fx_i[17] += 1
        elif char == 'W':
            fx_i[18] += 1
        elif char == 'Y':
            fx_i[19] += 1
        else:
            pass

    for i in range(0, 20):
        aa_num += fx_i[i]

    for i in range(0, 20):
        Vx_i[i] = fx_i[i] / aa_num

    return fx_i, Vx_i, aa_num


# rewrite this func, peptide2matrix(file_input, file_out, matrix_type, flag_new_line)
# flag_new_line is a boolen flag that determins whether to start a new line after converting an aa, if 0 is given the whole peptide will be output in one line
def peptide2matrix(file_input, file_out, matrix_type, flag_new_line, fix_dimension):
    f_out = open(file_out, 'w')
    f_input = open(file_input, 'r')

    if fix_dimension:
        if flag_new_line:
            print(
                'there is no use to fix dimension when using --fix and -n at the same time, for all aa is encoded in 20 dimensions!')
            for line in f_input:
                for char in line:
                    f_out.write(convert(char, matrix_type))
                    f_out.write('\n')
        else:
            biggest = 0
            for line in f_input:
                fx_i, Vx_i, L = count_aa(line)
                if L > biggest:
                    biggest = L

            biggest = biggest * 20
            f_input.seek(0)
            for line in f_input:
                dimension_count = 0
                for char in line:
                    if char == '\n':
                        break
                    else:
                        f_out.write(convert(char, matrix_type))
                        f_out.write('\t')
                        dimension_count += 20

                if dimension_count < biggest:
                    for i in range(0, int(biggest) - dimension_count):
                        f_out.write('0')
                        f_out.write('\t')
                f_out.write('\n')
    else:
        if flag_new_line:
            for line in f_input:
                for char in line:
                    f_out.write(convert(char, matrix_type))
                    f_out.write('\n')
        else:
            for line in f_input:
                for char in line:
                    f_out.write(convert(char, matrix_type))
                    f_out.write('\t')
                f_out.write('\n')

    f_out.close()
    f_input.close()


def acc(file_input, file_out):
    f_input = open(file_input, 'r')
    f_out = open(file_out, 'w')

    for line in f_input:

        fx_i, Vx_i, aa_num = count_aa(line)

        for i in range(0, 20):
            f_out.write(str(Vx_i[i]) + '\t')

        f_out.write('\n')

    f_input.close()
    f_out.close()


def edp(file_input, file_out):
    f_input = open(file_input, 'r')
    f_out = open(file_out, 'w')

    for line in f_input:
        H_x = 0.0
        Sx_i = [x * 0.0 for x in range(0, 20)]
        fx_i, Vx_i, aa_num = count_aa(line)

        for i in range(0, 20):
            if Vx_i[i] == 0:
                pass
            else:
                H_x += -Vx_i[i] * (math.log(Vx_i[i], 2))

        for i in range(0, 20):
            if Vx_i[i] == 0:
                pass
            else:
                Sx_i[i] = Vx_i[i] * (math.log(Vx_i[i], 10)) / (-H_x)

        for i in range(0, 20):
            f_out.write(str(Sx_i[i]) + '\t')

        f_out.write('\n')

    f_input.close()
    f_out.close()


def PseAAC(file_input, file_out, lamda, omega, matrix_type):
    # calc the THETA of two aa, take in two unfix length lists of aa property and return a float
    def thetA(aa_1, aa_2):
        if len(aa_1) != len(aa_2):
            print('the number of property chosen for every amino acids should be the same!')

        tmp_sum = 0.0
        for i in range(0, len(aa_1)):
            tmp_sum += math.pow((1.0 * aa_1[i] - 1.0 * aa_2[i]), 2)

        return tmp_sum / (len(aa_1))

    # calc the theta of an aa, return theta vector in list and the sum
    def theta(line, L):
        tht = []
        tht_sum = 0.0
        data_set.std_convert(matrix_type)

        for lmd in range(0, lamda):
            tmp_sum = 0.0
            for i in range(0, int(L - lmd - 1)):
                tmp_sum += thetA(data_set.dic[matrix_type + '_std'][line[i]],
                                 data_set.dic[matrix_type + '_std'][line[i + 1]])

            tht.append(tmp_sum / (L - lmd - 1))

        for t in tht:
            tht_sum += t

        return tht, tht_sum

    f_input = open(file_input, 'r')
    f_out = open(file_out, 'w')

    for line in f_input:
        fx_i, Vx_i, L = count_aa(line)
        tht, tht_sum = theta(line, L)
        X = []

        for u in range(0, 20 + lamda):
            if u < 20:
                x_u = Vx_i[u] / (1 + omega * tht_sum)
            elif u >= 20:
                x_u = (omega * tht[u - 20]) / (1 + omega * tht_sum)
            else:
                print('[-]something is wrong! check parameters you are using!')
                x_u = 0

            X.append(x_u)

        for x in X:
            f_out.write(str(x) + '\t')

        f_out.write('\n')


if __name__ == '__main__':

    MSG_example = 'Example:\n' + 'python3 peptide2matrix -B --fix -p peptide_train.txt -m result.txt \n'
    MSG_usage = 'usage: python3 peptide2matrix_old.py [-P --lamda <lamda> --omega <omega>] [-B --fix -n] [-A] [-E] -p <FILE_INPUT.txt> -m <FILE_OUT.txt>'

    # basic options, including acc and edp
    parser = OptionParser(usage=MSG_usage, epilog=MSG_example)
    parser.add_option('-p', action='store', dest='file_input', type='string',
                      help='the peptide file in txt format, one peptide each line')
    parser.add_option('-m', action='store', dest='file_out', type='string',
                      help='the output matrix, should be refered to a txt file')

    # PesAA options
    group_pesaa = OptionGroup(parser,
                              'PesAA specific options, use -P option to encode with PesAA, lamda and omega is needed. PI, hydrophilism and side chain molicular weight is choosen for property of aa in default, you can specify your own aa property in a txt file, refer to costomer input options for detail')
    group_pesaa.add_option('-P', '--PesAA', action='store_true', dest='pesaa', help='encode with PesAA', default=False)
    group_pesaa.add_option('--lambda', action='store', dest='lambda', type='int', help='', default=0)
    group_pesaa.add_option('--omega', action='store', dest='omega', type='float', help='', default=0)
    parser.add_option_group(group_pesaa)

    # BPP options
    group_binary = OptionGroup(parser, 'Binary specific options, use -b option to encode to binary matrix')
    group_binary.add_option('-B', '--binary', action='store_true', dest='flag_binary',
                            help='encode the peptide to binary matrix', default=False)
    group_binary.add_option('--fix', action='store_true', dest='dimension',
                            help='fix the dimension of the matrix according to the longest peptide in input, ignored by -n',
                            default=False)
    group_binary.add_option('-n', '--new-ln', action='store_true', dest='line',
                            help='use this option if you want to start a new line after converting an amino acid, which means that one peptide will be output in multi lines, default is False',
                            default=False)
    parser.add_option_group(group_binary)

    # other encoding options
    group_other = OptionGroup(parser, 'Some other encoding ')
    group_other.add_option('-A', '--acc', action='store_true', dest='flag_acc', help='encode with acc', default=False)
    group_other.add_option('-E', '--edp', action='store_true', dest='flag_edp', help='encode with edp', default=False)
    parser.add_option_group(group_other)

    # custom matrix file input
    group_cus = OptionGroup(parser, 'Custom amino acid encoding matrix')
    group_cus.add_option('-F', '--file', action='store', dest='cus_file',
                         help='the file containing your matrix. In the file each amino acid takes up one line seperated by tab, and the amino acid should be marked as a single upper case English letter. The file does not have to be completely new, which means you can enter part of amino acid to change or add a new amino acid the exsisting matrix in this program. When doing so, you have to specify an encoding method',
                         defaul='')
    group_cus.add_option('--new', action='store_true', dest='flag_file',
                         help='use this option if you are entering a completely new matrix for encoding. Do make sure your matrix contains all amino acids that is needed for your encoding or it may cause fatal error!',
                         defaut=False)
    parser.add_option_group(group_cus)

    (options, args) = parser.parse_args()

    if options.flag_binary:
        # if options.cus_file != '' and options.flag_file:
        # 	data_set.cus_in(f_cus=open(options.cus_file, 'r'), matrix_type='binary')
        # else:
        # 	print('[-]error:')
        peptide2matrix(options.file_input, options.file_out, 'binary', options.line, options.dimension)
        print('[*] done!check %s for detail!' % options.file_out)
    elif options.flag_edp:
        edp(options.file_input, options.file_out)
        print('[*] done!check %s for detail!' % options.file_out)
    elif options.flag_acc:
        acc(options.file_input, options.file_out)
        print('[*] done!check %s for detail!' % options.file_out)
    # re-write the argument passing method to support customer property input
    elif options.pesaa and options.lamda and options.omega:
        print('processing...')
        PseAAC(options.file_input, options.file_out, options.lamda, options.omega, 'chrt')
        print('[*] done!check %s for detail!' % options.file_out)
    else:
        print('[-] bad arguments!')
        print('type -h for help')

# # statistic info of one peptide
# def count_aa(line):
#     fx_i = [x * 0.0 for x in range(0, 20)]  # count of each kind of amino acid
#     Vx_i = [x * 0.0 for x in range(0, 20)]  # rate of each kind of amino acid
#     aa_num = 0.0  # count of total amino acids
#     # aa_index = 'ACDEFGHIKLMNPQRSTVWY'
#     # for aa in aa_index
#     for char in line:
#         if char == 'A':
#             fx_i[0] += 1
#         elif char == 'C':
#             fx_i[1] += 1
#         elif char == 'D':
#             fx_i[2] += 1
#         elif char == 'E':
#             fx_i[3] += 1
#         elif char == 'F':
#             fx_i[4] += 1
#         elif char == 'G':
#             fx_i[5] += 1
#         elif char == 'H':
#             fx_i[6] += 1
#         elif char == 'I':
#             fx_i[7] += 1
#         elif char == 'K':
#             fx_i[8] += 1
#         elif char == 'L':
#             fx_i[9] += 1
#         elif char == 'M':
#             fx_i[10] += 1
#         elif char == 'N':
#             fx_i[11] += 1
#         elif char == 'P':
#             fx_i[12] += 1
#         elif char == 'Q':
#             fx_i[13] += 1
#         elif char == 'R':
#             fx_i[14] += 1
#         elif char == 'S':
#             fx_i[15] += 1
#         elif char == 'T':
#             fx_i[16] += 1
#         elif char == 'V':
#             fx_i[17] += 1
#         elif char == 'W':
#             fx_i[18] += 1
#         elif char == 'Y':
#             fx_i[19] += 1
#         else:
#             pass
#     for i in range(0, 20):
#         aa_num += fx_i[i]
#     for i in range(0, 20):
#         Vx_i[i] = fx_i[i] / aa_num
#     return fx_i, Vx_i, int(aa_num)

