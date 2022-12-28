from typer.testing import CliRunner

from hutoolpy.cli import cli_app


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli_app)
    assert result.exit_code == 0
    assert "Python" in result.output
    help_result = runner.invoke(cli_app, ["--help"])
    assert help_result.exit_code == 0
    assert "shell_plus" in help_result.output
