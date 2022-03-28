import click
from datetime import datetime
import datetime


@click.command()
#@click.option('--hous', default=0, help='number of greetings')
#@click.argument('newyear', help='You name')

def main():
    a = datetime.datetime.today()
    b = datetime.datetime(2023, 1, 1)
    c = b - a
    mm, ss = divmod(c.seconds, 60)
    hh, mm = divmod(mm, 60)
    #print(c.days, 'days, ', hh, ' hours')
    click.echo(f"{c.days} days")
    click.echo(f"{hh} hours")
if __name__ == '__main__':
    main()
    