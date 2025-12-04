#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数据采集功能测试脚本
"""

import requests
import json

BASE_URL = 'http://127.0.0.1:5000'

# 登录信息（需要根据实际情况修改）
LOGIN_USERNAME = 'admin'
LOGIN_PASSWORD = 'admin123'

def test_crawl_data():
    """测试数据采集功能"""
    print("测试数据采集功能...")
    
    # 构造请求
    url = f'{BASE_URL}/admin/data/crawl'
    data = {'keyword': '人工智能'}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    
    try:
        # 发送登录请求获取cookies
        login_url = f'{BASE_URL}/login'
        login_data = {
            'username': LOGIN_USERNAME,
            'password': LOGIN_PASSWORD
        }
        session = requests.Session()
        login_response = session.post(login_url, data=login_data, headers=headers)
        
        # 发送数据采集请求
        response = session.post(url, data=data, headers=headers)
        print(f"状态码: {response.status_code}")
        print(f"响应头: {dict(response.headers)}")
        print(f"响应内容: {response.text[:500]}...")  # 只显示前500个字符
        
        response.raise_for_status()
        
        try:
            result = response.json()
            print(f"JSON响应: {json.dumps(result, ensure_ascii=False, indent=2)}")
            
            if result.get('code') == 0:
                print("✅ 数据采集功能测试通过")
                return result.get('data', {}).get('news_list', [])
            else:
                print(f"❌ 数据采集功能测试失败: {result.get('msg')}")
                return []
        except json.JSONDecodeError:
            print("❌ 响应不是有效的JSON格式")
            return []
            
    except requests.RequestException as e:
        print(f"❌ 数据采集功能测试失败: {e}")
        return []

def test_deep_crawl(news_list):
    """测试深度采集功能"""
    if not news_list:
        print("没有可测试的新闻数据")
        return
        
    print("\n测试深度采集功能...")
    
    # 选择第一条新闻进行深度采集
    news = news_list[0]
    url = news.get('original_url')
    
    if not url:
        print("❌ 没有找到原始URL")
        return
        
    # 构造请求
    deep_crawl_url = f'{BASE_URL}/admin/data/deep-crawl'
    data = {'url': url}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    
    try:
        # 发送登录请求获取cookies
        login_url = f'{BASE_URL}/login'
        login_data = {
            'username': LOGIN_USERNAME,
            'password': LOGIN_PASSWORD
        }
        session = requests.Session()
        login_response = session.post(login_url, data=login_data, headers=headers)
        
        # 发送深度采集请求
        response = session.post(deep_crawl_url, data=data, headers=headers)
        response.raise_for_status()
        
        result = response.json()
        print(f"状态码: {response.status_code}")
        print(f"响应结果: {json.dumps(result, ensure_ascii=False, indent=2)}")
        
        if result.get('code') == 0:
            print("✅ 深度采集功能测试通过")
        else:
            print(f"❌ 深度采集功能测试失败: {result.get('msg')}")
            
    except requests.RequestException as e:
        print(f"❌ 深度采集功能测试失败: {e}")

def test_save_news(news_list):
    """测试数据保存功能"""
    if not news_list:
        print("没有可测试的新闻数据")
        return
        
    print("\n测试数据保存功能...")
    
    # 选择第一条新闻进行保存
    news = news_list[0]
    
    # 构造请求
    save_url = f'{BASE_URL}/admin/data/save-news'
    headers = {'Content-Type': 'application/json'}
    
    try:
        # 发送登录请求获取cookies
        login_url = f'{BASE_URL}/login'
        login_data = {
            'username': LOGIN_USERNAME,
            'password': LOGIN_PASSWORD
        }
        session = requests.Session()
        session.post(login_url, data=login_data, headers={'Content-Type': 'application/x-www-form-urlencoded'})
        
        # 发送数据保存请求
        response = session.post(save_url, json=news, headers=headers)
        response.raise_for_status()
        
        result = response.json()
        print(f"状态码: {response.status_code}")
        print(f"响应结果: {json.dumps(result, ensure_ascii=False, indent=2)}")
        
        if result.get('code') == 0:
            print("✅ 数据保存功能测试通过")
        else:
            print(f"❌ 数据保存功能测试失败: {result.get('msg')}")
            
    except requests.RequestException as e:
        print(f"❌ 数据保存功能测试失败: {e}")

if __name__ == '__main__':
    print("=== 数据采集管理功能测试 ===")
    
    # 测试数据采集
    news_list = test_crawl_data()
    
    # 测试深度采集
    test_deep_crawl(news_list)
    
    # 测试数据保存
    test_save_news(news_list)
    
    print("\n=== 测试完成 ===")
