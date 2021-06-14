
---
title: '什么？你还搞不懂CSS盒模型？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5047b7d4f544c66943feb5a10f53d6c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 13 Jun 2021 21:17:20 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5047b7d4f544c66943feb5a10f53d6c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">盒模子型</h1>
<p>​在写这篇文章之前，我也阅读了其他文章，但我有个习惯：总想自己测试一遍，并记下笔记，从而更好的理解。也就是在这个过程中，我发现网上大部分博客阐述内容有一些问题，与实际测试并不相复合，下面我将详解这个过程。</p>
<h2 data-id="heading-1">什么是盒子模型？</h2>
<p>​展示在页面上的每一个元素都可以视为一个盒模型，且本质上都是一个矩形盒子，盒模型总共分为两种，分别为：<code>W3C标准盒模型</code>、<code>IE盒模型</code>。</p>
<p>​之所以分为两类，是因为二者在性质上有些不同，具体来说是在<strong>计算宽高时</strong>的差异。</p>
<p>​页面中的矩形盒子宽高可以通过<code>width</code>、<code>heitht</code>属性进行配置，但这只是设置了<strong>content</strong>内容部分的宽高，除此之外，盒子宽高还受<code>padding</code>、<code>border</code>两个属性的影响。</p>
<p>​<code>W3C标准盒模型</code>、<code>IE盒模型</code>两种盒子类型，也就是因为对<code>padding</code>、<code>border</code>两个属性处理的形式不同，从而划分为两类的。</p>
<h2 data-id="heading-2">W3C标准盒模型</h2>
<p><code>W3C标准盒模型</code>在计算盒子宽高时，为<code>width/height</code>、<code>padding</code>、<code>border</code>四个属性相加。</p>
<p>实际也就是 <code>content+padding+border</code>，因为我们通过css设置<code>width/height</code>属性就是用来定义盒子<strong>内容</strong>宽高的。</p>
<p>实际操作：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5047b7d4f544c66943feb5a10f53d6c~tplv-k3u1fbpfcp-watermark.image" alt="W3CBox1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
  <span class="hljs-selector-tag">article</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#16a085</span>;
  &#125;
  <span class="hljs-selector-class">.box</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">10px</span>;
    <span class="hljs-attribute">border</span>: <span class="hljs-number">10px</span> solid black;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">5px</span>;
    
    <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#f39c12</span>;
    <span class="hljs-attribute">color</span>: white;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">article</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box W3CBox"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">span</span>></span>W3CBox<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">article</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们通过控制台工具，看看盒子宽高到底是不是上文讲的那样： <code>content+padding+border</code></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8769b9f16f3e4fb38b6de367ae7d1ecf~tplv-k3u1fbpfcp-watermark.image" alt="W3CBox2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在来分析一下：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d194f417a394d56bce4de2f503f8d45~tplv-k3u1fbpfcp-watermark.image" alt="W3CBox3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol>
<li><strong>content</strong>：content= width/height =  100 * 100 (px)</li>
<li><strong>padding</strong>：在content的基础上设置padding为10px
<ul>
<li>此时盒子宽度 width+paddingLeft/Right =100 + 20 (px)</li>
<li>此时盒子高度 width+paddingTop/Bottom =100 + 20 (px)</li>
</ul>
</li>
<li><strong>border</strong>：在上面的基础上又对盒子宽高产生了影响
<ul>
<li>此时盒子宽度 width+paddingLeft/Right + borderLeft/Right =100 + 20 + 20(px)</li>
<li>此时盒子高度 width+paddingTop/Bottom + borderTop/Bottom =100 + 20 + 20(px)</li>
</ul>
</li>
</ol>
<p>整体计算下来，盒子宽高为 <code>140 *140 (px)</code>，完全符合上述结论。</p>
<p>值得注意的是：网上好多博客文章都将<code>margin</code>算入了盒子的宽高，虽然在视觉上，盒子最外层的确有了间隙，但这只是影响了布局，<strong>并没有影响盒子本身的尺寸</strong>，若盒子尺寸包含了<code>margin</code>，那最后得到的盒子尺寸应为 150 * 150 (px)，但事实并不是这样。</p>
<h2 data-id="heading-3">IE盒模型</h2>
<p><code>IE盒模型</code>在计算盒子宽高时，只包含<code>width/height</code>即内容<strong>content</strong>部分。但值得注意的是，这content包含了<code>padding</code>、<code>border</code>两个属性。</p>
<p>也即是说，盒子最终的宽高，就是我们设置的<code>width/height</code>,若我们又设置了<code>padding</code>、<code>border</code>两个属性，则这两个属性不会对宽高造成影响，而是包含在了设置的<code>width/height</code>中。</p>
<p>实际操作：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87cc46cd70e4474f9a818fec54878878~tplv-k3u1fbpfcp-watermark.image" alt="IEBox1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.IEBox</span> &#123; <span class="hljs-attribute">box-sizing</span>: border-box; &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box IEBox"</span>></span> <span class="hljs-tag"><<span class="hljs-name">span</span>></span>IEBox<span class="hljs-tag"></<span class="hljs-name">span</span>></span> <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以发现，其他配置相同，只是改变了盒子模型，但尺寸却差了好多，我们通过控制台工具，看看盒子宽高到底为多少？</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/04e7828f1a464fccb67e30d2ab2c987c~tplv-k3u1fbpfcp-watermark.image" alt="IEBox2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/93cd12c7b098432b9779b1c303a7a525~tplv-k3u1fbpfcp-watermark.image" alt="IEBox3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过结果来看，完全符合上述结论，盒子的尺寸只包含<strong>content</strong>部分，也就是我们定义的 <code>width/height</code>属性。之后定义的<code>padding</code>、<code>border</code>都会被包含到<strong>content</strong>中。</p>
<h2 data-id="heading-4">box-sizing</h2>
<p>上面两个例子已经让我们清晰的发现两种盒模型的差异，那我们怎么切换两种盒子模型呢，其实上文已经使用过了，也就是<code>box-sizing</code>属性。</p>
<p><strong>语法</strong></p>
<pre><code class="copyable">box-sizing: content-box|border-box|inherit;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>content-box
<ul>
<li>默认值，设置为W3C标准盒模型</li>
</ul>
</li>
<li>border-box
<ul>
<li>设置为IE盒模型</li>
</ul>
</li>
<li>inherit
<ul>
<li>继承父级盒子类型</li>
</ul>
</li>
</ul>
<h2 data-id="heading-5">总结</h2>
<ul>
<li><code>W3C标准盒模型</code>在计算盒子宽高时，为<code>width/height</code>、<code>padding</code>、<code>border</code>四个属性相加。</li>
<li><code>IE盒模型</code>在计算盒子宽高时，只包含<code>width/height</code>即内容<strong>content</strong>部分，且content包含了<code>padding</code>、<code>border</code>。</li>
<li><code>margin</code> 并不会影响盒子的尺寸，该属性影响的是布局。</li>
<li>可通过<code>box-sizing</code>改变盒子类型。</li>
</ul>
<h2 data-id="heading-6">最后</h2>
<p>盒子模型虽然非常基础，但也包含一些细节，导致我们认知模糊，这篇文章希望能帮到读者。</p>
<p>本文到此结束，希望对你有所帮助，我是 Ashun ，在校大学生，立志成为资深前端工程师，欢迎大家一起交流、学习。后续更新更多文章，请持续关注哦~</p>
<p>原创文章，文笔有限，才疏学浅，文中若有不正之处，速速告知。</p></div>  
</div>
            