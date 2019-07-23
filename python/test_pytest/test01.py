# -*- coding: utf-8 -*-
# @Data : 2019-07-23

import pytest

class Test01:

    # @pytest.mark.parametrize("case_name, param1, param2, expected", [
    #     ("case01: test", 1, 2, 3),
    #     ("case02: 浮点数相加不等于预期值", 1.1, 1.2, 2.3)
    # ])
    def test_fail(self):
        """case01: 这是一个用例"""
        
        assert ((1 + 2) == 3)