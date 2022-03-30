import click
import enum
import random

class Color(enum.Enum):
    Red = '#f00'
    Green = '#0f0'
    Blue = '#00f'
    Cyan = '#0ff'
    Magenta = '#f0f'
    Yellow = '#ff0'

@click.command()
@click.argument('toy')
def main(toy):
    click.echo(random.choice([Color.Red.name, Color.Green.name, Color.Blue.name, 
    Color.Cyan.name, Color.Magenta.name, Color.Yellow.name])
     +' ' + random.choice(['doll', 'car', 'ball', 'angel', 'bear', 'cubes']))
    
            
if __name__ == '__main__':
    main() 
