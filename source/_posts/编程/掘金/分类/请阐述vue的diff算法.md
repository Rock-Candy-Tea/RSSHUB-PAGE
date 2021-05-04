
---
title: '请阐述vue的diff算法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ace1690fb5ff40ce9233ce425c6e785a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 03 May 2021 20:53:13 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ace1690fb5ff40ce9233ce425c6e785a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><code>diff</code>是什么？<code>diff</code>就是比较两棵树，render会生成两颗树，一棵新树newVnode，一棵旧树oldVnode，然后两棵树进行对比更新找差异就是<code>diff</code>，全称<code>difference</code>，在vue里面 diff 算法是通过patch函数来完成的，所以有的时候也叫<code>patch算法</code></p>
<h2 data-id="heading-0">⏳ diff 发生的时机</h2>
<p><code>diff</code>发生在什么时候呢？当然我们可以说在数据更新的时候发生diff，因为数据更新会运行render函数得到虚拟dom树，最后页面重新渲染。</p>
<p>当组件创建的时候，组件所依赖的属性或者数据变化时，会运行一个函数 (下面代码中的<code>updateComponent</code>)，该函数会做两件事：</p>
<ul>
<li>运行<code>_render</code>生成一颗新的虚拟dom树（vnode tree）</li>
<li>运行<code>_updata</code>，传入_render生成的虚拟dom树的根节点，对新旧两棵树进行对比，最终完成对真实dom的更新</li>
</ul>
<p>核心代码如下，跟原代码有所差异，但都差不多，是这么个意思：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// vue构造函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Vue</span>(<span class="hljs-params"></span>)</span>&#123;
  <span class="hljs-comment">// ... 其他代码</span>
  <span class="hljs-keyword">var</span> updateComponent = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">this</span>._update(<span class="hljs-built_in">this</span>._render());
  &#125;
  <span class="hljs-keyword">new</span> Watcher(updateComponent);
  <span class="hljs-comment">// ... 其他代码</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong><code>diff</code>就发生在<code>_update</code>函数的运行过程中</strong></p>
<p>代码中先调用<code>_render</code>函数得到虚拟dom根节点，然后传入<code>_update</code>函数中，在将<code>updateComponent</code>传入<code>Watcher</code>中，watcher可以监听函数执行的过程，监测函数执行期间用到了哪些响应式数据并且进行依赖收集，关于watcher可以瞅瞅我上一篇文章：<a href="https://juejin.cn/post/6953172593067180040" target="_blank">一文带你了解vue2之响应式原理</a></p>
<h2 data-id="heading-1">🔨 _update函数在干什么？</h2>
<p><code>_update</code>函数会接收到一个<code>vonde</code>参数，这就是<strong>新</strong>生成的虚拟dom树，同时，_update函数通过当前组件的<code>_vnode属性</code>，拿到<strong>旧</strong>的虚拟dom树。_update函数首先会给组件的_vnode属性重新赋值，让它指向新树</p>
<p>简单用代码表示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">update</span>(<span class="hljs-params">vnode</span>)</span>&#123;
    <span class="hljs-comment">//vnode新树</span>
    <span class="hljs-comment">//this._vnode旧树</span>
    <span class="hljs-built_in">this</span>._vnode = vnode
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果只考虑更新虚拟dom树，这一步已经完成了，但是最终目的是要更新页面，所以就要用到diff进行树的节点对比，所以可以保存下旧树oldVnode用于对比</p>
<p>简单用代码表示：</p>
<pre><code class="hljs language-js copyable" lang="js"> <body>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
      <span class="hljs-keyword">const</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,
      &#125;);


      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">update</span>(<span class="hljs-params">vnode</span>) </span>&#123;
        <span class="hljs-comment">//vnode新树</span>
        <span class="hljs-comment">//this._vnode旧树</span>
        
        <span class="hljs-keyword">let</span> oldVnode = vm._vnode; <span class="hljs-comment">//保存旧树</span>
        
        <span class="hljs-built_in">this</span>._vnode = vnode; <span class="hljs-comment">//更新新树</span>
      &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
  </body>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对比<code>oldVnode</code>和<code>vnode</code>就行了，<strong>对比的目的就是更新真实dom</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ace1690fb5ff40ce9233ce425c6e785a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>接下来，会判断旧树oldVnode是否存在：</p>
<ul>
<li>不存在：说明这是第一次加载组件，于是通过内部的patch函数，直接遍历新树，为每个节点生成真实DOM，然后挂载到每个节点的<code>elm</code>属性上</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2040c051dc454aca80775380f5cac400~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>简单用代码表示：</p>
<pre><code class="hljs language-js copyable" lang="js"><body>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
      <span class="hljs-keyword">const</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
        <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,
      &#125;);
      <span class="hljs-built_in">console</span>.log(vm);

      <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">update</span>(<span class="hljs-params">vnode</span>) </span>&#123;
        <span class="hljs-comment">//vnode新树</span>
        <span class="hljs-comment">//this._vnode旧树</span>
        <span class="hljs-keyword">let</span> oldVnode = vm._vnode; <span class="hljs-comment">//保存旧树</span>
        <span class="hljs-built_in">this</span>._vnode = vnode; <span class="hljs-comment">//更新新树</span>

        <span class="hljs-comment">//如果旧树oldVnode不存在</span>
        <span class="hljs-keyword">if</span>(!oldVnode)&#123;
            <span class="hljs-built_in">this</span>.__patch__(vm.$el,vnode);
        &#125;
      &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
  </body>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>存在：说明之前已经渲染过该组件，于是通过内部的patch函数，对新旧两棵树进行对比，从而达到下面两个目标：</li>
</ul>
<ol>
<li>完成对所有真实dom的最小化处理</li>
<li>让新树的节点对应合适的真实dom</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91851217e9f24fe3abe8518fe6a4b0dd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">🙌 patch函数的对比流程</h2>
<h3 data-id="heading-3"><strong>术语解释：</strong> 一会看到以下字眼，均代表以下意思</h3>
<p>1.<strong>「相同」</strong>：是指两个虚拟节点的标签类型和key值均相同，但input元素还要看type属性。这个术语在vue源码中叫<code>sameVnode</code>，它是一个函数，用来判断两个虚拟节点是不是同一个节点</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9493d90d21ef4ec987f971bd2bf19527~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>例：两个虚拟节点div是否相同</p>
<pre><code class="hljs language-js copyable" lang="js"><div>法医</div>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>前端猎手<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>标签类型都为<code>div</code>，key值不仅仅在v-for遍历中，也可以用在任何标签中，上面两个div中没有key值，所以都为<code>undefined</code>，所以标签类型和key值都相同，不用看内容是否相同，它是另一个节点：<code>文本节点</code></p>
<pre><code class="hljs language-js copyable" lang="js"><div key=<span class="hljs-string">"fayi"</span>>法医</div>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">key</span>=<span class="hljs-string">"qdls"</span>></span>前端猎手<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面两个虚拟节点是不同的，因为key值不同</p>
<pre><code class="hljs language-js copyable" lang="js"> <input type=<span class="hljs-string">"text"</span>>
 <span class="xml"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"radio"</span>></span>
</span><span class="copy-code-btn">复制代码</span></code></pre>
<p>上面两个虚拟节点是不同的，因为input不仅仅要看key值和标签类型，还要看type是否相同</p>
<p>2.<strong>「新建元素」</strong>：是指根据一个虚拟节点提供的信息，创建一个真实dom元素，同时挂载到虚拟节点的elm属性上</p>
<p>3.<strong>「销毁元素」</strong>：是指：vnode.elm.remove()</p>
<p>4.<strong>「更新」</strong>：是指对两个虚拟节点进行对比更新，它仅发生在两个虚拟节点「相同」的情况下。具体过程稍后描述。</p>
<p>5.<strong>「对比子节点」</strong>：是指对两个虚拟节点的子节点进行对比，具体过程稍后描述</p>
<h3 data-id="heading-4">详细流程</h3>
<p><strong>根节点比较</strong></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6df11c96f2ce4c80865c99fb347570f9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>patch函数首先对根节点进行对比</p>
<p>如果两个节点：</p>
<ul>
<li><strong>「相同」</strong>，进入 <strong>「更新」</strong> 流程</li>
</ul>
<ol>
<li>将旧节点的真实dom赋值到新节点：<code>newVnode.elm = oldVnode.elem</code>，旧节点会被垃圾回收机制回收</li>
<li>对比新节点和旧节点的属性，有变化的更新到真实dom中</li>
<li>当前新旧两个节点处理完成，开始 <strong>「对比子节点」</strong></li>
</ol>
<ul>
<li>不 <strong>「相同」</strong></li>
</ul>
<ol>
<li>新节点<strong>递归</strong>， <strong>「新建元素」</strong></li>
<li>旧节点 <strong>「销毁元素」</strong></li>
</ol>
<p><strong>对比子节点</strong></p>
<p>虚拟dom树已经完成，就剩修改真实dom了，但是修改真实dom的效率是比较耗时的，vue的原则是能不改就不改，尽量啥也别做，在「对比子节点」时，vue一切的出发点，都是为了：</p>
<ul>
<li>
<p>尽量啥也别做</p>
</li>
<li>
<p>不行的话，尽量仅改动元素属性</p>
</li>
<li>
<p>还不行的话，尽量移动元素，而不是删除和创建元素</p>
</li>
<li>
<p>实在不行的话，删除和创建元素</p>
</li>
</ul>
<p><strong>对比流程：</strong></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff835b5ef5b4498da5e078bff47d56a8~tplv-k3u1fbpfcp-watermark.image" alt="未命名绘图.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>图片说明：</p>
<ul>
<li>黄色圆圈：表示旧子节点和新子节点所对应的相同节点类型</li>
<li>数字：表示key值，用来区分是不是同一个节点</li>
<li>蓝色方块：表示对比之前旧子节点所对应的真实dom</li>
<li>箭头：分别表示头指针和尾指针</li>
</ul>
<p>接下来，我们要做的就是对比<code>旧子节点</code>和<code>新子节点</code>之间的<code>差异</code>，目标是改变<code>真实dom</code>，并且将新虚拟子节点对应到真实dom里面去，vue使用两个指针分别指向新旧子节点树的头和尾</p>
<p>步骤：</p>
<ol>
<li>首先对比新树和旧树的头指针，瞅瞅两个节点是否一样，从图中可以看到是一样的，如果一样则进入 <strong>「更新」</strong> 流程：先将旧节点的真实dom赋值到新节点（真实dom连线到新子节点），然后循环对比新旧节点的属性，看看有没有不一样的地方，将有变化的更新到真实dom中，最后还要采用深度优先（一颗树的节点走到尽头，再走另一个节点）的方式递归循环这两个新旧子节点是否还有子节点，如果存在，则同理，这里我们就假设它不存子节点。<strong>灰色表示已经处理完成</strong>，然后两个头指针往后移动</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/37753595685049188c688ee601b5e2ff~tplv-k3u1fbpfcp-watermark.image" alt="未命名绘图.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>接下来，继续比较两个头指针，看看两个节点是否一样，很明显，两个节点是不一样的，因为key值不同，不一样的时候它不会销毁删除从建立，吃个🍗压压惊，淡定！前面有提到尽量别操作dom，它一定会找到一样的节点，一条道走到黑，然后会对比尾指针，可以看到尾指针是一样的，跟第一步是一样的：<strong>一顿操作猛如虎</strong>，先将旧节点的真实dom赋值到新节点（真实dom连线到新子节点），然后循环对比新旧节点的属性，将有变化的更新到真实dom中，接着还要递归循环这两个新旧子节点是否还有子节点，最后两个尾指针往前移动</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1805fc6f6a2f435790b59b1abe898ab5~tplv-k3u1fbpfcp-watermark.image" alt="未命名绘图.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>然后继续比较头指针，很明显不一样，尾指针呢？也不一样，因为key值还是不一样。随后它会比较头指针和尾指针，看看是否一样，可以看到旧节点的圆2头指针和新节点圆2尾指针是一样的，所以操作跟前两步是一样的，又是<strong>一顿操作猛如虎</strong>，结果如下图：</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0a5ceeda9924ec0a5a3d90e39f6c493~tplv-k3u1fbpfcp-watermark.image" alt="未命名绘图.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里我们要注意的是真实dom必须和新虚拟子节点要一一对应上的，所以除了更新变化的地方之外还要进行<code>位置移动</code>，移动到旧树尾指针的后面，最后旧树头指针往后移动，新树尾指针往前移动，如下图：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f05e947a9ce34657afb3e7bdcd200785~tplv-k3u1fbpfcp-watermark.image" alt="未命名绘图.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="4">
<li>继续比对，新旧头指针不同，尾指针不同，两个头尾也不同，然后它会以新树头指针为基准，循环旧虚拟子节点，看看新树圆3是否存在于旧虚拟子节点，存在的话在哪个位置，找到之后进行复用，连线，有变化的地方更新到真实dom，操作跟前面几步一样，真实dom也要进行<code>位置移动</code>，移动到旧树头指针之前。随后新树头指针继续往后移动到圆9位置，如下图:</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb0e4a86812a4ee6ab51747282e97392~tplv-k3u1fbpfcp-watermark.image" alt="未命名绘图.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="5">
<li>继续比对，新旧头指针不同，尾指针不同，但新树头指针和旧树尾指针相同，操作跟前面几步相同，但依然需要进行位置移动，移动到旧树头指针之前。随后新树头指针往后移动，与新树尾指针重合，旧树尾指针向前移动到圆1位置，如下图：</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9901f73cbdc74a87bd1c726886e45811~tplv-k3u1fbpfcp-watermark.image" alt="未命名绘图.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="6">
<li>继续比对，新旧两树头指针不同，尾指针不同，两个头尾也不同，然后它以新树头指针为基准，循环旧虚拟子节点，找圆8在旧树中存不存在，从图中可以看出，并不存在，这个时候确实没办法了，只能 <strong>「新建元素」</strong>。随后新树头指针继续向后移动到圆2位置，如图：</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38ca38587d044d63bcdf9840bbd9c9e6~tplv-k3u1fbpfcp-watermark.image" alt="未命名绘图.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="7">
<li>当头指针移动到圆2位置时，头指针已经不再是有效的了，当头指针超过尾指针的时候，循环结束，从过程我们可以看到新树先循环完成，但是旧树还有剩余的节点，这说明旧树中剩余的节点都是应该被删除的节点，所对应的真实dom也会被移除</li>
</ol>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0e8eac600a842b88d1ffcf5f59ac63e~tplv-k3u1fbpfcp-watermark.image" alt="未命名绘图.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>最终真实dom生成完毕，整个过程我们只新建了一个元素，如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/122fa1bd87e94225aefe3ed6300a2645~tplv-k3u1fbpfcp-watermark.image" alt="未命名绘图.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在面试的时候也会被问到关于diff算法的问题，以下是参考回答：</p>
<pre><code class="copyable">当组件创建和更新时，vue会执行内部的update函数，该函数使用render函数生成的虚拟dom树，将新旧两树进行对比，找到差异点，最终更新到真实dom

对比差异的过程叫diff，vue在内部通过一个叫patch的函数完成该过程

在对比时，vue采用深度优先、同级比较的方式进行比对。同级比较就是说它不会跨越结构进行比较

在判断两个节点是否相同时，vue是通过虚拟节点的key和tag来进行判断的

具体来说，首先对根节点进行对比，如果相同则将旧节点关联的真实dom的引用挂到新节点上，然后根据需要更新属性到真实dom，然后再对比其子节点数组；如果不相同，则按照新节点的信息递归创建所有真实dom，同时挂到对应虚拟节点上，然后移除掉旧的dom。

在对比其子节点数组时，vue对每个子节点数组使用了两个指针，分别指向头尾，然后不断向中间靠拢来进行对比，这样做的目的是尽量复用真实dom，尽量少的销毁和创建真实dom。如果发现相同，则进入和根节点一样的对比流程，如果发现不同，则移动真实dom到合适的位置。

这样一直递归的遍历下去，直到整棵树完成对比。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>😊 好了， 以上就是我的分享，大家对于<code>diff算法</code>还有其它理解的话可以在评论区讨论鸭～</p>
<p>希望小伙伴们点赞 👍 支持一下哦～ 😘，我会更有动力的 🤞</p></div>  
</div>
            