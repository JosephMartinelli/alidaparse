from input import InDataset


if __name__ == "__main__":
    dataset = InDataset.from_cli(n=2)
    print(dataset)
