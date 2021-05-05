
---
title: '【Vue】Vue-i18n 变量使用以及采坑总结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/982e0b549784445cb3a64d7a606a9f7e~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 04 May 2021 17:29:19 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/982e0b549784445cb3a64d7a606a9f7e~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>笔者目前在 <code>Shopee</code> 工作，我们公司主要业务是跨境电商，业务涉及到多个国家，所以我们各个系统都会涉及到国际化翻译。我们 <code>Vue</code> 项目技术上采用了 <code>Vue-i18n</code> 这个库。</p>
<p>今天就聊聊这个库的一个功能，在国际化时候使用变量。在翻译中使用变量是一个非常常见的场景，最简单的例子，比如以下的文案要国际化</p>
<pre><code class="copyable">I am Gopal.I am from China
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但其中 <strong>Gopal</strong> 和 <strong>China</strong> 是需要变量传入的，这个时候我们怎么办呢？</p>
<h2 data-id="heading-1">简单的传参</h2>
<p>首先我们定义要翻译的字符如下</p>
<pre><code class="copyable">"introTips": "I am &#123;name&#125;.I am from &#123;region&#125;"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在模板中使用</p>
<pre><code class="hljs language-js copyable" lang="js">$t(<span class="hljs-string">'introTips'</span>, &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'Gopal一号'</span>, <span class="hljs-attr">region</span>: <span class="hljs-string">'China'</span> &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>就可以渲染出 <strong>I am Gopal 一号.I am from China</strong></p>
<h2 data-id="heading-2">需要给变量加个颜色</h2>
<p>假如说我们 <strong>Gopal</strong> 不仅仅是一个文案，还需要变成红色？我们该怎么办？我们可以直接使用 v-html 渲染 html。这个时候我们就要修改翻译的字符如下</p>
<pre><code class="copyable">introTipsTwo: "I am <span class='name'>&#123;name&#125;</span>.I am from &#123;region&#125;"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 v-html 直接渲染</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span>
  <span class="hljs-attr">class</span>=<span class="hljs-string">"text"</span>
  <span class="hljs-attr">v-html</span>=<span class="hljs-string">"$t('introTipsTwo', &#123; name: 'Gopal一号', region: 'China' &#125;)"</span>
></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>渲染结果如下</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">data-v-763db97b</span>=<span class="hljs-string">""</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"text"</span>></span>
  I am <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"name"</span>></span>Gopal一号<span class="hljs-tag"></<span class="hljs-name">span</span>></span>.I am from China
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/982e0b549784445cb3a64d7a606a9f7e~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210430112350433" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>注意：这个方法很可能引发 XSS 攻击，所以不推荐使用该方法</strong></p>
<h2 data-id="heading-3">使用 place 属性</h2>
<p>首先翻译的文案先改回最开始变量的版本</p>
<pre><code class="copyable">introTips: "I am &#123;name&#125;.I am from &#123;region&#125;"
<span class="copy-code-btn">复制代码</span></code></pre>
<p>直接使用 i18n 组件以及 place 属性，其中 path 指的是上面的 key，place 指定变量</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">i18n</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"introTips"</span> <span class="hljs-attr">tag</span>=<span class="hljs-string">"div"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"name"</span> <span class="hljs-attr">place</span>=<span class="hljs-string">"name"</span>></span>Gopal 二号<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">place</span>=<span class="hljs-string">"region"</span>></span>China<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"></<span class="hljs-name">i18n</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>渲染结果如下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">data-v-763db97b</span>=<span class="hljs-string">""</span>></span>
  I am <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">data-v-763db97b</span>=<span class="hljs-string">""</span> <span class="hljs-attr">place</span>=<span class="hljs-string">"name"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"name"</span>></span>Gopal 二号<span class="hljs-tag"></<span class="hljs-name">span</span>></span>.I am from <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">data-v-763db97b</span>=<span class="hljs-string">""</span> <span class="hljs-attr">place</span>=<span class="hljs-string">"region"</span>></span>China<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92248db34c124c5fad23872af4400488~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210430113555745" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们已经实现了我们的方案，但<strong>这个方法会在下个版本中被淘汰</strong>，仔细看，这不是 Vue 中的插槽么？没错，官方推荐的最终的解决方案是 Slot，用法跟上面的非常相似</p>
<h2 data-id="heading-4">最终的方案——Slot</h2>
<p>直接上代码：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">i18n</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"introTips"</span> <span class="hljs-attr">tag</span>=<span class="hljs-string">"div"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot:name</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"name"</span>></span>Gopal 三号<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot:region</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span>></span>China<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"></<span class="hljs-name">i18n</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>渲染的结果跟上面的类似</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">data-v-763db97b</span>=<span class="hljs-string">""</span>></span>
  I am <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">data-v-763db97b</span>=<span class="hljs-string">""</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"name"</span>></span>Gopal 三号<span class="hljs-tag"></<span class="hljs-name">span</span>></span>.I am from <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">data-v-763db97b</span>=<span class="hljs-string">""</span>></span>China<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">问题</h2>
<p>在项目中使用的时候，却报错了...</p>
<p>我的办法跟上面的可谓是一模一样...</p>
<h3 data-id="heading-6">报错</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">i18n</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"introTips"</span> <span class="hljs-attr">tag</span>=<span class="hljs-string">"div"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot:name</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"name"</span>></span>Gopal 三号<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot:region</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">span</span>></span>China<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
<span class="hljs-tag"></<span class="hljs-name">i18n</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">vue.esm.js:<span class="hljs-number">628</span> [Vue warn]: <span class="hljs-built_in">Error</span> <span class="hljs-keyword">in</span> nextTick: <span class="hljs-string">"TypeError: Cannot create property 'isRootInsert' on string 'You submit '"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b9a27bb13f15481b94833dd4842f7244~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我感觉我又要掉头发了...。</p>
<h3 data-id="heading-7">断点查看</h3>
<p><code>Google</code> 了一下这个报错以及看了一下报错的堆栈信息，看起来像是 vNode 渲染的问题，然后我在报错的地方打了一个断点，可以看到下面 children 中数组的各项并不都是 vnode，第一项就是字符串，这应该就是导致报错的罪魁祸首</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c82b3b8a0c94c6aaf80da98758a6286~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">阅读源码</h3>
<p>我看了一下 node_modules 中 <code>vue-i18n</code> 的源码，这里注意我目前使用的版本是 <strong>8.15.0</strong></p>
<p>发现在 i18n 这个函数式组件的源码中有两句非常奇怪的代码，这个函数式组件源码见<a href="https://github.com/kazupon/vue-i18n/blob/v8.15.0/src/components/interpolation.js#L42" target="_blank" rel="nofollow noopener noreferrer">链接</a></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'i18n'</span>,
  <span class="hljs-attr">functional</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-comment">// 留意这里</span>
    <span class="hljs-attr">tag</span>: &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-built_in">String</span>
    &#125;,
<span class="hljs-comment">// ...</span>
  &#125;,
  render (h: <span class="hljs-built_in">Function</span>, &#123; data, parent, props, slots &#125;: <span class="hljs-built_in">Object</span>) &#123;
    <span class="hljs-keyword">const</span> &#123; $i18n &#125; = parent
<span class="hljs-comment">// ...</span>
    <span class="hljs-keyword">const</span> &#123; path, locale, places &#125; = props
    <span class="hljs-keyword">const</span> params = slots()
    <span class="hljs-keyword">const</span> children = $i18n.i(
      path,
      locale,
      onlyHasDefaultPlace(params) || places
        ? useLegacyPlaces(params.default, places)
        : params
    )

    <span class="hljs-keyword">const</span> tag = props.tag || <span class="hljs-string">'span'</span>
    <span class="hljs-keyword">return</span> tag ? h(tag, data, children) : children
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>留意最后两行代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> tag = props.tag || <span class="hljs-string">'span'</span>
<span class="hljs-keyword">return</span> tag ? h(tag, data, children) : children
<span class="copy-code-btn">复制代码</span></code></pre>
<p>啊，这。。。<code>children</code> 是不是永远没有机会执行了？</p>
<p>我尝试直接 return 回 <code>children</code>。额成功了...</p>
<h3 data-id="heading-9">尝试升级版本</h3>
<p>我想了想，升级到较新的版本试下？</p>
<p>果然，这个组件修改了...，简化了一下代码，源码可见<a href="https://github.com/kazupon/vue-i18n/blob/v8.22.0/src/components/interpolation.js" target="_blank" rel="nofollow noopener noreferrer">链接</a></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'i18n'</span>,
  <span class="hljs-attr">functional</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-comment">// 留意这里</span>
    <span class="hljs-attr">tag</span>: &#123;
      <span class="hljs-attr">type</span>: [<span class="hljs-built_in">String</span>, <span class="hljs-built_in">Boolean</span>, <span class="hljs-built_in">Object</span>],
      <span class="hljs-attr">default</span>: <span class="hljs-string">'span'</span>
    &#125;
    <span class="hljs-comment">// ...</span>
  &#125;,
  render (h: <span class="hljs-built_in">Function</span>, &#123; data, parent, props, slots &#125;: <span class="hljs-built_in">Object</span>) &#123;
    <span class="hljs-comment">// ....</span>
<span class="hljs-comment">// 留意这里</span>
    <span class="hljs-keyword">const</span> tag = (!!props.tag && props.tag !== <span class="hljs-literal">true</span>) || props.tag === <span class="hljs-literal">false</span> ? props.tag : <span class="hljs-string">'span'</span>
    <span class="hljs-keyword">return</span> tag ? h(tag, data, children) : children
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的 tag 可以传 String，Boolean 和 Object</p>
<p>看了一下官方文档</p>
<blockquote>
<p>You can choose the root container's node type by specifying a <code>tag</code> prop. If omitted, it defaults to <code>'span'</code>. You can also set it to the boolean value <code>false</code> to insert the child nodes directly without creating a root element.</p>
</blockquote>
<p>简单来说 <strong>tag 可以传 false，这样就不需要在翻译的外层再多加一个节点了</strong></p>
<p>我再去找了一下修改这个 <a href="https://github.com/kazupon/vue-i18n/pull/878" target="_blank" rel="nofollow noopener noreferrer">PR</a> 以及对应的 <a href="https://github.com/kazupon/vue-i18n/issues/876" target="_blank" rel="nofollow noopener noreferrer">Issue</a></p>
<h3 data-id="heading-10">解决问题</h3>
<p>虽然看起来为了解决不需要配置根节点的问题的，但我感觉也可以解决我的问题，以下升级版本后，我修改了一下我的代码</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"test-container"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">i18n</span> <span class="hljs-attr">path</span>=<span class="hljs-string">"introTips"</span> <span class="hljs-attr">:tag</span>=<span class="hljs-string">"false"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot:name</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"name"</span>></span>Gopal 三号<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot:region</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">span</span>></span>China<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">i18n</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这回真的成功了，非常开心，最终它的渲染如下</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">data-v-0b89d11d</span>=<span class="hljs-string">""</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"test-container"</span>></span>
  <span class="hljs-comment"><!-- 这里外层没有节点了 --></span>
  I am <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">data-v-0b89d11d</span>=<span class="hljs-string">""</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"name"</span>></span>Gopal 三号<span class="hljs-tag"></<span class="hljs-name">span</span>></span>.I am from <span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">data-v-0b89d11d</span>=<span class="hljs-string">""</span>></span>China<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到这个时候渲染出来就没有最外层的 tag 了</p>
<h2 data-id="heading-11">总结</h2>
<p>本文介绍了 vue-i18n 变量的使用方法，几种方法都较为简单易懂。主要是记录了自己踩过的一个坑，也算是学到了一些经验</p>
<ul>
<li>当没有思路的时候，可以看看源码。可以直接 node_modules 中查看，甚至在 dist  文件中找到相对应的代码，断点调试</li>
<li>源码调试不仅仅对定位问题有所帮助，也可以扩宽视野。比如上面提到的 i18n 函数式组件的实现。我当时看的时候，假如让我来写，我可以写出来么？</li>
<li>留意官方的 ISSUE，不过这次前期我都找过，只是都不是我这个错误...</li>
<li>官方的文档英文比较全，中文版和英文版差异较大（应该是翻译滞后了）</li>
</ul>
<h2 data-id="heading-12">最后</h2>
<p>之前提到了，笔者在 Shopee 工作，有需要换工作的同学可以找我内推哈~</p>
<p>五月份专场非常多机会，具体可以查看 <a href="https://app.mokahr.com/apply/shopee/2963#/" target="_blank" rel="nofollow noopener noreferrer">链接</a>。一线大厂薪资，少加班（公司提倡高效工作），团队氛围好，晋升机会多，感兴趣的同学请抓紧时间，发送简历到我邮箱 <a href="mailto:15521091584@163.com">15521091584@163.com</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/151f4f8955644aebbceeff23b14f3d68~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            