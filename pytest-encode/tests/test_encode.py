#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from pytest_encode import logger

@pytest.mark.parametrize('name', ['哈利', '赫敏'])
def test_encode(name):
    logger.info(f"test data: {name}")
    print(name)
