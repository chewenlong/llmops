#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/10/31 20:32
@Author  : chewl1
@File    : test_app_handler.py
"""
import pytest

from pkg.response import HttpCode


class TestHandler:
    """APP控制器的测试类"""

    @pytest.mark.parametrize("query", [None, "你好你是谁"])
    def test_completion(self, query, client):
        resp = client.post(
            "/http/completion",
            json={"query": query}
        )
        print("响应内容:", resp.json)
        assert resp.status_code == 200
        if query is None:
            assert resp.json.get("code") == HttpCode.VALIDATE_ERROR
        else:
            assert resp.json.get("code") == HttpCode.SUCCESS
        print("响应内容:", resp.json)
