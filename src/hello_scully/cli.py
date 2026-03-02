"""CLI entry point for hello-scully."""

import argparse
import random

GREETINGS = [
    "Hello {name}! 👽 The truth is out there... but first, coffee.",
    "Hey {name}! 🔬 Science doesn't sleep, and neither do I.",
    "Hello {name}! 🛸 I'm not saying it's aliens... but it's definitely not aliens.",
    "Greetings, {name}! 🔦 Trust no one — except this CLI.",
    "Hello {name}! 🧬 Another day, another unexplained phenomenon.",
]


def get_greeting(name: str) -> str:
    """Return a random Scully-flavored greeting."""
    return random.choice(GREETINGS).format(name=name)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Greet Agent Scully (or anyone).")
    parser.add_argument(
        "--name",
        default="Scully",
        help="Who to greet (default: Scully)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> None:
    """Main entry point."""
    args = parse_args(argv)
    print(get_greeting(args.name))


if __name__ == "__main__":
    main()
