
---
title: 'Poetry 1.2.0 发布，Python 依赖管理和打包工具'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2022/0907/082531_2cQs_2720166.gif'
author: 开源中国
comments: false
date: Wed, 07 Sep 2022 08:40:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2022/0907/082531_2cQs_2720166.gif'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0px; margin-right:0px; text-align:start">Poetry 1.2.0 已正式发布。在 2 年开发周期内，新版本包含许多变化、新特性和 Bugfix。</p> 
<blockquote> 
 <p>Poetry 是一款 Python 依赖管理和打包工具。</p> 
 <p><img src="https://static.oschina.net/uploads/space/2022/0907/082531_2cQs_2720166.gif" referrerpolicy="no-referrer"></p> 
</blockquote> 
<p><strong>主要变化</strong></p> 
<ul> 
 <li><strong>采用新的独立安装程序</strong></li> 
</ul> 
<p>旧版<code>get-poetry.py</code>安装脚本已替换为 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Finstall.python-poetry.org%2F" target="_blank">install.python-poetry.org</a>。安装程序现在是一个<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fpython-poetry%2Finstall.python-poetry.org" target="_blank">独立的项目</a>，有自己的问题跟踪器。</p> 
<p>新的安装程序包含以下改进：</p> 
<ul> 
 <li>从 standard wheels 安装发行版，而不是特定于平台的特殊档案。因此可支持<code>pipx</code>和手动安装，并防止发行版需要使用较新的依赖版本。</li> 
 <li>标准安装位置用于 Poetry 本身和<code>poetry</code>CLI 封装器。</li> 
 <li>支持从本地路径或 Git 仓库（包括分支或提交等引用）执行安装。</li> 
 <li>提供了修改指导<code>$PATH</code>，但用户的配置不会被自动化工具改变。</li> 
 <li>Poetry 将使用调用安装程序的 Python 解释器进行安装。</li> 
</ul> 
<pre><code># Linux, macOS, Windows (WSL)
$ curl -sSL https://install.python-poetry.org | python3 -

# Windows (Powershell)
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -</code></pre> 
<ul> 
 <li><strong>不再支持管理 Python 2.7 项目</strong></li> 
</ul> 
<p>Poetry 1.2 不再支持管理 Python 2.7 项目，原因包括：</p> 
<ul> 
 <li>它增加了技术债，并减缓了 Poetry 的发展。</li> 
 <li>项目有足够时间迁移到 Python 3。</li> 
</ul> 
<p>如果用户仍依赖 Poetry 管理 Python 2.7 项目，可继续使用 Poetry 1.1 分支，但官方将不再维护。</p> 
<ul> 
 <li><strong>不再支持将 Python 2.7, 3.5 和 3.6 作为运行时环境</strong></li> 
</ul> 
<p>Poetry 1.2 放弃了对 Python 2.7、3.5 和 3.6 的运行时环境支持。在这些版本上运行 Poetry 现在未经测试且不受支持。此更改是关于安装和运行 Poetry 本身，Poetry 仍然支持管理需要 Python 3.5 和 3.6 以及较旧的 Python 3 版本的项目。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fpython-poetry.org%2Fblog%2Fannouncing-poetry-1.2.0%2F" target="_blank">详情查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            