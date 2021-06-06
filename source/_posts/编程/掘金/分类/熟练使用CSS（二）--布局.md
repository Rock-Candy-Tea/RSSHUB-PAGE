
---
title: '熟练使用CSS（二）--布局'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7405'
author: 掘金
comments: false
date: Sat, 05 Jun 2021 06:30:56 GMT
thumbnail: 'https://picsum.photos/400/300?random=7405'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">布局</h2>
<p>在CSS中，布局是非常重要的部分，了解常用的布局及如何实现这些布局是必要的。让我们一起来学习CSS中的布局吧！</p>
<h3 data-id="heading-1">flex布局</h3>
<p>flex布局是目前最流行使用的布局方式，具有诸多优点，可以解决原有布局的各种问题。</p>
<p>它会设置一个<strong>主轴</strong>方向，与主轴向垂直的就是<strong>交叉轴</strong>，通过设置<strong>换行方式</strong>、<strong>项目在主轴的对齐方式</strong>、<strong>项目在交叉轴的对齐方式</strong>等来实现各式各样的效果。</p>
<p>关键点如下：</p>
<h4 data-id="heading-2">主轴的方向：flex-direction</h4>
<p>flex-direction决定了项目的主轴方向。它包括以下四个值：</p>
<ul>
<li>
<p>row: 默认值，项目的主轴方向为行，即项目左右排列。</p>
</li>
<li>
<p>column: 项目的主轴方向为列，即项目上下排列。</p>
</li>
<li>
<p>row-reverse: 主轴为行，但方向与row相反，从右往左。</p>
</li>
<li>
<p>column-reverse: 主轴为列，但方向与column相反，从下往上。</p>
</li>
</ul>
<h4 data-id="heading-3">换行方式：flex-wrap</h4>
<p>flex-wrap决定了项目在一条轴线上排不下，该如何换行。它包括以下三个值：</p>
<ul>
<li>
<p>nowrap: 默认值，不换行，将项目空间按比例分配。</p>
</li>
<li>
<p>wrap: 换行，第一行在上方</p>
</li>
<li>
<p>wrap-reverse: 换行，但是交叉轴方向相反，第一行在下方。</p>
</li>
</ul>
<h4 data-id="heading-4">项目在主轴上的对齐方式：justify-content</h4>
<p>justify-content决定了项目在交叉轴上是如何对齐的。它包括以下五个值：</p>
<ul>
<li>
<p>flex-start: 默认值，向前对齐</p>
</li>
<li>
<p>flex-end: 向后对齐</p>
</li>
<li>
<p>center: 居中</p>
</li>
<li>
<p>space-between: 两端对齐，项目之间的间隔相同</p>
</li>
<li>
<p>space-around: 每个项目两侧的间隔相等。所以，项目之间的间隔比项目与边框的间隔大一倍。</p>
</li>
</ul>
<h4 data-id="heading-5">项目在交叉轴上的对齐方式：align-items</h4>
<p>align-items决定了项目在交叉轴上的对齐方式。它包括以下五个值：</p>
<ul>
<li>
<p>stretch: 默认值，如果项目未设置高度或设为auto，将占满整个容器的高度</p>
</li>
<li>
<p>flex-start: 交叉轴的起点对齐</p>
</li>
<li>
<p>flex-end: 交叉轴的终点对齐</p>
</li>
<li>
<p>center: 交叉轴的终点对齐（居中）</p>
</li>
<li>
<p>baseline: 项目的第一行文字的基线对齐</p>
</li>
</ul>
<h3 data-id="heading-6">经典布局</h3>
<p>说完了重要的flex布局，我们再了解一些经典布局及常见样式问题，如：负margin问题。</p>
<h4 data-id="heading-7">负margin</h4>
<p>margin设置负值，根据设置的方向、元素是否浮动、其定位方式，最终会有不同的行为，我们一起来看看。</p>
<p><strong>元素没有设置浮动并且没有设置定位或者position为static</strong></p>
<ul>
<li>
<p>设置的margin的方向为top / left，元素会按照设置的方向移动相应的距离</p>
</li>
<li>
<p>设置的margin的方向为bottom / right，元素本身不会移动，元素后面的其它元素会往该元素的方向移动相应的距离，并覆盖在该元素的上方。</p>
</li>
</ul>
<p><strong>元素没有设置浮动且positive为relative</strong></p>
<ul>
<li>
<p>设置的margin的方向为top / left，元素会按照设置的方向移动相应的距离</p>
</li>
<li>
<p>设置的margin的方向为bottom / right，元素本身不会移动，元素后面的其它元素会往该元素的方向移动相应的距离，但是该元素会覆盖在后面的元素上面（后面的元素没有设置定位及z-index）。</p>
</li>
</ul>
<p><strong>元素没有设置浮动且positive为absolute</strong></p>
<ul>
<li>
<p>设置的margin的方向为top / left，元素会按照设置的方向移动相应的距离</p>
</li>
<li>
<p>设置的margin的方向为bottom / right，设置绝对定位的元素已经脱离了文档流，对后面的元素没有影响</p>
</li>
</ul>
<p><strong>元素设置了浮动</strong></p>
<p>如果给一个元素设置了浮动，再设置了positive：relative；和单独设置float是一样的。对设置了浮动的元素，设置margin为负值时，表现如下：</p>
<ul>
<li>
<p>设置的margin的方向和浮动的方向相同，则元素会往对应的方向移动对应的的距离</p>
</li>
<li>
<p>设置的margin的方向和浮动的方向相反，则元素本身不动，元素之前或之后的元素会向该元素的方向移动相应的距离，覆盖在该元素上。</p>
</li>
</ul>
<h4 data-id="heading-8">圣杯布局</h4>
<p>圣杯布局是指三栏布局，两侧宽度固定，中间宽度自适应。（我们这里假设高度为100px，两侧宽度分别为100px和150px）</p>
<p>我们来用flex和负margin两种方式来实现圣杯布局吧！</p>
<pre><code class="hljs language-css copyable" lang="css">// <span class="hljs-attribute">flex</span>布局
// dom结构
<<span class="hljs-selector-tag">div</span> id='container'>
    <<span class="hljs-selector-tag">div</span> id='<span class="hljs-attribute">left</span>'><span class="hljs-attribute">left</span></<span class="hljs-selector-tag">div</span>>
    <<span class="hljs-selector-tag">div</span> id='<span class="hljs-attribute">content</span>'><span class="hljs-attribute">content</span></<span class="hljs-selector-tag">div</span>>
    <<span class="hljs-selector-tag">div</span> id='<span class="hljs-attribute">right</span>'><span class="hljs-attribute">right</span></<span class="hljs-selector-tag">div</span>>
</<span class="hljs-selector-tag">div</span>>

// css样式
<span class="hljs-selector-id">#container</span> &#123;
    <span class="hljs-attribute">display</span>: flex;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
&#125;
<span class="hljs-selector-id">#left</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">background</span>: pink;
&#125;
<span class="hljs-selector-id">#content</span> &#123;
    <span class="hljs-attribute">flex</span>: <span class="hljs-number">1</span>;
    <span class="hljs-attribute">background</span>: lightYellow;
&#125;
<span class="hljs-selector-id">#right</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">150px</span>;
    <span class="hljs-attribute">background</span>: lightGreen;
&#125;

// 负<span class="hljs-attribute">margin</span>布局
// dom结构
<<span class="hljs-selector-tag">div</span> id='container'>
    <<span class="hljs-selector-tag">div</span> id='<span class="hljs-attribute">content</span>'><span class="hljs-attribute">content</span></<span class="hljs-selector-tag">div</span>>
    <<span class="hljs-selector-tag">div</span> id='<span class="hljs-attribute">left</span>'><span class="hljs-attribute">left</span></<span class="hljs-selector-tag">div</span>>
    <<span class="hljs-selector-tag">div</span> id='<span class="hljs-attribute">right</span>'><span class="hljs-attribute">right</span></<span class="hljs-selector-tag">div</span>>
</<span class="hljs-selector-tag">div</span>>

// css样式
<span class="hljs-selector-id">#container</span> &#123;
    <span class="hljs-attribute">overflow</span>: hidden;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span> <span class="hljs-number">100px</span>;
&#125;
<span class="hljs-selector-id">#content</span>, <span class="hljs-selector-id">#left</span>, <span class="hljs-selector-id">#right</span> &#123;
    <span class="hljs-attribute">float</span>: left;
&#125;
<span class="hljs-selector-id">#content</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">background</span>: lightYellow;
&#125;
<span class="hljs-selector-id">#left</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">background</span>: pink;
    <span class="hljs-attribute">margin-left</span>: -<span class="hljs-number">100%</span>;
    <span class="hljs-attribute">position</span>: relative;
    <span class="hljs-attribute">left</span>: -<span class="hljs-number">100px</span>;
&#125;
<span class="hljs-selector-id">#right</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">background</span>: lightGreen;
    <span class="hljs-attribute">margin-left</span>: -<span class="hljs-number">100px</span>;
    <span class="hljs-attribute">position</span>: relative;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">100px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">双飞翼布局</h4>
<p>双飞翼布局与圣杯布局相似，不同点在于它在middle中增加了一个middle-inner盒子，把middle的内容放到middle-inner盒子中，最后就不需要给left和right设置定位了。</p>
<pre><code class="hljs language-css copyable" lang="css">// dom结构
<<span class="hljs-selector-tag">div</span> id='container'>
    <<span class="hljs-selector-tag">div</span> id='<span class="hljs-attribute">content</span>'>
        <<span class="hljs-selector-tag">div</span> id='middle-inner'>middle</<span class="hljs-selector-tag">div</span>>
    </<span class="hljs-selector-tag">div</span>>
    <<span class="hljs-selector-tag">div</span> id='<span class="hljs-attribute">left</span>'><span class="hljs-attribute">left</span></<span class="hljs-selector-tag">div</span>>
    <<span class="hljs-selector-tag">div</span> id='<span class="hljs-attribute">right</span>'><span class="hljs-attribute">right</span></<span class="hljs-selector-tag">div</span>>
</<span class="hljs-selector-tag">div</span>>

// css样式
<span class="hljs-selector-id">#container</span> &#123;
    <span class="hljs-attribute">overflow</span>: fidden;
&#125;
<span class="hljs-selector-id">#left</span>, <span class="hljs-selector-id">#right</span>, <span class="hljs-selector-id">#content</span> &#123;
    <span class="hljs-attribute">float</span>: left;
&#125;
<span class="hljs-selector-id">#content</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">background</span>: lightYellow;
&#125;
<span class="hljs-selector-id">#middle-inner</span> &#123;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span> <span class="hljs-number">100px</span>;
&#125;
<span class="hljs-selector-id">#left</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">background</span>: pink;
    <span class="hljs-attribute">margin-left</span>: -<span class="hljs-number">100%</span>;
&#125;
<span class="hljs-selector-id">#right</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">background</span>: lightGreen;
    <span class="hljs-attribute">margin-left</span>: -<span class="hljs-number">100px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">总结</h3>
<p>在这一节，我们详细介绍了CSS的flex布局和常用的圣杯布局，以及介绍了负margin的使用。接下来我们会继续介绍其他CSS知识。</p>
<p>我是何以庆余年，如果文章对你起到了帮助，希望可以点个赞，谢谢！</p>
<p>如有问题，欢迎在留言区一起讨论。</p></div>  
</div>
            