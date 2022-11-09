#!/usr/bin/python3


def is_valid(user_dump: str) -> bool:
    keys = {elem.split(":")[0] for elem in user_dump.split()}
    return {"usr", "eme", "psw", "age", "loc", "fll"}.issubset(keys)


def main():
    nusers = 0
    nvalid_users = 0
    user_raw_data = ""

    f = open("users.txt", "r")
    for line in f:
        if line == "\n":
            nvalid_users += 1 if is_valid(user_raw_data) else 0
            user_raw_data = ""
            nusers += 1
        else:
            user_raw_data += line
    print(f"Result: {nvalid_users}/{nusers}")
    f.close()


if __name__ == '__main__':
    main()
