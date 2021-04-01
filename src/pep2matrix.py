import re
import pep_statistic
import random
import copy


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


class Peptide:
    def __init__(self, peptide_seq, dimension_tuple=None):
        self.sequence = peptide_seq
        self.matrix = []
        self.dimension_tuple = dimension_tuple
        self.do_transfer()

    # convert an amino acid character to vector according to matrix_type
    @staticmethod
    def convert(char, matrix_type):
        assert 65 <= ord(char) <= 90 or char== '*', 'unrecognized amino acid!'
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
        elif char == '*':
            rtn_str = property_dic[matrix_type]['E']
        else:
            print('[-]wrong character in peptide sequence!')
            rtn_str = 'None'
        return rtn_str

    # ************ bottom implementation *************
    def pep2matrix(self):
        def transpose(matrix):
            new_matrix = []
            for i in range(len(matrix[0])):
                matrix1 = []
                for j in range(len(matrix)):
                    matrix1.append(matrix[j][i])
                new_matrix.append(matrix1)
            return new_matrix

        for aa in self.sequence:
            try:
                tmp_vector = [self.convert(aa, 'index')]
                tmp = self.convert(aa, 'property')
                tmp_vector.extend(tmp.split('\t'))
                tmp = self.convert(aa, 'property_chou')
                tmp_vector.extend(tmp.split('\t'))
                self.matrix.append(tmp_vector)
            except AssertionError:
                print(self.sequence)
        self.matrix = transpose(self.matrix)
    # ************ bottom implementation *************

    def matrix_extend(self, dimensionX, dimensionY):
        X_matrix = len(self.matrix[0])
        Y_matrix = len(self.matrix)
        assert X_matrix <= dimensionX, 'target dimension X too small'
        assert Y_matrix <= dimensionY, 'target dimension Y too small'
        for row in self.matrix:
            for i in range(0, dimensionX - X_matrix):
                row.append('0')
        tmp_vec = ['0' for i in range(0, dimensionX)]
        for i in range(0, dimensionY - Y_matrix):
            self.matrix.append(tmp_vec)

    def do_transfer(self):
        self.pep2matrix()
        if self.dimension_tuple:
            self.matrix_extend(self.dimension_tuple[0], self.dimension_tuple[1])
        return self.matrix

    def matrix_output_to_file(self, file_path):
        with open(file_path, 'a') as fp_out:
            for row in self.matrix:
                for col in row:
                    fp_out.write(col + '\t')
                fp_out.write('\n')
            fp_out.write('\n')

    def print_matrix(self):
        for line in self.matrix:
            print(line)

    def print_sequence(self):
        print(self.sequence)


class PeptideDataset:
    def __init__(self, file_path, sequence_list=None, dimension_tuple=None, threshold_tuple=None):
        if sequence_list:
            self.sequence_total = sequence_list
        else:
            self.fp_in = open(file_path, 'r')
            self.sequence_total = [line.strip('\n') for line in self.fp_in]
            self.fp_in.close()
        self.remove_dirt()
        self.matrix_total = []
        self.matrix_num = 0
        self.seq_num = len(self.sequence_total)
        self.fix_dimension_tuple = dimension_tuple
        self.threshold = threshold_tuple
        self.split_dataset = {}
        self.statistic_info = pep_statistic.pep_statistics(self.sequence_total)
        self.training_dataset = None
        self.validation_dataset = None

    def remove_dirt(self):
        self.sequence_total = list(set(self.sequence_total))
        strange = []
        legal_seq = []
        for seq in self.sequence_total:
            if re.match('^[GAVLIFPSTHWCDEKYMNQR\*]+$', seq):
                legal_seq.append(seq.replace('*', 'E'))
            else:
                strange.append(seq)
        if strange:
            print('[+] sequence legal check: following %d lines are removed' % len(strange))
            for line in strange:
                print('\t' + line)
        self.sequence_total = legal_seq
        self.seq_num = len(self.sequence_total)

    def apply_threshold(self):
        if not self.threshold:
            print('[-] threshold not set')
            exit()
        _seq_list = []
        stripped_seq_list = []
        for _pep in self.sequence_total:
            if self.threshold[0] <= len(_pep) <= self.threshold[1]:
                _seq_list.append(_pep)
            else:
                stripped_seq_list.append(_pep)
        self.sequence_total = _seq_list
        self.seq_num = len(self.sequence_total)
        self.statistic_info = pep_statistic.pep_statistics(self.sequence_total)
        print('[+] apply peptide sequence length threshold: %d peptides removed, %d peptides left in dataset' % (len(stripped_seq_list), self.seq_num))
        return stripped_seq_list

    def sequence2matrix(self):
        if not len(self.matrix_total):
            for sequence in self.sequence_total:
                _pep = Peptide(sequence, self.fix_dimension_tuple)
                self.matrix_total.append(_pep.matrix)
            self.matrix_num = len(self.matrix_total)
        return self.matrix_total

    def pep_len_distribution(self, fig_store_path):
        pep_statistic.plot_pep_len_distribution(self.statistic_info, fig_store_path)
        print('[+] generate peptide length distribution figure')

    def aa_abundance_overview(self, fig_store_path):
        pep_statistic.plot_aa_abundance_overview(self.statistic_info, fig_store_path)
        print('[+] generate amino acid abundance global distribution figure')

    def matrix_output_file(self, output_file_path):
        if not len(self.matrix_total):
            self.sequence2matrix()
        with open(output_file_path, 'w') as fp:
            for matrix in self.matrix_total:
                for row in matrix:
                    for col in row:
                        fp.write(col + '\t')
                    fp.write('\n')
                fp.write('\n')
        print('[+] write %d matrices to file done' % len(self.matrix_total))

    def sequence_output_file(self, output_file_path):
        with open(output_file_path, 'w') as fp:
            for line in self.sequence_total:
                fp.write(line + '\n')
        print('[+] write %d peptide sequences to file done' % len(self.sequence_total))

    def print_sequence(self):
        for seq in self.sequence_total:
            print(seq)

    def print_matrix_num(self):
        if not len(self.matrix_total):
            self.sequence2matrix()
        self.matrix_num = len(self.matrix_total)
        print('[+] %d matrices in dataset' % self.matrix_num)

    def print_seq_num(self):
        self.seq_num = len(self.sequence_total)
        print('[+] %d peptides sequence in dataset' % self.seq_num)

    # split a dataset to training set and validation set
    # file_path_tuple = (training_seq_file, training_matrix_file, validation_seq_file, validation_matrix_file)
    def splitting_dataset(self, rate):
        validation_set_num = int(self.seq_num * rate)
        validation_set = []
        full_set = copy.deepcopy(self.sequence_total)
        while len(validation_set) < validation_set_num:
            validation_set.append(full_set.pop())
        training_set = full_set
        training_dataset = PeptideDataset(None, sequence_list=training_set, dimension_tuple=self.fix_dimension_tuple)
        print('[+] dataset splitting: %d peptides in training dataset' % training_dataset.seq_num)
        validation_dataset = PeptideDataset(None, sequence_list=validation_set, dimension_tuple=self.fix_dimension_tuple)
        print('[+] dataset splitting: %d peptides in validation dataset' % validation_dataset.seq_num)
        self.split_dataset = {'training_dataset': training_dataset, 'validation_dataset': validation_dataset}
        self.training_dataset = training_dataset
        self.validation_dataset = validation_dataset
        return self.split_dataset


class RandomPepDataset(PeptideDataset):
    # generate a random peptide dataset according to template(a PeptideDataset object)
    def __init__(self, template, num_rate=1):
        super(RandomPepDataset, self).__init__(None, sequence_list=template.sequence_total,
                                               dimension_tuple=template.fix_dimension_tuple, threshold_tuple=template.threshold)
        if not self.threshold:
            print('[-] to generate random peptides, threshold must be set on template dataset')
            exit()
        self.sequence_total = []
        self.seq_num = int(self.seq_num * num_rate)
        self.generate_random_peptides()
        self.statistic_info = pep_statistic.pep_statistics(self.sequence_total)

    def generate_random_peptides(self):
        aa_candidate = 'GAVLIFPSTHWCDEKYMNQR'
        pep_len_distribution = []
        for i in range(self.seq_num):
            gauss_num = 0
            while gauss_num < self.threshold[0] or gauss_num > self.threshold[1]:
                gauss_num = int(random.gauss(self.statistic_info['pep_len_average'], self.statistic_info['pep_len_deviation']))
            pep_len_distribution.append(gauss_num)
        for _len in pep_len_distribution:
            pep_seq = ''
            for i in range(0, _len):
                pep_seq += aa_candidate[random.randint(0, 19)]
            assert pep_seq != ''
            self.sequence_total.append(pep_seq)


if __name__ == '__main__':
    def wrapper(base_dir, file_name, dimension=None, threshold=None):
        if not dimension or not threshold:
            ds = PeptideDataset(base_dir + file_name)
            ds.print_seq_num()
            ds.pep_len_distribution(base_dir + file_name + '_len_distr.html')
            ds.aa_abundance_overview(base_dir + file_name + '_aa_distr.html')
            return
        ds = PeptideDataset(base_dir +file_name, dimension_tuple=dimension, threshold_tuple=threshold)
        ds.apply_threshold()
        ds.pep_len_distribution(base_dir + file_name + '_len_distr_pos.html')
        ds.aa_abundance_overview(base_dir + file_name + '_aa_distr_pos.html')
        ds.splitting_dataset(0.3)
        ds.training_dataset.matrix_output_file(base_dir + file_name + '_matrix_training_pos')
        ds.validation_dataset.matrix_output_file(base_dir + file_name + '_matrix_validation_pos')

        rnd_ds = RandomPepDataset(ds)
        rnd_ds.pep_len_distribution(base_dir + file_name + '_len_distr_neg.html')
        rnd_ds.aa_abundance_overview(base_dir + file_name + '_aa_distr_neg.html')
        rnd_ds.splitting_dataset(0.3)
        rnd_ds.training_dataset.matrix_output_file(base_dir + file_name + '_matrix_training_neg')
        rnd_ds.validation_dataset.matrix_output_file(base_dir +file_name + '_matrix_validation_neg')

    # wrapper('/home/han/文档/毕设/datasets/antimicrobial/', 'antimicrobial')
    wrapper('/home/han/文档/毕设/datasets/antimicrobial/', 'antimicrobial', dimension=(60, 13), threshold=(5, 60))

