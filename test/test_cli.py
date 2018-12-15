from click.testing import CliRunner
from quickstats.cli import memory


def test_memory():
    # Test that the command can be called without error
    runner = CliRunner()
    command_result = runner.invoke(memory)
    assert command_result.exit_code == 0
