
BATCH_SIZE = 10
NUM_WORKERS = 3

    
    
class BaseDataModule():
    def __init__(self, args) -> None:
        self.batch_size = args.get("batch_size",BATCH_SIZE)
        self.num_workers = args.get("num_workers",NUM_WORKERS)

    @staticmethod
    def add_to_argparse(parser):
        parser.add_argument("--batch_size", type=int, default=BATCH_SIZE,
        help="Number of Images to operate on per forward step")
        parser.add_argument("--num_workers", type=int, default=NUM_WORKERS,
        help="Number of processes to load data")
