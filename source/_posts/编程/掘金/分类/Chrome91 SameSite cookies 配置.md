
---
title: 'Chrome91 SameSite cookies 配置'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4110'
author: 掘金
comments: false
date: Thu, 03 Jun 2021 23:28:40 GMT
thumbnail: 'https://picsum.photos/400/300?random=4110'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>    因为开发环境需要, 我们把浏览器的<code>same-site-by-default-cookies</code>和<code>cookies-without-same-site-must-be-secure</code>两项都在flag里禁用了。但是更新到91版本后, Chromium直接把选项给关了（<a href="https://www.chromium.org/updates/same-site?pli=1#20210318" target="_blank" rel="nofollow noopener noreferrer">Chromium的更新日志</a>），而且设置成默认开启, 那就没办法在flag里设置了。</p>
<blockquote>
<p>The flags #same-site-by-default-cookies and #cookies-without-same-site-must-be-secure have been removed from chrome://flags as of Chrome 91, as the behavior is now enabled by default. In Chrome 94, the command-line flag --disable-features=SameSiteByDefaultCookies,CookiesWithoutSameSiteMustBeSecure will be removed.</p>
</blockquote>
<p>    也就是说我们可以通过命令行的形式在APP启动的时候作为启动参数传入：</p>
<ul>
<li>
<ol>
<li>（Windows）在右击Chrome/Edge的快捷方式, 点击"属性"。在"目标(Target)"属性中末尾加上<code>--flag-switches-begin --disable-features=SameSiteByDefaultCookies,CookiesWithoutSameSiteMustBeSecure --flag-switches-end</code>，然后重启浏览器。</li>
</ol>
</li>
<li>2.（Mac）通过脚本给浏览器添加启动参数</li>
<li>
<ul>
<li>2.1 新建一个文本（如<code>ChromeStart</code>）</li>
</ul>
</li>
<li>
<ul>
<li>2.2 然后编辑<code>ChromeStart</code>
<pre><code class="copyable">#!/bin/bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --args --disable-features=SameSiteByDefaultCookies,CookiesWithoutSameSiteMustBeSecure
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
<li>
<ul>
<li>2.3 给脚本添加执行权限
<pre><code class="copyable">sudo chmod u+x "ChromeStart"
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
<li>
<ul>
<li>2.4 关闭浏览器，执行脚本，就可以了</li>
</ul>
</li>
</ul>
<p>    但是这两种办法不是长久之计, Chromium 94后会连<code>comman-line</code>的方式也移除, 按照官方的说法是因为如果任由开发者禁用这两个选项, 开发者就会变成容易被攻击的目标。 因此为了保护开发者, Chromium选择逐渐关闭这个通道。</p>
<p><a href="https://www.jianshu.com/p/a8cc2c04ee7c" target="_blank" rel="nofollow noopener noreferrer">Mac Chrome添加启动参数</a></p></div>  
</div>
            