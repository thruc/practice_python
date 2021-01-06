import pytest


def pytest_addoption(parser):
    parser.addoption('--os-name', action="store", dest="name",
                     default='linux', help='os name')
                     
# 以下によってすべての小文字の短いオプションを制限されている
'''https://github.com/pytest-dev/pytest/blob/322190fd84e1b86d7b9a2d71f086445ca80c39b3/src/_pytest/config/argparsing.py#L362-L369
def _addoption_instance(self, option: "Argument", shortupper: bool = False) -> None:
    if not shortupper:
        for opt in option._short_opts:
            if opt[0] == "-" and opt[1].islower():
                raise ValueError("lowercase shortoptions reserved")
    if self.parser:
        self.parser.processoption(option)
    self.options.append(option)
'''


'''
# プラグイン使用方法
pytest_plugins = ["pytester"]
def pytest_addoption(parser):
    group = parser.getgroup("helloworld")
    group.addoption(
        "--name",
        action="store",
        dest="name",
        default="World",
        help='Default "name" for hello().',
    )


@pytest.fixture
def hello(request):
    name = request.config.getoption("name")

    def _hello(name=None):
        if not name:
            name = request.config.getoption("name")
        return "Hello {name}!".format(name=name)

    return _hello
'''
