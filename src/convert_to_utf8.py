
import pandas as pd

def convert_to_utf8(input_file, output_file):
    try:
        df = pd.read_csv(input_file, encoding='latin1')
    except UnicodeDecodeError:
        df = pd.read_csv(input_file, encoding='ISO-8859-1')

    df.to_csv(output_file, index=False, encoding='utf-8')

if __name__ == "__main__":
    convert_to_utf8('data/responses.csv', 'data/responses_utf8.csv')
