class bcolors:
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def color(text, color):
    if (color.lower() == 'blue'):
        return f"{bcolors.OKBLUE}{text}{bcolors.ENDC}"
    elif (color.lower() == 'cyan'):
        return f"{bcolors.OKCYAN}{text}{bcolors.ENDC}"
    elif (color.lower() == 'green'):
        return f"{bcolors.OKGREEN}{text}{bcolors.ENDC}"
    elif (color.lower() == 'red'):
        return f"{bcolors.FAIL}{text}{bcolors.ENDC}"
    elif (color.lower() == 'yellow'):
        return f"{bcolors.WARNING}{text}{bcolors.ENDC}"
    else:
        return text