from functools import reduce


def printInventory(entries):
    stringifiedEntries = reduce(lambda acc, val: acc + entry(val) + border(), entries, '')

    print(
        remove_last_line_from_string(
            thickBorder()
            + headerLine()
            + thickBorder()
            + stringifiedEntries
        )
        + thickBorder()
    )
    return ''


def headerLine():
    return '|         Product Name                             |      Available Qty       |\n'


def thickBorder():
    return '+==================================================+==========================+\n'


def border():
    return '+--------------------------------------------------+--------------------------+\n'


def entry(entry):
    template = '|{NAME}|{QTY}|\n'
    template = template.replace('{NAME}', entry.name[:50].center(50, ' '))
    return template.replace('{QTY}', str(entry.quantity)[:50].center(26, ' '))


def remove_last_line_from_string(s):
    return s[:s.rfind(border())]
