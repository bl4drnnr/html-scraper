from termcolor import colored


def set_pagination(url):
    is_pagination = input('Is there any pagination in case if you want to get data from a couple of pages, not only one? [Y/N]: ')
    provided_pagination = ''
    quantity_of_pages = 0

    if is_pagination == 'Y' or is_pagination == 'y':
        quantity_of_pages = input('\nWell, what about quantity of pages?: ')

        try:
            int(quantity_of_pages)
        except (Exception,):
            print(colored('Nah... Doesn\'t seem to be number...', 'red', attrs=['reverse']))

        pagination_already_provided = input('Were pagination already provided in URL params or as route? [Y/N]: ')

        if pagination_already_provided == 'Y' or pagination_already_provided == 'y':
            url_param_or_route = input('Is it URL param (example: https://example.com?page=4) or part or route (example: https://example.com/4/)? (1/2): ')
            if url_param_or_route == '1':
                provided_pagination = input('Provide pagination\'s key and value in the same way (and same value) as you did it providing it as param, for example - page=4: ')
                if provided_pagination not in url:
                    print(colored('\nWell... Probably you provided something wrong...', 'red', attrs=['reverse']))
                    exit()
            elif url_param_or_route == '2':
                provided_pagination = input('Set the place of this pagination (example for https://example.com/4/, you would provide /4/): ')
                if len(provided_pagination) != 3 or provided_pagination[0] != '/' or provided_pagination[-1] != '/' or provided_pagination[1] not in '0123456789':
                    print(colored('\nWrong format! Please, try again!', 'red', attrs=['reverse']))
                    exit()
            else:
                print(colored('\nNah... Doesn\'t seem to be right answer...', 'red', attrs=['reverse']))
                exit()
        else:
            print('\nWell, then you should provide it in URL route.')
            print('It could be URL param (example: https://example.com?page=4) or part or route (example: https://example.com/4/)')
            exit()

    return {
        'provided_pagination': provided_pagination,
        'quantity_of_pages': int(quantity_of_pages)
    }