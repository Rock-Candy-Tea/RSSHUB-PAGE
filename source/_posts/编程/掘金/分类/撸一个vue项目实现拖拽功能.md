
---
title: '撸一个vue项目实现拖拽功能'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/653a3786b9a14245bf6896a41282f551~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 10 Jun 2021 23:32:40 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/653a3786b9a14245bf6896a41282f551~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>最近在学习Vue，边做个小demo边学习。其中有一个小功能需要使用到拖放，顺便还学一下拖放。拖放是HTML5的标准，对着教程在普通的页面上很容易就实现了，但是vue中基本都是数据驱动，不推荐直接操作DOM。</p>
<h3 data-id="heading-0">内置HTML 拖放API</h3>
<p>HTML拖放API 是一种内置方法，它包含几个事件和属性，但是可以归纳为以两种类型的元素为思路来进行处理。</p>
<ul>
<li>可拖动元素：可以被拖动的元素</li>
<li>可放置元素：可以接受被拖动元素的元素</li>
</ul>
<p>如果这样分析，将会使分析拖放事件变得更加容易。</p>
<h3 data-id="heading-1">拖放事件</h3>
<p>API 中有八个拖放事件可以用在我们程序中。</p>
<ul>
<li>drag：可拖动的项目被拖动</li>
<li>dragstart：开始拖动可拖动元素</li>
<li>dragend：拖动结束（例如放开鼠标）</li>
<li>dragenter ：拖动的项目进入可放置元素</li>
<li>dragleave –可拖动的项目离开可放置元素</li>
<li>dragover：可拖动项目在可放置元素上移动（每一百毫秒左右调用一次）</li>
<li>drop：可拖动项目被放置在可放置元素上</li>
</ul>
<p><strong>dataTransfer对象</strong></p>
<p>关于拖放 API 最重要的一个知识点时它将 dataTransfer对象添加到事件中。</p>
<p>dataTransfer 对象允许我们在开始拖动元素时设置数据，并在将元素放在拖放区中时访问相同的数据。
我们应该知道一些关于 dataTransfer 的属性和方法（如果要了解更多，请查看dataTransfer API 文档）。</p>
<ul>
<li>dropEffect：当前的拖放操作（例如，移动，复制）</li>
<li>effectAllowed：指定拖放操作</li>
<li>setData（name，val）：允许我们向dataTransfer对象添加值</li>
<li>getData（name）：检索存储的值</li>
</ul>
<h3 data-id="heading-2">创建自己的拖放系统</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/653a3786b9a14245bf6896a41282f551~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
如你所见例子中有两个列表，我们可以在它们之间顺畅地拖放项目。</p>
<p><strong>配置我们的项目</strong></p>
<p>首先，我们必须设置数据。在脚本中，创建一个 item 对象数组，对象的属性有：</p>
<ul>
<li>id：唯一的 ID，以便我们可以查找对象</li>
<li>title：要显示文字</li>
<li>list：它所属的列表。</li>
</ul>
<p>这个数组中添加三项：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">data () &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">items</span>: [
      &#123;
        <span class="hljs-attr">id</span>: <span class="hljs-number">0</span>,
        <span class="hljs-attr">title</span>: <span class="hljs-string">'Item A'</span>,
        <span class="hljs-attr">list</span>: <span class="hljs-number">1</span>
      &#125;,
      &#123;
        <span class="hljs-attr">id</span>: <span class="hljs-number">1</span>,
        <span class="hljs-attr">title</span>: <span class="hljs-string">'Item B'</span>,
        <span class="hljs-attr">list</span>: <span class="hljs-number">1</span>
      &#125;,
      &#123;
        <span class="hljs-attr">id</span>: <span class="hljs-number">2</span>,
        <span class="hljs-attr">title</span>: <span class="hljs-string">'Item C'</span>,
        <span class="hljs-attr">list</span>: <span class="hljs-number">2</span>
      &#125;]
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>另外还创建了两个计算属性用来把项目列表过滤为列表1中的项目和列表2中的项目。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">computed: &#123;
    listOne () &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.items.filter(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.list === <span class="hljs-number">1</span>)
    &#125;,
    listTwo () &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.items.filter(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.list === <span class="hljs-number">2</span>)
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>创建的模板代码</strong></p>
<p>这是组件的轮廓。该代码将显示所有内容，但没有拖放功能。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'drop-zone'</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">'item in listOne'</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">'item.title'</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'drag-el'</span>></span>
        &#123;&#123; item.title &#125;&#125;
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'drop-zone'</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">'item in listTwo'</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">'item.title'</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'drag-el'</span>></span>
        &#123;&#123; item.title &#125;&#125;
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/efe7ed117b5f473aa56e6cb70ad9446b~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
组件的样式并不重要。重要的是，即使没有内部元素，你的放置区也必须具有一定的高度，否则，你无法将鼠标悬停在上面！</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><style scoped>
  .drop-zone &#123;
    background-color: #eee;
    margin-bottom: 10px;
    padding: 10px;
  &#125;
 
  .drag-el &#123;
    background-color: #fff;
    margin-bottom: 10px;
    padding: 5px;
  &#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过在拖放区样式中添加一些填充来实现。</p>
<p><strong>添加拖放功能</strong></p>
<p>首先在脚本中添加一些方法：一种在开始拖动元素时使用，另一种在拖放元素时使用。</p>
<p>对于 startDrag 方法，我们想使用前面讨论的 dataTransfer 属性存储要拖动的元素的 ID。另外这个拖动事件将是一个动作。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">startDrag: <span class="hljs-function">(<span class="hljs-params">evt, item</span>) =></span> &#123;
      evt.dataTransfer.dropEffect = <span class="hljs-string">'move'</span>
      evt.dataTransfer.effectAllowed = <span class="hljs-string">'move'</span>
      evt.dataTransfer.setData(<span class="hljs-string">'itemID'</span>, item.id)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在 ondrop 中检索存储的 ID，以便我们可以访问数组中正确的项目。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">onDrop (evt, list) &#123;
      <span class="hljs-keyword">const</span> itemID = evt.dataTransfer.getData(<span class="hljs-string">'itemID'</span>)
      <span class="hljs-keyword">const</span> item = <span class="hljs-built_in">this</span>.items.find(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.id == itemID)
      item.list = list
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面添加模板代码。
首先向事件添加事件。需要使元素可拖动并检测拖动开始事件。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span>
        <span class="hljs-attr">class</span>=<span class="hljs-string">'drag-el'</span>
        <span class="hljs-attr">v-for</span>=<span class="hljs-string">'item in listTwo'</span>
        <span class="hljs-attr">:key</span>=<span class="hljs-string">'item.title'</span>
        <span class="hljs-attr">draggable</span>
        @<span class="hljs-attr">dragstart</span>=<span class="hljs-string">'startDrag($event, item)'</span>
 ></span>
        &#123;&#123; item.title &#125;&#125;
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于添加了 draggable 属性，所以，如果你运行程序，应该可以像这样拖动元素，但是无法将其拖放到任何地方。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0765a4b20754c308d4544e15f5fa9a3~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
让我们给它一个接受可拖动元素的放置区域。先添加调用 onDrop 方法的 drop 事件侦听器。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span>
      <span class="hljs-attr">class</span>=<span class="hljs-string">'drop-zone'</span>
      @<span class="hljs-attr">drop</span>=<span class="hljs-string">'onDrop($event, 1)'</span>
></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是要注意，我们必须在 dragEnter 和 dragOver 这两个拖放 hooks 上调用 preventDefault。</p>
<p>因为在默认情况下，这两种方法不允许删除元素。所以为了使我们的 drop 事件能够正常运行，必须阻止其默认操作才行。</p>
<p>可以用 Vue 内置的 .prevent 事件修改器来完成此操作。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span>
      <span class="hljs-attr">class</span>=<span class="hljs-string">'drop-zone'</span>
      @<span class="hljs-attr">drop</span>=<span class="hljs-string">'onDrop($event, 1)'</span>
      @<span class="hljs-attr">dragover.prevent</span>
      @<span class="hljs-attr">dragenter.prevent</span>
></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在运行程序，可以看到一切正常。我们能够在两个不同的列表之间拖放元素。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10d02d14ec7c4581b158f4fd0e573ec0~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">最后求点个赞或者给个🌟🌟</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37e3a4cd0b4a4e2481bec4c5ee985803~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            