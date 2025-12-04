# GovlnSystem

## 项目简介
基于Flask框架开发的政府内网系统

## 技术栈
- Flask 2.x
- Python 3.8+
- Jinja2 模板引擎
- Layui 前端框架
- Flask-Migrate 数据库迁移
- pytest 测试框架

## 目录结构
```
├── app/                    # Flask 程序包（只放代码，不放静态文件）
├── migrations/             # Flask-Migrate 自动生成的迁移仓库
├── tests/                  # 单元测试 & 接口测试（pytest）
├── static/                 # Layui、img、upload（Nginx 直接托管）
├── templates/              # Jinja2 模板（仅放 .html）
├── docs/                   # 项目文档
├── requirements/           # 多环境依赖文件
├── tools/                  # 工具脚本
├── .env/                   # 环境变量模板
├── README.md
```

## 环境要求
- Python 3.8+
- pip 20.0+

## 安装与运行
1. 克隆代码
2. 安装依赖
3. 配置环境变量
4. 运行开发服务器

## 开发规范
- 使用PEP 8编码规范
- 代码注释清晰
- 遵循Flask最佳实践
- 编写单元测试和接口测试
