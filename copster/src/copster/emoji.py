fail = "❌"
pass_ = "✅"
warn = "⚠️"
run = "🏃"


def print_logo() -> None:
    msg = r"""
                         _
      ___ ___  _ __  ___| |_ ___ _ __
     / __/ _ \| '_ \/ __| __/ _ \ '__|
    | (_| (_) | |_) \__ \ ||  __/ |
     \___\___/| .__/|___/\__\___|_|
              |_|

    Opionated checker.
    This cop cannot be bribed.
    """

    print(msg)
