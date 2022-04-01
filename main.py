import click
from datetime import datetime
import datetime
import enum
import random
from pathlib import Path
import os


class Color(enum.Enum):
    Red = '#f00'
    Green = '#0f0'
    Blue = '#00f'
    Cyan = '#0ff'
    Magenta = '#f0f'
    Yellow = '#ff0'


@click.group()
def main():
    pass


@main.command()
def toy():
    click.echo(random.choice([Color.Red.name, Color.Green.name, Color.Blue.name, 
    Color.Cyan.name, Color.Magenta.name, Color.Yellow.name])
     +' ' + random.choice(['doll', 'car', 'ball', 'angel', 'bear', 'cubes']))


@main.command()
@click.option('--hours', is_flag=True)
def newyear(hours, type=str, help='the parameter of the number of hours until the new year'):
    a = datetime.datetime.today()
    newyear = datetime.datetime(2023, 1, 1)
    c = newyear - a
    minuta, secunda = divmod(c.seconds, 60)
    hour, minuta = divmod(minuta, 60)
    if hours:
        click.echo(f"{c.days} days, {hour} hours")
    else:
        click.echo(f"{c.days} days")


paths = (os.path.join(root, filename)
        for root, dirs, filenames in os.walk('D:\HOMEWORK9\directory')
        for filename in filenames)

@main.command()
def restructuredirectory():
    paths = (os.path.join(root, filename)
        for root, dirs, filenames in os.walk('D:\HOMEWORK9\directory')
        for filename in filenames)


    for path in paths:
        newname = path.replace('-', '\\')
        if newname != path:
            os.renames(path, newname)

main.add_command(toy)
main.add_command(newyear)
main.add_command(restructuredirectory)

print(toy.__annotations__)
print(newyear.__annotations__)


if __name__ == '__main__':
    main()   
