from django.core.management.base import BaseCommand
from blog.models import BlogCategory, Blog
from django.contrib.auth import get_user_model

User = get_user_model()

SAMPLE_CATEGORIES = ['Django', 'Python', 'JavaScript', '机器学习', '运维部署']

SAMPLE_BLOGS = [
    ('Django 5.0 新特性详解', 'Django', '<h2>自动字段默认值</h2><p>Django 5.0 引入了多项改进，最显著的是<strong>异步ORM支持</strong>和<code>JsonField</code>原生支持。</p><pre><code class="language-python">from django.db import models\n\nclass Article(models.Model):\n    data = models.JSONField()\n</code></pre><p>这些改进让 Django 在现代全栈开发中更具竞争力。</p>'),
    ('Python 异步编程指南', 'Python', '<p>Python 3.7+ 原生支持<code>asyncio</code>，理解以下核心概念是关键：</p><ul><li><strong>协程</strong>：用 <code>async def</code> 定义</li><li><strong>事件循环</strong>：用 <code>asyncio.run()</code> 启动</li><li><strong>等待</strong>：用 <code>await</code> 挂起</li></ul><pre><code class="language-python">import asyncio\n\nasync def main():\n    print("Hello")\n\nasyncio.run(main())\n</code></pre>'),
    ('JavaScript ES2024 新特性速览', 'JavaScript', '<p>ES2024 带来了<strong>Array Grouping</strong>、<strong>Temporal API</strong>等实用特性。</p><pre><code class="language-javascript">const data = [\n  { name: "Alice", score: 90 },\n  { name: "Bob", score: 80 },\n];\nconst grouped = Object.groupBy(data, d => d.score);\n</code></pre>'),
    ('Scikit-learn 快速入门', '机器学习', '<p>Scikit-learn 是 Python 最流行的机器学习库，适合<strong>入门到实战</strong>。</p><pre><code class="language-python">from sklearn.ensemble import RandomForestClassifier\nclf = RandomForestClassifier()\nclf.fit(X_train, y_train)\n</code></pre>'),
    ('Nginx + Gunicorn 部署 Django', '运维部署', '<p>生产环境推荐使用<strong>Gunicorn + Nginx</strong>组合：</p><ol><li>Gunicorn 负责运行 WSGI 应用</li><li>Nginx 负责反向代理、静态文件、HTTPS</li></ol><pre><code class="language-bash">gunicorn myproject.wsgi:application --bind 0.0.0.0:8000</code></pre>'),
]

class Command(BaseCommand):
    help = '初始化分类和示例博客数据'

    def handle(self, *args, **options):
        # 创建分类
        for name in SAMPLE_CATEGORIES:
            cat, _ = BlogCategory.objects.get_or_create(name=name)
            self.stdout.write(self.style.SUCCESS(f'分类已就绪: {cat.name}'))

        # 获取或创建示例用户
        user, _ = User.objects.get_or_create(
            username='demo',
            defaults={'email': 'demo@example.com'}
        )
        user.set_password('demo123')
        user.save()
        self.stdout.write(self.style.SUCCESS(f'示例用户: {user.username} / demo123'))

        # 创建示例博客
        for title, cat_name, content in SAMPLE_BLOGS:
            cat = BlogCategory.objects.filter(name=cat_name).first()
            if not cat:
                self.stdout.write(self.style.WARNING(f'分类不存在，跳过: {cat_name}'))
                continue
            blog, created = Blog.objects.get_or_create(
                title=title,
                defaults={'content': content, 'category': cat, 'author': user}
            )
            action = '创建' if created else '已存在'
            self.stdout.write(self.style.SUCCESS(f'博客[{action}]: {blog.title}'))

        self.stdout.write(self.style.SUCCESS('初始化完成！'))
