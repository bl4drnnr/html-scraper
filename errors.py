from termcolor import colored


def print_flags_error():
    print(colored('Wrong flag!', 'red', attrs=['reverse']))
    print(colored('Please, check documentation (-h, --help) in order to check all available flags.', 'red', attrs=['reverse']))
    exit(2)


def only_one_flag_allowed():
    print(colored('Only one flag is allowed!', 'red', attrs=['reverse']))
    print(colored('Please, check documentation (-h, --help) in order to check all available flags.', 'red', attrs=['reverse']))
    exit(2)
