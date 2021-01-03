import unittest
from cluc import Culc

release_name = 'prod'


class CalcTest(unittest.TestCase):
    def setUp(self):
        # テストそれぞれ開始時に呼ばれる
        print('setup')
        self.cal = Culc()

    def tearDown(self):
        # テストそれぞれ終了時時に呼ばれる
        print('clean up')
        del self.cal

    @unittest.skip('skip')  # テストをスキップする
    def test_add_num_and_double_skip(self):
        self.assertAlmostEqual(self.cal.add_and_doubel(1, 1), 4)

    # if リリースや開発環境で実行するテストを変えたい時使用
    @unittest.skipIf(release_name == 'prod', 'skip')
    def test_add_num_and_double_skip_if(self):
        self.assertAlmostEqual(self.cal.add_and_doubel(1, 1), 4)

    def test_add_num_and_double(self):
        self.assertAlmostEqual(self.cal.add_and_doubel(1, 1), 4)

    def test_add_num_and_double_raise(self):
        # 例外テスト　assertRaisesを使用
        with self.assertRaises(ValueError):
            (self.cal.add_and_doubel("1", "1"))


if __name__ == "__main__":
    unittest.main()
