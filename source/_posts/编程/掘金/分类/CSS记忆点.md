
---
title: 'CSS记忆点'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://user-gold-cdn.xitu.io/2019/7/20/16c0f492d4571704?imageView2/0/w/1280/h/960/ignore-error/1'
author: 掘金
comments: false
date: Fri, 23 Jul 2021 21:41:08 GMT
thumbnail: 'https://user-gold-cdn.xitu.io/2019/7/20/16c0f492d4571704?imageView2/0/w/1280/h/960/ignore-error/1'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、盒模型</h2>
<p>元素的内在盒子是由<code>margin box</code>、<code>border box</code>、<code>padding box</code>、<code>content box</code>组成的，这四个盒子由外到内构成了盒模型。</p>
<ul>
<li>content-box，默认值，只计算内容的宽度，border和padding不计算入width之内</li>
<li>padding-box，padding计算入宽度内</li>
<li>border-box，border和padding计算入宽度之内</li>
</ul>
<h2 data-id="heading-1">二、CSS基础</h2>
<h3 data-id="heading-2">1、 CSS 有哪些样式可以给子元素继承!</h3>
<ul>
<li>可继承的:<code>font-size</code>,<code>font-weight</code>,<code>line-height</code>,<code>color</code>,<code>cursor</code>等</li>
<li>不可继承的一般是会改变盒子模型的:<code>display</code>,<code>margin</code>、<code>border</code>、<code>padding</code>、<code>height</code>等</li>
</ul>
<p>更加全面的可以到引擎找</p>
<h3 data-id="heading-3">2、 行内元素有哪些？块级元素有哪些？ 空(void)元素有那些？</h3>
<p>块级元素是指单独撑满一行的元素，如<code>div、ul、li、table、p、h1</code>等元素。这些元素的display值默认是<code>block、table、list-item</code>等。</p>
<p>内联元素又叫行内元素，指只占据它对应标签的边框所包含的空间的元素，这些元素如果父元素宽度足够则并排在一行显示的，如<code>span、a、em、i、img、td</code>等。这些元素的display值默认是<code>inline、inline-block、inline-table、table-cell</code>等。</p>
<p>实际开发中，我们经常把<code>display</code>计算值为<code>inline</code> <code>inline-block</code> <code>inline-table</code> <code>table-cell</code>的元素叫做内联元素，而把<code>display</code>计算值为<code>block</code>的元素叫做块级元素。</p>
<h3 data-id="heading-4">3、width: auto 和 height: auto</h3>
<p><code>width</code>、<code>height</code>的默认值都是<code>auto</code>。</p>
<p>对于块级元素，流体布局之下<code>width: auto</code>自适应撑满父元素宽度。这里的撑满并不同于<code>width: 100%</code>的固定宽度，而是像水一样能够根据<code>margin</code>不同而自适应父元素的宽度。</p>
<p>对于内联元素，<code>width: auto</code>则呈现出包裹性，即由子元素的宽度决定。</p>
<p>无论内联元素还是块级元素，<code>height: auto</code>都是呈现包裹性，即高度由子级元素撑开。</p>
<p>注意父元素<code>height: auto</code>会导致子元素<code>height: 100%</code>百分比失效。</p>
<p>css的属性非常有意思，正常流下，如果块级元素的<code>width</code>是个固定值，<code>margin</code>是<code>auto</code>，则<code>margin</code>会撑满剩下的空间；如果<code>margin</code>是固定值，<code>width</code>是<code>auto</code>，则<code>width</code>会撑满剩下的空间。这就是流体布局的根本所在。</p>
<h3 data-id="heading-5">4、消除图片底部间隙的方法</h3>
<ul>
<li>图片块状化 - 无基线对齐：<code>img &#123; display: block; &#125;</code></li>
<li>图片底线对齐：<code>img &#123; vertical-align: bottom; &#125;</code></li>
<li>行高足够小 - 基线位置上移：<code>.box &#123; line-height: 0; &#125;</code></li>
</ul>
<h3 data-id="heading-6">5、层叠上下文</h3>
<p>层叠上下文好像是一个结界，层叠上下文内的元素如果跟层叠上下文外的元素发生层叠，则比较该层叠上下文和外部元素的层叠上下文的层叠水平高低。</p>
<p><strong>创建一个层叠上下文的方法就是给<code>position</code>值为<code>relative/aboslute/fixed</code>的元素设置<code>z-index</code>不为<code>auto</code>的值。</strong></p>
<h2 data-id="heading-7">三、CSS3特性</h2>
<h3 data-id="heading-8">1、CSS 中transition和animate有何区别? animate 如何停留在最后一帧!</h3>
<p>这种问题见仁见智,我的回答大体是这样的..待我捋捋.</p>
<p><code>transition</code>一般用来做过渡的, 没时间轴的概念, 通过事件触发(一次),没中间状态(只有开始和结束)</p>
<p>而<code>animate</code>则是做动效,有时间轴的概念(帧可控),可以重复触发和有中间状态;</p>
<p>过渡的开销比动效小,前者一般用于交互居多,后者用于活动页居多;</p>
<p>至于如何让<code>animate</code>停留在最后一帧也好办,就它自身参数的一个值就可以了</p>
<h3 data-id="heading-9">2、word-spacing 空格间隙</h3>
<p>不要被表面意思误导，<code>word-spacing</code>指的是字符“空格”的间隙。如果一段文字中没有空格，则该属性无效。下面代码设定空格间隙是<code>20px</code>，也就是说空格现在占据的宽度是原有的空格宽度+<code>20px</code>的宽度：</p>
<pre><code class="copyable"><p>我有空 格，我该死......</p>
<style>
  p &#123;
    word-spacing: 20px;
  &#125;
</style>
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">3、white-space 空白处理</h3>
<p>我们都知道如果在<code>html</code>中输入多个空白符，默认会被当成一个空白符处理，实际上就是这个属性控制的：<a href="https://link.juejin.cn/?target=http%3A%2F%2Fjs.jirengu.com%2Fdanim%2F1%2Fedit%3Fhtml%2Ccss%2Coutput" title="https://link.juejin.cn/?target=http%3A%2F%2Fjs.jirengu.com%2Fdanim%2F1%2Fedit%3Fhtml%2Ccss%2Coutput" target="_blank">地址</a></p>
<ol>
<li>normal：合并空白符和换行符；</li>
<li>nowrap：合并空白符，但不许换行；</li>
<li>pre：不合并空白符，并且只在有换行符的地方换行；</li>
<li>pre-wrap：不合并空白符，允许换行符换行和文本自动换行；</li>
</ol>
<p><img src="https://user-gold-cdn.xitu.io/2019/7/20/16c0f492d4571704?imageView2/0/w/1280/h/960/ignore-error/1" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-11">四、CSS选择器及其优先级</h2>
<h3 data-id="heading-12">1、CSS选择器</h3>
<ul>
<li>!important</li>
<li>内联样式style=""</li>
<li>ID选择器#id</li>
<li>类选择器/属性选择器/伪类选择器.class.active[href=""]</li>
<li>元素选择器/关系选择器/伪元素选择器html+div>span::after</li>
<li>通配符选择器*</li>
</ul>
<h3 data-id="heading-13">2、权重值和选择器 </h3>
<ol>
<li> 1,0,0,0 内联样式：style="" </li>
<li> 0,1,0,0 ID选择器：<code>#idName&#123;...&#125;</code> </li>
<li> 0,0,1,0 类、伪类、属性选择器：<code>.className&#123;...&#125;</code> / <code>:hover&#123;...&#125;</code> / <code>[type="text"] =&#123;...&#125;</code> </li>
<li> 0,0,0,1 标签、伪元素选择器：<code>div&#123;...&#125;</code> / <code>:after&#123;...&#125;</code> </li>
<li> 0,0,0,0 通用选择器（*）、子选择器（>）、相邻选择器（+）、同胞选择器（~）</li>
</ol>
<p>当两个权值进行比较的时候，是从高到低逐级将等级位上的权重值来进行比较的，而不是 1000个数 + 100个数 + 10个数 + 1个数 的总和来进行比较的，换句话说，低等级的选择器个数再多也不会超过高等级的选择器的优先级的。</p>
<h3 data-id="heading-14">3、<code>**!important**</code>的权重最高</h3>
<p>如果出现了<code>!important</code>，则不管权重如何都取有<code>!important</code>的属性值。但是宽高有例外情况，由于宽高会被<code>max-width</code>/<code>min-width</code>覆盖，所以<code>!important</code>会失效。</p>
<h3 data-id="heading-15">4、 !important问题</h3>
<p>超越<code>!important</code>：max-width会覆盖width，而且这种覆盖是超级覆盖，比<code>!important</code>的权重还要高</p>
<p>超越最大：min-width覆盖max-width，此规则发生在min-width和max-width冲突的时候，如下：</p>
<pre><code class="copyable">.container&#123;
    min-width:1400px;
    max-width:1200px;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">5、面试题举例</h3>
<pre><code class="copyable">// 假设下面样式都作用于同一个节点元素`span`，判断下面哪个样式会生效
body#god div.dad span.son &#123;width: 200px;&#125;
body#god span#test &#123;width: 250px;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因此上面那道的面试题比较应该是在第二等级id选择器的比较就结束了：(#god + #test = 0,2,0,0) > (#god = 0,1,0,0)；而上图种例子中两个权重分别是：(#test = 0,1,0,0) > (.test....test10 = 0,0,11,0)，也是在第二等级id选择器的比较时就结束了。所以以后比较权重，就先比较id选择器个数，如果id一样多，再比较class选择器个数。</p>
<h2 data-id="heading-17">五、BFC</h2>
<p>BFC（Block Formatting Context）格式化上下文，是Web页面中盒模型布局的CSS渲染模式，指一个独立的渲染区域或者说是一个隔离的独立容器。 </p>
<h3 data-id="heading-18">BFC应用</h3>
<ul>
<li>防止margin重叠</li>
<li>清除内部浮动</li>
<li>自适应两（多）栏布局</li>
<li>防止字体环绕</li>
</ul>
<h3 data-id="heading-19">触发BFC条件</h3>
<ul>
<li>根元素</li>
<li>float的值不为none</li>
<li>overflow的值不为visible</li>
<li>display的值为inline-block、table-cell、table-caption</li>
<li>position的值为absolute、fixed</li>
</ul>
<h3 data-id="heading-20">BFC的特性</h3>
<ul>
<li>
<p>内部的Box会在垂直方向上一个接一个的放置。</p>
</li>
<li>
<p>垂直方向上的距离由margin决定</p>
</li>
<li>
<p>bfc的区域不会与float的元素区域重叠。</p>
</li>
<li>
<p>计算bfc的高度时，浮动元素也参与计算</p>
</li>
<li>
<p>bfc就是页面上的一个独立容器，容器里面的子元素不会影响外面元素。</p>
</li>
</ul>
<h2 data-id="heading-21">六、水平居中</h2>
<p>1、行内元素</p>
<pre><code class="copyable">.parent &#123;
    text-align: center;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、块级元素</p>
<pre><code class="copyable">.son &#123;
    margin: 0 auto;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、flex布局</p>
<pre><code class="copyable">.parent &#123;
    display: flex;
    justify-content: center;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4、绝对定位定宽</p>
<pre><code class="copyable">.son &#123;
    position: absolute;
    width: 宽度;
    left: 50%;
    margin-left: -0.5*宽度
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>5、绝对定位不定宽</p>
<pre><code class="copyable">.son &#123;
    position: absolute;
    left: 50%;
    transform: translate(-50%, 0);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>6、left/right: 0</p>
<pre><code class="copyable">.son &#123;
    position: absolute;
    width: 宽度;
    left: 0;
    right: 0;
    margin: 0 auto;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-22">七、垂直居中</h2>
<p>1、行内元素</p>
<pre><code class="copyable">.parent &#123;
    height: 高度;
&#125;
.son &#123;
    line-height: 高度;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、table</p>
<pre><code class="copyable">.parent &#123;
  display: table;
&#125;
.son &#123;
  display: table-cell;
  vertical-align: middle;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、flex</p>
<pre><code class="copyable">.parent &#123;
    display: flex;
    align-items: center;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4、绝对定位定高</p>
<pre><code class="copyable">.son &#123;
    position: absolute;
    top: 50%;
    height: 高度;
    margin-top: -0.5高度;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>5、绝对定位不定高</p>
<pre><code class="copyable">.son &#123;
    position: absolute;
    top: 50%;
    transform: translate( 0, -50%);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>6、top/bottom: 0;</p>
<pre><code class="copyable">.son &#123;
    position: absolute;
    height: 高度;
    top: 0;
    bottom: 0;
    margin: auto 0;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h2 data-id="heading-23">八、CSS 引入的方式有哪些? link 和@import 的区别是?</h2>
<p>有四种：内联(元素上的style属性)、内嵌(style标签)、外链(link)、导入(@import) link和@import的区别：</p>
<ul>
<li>
<p><code>link</code>是XHTML标签，除了加载CSS外，还可以定义RSS等其他事务；<code>@import</code>属于CSS范畴，<code>只能加载CSS</code>。</p>
</li>
<li>
<p><code>link</code>引用CSS时，在<code>页面载入时同时加载</code>；<code>@import需要页面网页完全载入以后加载</code>。</p>
</li>
<li>
<p><code>link</code>是XHTML标签，<code>无兼容问题</code>；<code>@import</code>是在CSS2.1提出的，<code>低版本的浏览器不支持</code>。</p>
</li>
<li>
<p><code>link</code>支持使用Javascript控制DOM去<code>改变样式</code>；而<code>@import</code>不支持。</p>
</li>
</ul>
<h2 data-id="heading-24">九、flex布局</h2>
<h3 data-id="heading-25">父项常用属性</h3>
<ul>
<li>flex-direction：设置主轴的方向</li>
<li>justify-content：设置主轴上的子元素排列方式</li>
<li>flex-wrap：设置子元素是否换行</li>
<li>align-content：设置侧轴上的子元素的排列方式（多行）</li>
<li>align-items：设置侧轴上的子元素排列方式（单行）</li>
<li>flex-flow：复合属性，相当于同时设置了 flex-direction 和 flex-wrap</li>
</ul>
<h3 data-id="heading-26"><strong>flex-direction</strong></h3>
<p>在 flex 布局中，是分为主轴和侧轴两个方向，同样的叫法有 ： 行和列、x 轴和y 轴</p>
<ul>
<li>默认主轴方向就是 x 轴方向，水平向右</li>
<li>默认侧轴方向就是 y 轴方向，水平向下</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d41c14b8ca8049df93628bb15f58fa5c~tplv-k3u1fbpfcp-watermark.image" alt="<img src="./imgs/13.JPG">" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03ff6a64862c46eeae81ab0bdefc3493~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">： 主轴和侧轴是会变化的，就看 flex-direction 设置谁为主轴，剩下的就是侧轴。而我们的子元素是跟着主轴来排列的</p>
</blockquote>
<h3 data-id="heading-27"><strong>flex-wrap设置是否换行</strong></h3>
<ul>
<li>默认情况下，项目都排在一条线（又称”轴线”）上。flex-wrap属性定义，flex布局中默认是不换行的。</li>
<li>nowrap 不换行</li>
<li>wrap 换行</li>
</ul>
<h3 data-id="heading-28"><strong>justify-content 设置主轴上的子元素排列方式</strong></h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d7ec3b67898849098a3200bad3647a78~tplv-k3u1fbpfcp-watermark.image" alt="<img src="./imgs/14.jpg">" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>效果图</strong></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/12909eee01184c40bfa00e4045a30958~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"> <img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4b643805f83a429db6f87bcbb9efae3e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"> <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c820044d7fab4ca79f089f6eaa0e8cef~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"> <img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80be28824aa040b48989400dc268c457~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4cbefa7562ee4061b0c4a86486a78ead~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">： 这里讲下<code>space-around</code>和<code>space-evenly</code></p>
</blockquote>
<ul>
<li>space-around：项目之间的间距为左右两侧项目到容器间距的2倍。</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e8b1be252f784f058c76d2afff871733~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>space-evenly：项目两侧之间的间距与项目与容器两侧的间距相等，相当于除去项目宽度和容器和项目的两侧间距，剩下的平均分配了剩余宽度作为项目左右margin。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73eeb1a8bcdc43b7a23c084bee571806~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>**设置侧轴上的子元素排列方式：align-items(单行)/align-content(多行) **</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c1a465cf2e247c3997269f1e4619768~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b14b3aa24ce94c789942539bfdbaf5f8~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer">上图写能<code>设置多行</code>只能用于子项出现 换行 的情况（多行），在单行下是没有效果的。</p>
</blockquote>
<p>效果跟上面是一样的只不过是方向换了，上面是元素在主轴上排列，这个是在侧抽上，至于侧轴是不是Y轴就看你的<code>flex-direciton</code>怎么设置的了</p>
<h3 data-id="heading-29">子项常见属性</h3>
<ul>
<li>flex(复合属性): 默认: flex: 0 1 auto;
<ul>
<li>flex-grow</li>
<li>flex-shrink</li>
<li>flex-basis</li>
</ul>
</li>
<li>align-self：控制子项自己在侧轴的排列方式</li>
<li>order：定义子项的排列顺序(前后顺序), 0是第一个</li>
</ul>
<h3 data-id="heading-30"><strong>flex-grow</strong></h3>
<blockquote>
<p>默认0，用于决定项目在有剩余空间的情况下是否放大，默认不放大；注意，即便设置了固定宽度，也会放大。</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00a31e7f3f1e4506a1d82bf6a9cc7579~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>假设第一个项目默认为0，第二个项目为flex-grow:2，最后一个项目为1，则第二个项目在放大时所占空间是最后项目的两倍。</p>
<p>可以这么理解:</p>
<ul>
<li>
<p>flex: 1 => 在剩余的空间里我就占一份</p>
</li>
<li>
<p>flex: 2 => 在剩余的空间里我就占两份</p>
</li>
<li>
<p>flex: 3 => 在剩余的空间里我就占三份</p>
<p>假设三个盒子分别都设置了上面的属性: 那就将剩余空间分成6份, 各占自己的份数</p>
<p>假设前两个没有设置, 就最后一个设置了flex: 3 === flex: 1, 那就将剩余空间都给它
复制代码</p>
</li>
</ul>
<h3 data-id="heading-31"><strong>flex-shrink</strong></h3>
<blockquote>
<p>默认1，用于决定项目在空间不足时是否缩小，默认项目都是1，即空间不足时大家一起等比缩小；注意，即便设置了固定宽度，也会缩小。但如果某个项目flex-shrink设置为0，则即便空间不够，自身也不缩小。</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/85a26911f9c6477f8bc252f7ef3a5a3e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图中第二个项目flex-shrink为0，所以自身不会缩小。</p>
<h3 data-id="heading-32"><strong>flex-basis</strong></h3>
<blockquote>
<p>默认auto，用于设置项目宽度，默认auto时，项目会保持默认宽度，或者以width为自身的宽度，但如果设置了flex-basis，权重会width属性高，因此会覆盖widtn属性。</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/02d8e196e4ee4c37bc9781568a7992b2~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图中先设置了flex-basis属性，后设置了width属性，但宽度依旧以flex-basis属性为准。</p>
<blockquote>
<p>注意⚠: 如果当容器中有多个盒子并且还宽度100%, flex-basis会被影响, 如下图</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c58e210746a64abeb541eb61957d0a53~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>解决办法就是在我们设置<code>flex-basis</code>宽度时, 最好给他设置<code>flex-shrink</code>为0不缩放</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26bcb84abd3c496aa17d25e0b65e372b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-33">十、grid布局</h2>
<p><a href="https://juejin.cn/post/6854573220306255880" target="_blank" title="https://juejin.cn/post/6854573220306255880">最强大的 CSS 布局 —— Grid 布局 (juejin.cn)</a></p>
<h2 data-id="heading-34">十一、让元素消失</h2>
<p>visibility:hidden、display:none、z-index=-1、opacity：0</p>
<ol>
<li>
<p>opacity：0,该元素隐藏起来了，但不会改变页面布局，并且，如果该元素已经绑定了一些事件，如click事件也能触发</p>
</li>
<li>
<p>visibility:hidden,该元素隐藏起来了，但不会改变页面布局，但是不会触发该元素已经绑定的事件</p>
</li>
<li>
<p>display:none, 把元素隐藏起来，并且会改变页面布局，可以理解成在页面中把该元素删掉</p>
</li>
<li>
<p>z-index=-1置于其他元素下面</p>
</li>
</ol>
<h2 data-id="heading-35">十二、清除浮动</h2>
<ol>
<li>
<p>在浮动元素后面添加 <code>clear:both</code> 的空 div 元素，</p>
<div class="container">
    <div class="left"></div>
    <div class="right"></div>
    <div></div>
</div>
</li>
<li>
<p>给父元素添加 <code>overflow:hidden</code> 或者 auto 样式，触发BFC。</p>
<div class="container">
    <div class="left"></div>
    <div class="right"></div>
</div>
<p>.container&#123;
width: 300px;
background-color: #aaa;
overflow:hidden;
zoom:1;   /<em>IE6</em>/
&#125;</p>
</li>
<li>
<p>使用伪元素，也是在元素末尾添加一个点并带有 clear: both 属性的元素实现的。</p>
<div class="container clearfix">
    <div class="left"></div>
    <div class="right"></div>
</div>
<p>.clearfix&#123;
zoom: 1; /<em>IE6</em>/
&#125;
.clearfix:after&#123;
content: ".";
height: 0;
clear: both;
display: block;
visibility: hidden;
&#125;</p>
</li>
</ol>
<p><strong>推荐</strong>使用第三种方法，不会在页面新增div，文档结构更加清晰。</p>
<h2 data-id="heading-36">十三、calc函数</h2>
<p>calc函数是css3新增的功能，可以使用calc()计算border、margin、pading、font-size和width等属性设置动态值。</p>
<pre><code class="copyable">#div1 &#123;
    position: absolute;
    left: 50px;
    width: calc( 100% / (100px * 2) );
    //兼容写法
    width: -moz-calc( 100% / (100px * 2) );
    width: -webkit-calc( 100% / (100px * 2) );
    border: 1px solid black;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注意点：</p>
<ul>
<li>
<p>需要注意的是，运算符前后都需要保留一个空格，例如：width: calc(100% - 10px);</p>
</li>
<li>
<p>calc()函数支持 "+", "-", "*", "/" 运算;</p>
</li>
<li>
<p>对于不支持 calc() 的浏览器，整个属性值表达式将被忽略。不过我们可以对那些不支持 calc()的浏览器，使用一个固定值作为回退。</p>
</li>
</ul>
<h2 data-id="heading-37">十四、两边宽度固定中间自适应的三栏布局</h2>
<p>圣杯布局和双飞翼布局是前端工程师需要日常掌握的重要布局方式。两者的功能相同，都是为了实现一个两侧宽度固定，中间宽度自适应的三栏布局。</p>
<h3 data-id="heading-38">圣杯布局</h3>
<pre><code class="copyable"><style>
body&#123;
    min-width: 550px;
&#125;
#container&#123;
    padding-left: 200px;
    padding-right: 150px;
&#125;
#container .column&#123;
    float: left;
&#125;
#center&#123;
    width: 100%;
&#125;
#left&#123;
    width: 200px;
    margin-left: -100%;
    position: relative;
    right: 200px;
&#125;
#right&#123;
    width: 150px;
    margin-right: -150px;
&#125;
</style>
<div id="container">
    <div id="center" class="column">center</div>
    <div id="left" class="column">left</div>
    <div id="right" class="column">right</div>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7818898adc0846bc852ae153882ca047~tplv-k3u1fbpfcp-zoom-1.image" alt="Layout.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-39">双飞翼布局</h3>
<pre><code class="copyable"><style>
body &#123;
    min-width: 500px;
&#125;
#container &#123;
    width: 100%;
&#125;
.column &#123;
    float: left;
&#125;
#center &#123;
    margin-left: 200px;
    margin-right: 150px;
&#125;
#left &#123;
    width: 200px;
    margin-left: -100%;
&#125;
#right &#123;
    width: 150px;
    margin-left: -150px;
&#125;
</style>
<div id="container" class="column">
    <div id="center">center</div>
</div>
<div id="left" class="column">left</div>
<div id="right" class="column">right</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-40">十五、伪类和伪元素</h2>
<h3 data-id="heading-41">1、伪类</h3>
<p>伪类存在的意义是为了通过选择器找到那些不存在DOM树中的信息以及不能被常规CSS选择器获取到的信息。</p>
<ol>
<li>获取不存在与DOM树中的信息。比如a标签的:link、visited等，这些信息不存在与DOM树结构中，只能通过CSS选择器来获取；</li>
<li>获取不能被常规CSS选择器获取的信息。比如：要获取第一个子元素，我们无法用常规的CSS选择器获取，但可以通过 :first-child 来获取到。</li>
</ol>
<p><img src="https://user-gold-cdn.xitu.io/2019/12/12/16ef8eecad4f1adb?imageView2/0/w/1280/h/960/ignore-error/1" alt="weilei.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-42">2、伪元素</h3>
<p>伪元素用于创建一些不在文档树中的元素，并为其添加样式。比如说，我们可以通过:before来在一个元素前增加一些文本，并为这些文本添加样式。虽然用户可以看到这些文本，但是这些文本实际上不在文档树中。常见的伪元素有：<code>::before</code>，<code>::after</code>，<code>::first-line</code>，<code>::first-letter</code>，<code>::selection</code>、<code>::placeholder</code>等</p>
<blockquote>
<p>因此，伪类与伪元素的区别在于：有没有创建一个文档树之外的元素。</p>
</blockquote>
<h3 data-id="heading-43">3、::after和:after的区别</h3>
<p>在实际的开发工作中，我们会看到有人把伪元素写成<code>:after</code>，这实际是 CSS2 与 CSS3新旧标准的规定不同而导致的。</p>
<p>CSS2 中的伪元素使用1个冒号，在 CSS3 中，为了区分伪类和伪元素，规定伪元素使用2个冒号。所以，对于 CSS2 标准的老伪元素，比如<code>:first-line</code>，<code>:first-letter</code>，<code>:before</code>，<code>:after</code>，写一个冒号浏览器也能识别，但对于 CSS3 标准的新伪元素，比如::selection，就必须写2个冒号了。</p>
<h3 data-id="heading-44">4、基于伪元素的图片内容生成技术</h3>
<p>需求：图片还没加载时就把 <code>alt</code> 信息呈现出来。</p>
<p>实现：图片没有 <code>src</code> ，因此，<code>::before</code>和<code>::after</code> 可以生效，我们可以通过 <code>content</code> 属性呈现 alt 属性值。</p>
<pre><code class="copyable">img::after&#123;
    /* 生成 alt 信息 */
    content: attr(alt);
    /* 尺寸和定位 */
    postion:absolute; bottom: 0;
    width:100%;
    background-color:rgba(0,0,0,.5);
    transform: translateY(100%);
    transition: transform .2s;
&#125;
img:hover::after&#123;
    transform: translateY(0);
&#125;    
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我们给图片添加src 属性时图片从普通元素变成替换元素，原本还支持的<code>::before</code>和<code>::after</code> 此时全部无效，此时再hover图片，是不会有任何信息出现的。</p>
<h3 data-id="heading-45">5、 轻松实现hover图片变成另外一张图片</h3>
<pre><code class="copyable">img:hover&#123;
    content: url(laugh-tear.png);
&#125;
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>content 改变的仅仅是视觉呈现，当我们鼠标右键或其他形式保存这张图片时，所保存的还是原来 src 对应的图片。这种方法还可以用在官网标志上。</p>
<p>由于使用 conetnt 生成图片无法设置图片的尺寸，要想在移动端使用该技术，建议使用SVG图片</p>
<h2 data-id="heading-46">十六、流式布局与响应式布局的区别</h2>
<p><strong>流式布局</strong> 使用非固定像素来定义网页内容，<code>也就是百分比布局</code>，通过盒子的宽度设置成百分比来根据屏幕的宽度来进 行伸缩，不受固定像素的限制，内容向两侧填充。</p>
<p><strong>响应式开发</strong> 利用CSS3 中的 Media Query(媒介查询)，通过查询 screen 的宽度来指定某个宽度区间的网页布局。</p>
<ul>
<li>超小屏幕(移动设备) 768px 以下</li>
<li>小屏设备 768px-992px</li>
<li>中等屏幕 992px-1200px</li>
<li>宽屏设备 1200px 以上</li>
</ul>
<p>由于响应式开发显得繁琐些，一般使用第三方响应式框架来完成，比如 bootstrap 来完成一部分工作，当然也 可以自己写响应式。</p>
<p><strong>区别</strong></p>
<p>-</p>
<p>流式布局</p>
<p>响应式开发</p>
<p>开发方式</p>
<p>移动Web开发+PC开发</p>
<p>响应式开发</p>
<p>应用场景</p>
<p>一般在已经有PC端网站，开发移动的的时候只需要单独开发移动端</p>
<p>针对一些新建的网站，现在要求适配移动端，所以就一套页面兼容各种终端</p>
<p>开发</p>
<p>正对性强，开发效率高</p>
<p>兼容各种终端，效率低</p>
<p>适配</p>
<p>只适配移动设备，pad上体验相对较差</p>
<p>可以适配各种终端</p>
<p>效率</p>
<p>代码简洁，加载快</p>
<p>代码相对复杂，加载慢</p>
<h2 data-id="heading-47">十七、回流和重绘</h2>
<p><strong>回流</strong> 比如我们增删DOM节点，修改一个元素的宽高，页面布局发生变化，DOM树结构发生变化，那么肯定要重新构建DOM树，而DOM树与渲染树是紧密相连的。DOM树构建完，渲染树也随之对页面再次渲染，这个过程就叫回流。（结构会变）</p>
<p>导致回流的操作：</p>
<ul>
<li>页面首次渲染</li>
<li>浏览器窗口大小发生变化</li>
<li>元素尺寸发生改变（包括外边距、内边距、边框大小、高度和宽度）</li>
<li>元素的位置发生变化</li>
<li>元素内容变化（文字数量或图片大小等等）</li>
<li>元素字体大小变化</li>
</ul>
<p><strong>重绘</strong> 当页面中元素样式的改变并不影响它在文档流中的位置时（例如：color、background-color、visibility等），浏览器会将新样式赋予给元素并重新绘制它，这个过程称为重绘。（结构不变，样式改变）</p>
<h2 data-id="heading-48">十八、Sass常用的用法</h2>
<h3 data-id="heading-49">（1）变量</h3>
<p>SASS允许使用变量，所有变量以$开头。</p>
<pre><code class="copyable">/* 变量声明 */
$fontStack:    Helvetica, sans-serif;
$primaryColor: #333;

body &#123;
  font-family: $fontStack;
  color: $primaryColor;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>等同于👇css的写法</p>
<pre><code class="copyable">body &#123;
  font-family: Helvetica, sans-serif;
  color: #333;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果变量需要镶嵌在字符串之中，就必须需要写在#&#123;&#125;之中。</p>
<pre><code class="copyable">$side : left;
#div1 &#123;
    margin-#&#123;left&#125;:10px;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<h3 data-id="heading-50">（2）计算功能</h3>
</blockquote>
<p>SASS允许在代码中使用算式：</p>
<pre><code class="copyable">.div2 &#123;
    margin: 10px * 2;
    padding:(14px / 2);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>等同于👇css的写法</p>
<pre><code class="copyable">.div2 &#123;
    margin: 20px;
    padding: 7px;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<h3 data-id="heading-51">（3）嵌套</h3>
</blockquote>
<p>SASS允许选择器嵌套。比如:</p>
<ul>
<li>
<p><strong>选择器嵌套</strong></p>
<p>nav &#123;
ul &#123;
margin: 0;
padding: 0;
list-style: none;
&#125;</p>
<p>li &#123; display: inline-block; &#125;
&#125;</p>
</li>
</ul>
<p>等同于👇css的写法</p>
<pre><code class="copyable">nav ul &#123;
  margin: 0;
  padding: 0;
  list-style: none;
&#125;

nav li &#123;
  display: inline-block;
&#125;
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>&的嵌套</strong></li>
</ul>
<p>在嵌套的代码块内，可以使用<code>&</code>引用父元素。比如<code>a:hover</code>伪类，可以写成：</p>
<pre><code class="copyable">a &#123;
    margin: 10px;
    &:hover &#123;
        color: #000;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>等同于👇css的写法</p>
<pre><code class="copyable">a &#123;
    margin: 10px;
&#125;
a:hover &#123;
    color: #000;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><strong>属性嵌套(很少用，或者说不用，因为这样写更麻烦)</strong></li>
</ul>
<p>属性也可以嵌套，比如border-color属性，可以写成：</p>
<pre><code class="copyable">p&#123;
    border: &#123;  //注意，border后面必须加上冒号。
        color: #000;
    &#125;
&#125;

//转化css后
p&#123;
    border-color: #000;
&#125;
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<h3 data-id="heading-52">（4）继承</h3>
</blockquote>
<p>SASS允许一个选择器，继承另一个选择器。比如，现有div3：</p>
<pre><code class="copyable">.div3 &#123;
    margin: 2px;
&#125;

/* .div4继承.div3 */
.div4 &#123;  
    @extend .div3;
    font-size: 10px;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>等同于👇css的写法</p>
<pre><code class="copyable">.div3, .div4 &#123;
  margin: 2px;
&#125;
.div4 &#123;
  font-size: 10px;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<h3 data-id="heading-53">（5）Mixin</h3>
</blockquote>
<p>Mixin有点像C语言的宏（macro），是可以重用的代码块。</p>
<ul>
<li>
<p>1、使用@mixin命令，定义一个代码块</p>
</li>
<li>
<p>2、后续可以通过<code>@include</code>复用</p>
<p>@mixin p1 &#123;
float: left;
&#125;</p>
<p>div &#123;
/<em>使用@include命令，调用这个mixin。</em>/
@include p1;
top: 10px;
&#125;</p>
</li>
</ul>
<p>等同于👇css的写法</p>
<pre><code class="copyable">div &#123;
  float: left;
  top: 10px;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>mixin的强大之处，在于可以<strong>指定参数和缺省值</strong>。这样我们就可以复用一些样式，只需要传递一个参数，就像调用一个函数一样！</p>
</blockquote>
<ul>
<li>
<p>例子1: 没有默认值</p>
<p>@mixin box-sizing (<span class="math math-inline"><span class="katex-error" title="ParseError: KaTeX parse error: Expected '&#125;', got 'EOF' at end of input: …kit-box-sizing:" style="color:#cc0000">sizing) &#123;  -webkit-box-sizing:</span></span>sizing;<br>
-moz-box-sizing:<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>s</mi><mi>i</mi><mi>z</mi><mi>i</mi><mi>n</mi><mi>g</mi><mo separator="true">;</mo><mi>b</mi><mi>o</mi><mi>x</mi><mo>−</mo><mi>s</mi><mi>i</mi><mi>z</mi><mi>i</mi><mi>n</mi><mi>g</mi><mo>:</mo></mrow><annotation encoding="application/x-tex">sizing;  box-sizing:</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="mord mathnormal">s</span><span class="mord mathnormal">i</span><span class="mord mathnormal" style="margin-right:0.04398em;">z</span><span class="mord mathnormal">i</span><span class="mord mathnormal">n</span><span class="mord mathnormal" style="margin-right:0.03588em;">g</span><span class="mpunct">;</span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mord mathnormal">b</span><span class="mord mathnormal">o</span><span class="mord mathnormal">x</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span><span class="mbin">−</span><span class="mspace" style="margin-right:0.2222222222222222em;"></span></span><span class="base"><span class="strut" style="height:0.85396em;vertical-align:-0.19444em;"></span><span class="mord mathnormal">s</span><span class="mord mathnormal">i</span><span class="mord mathnormal" style="margin-right:0.04398em;">z</span><span class="mord mathnormal">i</span><span class="mord mathnormal">n</span><span class="mord mathnormal" style="margin-right:0.03588em;">g</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">:</span></span></span></span></span>sizing;
&#125;
.box-border&#123;
border:1px solid #ccc;
@include box-sizing(border-box);/<em>引用</em>/
&#125;</p>
</li>
</ul>
<p>等同于👇css的写法</p>
<pre><code class="copyable">.box-border &#123;
  border: 1px solid #ccc;
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>例子2:有默认值</p>
<ul>
<li>没有默认值的参数要放在参数列表的前面。</li>
</ul>
<p>@mixin p2(<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>v</mi><mi>a</mi><mi>l</mi><mn>1</mn><mo separator="true">,</mo></mrow><annotation encoding="application/x-tex">val1, </annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="mord mathnormal" style="margin-right:0.03588em;">v</span><span class="mord mathnormal">a</span><span class="mord mathnormal" style="margin-right:0.01968em;">l</span><span class="mord">1</span><span class="mpunct">,</span></span></span></span></span>val2:20px) &#123;
/* 如果不加入参数，就用默认参数 */
float: <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>v</mi><mi>a</mi><mi>l</mi><mn>1</mn><mo separator="true">;</mo><mi>t</mi><mi>o</mi><mi>p</mi><mo>:</mo></mrow><annotation encoding="application/x-tex">val1;  top: </annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="mord mathnormal" style="margin-right:0.03588em;">v</span><span class="mord mathnormal">a</span><span class="mord mathnormal" style="margin-right:0.01968em;">l</span><span class="mord">1</span><span class="mpunct">;</span><span class="mspace" style="margin-right:0.16666666666666666em;"></span><span class="mord mathnormal">t</span><span class="mord mathnormal">o</span><span class="mord mathnormal">p</span><span class="mspace" style="margin-right:0.2777777777777778em;"></span><span class="mrel">:</span></span></span></span></span>val2;
&#125;
//使用的时候，根据需要加入参数：
div &#123;
@include p2(left);
&#125;</p>
</li>
</ul>
<p>等同于👇css的写法</p>
<pre><code class="copyable">div &#123;
  float: left;
  top: 20px;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<h3 data-id="heading-54">（6）导入文件</h3>
</blockquote>
<ul>
<li>
<p>@import命令，用来插入外部文件。</p>
</li>
<li>
<p>如果插入的是.css文件，则等同于css的import命令。</p>
<p>@import "path/filename.scss";</p>
<p>@import "foo.css";</p>
</li>
</ul>
<blockquote>
<h3 data-id="heading-55">（7）注释</h3>
</blockquote>
<p>SASS共有两种注释风格。</p>
<ul>
<li>标准的CSS注释 /* comment */ ，会保留到编译后的文件。</li>
<li>单行注释 // comment，只保留在SASS源文件中，编译后被省略。</li>
</ul></div>  
</div>
            