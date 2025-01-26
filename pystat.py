import os
import subprocess
from getpass import getuser
from socket import gethostname
from platform import freedesktop_os_release


class Style(object):
    """
    here is a color dict and method for coloring text
    """

    def __init__(self):
        self.colors = {
            "red": "\33[31m",
            "green": "\33[32m",
            "yellow": "\33[33m",
            "blue": "\33[34m",
            "violet": "\33[35m",
            "pink": "\33[95m",
            "white": "\33[37m",
        }
        self.color_end = "\33[0m"

    def color_text(self, color, txt):
        """returns coloring text"""
        return color + txt + self.color_end


class PcInfo(Style):
    """
    here is  the system info needed for fetch
    """

    def __init__(self):
        Style.__init__(self)

    def get_username(self):
        """returns the name and hostname of the current user"""
        user = self.color_text(self.colors["white"], f"{getuser()}@{gethostname()}")
        return self.color_text(self.colors["red"], f"󰀄 user   {user}")

    def get_distro_name(self):
        """returns the system(distribution) name"""
        distro = self.color_text(
            self.colors["white"], str(freedesktop_os_release()["ID"])
        )
        return self.color_text(self.colors["yellow"], f"󰌽 distro {distro}")

    def get_pkgs_count(self):
        """return the count of installed pkgs on the system"""
        commands = [
            "pacman -Qq --color=never",  # Arch Linux
            "dpkg-query -f=${binary:Package}\\n -W",  # Debian, Ubuntu, Linux Mint,
            "dnf list installed -q",  # Fedora, RHEL
            "xbps-query -l",  # Void Linux
            "zypper search -i",  # openSuse
            "apk info",  # Apline Linux
            "pkg info -a",  # BSD
            "brew list",  # MacOS
        ]
        for command in commands:
            try:
                result = subprocess.check_output(command.split()).decode("utf-8")
                count = self.color_text(
                    self.colors["white"], str(len(result.splitlines()))
                )
                return self.color_text(self.colors["blue"], f"󰏗 pkgs   {count}")
            except FileNotFoundError:
                pass
        return -1

    def get_shell_name(self):
        """returns she'll name"""
        shell = self.color_text(self.colors["white"], os.getenv("SHELL"))
        return self.color_text(self.colors["green"], f"󰆍 shell  {shell}")

    def get_colors(self):
        """returns colored icons"""
        icons = {
            "yellow": "󰮯",
            "green": "󰧞",
            "red": "󰧞",
            "pink": "󰧞",
            "violet": "󰧞",
            "blue": "󰧞",
        }

        colored_icons = [
            self.color_text(self.colors[color], icon) for color, icon in icons.items()
        ]
        return " ".join(colored_icons)


if __name__ == "__main__":
    """SNAKE"""
    os.system("clear")
    obj = PcInfo()
    a = f"\n          .|.\t{obj.get_username()}"
    b = f"           |\t{obj.get_distro_name()}"
    c = f"        __/\t{obj.get_pkgs_count()}"
    d = f"       /\t{obj.get_shell_name()}"
    e = f"    __/\t\t{obj.get_colors()}\n"
    strings = [a, b, c, d, e]

    for i in strings:
        print(obj.color_text(obj.colors["green"], i))
