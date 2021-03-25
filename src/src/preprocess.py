import re
import copy
from pyecharts import options as opts
from pyecharts.charts import Pie, Bar
import os
import pickle
import seaborn


def pep_read_from_file(file_in):
    pep_list = []
    with open(file_in, 'r') as fp_in:
        for line in fp_in:
            pep_list.append(line.replace('\n', ''))
    return pep_list


def pep_write_to_file(pep_list, file_out):
    with open(file_out, 'w') as fp_out:
        for pep in pep_list:
            fp_out.write(pep)
            fp_out.write('\n')


def remove_dirt(pep_list):
    pep_list = list(set(pep_list))
    strange = []
    for pep in pep_list:
        match = re.search('^[GAVLIFPSTHWCDEKYMNQR]+$', pep)
        if not match:
            pep_list.remove(pep)
            strange.append(pep)
    if strange:
        print('following peptides are removed')
        for pep in strange:
            print(pep)
    return pep_list


def set_threshold(pep_list, lower_limit, upper_limit):
    rtn_list = []
    for pep in pep_list:
        if lower_limit <= len(pep) <= upper_limit:
            rtn_list.append(pep)
    return rtn_list


def pep_static(pep_list, info_store):
    if os.path.exists(info_store):
        with open(info_store, 'rb') as fp:
            return pickle.load(fp)

    info_dict = {'total_pep_num': len(pep_list), 'aa_abundance_position': [], 'pep_len_distribution': {}}
    aa_abundance_init = {'G': 0, 'A': 0, 'V': 0, 'L': 0, 'I': 0, 'F': 0, 'P': 0, 'S': 0, 'T': 0, 'H': 0, 'W': 0, 'C': 0,
                         'D': 0, 'E': 0, 'K': 0, 'Y': 0, 'M': 0, 'N': 0, 'Q': 0, 'R': 0}
    aa_count = 0
    info_dict['aa_abundance_overview'] = copy.deepcopy(aa_abundance_init)
    pep_longest = 0
    pep_shortest = 100
    for pep in pep_list:
        pep_len = len(pep)
        if pep_len in info_dict['pep_len_distribution'].keys():
            info_dict['pep_len_distribution'][pep_len] += 1
        else:
            info_dict['pep_len_distribution'][pep_len] = 1
        for i in range(0, pep_len):
            info_dict['aa_abundance_overview'][pep[i]] += 1
            if i+1 > len(info_dict['aa_abundance_position']):
                info_dict['aa_abundance_position'].append(copy.deepcopy(aa_abundance_init))
            info_dict['aa_abundance_position'][i][pep[i]] += 1
        aa_count += len(pep)
        if pep_len > pep_longest:
            pep_longest = pep_len
        if pep_len < pep_shortest:
            pep_shortest = pep_len
    info_dict['aa_count'] = aa_count
    info_dict['pep_len_average'] = aa_count / info_dict['total_pep_num']
    info_dict['pep_shortest'] = pep_shortest
    info_dict['pep_longest'] = pep_longest
    with open(info_store, 'wb') as fp:
        pickle.dump(info_dict, fp)
    return info_dict


def plot_aa_abundance_overview(abundance_overview, fig_store_path):
    overview = dict(sorted(abundance_overview.items(), key=lambda item: item[1]))
    c = (
        Pie()
        .add(
            "",
            [list(z) for z in zip(overview.keys(), overview.values())]
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title='amino acid abundance overview'),
            legend_opts=opts.LegendOpts(is_show=False)
        )
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))
        .render(fig_store_path)
    )


def plot_pep_len_distribution(len_distribution, fig_store_path):
    distribution = []
    for i in range(min(len_distribution.keys()), max(len_distribution.keys())):
        if i in len_distribution.keys():
            distribution.append(len_distribution[i])
        else:
            distribution.append(0)
    c = (
        Bar()
        .add_xaxis([x for x in range(min(len_distribution.keys()), max(len_distribution.keys()))])
        .add_yaxis("Num", distribution)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="peptide length distribution"),
            yaxis_opts=opts.AxisOpts(name="Count"),
            xaxis_opts=opts.AxisOpts(name="peptide length"),
            legend_opts=opts.LegendOpts(is_show=False)
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .render(fig_store_path)
    )


if __name__ == '__main__':
    antimicrobial_base_path = '/home/han/文档/毕设/datasets/antimicrobial/'
    antimicro_pep_list = pep_read_from_file(antimicrobial_base_path + 'antimicrobial_2455')
    antimicro_pep_list = remove_dirt(antimicro_pep_list)
    # antimicro_static = pep_static(antimicro_pep_list, antimicrobial_base_path + 'antimicrobial_2455_static')
    # plot_aa_abundance_overview(antimicro_static['aa_abundance_overview'], antimicrobial_base_path + 'antimicrobial_2455_aa_abundance_overview.html')
    # plot_pep_len_distribution(antimicro_static['pep_len_distribution'], antimicrobial_base_path + 'antimicrobial_2455_pep_len_distribution.html')

    antimicro_pep_list = set_threshold(antimicro_pep_list, 5, 50)
    print(len(antimicro_pep_list))
    antimicro_static = pep_static(antimicro_pep_list, antimicrobial_base_path + 'antimicrobial_2182_static')
    plot_aa_abundance_overview(antimicro_static['aa_abundance_overview'], antimicrobial_base_path + 'antimicrobial_2182_aa_abundance_overview.html')
    plot_pep_len_distribution(antimicro_static['pep_len_distribution'], antimicrobial_base_path + 'antimicrobial_2182_pep_len_distribution.html')
    print(antimicro_static)
