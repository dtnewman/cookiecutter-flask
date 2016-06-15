# -*- coding: utf-8 -*-
"""Test configs."""
from {{cookiecutter.app_name}}.app import create_app
from {{cookiecutter.app_name}}.settings import Local, Production


def test_production_config():
    """Production config."""
    app = create_app(Production)
    assert app.config['ENV'] == 'prod'
    assert app.config['DEBUG'] is False
    assert app.config['DEBUG_TB_ENABLED'] is False
    assert app.config['ASSETS_DEBUG'] is False


def test_dev_config():
    """Development config."""
    app = create_app(Local)
    assert app.config['ENV'] == 'dev'
    assert app.config['DEBUG'] is True
    assert app.config['ASSETS_DEBUG'] is True
