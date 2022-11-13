#!/usr/bin/python3


def chunkContainsKeys(chunk: str, required_keys: set) -> bool:
    keys = {elem.split(":")[0] for elem in chunk.split()}
    return required_keys.issubset(keys)


def getUsername(user_dump: str) -> str:
    for elem in user_dump.split():
        key, val = elem.split(':')
        if key == "usr":
            return val
    return None


def printResults(results: (int, str)) -> None:
    incorrect_solution = not results[0] or not results[1]

    if incorrect_solution:
        print("Error processiong file: Invalid Format?")
    else:
        print("Solution:")
        print(f"\tsubmit {results[0]}{results[1]}")


def finishedUserDataChunk(line: str, i: int, nlines: int) -> bool:
    is_last_line = i == nlines - 1
    empty_line = line == "\n"
    return is_last_line or empty_line


def readFileContent(path: str) -> str:
    f = open("users.txt", "r")
    lines = f.readlines()
    f.close()
    return lines


def getUserDataChunks(file_content: str) -> list:
    current_user_chunk = ""
    nlines = len(file_content)
    chunks = []
    for i, line in enumerate(file_content):
        if finishedUserDataChunk(line, i, nlines):
            chunks.append(current_user_chunk)
            current_user_chunk = ""
        else:
            current_user_chunk += line

    return chunks


def computeSolution(file_content: str) -> (int, str):
    required_keys = {"usr", "eme", "psw", "age", "loc", "fll"}
    nvalid_users = 0
    last_valid_username = ""

    user_data_chunks = getUserDataChunks(file_content)

    for user_data_chunk in user_data_chunks:
        if chunkContainsKeys(user_data_chunk, required_keys):
            nvalid_users += 1
            last_valid_username = getUsername(user_data_chunk)

    return (nvalid_users, last_valid_username)


def main():
    content = readFileContent("users.txt")
    results = computeSolution(content)
    printResults(results)


if __name__ == '__main__':
    main()
