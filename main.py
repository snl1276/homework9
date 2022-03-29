import click
from datetime import datetime
import datetime


@click.command()
@click.argument('newyear')
@click.option('--hours')
def main(newyear, hours):
    a = datetime.datetime.today()
    newyear = datetime.datetime(2023, 1, 1)
    c = newyear - a
    minuta, secunda = divmod(c.seconds, 60)
    hours, minuta = divmod(minuta, 60)
    #print(c.days, 'days, ', hh, ' hours')
    click.echo(f"{c.days} days")
    click.echo(f"{hours} hours")

    


if __name__ == '__main__':
    main()    
