import click
from datetime import datetime
import datetime
import enum
import random


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
def newyear(hours):
    a = datetime.datetime.today()
    newyear = datetime.datetime(2023, 1, 1)
    c = newyear - a
    minuta, secunda = divmod(c.seconds, 60)
    hour, minuta = divmod(minuta, 60)
    if hours:
        click.echo(f"{c.days} days, {hour} hours")
    else:
        click.echo(f"{c.days} days")


main.add_command(toy)
main.add_command(newyear)


if __name__ == '__main__':
    main()    
