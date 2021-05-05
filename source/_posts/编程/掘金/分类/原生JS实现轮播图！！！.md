
---
title: '原生JS实现轮播图！！！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56ea36ce6c5c40e58a867240a981c59b~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 04 May 2021 20:36:06 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56ea36ce6c5c40e58a867240a981c59b~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>轮播图原理就是图片的移动</strong>。所有轮播图片横向排列，在一个窗口中显示一张图片，窗口外的图片隐藏，每一次一排图片就是移动一张图片的距离，切换到下一张图片，即可实现图片轮播。</p>
<p>图片的移动有两种方式：</p>
<ol>
<li><code>translate</code> 实现的图片移动</li>
<li><code>position</code>定位实现图片的偏移</li>
</ol>
<p>图片的自动播放，那必然用到定时器吧，而且是间隔定时器 <code>setInterval</code></p>
<p>该案例实现效果：</p>
<ul>
<li>图片自动播放</li>
<li>点击中间圆点按钮，实现图片任意切换</li>
<li>点击左右箭头按钮，实现图片左右切换</li>
<li>图片的切换对应小圆点的样式变化，即每一个小圆点对应一张图片</li>
</ul>
<p>先来看一下效果图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/56ea36ce6c5c40e58a867240a981c59b~tplv-k3u1fbpfcp-zoom-1.image" alt="img" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0"><code>html</code>格式：</h2>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 引入css样式 --></span>
<span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"./demo.css"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"banner_container"</span>></span>
    <span class="hljs-comment"><!-- 6张图片 --></span>
    <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"img_box"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"图片4"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"图片1"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"图片2"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"图片3"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"图片4"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"图片1"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>

    <span class="hljs-comment"><!-- 中间圆点 --></span>
    <span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"sel_box"</span>></span>
        <span class="hljs-comment"><!-- 自定义属性 --></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">data-index</span>=<span class="hljs-string">"0"</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">data-index</span>=<span class="hljs-string">"1"</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">data-index</span>=<span class="hljs-string">"2"</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">data-index</span>=<span class="hljs-string">"3"</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>

    <span class="hljs-comment"><!-- 左箭头 --></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"left_btn"</span>></span><span class="hljs-symbol">&lt;</span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-comment"><!-- 右箭头 --></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"right_btn"</span>></span><span class="hljs-symbol">&gt;</span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-comment"><!-- 引入js代码 --></span>
<span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./demo.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>大家别被骗了，这里轮播图只实现4张图片的播放，至于另外多出的两张，其实另有用处</p>
<p>第一张图片放置的其实四张轮播图中的最后一张，第6张图片其实是四张轮播图中的第一张，目的很简单，就是为了实现图片无缝轮播，下面用到的地方会说明哈</p>
<h2 data-id="heading-1"><code>CSS</code>样式</h2>
<pre><code class="hljs language-css copyable" lang="css">* &#123;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">box-sizing</span>: border-box;
&#125;

<span class="hljs-selector-class">.banner_container</span> &#123;
    <span class="hljs-attribute">position</span>: relative;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">400px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">250px</span>;
    <span class="hljs-comment">/* 超出隐藏 */</span>
    <span class="hljs-attribute">overflow</span>: hidden;  
&#125;

<span class="hljs-selector-tag">ul</span><span class="hljs-selector-class">.img_box</span> &#123;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
    <span class="hljs-comment">/* html中的第一张图片不是我们想要显示，第二张才是我们轮播图的第一张图片因此要让这排图片往左移动一张图片的距离 */</span>
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateX</span>(-<span class="hljs-number">400px</span>);
&#125;

<span class="hljs-selector-class">.img_box</span> <span class="hljs-selector-tag">li</span> &#123;
    <span class="hljs-attribute">float</span>: left;
    <span class="hljs-attribute">list-style</span>: none;
&#125;

<span class="hljs-comment">/* 图片大小 */</span>
<span class="hljs-selector-class">.img_box</span> <span class="hljs-selector-tag">li</span> <span class="hljs-selector-tag">img</span> &#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">400px</span>;
&#125;

<span class="hljs-comment">/* 小圆点 */</span>
<span class="hljs-selector-class">.sel_box</span> &#123;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">bottom</span>: <span class="hljs-number">15px</span>;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateX</span>(-<span class="hljs-number">50%</span>);
&#125;

<span class="hljs-selector-class">.sel_box</span> <span class="hljs-selector-tag">li</span> &#123;
    <span class="hljs-attribute">list-style</span>: none;
    <span class="hljs-comment">/* 转换为行内块元素 -- 一行显示 */</span>
    <span class="hljs-attribute">display</span>: inline-block;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">10px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">10px</span>;
    <span class="hljs-attribute">background-color</span>: pink;
    <span class="hljs-attribute">margin-right</span>: <span class="hljs-number">3px</span>;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">5px</span>;
    <span class="hljs-attribute">transition</span>: all <span class="hljs-number">0.4s</span>;
&#125;

<span class="hljs-comment">/* 左箭头 */</span>
<span class="hljs-selector-class">.left_btn</span> &#123;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateY</span>(-<span class="hljs-number">50%</span>);
    <span class="hljs-attribute">width</span>: <span class="hljs-number">25px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">30px</span>;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#fff</span>;
    <span class="hljs-attribute">line-height</span>: <span class="hljs-number">30px</span>;
    <span class="hljs-attribute">padding-left</span>: <span class="hljs-number">3px</span>;
    <span class="hljs-comment">/* 将鼠标样式改为小手 */</span>
    <span class="hljs-attribute">cursor</span>: pointer;
&#125;

<span class="hljs-selector-class">.right_btn</span> &#123;
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">375px</span>;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateY</span>(-<span class="hljs-number">50%</span>);
    <span class="hljs-attribute">width</span>: <span class="hljs-number">25px</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">30px</span>;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#fff</span>;
    <span class="hljs-attribute">line-height</span>: <span class="hljs-number">30px</span>;
    <span class="hljs-attribute">padding-left</span>: <span class="hljs-number">5px</span>;
    <span class="hljs-attribute">cursor</span>: pointer;
&#125;


<span class="hljs-comment">/* 当前图片的小图点样式 */</span>
<span class="hljs-selector-class">.sel_box</span> <span class="hljs-selector-class">.cur</span> &#123;
    <span class="hljs-attribute">background-color</span>: red<span class="hljs-meta">!important</span>;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scale</span>(<span class="hljs-number">1.3</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是简单的<code>css</code>样式，大家可以根据自己喜好自行编写样式</p>
<h2 data-id="heading-2">JavaScript</h2>
<p>上面的<code>html</code>结构 和 <code>css</code> 样式大家可以实行设置，轮播图的实现才是我们的重头戏</p>
<h3 data-id="heading-3">1、获取相关标签变量</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> img_box = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.img_box'</span>);
<span class="hljs-keyword">let</span> imgs = <span class="hljs-built_in">document</span>.querySelectorAll(<span class="hljs-string">'img'</span>);
<span class="hljs-keyword">let</span> sel_box = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.sel_box'</span>)
<span class="hljs-keyword">let</span> lis = sel_box.querySelectorAll(<span class="hljs-string">'li'</span>);
<span class="hljs-keyword">let</span> left_btn = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.left_btn'</span>);
<span class="hljs-keyword">let</span> right_btn = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.right_btn'</span>);
<span class="hljs-comment">// 记录第几张图片</span>
<span class="hljs-keyword">let</span> index = <span class="hljs-number">0</span>;  
<span class="hljs-keyword">let</span> timer = <span class="hljs-literal">null</span>;  <span class="hljs-comment">// 定时器</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>设置容器以及当前图片小圆点初始样式</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 设置图片容器大小</span>
<span class="hljs-comment">// imgContainerW：img_box本身宽度，为400</span>
<span class="hljs-keyword">let</span> imgContainerW = img_box.offsetWidth
img_box.style.width = imgContainerW * imgs.length + <span class="hljs-string">'px'</span>
<span class="hljs-comment">// 设置容器位置</span>
img_box.style.left = <span class="hljs-number">0</span> + <span class="hljs-string">'px'</span>;

<span class="hljs-comment">// 设置第一个小图片作为当前按钮</span>
lis[<span class="hljs-number">0</span>].className = <span class="hljs-string">'cur'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们将常用的操作封装成函数，简化代码结构</p>
<h3 data-id="heading-4">2、 轮播图切换</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">swapImg</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// 修改img_box的定位，往左偏移 index * imgContainerW</span>
    img_box.style.left = -index * imgContainerW + <span class="hljs-string">'px'</span>;
    <span class="hljs-comment">// 排他算法</span>
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < lis.length; i++) &#123;
        lis[i].className = <span class="hljs-string">''</span>;
    &#125;
    <span class="hljs-comment">// 修改小图标的样式</span>
    lis[index].className = <span class="hljs-string">'cur'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">3、轮播切换规律</h3>
<p>当我们的图片切换到四张轮播图的最后一张，下一张应该是第一张，但是这样直接切回第一张没有了过渡效果，我们想要的是四张轮播图片像是一个圆，一直无缝循环</p>
<p>所以我们就在四张轮播图的再后面放上第一张图片，当四张轮播图切换完后，下一张就切换到新增的这第一张图片，切换完毕，我们再<strong>趁机切换到四张图片的第一张，注意这次切换时无过渡效果的</strong>，这样图片播放又从第一张图片开始。</p>
<p>这就像魔术一样，只要够快，完全能够掩人耳目，骗过观众智慧的双眼，而这完全可以实现</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">swapFormat</span>(<span class="hljs-params"></span>) </span>&#123;
    index++;  <span class="hljs-comment">// 进入下一张图片</span>
    <span class="hljs-comment">// 如果是在最后一张图片</span>
    <span class="hljs-keyword">if</span> (index >= <span class="hljs-number">4</span>) &#123;
        <span class="hljs-comment">// 此处是为了防止频繁点击按钮，index++，导致index超过4，变成5、6、7...</span>
        <span class="hljs-comment">// 当index>=4，我们强行让其等于4,类似防抖</span>
        index = <span class="hljs-number">4</span>;  
        img_box.style.transition = <span class="hljs-string">'all, linear, 1s'</span>;
        img_box.style.left = -index * imgContainerW + <span class="hljs-string">'px'</span>;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < lis.length; i++) &#123;
            lis[i].className = <span class="hljs-string">''</span>;
        &#125;
        <span class="hljs-comment">// 修改小图标的样式</span>
        lis[<span class="hljs-number">0</span>].className = <span class="hljs-string">'cur'</span>

        <span class="hljs-comment">// 此处就是我们为实现无缝轮播，做的手脚 </span>
        <span class="hljs-comment">// 通过延时定时器，当图片过渡完，立刻马上切换到第一张图片</span>
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
            index = <span class="hljs-number">0</span>;  <span class="hljs-comment">// 第一张图片</span>
            img_box.style.transition = <span class="hljs-string">''</span>;  <span class="hljs-comment">// 无过度</span>
            swapImg();
        &#125;, <span class="hljs-number">1500</span>)

        <span class="hljs-comment">// 如果是其它图片，正常过渡切换</span>
    &#125; <span class="hljs-keyword">else</span> &#123;
        img_box.style.transition = <span class="hljs-string">'all, linear, 1.5s'</span>;
        swapImg();
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">4、添加间隔定时器</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 添加定时器，调用函数</span>
timer = <span class="hljs-built_in">setInterval</span>(swapFormat, <span class="hljs-number">3000</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">5、右箭头</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 点击右箭头，图片移动方式与自动播放一样</span>
right_btn.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    swapFormat();
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">6、左箭头</h3>
<p>点击左箭头与右箭头相反，图片往左移动，索引需要减一；同理，我们首张放置的就是四张轮播图片的最后一张，其用处也是在这里，拿它来做个“跳板”，先过渡这张图片再切换到真正的最后一张，无缝轮播</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 点击左箭头</span>
left_btn.addEventListener(<span class="hljs-string">'click'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    index--;
    <span class="hljs-comment">// 如果要切换到第四章</span>
    <span class="hljs-keyword">if</span> (index < <span class="hljs-number">0</span>) &#123;
        index = -<span class="hljs-number">1</span>
        img_box.style.transition = <span class="hljs-string">'all, linear, 1.5s'</span>;
        img_box.style.left = -index * imgContainerW + <span class="hljs-string">'px'</span>;
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < lis.length; i++) &#123;
            lis[i].className = <span class="hljs-string">''</span>;
        &#125;
        <span class="hljs-comment">// 修改小图标的样式</span>
        lis[<span class="hljs-number">3</span>].className = <span class="hljs-string">'cur'</span>

        <span class="hljs-comment">// "出老千",迅速切换</span>
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
            index = <span class="hljs-number">3</span>
            img_box.style.transition = <span class="hljs-string">''</span>;
            swapImg();
        &#125;, <span class="hljs-number">1000</span>)

    &#125; <span class="hljs-keyword">else</span> &#123;
        img_box.style.transition = <span class="hljs-string">'all, linear, 1.5s'</span>;
        swapImg();
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">7、清除和开启定时器</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 当鼠标在图片上、左箭头、右箭头时清除定时器，即图片不轮播</span>
img_box.addEventListener(<span class="hljs-string">'mouseover'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">clearInterval</span>(timer)
&#125;)

right_btn.addEventListener(<span class="hljs-string">'mouseover'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">clearInterval</span>(timer)
&#125;)

left_btn.addEventListener(<span class="hljs-string">'mouseover'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-built_in">clearInterval</span>(timer)
&#125;)

<span class="hljs-comment">// 当鼠标离开图片、左箭头、右箭头时开启定时器，即图片继续轮播</span>
img_box.addEventListener(<span class="hljs-string">'mouseout'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    timer = <span class="hljs-built_in">setInterval</span>(swapFormat, <span class="hljs-number">3000</span>)
&#125;)

left_btn.addEventListener(<span class="hljs-string">'mouseout'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    timer = <span class="hljs-built_in">setInterval</span>(swapFormat, <span class="hljs-number">3000</span>)
&#125;)

right_btn.addEventListener(<span class="hljs-string">'mouseout'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    timer = <span class="hljs-built_in">setInterval</span>(swapFormat, <span class="hljs-number">3000</span>)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总结：</p>
<ol>
<li>我们要在全局上声明一个<code>index</code>变量来记录目前是第几张图片，这样无论我们在点击左箭头还是右箭头或是小圆点之后，下一步的操作才能接着我们上面的图片进行轮播</li>
<li>实现图片无缝轮播救是在轮播图的前面和后面放置“跳板图片”，供我们跳转到正确的图片使用</li>
</ol></div>  
</div>
            