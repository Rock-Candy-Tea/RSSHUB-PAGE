
---
title: 'VS 显示方法引用的设置方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8526e20a81134662aaed0a11da43ca8b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 06:05:03 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8526e20a81134662aaed0a11da43ca8b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文已参与掘金创作者训练营第三期「高产更文」赛道，详情查看：<a href="https://juejin.cn/post/6994417198164869133" title="https://juejin.cn/post/6994417198164869133" target="_blank">掘力计划｜创作者训练营第三期正在进行，「写」出个人影响力。</a></p>
<h1 data-id="heading-0">前言</h1>
<blockquote>
<p>使用VS开发时，通过方法引用来查看此方法在哪里调用了，从而判断此调用逻辑是否正确。因此当没有方法引用时，不能通过简单的方式第一时间看到引用，总感觉心里不踏实。</p>
</blockquote>
<h1 data-id="heading-1">遇到问题</h1>
<p>新安装的  <strong>社区版</strong> VS，在Codelens目录下面，没有相关设置，如下图：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8526e20a81134662aaed0a11da43ca8b~tplv-k3u1fbpfcp-watermark.image" alt="1.2" loading="lazy" referrerpolicy="no-referrer">
正常情况下，没有引用按照“工具” -- “选项” -- “CodeLens” -- 显示引用，即可解决问题。可是我的“CodeLens” 面板上并没有相关设置。</p>
<hr>
<h1 data-id="heading-2">尝试解决：</h1>
<p>我以为是我少安装了哪个模块或者是少安装了哪个组件包，于是开始尝试可能和CodeLens面板相关的模块组件：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d64b23d9a6264c90be62b9e05d222c36~tplv-k3u1fbpfcp-watermark.image" alt="1.2" loading="lazy" referrerpolicy="no-referrer">
但是不管我安装了什么，重启后再次尝试查看CodeLens面板都没有进行改善。</p>
<hr>
<h1 data-id="heading-3">解决问题：</h1>
<p>下载<strong>专业版</strong>或者<strong>企业版</strong>：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00315317e58442629515018a14ae9663~tplv-k3u1fbpfcp-watermark.image" alt="1.4" loading="lazy" referrerpolicy="no-referrer">
安装后，新的CodeLens面板：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ac1ec67435a4c29ba0638200f8cc705~tplv-k3u1fbpfcp-watermark.image" alt="1.5" loading="lazy" referrerpolicy="no-referrer"></p>
<p>调试后的结果：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26a777893ebc4681a689af7d14045ca3~tplv-k3u1fbpfcp-watermark.image" alt="1.6" loading="lazy" referrerpolicy="no-referrer"></p>
<p>终于可以愉快的玩耍了。</p>
<p><strong>小结：</strong></p>
<ol>
<li>打开VS后，查看“工具” -- “选项” -- 在弹窗搜索“CodeLens”面板 -- 勾选显示引用方法即可。</li>
<li>打开"CodeLens"面板 若没有相关设置，确定下你的VS是否是社区版，社区版是没有此功能的。</li>
</ol>
<hr></div>  
</div>
            