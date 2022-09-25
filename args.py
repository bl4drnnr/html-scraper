import getopt
import sys
import prints
import errors


def get_input_args():
    flags = sys.argv[1:]
    short_flags = 'ho:u:'
    long_flags = ['help', 'output=', 'url=']

    try:
        opts, args = getopt.getopt(flags, short_flags, long_flags)

        output = ''
        start_url = ''
        for o, a in opts:
            if o in ('-h', '--help'):
                prints.print_help()
            elif o in ('-o', '--output'):
                output = a
            elif o in ('-u', '--url'):
                start_url = a
            else:
                errors.print_flags_error()

        return {
            'start_url': start_url,
            'output': output
        }
    except getopt.GetoptError:
        errors.print_flags_error()
