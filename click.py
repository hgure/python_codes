import click
import psutil

@click.command()
@click.option('--task', default='all', help='all, cpu or disk')
def get_stats(task):
  click.echo('getting stats %s' % task)
  if (task == 'cpu' or task == 'all'):
    cpu_stats = psutil.cpu_stats();
    click.echo(cpu_stats)
  if (task == 'disk' or task == 'all'):
    disk_usage = psutil.disk_usage('C:/')
    click.echo(disk_usage)

if __name__ == '__main__':
  get_stats()