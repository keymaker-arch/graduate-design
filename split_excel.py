import pandas as pd
import argparse
import os
import re


def split_excel(excel_path, sheet_name, column_name):
    df = pd.read_excel(excel_path, sheet_name=sheet_name)
    array = df.loc[:, [column_name]].values.tolist()
    column_split_by = []
    for name in array:
        for i in name:
            if i not in column_split_by:
                column_split_by.append(i)
    df_dic = {}
    for name in column_split_by:
        df_dic[name] = df.loc[df[column_name] == name]
    return df_dic


def write_excel(df_dic, out_base_path):
    for key, value in df_dic.items():
        out_path = out_base_path + key + '.xlsx'
        value.to_excel(out_path, index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="split excel file according to column value, and store separately")
    parser.add_argument("file_path", type=str, action='store', help="file path to excel file")
    parser.add_argument('-c', type=str, action='store', required=True, dest='col_name', help='column name that the file split by')
    parser.add_argument('-s', type=str, action='append', dest='sheet_name', required=True, help='sheet(s) in excel file to split, separate by comma')
    parser.add_argument('-p', type=str, action='store', dest='store_path', required=False, help='specify store path of split files')
    # args = parser.parse_args()
    args = parser.parse_args('-h'.split())
    if '/' in args.file_path or '\\' in args.file_path:
        excel_file_path = args.file_path
    else:
        excel_file_path = os.path.dirname(os.getcwd()) + args.file_path

    if args.store_path:
        store_file_path = args.store_path
    else:
        store_file_path = os.path.dirname(args.file_path) + '/' + os.path.basename(args.file_path)

    for sheet in args.sheet_name:
        tmp_dic = split_excel(args.file_path, sheet, args.col_name)
        write_excel(tmp_dic, store_file_path + '_' + sheet + '_')