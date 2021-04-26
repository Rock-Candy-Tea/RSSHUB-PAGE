
---
title: '前端初学者读滴滴Dokit小程序源代码（三）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1687082a396741f8a36ff6794db139ea~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 23 Apr 2021 08:23:47 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1687082a396741f8a36ff6794db139ea~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>第二篇文章里我们简要介绍了微信小程序的一些特色语法，如条件渲染、数据绑定、事件通信等功能；并介绍了index组件如何通过事件通信的方式切换成其他的组件。<br>
接下来我们就要看看其他的Dokit功能组件了，我们先来看主菜单组件debug组件。</p>
<h1 data-id="heading-0">debug组件：组件菜单</h1>
<h2 data-id="heading-1">index组件中渲染debug组件</h2>
<p>回顾一下上次阅读的index组件代码，在第一次加载index界面的时候，index中的data属性里的<code>curCom</code>值为dokit，因此条件渲染的是以下代码：</p>
<pre><code class="hljs language-html copyable" lang="html">    <span class="hljs-tag"><<span class="hljs-name">cover-image</span>
        <span class="hljs-attr">bindtap</span>=<span class="hljs-string">"tooggleComponent"</span>
        <span class="hljs-attr">data-type</span>=<span class="hljs-string">"debug"</span>
        <span class="hljs-attr">class</span>=<span class="hljs-string">"dokit-entrance"</span>
        <span class="hljs-attr">src</span>=<span class="hljs-string">"//pt-starimg.didistatic.com/static/starimg/img/W8OeOO6Pue1561556055823.png"</span>
    ></span><span class="hljs-tag"></<span class="hljs-name">cover-image</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>1、响应点击事件 2、事件处理函数为toggleComponent 3、传递dataset中属性为type的值<code>"debug"</code><br>
在事件处理函数toggleComponent中，将<code>curCom</code>的值赋值为debug字符串;这样,通过下面的条件渲染语句，index组件中渲染了debug组件：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">block</span> <span class="hljs-attr">wx:if</span>=<span class="hljs-string">"&#123;&#123; curCom!= 'dokit' &#125;&#125;"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">debug</span> <span class="hljs-attr">wx:if</span>=<span class="hljs-string">"&#123;&#123; curCom === 'debug' &#125;&#125;"</span> <span class="hljs-attr">bindtoggle</span>=<span class="hljs-string">"tooggleComponent"</span>></span><span class="hljs-tag"></<span class="hljs-name">debug</span>></span>
    ......
<span class="hljs-tag"></<span class="hljs-name">block</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">debug组件功能展示</h2>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1687082a396741f8a36ff6794db139ea~tplv-k3u1fbpfcp-watermark.image" alt="bebug.png" loading="lazy" referrerpolicy="no-referrer"><br>
可以看到，组件中罗列了Dokit可使用的功能，点击不同的图标即可使用不同的功能。<br>
debug组件作为Dokit功能展示的菜单，其代码实现比较简单，这部分需要注意的有两个部分：wxml的<strong>列表渲染</strong>与<strong>更新版本</strong>的这一功能，我们先来看列表渲染功能。</p>
<h2 data-id="heading-3">列表渲染</h2>
<p>列表渲染是微信小程序wxml中的一个特色功能，通过<code>wx:for</code>语法来遍历一个绑定好的数组，用数组内的元素渲染同一个组件；可以嵌套使用该语法，debug的菜单各个组件就是嵌套渲染的：</p>
<pre><code class="hljs language-html copyable" lang="html">    <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">wx:for</span>=<span class="hljs-string">"&#123;&#123;tools&#125;&#125;"</span> <span class="hljs-attr">wx:key</span>=<span class="hljs-string">"index"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"debug-collections card"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"debug-collections-title"</span>></span>&#123;&#123;item.title&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">view</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"debug-collections-main"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">view</span> <span class="hljs-attr">wx:for</span>=<span class="hljs-string">"&#123;&#123;item.tools&#125;&#125;"</span>
              <span class="hljs-attr">wx:for-index</span>=<span class="hljs-string">"idx"</span>
              <span class="hljs-attr">wx:for-item</span>=<span class="hljs-string">"tool"</span>
              <span class="hljs-attr">wx:key</span>=<span class="hljs-string">"idx"</span>
              <span class="hljs-attr">data-type</span>=<span class="hljs-string">"&#123;&#123;tool.type&#125;&#125;"</span>
              <span class="hljs-attr">bindtap</span>=<span class="hljs-string">"onToggle"</span>
              <span class="hljs-attr">class</span>=<span class="hljs-string">"card-item"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">image</span>
              <span class="hljs-attr">class</span>=<span class="hljs-string">"debug-item-image"</span>
              <span class="hljs-attr">src</span>=<span class="hljs-string">"&#123;&#123;tool.image&#125;&#125;"</span>
          ></span><span class="hljs-tag"></<span class="hljs-name">image</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">text</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"debug-text"</span>></span>&#123;&#123;tool.title&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">text</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">view</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">view</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">view</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>具体内外层的渲染组件如图：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/195263b182004f8f948360bf65dd053d~tplv-k3u1fbpfcp-watermark.image" alt="嵌套列表渲染.png" loading="lazy" referrerpolicy="no-referrer"><br>
红框是外层列表渲染的组件：标题为常用工具的卡片，蓝框是内层列表渲染的组件，七个功能组件入口。<br>
我们很快就注意到一个情况：<strong>外层</strong>列表渲染<strong>只渲染了一个卡片</strong>，这种情况下真的有必要使用列表渲染吗？<br>
这个问题的答案可以通过Dokit其他应用端的工具列表得到提示：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b81a6f9345934304a7f6fcd85c58d87e~tplv-k3u1fbpfcp-watermark.image" alt="可扩展性.png" loading="lazy" referrerpolicy="no-referrer"><br>
可以看到其他应用端的工具列表不止包括常用工具、还包括性能监控等常用工具。<br>
因此，考虑到日后Dokit工具的<strong>可拓展性</strong>，外层卡片使用列表渲染的原因也得到了解释：便于日后添加其他方向的功能。</p>
<h2 data-id="heading-4">更新版本</h2>
<p>通过上面的代码我们可以看到，各个功能的入口都绑定了响应函数为<code>onToggle</code>的点击事件。而该响应函数的代码如下：</p>
<pre><code class="hljs language-js copyable" lang="js">        onToggle (event) &#123;
            <span class="hljs-keyword">const</span> type = event.currentTarget.dataset.type;
            <span class="hljs-keyword">if</span>(type === <span class="hljs-string">'onUpdate'</span>) &#123;
                <span class="hljs-built_in">this</span>[type]();
            &#125; <span class="hljs-keyword">else</span> &#123;
                <span class="hljs-built_in">this</span>.triggerEvent(<span class="hljs-string">'toggle'</span>, &#123; <span class="hljs-attr">componentType</span>: type &#125;)
            &#125;
        &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>函数内检查当前组件的type是否为<code>onUpdate</code>，如果是onUpdate，那么执行函数<code>onUpdate()</code>，不然就触发toggle事件。<br>
除了更新版本的组件外，其他的组件入口都是触发toggle事件进行组件切换，与index组件的组件切换方式是相同的，所以我们可以集中注意力在更新版本这个功能上。</p>
<pre><code class="hljs language-js copyable" lang="js">        onUpdate () &#123;
            <span class="hljs-keyword">const</span> updateManager = wx.getUpdateManager();
            updateManager.onCheckForUpdate(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">res</span>) </span>&#123;
                <span class="hljs-keyword">if</span>(!res.hasUpdate) &#123;
                    <span class="hljs-comment">// 请求完新版本信息的回调</span>
                    wx.showModal(&#123;
                        <span class="hljs-attr">title</span>: <span class="hljs-string">'更新提示'</span>,
                        <span class="hljs-attr">content</span>: <span class="hljs-string">'当前已经是最新版本'</span>
                    &#125;)
                &#125;
            &#125;);
            updateManager.onUpdateReady(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                wx.showModal(&#123;
                    <span class="hljs-attr">title</span>: <span class="hljs-string">'更新提示'</span>,
                    <span class="hljs-attr">content</span>: <span class="hljs-string">'新版本已经准备好，是否重启应用？'</span>,
                    <span class="hljs-function"><span class="hljs-title">success</span>(<span class="hljs-params">res</span>)</span> &#123;
                        <span class="hljs-keyword">if</span> (res.confirm) &#123;
                            <span class="hljs-comment">// 新的版本已经下载好，调用 applyUpdate 应用新版本并重启</span>
                            updateManager.applyUpdate()
                        &#125;
                    &#125;
                &#125;)
            &#125;);
            updateManager.onUpdateFailed(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                <span class="hljs-comment">// 新版本下载失败</span>
            &#125;)
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个函数中的内容比较容易理解，通过调用微信提供的接口函数得到版本更新管理器<code>UpdateManager</code>对象，之后调用</p>
<ol>
<li><code>onCheckForUpdate</code>函数检查更新结果</li>
<li><code>onUpdateReady</code>函数，在有版本更新的情况下会触发下载新版本</li>
<li><code>applyUpdate</code>函数强制小程序重启并使用新版本</li>
<li><code>onUpdateFailed</code>函数监听小程序更新失败的情况执行相应回调函数</li>
</ol>
<h1 data-id="heading-5">总结</h1>
<p>继上一篇我们了解了数据绑定、事件通信、条件渲染系统后，我们这次了解了微信小程序的列表渲染功能。到目前为止，我们已具备了阅读Dokit小程序端源代码的基础小程序知识。<br>
从下一篇开始我们将从另一个角度来阅读Dokit源代码：了解Dokit业务代码零侵入的思想。</p></div>  
</div>
            