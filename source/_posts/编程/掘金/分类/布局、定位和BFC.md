
---
title: '布局、定位和BFC'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3365'
author: 掘金
comments: false
date: Sun, 29 Aug 2021 02:36:57 GMT
thumbnail: 'https://picsum.photos/400/300?random=3365'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、布局基础</h2>
<p>1、布局：按照设计图要求，进行区域划分</p>
<p>2、布局时一个循环往复的过程</p>
<p>3、常用设计布局：(高度都不设置，让其根据内容自动)</p>
<p>1、所有内容全部居中</p>
<pre><code class="copyable"><body>
    <div class="container">
        
    </div>
</body>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">.container&#123;
    width: XXpx;
    margin: 0 auto;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、头部贯穿，下面主体居中</p>
<pre><code class="copyable"><body>
    <header></header>
    <div class="container">
​
    </div>
</body>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">header&#123;
    width: 100%;
&#125;
.container&#123;
    width: XXpx;
    margin: 0 auto;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、头部、脚部贯穿，中间内容居中</p>
<pre><code class="copyable"><body>
    <header></header>
    <div class="container">
    </div>
   <footer></footer>
</body>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">header,footer&#123;
    width: 100%;
&#125;
.container&#123;
    width: XXpx;
    margin: 0 auto;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">二、flex布局</h2>
<p>1、容器和项目</p>
<p>容器：装东西（父元素）</p>
<p>项目：子元素</p>
<p>2、主轴和交叉轴</p>
<p>默认情况下，主轴水平向右，交叉轴垂直向下</p>
<p>3、创建弹性布局</p>
<p>在父元素中创建display:flex; 父元素就是容器，在默认状态下里面的项目显示在一行，</p>
<p>当项目宽度总和超过容器宽度，它会自动等比例压缩项目宽度。</p>
<p>（1）项目换行：flex-wrap</p>
<p>flex-wrap: nowrap; 不换行 默认情况</p>
<p>flex-wrap: wrap; 换行</p>
<p>flex-wrap: wrap-reverse; 倒放换行</p>
<p>（2）控制主轴方向对齐方式：justify-content</p>
<p>justify-content: center; 所有项目居中显示</p>
<p>justify-content: flex-start; 靠左对齐</p>
<p>justify-content: flex-end; 靠右对齐</p>
<p>justify-content: space-between; 项目与项目之间等距分配，项目与容器距离为0</p>
<p>justify-content: space-around; 项目与项目之间距离相等，项目与容器距离为 项目与项目之间距离的一半</p>
<p>justify-content: space-evenly; 所有空白部分距离相等</p>
<p>（3）控制交叉轴方向对齐方式：align-items</p>
<p>align-items: center; 居中</p>
<p>align-items: flex-start; 上方排列</p>
<p>align-items: flex-end; 底部排列</p>
<p>align-items: baseline； 项目的第一行文字的基线对齐</p>
<p>align-items: stretch; 默认值，如果项目未设置高度或设为auto，将占满整个容器的高度</p>
<p>（4）改变主轴方向：flex-direction</p>
<p>flex-direction: row; 默认值，主轴为水平方向，起点在左端</p>
<p>flex-direction: row-reverse; 主轴为水平方向，起点在右端</p>
<p>flex-direction: column; 主轴为垂直方向，起点在上沿</p>
<p>flex-direction: column-reverse; 主轴为垂直方向，起点在下沿</p>
<p>（黑色表示主轴，橙色表示交叉轴，交叉轴随主轴变化）</p>
<p>（5）定义多根轴线的对齐方式：align-content（如果项目只有一根轴线，该属性不起作用）</p>
<p>align-content：flex-start; 与交叉轴的起点对齐</p>
<p>align-content：flex-end; 与交叉轴的终点对齐</p>
<p>align-content：center; 与交叉轴的中点对齐</p>
<p>align-content：space-between; 与交叉轴两端对齐，轴线之间的间隔平均分布</p>
<p>align-content：space-around; 每根轴线两侧的间隔都相等。所以，轴线之间的间隔比轴线与边框的间隔大一倍</p>
<p>align-content：stretch; 默认值，轴线占满整个交叉轴</p>
<p>（6）把剩余部分按比例分给子元素：flex-grow (写在子元素里面，后面的数字代表比例)</p>
<h2 data-id="heading-2">三、定位</h2>
<p>元素设置了position属性：</p>
<pre><code class="copyable">div&#123;
    /* 静态定位 默认值 */
    position: static;
    /* 相对定位 */
    position: relative;
    /* 绝对定位 */
    position: absolute;
    /* 固定定位 */
    position: fixed;
    /* 粘性定位 */
    position: static;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>1、相对定位</p>
<p>相对盒子原来的位置偏移，原本所占空间不变，没有脱离文档流，一般用来做绝对定位的父元素。</p>
<p>2、绝对定位</p>
<ul>
<li>当浮动元素被设置为绝对定位，元素的float属性会失效</li>
<li>相对于设置了定位属性（除static）的父元素偏移</li>
<li>如果没有就相对于html元素偏移</li>
<li>脱离了文档流，不再占据空间</li>
<li>子绝父相</li>
</ul>
<p>子元素设置为绝对定位，父元素设置为相对定位，父元素位置发生变化，子元素跟着变化。</p>
<ul>
<li>使用z-index可以改变堆叠顺序，数值越大，堆叠在越上方</li>
</ul>
<p>3、固定定位</p>
<p>相对于浏览器窗口的固定位置，不会随着用户的滚动变化，脱离文档流。</p>
<p>4、粘性定位</p>
<p>依赖于用户的滚动，在相对定位与固定定位之间切换，指定top、left、right、bottom四个阈值其中之一，粘性才会生效。</p>
<h2 data-id="heading-3">四、块级格式化上下文</h2>
<p>块级格式化上下文：block formatting context（简称BFC），它时一个独立的渲染区域，这个区域与外部毫不相干。</p>
<p>1、如何创建BFC</p>
<ul>
<li>float不能是none</li>
<li>position的值不是static或者relative</li>
<li>display的值是line-block、table-cell、flex、table-caption或者inline-flex</li>
<li>overflow的值不是visible</li>
</ul>
<p>2、作用</p>
<ul>
<li>避免上下两个相邻元素垂直方向的margin重叠</li>
</ul>
<pre><code class="copyable"> <p>看看我的 margin是多少</p>
    <div>
        <p>看看我的 margin是多少</p>
    </div>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"> *&#123;
        margin: 0;
        padding: 0;
    &#125;
    p &#123;
        color: #f555;
        background: yellow;
        width: 200px;
        line-height: 100px;
        text-align:center;
        margin: 30px;
    &#125;
    div&#123;
        /* 激活BFC */
        overflow: hidden;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>激活后，两个p元素之间的margin为60px</p>
<ul>
<li>解决父元素高度坍塌问题，通过激活父元素的BFC</li>
</ul>
<pre><code class="copyable">  <div class="par">
        <div class="child"></div>
        <div class="child"></div>
    </div>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"> .par &#123;
        border: 5px solid rgb(91, 243, 30);
        width: 300px;
       /* 激活BFC */
        overflow: hidden;
    &#125;
    
    .child &#123;
        border: 5px solid rgb(233, 250, 84);
        width:100px;
        height: 100px;
        float: left;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>自适应两栏布局</li>
</ul>
<pre><code class="copyable"> <div class="left">LEFT</div>
 <div class="right">RIGHT</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"> *&#123;
        margin: 0;
        padding: 0;
    &#125;
    body &#123;
        width: 100%;
        position: relative;
    &#125;
 
    .left &#123;
        width: 100px;
        height: 150px;
        float: left;
        background: rgb(139, 214, 78);
        text-align: center;
        line-height: 150px;
        font-size: 20px;
    &#125;
 
    .right &#123;
         /* 激活BFC */
        overflow: hidden;
        height: 300px;
        background: rgb(170, 54, 236);
        text-align: center;
        line-height: 300px;
        font-size: 40px;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>总结：因为BFC内部的元素和外部的元素绝对不会互相影响，因此， 当BFC外部存在浮动时，它不应该影响BFC内部Box的布局，BFC会通过变窄，而不与浮动有重叠。同样的，当BFC内部有浮动时，为了不影响外部元素的布局，BFC计算高度时会包括浮动的高度。避免margin重叠也是这样的一个道理。</strong></p></div>  
</div>
            