import io
import sys
import src.constants as c


# FIXME: Get file statistics by going through the whole file once.
class File:
    def __init__(self, file: io.TextIOWrapper):
        self.f = file

    def get_word_count(self) -> int:
        word_ctr = 0

        self.f.seek(0)
        for l in self.f:
            for w in l.split():
                if w.isalpha():
                    word_ctr += 1

        return word_ctr

    def get_char_count(self) -> list[dict[str, str | int]]:
        char_count = {}

        self.f.seek(0)
        for l in self.f:
            ln = l.lower()
            ln.isspace
            for i in range(len(ln)):
                ch = ln[i]
                if not ch.isalpha():
                    continue

                if ch in char_count:
                    char_count[ch] += 1
                else:
                    char_count[ch] = 1

        record = []
        for k, v in char_count.items():
            record.append({"char": k, "occurence": v})

        record.sort(reverse=True, key=lambda x: x["occurence"])
        return record


def main():
    if len(sys.argv) < 2:
        print("Usage: Include a file." + "python3 main.py <file-name>")
        sys.exit(c.ARGS_FILE_NOT_SUPPLIED)

    fn = sys.argv[1]
    f = open(fn)
    file = File(f)
    char_count = file.get_char_count()
    word_count = file.get_word_count()
    f.close()

    print(f"--- Begin report of {fn} ---")
    print(f"{word_count} words found in the document.\n")

    for ch in char_count:
        print(f"The '{ch.get("char")}' character was found {ch.get("occurence")} times")
    print(f"--- End report ---")


if __name__ == "__main__":
    main()
