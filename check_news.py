#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
检查数据库中的新闻数据
"""

from app import create_app
from app.models import News

def check_news():
    """检查数据库中的新闻"""
    app = create_app()
    with app.app_context():
        news_count = News.query.count()
        print(f"数据库中共有 {news_count} 条新闻")
        
        if news_count > 0:
            print("\n新闻列表:")
            for i, news in enumerate(News.query.all(), 1):
                print(f"{i}. [{news.id}] {news.title[:50]}...")

if __name__ == "__main__":
    check_news()
