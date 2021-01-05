from unit_test_module import cluc
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


    @pytest.mark.skipif(is_release==True, reason="is_release")
    def test_add_num_and_double_skip_if(self):
        assert self.cal.add_and_doubel(1, 1) == 4
