from inspect import currentframe, getframeinfo
from pathlib import Path
import argparse
import toml

this_file = getframeinfo(currentframe()).filename
here = Path(this_file).resolve().parent


def load_toml() -> toml: 
    config = None
    try: 
        config = toml.load(here/'cfg.toml')
    except FileNotFoundError:
        config = toml.load(here/'cfg.example.toml')
    return config
    

def get_extract_data():
    configure_file = load_toml()
    data_file = configure_file['data']['school_csv']
    print(data_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Model complexity of teacher workloads")
    parser.add_argument(
        '-e',
        '--extract',
        action="store_true",
        help="CSV file to extract teacher | unit | student data",
    )
    
    args = parser.parse_args(['-e'])

    if args.extract:
        get_extract_data()
    else: 
        print(args)

    # print(parser.parse_args(['-h']))
    