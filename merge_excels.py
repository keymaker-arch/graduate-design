import pandas as pd
import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="merge excel files with identical columns, the files should be stored within one directory")
    parser.add_argument('path_dir', type=str, action='store', help='path to a directory containing excel files to be merged')
    parser.add_argument('-p', type=str, action='store', dest='store_path', help='path to store the merged excel file')
    args = parser.parse_args()

    df_l = []
    for root, dirs, files in os.walk(args.path_dir):
        for file in files:
            df_l.append(pd.read_excel(os.path.join(root, file)))
    df = pd.concat(df_l)
    df.to_excel(os.path.join(os.path.dirname(args.store_path), 'merged.xlsx'), index=False)


