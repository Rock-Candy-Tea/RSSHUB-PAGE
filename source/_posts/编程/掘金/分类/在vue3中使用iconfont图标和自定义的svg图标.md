
---
title: '在vue3中使用iconfont图标和自定义的svg图标'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8154741160164285b295ce8c39a0eec3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 26 Aug 2021 07:10:58 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8154741160164285b295ce8c39a0eec3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">创建一个Icon组件，供自定义的svg图标使用和iconfont图标使用</h2>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"icon"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">use</span> <span class="hljs-attr">:href</span>=<span class="hljs-string">"id"</span>></span><span class="hljs-tag"></<span class="hljs-name">use</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">svg</span>></span></span>
</template>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; defineComponent, ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'Icon'</span>,
  <span class="hljs-attr">props</span>: &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">String</span>,
  &#125;,
  <span class="hljs-function"><span class="hljs-title">setup</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-keyword">const</span> id = ref(<span class="hljs-string">`#<span class="hljs-subst">$&#123;props.name&#125;</span>`</span>)
    <span class="hljs-keyword">return</span> &#123;
      id,
    &#125;
  &#125;,
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
<span class="hljs-selector-class">.icon</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">vertical-align</span>: -<span class="hljs-number">0.15em</span>;
  fill: currentColor;
  <span class="hljs-attribute">overflow</span>: hidden;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">如何inconfont图标</h2>
<ol>
<li>访问iconfont官网，保存图标到自己创建的项目中，然后点击symbol的形式引入。</li>
<li>将js文件引入public/index.html中。</li>
<li>使用。直接通过class来控制图标样式和大小。class会直接绑定到Icon组件的根组件上。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js">
  <Icon name=<span class="hljs-string">"icon-weixin"</span> <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"icon-weixin"</span>></Icon>
  <span class="hljs-comment">// 通过class来控制图标的样式</span>
  .icon-weixin &#123;
      <span class="hljs-attr">width</span>: 20px;
      height: 20px;
      color: red;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">定义和使用自定义图标</h2>
<ol>
<li>在public/index.html中设计svg图标。</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">svg</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">defs</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">symbol</span> <span class="hljs-attr">viewBox</span>=<span class="hljs-string">"0 0 100 100"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"iconRect"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">rect</span> <span class="hljs-attr">x</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">y</span>=<span class="hljs-string">"0"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"100"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"100"</span>></span><span class="hljs-tag"></<span class="hljs-name">rect</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">symbol</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">defs</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">svg</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>使用。</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><Icon name=<span class="hljs-string">"iconRect"</span> <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"icon-rect"</span>></Icon>
  <span class="hljs-comment">// 通过class来控制图标的样式</span>
  .icon-rect &#123;
      <span class="hljs-attr">width</span>: 20px;
      height: 20px;
      color: red;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8154741160164285b295ce8c39a0eec3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            