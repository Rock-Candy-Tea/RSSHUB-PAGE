
---
title: '虚拟DOM和diff算法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d05fa9f6a1d47739861373915b50a25~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 20 Aug 2021 00:44:39 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d05fa9f6a1d47739861373915b50a25~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">虚拟 DOM 和 diff 算法</h1>
<p>虚拟 DOM 和 diff 算法其实对于大家并不陌生，不管我们开发中使用的什么框架，其实都离不开虚拟 DOM 和 diff。</p>
<p>当有人问你：你了解虚拟 DOM 和 diff 算法吗？ 我相信，大部分人其实都能说出一点相关知识。但是，请各位亲们扪心自问，你真的懂虚拟 DOM 和 diff 算法吗？</p>
<p>本次分享将带大家一起探索虚拟 DOM 和 diff 算法的奥秘。我们将通过代码演示以及手写相关实现代码来一起打开 diff 算法的神秘面纱。核心代码每一行都安排得明明白白，由简入深，循序渐进，让大家都能听懂，干货满满！</p>
<h2 data-id="heading-1">一、简单认识虚拟 DOM 和 diff 算法</h2>
<p>虚拟 DOM：用 js 对象形式描述真实 DOM</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>我是一个标题<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>java<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>php<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>python<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
  <span class="hljs-string">"sel"</span>: <span class="hljs-string">"div"</span>,
  <span class="hljs-string">"data"</span>: &#123; <span class="hljs-string">"class"</span>: &#123; <span class="hljs-string">"box"</span>: <span class="hljs-literal">true</span> &#125; &#125;,
  <span class="hljs-string">"children"</span>: [
    &#123;
      <span class="hljs-string">"sel"</span>: <span class="hljs-string">"h3"</span>,
      <span class="hljs-string">"data"</span>: &#123;&#125;,
      <span class="hljs-string">"text"</span>: <span class="hljs-string">"我是一个标题"</span>,
    &#125;,
    &#123;
      <span class="hljs-string">"sel"</span>: <span class="hljs-string">"ul"</span>,
      <span class="hljs-string">"data"</span>: &#123;&#125;,
      <span class="hljs-string">"children"</span>: [
        &#123; <span class="hljs-string">"sel"</span>: <span class="hljs-string">"li"</span>, <span class="hljs-string">"data"</span>: &#123;&#125;, <span class="hljs-string">"text"</span>: <span class="hljs-string">"java"</span> &#125;,
        &#123; <span class="hljs-string">"sel"</span>: <span class="hljs-string">"li"</span>, <span class="hljs-string">"data"</span>: &#123;&#125;, <span class="hljs-string">"text"</span>: <span class="hljs-string">"php"</span> &#125;,
        &#123; <span class="hljs-string">"sel"</span>: <span class="hljs-string">"li"</span>, <span class="hljs-string">"data"</span>: &#123;&#125;, <span class="hljs-string">"text"</span>: <span class="hljs-string">"python"</span> &#125;,
      ],
    &#125;,
  ],
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>diff: 最小量更新</p>
<p>变为</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">h3</span>></span>我是一个标题<span class="hljs-tag"></<span class="hljs-name">h3</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">span</span>></span>我是一个新的span<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>java<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>php<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>python<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>javascript<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种场景在实际开发中经常出现，那么 diff 算法怎么做处理的呢？有人说，直接拆掉整个 DOM，然后重新上树，计算机是很快的嘛 ~ 但是，涉及到比较庞大的 DOM 结构时，还是会有很多性能问题。就好比你要在家里客厅放一个桌子，你总不可能把家拆了重新装修吧。</p>
<p>我们来看 DOM 结构，其实就是多了一个 span，多了一个 li，其余东西并没有发生任何变化，diff 算法的核心就在于
<code>进行精细化比较，实现最小量更新</code>。</p>
<h2 data-id="heading-2">二、snabbdom</h2>
<ul>
<li>snabbdom 简介</li>
<li>snabbdom 的 h 函数如何工作</li>
<li>感受diff 算法</li>
</ul>
<h3 data-id="heading-3">2.1 snabbdom 简介</h3>
<p>snabbdom 是瑞典语单词，单词原意“速度”</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d05fa9f6a1d47739861373915b50a25~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>snabbdom 是著名的虚拟 DOM 库，是 diff 算法的鼻祖，Vue 源码借鉴了 snabbdom</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fsnabbdom%2Fsnabbdom" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/snabbdom/snabbdom" ref="nofollow noopener noreferrer">snabbdom github 地址</a></p>
<h4 data-id="heading-4">2.1.1 搭建 snabbdom 环境</h4>
<p>1.用<code>npm init</code>构建项目即可<br>
2.安装以下几个包 <code>snabbdom</code>、<code>webpack</code>、<code>webpack-cli</code>、<code>webpack-dev-server</code><br></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-string">"dependencies"</span>: &#123;
<span class="hljs-string">"snabbdom"</span>: <span class="hljs-string">"^3.0.3"</span>,
<span class="hljs-string">"webpack"</span>: <span class="hljs-string">"^5.48.0"</span>,
<span class="hljs-string">"webpack-cli"</span>: <span class="hljs-string">"^3.3.12"</span>,
<span class="hljs-string">"webpack-dev-server"</span>: <span class="hljs-string">"^3.11.2"</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.新建<code>src/index.js</code><br>
4.新建<code>www/index.html</code><br></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span> /></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span> /></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span> /></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"container"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"xuni/bundle.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>5.创建<code>webpack.config.js</code></p>
<pre><code class="copyable">```javascript
module.exports = &#123;
  entry: "./src/index.js",
  output: &#123;
    publicPath: "xuni",
    filename: "bundle.js",
  &#125;,
  devServer: &#123;
    port: 9999,
    contentBase: "www",
  &#125;,
&#125;;
```
<span class="copy-code-btn">复制代码</span></code></pre>
<p>复制github上的demo代码到index.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123;
  init,
  classModule,
  propsModule,
  styleModule,
  eventListenersModule,
  h,
&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"snabbdom"</span>;

<span class="hljs-keyword">const</span> patch = init([
  <span class="hljs-comment">// Init patch function with chosen modules</span>
  classModule, <span class="hljs-comment">// makes it easy to toggle classes</span>
  propsModule, <span class="hljs-comment">// for setting properties on DOM elements</span>
  styleModule, <span class="hljs-comment">// handles styling on elements with support for animations</span>
  eventListenersModule, <span class="hljs-comment">// attaches event listeners</span>
]);

<span class="hljs-keyword">const</span> container = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"container"</span>);

<span class="hljs-keyword">const</span> someFn = <span class="hljs-function">() =></span> &#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">1</span>)
&#125;

<span class="hljs-keyword">const</span> vnode = h(<span class="hljs-string">"div#container.two.classes"</span>, &#123;
  <span class="hljs-attr">on</span>: &#123;
    <span class="hljs-attr">click</span>: someFn
  &#125;
&#125;, [
  h(<span class="hljs-string">"span"</span>, &#123;
    <span class="hljs-attr">style</span>: &#123;
      <span class="hljs-attr">fontWeight</span>: <span class="hljs-string">"bold"</span>
    &#125;,
  &#125;, <span class="hljs-string">"This is bold"</span>),
  <span class="hljs-string">" and this is just normal text"</span>,
  h(<span class="hljs-string">"a"</span>, &#123;
    <span class="hljs-attr">props</span>: &#123;
      <span class="hljs-attr">href</span>: <span class="hljs-string">"/foo"</span>
    &#125;
  &#125;, <span class="hljs-string">"I'll take you places!"</span>),
]);
<span class="hljs-comment">// Patch into empty DOM element – this modifies the DOM as a side effect</span>
  patch(container, vnode);

<span class="hljs-keyword">const</span> newVnode = h(
  <span class="hljs-string">"div#container.two.classes"</span>,
  &#123; <span class="hljs-attr">on</span>: &#123; <span class="hljs-attr">click</span>: someFn &#125; &#125;,
  [
    h(
      <span class="hljs-string">"span"</span>,
      &#123; <span class="hljs-attr">style</span>: &#123; <span class="hljs-attr">fontWeight</span>: <span class="hljs-string">"normal"</span>, <span class="hljs-attr">fontStyle</span>: <span class="hljs-string">"italic"</span> &#125; &#125;,
      <span class="hljs-string">"This is now italic type"</span>
    ),
    <span class="hljs-string">" and this is still just normal text"</span>,
    h(<span class="hljs-string">"a"</span>, &#123; <span class="hljs-attr">props</span>: &#123; <span class="hljs-attr">href</span>: <span class="hljs-string">"/bar"</span> &#125; &#125;, <span class="hljs-string">"I'll take you places!"</span>),
  ]
);
<span class="hljs-comment">// Second `patch` invocation</span>
patch(vnode, newVnode); <span class="hljs-comment">// Snabbdom efficiently updates the old view to the new state</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意，需要把demo中的<code>someFn</code>定义一下。如果页面显示下面的内容，则环境基本搭建完成：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0499887e446b4bfa8b97b19298d8a34d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">2.2 虚拟DOM和h函数</h3>
<ul>
<li>
<p>虚拟DOM</p>
<p>用JavaScript对象描述DOM的层次结构。DOM中的一切属性都在虚拟DOM中有对应的属性。</p>
</li>
<li>
<p>diff是发生在虚拟DOM上的</p>
<p>新虚拟DOM和老虚拟DOM进行diff，算出如何最小化更新，最后反映到真实的DOM上。</p>
</li>
<li>
<p>研究1：虚拟DOM如何通过渲染函数(<code>h函数</code>)产生的</p>
<p>手写h函数。</p>
</li>
<li>
<p>研究2: diff算法原理</p>
<p>手写diff算法。</p>
</li>
<li>
<p>研究3：虚拟DOM如何通过diff变成真正的DOM</p>
<p>事实上，虚拟DOM变为真正DOM，是涵盖在diff算法里的。</p>
</li>
</ul>
<p>注意： DOM如何变为虚拟DOM，是属于<code>模板编译</code>原理范畴，我们这里不做讨论。</p>
<h4 data-id="heading-6">2.2.1 h函数</h4>
<p>h函数用来产生<code>虚拟节点(vnode)</code></p>
<p>比如这样调用h函数：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">h(<span class="hljs-string">'a'</span>, &#123;<span class="hljs-attr">props</span>: &#123; <span class="hljs-attr">href</span>: <span class="hljs-string">'https://www.baidu.com'</span> &#125;&#125;, <span class="hljs-string">'百度一下，你还是不知道'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>得到这样的虚拟节点：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5aebb7bc3ded4460b986201ce2cc2ed6~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">
他表示真正的DOM节点：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">'https://www.baidu.com'</span>></span>百度一下，你还是不知道<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>字段解释：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
  <span class="hljs-attr">children</span>: <span class="hljs-literal">undefined</span>, <span class="hljs-comment">// 子元素</span>
  <span class="hljs-attr">data</span>: &#123;&#125;, <span class="hljs-comment">// 属性 样式 等</span>
  <span class="hljs-attr">elm</span>: <span class="hljs-literal">undefined</span>, <span class="hljs-comment">// 有没有对应的DOM节点，有没有上树</span>
  <span class="hljs-attr">key</span>: <span class="hljs-literal">undefined</span>, <span class="hljs-comment">// 唯一标识</span>
  <span class="hljs-attr">sel</span>: <span class="hljs-string">'div'</span>, <span class="hljs-comment">// 选择器</span>
  <span class="hljs-attr">text</span>: <span class="hljs-string">'我是一个盒子'</span> <span class="hljs-comment">// 文字</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>调用patch函数（后面会讲到），可以使虚拟DOM上树。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123;
  init,
  classModule,
  propsModule,
  styleModule,
  eventListenersModule,
  h,
&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"snabbdom"</span>;

<span class="hljs-keyword">const</span> patch = init([
  <span class="hljs-comment">// Init patch function with chosen modules</span>
  classModule, <span class="hljs-comment">// makes it easy to toggle classes</span>
  propsModule, <span class="hljs-comment">// for setting properties on DOM elements</span>
  styleModule, <span class="hljs-comment">// handles styling on elements with support for animations</span>
  eventListenersModule, <span class="hljs-comment">// attaches event listeners</span>
]);

<span class="hljs-keyword">const</span> container = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"container"</span>);

<span class="hljs-comment">// 创建虚拟节点</span>
<span class="hljs-keyword">const</span> vnode = h(<span class="hljs-string">'a'</span>, &#123; <span class="hljs-attr">props</span>: &#123; <span class="hljs-attr">href</span>: <span class="hljs-string">'https://www.baidu.com'</span> &#125; &#125;, <span class="hljs-string">'百度一下，你还是不知道'</span>)

<span class="hljs-comment">// 让虚拟节点上树</span>
patch(container, vnode)

<span class="hljs-built_in">console</span>.log(vnode)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d5b316520214138ac744e475487243d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>h函数可以嵌套，从而得到虚拟DOM树。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> vnode = h(<span class="hljs-string">'ul'</span>, &#123;&#125;, [
  h(<span class="hljs-string">'li'</span>, &#123; <span class="hljs-attr">style</span>: &#123; <span class="hljs-attr">color</span>: <span class="hljs-string">'#f00'</span> &#125; &#125;, <span class="hljs-string">'java'</span>),
  h(<span class="hljs-string">'li'</span>, <span class="hljs-string">'php'</span>),
  h(<span class="hljs-string">'li'</span>, <span class="hljs-string">'python'</span>),
])
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c576325ec4441a9af6cb74df6924885~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-7">原版h函数TS版本核心代码</h4>
<p>h.ts</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">h</span>(<span class="hljs-params">sel: <span class="hljs-built_in">string</span></span>): <span class="hljs-title">VNode</span></span>;
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">h</span>(<span class="hljs-params">sel: <span class="hljs-built_in">string</span>, data: VNodeData | <span class="hljs-literal">null</span></span>): <span class="hljs-title">VNode</span></span>;
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">h</span>(<span class="hljs-params">sel: <span class="hljs-built_in">string</span>, children: VNodeChildren</span>): <span class="hljs-title">VNode</span></span>;
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">h</span>(<span class="hljs-params">
  sel: <span class="hljs-built_in">string</span>,
  data: VNodeData | <span class="hljs-literal">null</span>,
  children: VNodeChildren
</span>): <span class="hljs-title">VNode</span></span>;
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">h</span>(<span class="hljs-params">sel: <span class="hljs-built_in">any</span>, b?: <span class="hljs-built_in">any</span>, c?: <span class="hljs-built_in">any</span></span>): <span class="hljs-title">VNode</span> </span>&#123;
  <span class="hljs-keyword">let</span> data: VNodeData = &#123;&#125;;
  <span class="hljs-keyword">let</span> children: <span class="hljs-built_in">any</span>;
  <span class="hljs-keyword">let</span> text: <span class="hljs-built_in">any</span>;
  <span class="hljs-keyword">let</span> i: <span class="hljs-built_in">number</span>;
  <span class="hljs-keyword">if</span> (c !== <span class="hljs-literal">undefined</span>) &#123;
    <span class="hljs-keyword">if</span> (b !== <span class="hljs-literal">null</span>) &#123;
      data = b;
    &#125;
    <span class="hljs-keyword">if</span> (is.array(c)) &#123;
      children = c;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (is.primitive(c)) &#123;
      text = c;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (c && c.sel) &#123;
      children = [c];
    &#125;
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (b !== <span class="hljs-literal">undefined</span> && b !== <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-keyword">if</span> (is.array(b)) &#123;
      children = b;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (is.primitive(b)) &#123;
      text = b;
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (b && b.sel) &#123;
      children = [b];
    &#125; <span class="hljs-keyword">else</span> &#123;
      data = b;
    &#125;
  &#125;
  <span class="hljs-keyword">if</span> (children !== <span class="hljs-literal">undefined</span>) &#123;
    <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < children.length; ++i) &#123;
      <span class="hljs-keyword">if</span> (is.primitive(children[i]))
        children[i] = vnode(
          <span class="hljs-literal">undefined</span>,
          <span class="hljs-literal">undefined</span>,
          <span class="hljs-literal">undefined</span>,
          children[i],
          <span class="hljs-literal">undefined</span>
        );
    &#125;
  &#125;
  <span class="hljs-keyword">if</span> (
    sel[<span class="hljs-number">0</span>] === <span class="hljs-string">"s"</span> &&
    sel[<span class="hljs-number">1</span>] === <span class="hljs-string">"v"</span> &&
    sel[<span class="hljs-number">2</span>] === <span class="hljs-string">"g"</span> &&
    (sel.length === <span class="hljs-number">3</span> || sel[<span class="hljs-number">3</span>] === <span class="hljs-string">"."</span> || sel[<span class="hljs-number">3</span>] === <span class="hljs-string">"#"</span>)
  ) &#123;
    addNS(data, children, sel);
  &#125;
  <span class="hljs-keyword">return</span> vnode(sel, data, children, text, <span class="hljs-literal">undefined</span>);
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>vnode.ts</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">vnode</span>(<span class="hljs-params">
  sel: <span class="hljs-built_in">string</span> | <span class="hljs-literal">undefined</span>,
  data: <span class="hljs-built_in">any</span> | <span class="hljs-literal">undefined</span>,
  children: <span class="hljs-built_in">Array</span><VNode | <span class="hljs-built_in">string</span>> | <span class="hljs-literal">undefined</span>,
  text: <span class="hljs-built_in">string</span> | <span class="hljs-literal">undefined</span>,
  elm: Element | Text | <span class="hljs-literal">undefined</span>
</span>): <span class="hljs-title">VNode</span> </span>&#123;
  <span class="hljs-keyword">const</span> key = data === <span class="hljs-literal">undefined</span> ? <span class="hljs-literal">undefined</span> : data.key;
  <span class="hljs-keyword">return</span> &#123; sel, data, children, text, elm, key &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从h.ts里面的代码来看，h函数有很多种用法（TS的函数重载）:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">h(<span class="hljs-string">'div'</span>)
h(<span class="hljs-string">'div'</span>, <span class="hljs-string">'文字'</span>)
h(<span class="hljs-string">'div'</span>, [])
h(<span class="hljs-string">'div'</span>, h())
h(<span class="hljs-string">'div'</span>, &#123;&#125;, <span class="hljs-string">'文字'</span>)
h(<span class="hljs-string">'div'</span>, &#123;&#125;, [])
h(<span class="hljs-string">'div'</span>, &#123;&#125;, h())
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面到了手写h函数的环节，我们在这里只实现阉割版的h函数，只实现3个参数的情况，因为原版代码里就是给a、b、c三个参数赋值而已。</p>
<h4 data-id="heading-8">手写h函数</h4>
<p>看原版的TS代码，仿写JS代码。因为我们今天重点不在TS。</p>
<p>只要主干功能，放弃实现一些细节，保证让大家都能理解核心是怎么实现的。</p>
<p>vnode.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 非常简单，只是把传入参数合组合成对象返回</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">sel, data, children, text, elm</span>) </span>&#123;
  <span class="hljs-keyword">const</span> key = data === <span class="hljs-literal">undefined</span> ? <span class="hljs-literal">undefined</span> : data.key;
  <span class="hljs-keyword">return</span> &#123;
    sel, data, children, text, elm, key
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>h.js</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> vnode <span class="hljs-keyword">from</span> <span class="hljs-string">'./vnode.js'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">sel, data, c</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">arguments</span>.length !== <span class="hljs-number">3</span>) &#123;
    <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'对不起，我们是阉割版的h函数，只实现3个参数的情况，QAQ'</span>)
  &#125;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> c === <span class="hljs-string">'string'</span> || <span class="hljs-keyword">typeof</span> c === <span class="hljs-string">'number'</span>) &#123;
    <span class="hljs-keyword">return</span> vnode(sel, data, <span class="hljs-literal">undefined</span>, c, <span class="hljs-literal">undefined</span>)
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(c)) &#123;
    <span class="hljs-keyword">const</span> children = []
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < c.length; i++) &#123;
      <span class="hljs-comment">// 检查c[i]必须是一个对象</span>
      <span class="hljs-keyword">if</span> (!(<span class="hljs-keyword">typeof</span> c[i] === <span class="hljs-string">'object'</span> && c[i].hasOwnProperty(<span class="hljs-string">'sel'</span>))) &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'传入的数组参数中有项不是h函数'</span>)
      &#125;
      children.push(c[i])
    &#125;
    <span class="hljs-keyword">return</span> vnode(sel, data, children, <span class="hljs-literal">undefined</span>, <span class="hljs-literal">undefined</span>)
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> c === <span class="hljs-string">'object'</span> && c.hasOwnProperty(<span class="hljs-string">'sel'</span>)) &#123;
    <span class="hljs-keyword">const</span> children = [c]
    <span class="hljs-keyword">return</span> vnode(sel, data, children, <span class="hljs-literal">undefined</span>, <span class="hljs-literal">undefined</span>)
  &#125;
  <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'对不起，参数错误'</span>)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，我们已经实现了一个阉割版的h函数，直接上例子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> h <span class="hljs-keyword">from</span> <span class="hljs-string">"./mysnabbdom/h.js"</span>;

<span class="hljs-keyword">const</span> vnode = h(<span class="hljs-string">'div'</span>, &#123;&#125;, [
  h(<span class="hljs-string">'h2'</span>, &#123;&#125;, <span class="hljs-string">'我是一个标题'</span>),
  h(<span class="hljs-string">'div'</span>, &#123;&#125;, h(<span class="hljs-string">'p'</span>, &#123;&#125;, <span class="hljs-string">'我是一个p'</span>)),
  h(<span class="hljs-string">'ul'</span>, &#123;&#125;, [
    h(<span class="hljs-string">'li'</span>, &#123;&#125;, <span class="hljs-string">'java'</span>),
    h(<span class="hljs-string">'li'</span>, &#123;&#125;, <span class="hljs-string">'php'</span>),
    h(<span class="hljs-string">'li'</span>, &#123;&#125;, <span class="hljs-string">'python'</span>),
  ])
])

<span class="hljs-built_in">console</span>.log(vnode)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当当当当~~~</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/35ebce66c623451f89011fb03bb12b93~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>完美收官！</p>
<h3 data-id="heading-9">2.3 感受diff算法</h3>
<p>一直都在说diff，那么diff到底干了什么？<br>
通过这一章节的学习（例子以及演示），你将会对diff算法有了进一步了解，知道它干了什么。<br>
看个例子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> container = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"container"</span>);
<span class="hljs-keyword">const</span> btn = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"btn"</span>);

<span class="hljs-keyword">const</span> vnode1 = h(<span class="hljs-string">'ul'</span>, &#123;&#125;, [
  h(<span class="hljs-string">'li'</span>, &#123;&#125;, <span class="hljs-string">'A'</span>),
  h(<span class="hljs-string">'li'</span>, &#123;&#125;, <span class="hljs-string">'B'</span>),
  h(<span class="hljs-string">'li'</span>, &#123;&#125;, <span class="hljs-string">'C'</span>),
  h(<span class="hljs-string">'li'</span>, &#123;&#125;, <span class="hljs-string">'D'</span>),
])

patch(container, vnode1)

<span class="hljs-comment">// 点击按钮时 将 vnode1 换成 vnode2 </span>
btn.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> vnode2 = h(<span class="hljs-string">'ul'</span>, &#123;&#125;, [
    h(<span class="hljs-string">'li'</span>, &#123;&#125;, <span class="hljs-string">'A'</span>),
    h(<span class="hljs-string">'li'</span>, &#123;&#125;, <span class="hljs-string">'B'</span>),
    h(<span class="hljs-string">'li'</span>, &#123;&#125;, <span class="hljs-string">'C'</span>),
    h(<span class="hljs-string">'li'</span>, &#123;&#125;, <span class="hljs-string">'D'</span>),
    h(<span class="hljs-string">'li'</span>, &#123;&#125;, <span class="hljs-string">'E'</span>),
  ])
  patch(vnode1, vnode2)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38452689711b45ab922556e94e484960~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们成功的把vnode1替换成了vnode2。<br>
那diff算法内部到底干了什么？按我们已经知道的知识，diff应该知道ABCD是不会变的，那么真的是这样吗？怎么验证？<br>
看下面的图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da4c975726ff4538964086209a8db5b6~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>很明显的看到，我们手动把li的文字改掉，点击按钮后，文字并没有发生变化(没有变为ABCD)，故diff知道了ABCD没有任何变化，所以复用并保留了它们。说明diff是最小量更新，diff真是太牛啦！</p>
<p>那么，diff真的有这么智能吗？<br>
看下面的例子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> container = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"container"</span>);
<span class="hljs-keyword">const</span> btn = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"btn"</span>);

<span class="hljs-keyword">const</span> vnode1 = h(<span class="hljs-string">'ul'</span>, &#123;&#125;, [
  h(<span class="hljs-string">'li'</span>, &#123;&#125;, <span class="hljs-string">'A'</span>),
  h(<span class="hljs-string">'li'</span>, &#123;&#125;, <span class="hljs-string">'B'</span>),
  h(<span class="hljs-string">'li'</span>, &#123;&#125;, <span class="hljs-string">'C'</span>),
  h(<span class="hljs-string">'li'</span>, &#123;&#125;, <span class="hljs-string">'D'</span>),
])

patch(container, vnode1)

<span class="hljs-comment">// 点击按钮时 将 vnode1 换成 vnode2 </span>
btn.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> vnode2 = h(<span class="hljs-string">'ul'</span>, &#123;&#125;, [
    h(<span class="hljs-string">'li'</span>, &#123;&#125;, <span class="hljs-string">'E'</span>),
    h(<span class="hljs-string">'li'</span>, &#123;&#125;, <span class="hljs-string">'A'</span>),
    h(<span class="hljs-string">'li'</span>, &#123;&#125;, <span class="hljs-string">'B'</span>),
    h(<span class="hljs-string">'li'</span>, &#123;&#125;, <span class="hljs-string">'C'</span>),
    h(<span class="hljs-string">'li'</span>, &#123;&#125;, <span class="hljs-string">'D'</span>),
  ])
  patch(vnode1, vnode2)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们在前面插入一个E，看看会发生什么。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d78986ca3bd4057accbf1ff60f82cf5~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>好像。。。没啥毛病。那么问题来了，diff到底是在前面插入E，还是在后面插入一个节点，依次把文字替换呢？<br>
即A=>E    B=>A   C=>B  D=>C   ''=>E</p>
<p>不卖关子了，我们用同样的方式上图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/31dc00ccd2704892981fb322a61376f7~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们发现，E并不是在前面插入的，所以，并没有那么智能。但是，diff真的这么笨吗？<br>
我们来继续看下面的例子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> vnode1 = h(<span class="hljs-string">'ul'</span>, &#123;&#125;, [
  h(<span class="hljs-string">'li'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'A'</span> &#125;, <span class="hljs-string">'A'</span>),
  h(<span class="hljs-string">'li'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'B'</span> &#125;, <span class="hljs-string">'B'</span>),
  h(<span class="hljs-string">'li'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'C'</span> &#125;, <span class="hljs-string">'C'</span>),
  h(<span class="hljs-string">'li'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'D'</span> &#125;, <span class="hljs-string">'D'</span>),
])

patch(container, vnode1)

<span class="hljs-comment">// 点击按钮时 将 vnode1 换成 vnode2 </span>
btn.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> vnode2 = h(<span class="hljs-string">'ul'</span>, &#123;&#125;, [
    h(<span class="hljs-string">'li'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'E'</span> &#125;, <span class="hljs-string">'E'</span>),
    h(<span class="hljs-string">'li'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'A'</span> &#125;, <span class="hljs-string">'A'</span>),
    h(<span class="hljs-string">'li'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'B'</span> &#125;, <span class="hljs-string">'B'</span>),
    h(<span class="hljs-string">'li'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'C'</span> &#125;, <span class="hljs-string">'C'</span>),
    h(<span class="hljs-string">'li'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'D'</span> &#125;, <span class="hljs-string">'D'</span>),
  ])
  patch(vnode1, vnode2)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们加了一个key，看到这，你是不是脑子里灵光一闪，突然好像明白了什么。<br>
上图！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c2148a11d7b42bf91fa7858105ba689~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>很直观的发现，加上key后，diff就真的在前面插入了E。因为我们告诉了diff，A就是A、B就是B。。。<br>
key的作用就是为了服务于最小量更新，这就知道为什么我们写项目的时候列表为什么必须要加key的原因。</p>
<p>再来一个例子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> vnode1 = h(<span class="hljs-string">'ul'</span>, &#123;&#125;, [
  h(<span class="hljs-string">'li'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'A'</span> &#125;, <span class="hljs-string">'A'</span>),
  h(<span class="hljs-string">'li'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'B'</span> &#125;, <span class="hljs-string">'B'</span>),
  h(<span class="hljs-string">'li'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'C'</span> &#125;, <span class="hljs-string">'C'</span>),
  h(<span class="hljs-string">'li'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'D'</span> &#125;, <span class="hljs-string">'D'</span>),
])

patch(container, vnode1)

<span class="hljs-comment">// 点击按钮时 将 vnode1 换成 vnode2 </span>
btn.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> vnode2 = h(<span class="hljs-string">'ol'</span>, &#123;&#125;, [
    h(<span class="hljs-string">'li'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'A'</span> &#125;, <span class="hljs-string">'A'</span>),
    h(<span class="hljs-string">'li'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'B'</span> &#125;, <span class="hljs-string">'B'</span>),
    h(<span class="hljs-string">'li'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'C'</span> &#125;, <span class="hljs-string">'C'</span>),
    h(<span class="hljs-string">'li'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'D'</span> &#125;, <span class="hljs-string">'D'</span>),
  ])
  patch(vnode1, vnode2)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们加了一个key，看到这，你是不是脑子里灵光一闪，突然好像明白了什么。<br>
上图！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46c08b50d53c451eb3dd79bf3280b203~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们把ul换成了ol，整个DOM被替换掉了。</p>
<p>最后一个例子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> vnode1 = h(<span class="hljs-string">'div'</span>, &#123;&#125;, [
  h(<span class="hljs-string">'p'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'A'</span> &#125;, <span class="hljs-string">'A'</span>),
  h(<span class="hljs-string">'p'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'B'</span> &#125;, <span class="hljs-string">'B'</span>),
  h(<span class="hljs-string">'p'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'C'</span> &#125;, <span class="hljs-string">'C'</span>),
  h(<span class="hljs-string">'p'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'D'</span> &#125;, <span class="hljs-string">'D'</span>),
])

patch(container, vnode1)

<span class="hljs-comment">// 点击按钮时 将 vnode1 换成 vnode2 </span>
btn.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> vnode2 = h(<span class="hljs-string">'div'</span>, &#123;&#125;, h(<span class="hljs-string">'div'</span>, &#123;&#125;, [
    h(<span class="hljs-string">'p'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'A'</span> &#125;, <span class="hljs-string">'A'</span>),
    h(<span class="hljs-string">'p'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'B'</span> &#125;, <span class="hljs-string">'B'</span>),
    h(<span class="hljs-string">'p'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'C'</span> &#125;, <span class="hljs-string">'C'</span>),
    h(<span class="hljs-string">'p'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'D'</span> &#125;, <span class="hljs-string">'D'</span>),
  ]))
  patch(vnode1, vnode2)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bba7cad0e62e47058fa11962093fd924~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>心得：<br>
1、最小量更新真是太厉害啦，真的是最小量更新！当然，key很重要。key是这个节点的唯一标识，告诉diff算法，在更改前后，它们是用一个DOM节点。<br>
2、只有是同一个虚拟节点，才会进行精细化比较。否则就是暴力删除旧的、插入新的。如何定义是同一个虚拟节点：选择器相同且key相同。<br>
3、只进行同层比较，不会进行跨层比较。即使是同一片虚拟节点，但是跨层了，对不起，精细化比较不diff你，而是暴力删除旧的、插入新的。<br></p>
<p>可能你会问，diff并不是那么牛逼啊！但真的影响效率吗？<br>
答：相关的操作在实际开发中，基本不会遇到，所以这是合理的优化机制。<br>
就好比你在开发中，并不会写这种代码：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">'flag'</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">li</span>></span>A<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">li</span>></span>B<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">li</span>></span>C<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"><<span class="hljs-name">ol</span> <span class="hljs-attr">v-else</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">li</span>></span>A<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">li</span>></span>B<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">li</span>></span>C<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ol</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">'flag'</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
   <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">'!flag'</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">'!flag'</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">v-if</span>=<span class="hljs-string">'!flag'</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>虽然这一章节只是感受diff算法，但我相信你肯定会有收获的~~~</p>
<h2 data-id="heading-10">三、手写diff</h2>
<p>我们手写之前先简单看下源码。<br>
从一开始的demo中，我们可以发现调用了init方法返回了patch函数。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123;
  init,
  classModule,
  propsModule,
  styleModule,
  eventListenersModule,
  h,
&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"snabbdom"</span>;

<span class="hljs-keyword">const</span> patch = init([
  <span class="hljs-comment">// Init patch function with chosen modules</span>
  classModule, <span class="hljs-comment">// makes it easy to toggle classes</span>
  propsModule, <span class="hljs-comment">// for setting properties on DOM elements</span>
  styleModule, <span class="hljs-comment">// handles styling on elements with support for animations</span>
  eventListenersModule, <span class="hljs-comment">// attaches event listeners</span>
]);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>init.ts 源码截图</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a6386382e3e4c55ba1d74b5b904db10~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>patch方法</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patch</span>(<span class="hljs-params">oldVnode: VNode | Element, vnode: VNode</span>): <span class="hljs-title">VNode</span> </span>&#123;
    <span class="hljs-keyword">let</span> i: <span class="hljs-built_in">number</span>, <span class="hljs-attr">elm</span>: Node, <span class="hljs-attr">parent</span>: Node;
    <span class="hljs-keyword">const</span> insertedVnodeQueue: VNodeQueue = [];<span class="hljs-comment">// 不用看</span>
    <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < cbs.pre.length; ++i) cbs.pre[i]();<span class="hljs-comment">// 不用看</span>

    <span class="hljs-keyword">if</span> (!isVnode(oldVnode)) &#123;
      oldVnode = emptyNodeAt(oldVnode);
    &#125;

    <span class="hljs-keyword">if</span> (sameVnode(oldVnode, vnode)) &#123;
      patchVnode(oldVnode, vnode, insertedVnodeQueue);
    &#125; <span class="hljs-keyword">else</span> &#123;
      elm = oldVnode.elm!;
      parent = api.parentNode(elm) <span class="hljs-keyword">as</span> Node;

      createElm(vnode, insertedVnodeQueue);

      <span class="hljs-keyword">if</span> (parent !== <span class="hljs-literal">null</span>) &#123;
        api.insertBefore(parent, vnode.elm!, api.nextSibling(elm));
        removeVnodes(parent, [oldVnode], <span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
      &#125;
    &#125;

    <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < insertedVnodeQueue.length; ++i) &#123;
      insertedVnodeQueue[i].data!.hook!.insert!(insertedVnodeQueue[i]);<span class="hljs-comment">// 不用看</span>
    &#125;
    <span class="hljs-keyword">for</span> (i = <span class="hljs-number">0</span>; i < cbs.post.length; ++i) cbs.post[i]();<span class="hljs-comment">// 不用看</span>
    <span class="hljs-keyword">return</span> vnode;
  &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看patch方法源码我们可以知道简单的流程：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/834c3414f2a144818265af7c24da7b13~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">3.1 新建patch函数</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> vnode <span class="hljs-keyword">from</span> <span class="hljs-string">'./vnode.js'</span>
<span class="hljs-keyword">import</span> api <span class="hljs-keyword">from</span> <span class="hljs-string">'./htmldomapi.js'</span>

<span class="hljs-comment">// 是不是虚拟节点</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isVnode</span>(<span class="hljs-params">vnode</span>) </span>&#123;
  <span class="hljs-keyword">return</span> vnode.sel === <span class="hljs-string">''</span> || vnode.sel !== <span class="hljs-literal">undefined</span>;
&#125;

<span class="hljs-comment">// 把oldVnode包装成虚拟节点</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">emptyNodeAt</span>(<span class="hljs-params">elm</span>) </span>&#123;
  <span class="hljs-keyword">return</span> vnode(
    api.tagName(elm).toLowerCase(),
    &#123;&#125;,
    [],
    <span class="hljs-literal">undefined</span>,
    elm
  );
&#125;

<span class="hljs-comment">// 是不是同一个虚拟节点</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sameVnode</span>(<span class="hljs-params">vnode1, vnode2</span>) </span>&#123;
  <span class="hljs-keyword">return</span> vnode1.sel === vnode2.sel && vnode1.key === vnode2.key
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patch</span>(<span class="hljs-params">oldVnode, newVnode</span>) </span>&#123;
  <span class="hljs-comment">// 判断是不是虚拟节点</span>
  <span class="hljs-keyword">if</span> (!isVnode(oldVnode)) &#123;
    <span class="hljs-comment">// 不是虚拟节点 则包装成虚拟节点</span>
    oldVnode = emptyNodeAt(oldVnode)
  &#125;

  <span class="hljs-keyword">if</span> (sameVnode(oldVnode, newVnode)) &#123;
    <span class="hljs-comment">// 精细化比较</span>
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 暴力插入新的，删除新的</span>
  &#125;
  
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其中，里面的vnode就是之前定义的vnode函数，api是操作dom的api，这里就不放代码了，大家应该能看懂。<br>
目前已经实现了上面流程图里的部分功能，接下来到了第一个比较难的部分，就是插入新的，删除旧的。</p>
<h3 data-id="heading-12">3.2 createElement函数</h3>
<p>我们先考虑最简单的，h函数第三个参数是文本的情况。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> h <span class="hljs-keyword">from</span> <span class="hljs-string">'./mysnabbdom/h'</span>
<span class="hljs-keyword">import</span> patch <span class="hljs-keyword">from</span> <span class="hljs-string">'./mysnabbdom/patch'</span>

<span class="hljs-keyword">const</span> container = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"container"</span>);

<span class="hljs-keyword">const</span> vnode1 = h(<span class="hljs-string">'h1'</span>, &#123;&#125;, <span class="hljs-string">'你好'</span>)

patch(container, vnode1)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 真正创建节点，将 vnode 创建为 DOM ，插入到 pivot 元素之前</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElement</span>(<span class="hljs-params">vnode, pivot</span>) </span>&#123;
  <span class="hljs-comment">// 创建DOM节点</span>
  <span class="hljs-keyword">let</span> domNode = <span class="hljs-built_in">document</span>.createElement(vnode.sel)
  <span class="hljs-comment">// 有子节点还是有文本</span>
  <span class="hljs-keyword">if</span> (vnode.text !== <span class="hljs-string">''</span> && (vnode.children === <span class="hljs-literal">undefined</span> || vnode.children.length === <span class="hljs-number">0</span>)) &#123;
    <span class="hljs-comment">// 他内部是文本</span>
    domNode.innerText = vnode.text
    <span class="hljs-comment">// 上树 让是 pivot 的父元素调用 insertBefore 方法 ，将新的节点 domNode 插入到 pivot 之前</span>
    pivot.parentNode.insertBefore(domNode, pivot)
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patch</span>(<span class="hljs-params">oldVnode, newVnode</span>) </span>&#123;
  <span class="hljs-comment">// 判断是不是虚拟节点</span>
  <span class="hljs-keyword">if</span> (!isVnode(oldVnode)) &#123;
    <span class="hljs-comment">// 不是虚拟节点 则包装成虚拟节点</span>
    oldVnode = emptyNodeAt(oldVnode)
  &#125;

  <span class="hljs-keyword">if</span> (sameVnode(oldVnode, newVnode)) &#123;
    <span class="hljs-comment">// 精细化比较</span>
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 暴力插入新的，删除新的</span>
    createElement(newVnode, oldVnode.elm)
  &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>页面已经成功显示 你好。我们完成了第一次上树。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22463ec541494ae08236fcca5f79cd1f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们接下来考虑h函数第三个参数是数组的情况。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> vnode1 = h(<span class="hljs-string">'ul'</span>, &#123;&#125;, [
  h(<span class="hljs-string">'li'</span>, &#123;&#125;, <span class="hljs-string">'A'</span>),
  h(<span class="hljs-string">'li'</span>, &#123;&#125;, <span class="hljs-string">'B'</span>),
  h(<span class="hljs-string">'li'</span>, &#123;&#125;, <span class="hljs-string">'C'</span>),
  h(<span class="hljs-string">'li'</span>, &#123;&#125;, <span class="hljs-string">'D'</span>),
])

patch(container, vnode1)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于有很多子节点，我们需要递归创建节点，同时递归需要有个结束条件，也就是h函数第三个参数为文本的时候。<br>
这种情况我们会发现，createElement第二个参数在这里不知道传什么，所以我们先改造一下createElement函数，第二个参数我们不传，我们只用createElement创建节点，不进行插入操作，我们在patch函数里执行插入。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElement</span>(<span class="hljs-params">vnode</span>) </span>&#123;
  <span class="hljs-comment">// 创建DOM节点</span>
  <span class="hljs-keyword">let</span> domNode = <span class="hljs-built_in">document</span>.createElement(vnode.sel)
  <span class="hljs-comment">// 有子节点还是有文本</span>
  <span class="hljs-keyword">if</span> (vnode.text !== <span class="hljs-string">''</span> && (vnode.children === <span class="hljs-literal">undefined</span> || vnode.children.length === <span class="hljs-number">0</span>)) &#123;
    <span class="hljs-comment">// 他内部是文本</span>
    domNode.innerText = vnode.text
    <span class="hljs-comment">// 补充elm属性</span>
    vnode.elm = domNode
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(vnode.children) && vnode.children.length > <span class="hljs-number">0</span>) &#123;
    <span class="hljs-comment">// 内部是子节点，就要递归创建节点</span>
  &#125;
  <span class="hljs-comment">// 返回elm 纯dom对象</span>
  <span class="hljs-keyword">return</span> vnode.elm
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时，我们要改造上面第一个简单的例子：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patch</span>(<span class="hljs-params">oldVnode, newVnode</span>) </span>&#123;
  <span class="hljs-comment">// 判断是不是虚拟节点</span>
  <span class="hljs-keyword">if</span> (!isVnode(oldVnode)) &#123;
    <span class="hljs-comment">// 不是虚拟节点 则包装成虚拟节点</span>
    oldVnode = emptyNodeAt(oldVnode)
  &#125;

  <span class="hljs-keyword">if</span> (sameVnode(oldVnode, newVnode)) &#123;
    <span class="hljs-comment">// 精细化比较</span>
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 暴力插入新的，删除新的</span>
    <span class="hljs-keyword">let</span> newVnodeElm = createElement(newVnode)
    oldVnode.elm.parentNode.insertBefore(newVnodeElm, oldVnode.elm)
  &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们在页面上成功显示 你好。</p>
<p>我们这样改造的目的就是为了让createElement只做创建节点的事情，不做其他事情，便于后续递归。<br>
那么，我们便可以开始写递归了。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> vnode <span class="hljs-keyword">from</span> <span class="hljs-string">'./vnode.js'</span>
<span class="hljs-keyword">import</span> api <span class="hljs-keyword">from</span> <span class="hljs-string">'./htmldomapi.js'</span>

<span class="hljs-comment">// 是不是虚拟节点</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isVnode</span>(<span class="hljs-params">vnode</span>) </span>&#123;
  <span class="hljs-keyword">return</span> vnode.sel === <span class="hljs-string">''</span> || vnode.sel !== <span class="hljs-literal">undefined</span>;
&#125;

<span class="hljs-comment">// 把oldVnode包装成虚拟节点</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">emptyNodeAt</span>(<span class="hljs-params">elm</span>) </span>&#123;
  <span class="hljs-keyword">return</span> vnode(
    api.tagName(elm).toLowerCase(),
    &#123;&#125;,
    [],
    <span class="hljs-literal">undefined</span>,
    elm
  );
&#125;

<span class="hljs-comment">// 是不是同一个虚拟节点</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sameVnode</span>(<span class="hljs-params">vnode1, vnode2</span>) </span>&#123;
  <span class="hljs-keyword">return</span> vnode1.key === vnode2.key && vnode1.sel === vnode2.sel
&#125;

<span class="hljs-comment">// 真正创建节点，将 vnode 创建为 DOM 但不进行插入操作</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElement</span>(<span class="hljs-params">vnode</span>) </span>&#123;
  <span class="hljs-comment">// 创建DOM节点</span>
  <span class="hljs-keyword">let</span> domNode = <span class="hljs-built_in">document</span>.createElement(vnode.sel)
  <span class="hljs-comment">// 有子节点还是有文本</span>
  <span class="hljs-keyword">if</span> (vnode.text !== <span class="hljs-string">''</span> && (vnode.children === <span class="hljs-literal">undefined</span> || vnode.children.length === <span class="hljs-number">0</span>)) &#123;
    <span class="hljs-comment">// 他内部是文本</span>
    domNode.innerText = vnode.text
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(vnode.children) && vnode.children.length > <span class="hljs-number">0</span>) &#123;
    <span class="hljs-comment">// 内部是子节点，就要递归创建节点</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < vnode.children.length; i++) &#123;
      <span class="hljs-comment">// 得到当前children</span>
      <span class="hljs-keyword">let</span> ch = vnode.children[i]
      <span class="hljs-comment">// 创建出它的dom，一旦调用了createElement意味着：创建出dom了，并且它的elm属性指向了创建出的dom，但是还没有上树</span>
      <span class="hljs-keyword">let</span> chDom = createElement(ch)
      <span class="hljs-comment">// 上树</span>
      domNode.appendChild(chDom)
    &#125;
  &#125;
  <span class="hljs-comment">// 补充elm属性</span>
  vnode.elm = domNode
  <span class="hljs-comment">// 返回elm 纯dom对象</span>
  <span class="hljs-keyword">return</span> vnode.elm
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patch</span>(<span class="hljs-params">oldVnode, newVnode</span>) </span>&#123;
  <span class="hljs-comment">// 判断是不是虚拟节点</span>
  <span class="hljs-keyword">if</span> (!isVnode(oldVnode)) &#123;
    <span class="hljs-comment">// 不是虚拟节点 则包装成虚拟节点</span>
    oldVnode = emptyNodeAt(oldVnode)
  &#125;

  <span class="hljs-keyword">if</span> (sameVnode(oldVnode, newVnode)) &#123;
    <span class="hljs-comment">// 精细化比较</span>
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 暴力插入新的，删除新的</span>
    <span class="hljs-keyword">let</span> newVnodeElm = createElement(newVnode)

    <span class="hljs-keyword">if</span> (oldVnode.elm.parentNode && newVnodeElm) &#123;
      oldVnode.elm.parentNode.insertBefore(newVnodeElm, oldVnode.elm)
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>页面成功显示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/109bd9a5ca58477f8024b657ac613019~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>例2：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> vnode1 = h(<span class="hljs-string">'ul'</span>, &#123;&#125;, [
  h(<span class="hljs-string">'li'</span>, &#123;&#125;, <span class="hljs-string">'A'</span>),
  h(<span class="hljs-string">'li'</span>, &#123;&#125;, <span class="hljs-string">'B'</span>),
  h(<span class="hljs-string">'li'</span>, &#123;&#125;, <span class="hljs-string">'C'</span>),
  h(<span class="hljs-string">'li'</span>, &#123;&#125;, [
    h(<span class="hljs-string">'div'</span>,&#123;&#125;,<span class="hljs-string">'DD1'</span>),
    h(<span class="hljs-string">'div'</span>,&#123;&#125;,<span class="hljs-string">'DD2'</span>),
    h(<span class="hljs-string">'div'</span>,&#123;&#125;,<span class="hljs-string">'DD3'</span>),
  ]),
])

patch(container, vnode1)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bfa84528f4ef47649fc677abf5239776~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>到此，我们的递归写得差不多了。</p>
<p>噢，对了，我们还没有删除老节点，只需要加上一行代码即可。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">if</span> (oldVnode.elm.parentNode && newVnodeElm) &#123;
   oldVnode.elm.parentNode.insertBefore(newVnodeElm, oldVnode.elm)
   <span class="hljs-comment">// 删除老节点</span>
   oldVnode.elm.parentNode.removeChild(oldVnode.elm)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们再把按钮加上，改变DOM：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> h <span class="hljs-keyword">from</span> <span class="hljs-string">'./mysnabbdom/h'</span>
<span class="hljs-keyword">import</span> patch <span class="hljs-keyword">from</span> <span class="hljs-string">'./mysnabbdom/patch'</span>

<span class="hljs-keyword">const</span> container = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"container"</span>);
<span class="hljs-keyword">const</span> btn = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"btn"</span>);

<span class="hljs-keyword">const</span> vnode1 = h(<span class="hljs-string">'ul'</span>, &#123;&#125;, [
  h(<span class="hljs-string">'li'</span>, &#123;&#125;, <span class="hljs-string">'A'</span>),
  h(<span class="hljs-string">'li'</span>, &#123;&#125;, <span class="hljs-string">'B'</span>),
  h(<span class="hljs-string">'li'</span>, &#123;&#125;, <span class="hljs-string">'C'</span>),
])

patch(container, vnode1)

btn.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> vnode2 = h(<span class="hljs-string">'ol'</span>, &#123;&#125;, [
    h(<span class="hljs-string">'li'</span>, &#123;&#125;, <span class="hljs-string">'AA'</span>),
    h(<span class="hljs-string">'li'</span>, &#123;&#125;, <span class="hljs-string">'BB'</span>),
    h(<span class="hljs-string">'li'</span>, &#123;&#125;, <span class="hljs-string">'CC'</span>),
  ])

  patch(vnode1, vnode2)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b2c3ad7691643478b210ccf94766c1e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>over。</p>
<h3 data-id="heading-13">3.3 diff处理新旧节点是同一个节点时</h3>
<p>先上个流程图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c2d4efed43442d6a23c1e9f39fa06b5~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-14">3.3.1 newVnode有text的情况</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">if</span> (sameVnode(oldVnode, newVnode)) &#123;
    <span class="hljs-comment">// 在内存中是同一个对象</span>
    <span class="hljs-keyword">if</span> (oldVnode === newVnode) <span class="hljs-keyword">return</span>
    <span class="hljs-keyword">if</span> (newVnode.text !== <span class="hljs-literal">undefined</span> && (newVnode.children === <span class="hljs-literal">undefined</span> || newVnode.children.length === <span class="hljs-number">0</span>)) &#123;
      <span class="hljs-comment">// 新vnode有text属性</span>
      <span class="hljs-keyword">if</span> (newVnode.text !== oldVnode.text) &#123;
        oldVnode.elm.innerText = newVnode.text
      &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 新vnode没有text属性</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们实现了newVnode有text的情况，下面两段代码都能实现效果，比较简单，这里就不上图了。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 第一段</span>
<span class="hljs-keyword">const</span> vnode1 = h(<span class="hljs-string">'h2'</span>, &#123;&#125;, <span class="hljs-string">'hh'</span>)

patch(container, vnode1)

btn.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> vnode2 = h(<span class="hljs-string">'h2'</span>, &#123;&#125;, <span class="hljs-string">'xx'</span>)
  patch(vnode1, vnode2)
&#125;

<span class="hljs-comment">// 第二段</span>
<span class="hljs-keyword">const</span> vnode1 = h(<span class="hljs-string">'h2'</span>, &#123;&#125;, [
  h(<span class="hljs-string">'p'</span>, &#123;&#125;, <span class="hljs-string">'A'</span>),
  h(<span class="hljs-string">'p'</span>, &#123;&#125;, <span class="hljs-string">'B'</span>),
  h(<span class="hljs-string">'p'</span>, &#123;&#125;, <span class="hljs-string">'C'</span>),
])

patch(container, vnode1)

btn.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> vnode2 = h(<span class="hljs-string">'h2'</span>, &#123;&#125;, <span class="hljs-string">'xx'</span>)
  patch(vnode1, vnode2)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">3.3.2 newVnode没有text的情况(有children)</h4>
<p>1、oldVnode没有children</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">if</span> (sameVnode(oldVnode, newVnode)) &#123;
    <span class="hljs-comment">// 在内存中是同一个对象</span>
    <span class="hljs-keyword">if</span> (oldVnode === newVnode) <span class="hljs-keyword">return</span>
    <span class="hljs-keyword">if</span> (newVnode.text !== <span class="hljs-literal">undefined</span> && (newVnode.children === <span class="hljs-literal">undefined</span> || newVnode.children.length === <span class="hljs-number">0</span>)) &#123;
      <span class="hljs-comment">// 新vnode有text属性</span>
      <span class="hljs-keyword">if</span> (newVnode.text !== oldVnode.text) &#123;
        oldVnode.elm.innerText = newVnode.text
      &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 新vnode没有text属性</span>
      <span class="hljs-keyword">if</span> (oldVnode.children !== <span class="hljs-literal">undefined</span> && oldVnode.children.length > <span class="hljs-number">0</span>) &#123;
        <span class="hljs-comment">// 老的有children</span>
        <span class="hljs-comment">// 最复杂的情况</span>
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 老的没有children 新的有children</span>
        <span class="hljs-comment">// 第一步：清空老节点内容</span>
        oldVnode.elm.innerText = <span class="hljs-string">''</span>
        <span class="hljs-comment">// 第二步：遍历新的vnode子节点 创建DOM上树</span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < newVnode.children.length; i++) &#123;
          <span class="hljs-keyword">const</span> dom = createElement(newVnode.children[i])
          oldVnode.elm.appendChild(dom)
        &#125;
      &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现效果：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> vnode1 = h(<span class="hljs-string">'h2'</span>, &#123;&#125;, <span class="hljs-string">'hh'</span>)

patch(container, vnode1)

btn.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> vnode2 = h(<span class="hljs-string">'h2'</span>, &#123;&#125;, [
    h(<span class="hljs-string">'p'</span>, &#123;&#125;, <span class="hljs-string">'A'</span>),
    h(<span class="hljs-string">'p'</span>, &#123;&#125;, <span class="hljs-string">'B'</span>),
    h(<span class="hljs-string">'p'</span>, &#123;&#125;, <span class="hljs-string">'C'</span>)
  ])
  patch(vnode1, vnode2)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6cd642dc83ae43f991cd599d9d47a69e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>2、oldVnode有children</p>
<p>这一块是diff算法最核心的部分。<br>
为了便于后续操作，我们先把上面的代码单独抽出来，新增patchVnode方法：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patchVnode</span>(<span class="hljs-params">oldVnode, newVnode</span>) </span>&#123;
  <span class="hljs-comment">// 在内存中是同一个对象</span>
  <span class="hljs-keyword">if</span> (oldVnode === newVnode) <span class="hljs-keyword">return</span>
  <span class="hljs-keyword">if</span> (newVnode.text !== <span class="hljs-literal">undefined</span> && (newVnode.children === <span class="hljs-literal">undefined</span> || newVnode.children.length === <span class="hljs-number">0</span>)) &#123;
    <span class="hljs-comment">// 新vnode有text属性</span>
    <span class="hljs-keyword">if</span> (newVnode.text !== oldVnode.text) &#123;
      oldVnode.elm.innerText = newVnode.text
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 新vnode没有text属性</span>
    <span class="hljs-keyword">if</span> (oldVnode.children !== <span class="hljs-literal">undefined</span> && oldVnode.children.length > <span class="hljs-number">0</span>) &#123;
      <span class="hljs-comment">// 老的有children</span>
      <span class="hljs-comment">// 最复杂的情况</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 老的没有children 新的有children</span>
      <span class="hljs-comment">// 第一步：清空老节点内容</span>
      oldVnode.elm.innerText = <span class="hljs-string">''</span>
      <span class="hljs-comment">// 第二步：便利新的vnode子节点 创建DOM上树</span>
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < newVnode.children.length; i++) &#123;
        <span class="hljs-keyword">let</span> dom = createElement(newVnode.children[i])
        oldVnode.elm.appendChild(dom)
      &#125;
    &#125;
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patch</span>(<span class="hljs-params">oldVnode, newVnode</span>) </span>&#123;
  <span class="hljs-comment">// 判断是不是虚拟节点</span>
  <span class="hljs-keyword">if</span> (!isVnode(oldVnode)) &#123;
    <span class="hljs-comment">// 不是虚拟节点 则包装成虚拟节点</span>
    oldVnode = emptyNodeAt(oldVnode)
  &#125;
  <span class="hljs-keyword">if</span> (sameVnode(oldVnode, newVnode)) &#123;
    patchVnode(oldVnode, newVnode)
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 暴力插入新的，删除新的</span>
    <span class="hljs-keyword">let</span> newVnodeElm = createElement(newVnode)
    <span class="hljs-keyword">if</span> (oldVnode.elm.parentNode && newVnodeElm) &#123;
      oldVnode.elm.parentNode.insertBefore(newVnodeElm, oldVnode.elm)
      <span class="hljs-comment">// 删除老节点</span>
      oldVnode.elm.parentNode.removeChild(oldVnode.elm)
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">3.3.3 分析diff算法 更新子节点操作（重要）</h4>
<p>diff提供了4种命中查找方式(4个指针)：<br>
1、新前与旧前<br>
2、新后与旧后<br>
3、新后与旧前（涉及移动节点，新后指向的节点，移动到旧后之后）<br>
4、新前与旧后（涉及移动节点，新前指向的节点，移动到旧前之前）<br>
命中判断由上往下，命中一种就不会再命中判断了。<br>
如果都没有命中，就循环来寻找。<br></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/79fc36aa491e4cd19635a35701dc1e34~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>1、新前 newStart 与旧前 oldStart <br>
如果命中 1 了，patch之后就移动指针，newStart++，oldStart++</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd57ef2c6cc2432aa9dd576b4cb22888~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>新增 updateChildren 方法。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateChildren</span>(<span class="hljs-params">parentElm, oldCh, newCh</span>) </span>&#123;
  <span class="hljs-keyword">let</span> oldStartIdx = <span class="hljs-number">0</span> <span class="hljs-comment">// 旧前</span>
  <span class="hljs-keyword">let</span> newStartIdx = <span class="hljs-number">0</span> <span class="hljs-comment">// 新前</span>
  <span class="hljs-keyword">let</span> oldEndIdx = oldCh.length - <span class="hljs-number">1</span> <span class="hljs-comment">// 旧后</span>
  <span class="hljs-keyword">let</span> newEndIdx = newCh.length - <span class="hljs-number">1</span> <span class="hljs-comment">// 新后</span>
  <span class="hljs-keyword">let</span> oldStartVnode = oldCh[<span class="hljs-number">0</span>] <span class="hljs-comment">// 旧前节点</span>
  <span class="hljs-keyword">let</span> oldEndVnode = oldCh[oldEndIdx] <span class="hljs-comment">// 旧后节点</span>
  <span class="hljs-keyword">let</span> newStartVnode = newCh[<span class="hljs-number">0</span>] <span class="hljs-comment">// 新前节点</span>
  <span class="hljs-keyword">let</span> newEndVnode = newCh[newEndIdx] <span class="hljs-comment">// 新后节点</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patchVnode</span>(<span class="hljs-params">oldVnode, newVnode</span>) </span>&#123;
  <span class="hljs-comment">// 在内存中是同一个对象</span>
  <span class="hljs-keyword">if</span> (oldVnode === newVnode) <span class="hljs-keyword">return</span>
  <span class="hljs-keyword">if</span> (newVnode.text !== <span class="hljs-literal">undefined</span> && (newVnode.children === <span class="hljs-literal">undefined</span> || newVnode.children.length === <span class="hljs-number">0</span>)) &#123;
    <span class="hljs-comment">// 新vnode有text属性</span>
    <span class="hljs-keyword">if</span> (newVnode.text !== oldVnode.text) &#123;
      oldVnode.elm.innerText = newVnode.text
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 新vnode没有text属性</span>
    <span class="hljs-keyword">if</span> (oldVnode.children !== <span class="hljs-literal">undefined</span> && oldVnode.children.length > <span class="hljs-number">0</span>) &#123;
      <span class="hljs-comment">// 老的有children</span>
      <span class="hljs-comment">// 最复杂的情况</span>
      updateChildren(oldVnode.elm, oldVnode.children, newVnode.children)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 老的没有children 新的有children</span>
      <span class="hljs-comment">// 第一步：清空老节点内容</span>
      oldVnode.elm.innerText = <span class="hljs-string">''</span>
      <span class="hljs-comment">// 第二步：便利新的vnode子节点 创建DOM上树</span>
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < newVnode.children.length; i++) &#123;
        <span class="hljs-keyword">let</span> dom = createElement(newVnode.children[i])
        oldVnode.elm.appendChild(dom)
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>开始循环判断：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateChildren</span>(<span class="hljs-params">parentElm, oldCh, newCh</span>) </span>&#123;
  <span class="hljs-keyword">let</span> oldStartIdx = <span class="hljs-number">0</span> <span class="hljs-comment">// 旧前</span>
  <span class="hljs-keyword">let</span> newStartIdx = <span class="hljs-number">0</span> <span class="hljs-comment">// 新前</span>
  <span class="hljs-keyword">let</span> oldEndIdx = oldCh.length - <span class="hljs-number">1</span> <span class="hljs-comment">// 旧后</span>
  <span class="hljs-keyword">let</span> newEndIdx = newCh.length - <span class="hljs-number">1</span> <span class="hljs-comment">// 新后</span>
  <span class="hljs-keyword">let</span> oldStartVnode = oldCh[<span class="hljs-number">0</span>] <span class="hljs-comment">// 旧前节点</span>
  <span class="hljs-keyword">let</span> oldEndVnode = oldCh[oldEndIdx] <span class="hljs-comment">// 旧后节点</span>
  <span class="hljs-keyword">let</span> newStartVnode = newCh[<span class="hljs-number">0</span>] <span class="hljs-comment">// 新前节点</span>
  <span class="hljs-keyword">let</span> newEndVnode = newCh[newEndIdx] <span class="hljs-comment">// 新后节点</span>
  
  <span class="hljs-comment">// 开始循环</span>
  <span class="hljs-keyword">while</span> (oldStartIdx <= oldEndIdx && newStartIdx <= newEndIdx) &#123;
    <span class="hljs-keyword">if</span> (sameVnode(oldStartVnode, newStartVnode)) &#123;
      patchVnode(oldStartVnode, newStartVnode)
      <span class="hljs-comment">// 移动指针</span>
      oldStartVnode = oldCh(++oldStartIdx)
      newStartVnode = newCh(++newStartIdx)
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果没命中，就接着比较下一种情况。<br></p>
<p>2、新后 newEnd 和 旧后 oldEnd<br>
如果命中 1 了，patch之后就移动指针，newEnd--，oldEnd--<br></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7c153f41bbd403e827cc04054b63c87~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">if</span> (sameVnode(newEndVnode, oldEndVnode)) &#123; <span class="hljs-comment">// 新后与旧后</span>
    patchVnode(oldEndVnode, newEndVnode)
    <span class="hljs-comment">// 移动指针</span>
    oldEndVnode = oldCh[--oldEndIdx]
    newEndVnode = newCh[--newEndIdx]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果没命中，就接着比较下一种情况。<br></p>
<p>3、新后 newEnd 与旧前 oldStart<br>
如果命中 3 了，将 新后newEnd 指向的节点移动到 旧后oldEnd 之后，移动指针oldStart++，newEnd--<br></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99f2deb9939a46f681b60dde32750ceb~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">if</span> (sameVnode(newEndVnode, oldStartVnode)) &#123; <span class="hljs-comment">// 新后与旧前</span>
    patchVnode(oldStartVnode, newEndVnode);
    <span class="hljs-comment">// 当 新后与旧前 命中的时候，此时要移动节点。移动 新后（旧前）指向的这个节点到老节点的 旧后的后面</span>
    <span class="hljs-comment">// 移动节点：只要插入一个已经在DOM树上 的节点，就会被移动</span>
    parentElm.insertBefore(oldStartVnode.elm, oldEndVnode.elm.nextSibling);
    oldStartVnode = oldCh[++oldStartIdx];
    newEndVnode = newCh[--newEndIdx];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果没命中，就接着比较下一种情况。</p>
<p>4、新前 newStart 与旧后 oldEnd<br>
如果命中 4 了，将 新前newStart 指向的节点移动到 旧前oldStart 之前，oldEnd--，newStart++<br></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a6af658f6174edfb8322df12491a289~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">if</span> (sameVnode(newStartVnode, oldEndVnode)) &#123; <span class="hljs-comment">// 新前与旧后</span>
    patchVnode(oldEndVnode, newStartVnode);
    <span class="hljs-comment">// 当 新前与旧后 命中的时候，此时要移动节点。移动 新前（旧后）指向的这个节点到老节点的 旧前的前面</span>
    <span class="hljs-comment">// 移动节点：只要插入一个已经在DOM树上 的节点，就会被移动</span>
    parentElm.insertBefore(oldEndVnode.elm, oldStartVnode.elm);
    oldEndVnode = oldCh[--oldEndIdx];
    newStartVnode = newCh[++newStartIdx];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>5、四种都没命中，遍历oldVnode中的key
找到了就移动位置，移动指针newStart++
用例子分析如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> vnode1 = h(<span class="hljs-string">'ul'</span>, &#123;&#125;, [
  h(<span class="hljs-string">'li'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'A'</span> &#125;, <span class="hljs-string">'A'</span>),
  h(<span class="hljs-string">'li'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'B'</span> &#125;, <span class="hljs-string">'B'</span>),
  h(<span class="hljs-string">'li'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'C'</span> &#125;, <span class="hljs-string">'C'</span>),
  h(<span class="hljs-string">'li'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'D'</span> &#125;, <span class="hljs-string">'D'</span>),
  h(<span class="hljs-string">'li'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'E'</span> &#125;, <span class="hljs-string">'E'</span>),
])

patch(container, vnode1)

btn.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> vnode2 = h(<span class="hljs-string">'ul'</span>, &#123;&#125;, [
    h(<span class="hljs-string">'li'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'B'</span> &#125;, <span class="hljs-string">'B'</span>),
    h(<span class="hljs-string">'li'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'Q'</span> &#125;, <span class="hljs-string">'Q'</span>),
    h(<span class="hljs-string">'li'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'A'</span> &#125;, <span class="hljs-string">'A'</span>),
    h(<span class="hljs-string">'li'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'D'</span> &#125;, <span class="hljs-string">'D'</span>),
  ])
  patch(vnode1, vnode2)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/763b85008dc742a88f0a543aee67b374~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过这个流程，我们可以写出下面的代码：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> keyMap = <span class="hljs-literal">null</span>;
<span class="hljs-comment">// 开始循环</span>
  <span class="hljs-keyword">while</span> (oldStartIdx <= oldEndIdx && newStartIdx <= newEndIdx) &#123;
    <span class="hljs-comment">// 首先不是判断四种命中，而是要略过已经加undefined标记的东西</span>
    <span class="hljs-keyword">if</span> (oldStartVnode == <span class="hljs-literal">null</span>) &#123;
      oldStartVnode = oldCh[++oldStartIdx];
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oldEndVnode == <span class="hljs-literal">null</span>) &#123;
      oldEndVnode = oldCh[--oldEndIdx];
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (newStartVnode == <span class="hljs-literal">null</span>) &#123;
      newStartVnode = newCh[++newStartIdx];
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (newEndVnode == <span class="hljs-literal">null</span>) &#123;
      newEndVnode = newCh[--newEndIdx];
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldStartVnode, newStartVnode)) &#123; <span class="hljs-comment">// 新前与旧前</span>
      patchVnode(oldStartVnode, newStartVnode)
      <span class="hljs-comment">// 移动指针</span>
      oldStartVnode = oldCh[++oldStartIdx]
      newStartVnode = newCh[++newStartIdx]
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(newEndVnode, oldEndVnode)) &#123; <span class="hljs-comment">// 新后与旧后</span>
      patchVnode(oldEndVnode, newEndVnode)
      <span class="hljs-comment">// 移动指针</span>
      oldEndVnode = oldCh[--oldEndIdx]
      newEndVnode = newCh[--newEndIdx]
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(newEndVnode, oldStartVnode)) &#123; <span class="hljs-comment">// 新后与旧前</span>
      patchVnode(oldStartVnode, newEndVnode);
      <span class="hljs-comment">// 当 新后与旧前 命中的时候，此时要移动节点。移动 新后（旧前）指向的这个节点到老节点的 旧后的后面</span>
      <span class="hljs-comment">// 移动节点：只要插入一个已经在DOM树上 的节点，就会被移动</span>
      parentElm.insertBefore(oldStartVnode.elm, oldEndVnode.elm.nextSibling);
      oldStartVnode = oldCh[++oldStartIdx];
      newEndVnode = newCh[--newEndIdx];
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(newStartVnode, oldEndVnode)) &#123; <span class="hljs-comment">// 新前与旧后</span>
      patchVnode(oldEndVnode, newStartVnode);
      <span class="hljs-comment">// 当 新前与旧后 命中的时候，此时要移动节点。移动 新前（旧后）指向的这个节点到老节点的 旧前的前面</span>
      <span class="hljs-comment">// 移动节点：只要插入一个已经在DOM树上 的节点，就会被移动</span>
      parentElm.insertBefore(oldEndVnode.elm, oldStartVnode.elm);
      oldEndVnode = oldCh[--oldEndIdx];
      newStartVnode = newCh[++newStartIdx];
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 用这种方式替换每次遍历操作 很优雅</span>
      <span class="hljs-keyword">if</span> (!keyMap) &#123;
        keyMap = &#123;&#125;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = oldStartIdx; i <= oldEndIdx; i++) &#123;
          <span class="hljs-keyword">const</span> key = oldCh[i].key
          <span class="hljs-keyword">if</span> (key) &#123;
            keyMap[key] = i
          &#125;
        &#125;
      &#125;
      <span class="hljs-comment">// 寻找当前项（newStartIdx）在keyMap中映射的序号</span>
      <span class="hljs-keyword">const</span> idxInOld = keyMap[newStartVnode.key];
      <span class="hljs-keyword">if</span> (!idxInOld) &#123;
        <span class="hljs-comment">// 如果 idxInOld 是 undefined 说明是全新的项，要插入</span>
        <span class="hljs-comment">// 被加入的项（就是newStartVnode这项)现不是真正的DOM节点</span>
        <span class="hljs-keyword">const</span> dom = createElement(newStartVnode)
        parentElm.insertBefore(dom, oldStartVnode.elm);
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 说明不是全新的项，要移动</span>
        <span class="hljs-keyword">const</span> elmToMove = oldCh[idxInOld];
        patchVnode(elmToMove, newStartVnode);
        <span class="hljs-comment">// 把这项设置为undefined，表示我已经处理完这项了</span>
        oldCh[idxInOld] = <span class="hljs-literal">undefined</span>;
        <span class="hljs-comment">// 移动</span>
        parentElm.insertBefore(elmToMove.elm, oldStartVnode.elm);
      &#125;
      newStartVnode = newCh[++newStartIdx];
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>6、while循环结束后</p>
<p>循环结束后，有两种情况：</p>
<ul>
<li>newStartIdx<=newEndIdx<br></li>
</ul>
<p>说明newVnode还有剩余节点没处理完成，所以要添加这些节点</p>
<ul>
<li>oldStartIdx<=oldEndIdx<br></li>
</ul>
<p>说明oldVnode还有剩余节点没处理完成，所以要删除这些节点</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 循环结束</span>
<span class="hljs-keyword">if</span> (newStartIdx <= newEndIdx) &#123;
  <span class="hljs-comment">// 说明newVndoe还有剩余节点没有处理，所以要添加这些节点</span>
  <span class="hljs-keyword">const</span> before = oldCh[oldStartIdx] == <span class="hljs-literal">null</span> ? <span class="hljs-literal">null</span> : oldCh[oldStartIdx].elm;
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = newStartIdx; i <= newEndIdx; i++) &#123;
    <span class="hljs-keyword">const</span> dom = createElement(newCh[i])
    parentElm.insertBefore(dom, before);
  &#125;
&#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oldStartIdx <= oldEndIdx) &#123;
  <span class="hljs-comment">// 说明oldVnode还有剩余节点没有处理，所以要删除这些节点</span>
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = oldStartIdx; i <= oldEndIdx; i++) &#123;
    <span class="hljs-keyword">if</span> (oldCh[i]) &#123;
      parentElm.removeChild(oldCh[i].elm);
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此，diff算法已大工告成！！！</p>
<p>用上面的例子演示：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> vnode1 = h(<span class="hljs-string">'ul'</span>, &#123;&#125;, [
  h(<span class="hljs-string">'li'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'A'</span> &#125;, <span class="hljs-string">'A'</span>),
  h(<span class="hljs-string">'li'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'B'</span> &#125;, <span class="hljs-string">'B'</span>),
  h(<span class="hljs-string">'li'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'C'</span> &#125;, <span class="hljs-string">'C'</span>),
  h(<span class="hljs-string">'li'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'D'</span> &#125;, <span class="hljs-string">'D'</span>),
  h(<span class="hljs-string">'li'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'E'</span> &#125;, <span class="hljs-string">'E'</span>),
])

patch(container, vnode1)

btn.onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> vnode2 = h(<span class="hljs-string">'ul'</span>, &#123;&#125;, [
    h(<span class="hljs-string">'li'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'B'</span> &#125;, <span class="hljs-string">'B'</span>),
    h(<span class="hljs-string">'li'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'Q'</span> &#125;, <span class="hljs-string">'Q'</span>),
    h(<span class="hljs-string">'li'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'A'</span> &#125;, <span class="hljs-string">'A'</span>),
    h(<span class="hljs-string">'li'</span>, &#123; <span class="hljs-attr">key</span>: <span class="hljs-string">'D'</span> &#125;, <span class="hljs-string">'D'</span>),
  ])
  patch(vnode1, vnode2)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f658506bfade4a1c89d053a3601d483f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-17">四、patch函数整体代码</h2>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> vnode <span class="hljs-keyword">from</span> <span class="hljs-string">'./vnode.js'</span>
<span class="hljs-keyword">import</span> api <span class="hljs-keyword">from</span> <span class="hljs-string">'./htmldomapi.js'</span>

<span class="hljs-comment">// 是不是虚拟节点</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">isVnode</span>(<span class="hljs-params">vnode</span>) </span>&#123;
  <span class="hljs-keyword">return</span> vnode.sel === <span class="hljs-string">''</span> || vnode.sel !== <span class="hljs-literal">undefined</span>;
&#125;

<span class="hljs-comment">// 把oldVnode包装成虚拟节点</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">emptyNodeAt</span>(<span class="hljs-params">elm</span>) </span>&#123;
  <span class="hljs-keyword">return</span> vnode(
    api.tagName(elm).toLowerCase(),
    &#123;&#125;,
    [],
    <span class="hljs-literal">undefined</span>,
    elm
  );
&#125;

<span class="hljs-comment">// 是不是同一个虚拟节点</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sameVnode</span>(<span class="hljs-params">vnode1, vnode2</span>) </span>&#123;
  <span class="hljs-keyword">return</span> vnode1.key === vnode2.key && vnode1.sel === vnode2.sel
&#125;

<span class="hljs-comment">// 真正创建节点，将 vnode 创建为 DOM 但不进行插入操作</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createElement</span>(<span class="hljs-params">vnode</span>) </span>&#123;
  <span class="hljs-comment">// 创建DOM节点</span>
  <span class="hljs-keyword">let</span> domNode = <span class="hljs-built_in">document</span>.createElement(vnode.sel)
  <span class="hljs-comment">// 有子节点还是有文本</span>
  <span class="hljs-keyword">if</span> (vnode.text !== <span class="hljs-string">''</span> && (vnode.children === <span class="hljs-literal">undefined</span> || vnode.children.length === <span class="hljs-number">0</span>)) &#123;
    <span class="hljs-comment">// 他内部是文本</span>
    domNode.innerText = vnode.text
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (<span class="hljs-built_in">Array</span>.isArray(vnode.children) && vnode.children.length > <span class="hljs-number">0</span>) &#123;
    <span class="hljs-comment">// 内部是子节点，就要递归创建节点</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < vnode.children.length; i++) &#123;
      <span class="hljs-comment">// 得到当前children</span>
      <span class="hljs-keyword">let</span> ch = vnode.children[i]
      <span class="hljs-comment">// 创建出它的dom，一旦调用了createElement意味着：创建出dom了，并且它的elm属性指向了创建出的dom，但是还没有上树</span>
      <span class="hljs-keyword">let</span> chDom = createElement(ch)
      <span class="hljs-comment">// 上树</span>
      domNode.appendChild(chDom)
    &#125;
  &#125;
  <span class="hljs-comment">// 补充elm属性</span>
  vnode.elm = domNode
  <span class="hljs-comment">// 返回elm 纯dom对象</span>
  <span class="hljs-keyword">return</span> vnode.elm
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patchVnode</span>(<span class="hljs-params">oldVnode, newVnode</span>) </span>&#123;
  <span class="hljs-comment">// 在内存中是同一个对象</span>
  <span class="hljs-keyword">if</span> (oldVnode === newVnode) <span class="hljs-keyword">return</span>
  <span class="hljs-keyword">if</span> (newVnode.text !== <span class="hljs-literal">undefined</span> && (newVnode.children === <span class="hljs-literal">undefined</span> || newVnode.children.length === <span class="hljs-number">0</span>)) &#123;
    <span class="hljs-comment">// 新vnode有text属性</span>
    <span class="hljs-keyword">if</span> (newVnode.text !== oldVnode.text) &#123;
      oldVnode.elm.innerText = newVnode.text
    &#125;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 新vnode没有text属性</span>
    <span class="hljs-keyword">if</span> (oldVnode.children !== <span class="hljs-literal">undefined</span> && oldVnode.children.length > <span class="hljs-number">0</span>) &#123;
      <span class="hljs-comment">// 老的有children</span>
      <span class="hljs-comment">// 最复杂的情况</span>
      updateChildren(oldVnode.elm, oldVnode.children, newVnode.children)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 老的没有children 新的有children</span>
      <span class="hljs-comment">// 第一步：清空老节点内容</span>
      oldVnode.elm.innerText = <span class="hljs-string">''</span>
      <span class="hljs-comment">// 第二步：便利新的vnode子节点 创建DOM上树</span>
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < newVnode.children.length; i++) &#123;
        <span class="hljs-keyword">let</span> dom = createElement(newVnode.children[i])
        oldVnode.elm.appendChild(dom)
      &#125;
    &#125;
  &#125;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateChildren</span>(<span class="hljs-params">parentElm, oldCh, newCh</span>) </span>&#123;
  <span class="hljs-keyword">let</span> oldStartIdx = <span class="hljs-number">0</span> <span class="hljs-comment">// 旧前</span>
  <span class="hljs-keyword">let</span> newStartIdx = <span class="hljs-number">0</span> <span class="hljs-comment">// 新前</span>
  <span class="hljs-keyword">let</span> oldEndIdx = oldCh.length - <span class="hljs-number">1</span> <span class="hljs-comment">// 旧后</span>
  <span class="hljs-keyword">let</span> newEndIdx = newCh.length - <span class="hljs-number">1</span> <span class="hljs-comment">// 新后</span>
  <span class="hljs-keyword">let</span> oldStartVnode = oldCh[<span class="hljs-number">0</span>] <span class="hljs-comment">// 旧前节点</span>
  <span class="hljs-keyword">let</span> oldEndVnode = oldCh[oldEndIdx] <span class="hljs-comment">// 旧后节点</span>
  <span class="hljs-keyword">let</span> newStartVnode = newCh[<span class="hljs-number">0</span>] <span class="hljs-comment">// 新前节点</span>
  <span class="hljs-keyword">let</span> newEndVnode = newCh[newEndIdx] <span class="hljs-comment">// 新后节点</span>

  <span class="hljs-keyword">let</span> keyMap = <span class="hljs-literal">null</span>

  <span class="hljs-comment">// 开始循环</span>
  <span class="hljs-keyword">while</span> (oldStartIdx <= oldEndIdx && newStartIdx <= newEndIdx) &#123;
    <span class="hljs-comment">// 首先不是判断四种命中，而是要略过已经加undefined标记的东西</span>
    <span class="hljs-keyword">if</span> (oldStartVnode == <span class="hljs-literal">null</span>) &#123;
      oldStartVnode = oldCh[++oldStartIdx];
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oldEndVnode == <span class="hljs-literal">null</span>) &#123;
      oldEndVnode = oldCh[--oldEndIdx];
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (newStartVnode == <span class="hljs-literal">null</span>) &#123;
      newStartVnode = newCh[++newStartIdx];
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (newEndVnode == <span class="hljs-literal">null</span>) &#123;
      newEndVnode = newCh[--newEndIdx];
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(oldStartVnode, newStartVnode)) &#123; <span class="hljs-comment">// 新前与旧前</span>
      patchVnode(oldStartVnode, newStartVnode)
      <span class="hljs-comment">// 移动指针</span>
      oldStartVnode = oldCh[++oldStartIdx]
      newStartVnode = newCh[++newStartIdx]
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(newEndVnode, oldEndVnode)) &#123; <span class="hljs-comment">// 新后与旧后</span>
      patchVnode(oldEndVnode, newEndVnode)
      <span class="hljs-comment">// 移动指针</span>
      oldEndVnode = oldCh[--oldEndIdx]
      newEndVnode = newCh[--newEndIdx]
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(newEndVnode, oldStartVnode)) &#123; <span class="hljs-comment">// 新后与旧前</span>
      patchVnode(oldStartVnode, newEndVnode);
      <span class="hljs-comment">// 当 新后与旧前 命中的时候，此时要移动节点。移动 新后（旧前）指向的这个节点到老节点的 旧后的后面</span>
      <span class="hljs-comment">// 移动节点：只要插入一个已经在DOM树上 的节点，就会被移动</span>
      parentElm.insertBefore(oldStartVnode.elm, oldEndVnode.elm.nextSibling);
      oldStartVnode = oldCh[++oldStartIdx];
      newEndVnode = newCh[--newEndIdx];
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (sameVnode(newStartVnode, oldEndVnode)) &#123; <span class="hljs-comment">// 新前与旧后</span>
      patchVnode(oldEndVnode, newStartVnode);
      <span class="hljs-comment">// 当 新前与旧后 命中的时候，此时要移动节点。移动 新前（旧后）指向的这个节点到老节点的 旧前的前面</span>
      <span class="hljs-comment">// 移动节点：只要插入一个已经在DOM树上 的节点，就会被移动</span>
      parentElm.insertBefore(oldEndVnode.elm, oldStartVnode.elm);
      oldEndVnode = oldCh[--oldEndIdx];
      newStartVnode = newCh[++newStartIdx];
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">if</span> (!keyMap) &#123;
        keyMap = &#123;&#125;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = oldStartIdx; i <= oldEndIdx; i++) &#123;
          <span class="hljs-keyword">const</span> key = oldCh[i].key
          <span class="hljs-keyword">if</span> (key) &#123;
            keyMap[key] = i
          &#125;
        &#125;
      &#125;
      <span class="hljs-comment">// 寻找当前项（newStartIdx）在keyMap中映射的序号</span>
      <span class="hljs-keyword">const</span> idxInOld = keyMap[newStartVnode.key];
      <span class="hljs-keyword">if</span> (!idxInOld) &#123;
        <span class="hljs-comment">// 如果 idxInOld 是 undefined 说明是全新的项，要插入</span>
        <span class="hljs-comment">// 被加入的项（就是newStartVnode这项)现不是真正的DOM节点</span>
        <span class="hljs-keyword">const</span> dom = createElement(newStartVnode)
        parentElm.insertBefore(dom, oldStartVnode.elm);
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-comment">// 说明不是全新的项，要移动</span>
        <span class="hljs-keyword">const</span> elmToMove = oldCh[idxInOld];
        patchVnode(elmToMove, newStartVnode);
        <span class="hljs-comment">// 把这项设置为undefined，表示我已经处理完这项了</span>
        oldCh[idxInOld] = <span class="hljs-literal">undefined</span>;
        <span class="hljs-comment">// 移动，调用insertBefore也可以实现移动。</span>
        parentElm.insertBefore(elmToMove.elm, oldStartVnode.elm);
      &#125;
      newStartVnode = newCh[++newStartIdx];
    &#125;
  &#125;

  <span class="hljs-comment">// 循环结束</span>
  <span class="hljs-keyword">if</span> (newStartIdx <= newEndIdx) &#123;
    <span class="hljs-comment">// 说明newVndoe还有剩余节点没有处理，所以要添加这些节点</span>
    <span class="hljs-keyword">const</span> before = oldCh[oldStartIdx] == <span class="hljs-literal">null</span> ? <span class="hljs-literal">null</span> : oldCh[oldStartIdx].elm;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = newStartIdx; i <= newEndIdx; i++) &#123;
      <span class="hljs-keyword">const</span> dom = createElement(newCh[i])
      parentElm.insertBefore(dom, before);
    &#125;
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (oldStartIdx <= oldEndIdx) &#123;
    <span class="hljs-comment">// 说明oldVnode还有剩余节点没有处理，所以要删除这些节点</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = oldStartIdx; i <= oldEndIdx; i++) &#123;
      <span class="hljs-keyword">if</span> (oldCh[i]) &#123;
        parentElm.removeChild(oldCh[i].elm);
      &#125;
    &#125;
  &#125;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">patch</span>(<span class="hljs-params">oldVnode, newVnode</span>) </span>&#123;
  <span class="hljs-comment">// 判断是不是虚拟节点</span>
  <span class="hljs-keyword">if</span> (!isVnode(oldVnode)) &#123;
    <span class="hljs-comment">// 不是虚拟节点 则包装成虚拟节点</span>
    oldVnode = emptyNodeAt(oldVnode)
  &#125;
  <span class="hljs-keyword">if</span> (sameVnode(oldVnode, newVnode)) &#123;
    patchVnode(oldVnode, newVnode)
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-comment">// 暴力插入新的，删除新的</span>
    <span class="hljs-keyword">let</span> newVnodeElm = createElement(newVnode)
    <span class="hljs-keyword">if</span> (oldVnode.elm.parentNode && newVnodeElm) &#123;
      oldVnode.elm.parentNode.insertBefore(newVnodeElm, oldVnode.elm)
      <span class="hljs-comment">// 删除老节点</span>
      oldVnode.elm.parentNode.removeChild(oldVnode.elm)
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果这篇文章对您有帮助，请给个赞吧~~~</p></div>  
</div>
            