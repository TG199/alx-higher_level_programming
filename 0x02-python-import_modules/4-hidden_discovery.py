#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hidden

    for name in dir(hidden):
        if name[0] != '_' and name[1] != '_':
            print(name)
