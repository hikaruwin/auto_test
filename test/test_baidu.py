import pytest

from test.common.baidu_page import BaiduPage


class TestBaidu:

    def setup(self):
        self.bs = BaiduPage()

    def test_01_baidu(self):
        self.bs.search()

    def teardown(self):
        self.bs.quit()


if __name__ == '__main__':
    pytest.main()
