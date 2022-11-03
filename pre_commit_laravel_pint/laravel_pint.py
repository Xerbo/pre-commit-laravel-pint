from __future__ import annotations

import subprocess
import argparse
from typing import Sequence


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)

    compose_prefix = ''
    try:
        file = open('.env')
        for line in file:
            keyval = line.strip().split('=')
            if keyval[0] == 'COMPOSE_PROJECT_NAME':
                compose_prefix = keyval[1]
    except FileNotFoundError:
        compose_prefix = ''

    command_prefix = []
    if compose_prefix != '':
        command_prefix = ['docker', 'exec', '{}-laravel-1'.format(compose_prefix)]

    return subprocess.run(command_prefix + ['./vendor/bin/pint', '--test'] + args.filenames).returncode


if __name__ == '__main__':
    raise SystemExit(main())
