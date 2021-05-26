
---
title: 'js中compositionstart和compositionend事件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e98aecfbbd04812a823991444dfb18a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 25 May 2021 18:41:26 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e98aecfbbd04812a823991444dfb18a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>大家好，我是前端队长Daotin，想要获取更多前端精彩内容，关注我，解锁前端成长新姿势。</p>
<blockquote>
<p>最近热门文章：</p>
<ul>
<li><a href="https://juejin.cn/post/6963071339108237319" target="_blank">图片瀑布流，就是如此简单（so easy）</a></li>
<li><a href="https://juejin.cn/post/6961968236837470216" target="_blank">梳理ajax跨域常用4种解决方案（简单易懂）</a></li>
<li><a href="https://juejin.cn/post/6961226664869101605" target="_blank">Vue.js命名风格指南（易记版）</a></li>
</ul>
</blockquote>
<p>以下正文：</p>
<h2 data-id="heading-0">需求</h2>
<p>最近有个需求，根据input输入的文字进行列表过滤。这是个很常见的需求。于是大致的代码如下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">:value</span>=<span class="hljs-string">"filterText"</span> @<span class="hljs-attr">input</span>=<span class="hljs-string">"onInput"</span> /></span>
    <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in filteredList"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"item"</span>></span>
        &#123;&#123; item &#125;&#125;
      <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"app"</span>,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">filterText</span>: <span class="hljs-string">""</span>,
      <span class="hljs-attr">list</span>: [
        <span class="hljs-string">"爱与希望"</span>,
        <span class="hljs-string">"花海"</span>,
        <span class="hljs-string">"Mojito"</span>,
        <span class="hljs-string">"最长的电影"</span>,
        <span class="hljs-string">"爷爷泡的茶"</span>
      ]
    &#125;;
  &#125;,
  <span class="hljs-attr">computed</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">filteredList</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.filterText) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.list;
      &#125;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.list.filter(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.indexOf(<span class="hljs-built_in">this</span>.filterText) > -<span class="hljs-number">1</span>);
    &#125;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">onInput</span>(<span class="hljs-params">e</span>)</span> &#123;
      <span class="hljs-built_in">this</span>.filterText = e.target.value;
    &#125;
  &#125;
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在输入框中监听input事件，然后触发filteredList列表的改变。</p>
<p>一切都是那么自然。</p>
<p>然而当我们输入中文的时候，由于拼音会先显示，导致在输入中文的过程中，触发筛选的列表空的，最后中文显示出来的时候，才会有显示结果。</p>
<h2 data-id="heading-1">compositionstart和compositionend</h2>
<p>于是在网上搜索有这么两个事件， <code>compositionstart</code>和 <code>compositionend</code></p>
<blockquote>
<p>MDN: <a href="https://developer.mozilla.org/zh-CN/docs/Web/Events/compositionstart" target="_blank" rel="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a></p>
</blockquote>
<p><strong>当用户使用拼音输入法开始输入汉字时，compositionstart事件就会被触发。当文本段落的组成完成或取消时, compositionend 事件将被触发。</strong></p>
<p>也就是说，在我们开始输入中文的时候会触发一次compositionstart事件，中文输入过程中不会再出发compositionstart事件，最后输入中文完成触发compositionend 事件。</p>
<blockquote>
<p>而且经过试验发现，在输入中文的时候，compositionstart先于input事件触发。</p>
</blockquote>
<p>有了这个前提那这就好办了，我只需打个标 <code>lock</code>，当compositionstart触发时， <code>lock=true</code>，当compositionend触发时， <code>lock=false</code>。只有在lock为false的时候，才执行input事件中的筛选操作。</p>
<p>代码变成如下：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">:value</span>=<span class="hljs-string">"filterText"</span> 
        @<span class="hljs-attr">input</span>=<span class="hljs-string">"onInput"</span> 
        @<span class="hljs-attr">compositionstart</span>=<span class="hljs-string">"onCompositionStart"</span>
        @<span class="hljs-attr">compositionend</span>=<span class="hljs-string">"onCompositionEnd"</span>
        /></span>
    <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">v-for</span>=<span class="hljs-string">"item in filteredList"</span> <span class="hljs-attr">:key</span>=<span class="hljs-string">"item"</span>></span>
        &#123;&#123; item &#125;&#125;
      <span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">"app"</span>,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">filterText</span>: <span class="hljs-string">""</span>,
      <span class="hljs-attr">list</span>: [
        <span class="hljs-string">"爱与希望"</span>,
        <span class="hljs-string">"花海"</span>,
        <span class="hljs-string">"Mojito"</span>,
        <span class="hljs-string">"最长的电影"</span>,
        <span class="hljs-string">"爷爷泡的茶"</span>
      ]，
      lock; <span class="hljs-literal">false</span>, <span class="hljs-comment">// 打标</span>
    &#125;;
  &#125;,
  <span class="hljs-attr">computed</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">filteredList</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.filterText) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.list;
      &#125;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.list.filter(<span class="hljs-function"><span class="hljs-params">item</span> =></span> item.indexOf(<span class="hljs-built_in">this</span>.filterText) > -<span class="hljs-number">1</span>);
    &#125;
  &#125;,
  <span class="hljs-attr">methods</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">onInput</span>(<span class="hljs-params">e</span>)</span> &#123;
      <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">this</span>.lock) &#123;
        <span class="hljs-built_in">this</span>.filterText = e.target.value;
      &#125;
    &#125;，
    <span class="hljs-function"><span class="hljs-title">onCompositionStart</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">this</span>.lock = <span class="hljs-literal">true</span>;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">onCompositionEnd</span>(<span class="hljs-params">e</span>)</span> &#123;
      <span class="hljs-built_in">this</span>.filterText = e.data;
      <span class="hljs-built_in">this</span>.lock = <span class="hljs-literal">false</span>;
    &#125;
  &#125;
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">v-model形式</h2>
<p>上面的代码我们使用的不是vue的 <code>v-model</code>双向绑定的形式，如果你使用 <code>v-model</code>的形式，你会发现在输入中文的过程中不会触发input事件。</p>
<p>查看vue的源码 <code>src/platforms/web/runtime/directives/model.js</code>，有这么几行代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  inserted (el, binding, vnode) &#123;
    <span class="hljs-keyword">if</span> (vnode.tag === <span class="hljs-string">'select'</span>) &#123;
      setSelected(el, binding, vnode.context)
      el._vOptions = [].map.call(el.options, getValue)
    &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (vnode.tag === <span class="hljs-string">'textarea'</span> || isTextInputType(el.type)) &#123;
      el._vModifiers = binding.modifiers
      <span class="hljs-keyword">if</span> (!binding.modifiers.lazy) &#123;
        <span class="hljs-comment">// Safari < 10.2 & UIWebView doesn't fire compositionend when</span>
        <span class="hljs-comment">// switching focus before confirming composition choice</span>
        <span class="hljs-comment">// this also fixes the issue where some browsers e.g. iOS Chrome</span>
        <span class="hljs-comment">// fires "change" instead of "input" on autocomplete.</span>
        el.addEventListener(<span class="hljs-string">'change'</span>, onCompositionEnd)
        <span class="hljs-keyword">if</span> (!isAndroid) &#123;
          el.addEventListener(<span class="hljs-string">'compositionstart'</span>, onCompositionStart)
          el.addEventListener(<span class="hljs-string">'compositionend'</span>, onCompositionEnd)
        &#125;
        <span class="hljs-comment">/* istanbul ignore if */</span>
        <span class="hljs-keyword">if</span> (isIE9) &#123;
          el.vmodel = <span class="hljs-literal">true</span>
        &#125;
      &#125;
    &#125;
  &#125;
&#125;

<span class="hljs-comment">//...</span>

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onCompositionStart</span> (<span class="hljs-params">e</span>) </span>&#123;
  e.target.composing = <span class="hljs-literal">true</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onCompositionEnd</span> (<span class="hljs-params">e</span>) </span>&#123;
  <span class="hljs-comment">// prevent triggering an input event for no reason</span>
  <span class="hljs-keyword">if</span> (!e.target.composing) <span class="hljs-keyword">return</span>
  e.target.composing = <span class="hljs-literal">false</span>
  trigger(e.target, <span class="hljs-string">'input'</span>)
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">trigger</span> (<span class="hljs-params">el, type</span>) </span>&#123;
  <span class="hljs-keyword">const</span> e = <span class="hljs-built_in">document</span>.createEvent(<span class="hljs-string">'HTMLEvents'</span>)
  e.initEvent(type, <span class="hljs-literal">true</span>, <span class="hljs-literal">true</span>)
  el.dispatchEvent(e)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以发现，原来vue早已做了相同的操作，所以v-model帮我们做了很多优化处理，这也是vue如此优秀的原因之一。</p>
<hr>
<p>想看更多精彩内容，关注我获取更多前端技术与个人成长相关内容，我相信有趣的人终会相遇！</p>
<p>听说点赞的人，一个月后都会运气爆棚，升职加薪哦~</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e98aecfbbd04812a823991444dfb18a~tplv-k3u1fbpfcp-watermark.image" alt="微信图片_20210427113225.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            