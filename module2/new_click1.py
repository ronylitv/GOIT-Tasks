import click


@click.command()
@click.argument('name')
@click.argument('contact')
def write_to_file(name, contact):
    while True:
        with open('text.txt', 'a') as f:
            f.write(f'{name} {contact}\n')
        b = input('Do u want to continue? (y/n)')
        if b == 'n':
            break


if __name__ == '__main__':
    write_to_file()
