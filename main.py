import click
from datetime import datetime
import datetime


@click.command()
@click.argument('newyear')
@click.option('--hours', is_flag=True)
def main(newyear, hours):
    a = datetime.datetime.today()
    newyear = datetime.datetime(2023, 1, 1)
    c = newyear - a
    minuta, secunda = divmod(c.seconds, 60)
    hour, minuta = divmod(minuta, 60)
    #print(c.days, 'days, ', hh, ' hours')
    if hours:
        click.echo(f"{c.days} days, {hour} hours")
    else:
        click.echo(f"{c.days} days")


if __name__ == '__main__':
    main()    
