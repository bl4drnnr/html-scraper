def print_input():
    print('****************************************************************************')
    print(' _   _ ________  ___ _          _____ _____ ______  ___  ______ ___________ ')
    print('| | | |_   _|  \/  || |        /  ___/  __ \| ___ \/ _ \ | ___ \  ___| ___ \\')
    print('| |_| | | | | .  . || |  ______\ `--.| /  \/| |_/ / /_\ \| |_/ / |__ | |_/ /')
    print('|  _  | | | | |\/| || | |______|`--. \ |    |    /|  _  ||  __/|  __||    / ')
    print('| | | | | | | |  | || |____    /\__/ / \__/\| |\ \| | | || |   | |___| |\ \ ')
    print('\_| |_/ \_/ \_|  |_/\_____/    \____/ \____/\_| \_\_| |_/\_|   \____/\_| \_|')
    print('****************************************************************************')

    print('Welcome, username, you here to scrap some HTML, right? Well, I knew that, so, let\'s start then!')
    print('Let\'s start with simple configuration of what you exactly want.\n')


def print_format_request():
    print('\nAnd the last thing - is tag to extract. What you should do, is to inspect the page and provide the tag.')
    print('Here is couple of examples how format should look like:')
    print('--------------------------')
    print('Examples:')
    print('div[@title="buyer-name"]')
    print('span[@class="item-price"]')
    print('--------------------------\n')


def print_help():
    print('Documentation.')
    print('-h, --help\tPrint documentation manual.')
    print('-u, --url\tPass URL of page of page to scrap. Example: -u https://example.com or --url=https://example.com')
    print('-s, --start\tStart program in interactive mode.')
    exit()


def print_flags_error():
    print('Wrong flag!')
    print('Please, check documentation (-h, --help) in order to check all available flags.')
    exit()


def only_one_flag_allowed():
    print('Only one flag is allowed!')
    print('Please, check documentation (-h, --help) in order to check all available flags.')
    exit()
