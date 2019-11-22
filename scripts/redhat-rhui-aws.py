import argparse
import ConfigParser, os
import sys


def read_config(filename):
    config = ConfigParser.ConfigParser()
    with open(filename, "r") as _:
        config.readfp(_)
    return config


def write_config(config, filename):
    with open(filename, "w") as _:
        config.write(_)


def get_repos(filename):
    """Read the repositories in an ini file.
    
    Args:
        filename (str): Absolute path to the file that contains the repositories.
    """
    config = read_config(filename)
    repos = "\n".join([repo for repo in config.sections()])
    print(repos)


def enable_repos(repos, filename):
    config = read_config(filename)
    for repo in repos:
        config.set(repo, "enabled", "1")

    write_config(config, filename)


def disable_repos(repos, filename):
    config = read_config(filename)
    for repo in repos:
        config.set(repo, "enabled", "0")

    write_config(config, filename)


def main():
    parser = argparse.ArgumentParser(
        description="Work with RedHat RHUI INI File", usage="%(prog)s [options]"
    )

    parser.add_argument(
        "repo_ini",
        metavar="filename",
        help="Return the list of repositories available in the ini file",
        action="store",
    )
    parser.add_argument(
        "-disable",
        metavar="disable_repo_name",
        action="append",
        help="Name of repository to disable",
    )

    parser.add_argument(
        "-enable",
        metavar="enable_repo_name",
        action="append",
        help="Name of repository to enable",
    )

    if len(sys.argv) == 1:
        parser.print_help()
        parser.exit()
        return
    else:
        args = parser.parse_args()

    if args.repo_ini is None:
        parser.print_help()
        parser.exit()

    if args.disable is not None:
        disable_repos(args.disable, args.repo_ini)

    if args.enable is not None:
        enable_repos(args.enable, args.repo_ini)

    get_repos(args.repo_ini)


if __name__ == "__main__":
    main()
