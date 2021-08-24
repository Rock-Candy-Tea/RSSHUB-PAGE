
---
title: '我用index作为key也没啥问题啊'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b05353952abf4b08bb2f7fe3953ef765~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 01:52:00 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b05353952abf4b08bb2f7fe3953ef765~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>所有熟悉 <code>Vue</code> 技术栈的小伙伴，都知道在列表渲染的场景下，不能使用 <code>index</code> 或 <code>random</code> 作为 <code>key</code>。</p>
<p>也有很多小伙伴在面试的时候会被面试官比较详细的追问，假如使用 <code>index</code> 作为 <code>key</code> 会有什么问题？假如使用 <code>random</code> 作为 <code>key</code> 会有什么问题？假如使用一个唯一不变的 <code>id</code> 作为 <code>key</code> 有什么好处呢？</p>
<p>这道题目，表面上看起来是考察我们对同级比较过程中 <code>diff</code> 算法的理解，唯一不变的 <code>key</code> 可以帮助我们更快的找到可复用的 <code>VNode</code>，节省性能开销，使用 <code>index</code> 作为 <code>key</code> 有可能造成 <code>VNode</code> 错误的复用，从而产生 <code>bug</code> ，而使用 <code>random</code> 作为 <code>key</code> 会导致<code>VNode</code> 始终无法复用，极大的影响性能。</p>
<p>这么回答有问题么？没有问题。</p>
<p>但是假如这道题目满分100，我只能给你99分。</p>
<p>还有 <code>1分</code>，涉及到 <code>Vue</code> <code>更新流程</code>中的一点点细节，若不理清，可能在实际的业务场景中给我们造成困扰。</p>
<p>啥困扰呢？</p>
<h2 data-id="heading-1">举个栗子</h2>
<p>直奔主题，看一段代码，<code>index</code> 作为 <code>key</code> ，假如我们删除某一条，结果会是啥呢？</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"(item, index) in data"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"index"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Child</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"handleDelete(index)"</span>></span>删除这一行<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
​
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
​
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"App"</span>,
  <span class="hljs-attr">components</span>: &#123;
    <span class="hljs-attr">Child</span>: &#123;
      <span class="hljs-attr">template</span>: <span class="hljs-string">'<span>&#123;&#123;name&#125;&#125;&#123;&#123;Math.floor(Math.random() * 1000)&#125;&#125;</span>'</span>,
      <span class="hljs-attr">props</span>: [<span class="hljs-string">'name'</span>]
    &#125;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">data</span>: [
        &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"小明"</span> &#125;,
        &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"小红"</span> &#125;,
        &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"小蓝"</span> &#125;,
        &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">"小紫"</span> &#125;,
      ]
    &#125;;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">handleDelete</span>(<span class="hljs-params">index</span>)</span> &#123;
      <span class="hljs-built_in">this</span>.data.splice(index, <span class="hljs-number">1</span>);
    &#125;,
  &#125;
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看结果</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b05353952abf4b08bb2f7fe3953ef765~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以观察到，虽然我们删除的不是最后一条，但最终却是最后一条被删除了，看起来很奇怪，但是假如你了解过 <code>Vue</code> 的 <code>diff</code> 流程，这个结果应该是可以符合你的预期的。</p>
<h2 data-id="heading-2">diff</h2>
<p>大段的列源码，会增加我们的理解负担，所以我把 <code>Vue</code> 的<code>更新流程</code>简化成一张图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc6584989d934b57ba795f1904122ef1~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>通常来讲，我们说 <code>Vue</code> 的 <code>diff</code> 流程，指的就是 <code>patchVnode</code> ，其中 <code>updateChildren</code> 就是我们说的同层比较，其实就是比较新旧两个 <code>Vnode</code> 数组。</p>
<p><code>Vue</code> 会声明四个指针变量，分别记录新旧 <code>Vnode</code> 数组的首尾索引，通过首尾索引指针的移动，根据新头旧头、新尾旧尾、旧头新尾、旧尾新头的顺序，依次比较新旧 <code>Vnode</code> ，若不能命中 <code>sameVnode</code>，则将<code>oldVnode.key</code> 维护成一个 <code>map</code>， 继续查询是否包含<code>newVnode.key</code> ，若命中 <code>sameVnode</code> ，则递归执行 <code>patchVnode</code>。若最终无法命中，说明无可复用的 <code>Vnode</code> ，创建新的 <code>dom</code> 节点。</p>
<p>若 <code>newVnode</code> 的首尾指针先相遇，说明 <code>newVnode</code> 已经遍历完成，直接移除 <code>oldVnode</code> 多余部分，若 <code>oldVnode</code> 的首尾指针先相遇，说明 <code>oldVnode</code> 已经遍历完成，直接新增 <code>newVnode</code> 的多余部分。</p>
<p>这种直接的文字描述会显得比较苍白，所以我给大家准备了个<code>动画</code>：</p>
<p><strong>第一步：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c5db07d0927446b9901f294623889dfd~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>第二步：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad3bfcf084ce4bfcaf75df69d259f06a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>第三步：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea8441123b354370bd806490a9c3aef1~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>第四步：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e56928fef6454837b982e160aa45043e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>第五步：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3936f9fe75cb4512a8ba4999d59fbf55~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>第六步：</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/051246de339440b0a00502f61cb3fc3f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>理论上，只要你滑动的足够快，这几张图就可以动起来😊</p>
<blockquote>
<p>上面描述updateChildren过程的图片均摘自 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fustbhuangyi.github.io%2Fvue-analysis%2Fv2%2Freactive%2Fcomponent-update.html%23updatechildren" target="_blank" rel="nofollow noopener noreferrer" title="https://ustbhuangyi.github.io/vue-analysis/v2/reactive/component-update.html#updatechildren" ref="nofollow noopener noreferrer">Vue技术揭秘</a> <strong>组件更新</strong>章节，建议大家翻阅原文</p>
<p>我尝试了半天实在做不出来动画，同时感觉这几张图已经可以带给我们足够直观的感受了，所以直接搬运了</p>
<p><strong>侵删</strong>。</p>
</blockquote>
<h2 data-id="heading-3">使用 <code>index</code> 作为 <code>key</code> 会有什么问题</h2>
<p>上面我们讲，判断新旧 <code>Vnode</code> 是否可以复用，取决于 <code>sameNode</code> 方法，这个方法非常简单，就是比对 <code>Vnode</code> 的部分属性，其中 <code>key</code> 是最关键的因素</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sameVnode</span> (<span class="hljs-params">a, b</span>) </span>&#123;
    <span class="hljs-keyword">return</span> (
      a.key === b.key &&
      a.asyncFactory === b.asyncFactory && (
        (
          a.tag === b.tag &&
          a.isComment === b.isComment &&
          isDef(a.data) === isDef(b.data) &&
          sameInputType(a, b)
        ) || (
          isTrue(a.isAsyncPlaceholder) &&
          isUndef(b.asyncFactory.error)
        )
      )
    )
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们再回到上面的栗子，看看是哪里出了问题</p>
<p>上面代码生成的 <code>VNode</code> 大约是这样的：</p>
<pre><code class="hljs language-js copyable" lang="js">[
  &#123;
    <span class="hljs-attr">tag</span>: <span class="hljs-string">'div'</span>,
    <span class="hljs-attr">key</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">children</span>: [
      &#123;
        <span class="hljs-attr">tag</span>: VueComponent, 
        <span class="hljs-attr">elm</span>: <span class="hljs-number">408</span>, <span class="hljs-comment">// 这个Vnode对应的真实dom是408</span>
      &#125;,
      &#123;
        <span class="hljs-attr">tag</span>: <span class="hljs-string">'button'</span>
      &#125;
    ]
  &#125;,
  &#123;
    <span class="hljs-attr">tag</span>: <span class="hljs-string">'div'</span>,
    <span class="hljs-attr">key</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">children</span>: [
      &#123;
        <span class="hljs-attr">tag</span>: VueComponent,
        <span class="hljs-attr">elm</span>: <span class="hljs-number">227</span>, <span class="hljs-comment">// 这个Vnode对应的真实dom是227</span>
      &#125;,
      &#123;
        <span class="hljs-attr">tag</span>: <span class="hljs-string">'button'</span>
      &#125;
    ]
  &#125;
  ...
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们删除第一条数据，新的 <code>VNode</code> 大约是这样的：</p>
<pre><code class="hljs language-js copyable" lang="js">[
  &#123;
    <span class="hljs-attr">tag</span>: <span class="hljs-string">'div'</span>,
    <span class="hljs-attr">key</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">children</span>: [
      &#123;
        <span class="hljs-attr">tag</span>: VueComponent,
        <span class="hljs-attr">elm</span>: <span class="hljs-number">227</span>, <span class="hljs-comment">// 这个Vnode对应的真实dom是227</span>
      &#125;,
      &#123;
        <span class="hljs-attr">tag</span>: <span class="hljs-string">'button'</span>
      &#125;
    ]
  &#125;,
  &#123;
    <span class="hljs-attr">tag</span>: <span class="hljs-string">'div'</span>,
    <span class="hljs-attr">key</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">children</span>: [
      &#123;
        <span class="hljs-attr">tag</span>: VueComponent,
        <span class="hljs-attr">elm</span>: <span class="hljs-number">324</span>, <span class="hljs-comment">// 这个Vnode对应的真实dom是324</span>
      &#125;,
      &#123;
        <span class="hljs-attr">tag</span>: <span class="hljs-string">'button'</span>
      &#125;
    ]
  &#125;
  ...
]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们<strong>人肉逻辑</strong> 一下这两个 <code>Vnode</code> 数组，由于 <code>key</code> 都是0，所以比较第一条的时候，就会命中 <strong>sameNode</strong> ，导致错误复用，然后 <code>updateChildren</code> ，子节点的 <code>Vnode</code> 依然会命中 <code>sameVnode</code> ，同理，第二、三条均会命中 <code>sameVnode</code> ，而直接错误复用其关联的真实 <code>dom</code> 节点，所以我们明明删除的是第一条，UI表现却是最后一条被删除了。</p>
<p><strong>那么到这里就结束了么？</strong></p>
<p><strong>当然没有，因为很多小伙伴在刚接触 <code>Vue</code> 的时候，也用过 <code>index</code> 作为 <code>key</code> ，部分牛逼的项目甚至已经上线了，似乎也没人来找麻烦</strong></p>
<p><strong>why？</strong></p>
<h2 data-id="heading-4">为什么我用 <code>index</code> 作为 <code>key</code> 没出现问题</h2>
<p>如果我把代码改成这样，再删除某一条，会是什么结果呢？</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"(item, index) in data"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"index"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Child</span> <span class="hljs-attr">:name</span>=<span class="hljs-string">"`$&#123;item.name&#125;`"</span> /></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"handleDelete(index)"</span>></span>删除这一行<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看结果</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f40b1fcda21f483e88cd525445aecedd~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>法克，我们明明把 <code>Vue</code> 的<code>更新流程</code>捋清楚了，用 <code>index</code> 作为 <code>key</code> 会导致 <code>Vnode</code> 错误复用啊，怎么这里表现却正常了呢？</p>
<p>我们再看一下<code>更新流程</code>简化图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/233515332b65424e93bbfa44669e8f9b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>组件类型的 <code>Vnode</code> ，在 <code>patchVnode</code> 的过程中会执行 <code>prePatch</code> 钩子函数，给组件的 <code>propsData</code> 重新赋值，从而触发 <code>setter</code> ，假如 <code>propsData</code> 的值有变化，则会触发 <code>update</code> ，重新渲染组件</p>
<p>我们可以再<strong>人肉逻辑</strong> 一下，这次我们删除的是第二条，因为<code>key</code> 一致，新的 <code>Vnode</code> 数组依然会复用旧的 <code>Vnode</code> 数组的前三条，第一条 <code>Vnode</code> 是正确复用，组件的 <code>propsData</code> 未发生变化，不会触发 <code>update</code> ，直接复用其关联的真实 <code>dom</code> 节点，但是第二条 <code>Vnode</code> 是错误复用，但是组件的 <code>propsData</code> 发生变化，由小红变成了小蓝，触发了 <code>update</code> ，组件重新渲染，因此我们看到其实连 <code>random</code> 都发生了变化，第三条同理。</p>
<p>呼~</p>
<p>到这里，总算是搞明白了，我可真是个小机灵鬼</p>
<p><strong>那么到这里就结束了么？</strong></p>
<p><strong>其实还没有，比如我们再改一下代码</strong></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"(item, index) in data"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"index"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;&#123;item.name&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"handleDelete(index)"</span>></span>删除这一行<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看结果</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75b21fe4b0fe46f3a814f9292584bd91~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这次我们没有组件类型 <code>Vnode</code> ，不会执行 <code>prePatch</code>，为啥表现还是正常的呢？</p>
<p>再观察一下上面的<code>更新流程</code>图，文本类型的 <code>Vnode</code> ，新旧文本不同的时候是会直接覆盖的。</p>
<p>到这里，我们已经完全明白，列表渲染的场景下，为什么推荐使用唯一不变的 <code>id</code> 作为 <code>key</code>了。抛开代码规范不谈，即使某些场景下，问题并未以 <code>bug</code> 的形式暴露出来，但是不能复用、或者错误复用 <code>Vnode</code> ，都会导致组件重新渲染，这部分的性能包袱还是非常沉重的！</p>
<h2 data-id="heading-5">最后的1分</h2>
<p><strong>纸上得来终觉浅，绝知此事要躬行</strong></p>
<p>我第一次读完 <code>Vue2</code> 源码的时候，以为自己已经清晰的明白了这部分知识，直到团队里的小伙伴拿着一个纯文本类型的列表来质问我</p>
<p>不得已仔细 <code>debug</code> 了一遍<code>更新流程</code>，才算解开了心中疑惑，补上了这 <code>1分</code> 的缺口</p>
<p>引用如下：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/vuejs/vue" ref="nofollow noopener noreferrer">Vue2源码</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fustbhuangyi.github.io%2Fvue-analysis%2Fv2%2Fprepare%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://ustbhuangyi.github.io/vue-analysis/v2/prepare/" ref="nofollow noopener noreferrer">Vue技术揭秘</a></p></div>  
</div>
            