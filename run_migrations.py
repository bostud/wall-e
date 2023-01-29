from core.migrations.first_migration import run_up


def run_migrations():
    run_up()


if __name__ == '__main__':
    run_migrations()
