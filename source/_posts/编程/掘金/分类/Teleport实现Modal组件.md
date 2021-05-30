
---
title: 'Teleport实现Modal组件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61ee8c5c53b0493cb5365b14fa4b35d1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 29 May 2021 22:50:13 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61ee8c5c53b0493cb5365b14fa4b35d1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1.认识Teleport</h1>
<p><a href="https://v3.cn.vuejs.org/guide/teleport.html" target="_blank" rel="nofollow noopener noreferrer">vue3新增特性Teleport</a></p>
<blockquote>
<p>Teleport 提供了一种干净的方法，允许我们控制在 DOM 中哪个父节点下渲染了 HTML，而不必求助于全局状态或将其拆分为两个组件。</p>
</blockquote>
<p>像我们如果写Modal组件、Message组件、Loading组件这种全局式组件，没有Teleport的话，将它们引入一个.vue文件中，则他们的HTML结构会被添加到组件模板中，这是不够完美的。</p>
<ul>
<li>没有Teleport</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61ee8c5c53b0493cb5365b14fa4b35d1~tplv-k3u1fbpfcp-watermark.image" alt="1622354766953.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>有Teleport</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79a11b9ea3034b17a6a518fdc21f76c9~tplv-k3u1fbpfcp-watermark.image" alt="WX20210530-140832@2x.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>下面就实战介绍一下如何用Teleport开发Modal组件</p>
<h1 data-id="heading-1">2.Teleport的基本用法</h1>
<p>Teleport的写法十分简单，只需要用<code><Teleport></Teleport></code>将内容包裹，并用<code>to</code>指定将HTML挂到哪个父节点下，就可以啦。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">teleport</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"#modal"</span>></span>
内容
<span class="hljs-tag"></<span class="hljs-name">teleport</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">3.第一步优化</h1>
<p>如果我们在代码中将Teleport要挂载的DOM写死，那么每创建一个全局式组件，就需要有一个DOM节点，会越来越多，并且一直存在，这样的写法不是很优雅。比较好的解决方案就是：</p>
<ul>
<li>在创建组件的时候，动态创建一个dom节点<code>document.createElement()</code>，</li>
<li>并添加到body中，<code>document.body.appendChild()</code>，</li>
<li>在组件卸载的时候销毁这个dom <code>document.body.removeChild()</code>，</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-keyword">const</span> node = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'div'</span>)
  node.id = <span class="hljs-string">'modal'</span>
  <span class="hljs-built_in">document</span>.body.appendChild(node)
  onUnmounted(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">document</span>.body.removeChild(node)
  &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">4.第二步优化</h1>
<p>如果我们后续还要添加Message组件，Loading组件等功能，同样要用到Teleport，在每一个组件内部都写这么一段代码，实在有点冗余，vue3使我们能够很方便的将逻辑功能提取出来，从而达到逻辑复用的目的。</p>
<p>我们在src-hooks文件夹下创建<code>useDOMCreate.ts</code>文件，来封装这一块逻辑</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// hooks/useDOMCreate.ts</span>
<span class="hljs-keyword">import</span> &#123; onUnmounted &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">useDOMCreate</span>(<span class="hljs-params">nodeId:<span class="hljs-built_in">string</span></span>):<span class="hljs-title">void</span> </span>&#123;
  <span class="hljs-keyword">const</span> node = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'div'</span>)
  node.id = nodeId
  <span class="hljs-built_in">document</span>.body.appendChild(node)
  onUnmounted(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">document</span>.body.removeChild(node)
  &#125;)
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> useDOMCreate

<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> useDOMCreate <span class="hljs-keyword">from</span> <span class="hljs-string">'../hooks/useDOMCreate'</span>
<span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props, ctx</span>)</span> &#123;
    useDOMCreate(<span class="hljs-string">'modal'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">5.实现Modal组件</h1>
<p>具体封装Modal组件的细节这里就不讲啦，也没有什么复杂的逻辑。直接上代码。</p>
<pre><code class="hljs language-html copyable" lang="html">//Modal.vue
<span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">teleport</span> <span class="hljs-attr">to</span>=<span class="hljs-string">"#modal"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"modal d-block"</span> <span class="hljs-attr">tabindex</span>=<span class="hljs-string">"-1"</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">"isVisible"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"modal-dialog"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"modal-content"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"modal-header"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h5</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"modal-title"</span>></span>&#123;&#123;title&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">h5</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"close"</span> <span class="hljs-attr">data-dismiss</span>=<span class="hljs-string">"modal"</span> <span class="hljs-attr">aria-label</span>=<span class="hljs-string">"Close"</span>></span>
              <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">aria-hidden</span>=<span class="hljs-string">"true"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"onClose"</span>></span><span class="hljs-symbol">&times;</span><span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"modal-body"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">slot</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"modal-footer"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn btn-secondary"</span> <span class="hljs-attr">data-dismiss</span>=<span class="hljs-string">"modal"</span>  @<span class="hljs-attr">click</span>=<span class="hljs-string">"onClose"</span>></span>取消<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn btn-primary"</span>  @<span class="hljs-attr">click</span>=<span class="hljs-string">"onConfirm"</span>></span>确定<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
          <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">teleport</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; defineComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> useDOMCreate <span class="hljs-keyword">from</span> <span class="hljs-string">'../hooks/useDOMCreate'</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'Modal'</span>,
  <span class="hljs-attr">emits</span>: [<span class="hljs-string">'model-close'</span>, <span class="hljs-string">'model-confirm'</span>],
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">title</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-string">''</span>
    &#125;,
    <span class="hljs-attr">isVisible</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">Boolean</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-literal">false</span>
    &#125;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props, ctx</span>)</span> &#123;
    useDOMCreate(<span class="hljs-string">'modal'</span>)
    <span class="hljs-keyword">const</span> onClose = <span class="hljs-function">() =></span> &#123;
      ctx.emit(<span class="hljs-string">'model-close'</span>)
    &#125;
    <span class="hljs-keyword">const</span> onConfirm = <span class="hljs-function">() =></span> &#123;
      ctx.emit(<span class="hljs-string">'model-confirm'</span>)
    &#125;
    <span class="hljs-keyword">return</span> &#123;
      onClose,
      onConfirm
    &#125;
  &#125;
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用示例</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"post-detail-page"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"btn btn-danger"</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"handleDelete"</span>></span>删除<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">modal</span> <span class="hljs-attr">title</span>=<span class="hljs-string">'是否确认删除？'</span> <span class="hljs-attr">:isVisible</span>=<span class="hljs-string">"modalVisible"</span> @<span class="hljs-attr">model-close</span>=<span class="hljs-string">"hanldeModalClose"</span> @<span class="hljs-attr">model-confirm</span>=<span class="hljs-string">"handleModalConfim"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span>确认要删除这篇文章吗？<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">modal</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"ts"</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; defineComponent, ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>
<span class="hljs-keyword">import</span> Modal <span class="hljs-keyword">from</span> <span class="hljs-string">'../components/Modal.vue'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'post-detail'</span>,
  <span class="hljs-attr">components</span>: &#123; Modal &#125;,
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">const</span> modalVisible = ref(<span class="hljs-literal">false</span>)
    <span class="hljs-keyword">const</span> handleDelete = <span class="hljs-function">() =></span> &#123;
      modalVisible.value = <span class="hljs-literal">true</span>
    &#125;
    <span class="hljs-keyword">const</span> hanldeModalClose = <span class="hljs-function">() =></span> &#123;
      modalVisible.value = <span class="hljs-literal">false</span>
    &#125;
    <span class="hljs-keyword">const</span> handleModalConfim = <span class="hljs-function">() =></span> &#123;
      modalVisible.value = <span class="hljs-literal">false</span>
      ...
     / /后续逻辑处理
    &#125;
    <span class="hljs-keyword">return</span> &#123;
      hanldeModalClose,
      handleModalConfim,
      handleDelete,
      modalVisible
    &#125;
  &#125;
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">6.git地址</h1>
<p>后续添加</p></div>  
</div>
            