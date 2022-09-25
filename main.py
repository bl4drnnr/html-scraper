import sys

from termcolor import colored

from modules.prints import print_input, print_format_request
from modules.options import set_option
from modules.pagination import set_pagination
from modules.args import get_input_args
from modules.request import request_with_pagination, single_request


def main(start_url='', output=''):
    print_input()

    if len(start_url) == 0:
        url = input('First of all, provide me with url of page to scrap: ')
    else:
        url = start_url

    if url[0:7] != 'http://' and url[0:8] != 'https://':
        print(colored('\nURL must start with http:// or https:// !', 'red', attrs=['reverse']))
        exit()

    print(colored('\nOkay, here we go with options!', 'yellow', attrs=['reverse']))

    updated_url = set_option('params', url)
    cookies = set_option('cookies')
    headers = set_option('headers')
    pages = set_pagination(url)

    print_format_request()

    tag_to_extract = input('So, what about tag to extract?: ')

    print(colored('\nAnd... That\'s it! Here we go!', 'yellow', attrs=['reverse']))

    content = request_with_pagination(updated_url, cookies, headers, tag_to_extract, pages) if len(pages['provided_pagination']) > 0 else single_request(updated_url, cookies, headers, tag_to_extract)

    print(colored('\nOf... Seems like everything went right. Let\'s end up with this.', 'yellow', attrs=['reverse']))

    remove_whitespaces = input('Wanna remove all whitespace signs? [Y/N]: ')
    if remove_whitespaces == 'Y' or remove_whitespaces == 'y':
        updated_content = []
        for item in content:
            updated_content.append(item.strip())
        content = updated_content

    save_to_file = input('Save result to file? [Y/N]: ')
    if save_to_file == 'Y' or save_to_file == 'y':
        try:
            if len(output) != 0:
                file_name = output
            else:
                file_name = input('Please, provide file name: ')

            final_content = ''

            f = open(f'{file_name}.txt', 'w')

            for item in content:
                final_content += f'{item},'

            f.write(final_content)
            f.close()

            print(colored('And... Done!', 'green', attrs=['reverse']))
        except (Exception,):
            print(colored('Oops... Something went wrong! Please, check file name.', 'red', attrs=['reverse']))
    else:
        print('\n---------------------')
        print('Result:', content)
        print('---------------------\n')


if __name__ == '__main__':
    if len(sys.argv[1:]) == 0:
        main()
    else:
        ops = get_input_args()
        main(ops['start_url'], ops['output'])

