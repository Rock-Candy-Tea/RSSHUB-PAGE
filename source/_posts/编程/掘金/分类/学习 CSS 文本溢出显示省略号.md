
---
title: '学习 CSS 文本溢出显示省略号'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f13ba298153c41c8bc15742e1bf7092b~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 05 Jun 2021 05:51:54 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f13ba298153c41c8bc15742e1bf7092b~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第5天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p>在开发中经常会用到文本溢出省略打点，为了更好的记住它，现在开始深入了解。</p>
<h2 data-id="heading-0">单行文本显示省略号</h2>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    <span class="hljs-selector-class">.text</span> &#123;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
      <span class="hljs-attribute">white-space</span>: nowrap;
      <span class="hljs-attribute">overflow</span>: hidden;
      <span class="hljs-attribute">text-overflow</span>: ellipsis;
    &#125;
  </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"text"</span>></span>单行文本显示省略号<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f13ba298153c41c8bc15742e1bf7092b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>使用<code>white-space属性</code>设置不换行、<code>overflow属性</code>隐藏超出部分,<code>text-overflow属性</code>添加省略号。需注意必须有固定宽度才会出现效果。</li>
</ul>
<ol>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/white-space" target="_blank" rel="nofollow noopener noreferrer"><code>white-space属性</code></a> 用来设置如何处理元素中的空白。</li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/overflow" target="_blank" rel="nofollow noopener noreferrer"><code>overflow属性</code></a> 定义当一个元素的内容太大而无法适应时，块级格式化上下文如何处理。它是 <code>overflow-x 和 overflow-y</code>的简写属性 。</li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/overflow" target="_blank" rel="nofollow noopener noreferrer"><code>text-overflow属性</code></a> 确定如何向用户发出未显示的溢出内容信号。它可以被剪切，显示一个省略号（'...'）或显示一个自定义字符串。</li>
</ol>
<h2 data-id="heading-1">多行文本显示省略号</h2>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    <span class="hljs-selector-class">.text</span> &#123;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
      <span class="hljs-attribute">overflow</span>: hidden;
      <span class="hljs-attribute">text-overflow</span>: ellipsis;
      <span class="hljs-attribute">display</span>: -webkit-box;
      -webkit-line-clamp: <span class="hljs-number">3</span>;
      -webkit-box-orient: vertical;
    &#125;
  </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"text"</span>></span>单行文本显示省略号多行文本显示省略号行文本显示省略号<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c1982378b4c4650ba0e58bc66a9cb8f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>多行文本主要是把<code>white-space</code>属性修改为使用<code>-webkit-line-clamp</code>，限制在一个块元素显示的文本的行数来实现的。</li>
</ul>
<ol>
<li><code>display: -webkit-box</code> 设置<code>div</code>为弹性伸缩盒子模型。</li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/-webkit-line-clamp" target="_blank" rel="nofollow noopener noreferrer"><code>-webkit-line-clamp</code></a> 可以把块容器中的内容限制为指定的行数。它只有在 <code>display</code> 属性设置成 <code>-webkit-box</code> 或者 <code>-webkit-inline-box</code> 并且 <code>-webkit-box-orient</code>属性设置成 <code>vertical</code> 时才有效果。</li>
<li><a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/box-orient" target="_blank" rel="nofollow noopener noreferrer"><code>-webkit-box-orient</code></a> 用来设置一个元素是水平还是垂直布局其内容。该特性是非标准的，使用时需要注意兼容性。</li>
</ol>
<h2 data-id="heading-2">展示全文</h2>
<p>最简单的方式是，使用<code>html</code>自带的<code>title属性</code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"单行文本显示省略号多行文本显示省略号行文本显示省略号"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"text"</span>></span>
    单行文本显示省略号多行文本显示省略号行文本显示省略号
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/59749dc12d2e46048a2c267f1616e84f~tplv-k3u1fbpfcp-watermark.image" alt="1.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在块容器外面，创建一个新的元素，来提示全文。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    <span class="hljs-selector-class">.text</span> &#123;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
      <span class="hljs-attribute">overflow</span>: hidden;
      <span class="hljs-attribute">text-overflow</span>: ellipsis;
      <span class="hljs-attribute">display</span>: -webkit-box;
      -webkit-line-clamp: <span class="hljs-number">3</span>;
      -webkit-box-orient: vertical;
    &#125;

    <span class="hljs-selector-class">.textTitle</span> &#123;
      <span class="hljs-attribute">position</span>: relative;
    &#125;
    <span class="hljs-selector-class">.textTitle</span><span class="hljs-selector-pseudo">::after</span> &#123;
      <span class="hljs-attribute">display</span>: none;
      <span class="hljs-attribute">content</span>: <span class="hljs-built_in">attr</span>(data-text);
      <span class="hljs-attribute">position</span>: absolute;
      <span class="hljs-attribute">top</span>: -<span class="hljs-number">60px</span>;
      <span class="hljs-attribute">left</span>: <span class="hljs-number">5px</span>;

      <span class="hljs-attribute">padding</span>: <span class="hljs-number">7px</span> <span class="hljs-number">4px</span> <span class="hljs-number">6px</span> <span class="hljs-number">6px</span>;
      <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid <span class="hljs-number">#bed48f</span>;
      <span class="hljs-attribute">border-left</span>: none;
      <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#effaeb</span>;

      <span class="hljs-attribute">height</span>: <span class="hljs-number">20px</span>;
    &#125;
    <span class="hljs-selector-class">.text</span><span class="hljs-selector-pseudo">:hover</span> + <span class="hljs-selector-class">.textTitle</span><span class="hljs-selector-pseudo">::after</span> &#123;
      <span class="hljs-attribute">display</span>: block;
    &#125;
  </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"text"</span>></span>单行文本显示省略号多行文本显示省略号行文本显示省略号<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"textTitle"</span> <span class="hljs-attr">data-text</span>=<span class="hljs-string">"单行文本显示省略号多行文本显示省略号行文本显示省略号"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/84a6d28cdc4a44dca5fdf6c2924467af~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>主要使用伪类，获取自定义标签中的文字。根据<code>:hover</code>的特性来判断，提示信息是否展示。</p>
<h2 data-id="heading-3">其他效果</h2>
<p>对标签块使用省略效果。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    <span class="hljs-selector-class">.text</span> &#123;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
    &#125;
    <span class="hljs-selector-class">.text_desc</span> &#123;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
      <span class="hljs-attribute">white-space</span>: nowrap;
      <span class="hljs-attribute">overflow</span>: hidden;
      <span class="hljs-attribute">text-overflow</span>: ellipsis;
    &#125;
    <span class="hljs-selector-class">.text_desc</span> <span class="hljs-selector-tag">span</span> &#123;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">50px</span>;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">20px</span>;
      <span class="hljs-attribute">padding</span>: <span class="hljs-number">2px</span>;
      <span class="hljs-attribute">background-color</span>: burlywood;
    &#125;
  </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"text"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"text_desc"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>></span>FE<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>></span>UI<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>></span>UX Designer<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>></span>前端工程师<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1002c5a9b1b641d497741ec97d148e25~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            