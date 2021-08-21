
---
title: '【自种树自乘凉】Flexbox 弹性布局'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6c560f925fb4124b7ed2bcd83d5b0f2~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 20 Aug 2021 21:12:34 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6c560f925fb4124b7ed2bcd83d5b0f2~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>本文已参与掘金创作者训练营第三期「高产更文」赛道，详情查看：<a href="https://juejin.cn/post/6994417198164869133" title="https://juejin.cn/post/6994417198164869133" target="_blank">掘力计划｜创作者训练营第三期正在进行，「写」出个人影响力</a>。</p>
<h2 data-id="heading-0">为什么要学这个布局？</h2>
<p>CSS3 中的 Flexbox 生来就是为了布局而生的，使用它能使许多布局布局变得简单。典型的三栏式布局、垂直水平居中布局，使用的是传统的浮动法、定位法，代码相对复杂难懂，如果使用 Flexbox 就会变得很简单。</p>
<h2 data-id="heading-1">将一个元素变成 Flexbox</h2>
<p>定义容器的语法：</p>
<p><code>display : flex</code> or <code>display : inline-flex</code></p>
<p>定义了容器后该伸缩容器中的元素将变成伸缩项，并且该容器将生成两条轴：主轴 和 侧轴。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6c560f925fb4124b7ed2bcd83d5b0f2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea6ad1b258114194a79d5b5acad351b9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">常用的容器属性</h2>
<p>第一组：</p>
<p><code>flex-direction</code>：<strong>改变主轴方向用</strong>，默认值为 row</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">flex-direction</span>: <span class="hljs-built_in">row</span>(从左到右) | <span class="hljs-built_in">row-reverse</span>(从右到左) | <span class="hljs-built_in">column</span>(从上到下) | <span class="hljs-built_in">column-reverse</span>(从下到上)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>flex-wrap</code>：<strong>自动换行和改变侧轴方向</strong>，默认值为 nowrap</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">flex-wrap</span>: <span class="hljs-built_in">nowrap</span>(不换行) | <span class="hljs-built_in">wrap</span>(换行) | <span class="hljs-built_in">wrap-reverse</span>(换行且改变侧轴方向)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>flex-flow</code>：前两者的缩写</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">flex-flow</span>: <flex-direction> || <flex-wrap>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二组：</p>
<p><code>justify-content</code>：<strong>控制子项在主轴的对齐方式</strong>，默认值为 flex-start</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">justify-content</span>: <span class="hljs-built_in">flex-start</span>(起点对齐) | <span class="hljs-built_in">flex-end</span>(终点对齐) | <span class="hljs-built_in">center</span>(居中) | <span class="hljs-built_in">space-between</span>(两端对齐) | <span class="hljs-built_in">space-around</span>(平均分配)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>align-items</code>：<strong>控制子项在侧轴的对齐方式</strong>，默认值为 stretch</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">align-items</span>: <span class="hljs-built_in">flex-start</span>(起点对齐) | <span class="hljs-built_in">flex-end</span>(终点对齐) | <span class="hljs-built_in">center</span>(居中) | <span class="hljs-built_in">stretch</span>(未设置高度就铺满侧轴)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>align-content</code>：<strong>控制子项所组成的行（列）在侧轴的对齐方式</strong></p>
<pre><code class="copyable">属性同 justify-content 几乎一致
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">常用的项目（子项）属性</h2>
<p>第一组：</p>
<p><code>order</code>：<strong>用来改变子项位置</strong>，默认值为 0</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">order</span>: <span class="hljs-number">0</span> // 值越大位置越靠后
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二组：</p>
<p><code>align-self</code>：<strong>控制单个子项在侧轴的对齐方式</strong></p>
<pre><code class="copyable">属性同 align-items 几乎一致
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第三组：</p>
<p><code>flex-grow</code>：<strong>子项的伸展比例</strong>，默认值为 0，即如果存在剩余空间，也不放大。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">flex-grow</span>: <span class="hljs-number">0</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>flex-shrink</code>：<strong>子项的收缩比例</strong>，默认值为1，即如果空间不足，该子项将缩小。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">flex-shrink</span>: <span class="hljs-number">1</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>flex-basis</code>：<strong>定义子项的伸缩前的长度</strong>（和使用 width 差不多），默认值为 auto，即原本的大小。</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">flex-basis</span>: auto;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>flex</code>：前三者的简写形式，后两个属性可选，默认值 0 1 auto</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-attribute">flex</span>: <span class="hljs-number">0</span> <span class="hljs-number">1</span> auto;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">实例</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aac59997d7cc4d678d5f951aa6396402~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Flexbox 实现垂直水平居中<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">style</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text/css"</span>></span><span class="css">
    <span class="hljs-selector-id">#div_0</span> &#123;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">300px</span>;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">500px</span>;
      <span class="hljs-attribute">background-color</span>: dimgray;
      <span class="hljs-attribute">display</span>: flex;
      <span class="hljs-comment">/* 弹性盒子*/</span>
      <span class="hljs-attribute">justify-content</span>: center;
      <span class="hljs-comment">/* 显示在主轴的中间 */</span>
      <span class="hljs-attribute">align-items</span>: center;
      <span class="hljs-comment">/* 子项在侧轴中间位置 */</span>
    &#125;
    <span class="hljs-selector-id">#div_1</span> &#123;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
      <span class="hljs-attribute">background-color</span>: burlywood;
    &#125;
  </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"div_0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"div_1"</span>></span>居中的元素<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            