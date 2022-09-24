def set_option_type(option_type):
    return {
        'headers': {
            'set': 'Wanna set headers? (for example, if access to page is restricted by authentication) [Y/N]: ',
            'quantity': '\nWhat about quantity of headers? (Integer number only): ',
            'format': 'Provide header in next format - key=value'
        },
        'cookies': {
            'set': 'Wanna send with some cookie? (for example, if access to page is restricted by authentication) [Y/N]: ',
            'quantity': '\nWhat about quantity of cookies? (Integer number only): ',
            'format': 'Provide cookie in next format - key=value'
        },
        'params': {
            'set': 'Are there any URL params you want to provide (if you haven\'t done it in URL yet) [Y/N]: ',
            'quantity': '\nWhat about quantity of params? (Integer number only): ',
            'format': 'Now, provide URL params in the next format - key=value.'
        }
    }[option_type]
