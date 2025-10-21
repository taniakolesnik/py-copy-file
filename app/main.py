import os


def copy_file(command: str) -> None:
    params = command.split()

    if len(params) < 3:
        return

    if params[0] != "cp":
        return

    if not os.path.exists(params[1]):
        return

    if params[1] != params[2]:
        with open(params[1], "r") as file_in, open(params[2], "w") as file_out:
            for line in file_in:
                file_out.write(line)
