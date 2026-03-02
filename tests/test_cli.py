"""Tests for hello_scully CLI."""

from hello_scully.cli import GREETINGS, get_greeting, main, parse_args


def test_default_name():
    args = parse_args([])
    assert args.name == "Scully"


def test_custom_name():
    args = parse_args(["--name", "Mulder"])
    assert args.name == "Mulder"


def test_greeting_contains_name():
    assert "Scully" in get_greeting("Scully")


def test_greeting_custom_name():
    assert "Mulder" in get_greeting("Mulder")


def test_greeting_is_from_list():
    name = "Scully"
    greeting = get_greeting(name)
    expected = [t.format(name=name) for t in GREETINGS]
    assert greeting in expected


def test_main_prints_output(capsys):
    main([])
    captured = capsys.readouterr()
    assert "Scully" in captured.out


def test_main_custom_name(capsys):
    main(["--name", "Dana"])
    captured = capsys.readouterr()
    assert "Dana" in captured.out
