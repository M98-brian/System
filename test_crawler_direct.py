import sys
import os

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.crawler import BaiduNewsCrawler

def test_crawler_directly():
    """直接测试爬虫功能"""
    print("=== 直接测试爬虫功能 ===")
    
    # 创建爬虫实例
    crawler = BaiduNewsCrawler()
    
    # 测试抓取新闻
    keyword = "科技"
    print(f"\n使用关键字 '{keyword}' 抓取新闻...")
    
    news_list = crawler.fetch_news(keyword)
    
    print(f"\n抓取结果：")
    print(f"共抓取到 {len(news_list)} 条新闻")
    
    if news_list:
        print(f"\n第一条新闻：")
        first_news = news_list[0]
        for key, value in first_news.items():
            print(f"{key}: {value}")
    else:
        print("未抓取到任何新闻数据")
    
    print("\n=== 测试完成 ===")

if __name__ == "__main__":
    test_crawler_directly()