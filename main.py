def hello(name: str, follow_up: str | None = None) -> str:
    follow_up = ' ' + follow_up if follow_up else None
    return f"Hello, {name}!{follow_up}"
