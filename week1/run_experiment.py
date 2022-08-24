# training process file

import argparse
import importlib
import pandas as pd

# from torch.utils.data import ConcatDataset, DataLoader
# from models.cnn import CNN
# from models.mlp import MLP
# from models.lstm import LSTM

from models import CNN, MLP, LSTM

def import_class(str_name):
    module_name, class_name = str_name.rsplit('.',1) 
    module = importlib.import_module(module_name)
    class_ = getattr(module, class_name)
    return class_

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_class", type=str, default="CNN")
    temp_args, _ = parser.parse_known_args()
    model_class = import_class(f"models.{temp_args.model_class}")
    print(model_class)
    model_group = parser.add_argument_group("Model Args")
    model_class.add_to_argparse(model_group)

if __name__ == '__main__':
    main()