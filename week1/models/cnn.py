import argparse
from typing import Any, Dict
# import torch.nn as nn

CONV_DIM = 16
FC_DIM = 18

class CNN(): # nn.Module
    def __init__(self, data_config: Dict[str, Any], args: argparse.Namespace = None) -> None:
        
        # data_config["...."]
        
        pass

    @staticmethod
    def add_to_argparse(parser):
        parser.add_argument("--conv_dim", type=int, default=CONV_DIM)
        parser.add_argument("--fc_dim", type=int, default=FC_DIM)