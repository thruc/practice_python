from .. import cluc
import pytest

is_release = True


class TestCal:
    @classmethod
    def setup_class(cls):
        print('start')

    @classmethod
    def teardown_class(cls):
        print('end')

    def setup_method(self, method):
        # テストそれぞれ開始時に呼ばれる
        print('setup')
        self.cal = cluc.Culc()

    def teardown_method(self, method):
        # テストそれぞれ終了時時に呼ばれる
        print('clean up')
        del self.cal

    def test_add_num_and_double(self):
        assert self.cal.add_and_doubel(1, 1) == 4

    def test_add_num_and_double_raise(self):
        # 例外テスト　pytest.raisesを使用
        with pytest.raises(ValueError):
            (self.cal.add_and_doubel("1", "1"))

    @pytest.mark.skipif(is_release == True, reason="is_release")
    def test_add_num_and_double_skip_if(self):
        assert self.cal.add_and_doubel(1, 1) == 4

'''
# プラグイン使用方法
def test_hello(pytester):
    """Make sure that our plugin works."""

    # create a temporary conftest.py file
    pytester.makeconftest(
        """
        import pytest

        @pytest.fixture(params=[
            "Brianna",
            "Andreas",
            "Floris",
        ])
        def name(request):
            return request.param
    """
    )

    # create a temporary pytest test file
    pytester.makepyfile(
        """
        def test_hello_default(hello):
            assert hello() == "Hello World!"

        def test_hello_name(hello, name):
            assert hello(name) == "Hello {0}!".format(name)
    """
    )

    # run all tests with pytest
    result = pytester.runpytest()

    # check that all 4 tests passed
    result.assert_outcomes(passed=4)
'''