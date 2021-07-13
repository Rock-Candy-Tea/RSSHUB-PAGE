
---
title: 'github中创建仓库步骤'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/488400877fea48bcab5c848381068ed3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 12 Jul 2021 02:32:57 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/488400877fea48bcab5c848381068ed3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>纯小白，部门大神操作了仓库搭建步骤，怕记不住，写下来以备查看~~~</p>
<h2 data-id="heading-0">1.向仓库中添加已有的项目</h2>
<p>步骤：</p>
<h4 data-id="heading-1">1.在GitHub中创建新的仓库</h4>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/488400877fea48bcab5c848381068ed3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1de13f4d7e39438588eb05e82192dc8e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-2">2.用vscode(任何一个编程工具都可以)打开已有项目，对应输入以下命令行语句（当前用第二种）</h4>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b30b912a070b4762b68f906c4f836cb4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">注意：容易出现的一些报错：</h3>
<ol>
<li>输入最后一句后报错：</li>
</ol>
<pre><code class="copyable">git remote add origin**************
fatal: remote origin already exists.
（报错远程起源已经存在。）
<span class="copy-code-btn">复制代码</span></code></pre>
<p>网上解决办法：</p>
<pre><code class="copyable">1、先输入 git remote rm origin
2、再输入 git remote add origin **************
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.请求超时：</p>
<pre><code class="copyable">git push -u origin main
fatal: unable to access '**************': Failed to connect to github.com port 443: Timed out
<span class="copy-code-btn">复制代码</span></code></pre>
<p>等一会再试吧~~~</p>
<p>后续遇到问题再补充~~~</p>
<h2 data-id="heading-4">2.向仓库中添加一个全新的项目（啥也没有）</h2>
<p>步骤：</p>
<h4 data-id="heading-5">1.在GitHub中创建新的仓库（一样的操作不赘述了）</h4>
<h4 data-id="heading-6">2.一个项目总的有个文件夹吧，新建一个文件夹</h4>
<h4 data-id="heading-7">3.用vscode打开这个文件夹</h4>
<h4 data-id="heading-8">4.依次输入对应命令行语句（第一种）</h4>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b30b912a070b4762b68f906c4f836cb4~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d7110121f11c41beaa625d24d7ec5bf3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
完美！小白又学会了一个新东西，期待打开GitHub的大门</p>
<h3 data-id="heading-9">补充一个贼6的操作 搬运自：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fgbz3300255%2Farticle%2Fdetails%2F97103621%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/gbz3300255/article/details/97103621/" ref="nofollow noopener noreferrer">csdn</a></h3>
<p>解决了在GitHub经常clone代码不成功的问题</p>
<pre><code class="copyable">git clone 遇到问题：fatal: unable to access 'https://github.comxxxxxxxxxxx': Failed to connect to xxxxxxxxxxxxx

将命令行里的http改为git重新执行。
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            