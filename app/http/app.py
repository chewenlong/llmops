#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/10/29 21:52
@Author  : chewl1
@File    : http.py
"""
import dotenv
from injector import Injector

from config import Config
from internal.router import Router
from internal.server.http import Http
from pkg.sqlalchemy import SQLAlchemy
from .module import ExtensionModule

dotenv.load_dotenv()

config = Config()

injector = Injector([ExtensionModule])

app = Http(__name__, conf=config, db=injector.get(SQLAlchemy), router=injector.get(Router))

if __name__ == '__main__':
    app.run(debug=True)
