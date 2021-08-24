
---
title: 'Vue中的钩子函数'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a6295622c404d08906e317c2c9f750b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 23:03:44 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a6295622c404d08906e317c2c9f750b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第24
天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<p>每个Vue实例在被<strong>创建</strong>之前都要经过一系列的初始化过程,这个过程就是vue的生命周期，同时在这个过程中也会运行一些叫做<strong>生命周期钩子</strong>的函数，这给了用户在不同阶段添加自己的代码的机会。也就是说在你的页面被渲染出来之前，vue会在特定的时期来调用一些特殊的函数</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a6295622c404d08906e317c2c9f750b~tplv-k3u1fbpfcp-watermark.image" alt="生命周期.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-0">1.钩子函数</h3>
<p>那我们先来看一下有哪些钩子函数，不同的钩子函数会在不同的时候被调用，比如 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fapi%2F%23created" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/v2/api/#created" ref="nofollow noopener noreferrer"><code>created</code></a> 钩子可以用来在一个实例被创建之后执行代码，</p>
<p><strong>开始创建</strong></p>
<ul>
<li><strong>beforeCreate</strong></li>
</ul>
<p><strong>已经创建</strong></p>
<ul>
<li><strong>created</strong></li>
</ul>
<p><strong>虚拟dom替换真实dom</strong></p>
<ul>
<li><strong>beforeMount</strong></li>
</ul>
<blockquote>
<p><strong>该钩子在服务器端渲染期间不被调用，因为只有初次渲染会在服务端进行。</strong></p>
</blockquote>
<ul>
<li><strong>mounted</strong></li>
</ul>
<p><strong>更新状态</strong></p>
<ul>
<li><strong>beforeUpdate</strong></li>
<li><strong>updated</strong></li>
</ul>
<p><strong>销毁vue实例</strong></p>
<ul>
<li><strong>beforeDestroy</strong></li>
<li><strong>destroyed</strong></li>
</ul>
<h3 data-id="heading-1">2.常用的生命周期方法</h3>
<p>1.mounted(): 发送 ajax 请求, 启动定时器等异步任务</p>
<p>2.beforeDestory(): 做收尾工作, 如: 清除定时器</p>
<h3 data-id="heading-2">3.演示</h3>
<pre><code class="hljs language-html copyable" lang="html">    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        &#123;&#123;data&#125;&#125;
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>:<span class="hljs-string">"#app"</span>,
        <span class="hljs-attr">data</span>:&#123;
            <span class="hljs-attr">data</span>:<span class="hljs-string">"best"</span>,
            <span class="hljs-attr">name</span>:<span class="hljs-string">"badspider"</span>
        &#125;,
        <span class="hljs-attr">beforeCreate</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"创建前"</span>)
            <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.data)
            <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$el)
        &#125;,
        <span class="hljs-attr">created</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"已创建"</span>)
            <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
            <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$el)
        &#125;,
        <span class="hljs-attr">beforeMount</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"挂载之前"</span>)
            <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
            <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$el)
        &#125;,
        <span class="hljs-attr">mounted</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"挂载"</span>)
            <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
            <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$el)
        &#125;,
        <span class="hljs-attr">beforeUpdate</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"更新前"</span>);

        &#125;,
        <span class="hljs-attr">updated</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"更新完成"</span>);
        &#125;,
        <span class="hljs-attr">beforeDestroy</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"销毁前"</span>)
            <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
            <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$el)
        &#125;,
        <span class="hljs-attr">destroyed</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"已销毁"</span>)
            <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.name)
            <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.$el)
        &#125;
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69a5cc013cf34f24925d69e04fe1adb5~tplv-k3u1fbpfcp-watermark.image" alt="QQ截图20210824145429.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">其他的三个钩子函数</h3>
<ul>
<li>actived ------- 被 keep-alive 缓存的组件激活时调用。</li>
</ul>
<blockquote>
<p><strong>该钩子在服务器端渲染期间不被调用。</strong></p>
</blockquote>
<ul>
<li>deactivated ---------被 keep-alive 缓存的组件停用时调用。</li>
<li>errorCaptured ------当捕获一个来自后代组件的错误时被调用</li>
</ul>
<p>可能现在看还是有点懵，但是在你之后的使用中，你会慢慢的认识到这些函数的强大</p></div>  
</div>
            