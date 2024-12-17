import io
import sys
import src.constants as c


class File:
    def __init__(self, file: io.TextIOWrapper):
        self.f = file

    def get_length(self) -> int:
        word_ctr = 0

        for l in self.f:
            for w in l.split():
                if w != "\n" and w != "":
                    word_ctr += 1

        return word_ctr


def main():
    if len(sys.argv) < 2:
        print("Usage: Include a file." + "python3 main.py <file-name>")
        sys.exit(c.ARGS_FILE_NOT_SUPPLIED)

    f = open("./frankenstein.txt")
    file = File(f)
    print(file.get_length())
    f.close()


if __name__ == "__main__":
    main()
