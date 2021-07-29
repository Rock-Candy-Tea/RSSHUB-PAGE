
---
title: 'Webstorm中配置Microsoft Edge启动'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b199597073044e4c9e04f54bb2ea669c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 02:39:57 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b199597073044e4c9e04f54bb2ea669c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>在Webstorm中<code>.html</code>文件的默认启动方式中没有microsoft edge，本文解决了这个问题，增加了edge的快捷启动选项。</p>
<h2 data-id="heading-1">方式</h2>
<p>打开preference/settings（windows）找到Tools -> Web Browsers</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b199597073044e4c9e04f54bb2ea669c~tplv-k3u1fbpfcp-watermark.image" alt="image-20210728183443700.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>添加新的一栏，按照图上配置。</p>
<ul>
<li>mac系统在后面填上</li>
</ul>
<pre><code class="copyable">/Applications/Microsoft Edge.app
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>windows系统在后面填上你的默认安装路径(也可以尝试直接填上microsoft-edge，我不行，有人可以)</li>
</ul>
<pre><code class="copyable">//示例 具体要看你的安装位置
C:\Program Files(x86)\Microsoft\Edge...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>再看文件，默认选项已经被加上了：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d49c2c410f87498c85252d0ed3f2ee89~tplv-k3u1fbpfcp-watermark.image" alt="image-20210728183824158.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>没有Edge的图标有点让人沮丧。</p>
<p>以上。</p>
<h2 data-id="heading-2">参考文档</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F66615483%2Fwebstorm-cant-find-browser-when-hitting-run" target="_blank" rel="nofollow noopener noreferrer" title="https://stackoverflow.com/questions/66615483/webstorm-cant-find-browser-when-hitting-run" ref="nofollow noopener noreferrer">jetbrains ide - WebStorm can't find browser when hitting 'Run' - Stack Overflow</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWEB-19564" target="_blank" rel="nofollow noopener noreferrer" title="https://youtrack.jetbrains.com/issue/WEB-19564" ref="nofollow noopener noreferrer">Web Browsers: support Microsoft Edge browser : WEB-19564 (jetbrains.com)</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fyoutrack.jetbrains.com%2Fissue%2FWEB-45326" target="_blank" rel="nofollow noopener noreferrer" title="https://youtrack.jetbrains.com/issue/WEB-45326" ref="nofollow noopener noreferrer">Chromium-based browsers Edge and Opera are assigned to non-Chrome family in "Settings → Tools → Web Browsers" window : WEB-45326 (jetbrains.com)</a></li>
</ul></div>  
</div>
            