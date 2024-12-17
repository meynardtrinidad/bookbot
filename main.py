import io
import sys
import src.constants as c


def is_white_space(ch: str) -> bool:
    if ch == "\n" or ch == "" or ch == " " or ch == "\t":
        return True

    return False


class File:
    def __init__(self, file: io.TextIOWrapper):
        self.f = file

    def get_word_count(self) -> int:
        word_ctr = 0

        for l in self.f:
            for w in l.split():
                if not is_white_space(w):
                    word_ctr += 1

        return word_ctr

    def get_letter_count(self) -> dict[str, int]:
        record = {}

        for l in self.f:
            ln = l.lower()
            for i in range(len(ln)):
                ch = ln[i]
                if is_white_space(ch):
                    continue

                if ch in record:
                    record[ch] += 1
                else:
                    record[ch] = 1

        return record


def main():
    if len(sys.argv) < 2:
        print("Usage: Include a file." + "python3 main.py <file-name>")
        sys.exit(c.ARGS_FILE_NOT_SUPPLIED)

    f = open("./frankenstein.txt")
    file = File(f)
    # print(file.get_word_count())
    print(file.get_letter_count())
    f.close()


if __name__ == "__main__":
    main()
