# -*- coding: utf-8 -*-
"""Application configuration."""
import os


class Config(object):
    """Base configuration."""

    SECRET_KEY = os.environ.get('{{cookiecutter.app_name | upper}}_SECRET', 'secret-key')  # TODO: Change me
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    BCRYPT_LOG_ROUNDS = 13
    ASSETS_DEBUG = False
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Local(Config):
    """Production configuration."""

    ENV = 'lcl'
    DEBUG = True
    ASSETS_DEBUG = True
    SQLALCHEMY_DATABASE_URI =  'postgresql://kyruus:kyruus@localhost:5432/myflaskapp'
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar


class Production(Config):
    """Production configuration."""

    ENV = 'prd'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://address_to_remote_db'  # TODO: Change me
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar


class TestConfig(Config):
    """Test configuration."""

    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    BCRYPT_LOG_ROUNDS = 4  # For faster tests; needs at least 4 to avoid "ValueError: Invalid rounds"
    WTF_CSRF_ENABLED = False  # Allows form testing
