import sys

import click
import click_completion
import crayons
from click_didyoumean import DYMCommandCollection

from prevenger.kit.captcha_kit import create_wheezy_captcha
from prevenger.kit.rand_kit import rand_letters_digits

click_completion.init()

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


class PrevengerGroup(click.Group):
    def get_help_option(self, ctx):
        help_options = self.get_help_option_names(ctx)

        def show_help(ctx, param, value):
            click.echo(ctx.get_help(), color=ctx.color)

        return click.Option(
            help_options,
            is_flag=True,
            is_eager=True,
            expose_value=False,
            callback=show_help,
            help="Show this message and exit.",
        )


def setup_verbose(ctx, param, value):
    if value:
        import logging

        logging.getLogger("requests").setLevel(logging.INFO)
    return value


@click.group(
    cls=PrevengerGroup, invoke_without_command=True, context_settings=CONTEXT_SETTINGS
)
@click.option("-v", "--verbose", is_flag=True, help="Enables verbose mode.")
@click.version_option(prog_name=crayons.white("prevenger", bold=True))
@click.pass_context
def cli(ctx, verbose):
    """
    The Must-Have Utils For Every Pythonista 2018 - 2019.
    """
    ctx.verbose = verbose


@click.command(
    short_help="execute python and then enter ipython",
    context_settings=dict(ignore_unknown_options=True, allow_extra_args=True),
)
def run():
    click.echo("is executing")
    pass


@click.command(
    short_help="self testing",
    context_settings=dict(ignore_unknown_options=True, allow_extra_args=True),
)
def self_test():
    click.echo("is self test")
    """使用REQUESTS请求某个地址,跳转到IPython便于下一步解析."""
    all_colors = "black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"
    for color in all_colors:
        click.echo(click.style("I am colored %s" % color, fg=color))
    for color in all_colors:
        click.echo(click.style("I am colored %s and bold" % color, fg=color, bold=True))
    for color in all_colors:
        click.echo(
            click.style("I am reverse colored %s" % color, fg=color, reverse=True)
        )

    click.echo(click.style("I am blinking", blink=True))
    click.echo(click.style("I am underlined", underline=True))
    args_str = ["-s"]
    import pytest

    pytest.cmdline.main(args_str)


@click.command(
    short_help="create wheezy captcha",
)
@click.option("--f", default=".", help="make captcha.")
def captcha(f="."):
    chars = rand_letters_digits(5)
    create_wheezy_captcha(chars).save(f"{f}/captcha.png")


@click.command()
def touch(f):
    click.echo(click.format_filename(f))


# Install click commands.
cli.add_command(self_test)
cli.add_command(captcha)

if "-" not in "".join(sys.argv) and len(sys.argv) > 1:
    cli = DYMCommandCollection(sources=[cli])


def main():
    cli()


if __name__ == "__main__":
    main()
