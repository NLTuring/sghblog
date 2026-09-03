# SchoolHall 博客 — 仿 CSDN 博客系统

![Django](https://img.shields.io/badge/Django-5.0.3-green)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-blue)
![License](https://img.shields.io/badge/许可证-MIT-yellow)

一个基于 **Django 5.0 + Bootstrap 5 + WangEditor** 构建的轻量级个人博客系统，界面风格仿照 CSDN，支持 Markdown-like 富文本编辑、代码高亮、分类管理、评论系统和全文检索。

---

## 📸 功能截图

| 首页列表 | 博客详情 | 发布博客 |
|---------|---------|---------|
| 卡片式布局，每页 5 篇，支持分页 | 代码语法高亮，bleach 安全过滤 | 富文本编辑器，含分类选择 |
| 登录 / 注册 | 评论功能 | 搜索功能 |
| 邮箱验证码注册，记住我 | 按博客逐条评论 | 标题 + 内容全文检索 |

---

## ✨ 主要特性

- **📝 富文本发布**：集成 WangEditor 5，支持图片、代码块、格式化等
- **🔍 代码高亮**：highlight.js 支持 190+ 编程语言，博客详情页自动高亮
- **🔐 用户系统**：邮箱注册 + 验证码 + 登录状态持久化（记住我）
- **📂 分类管理**：每篇博客归入一个分类，Django Admin 可视化管理
- **💬 评论系统**：登录用户可对博客发表评论
- **🔎 全文检索**：支持按标题和内容关键字搜索
- **🛡️ XSS 防护**：bleach 自动过滤危险 HTML 标签，只保留安全标签
- **📄 分页展示**：首页列表每页 5 篇，支持上一页 / 下一页 / 页码跳转
- **🐍 零依赖启动**：默认 SQLite 数据库，无需 MySQL，双击 `start.cmd` 即可运行

---

## 🛠️ 技术栈

| 层次 | 技术 |
|------|------|
| 后端 | Django 5.0.3（Python 3.11） |
| 前端 | Bootstrap 5.3 · jQuery 3.7 · WangEditor 5 |
| 代码高亮 | highlight.js（含 190+ 语言包） |
| 数据库 | SQLite 3（开发） / MySQL 8（生产可选） |
| 安全 | bleach 6.2（HTML 消毒）· Django CSRF · 密码哈希 |

---

## 📁 项目结构

```
sghblog/
├── blog/                          # 博客主应用
│   ├── models.py                  # Blog / BlogCategory / BlogComment 模型
│   ├── views.py                   # 首页、详情、发布、搜索、评论 视图
│   ├── urls.py                    # 博客路由
│   ├── forms.py                   # 发布博客表单
│   ├── admin.py                   # Django Admin 注册
│   ├── management/
│   │   └── commands/
│   │       └── init_sample_data.py   # 一键生成示例数据管理命令
│   └── migrations/                # 数据库迁移文件
│
├── sghauth/                       # 用户认证应用
│   ├── models.py                  # CaptchaModel（验证码）
│   ├── views.py                   # 登录 / 注册 / 退出 / 邮箱验证码
│   ├── forms.py                   # RegisterForm / LoginForm
│   ├── urls.py                    # 认证路由
│   └── admin.py
│
├── sghblog/                       # 项目配置
│   ├── settings.py                # Django 全局配置
│   ├── urls.py                    # 根路由
│   └── wsgi.py / asgi.py
│
├── templates/                     # HTML 模板
│   ├── base.html                  # 基础布局（导航栏 + 搜索框）
│   ├── index.html                 # 首页博客列表（含分页）
│   ├── blog_detail.html           # 博客详情 + 评论 + 代码高亮
│   ├── pub_blog.html              # 发布博客页（WangEditor）
│   ├── login.html                 # 登录页
│   ├── register.html              # 注册页
│   └── 404.html                   # 自定义 404 页面
│
├── static/                        # 静态资源
│   ├── bootstrap5/                # Bootstrap CSS + JS
│   ├── highlight/                 # highlight.js 全量语言包
│   ├── jquery/                    # jQuery 3.7.1
│   ├── wangeditor/                # WangEditor 5
│   ├── css/base.css               # 自定义样式
│   └── js/
│       ├── pub_blog.js            # 发布博客 AJAX 提交
│       └── register.js            # 注册页验证码倒计时
│
├── start.cmd                      # ⭐ 双击启动开发服务器
├── init_data.cmd                  # ⭐ 双击一键生成示例数据
├── manage.py                      # Django 管理入口
├── db.sqlite3                     # SQLite 数据库文件
└── my.cnf                         # MySQL 配置（生产可选）
```

---

## 🚀 快速开始

### 方式一：双击运行（推荐）

1. **双击 `init_data.cmd`** — 初始化数据库 + 生成示例数据
2. **双击 `start.cmd`** — 启动服务器 + 自动打开浏览器

> 浏览器访问 http://127.0.0.1:8000

### 方式二：命令行

```bash
# 克隆项目
git clone https://github.com/NLTuring/sghblog.git
cd sghblog

# 安装依赖（确保已安装 Python 3.11 + Django 5.0）
pip install django==5.0.3

# 初始化数据库
python manage.py migrate

# 生成示例数据（5 个分类 + demo 用户 + 5 篇博客）
python manage.py init_sample_data

# 启动开发服务器
python manage.py runserver
```

---

## 🧑‍💻 示例账号

启动后可通过以下账号登录体验：

| 字段 | 值 |
|------|----|
| 邮箱 | `demo@example.com` |
| 密码 | `demo123` |

或在首页点击 **注册** 自行注册新账号。

---

## 🔧 管理后台

Django Admin 提供分类、博客、评论的后台管理：

```bash
python manage.py createsuperuser    # 创建超级管理员
python manage.py runserver
# 访问 http://127.0.0.1:8000/admin
```

---

## 🛡️ 安全设计

- **bleach HTML 消毒**：博客内容渲染前经过 bleach 清洗，只允许 `<b>` / `<code>` / `<a>` / `<blockquote>` / `<pre>` / `<ul>` / `<ol>` / `<li>` / `<p>` / `<br>` / `<span>` 等安全标签，杜绝 XSS 注入
- **Django CSRF 防护**：所有表单提交均携带 CSRF token
- **密码哈希**：使用 Django 内置 PBKDF2 算法存储用户密码
- **会话安全**：支持「记住我」选项，未勾选时浏览器关闭即登出

---

## 📌 待改进方向

- [ ] 博客编辑 / 删除功能（目前仅支持发布）
- [ ] 博客封面图片上传
- [ ] 分类 CRUD 前端页面
- [ ] Markdown 原生支持
- [ ] 评论回复（嵌套评论）
- [ ] 博客点赞 / 收藏
- [ ] 邮件 SMTP 实际配置（当前为硬编码示例）
- [ ] Docker 部署配置

---

## 📄 许可证

MIT License

---

> 本项目为学习练习用途，部分 UI 设计参考 [CSDN](https://www.csdn.net/)。
