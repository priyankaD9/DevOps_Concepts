"""
conditions.py
--------------
Real-world usage of conditional statements in Python
with DevOps-inspired examples.

"""

def check_server_status(cpu_usage: int) -> str:
    """Evaluate server health based on CPU usage."""
    if cpu_usage > 90:
        return "CRITICAL: Server overloaded "
    elif cpu_usage > 70:
        return "WARNING: High CPU usage"
    else:
        return "OK: Server running smoothly"


def check_login_access(username: str, password: str) -> str:
    """Simple authentication check."""
    valid_user = "admin"
    valid_pass = "devops123"

    if username == valid_user and password == valid_pass:
        return "Access Granted"
    else:
        return "Access Denied"


def environment_check(env: str) -> str:
    """Check environment type."""
    if env.lower() == "production":
        return "Be careful! You are in PRODUCTION"
    elif env.lower() == "staging":
        return "This is STAGING environment"
    else:
        return "Development mode"


if __name__ == "__main__":
    print("=== DevOps Condition Checks ===\n")

    print(check_server_status(85))
    print(check_login_access("admin", "devops123"))
    print(environment_check("production"))