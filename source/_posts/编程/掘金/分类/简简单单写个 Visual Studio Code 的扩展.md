
---
title: '简简单单写个 Visual Studio Code 的扩展'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec261632788b4732ad69404ed4053858~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 21:35:07 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec261632788b4732ad69404ed4053858~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第 5 天，活动详情查看:<a href="https://juejin.cn/post/6967194882926444557?utm_campaign=30day&utm_medium=Ccenter&utm_source=20210528" target="_blank">更文挑战</a></p>
<p>今天我们来写一个 Visual Studio code 的扩展，不过这次写的相对简单。虽然简单，如果大家通过这次分享还是可以了解到如何写一个 Visual Studio Code 扩展的基本流程</p>
<h4 data-id="heading-0">搭建开发环境</h4>
<p>在开始 coding 之前，先需要做一些准备工作下载安装 <a href="https://yeoman.io/" target="_blank" rel="nofollow noopener noreferrer">yeoman</a></p>
<pre><code class="copyable">npm i -g yo
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以通过 npm 包管理工具全局安装 yeoman ，使用 yeoman 来创建一个项目，而且 yeoman 中提供了有许多好用预设模板供我们使用，从而避免了把过多时间浪费在搭建项目上。然后安装 generator-code 用于生产 visual studio 代码。</p>
<pre><code class="copyable">npm i -g generator-code
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-1">创建目录</h4>
<p>使用 yo 来创建一个 Visual Studio 扩展的项目</p>
<pre><code class="copyable">yo code
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后根据提示，本次我们选择简单扩展，该扩展只是为了创建代码段，类似输入名称生产代码。</p>
<pre><code class="copyable">? What type of extension do you want to create? New Code Snippets
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以选择 New Code Snippets</p>
<pre><code class="copyable">? Folder name for import or none for new: 
? What's the name of your extension? zisnippets
? What's the identifier of your extension? zisnippets
? What's the description of your extension? simple zi sinippets generator
<span class="copy-code-btn">复制代码</span></code></pre>
<p>根据提示我们一个一个根据项目实际回答出来</p>
<pre><code class="copyable">? Language id: html
<span class="copy-code-btn">复制代码</span></code></pre>
<p>语言我们选择 html，可以随着追加对其他语言的支持，表示我们定义 snippets 适用于该语言。</p>
<pre><code class="copyable">&#123;
    "name": "zisnippets",
    "displayName": "zisnippets",
    "description": "simple zi sinippets generator",
    "version": "0.0.1",
    "engines": &#123;
        "vscode": "^1.35.0"
    &#125;,
    "categories": [
        "Snippets"
    ],
    "contributes": &#123;
        "snippets": [
            &#123;
                "language": "html",
                "path": "./snippets/snippets.json"
            &#125;
        ]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 snippets/sinppets.json 文件中我们可以写自己</p>
<pre><code class="copyable">&#123;
    "Zi Started Template": &#123;
        "prefix": "zinav",
        "body": [
            "<div>",
            "\t<nav>",
            "\t\t$&#123;1:Title&#125;",
            "\t<\/nav>",
            "<div>"
        ],
        "description": "Creates zi nav"
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>prefix 表示我们在代码编辑器中输入 zinav 就会输出下面代码</li>
<li>$&#123;1:Title&#125; 表示占位符让用户进行输入，1 表示其 id 吧，可以按顺序进行定义。还有一些全局变量让我们使用文件名称、时间这些大家可以看相关帮助文档。</li>
</ul>
<p>好了差不多少，这么简单我们怎么好意发布呢，不过发布也不难，随后可以根据需要发布一个自己扩展。我们可以自己使用一些编写组件。</p>
<p>将项目文件夹复制到 visual studio code 的.vscode 下的 extension 文件夹下，然后重启项目就可以扩展目录最后看到我们定义扩展。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec261632788b4732ad69404ed4053858~tplv-k3u1fbpfcp-zoom-1.image" alt="扩展组件" loading="lazy" referrerpolicy="no-referrer"></p>
<p>测试一下，这里修改了 prefix 呵呵大家不要 confusing。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b03dcf59304848d3be3004988fc37847~tplv-k3u1fbpfcp-zoom-1.image" alt="测试" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b0883ac8fe7495f8feada6b5e2e1721~tplv-k3u1fbpfcp-zoom-1.image" alt="输入" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            