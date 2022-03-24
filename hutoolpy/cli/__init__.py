from hutoolpy.cli.base import cli_app

from .extra import *


@cli_app.command("shell_plus")
def shell_plus():
    from IPython import embed
    import cProfile
    import pdb
    ctx = {}
    ctx.update(
        {
            "ipdb": pdb,
            "cProfile": cProfile,
        }
    )
    embed(user_ns=ctx, banner2="", using="asyncio", colors="neutral")
