import click


@click.group()
def cli():
    pass


@click.command()
@click.option('--add', nargs=2, type=(str, str))
def handle_add(add):
    name, contact = add
    with open('text.txt', 'a+') as f:
        f.write(f'{name} {contact}\n')
    print(f'Name: {name} - Contact: {contact}')


@click.command()
@click.option('--change', nargs=2, type=(str, str))
def handle_change(change):
    name, contact = change
    with open('text.txt', 'w') as f:
        lines = f.readlines()
        for item in lines:
            index_cont = lines.index(item)
            if item.split(' ')[0] == name:
                lines.remove(item)
                lines = lines.insert(index_cont, f'{name} {contact}\n')
        for i in lines:
            f.write(i)


cli.add_command(handle_add)
cli.add_command(handle_change)
if __name__ == '__main__':
    cli()

