
---
title: '用CSS造出詞云效果'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a275c6acc87498a9641a011d22b81fd~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 11 Jun 2021 21:20:50 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a275c6acc87498a9641a011d22b81fd~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>前段时间，接到一个需求要做一个充满随机词云的区域，而且词云要互相不重叠，效果如下图:</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a275c6acc87498a9641a011d22b81fd~tplv-k3u1fbpfcp-watermark.image" alt="word-cloud" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我刚开始打算先把词云做出来，然后用js算每一个的位置，但实在太难和太麻烦，一方面要用js去随机生成每一个云的位置，另一方面还要考虑生成的位置不发生重叠。后来转个思路去想，不用js，只用css可以吗？最后想到用flex做布局，然后利用js随机生成位置偏移，为了不发生重叠，给每个词云相应的间距就可以了。</p>
<p>现在开始把效果实现吧。</p>
<h1 data-id="heading-0">单个词云的实现</h1>
<p>在去实现一堆随机词云前，先看下怎样实现单个词云。</p>
<p>首先先把元素写好:</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"word-cloud"</span>></span>
  Hello World
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后是css:</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.word-cloud</span> &#123;
  <span class="hljs-attribute">position</span>: relative;
  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">justify-content</span>: center;
  <span class="hljs-attribute">align-items</span>: center;
  <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">96px</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">200px</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#01FFFC</span>;
  <span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">20px</span> <span class="hljs-number">7px</span> <span class="hljs-number">#01FFFC</span> inset;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ab9d0d9077284b93a6d4ea41206f0481~tplv-k3u1fbpfcp-watermark.image" alt="one-cloud" loading="lazy" referrerpolicy="no-referrer"></p>
<p><a href="https://codepen.io/dominguitolamo/pen/xxqypNm" target="_blank" rel="nofollow noopener noreferrer">codepen在綫演示</a></p>
<p>词云实现是没有什么难度的，重点是 <code>box-shadow</code>，利用<code>inset</code>，使阴影向内，把前两个参数设成0, 就可以使阴影向四周扩散。关于<code>box-shadow</code>的更多实现，可以看:</p>
<p><a href="https://juejin.cn/post/6844903704986910728" target="_blank">你所不知道的 CSS 阴影技巧与细节</a></p>
<h1 data-id="heading-1">词云布局</h1>
<p>(为了方便，这里我用vue来实现，其实用原生js也可以实现)</p>
<p>接下来去做一堆词云吧。先把布局做好：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">body</span> &#123;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span>;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span>;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">rgba</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">1</span>);
&#125;

<span class="hljs-selector-id">#app</span> &#123;
  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">flex-direction</span>: row;
  <span class="hljs-attribute">flex-wrap</span>: wrap;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">30px</span>;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">800px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>先把背景色设为黑色，然后做一个flex布局。</p>
<p>定义一些随机词云数据：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;
      <span class="hljs-attr">cloudTexts</span>: [
        <span class="hljs-string">'hello'</span>,
        <span class="hljs-string">'world'</span>,
        <span class="hljs-string">'monday'</span>,
        <span class="hljs-string">'tuesday'</span>,
        <span class="hljs-string">'sanday'</span>,
        <span class="hljs-string">'foo'</span>,
        <span class="hljs-string">'bar'</span>,
        <span class="hljs-string">'cheers'</span>,
        <span class="hljs-string">'cloud'</span>,
        <span class="hljs-string">'text'</span>,
        <span class="hljs-string">'taste'</span>,
        <span class="hljs-string">'dog'</span>,
        <span class="hljs-string">'rose'</span>,
        <span class="hljs-string">'boy'</span>,
        <span class="hljs-string">'girl'</span>,
        <span class="hljs-string">'egg'</span>
      ]
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实现一个方法来生成词云的样式：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-function"><span class="hljs-title">genStyles</span>(<span class="hljs-params"></span>)</span> &#123;
     <span class="hljs-comment">// 设定颜色</span>
     <span class="hljs-keyword">const</span> colors = [[<span class="hljs-string">'#01FFFC'</span>, <span class="hljs-string">'#01FFFC'</span>], [<span class="hljs-string">'#01FF84'</span>, <span class="hljs-string">'#01FF84'</span>], [<span class="hljs-string">'#5843D7'</span>, <span class="hljs-string">'#E2DDFF'</span>], [<span class="hljs-string">'#FD374E'</span>, <span class="hljs-string">'#FD374E'</span>]]
    <span class="hljs-keyword">const</span> colorIndex = <span class="hljs-built_in">Math</span>.floor(<span class="hljs-built_in">Math</span>.random() * <span class="hljs-number">4</span>)
    <span class="hljs-comment">// 设定随机位置</span>
    <span class="hljs-keyword">const</span> top = <span class="hljs-built_in">Math</span>.floor((<span class="hljs-built_in">Math</span>.random() * <span class="hljs-number">140</span>) - <span class="hljs-number">70</span>)
    <span class="hljs-keyword">const</span> left = <span class="hljs-built_in">Math</span>.floor((<span class="hljs-built_in">Math</span>.random() * <span class="hljs-number">160</span>) - <span class="hljs-number">80</span>)
    
    <span class="hljs-comment">// 给予间隔，防止折迭</span>
    <span class="hljs-keyword">const</span> margin = <span class="hljs-string">`<span class="hljs-subst">$&#123;<span class="hljs-built_in">Math</span>.abs(top) + <span class="hljs-number">4</span>&#125;</span>px <span class="hljs-subst">$&#123;<span class="hljs-built_in">Math</span>.abs(left) + <span class="hljs-number">4</span>&#125;</span>px`</span>
      
      <span class="hljs-keyword">return</span> &#123;
        <span class="hljs-attr">position</span>: <span class="hljs-string">'relative'</span>,
        top,
        left,
        <span class="hljs-attr">display</span>: <span class="hljs-string">'flex'</span>,
        <span class="hljs-string">'justify-content'</span>: <span class="hljs-string">'center'</span>,
        <span class="hljs-string">'align-items'</span>: <span class="hljs-string">'center'</span>,
        <span class="hljs-string">'border-radius'</span>: <span class="hljs-string">'96px'</span>,
        <span class="hljs-attr">width</span>: <span class="hljs-string">'150px'</span>,
        <span class="hljs-attr">height</span>: <span class="hljs-string">'70px'</span>,
        margin,
        <span class="hljs-attr">color</span>: colors[colorIndex][<span class="hljs-number">1</span>],
        <span class="hljs-string">'box-shadow'</span>: <span class="hljs-string">`0 0 20px 7px <span class="hljs-subst">$&#123;colors[colorIndex][<span class="hljs-number">0</span>]&#125;</span> inset`</span>
      &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>生成随机数后再相减，使偏移值可以是正或负，然后为了不让词云互相重叠，给每个词云与偏移值相等的间距，保証它们互相不重叠。</p>
<p>最后效果可以看演示：</p>
<p><a href="https://codepen.io/dominguitolamo/pen/abJRqOX" target="_blank" rel="nofollow noopener noreferrer">codepen在綫演示</a></p></div>  
</div>
            