
---
title: 'CSS垂直居中'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8075'
author: 掘金
comments: false
date: Fri, 26 Mar 2021 02:07:29 GMT
thumbnail: 'https://picsum.photos/400/300?random=8075'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">垂直居中</h2>
<p><code>CSS</code>让人头疼的问题就是<code>垂直居中</code>。实现<code>垂直居中</code>好几种方式，但每一种方式都有一定的局限性,所以<code>垂直居中</code>可以根据实际的业务场景来使用。</p>
<p>在容器里让内容居中最好的方式是根据特定场景考虑不同因素。做出判断前，先逐个询问自己以下几个问题，直到找到合适的解决办法。</p>
<ul>
<li>容器里面的内容只有一行文字？</li>
<li>容器自然高度？</li>
<li>容器需要指定高度或者避免使用内边距？</li>
<li>使用<code>Flexbox</code>布局？</li>
<li>容器和内容的高度都知道？</li>
<li>不知道内部元素的高度？</li>
</ul>
<h3 data-id="heading-1">容器里面的内容只有一行文字</h3>
<p>设置一个大的行高，让它等于理想的容器高度。这样会让容器高度扩展到能够容纳行高。如果内容不是行内元素，可以设置为<code>inline-block</code>。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    * &#123;
      <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
      <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
    &#125;
    <span class="hljs-selector-tag">div</span> &#123;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">60px</span>;
      <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#1888fa</span>;
      <span class="hljs-attribute">color</span>: white;
    &#125;
    <span class="hljs-selector-tag">span</span> &#123;
      <span class="hljs-attribute">line-height</span>: <span class="hljs-number">60px</span>;
    &#125;
  </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">span</span>></span>测试居中<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">容器自然高度</h3>
<p><code>CSS</code>中最简单的<code>垂直居中</code>方法是给容器相等的上下内边距，让容器和内容自行决定自己的高度。</p>
<p>看下面的例子, 通过设置<code>padding-top</code> 和<code>padding-bottom</code>相等的值，让内容在父容器垂直剧中。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
      * &#123;
        <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
      &#125;
      <span class="hljs-selector-tag">div</span> &#123;
        <span class="hljs-attribute">padding-top</span>: <span class="hljs-number">20px</span>;  
        <span class="hljs-attribute">padding-bottom</span>: <span class="hljs-number">20px</span>;
        <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#1888FA</span>;
        <span class="hljs-attribute">color</span>: white;
      &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
         <span class="hljs-tag"><<span class="hljs-name">span</span>></span>测试居中<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">容器需要指定高度或者避免使用内边距</h3>
<p>可以给父容器设置<code>display: table</code>, 子元素设置<code>display: table-cell;       vertical-align: middle;</code>, 让子元素来垂直居中。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    * &#123;
      <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
      <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
    &#125;
    <span class="hljs-selector-tag">div</span> &#123;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">60px</span>;
      <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#1888fa</span>;
      <span class="hljs-attribute">color</span>: white;
      <span class="hljs-attribute">display</span>: table;
    &#125;
    <span class="hljs-selector-tag">span</span> &#123;
      <span class="hljs-attribute">display</span>: table-cell;
      <span class="hljs-attribute">vertical-align</span>: middle;
    &#125;
  </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">span</span>></span>测试居中<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">使用 FlexBox</h3>
<p>使用<code>flex</code>布局在做居中的时候非常容易。</p>
<pre><code class="hljs language-js copyable" lang="js"><!DOCTYPE html>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    * &#123;
      <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
      <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
    &#125;
    <span class="hljs-selector-tag">div</span> &#123;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">60px</span>;
      <span class="hljs-attribute">display</span>: flex;
      <span class="hljs-attribute">align-items</span>: center;
      <span class="hljs-attribute">justify-content</span>: center;
      <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#1888fa</span>;
      <span class="hljs-attribute">color</span>: white;
    &#125;
  </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">span</span>></span>测试居中<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">容器和内容的高度都知道</h3>
<p>将内容使用绝对定位， 只有其他方法都无法实现，才推荐这种。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    * &#123;
      <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
      <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
    &#125;
    <span class="hljs-selector-tag">div</span> &#123;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
      <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#1888fa</span>;
      <span class="hljs-attribute">color</span>: white;
      <span class="hljs-attribute">position</span>: relative;
    &#125;
    <span class="hljs-selector-tag">span</span>&#123;
      <span class="hljs-attribute">position</span>: absolute;
      <span class="hljs-attribute">top</span>: <span class="hljs-number">35px</span>;
      <span class="hljs-attribute">display</span>: inline-block;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">30px</span>;
    &#125;
  </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">span</span>></span>测试居中<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">不知道内部元素的高度</h3>
<p>将内容使用<code>绝对定位</code> + <code>transform</code>， 只有其他方法都无法实现，才推荐这种。</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
    * &#123;
      <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
      <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
    &#125;
    <span class="hljs-selector-tag">div</span> &#123;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
      <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#1888fa</span>;
      <span class="hljs-attribute">color</span>: white;
      <span class="hljs-attribute">position</span>: relative;
    &#125;
    <span class="hljs-selector-tag">span</span> &#123;
      <span class="hljs-attribute">position</span>: absolute;
      <span class="hljs-attribute">top</span>: <span class="hljs-number">50%</span>;
      <span class="hljs-attribute">left</span>: <span class="hljs-number">50%</span>;
      <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(-<span class="hljs-number">50%</span>, -<span class="hljs-number">50%</span>);
    &#125;
  </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">span</span>></span>测试居中<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">总结</h2>
<p>应结合实际的业务场景来具体使用哪种方式。</p>
<h2 data-id="heading-8">参考</h2>
<p><a href="http://howtocenterincss.com/" target="_blank" rel="nofollow noopener noreferrer">How to Center in CSS</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            