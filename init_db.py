#!/usr/bin/env python3
"""
初始化数据库，添加默认角色和管理员用户
"""

import os
import sys
from datetime import datetime
from werkzeug.security import generate_password_hash

# 添加项目根目录到Python路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app import create_app
from app.models import db, User, Role

app = create_app()

with app.app_context():
    print("初始化数据库...")
    
    # 创建默认角色
    print("创建默认角色...")
    admin_role = Role(
        name='admin',
        description='系统管理员，拥有所有功能权限',
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    
    user_role = Role(
        name='user',
        description='普通用户，只能查看数据报表和报告',
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    
    # 检查角色是否已存在
    if not Role.query.filter_by(name='admin').first():
        db.session.add(admin_role)
    if not Role.query.filter_by(name='user').first():
        db.session.add(user_role)
    
    # 创建默认管理员用户
    print("创建默认管理员用户...")
    if not User.query.filter_by(username='admin').first():
        admin_user = User(
            username='admin',
            email='admin@example.com',
            password_hash=generate_password_hash('admin123'),
            role_id=Role.query.filter_by(name='admin').first().id,
            is_active=True,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        db.session.add(admin_user)
    
    # 创建默认普通用户
    print("创建默认普通用户...")
    if not User.query.filter_by(username='user').first():
        normal_user = User(
            username='user',
            email='user@example.com',
            password_hash=generate_password_hash('user123'),
            role_id=Role.query.filter_by(name='user').first().id,
            is_active=True,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        db.session.add(normal_user)
    
    # 提交更改
    db.session.commit()
    print("数据库初始化完成！")
    print("\n默认账号：")
    print("管理员：admin / admin123")
    print("普通用户：user / user123")
