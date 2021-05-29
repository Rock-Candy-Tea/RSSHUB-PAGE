
---
title: '用jQuery写出vue的味道，这个小插件真猛！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c68bd832a3a249bfa1bcb47d2b0c778b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 28 May 2021 06:49:21 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c68bd832a3a249bfa1bcb47d2b0c778b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>你肯定用过vue，别猜，我隔着屏幕都能读到你此刻的想法。但是，你想过用jquery写出的代码像vue一样简单，也具有响应式效果吗？话不多说，先来 show me the code：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;&#123;name&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;&#123;age&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">jq-on</span>=<span class="hljs-string">"click:grow"</span>></span>Grow<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  $(<span class="hljs-string">'#app'</span>)
      .vm(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'tom'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">10</span> &#125;)
      .fn(<span class="hljs-string">'grow'</span>, <span class="hljs-function"><span class="hljs-params">state</span> =></span> state.age ++)
      .mount()
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>怎么样有没有一种熟悉的味道？而这，仅仅靠一个几百行的jquery插件。
你只需要在你的页面中引入对应的插件文件：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://unpkg.com/jquery/dist/jquery.min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://unpkg.com/jqvm/dist/jqvm.min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>编译？构建？都没有，它只是一个jquery插件。当然，你也可以使用构建系统来做，比如：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; useJQuery &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'jqvm'</span>
<span class="hljs-keyword">import</span> jQuery <span class="hljs-keyword">from</span> <span class="hljs-string">'jquery'</span>

<span class="hljs-keyword">const</span> $ = useJQuery(jQuery)
<span class="hljs-keyword">const</span> view = $(<span class="hljs-string">`
  <template>
      <span>&#123;&#123;name&#125;&#125;</span>
      <span>&#123;&#123;age&#125;&#125;</span>
      <button jq-on="click:grow">Grow</button>
  </template>
`</span>)
    .vm(&#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'tom'</span>, <span class="hljs-attr">age</span>: <span class="hljs-number">10</span> &#125;)
    .fn(<span class="hljs-string">'grow'</span>, <span class="hljs-function"><span class="hljs-params">state</span> =></span> state.age ++)
    
view.mount(<span class="hljs-string">'#app'</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>和vue的响应式方式一样，你只需要直接修改state就可以让界面重新渲染。</p>
<p>指令控制？没问题的：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">jq-if</span>=<span class="hljs-string">"age > 10"</span>></span>I am older than 10.<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>循环？这个有点难搞，不过也没问题：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">jq-repeat</span>=<span class="hljs-string">"value,index in data traceby value.id"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;&#123;index + 1&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;&#123;value.name&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">span</span>></span>&#123;&#123;value.time&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>双向绑定？嗯，有的：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">jq-bind</span>=<span class="hljs-string">"age"</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>组件？这个稍微没那么好，勉强够用：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"box"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>width: &#123;&#123;width&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span>></span>height: &#123;&#123;height&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">my-box</span>></span><span class="hljs-tag"></<span class="hljs-name">my-box</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">const</span> box = $(<span class="hljs-string">'#box'</span>).vm(&#123; <span class="hljs-attr">width</span>: <span class="hljs-number">100</span>, <span class="hljs-attr">height</span>: <span class="hljs-number">100</span> &#125;)
  <span class="hljs-keyword">const</span> app = $(<span class="hljs-string">'#app'</span>).vm(&#123;&#125;)
      .component(<span class="hljs-string">'my-box'</span>, box) <span class="hljs-comment">// 把box注册为一个组件</span>
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是不是闻着有点vue的味道了？不过你放120万个心，它还是jquery，是你熟悉的味道，撸起来飞快如箭。</p>
<p>至于它怎么做到的，你应该听说过vue用Object.defineProperty拦截数据的原理，jQvm也是一样，不过它给state增加了 $set,$del,$get 方法，比如 state.$set('new_prop', 'value') 就可以了，怎样，简单。</p>
<p>在线小demo地址 <a href="https://unpkg.com/jqvm@3.2.0/index.html" target="_blank" rel="nofollow noopener noreferrer">unpkg.com/jqvm@3.2.0/…</a> ，
最后放上仓库地址 <a href="https://github.com/tangshuang/jqvm" target="_blank" rel="nofollow noopener noreferrer">github.com/tangshuang/…</a>
热爱编程的小伙伴，都会送上一个star。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c68bd832a3a249bfa1bcb47d2b0c778b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>关于作者<br>
前端工程师一枚<br>
公众号：wwwtangshuangnet</p></div>  
</div>
            