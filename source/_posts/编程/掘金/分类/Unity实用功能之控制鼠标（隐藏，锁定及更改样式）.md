
---
title: 'Unity实用功能之控制鼠标（隐藏，锁定及更改样式）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fcd27af6316e4c8784b0fc080a2ef951~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 11 Aug 2021 16:47:57 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fcd27af6316e4c8784b0fc080a2ef951~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第12天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">概述</h2>
<p>平时在开发过程中，为了程序美化，经常会需要隐藏鼠标，当需要点击的时候在显示出来，比如在游戏中的时候隐藏鼠标，打开背包后显示鼠标。或者是在程序中更改一个鼠标样式，是玩家能够更好的融入到游戏中。本片文章主要介绍一下如何隐藏与显示鼠标和在程序中更换鼠标样式。</p>
<h2 data-id="heading-1">鼠标显示与隐藏</h2>
<p>在Unity中，想要控制鼠标，我们需要使用到<code>Cursor</code>。我们直接通过设置<code>Cursor.visible</code>属性，即可达到鼠标的显示与隐藏<br>
状态：true显示，false隐藏</p>
<pre><code class="copyable">//隐藏鼠标
Cursor.visible = false;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">鼠标锁定</h2>
<p>通常隐藏鼠标之后，有的时候不知道鼠标在哪里，这就导致当需要显示鼠标的时候我们还要满屏幕寻找显示的鼠标。这时候就需要<code>Cursor.lockState</code>属性的配合,<code>Cursor.lockState</code>属性的作用是锁住鼠标，使其一直保持在屏幕中心。防止即使隐藏了鼠标，依然还会把鼠标移到游戏外面，和显示鼠标时还需要到处寻找鼠标的问题。让我们来看一下<code>Cursor.lockState</code>的属性都有哪些</p>
<ol>
<li>鼠标锁定并消失</li>
</ol>
<pre><code class="copyable">Cursor.lockState = CursorLockMode.Locked;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>鼠标解锁并显示</li>
</ol>
<pre><code class="copyable">Cursor.lockState = CursorLockMode.None;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>鼠标限定在Game视图中</li>
</ol>
<pre><code class="copyable">Cursor.lockState = CursorLockMode.Confined;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终实现结果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fcd27af6316e4c8784b0fc080a2ef951~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8aad37b46c434f5a9b67f9f5325cf0aa~tplv-k3u1fbpfcp-watermark.image" alt="45453424234.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">更改鼠标样式</h2>
<p>在Unity中修改鼠标样式方法有多中，一种是在Unity中设置，还有一种是通过代码修改。前提是都需要准备一张鼠标样式图片</p>
<h3 data-id="heading-4">方法一、通过设置修改鼠标样式</h3>
<p>此方法操作非常简单，而且修改完立刻生效，在Unity的Game视图中不论是否运行状态，都能够直接显示更改后的鼠标样式。<br>
首先导入需要使用的鼠标图片，每张图片导入进来后都会默认有一个Texture Type，一般为<code>Default</code>格式或<code>Sprite(2D and UI)</code> 格式，第一步需要做的是将图片格式修改为<code>Cursor</code>，切记修改完后要点击<code>Apply</code>.
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66af26aac1a2474489473b8a69d4a0d0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
如果不修改图片格式，修改完鼠标样式就有可能出现如下情况，显示不出来鼠标图片
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2fc2a67afd1a4968867257a74be6baef~tplv-k3u1fbpfcp-watermark.image" alt="454534242.gif" loading="lazy" referrerpolicy="no-referrer">
修改完鼠标鼠标图片格式，接下来就是修改鼠标样式了，在<code>Edit->Project Setting->Player->Default Cursor</code>中设置，将更改好的图片拖拽赋值到<code>Default Cursor</code>中即可，具体位置如图</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/668fa53e56c64dfb88a9536f17391c20~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
效果如下，此方法只会在Game视图发生变化，其他地方还是原来的样式。而且只需要更改这一个地方，很方便！</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb41c8344af94dffbba5f95965896c48~tplv-k3u1fbpfcp-watermark.image" alt="45453.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">方法二、通过代码修改鼠标样式</h3>
<p>上面的方法修改起来非常简单，但是实用性不太好，上述方法修改完后只能一直保持一种状态，无法实现多种状态切换，多以，接下来的方法正好能够完美的解决。
其核心代码只有一句话，就是调用<code>Cursor.SetCursor</code>,如下图</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5375add6626e44bea1c12f213e58bec1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
让我们来看一下此句代码的具体参数。</p>
<pre><code class="copyable">public static void SetCursor(Texture2D texture, Vector2 hotspot, CursorMode cursorMode);
<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>Texture2D texture：要替换的光标图片</li>
<li>Vector2 hotspot： 响应区域 (vector2.zero)</li>
<li>CursorMode cursorMode：渲染形式<br>
渲染形式共有两种:
<ol>
<li>
<pre><code class="copyable">Auto:平台自适应显示
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<pre><code class="copyable">ForceSoftware:强制使用软件游标
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
</li>
</ol>
<p>只要在想要修改鼠标样式的时候调用这一行代码，将里面的第一个参数赋值成我们想要的图片样式就好了！可以是鼠标进入一个状态，鼠标点击一个状态等等，就等着大家自由发挥了。。。</p>
<h2 data-id="heading-6">写在最后</h2>
<p>所有分享的内容均为作者在日常开发过程中使用过的各种小功能点，分享出来也变相的回顾一下，如有写的不好的地方还请多多指教。Demo源码会在之后整理好之后分享给大家。欢迎大家相互学习进步。</p></div>  
</div>
            