def pytest_addoption(parser):
    """ Add flags option to the pytset command"""
    parser.addoption(
        "--environment", action="store", default="local", help="Environments: local, qa, prod"
    )
