import tarfile


def compress():
    with tarfile.open("massive-raw.tar.gz", "w:gz") as tar:
        tar.add("1.1")


if __name__ == "__main__":
    compress()
