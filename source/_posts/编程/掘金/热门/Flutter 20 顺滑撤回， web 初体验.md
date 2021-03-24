
---
title: 'Flutter 2.0 顺滑撤回， web 初体验'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://picsum.photos/400/300?random=8644'
author: 掘金
comments: false
date: Wed, 03 Mar 2021 19:15:27 GMT
thumbnail: 'https://picsum.photos/400/300?random=8644'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>Flutter 2.0 今早发布，web 开发现已在 stable channel 支持了，非常激动！</p>
<blockquote>
<p>Flutter 2.0 的更新说明</p>
<ul>
<li><a href="https://flutter.dev/docs/development/tools/sdk/release-notes/release-notes-2.0.0" target="_blank" rel="nofollow noopener noreferrer">release-notes-2.0.0</a></li>
<li><a href="https://medium.com/flutter/whats-new-in-flutter-2-0-fe8e95ecc65" target="_blank" rel="nofollow noopener noreferrer">What’s New in Flutter 2</a></li>
<li><a href="https://juejin.cn/post/6935520179262586917" target="_blank">Flutter 2.0 发布 | 针对 Web，移动端和桌面端构建的下一代 Flutter</a></li>
</ul>
</blockquote>
<p>因本人的特殊性，对 Flutter 有多个版本的需求。比如：</p>
<ul>
<li>混合开发，需要在 1.17.5 的 Flutter 版本</li>
<li>旧版 web 开发，需要在 beta 的 channel 下开发</li>
<li>纯 Flutter 项目，跟随 stable channel</li>
</ul>
<p>为了能够在各个项目中开发，我需要快速切换 Flutter 环境。所以我采用 <a href="https://github.com/leoafarias/fvm" target="_blank" rel="nofollow noopener noreferrer">fvm</a> 这个工具。</p>
<p>如果你不知道如何使用 FVM，可以直接参考项目的使用文档，或者参考上一篇：<a href="https://juejin.cn/post/6919469825547272205" target="_blank">《FVM 愉快的切换 Flutter 版本，强烈推荐！》</a></p>
<p>如果你是 FVM 的使用老手，那么下面的内容可以忽略了。</p>
<h2 data-id="heading-0">实战</h2>
<p>假设在 Flutter 2.0 之前， 有这么个 flt_demo 项目：</p>
<ul>
<li>使用了 FVM</li>
<li>指定了 Flutter 的版本为 stable</li>
</ul>
<h3 data-id="heading-1">基于最新的 stable channel 创建 web 工程</h3>
<p>创建个新项目 web_demo，且需要用 Flutter 2.0 进行 web 开发:</p>
<pre><code class="hljs language-sh copyable" lang="sh">$ mkdir web_demo
$ <span class="hljs-built_in">cd</span> web_demo
$ fvm use stable --force 
$ fvm flutter create .
$ fvm flutter doctor
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后我们获取到的还是 1.22.6 的 Flutter 版本。</p>
<p>需要更新到最新的 stable 版本：</p>
<pre><code class="hljs language-sh copyable" lang="sh">$ fvm flutter upgrade
$ fvm flutter doctor
<span class="copy-code-btn">复制代码</span></code></pre>
<p>👌🏻，web_demo 的 Flutter 环境已经完成，可以愉快的玩耍了。</p>
<h3 data-id="heading-2">解救基于旧版 stable channel 开发的 fltDemo 工程</h3>
<p>由于 flt_demo 也是在 stable channel 进行开发，当我们重新运行项目的时候，会报一些错误(某些 api 被废弃了，一些第三方库报错)。</p>
<p>现有的 stable channel 是 Flutter 2.0 版本，但是对 flt_demo 来说，在 Flutter 2.0 是无法运行的。所以我们需要旧版的 stable 环境。</p>
<p>可以通过以下命令获取 flutter 已发布的版本号。</p>
<pre><code class="hljs language-sh copyable" lang="sh">$ fvm releases
<span class="copy-code-btn">复制代码</span></code></pre>
<p>旧版的 stable channel 对应的是 1.22.6 的版本。</p>
<p>所以我们需要修改 fltDemo 的 flutter 环境为 1.22.6。</p>
<pre><code class="hljs language-sh copyable" lang="sh">$ <span class="hljs-built_in">cd</span> flt_demo
$ fvm install 1.22.6
$ fvm use 1.22.6 --force
$ fvm flutter doctor
<span class="copy-code-btn">复制代码</span></code></pre>
<p>👌🏻，完成 flt_demo 的 flutter 环境指定。</p>
<p>如果 flt_demo 是团队项目，提交你的修改。同事拉取代码后，在项目根路径下执行</p>
<pre><code class="hljs language-sh copyable" lang="sh">$ fvm install
<span class="copy-code-btn">复制代码</span></code></pre>
<p>即可。</p>
<p>可以继续愉快的玩耍了。</p>
<blockquote>
<p>Flutter2.0 for web，现已完成一个博客站点：</p>
<ul>
<li>源码：<a href="https://github.com/swiftdo/web-demo" target="_blank" rel="nofollow noopener noreferrer">swiftdo/web-demo</a></li>
<li>站点：<a href="http://webdemo.loveli.site/" target="_blank" rel="nofollow noopener noreferrer">webdemo.loveli.site</a></li>
<li>文章: <a href="https://juejin.cn/post/6940962419355156494" target="_blank">Flutter2 for Web，写了个博客站点，已上线</a></li>
</ul>
</blockquote>
<p>更多干货阅读，请关注官方微信公众号: <strong>OldBirds</strong></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            