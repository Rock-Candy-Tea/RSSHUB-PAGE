
---
title: 'CSS动画与LESS、SASS框架'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2137'
author: 掘金
comments: false
date: Thu, 02 Sep 2021 19:39:37 GMT
thumbnail: 'https://picsum.photos/400/300?random=2137'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">实体字符</h2>
<p>可通过html代码、css代码来实现</p>
<p>调整实体字符在页面的显示方向：</p>
<p>顺时针转换方向</p>
<p>transform: rotate(361deg)</p>
<h2 data-id="heading-1">字体字符</h2>
<p>通过link <a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.fontawesome.com.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://www.fontawesome.com.cn/" ref="nofollow noopener noreferrer">www.fontawesome.com.cn/</a>引入字体字符样式表</p>
<p>控制大小需要在后面加一个类名单独控制</p>
<p>类名前加上 fa-spin可以让图标旋转</p>
<p>fa-pulse可以让图片八个方位旋转</p>
<h5 data-id="heading-2">1、通过bootCDN 搜索font-awesome 选择4.7.0版本，复制link路径min.css</h5>
<h5 data-id="heading-3">2、打开字体图标<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.fontawesome.com.cn" target="_blank" rel="nofollow noopener noreferrer" title="http://www.fontawesome.com.cn" ref="nofollow noopener noreferrer">www.fontawesome.com.cn</a>，复制图标代码</h5>
<h2 data-id="heading-4">CSS文本效果</h2>
<p>添加文本阴影：text-shadow: 5px 5px #ff0000;</p>
<pre><code class="copyable">h1
&#123;
    /* 三个值分别表示水平阴影，垂直阴影，模糊的距离，至少要有两个值 */
    text-shadow: 5px 5px 5px #FF0000;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>添加盒子阴影：box-shadow: 5px 5px 5px pink;</p>
<pre><code class="copyable">div
&#123;
    width:300px;
    height:100px;
    background-color:yellow;
    /* 前三个值与文本阴影表示的相同，盒子阴影可以取四个值，第四个值越大，盒子阴影的范围越大 */
    box-shadow: 10px 10px 5px #888888;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>写 box-shadow 的依次顺序为：</p>
<pre><code class="copyable">h-shadow   v-shadow   blur   spread   color   insect
​
水平阴影    垂直阴影   模糊    阴影尺寸  颜色   外阴影转到内阴影 
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-5">也可以在 ::before 和 ::after 两个伪元素中添加阴影效果</h6>
<h5 data-id="heading-6">当容器中的内容不能完全显示时，控制多余部分的显示样式</h5>
<p>1、显示省略号：text-overflow: ellipsis;</p>
<p>2、裁剪：text-overflow: clip;</p>
<pre><code class="copyable">.box5 &#123;
    width: 300px;
    height: 100px;
    overflow: hidden
     /* 溢出的文本会显示省略号 */
    text-overflow: ellipsis;
    /* 溢出的文本会直接被截断 */
    text-overflow: clip;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-7">允许长文本换行:</h5>
<p>字换行：p &#123;word-wrap:break-word;&#125;</p>
<p>单词拆分换行：p &#123;word-break: keep-all;&#125;</p>
<pre><code class="copyable">p&#123;
    width: 11em;
    border: 1px solid;
    /* 强制换行 */
    word-wrap:break-word;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-8">不生成盒子，内容不显示：display：none；</h5>
<h4 data-id="heading-9">不显示内容，会生成盒子占位置：visibility：hidden；</h4>
<h2 data-id="heading-10">2D转换</h2>
<h2 data-id="heading-11">translate() 方法</h2>
<p>1、转换位置：transform</p>
<p>translate（50px，100px）是从元素左边移动50个像素，并从顶部移动100像素。</p>
<pre><code class="copyable">.box2&#123;
    width: 400px;
    height: 200px;
    background-color:darksalmon;
    /* 要给两个值  第一个值表示水平位置，第二个值表示垂直位置 */
    transform: translate(100px,200px);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、transform:转换角度</p>
<p>rotate(90deg)在一个给定度数顺时针旋转的元素。允许负值，这样是元素逆时针旋转。使它旋转必须要更改display的值为行内块盒</p>
<pre><code class="copyable">div
&#123;
    width:200px;
    height:100px;
    background-color:yellow;
    /* 使它旋转必须要更改display的值 */
    display: inline-block;
    transform:rotate(30deg);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、转换大小：transform:scale(2,3);</p>
<p>该元素增加或减少的大小，取决于宽度（X轴）和高度（Y轴）的参数：转变宽度为原来的大小的2倍，和其原始大小3倍的高度。</p>
<pre><code class="copyable">.box3&#123;
    width: 400px;
    height: 200px;
    background-color:rgb(203, 233, 122);
    /* 转变宽度为原来的大小的2倍，和其原始大小3倍的高度 */
    transform: scale(2,3);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4、transform: skew(30deg,20deg);</p>
<p>包含两个参数值，分别表示X轴和Y轴倾斜的角度，如果第二个参数为空，则默认为0，参数为负表示向相反方向倾斜。</p>
<ul>
<li>
<p>skewX();表示只在X轴(水平方向)倾斜。</p>
</li>
<li>
<p>skewY();表示只在Y轴(垂直方向)倾斜。</p>
<h2 data-id="heading-12">matrix() 方法</h2>
<p>matrix()方法和2D变换方法合并成一个。</p>
<p>matrix 方法有六个参数，包含旋转，缩放，移动（平移）和倾斜功能。</p>
<p>利用matrix()方法旋转div元素30°</p>
<pre><code class="copyable">div
&#123;
transform:matrix(0.866,0.5,-0.5,0.866,0,0);
-ms-transform:matrix(0.866,0.5,-0.5,0.866,0,0);
-webkit-transform:matrix(0.866,0.5,-0.5,0.866,0,0);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h6 data-id="heading-13">画三角形：</h6>
<h6 data-id="heading-14">设置四个方向的边框线，其他三个方向设置透明transparent</h6>
<h2 data-id="heading-15">置换元素</h2>
<h5 data-id="heading-16">1、置换元素就是浏览器根据元素的标签和属性，来决定元素的具体展示内容。</h5>
<p>一个内容 不受CSS视觉格式化模型控制，CSS渲染模型并不考虑对此内容的渲染，且元素本身一般拥有固有尺寸（宽度，高度，宽高比）的元素，被称之为置换元素。置换元素一般有内在尺寸，所以具有width和height，可以进行设定。</p>
<p>HTML中的img、input、textarea、select、object都是置换元素。这些元素往往没有实际的内容，即是一个空元素。</p>
<h5 data-id="heading-17">2、非置换元素</h5>
<p>可以认为除去置换元素都是非置换元素</p>
<h2 data-id="heading-18">CSS动画</h2>
<p>创建动画：</p>
<pre><code class="copyable">@keyframes myfirst
&#123;
    /* 起始 */
    from &#123;background: red;&#125;
    /* 结束 */
    to &#123;background: yellow;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>绑定动画：</p>
<pre><code class="copyable">div
&#123;
    animation: myfirst 5s;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">.mydiv3&#123;
    width: 250px;
    height: 250px;
    position: absolute;
    animation: mydiv3 3s linear infinite;   
    /* infinite表示无限循环 */
&#125;
@keyframes mydiv3&#123;
    0%&#123;
        left: 0;
        top: 0;
    &#125;
    25%&#123;
        left: 1000px;
        top: 0;
    &#125;
    50%&#123;
        left: 1000px;
        top: 600px;
        transform: rotateX(150deg);   
    &#125;
    75%&#123;
        left: 0;
        top: 600px;
    &#125;
    100%&#123;
        left: 0;
        top: 0;
    &#125;
    0%&#123;
        background-color: pink;
    &#125;
    20%&#123;
        background-color: blueviolet;
    &#125;
    50%&#123;
        background-color: chartreuse;
    &#125;
    80%&#123;
        background-color: darkorange;
    &#125;
    100%&#123;
        background-color: pink;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable"> /* 为了更精确的效果，可将from、to改为百分数 */
@keyframes mymove&#123;
0%&#123;
    background-color: rgb(219, 163, 219);left: 0;top: 0;
&#125;
20%&#123;
    background-color: greenyellow;left: 200px;top: 200px;
&#125;
50%&#123;
    background-color: indianred;left: 150px;top: 70px;
&#125;
80%&#123;
    background-color:lightseagreen;left: 50px;top: 200px;
&#125;
100%&#123;
    background-color: rgb(219, 163, 219);left: 0;top: 0;
&#125;
 .box2&#123;
    width: 100px;
    height: 100px;
    background-color: rgb(219, 163, 219);
    position: absolute;
    animation: mymove linear 5s infinite;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-19">LESS框架与SASS框架</h1>
<h3 data-id="heading-20">三角形</h3>
<p>宽高为0，设置四周边框，其中一边设置透明</p>
<pre><code class="copyable">div&#123;
    width: 0;
    height: 0;
    border-top: 100px solid red;
    border-right: 100px solid green;
    border-bottom: 100px solid transparent;
    border-left: 100px solid pink;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-21">less与CSS区别</h2>
<h5 data-id="heading-22">1、注释：</h5>
<p>单行注释：// 不会出现在css里面</p>
<h5 data-id="heading-23">2、嵌套</h5>
<p>可以根据dom树（html文档结构）嵌套</p>
<h5 data-id="heading-24">3、可以定义变量</h5>
<p>全局作用域：写在最外面，没有包含块，可以复用</p>
<p>局部作用域：写在包含块里面，其他元素不能复用</p>
<h5 data-id="heading-25">4、可以进行四则运算（加减乘除），颜色不能进行运算</h5>
<h5 data-id="heading-26">5、mixins混入，声明一个样式快，直接运用</h5>
<h3 data-id="heading-27">声明变量：@</h3>
<pre><code class="copyable">@mycolor:red;
@width:300px;
@height:100px;
​
.box1&#123;
    width: @width;
    height: @height;
    background-color: @mycolor;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-28">全局作用域：</h4>
<pre><code class="copyable">// 其他元素可以复用当前变量
@mycolor:red;
@width:300px;
@height:100px;
.box1&#123;
    width: @width;
    height: @height;
    background-color: @mycolor;
&#125;
.box2&#123;
    width: @width;
    height: @height;
    background-color: @mycolor;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-29">局部作用域：</h4>
<pre><code class="copyable">//声明块里面的变量 其他元素不能复用
//访问不到变量，会报错
.box3&#123;
    @masize:30px;
    font-size: @masize;    
&#125;
.box4&#123;
    font-size: @masize;
&#125;
​
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-30">嵌套：</h4>
<p>直接写到父元素里面，css里面会以后代选择器的方式显示</p>
<pre><code class="copyable"> <div class="box5">
        <p>王盗盗</p>
        <p>
            <a href="">盆鱼宴</a>
        </p>
    </div>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">.box5&#123;
    width: @width;
    height: @height;
    p&#123;
        width: 50px;
        height: 50px;
        background-color: pink;
    &#125;
    a&#123;
        text-decoration: line-through;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-31">mixins（混入）</h4>
<p>直接引入其他带有声明块的（class）属性</p>
<pre><code class="copyable">.border&#123;
    border: 2px dotted;
&#125;
.box6&#123;
    width: @width;
    height: @height;
    .border;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-32">默认不带值</h4>
<p>用的时候需要给他传值</p>
<pre><code class="copyable">.common(@radius,@padding,@color)&#123;
    border-radius: @rodius;
    padding: @padding;
    color: @color;
&#125;
//设置值之后传回.common计算
.box7&#123;
    width: @width;
    height: @height;
    background-color: @mycolor
    .common(100%,30px,pink);
&#125;
.box8&#123;
    width: @width;
    height: @height;
    background-color: @mycolor
    .common(100%,30px,pink);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-33">带值</h4>
<pre><code class="copyable">.common(@radius,@padding:30px,@color:green)&#123;
    border-radius: @radius;
    padding: @padding;
    color: @color;
&#125;
.box9&#123; 
    width: @width;
    height: @height;
    background-color: @mycolor;
    .common(100%,@padding,@color);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-34">不带值(要传值)的写在最前面,不传值的写在后面，可以不写</h4>
<pre><code class="copyable">.common(@radius：20%,@padding：20px,@color)&#123;
    color: @color;//不带值，需要传值的写在最前面
    border-radius: @radius;
    padding: @padding;    
&#125;
.box9&#123; 
    width: @width;
    height: @height;
    background-color: @mycolor;
    .common(pink,@radius，@padding//不传值的写在后面，可以不写);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-35">两个都有值的时候，优先使用距离最近的值</h4>
<pre><code class="copyable">.common(@radius,@padding:30px,@color:green)&#123;
    border-radius: @radius;
    padding: @padding;
    color: @color;
&#125;
.box9&#123; 
    width: @width;
    height: @height;
    background-color: @mycolor;
    .common(100%,50px,pink);
&#125;
//padding会取50px的值
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-36">可以进行四则运算，除号需要用括号包起来</h4>
<pre><code class="copyable"> /* 减号前后要空一格*/
.common(@radius,@padding,@color:green)&#123;
    border-radius: @radius;
    padding: @padding;
    color: @color;
&#125;
.box10&#123; 
    width: (@width/2);
    height: （@height /3）;
    background-color: @mycolor;
    .common(100%,50px,pink);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-37">SCSS</h2>
<h4 data-id="heading-38">什么时候声明变量</h4>
<p>1、该值至少重复出现2次</p>
<p>2、该值至少可能被更新一次</p>
<p>3、该值所有的表现都与变量有关</p>
<h5 data-id="heading-39">通过@include引用混合宏</h5>
<pre><code class="copyable">/*default表示默认值*/
$mycolor:pink !default;
$margin:20px 0;
/*使⽤@mixin声明了⼀个混合宏后，需要使⽤ @include 来调⽤声明好的混合宏 
 混合宏传多个参数与less的混入规则相同*/
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">​
// 混合宏 声明变量
@mixin border-radius&#123;
    border-radius: 30%;
&#125;
button&#123;
    //调用混合宏
    @include border-radius;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-40">继承</h4>
<h5 data-id="heading-41">通过@extend 来继承已经存在的样式块</h5>
<pre><code class="copyable">.button &#123;
    border   : 1px solid #ccc;
    padding  : 5px 10px;
    font-size: 20px;
&#125;
.box &#123;
    background: #f36;
    color     : white;
    @extend .button;
&#125;
.box &#123;
    background: #ddd;
    color     : #000;
    @extend .button;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-42">占位符</h4>
<pre><code class="copyable">/*占位符 %zhanwei声明的代码如果不被@extend调⽤的话，不会产⽣任何代码。取代从前CSS中的代码冗余的情形。*/
%zhanwei &#123;
    margin-top: 5px;
    padding-top: 5px;
&#125;
/*这段代码没有被 @extend 调⽤，他并没有产⽣任何代码块，只是静静的躺在你的某个 SCSS ⽂件中。
只有通过 @extend 调⽤才会产⽣代码：*/
.size &#123;
    width: 100px;
    height: 100px;
&#125;
.box4 &#123;
    @extend .size ;
    background-color: $mycolor;
    @extend %zhanwei;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-43">响应式布局</h2>
<p>针对不同屏幕显示不同效果</p>
<h4 data-id="heading-44">媒体查询</h4>
<p>媒体查询可以控制在不同屏幕宽度显示的效果</p>
<p>1、通过@media 关键字定义媒体查询</p>
<p>2、min-width 屏幕最小宽度</p>
<p>3、max-width 屏幕最大宽度</p>
<p>4、给定范围时，通过 and 连接</p>
<h5 data-id="heading-45">浏览器视口小于600px时</h5>
<pre><code class="copyable">.box1&#123;
            width: 100px;
            height: 100px;
            background-color: blueviolet;
        &#125;
         @media (max-width:600px)/* 视口宽度小于600px */&#123;
             .box1&#123;
                 width: 600px;
                 height: 600px;
                 background-color: yellow;
             &#125;
         &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-46">浏览器视口大于或等于600px时</h5>
<pre><code class="copyable">.box1&#123;
            width: 100px;
            height: 100px;
            background-color: blueviolet;
        &#125;
        /* 屏幕（浏览器视口）宽度大于或等于600时 生效*/
         @media (min-width:600px)&#123;
            .box1&#123;
                width: 500px;
                height: 500px;
                background-color: pink;
            &#125;
        &#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-47">另一种写法 给定范围通过and连接</h5>
<pre><code class="copyable">@media screen and (max-width:600px)&#123;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-48">屏幕宽度在600-1000之间时</h5>
<pre><code class="copyable"> .box1&#123;
            width: 100px;
            height: 100px;
            background-color: blueviolet;
        &#125;
        @media (min-width:600px) and (max-width:1000px)&#123;
            .box1&#123;
                width: 600px;
                height: 600px;
                background-color: pink;
            &#125;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-49">屏幕宽度在1000-1600px时</h5>
<pre><code class="copyable">.box1&#123;
            width: 100px;
            height: 100px;
            background-color: blueviolet;
        &#125;
        @media (min-width:1000px) and (max-width:1600px)&#123;
            .box1&#123;
                width: 600px;
                height: 600px;
                background-color: orange;
            &#125;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-50">单独创建媒体查询css样式，通过link引入</h3>
<h3 data-id="heading-51">设置media范围</h3>
<pre><code class="copyable"><head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="./day16-1.css" media="(max-width:600px)">
    <link rel="stylesheet" href="./media600.css" media="(min-width:600px) and (max-width:1000px)">
    <link rel="stylesheet" href="./media1000.css" media="(min-width:1000px) and (max-width:1600px)">
</head>
<body>
    <div class="box1"></div>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-52">media600.css</h4>
<pre><code class="copyable">@media (min-width:600px) and (max-width:1000px)&#123;
    .box1&#123;
        width: 500px;
        height: 300px;
        background-color: blue;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-53">media1000.css</h4>
<pre><code class="copyable">@media (min-width:1000px)&#123;
    .box1&#123;
        width: 600px;
        height: 300px;
        background-color: pink;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-54">开发方式</h2>
<h4 data-id="heading-55">渐进增强，优雅降级</h4>
<p>渐进增强：更新新功能、新人物、新玩法等</p>
<p>优雅降级：特殊性企业，为了保证安全等，一直保持低版本</p>
<h4 data-id="heading-56">业务挂钩，用户群体</h4>
<p>开发采用的方式跟项目类型和所针对的用户群体有关，不同项目有不同的开发方式</p></div>  
</div>
            