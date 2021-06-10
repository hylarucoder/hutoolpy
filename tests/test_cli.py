from click.testing import CliRunner

from hutoolpy.cli import cli


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli)
    assert result.exit_code == 0
    assert "Pythonista" in result.output
    help_result = runner.invoke(cli, ["--help"])
    assert help_result.exit_code == 0
    assert "Pythonista" in help_result.output
