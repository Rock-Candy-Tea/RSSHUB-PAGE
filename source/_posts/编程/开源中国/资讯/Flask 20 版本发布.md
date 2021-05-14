
---
title: 'Flask 2.0 版本发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-bb7c6866e0b73622293126cc664cd2f5719.png'
author: 开源中国
comments: false
date: Thu, 13 May 2021 23:26:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-bb7c6866e0b73622293126cc664cd2f5719.png'
---

<div>   
<div class="content">
                                                                    
                                                        <blockquote> 
 <p>本文已获<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgreyli.com%2Fabout%2F" target="_blank">李辉</a>授权转载。<br> 原文地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgreyli.com%2Fflask2%2F" target="_blank">https://greyli.com/flask2/</a></p> 
</blockquote> 
<p>Flask 以及 Flask 依赖的 5 个 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpalletsprojects.com%2F" target="_blank">Pallets 项目</a>都在今天发布了新的主版本（下面的链接指向各个项目的主版本变动日志）：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fflask.palletsprojects.com%2Fen%2F2.0.x%2Fchanges%23version-2-0-0" target="_blank">Flask 2.0</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwerkzeug.palletsprojects.com%2Fen%2F2.0.x%2Fchanges%2F%23version-2-0-0" target="_blank">Werkzeug 2.0</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjinja.palletsprojects.com%2Fen%2F3.0.x%2Fchanges%2F%23version-3-0-0" target="_blank">Jinja 3.0</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fclick.palletsprojects.com%2Fen%2F8.0.x%2Fchanges%2F%23version-8-0" target="_blank">Click 8.0</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fitsdangerous.palletsprojects.com%2Fen%2F2.0.x%2Fchanges%2F%23version-2-0-0" target="_blank">ItsDangerous 2.0</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fmarkupsafe.palletsprojects.com%2Fen%2F2.0.x%2Fchanges%2F%23version-2-0-0" target="_blank">MarkupSafe 2.0</a></li> 
</ul> 
<p>​你可以使用下面的命令更新 Flask：</p> 
<pre><code class="language-bash">pip install -U flask</code></pre> 
<p>如果你使用的国内 PyPI 镜像还没有同步最新版本，可以通过下面的命令临时切换到官方 PyPI 源：</p> 
<pre><code class="language-bash">pip install -U flask -i https://pypi.org/simple/</code></pre> 
<p>这篇文章会介绍一些 Flask 新增的特性，完整的变动可以参考上面各个项目的变动日志。</p> 
<h2>三个核心特性</h2> 
<p><strong>嵌套蓝本（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpallets%2Fflask%2Fpull%2F3923" target="_blank">#3923</a>）</strong></p> 
<p>对于一个比较大的项目，一般会使用蓝本来组织不同的模块。而如果你的项目非常大，那么嵌套蓝本就可以派上用场了。借助嵌套蓝本支持，你可以在某个蓝本之再创建多个子蓝本，对项目进行多层模块化组织（而且支持无限嵌套，你可以嵌套很多层）：</p> 
<pre><code class="language-python"> parent = Blueprint("parent", __name__)  # 创建父蓝本
 child = Blueprint("child", __name__)  # 创建子蓝本
 parent.register_blueprint(child, url_prefix="/child")  # 把子蓝本注册到父蓝本上
 app.register_blueprint(parent, url_prefix="/parent")  # 把父蓝本注册到程序实例上</code></pre> 
<p>这样在生成子蓝本的 URL 时需要传入完整的端点链：</p> 
<pre><code class="language-python"> url_for('parent.child.create')
 /parent/child/create</code></pre> 
<p>这个特性来源于一个 2012 年创建的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpallets%2Fflask%2Fissues%2F593" target="_blank">feature request issue</a>。</p> 
<p><strong>基本的 async/await 支持（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpallets%2Fflask%2Fpull%2F3412" target="_blank">#3412</a>）</strong></p> 
<p>Flask 2.0 带来了基本的异步支持，现在你可以定义异步视图（以及异步错误处理函数、异步请求钩子函数）：</p> 
<pre><code class="language-python"> import asyncio
 from flask import Flask
 ​
 app = Flask(__name__)
 ​
 @app.route('/')
 async def say_hello():
     await asyncio.sleep(1)
     return &#123;'message': 'Hello!'&#125;</code></pre> 
<p>注意要先安装额外依赖：</p> 
<pre><code class="language-bash">pip install -U flask[async]</code></pre> 
<p>顺便说一句，如果你在 Windows 上使用 Python 3.8，那么会有一个来自 Python 或 asgiref 的 bug 导致出错：ValueError: set_wakeup_fd only works in main thread。可以通过下面两种方式（任选一种）处理（具体参考<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fstackoverflow.com%2Fa%2F67308923%2F5511849" target="_blank">这个 SO 回答</a>）：</p> 
<ul> 
 <li>升级到 Python 3.9</li> 
 <li>在你的入口脚本顶部添加临时修复代码：</li> 
</ul> 
<pre><code class="language-python"> # top of the file
 import sys, asyncio
 ​
 if sys.platform == "win32" and (3, 8, 0) <= sys.version_info < (3, 9, 0)::
     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())</code></pre> 
<p>不过目前只是一个基于 asgiref 的异步实现，作为异步支持的第一步，后续还会进行更多的优化和改进，更多相关信息可以参考<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fflask.palletsprojects.com%2Fen%2F2.0.x%2Fasync-await%2F" target="_blank">文档</a>。</p> 
<p><strong>快捷路由装饰器（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpallets%2Fflask%2Fpull%2F3907" target="_blank">#3907</a>）</strong></p> 
<p>新增了下面的快捷路由装饰器：</p> 
<ul> 
 <li><code>app.get()</code></li> 
 <li><code>app.post()</code></li> 
 <li><code>app.delete()</code></li> 
 <li><code>app.put()</code></li> 
 <li><code>app.patch()</code></li> 
</ul> 
<p>举例来说，使用 <code>app.post()</code> 等同于 <code>app.route(methods=['POST'])</code>：</p> 
<pre><code class="language-python"> from flask import Flask
 ​
 app = Flask(__name__)
 ​
 @app.post('/')
 def index():
     return &#123;'message': 'Hello!'&#125;</code></pre> 
<p>注意不要在这些快捷装饰器里传入 <code>methods</code> 参数。如果需要在单个视图处理多个方法的请求，使用 <code>app.route()</code>。</p> 
<p>我在某次 pallets 会议上提议添加这些装饰器时一开始是被拒绝的，后来 Phil Jones 创建了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpallets%2Fflask%2Fpull%2F3907" target="_blank">#3907</a> 经过二次讨论后才最终合并（被拒绝后我就把当时正在开发的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgreyli%2Fapiflask" target="_blank">APIFlask</a> 从扩展改成了继承 Flask 基类的框架，然后加了这些装饰器）。</p> 
<h2>我添加的三个特性</h2> 
<p><strong>修复执行 flask run 找不到程序的奇怪设定（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpallets%2Fflask%2Fpull%2F3560" target="_blank">#3560</a>）</strong></p> 
<p>这个像 bug 又像是 feature 的设定我在《<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgreyli.com%2Fa-flask-bug-that-bother-me-two-years%2F" target="_blank">一个困扰我两年的 Flask「Bug」</a>》里详细说过，最终终于在两年后修复了。</p> 
<p><strong>支持在 .flaskenv 和 .env 文件里写中文（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpallets%2Fflask%2Fpull%2F3932" target="_blank">#3932</a>）</strong></p> 
<p>我在《Flask Web 开发实战》第一章介绍 .flaskenv 文件时给了一个示例，演示如何添加注释：</p> 
<pre><code class="language-python">SOME_VAR=1
# 这是注释</code></pre> 
<p>但这个示例没有实际测试……加了中文其实会报错，后来有两次收到读者反馈，最终终于在三年后修复了。</p> 
<p><strong>为文档添加命令切换面板（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpallets%2Fflask%2Fpull%2F3714" target="_blank">#3714</a>）</strong></p> 
<p>这个或许算不上特性，不过在我看来是对用户非常友好的变动。除了个别不需要区分操作系统和命令行程序的命令外，我给文档里所有的命令添加了支持切换 Bash/CMD/Powershell 以及 macOS/Linux/Windows 的切换面板（面板的样式后续会有一些<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpallets%2Fpallets-sphinx-themes%2Fpull%2F31" target="_blank">优化</a>）：</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-bb7c6866e0b73622293126cc664cd2f5719.png" referrerpolicy="no-referrer"></p> 
<h2>其他的有用特性</h2> 
<ul> 
 <li>优化了浏览器缓存控制，对 CSS、图片等静态文件做出的变动会在程序重载后立刻更新，不再需要手动清除页面缓存。</li> 
 <li>Werkzeug 的 multipart 解析（尤其是大文件上传处理）性能提高了 15 倍。</li> 
 <li>配置对象增加 <code>Config.from_file()</code> 方法支持从任意文件加载器导入配置（比如 <code>toml.load</code>、<code>json.load</code>），未来会取代 <code>Config.from_json()</code> 方法。</li> 
 <li>在使用环境变量 <code>FLASK_APP</code> 指定工厂函数时支持传入关键字参数。</li> 
 <li><code>flask shell</code> 支持 tab 和历史补全（需要安装 <code>readline</code>）。</li> 
 <li>CLI 系统优化了找不到程序时的错误处理和错误输出显示，同时修正了 Windows 上的命令行颜色输出。</li> 
</ul> 
<h2>破坏性变动</h2> 
<p>主要的破坏性变动（breaking change）是意外的把 <code>send_from_directory()</code> 函数的第二个参数名称直接由 <code>filename</code> 重命名为 <code>path</code>，将会在 2.0.1 加回来（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpallets%2Fflask%2Fpull%2F4019" target="_blank">#4019</a>）。</p> 
<p>另外 <code>send_file()</code> 函数的三个参数也进行了重命名（旧名称将在 2.1.0 移除）：</p> 
<ul> 
 <li><code>attachment_filename</code> -> <code>download_name</code></li> 
 <li><code>cache_timeout</code> -> <code>max_age</code></li> 
 <li><code>add_etags</code> -> <code>etag</code></li> 
</ul> 
<h2>其他重要变化</h2> 
<ul> 
 <li>不再支持 Python 2 和 Python 3.5。</li> 
 <li>所有 Pallets 项目都添加了 type hinting，这意味着更好的 IDE 自动补全体验。</li> 
 <li>所有仓库的主分支由 master 改为 main。如果你在本地克隆了 Flask 等仓库，可以使用下面的命令来更新：</li> 
</ul> 
<pre><code class="language-bash"> git branch -m master main
 git fetch origin
 git branch -u origin/main main
 git remote set-head origin -a</code></pre> 
<h2>感谢支持</h2> 
<p>这次更新对于整个 Pallets 项目来说是一个新的里程碑。接下来还有许多事情要做：FlaskCon 2021 正在准备中，新建立的 Flask 社区工作小组（Flask Community Work Group）正在进行 Flask 文档翻译（如果你对中文翻译感兴趣，可以订阅<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fgreyli%2Fhelloflask%2Fdiscussions%2F239" target="_blank">这个讨论</a>）、被遗弃扩展收容计划（这是我一直想做的事情）等等。感谢支持，敬请期待！</p> 
<p>欢迎通过下列途径关注 Pallets 项目：</p> 
<ul> 
 <li>关注 Twitter <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Ftwitter.com%2FPalletsTeam" target="_blank">@PalletsTeam</a></li> 
 <li>订阅 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpalletsprojects.com%2Fblog%2Ffeed.xml" target="_blank">Pallets 博客 RSS</a></li> 
 <li>加入 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdiscord.gg%2Fpallets" target="_blank">Pallets Discord 服务器</a></li> 
 <li>在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpallets%2Fflask" target="_blank">GitHub</a> 点击 Watch 按钮关注项目动态</li> 
</ul> 
<p>相关文章：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpalletsprojects.com%2Fblog%2Fflask-2-0-released%2F" target="_blank">New Major Versions Released! Flask 2.0, Werkzeug 2.0, and more – Pallets Blog</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DG54QyX_lWo8%26t%3D166s%26ab_channel%3DTalkPython" target="_blank">Flask 2.0 – Talk Python Podcast</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgreyli.com%2Fbetter-than-typo-fix%2F" target="_blank">比修 Typo 还简单的开源贡献方式</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgreyli.com%2Fwhat-flask-book-bring-to-the-community%2F" target="_blank">写作一本技术书，能给一个社区带来哪些改变？</a></li> 
</ul> 
<p>本条目发布于<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgreyli.com%2Fflask2%2F" target="_blank">2021年5月12日</a>。属于<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgreyli.com%2Fcategory%2Fcode%2F" target="_blank">计算机与编程</a>分类，被贴了 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgreyli.com%2Ftag%2Fflask%2F" target="_blank">Flask</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgreyli.com%2Ftag%2Fflask2%2F" target="_blank">Flask2</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgreyli.com%2Ftag%2Fpallets%2F" target="_blank">Pallets</a> 标签。</p>
                                        </div>
                                      
</div>
            