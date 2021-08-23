
---
title: 'CSS 基础（新手友好）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe26a53483a141dda77a3a10632a842f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 22 Aug 2021 17:09:36 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe26a53483a141dda77a3a10632a842f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第23天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h1 data-id="heading-0">CSS 概念</h1>
<p>首先，什么是CSS？cascading style sheets    汉译层叠样式表，WEB标准中的表现标准语言,表现标准语言在网页中主要对网页信息的显示进行控制，简单说就是如何修饰网页信息的显示样式。</p>
<p>通俗易懂的说，页面好不好看都由CSS来决定，CSS的学习我们可以按照进阶的步调来走</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe26a53483a141dda77a3a10632a842f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"><img src="https://juejin.cn/post/6999426456661000199" alt title="点击并拖拽以移动" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">使用步骤</h2>
<p><strong>第一步：怎么创建CSS？CSS样式表创建的3种方式？</strong></p>
<p>答：</p>
<ol>
<li>内部样式 ：通过<code><style></style></code>标签进行创建，编写在<code>html</code>页面的<code>head</code>当中</li>
<li>外部样式： 创建 css 文件，通过<code><link rel="stylesheet" type="text/css" href="main.css" /> </code>进行引入，当然还有第二种引入的方式<code>@import url(main.css) </code> ,那么问题来了，我们该使用哪一个呢？以后更推荐<code>link</code>引入的方式，因为<code>import</code>的方式低版本浏览器不支持，而且在 JS 操作中，无法对它进行操作</li>
<li>内联（行内）样式：这个就比较亲民了，写法也很 easy 直接在标签内部添加<code>style</code>即可。<code><p style="" ></p></code></li>
</ol>
<blockquote>
<p>总结：以后实际开发中，更推荐的方式是外部样式 。 那么优先级呢？最高的是 内联样式-》内部/外部 看具体的书写顺序</p>
</blockquote>
<p><strong>第二步：知道 CSS 写在哪了，那具体的 CSS 要怎么写呢？</strong></p>
<p>答：1. CSS 语法： 选择符&#123;  属性：属性值；属性：属性值；  &#125; 注意分号不可丢</p>
<h2 data-id="heading-2">CSS 选择符(选择器)</h2>
<p>选择符的目的就是为了帮助我们找到页面上面的元素</p>
<ol>
<li>
<p>ID 选择器：在 html 中给标签添加 ID ，在 CSS 中通过  <code>#ID </code>名<code>&#123;  &#125; </code> 即可找到这个元素。注意<code>#</code>不可改,<code>id</code>不要重复（常用）</p>
</li>
<li>
<p>Class 选择符：在标签中添加 class，css 文件中通过 <code>.class名称&#123;  &#125; </code>，可以多个标签都用同一个<code>class</code>，当然一个标签也能用多个 class 通过空格分隔（常用）</p>
</li>
<li>
<p>通配符：<code>* </code>一个星号，有了它页面上所有的标签都会生效这个样式，它一般用来设置字体字号的</p>
</li>
<li>
<p>标签选择器：html 的标签名拿过来直接就是了，例如：<code>p&#123;  &#125; </code> 当然你这样写完之后，你页面上所有的<code>p</code>标签都会应用这个样式（常用）</p>
</li>
<li>
<p> 群组选择符：单个样式已经不能够阻挡你了，那么多个怎么写呢，很简单，通过逗号分隔就OK ，例如：<code>p,a,div&#123;  &#125; .div1,.p1,.a1&#123; &#125;</code>（常用）</p>
</li>
<li>
<p>后代选择符：当你想找到一个元素下的孩子们的时候，你会想到这个选择符，它的用法只需中间加一个空格，例如：<code>div a&#123;  &#125; </code>这句的意思就是 div 下面所有的a都会应用你写的这个 CSS 样式，注意：空格不可少（常用）</p>
</li>
<li>
<p>子元素选择符：写法 <code>div > a&#123;  &#125; </code>和后代的区别呢，很简单，子元素在家谱来说，就是只找到自己的孩子，孙子很明显不归它管</p>
</li>
<li>
<p>相邻兄弟选择器：<code>div + a &#123;  &#125; </code>和<code>div</code> 同级的<code>a</code>标签会生效样式，但是要求是必须是睡在上铺的兄弟，对面铺的都不行，必须要挨着<code>div</code>才行</p>
</li>
<li>
<p>后续兄弟选择器：<code>div~a&#123; &#125; </code>这个只要是同级的都可以找到</p>
</li>
</ol>
<h3 data-id="heading-3">选择符的优先级</h3>
<p>CSS 选择符有权重，如下：</p>
<ul>
<li>css中用四位数字表示权重，权重的表达方式如：0，0，0，0</li>
<li>类型选择符的权重为0001</li>
<li>class选择符的权重为0010</li>
<li>id选择符的权重为0100</li>
<li>子选择符的权重为0000</li>
<li>属性选择符的权重为0010</li>
<li>伪类选择符的权重为0010</li>
<li>伪元素选择符的权重为0010</li>
<li>包含选择符的权重：为包含选择符的权重之和</li>
<li>内联样式的权重为1000</li>
<li>继承样式的权重为0000</li>
</ul>
<p>从样式选择器看权重优先级：<code>important</code> > 内嵌样式 > <code>ID</code> > 类 > 标签 | 伪类 | 属性选择 > 伪对象 > 继承 > 通配符。</p>
<p>还有一点，CSS 选择符的权重，是计算的，比如你写了一个 ID 选择器和标签选择器，那么它的权重是把两个相加得到的结果</p>
<p>终于到了开始正式写CSS的地方了 噗 那上面都是什么，都是一群铺垫</p>
<h1 data-id="heading-4">CSS 基础</h1>
<h2 data-id="heading-5">文本相关的样式</h2>
<ol>
<li>
<p>文字大小 font-size   单位是px/em  注意；一般情况下PS量取字体的时候都是偶数</p>
</li>
<li>
<p>文字颜色 color 有三种方式写颜色 red 单词  #ccccc 16进制的方式 rgb(255,255,1)</p>
</li>
<li>
<p>字体 font-family 可以设置多个字体，逗号分隔，生效是看用户电脑上安装的字体，注意写字体加引号</p>
</li>
<li>
<p>加粗：&#123;font-weight:bolder(更粗的)/bold（加粗）/normal（常规）/100—900; but 600-900才能看出了加粗的效果</p>
</li>
<li>
<p>倾斜：font-style：italic(倾斜度小)/oblique（倾斜度大）/normal（取消倾斜，常规显示）;but 倾斜度小or大并看不出来</p>
</li>
<li>
<p>水平对齐方式 text-align:left/right/center</p>
</li>
<li>
<p>行高 &#123; line-height:normal/value; &#125; 行高小技巧，把行高和高度设置一样的，可以让元素内的内容垂直居中</p>
</li>
<li>
<p>文本修饰：text-decoration:none/underline/overline/line-through</p>
</li>
</ol>
<p>说明：</p>
<ul>
<li>none:没有修饰</li>
<li>underline:添加下划线</li>
<li>overline:添加上划线</li>
<li>line-through:添加删除线</li>
</ul>
<ol start="9">
<li>都是font开头的，font的简写版：</li>
</ol>
<p>说明:font的属性值应按以下次序书写(各个属性之间用空格隔开)
顺序: <code>font-style </code>| <code>font-weight </code>|<code> font-size</code> / <code>line-height</code> |<code> font-family</code>
例如：<code>font:bold italic 30px </code>"微软雅黑"</p>
<p>10.首行缩进：<code>&#123;text-indent:value;&#125; </code>那么值该是多少呢？如果你的字体大小是<code>12px</code>，想空两个格，那么就<code>text-indent:24px; </code>当然你也发现了这样计算好烦，虽然并没有超过100，还有一种更简单的方式，换个单位，<code>em</code> ，<code>1em=16px=100% </code>如果想空两个字，直接写<code>text-indent:2em;</code> 呦嚯嚯~</p>
<p>11.字间距<code>&#123;letter-spacing:value;&#125;</code>控制英文字母和汉字的字距。（英文字母和汉字）</p>
<ol start="12">
<li>词间距<code>&#123;word-spacing:value;&#125;</code>控制英文单词词距。（通用于英文词和词之间的间距,）对中文不起效果</li>
</ol>
<h2 data-id="heading-6">列表相关样式</h2>
<ol>
<li>
<p>定义列表符号样式：<code>list-style-type：disc(实心圆)/circle(空心圆)/square(实心方块)/none(去掉列表符号)；</code></p>
</li>
<li>
<p>定义列表符号的位置：<code>list-style-position:outside(外边)/inside(里边)；</code></p>
</li>
<li>
<p>使用图片作为列表符号：<code>list-style-image：url(所使用图片的路径及全称)；</code></p>
</li>
</ol>
<h2 data-id="heading-7">背景相关样式</h2>
<ol>
<li>
<p>背景颜色 语法：选择符<code>&#123;background-color:颜色值;&#125;</code></p>
</li>
<li>
<p>背景图片的设置  语法：<code>background-image：url(背景图片的路径及全称)；</code></p>
</li>
</ol>
<p>了解下目前的图片格式撒：</p>
<ul>
<li>jpg:有损压缩格式，靠损失图片本身的质量来减小图片的体积，适用于颜色丰富的图像;(像素点组成的，像素点越多会越清晰 )</li>
<li>gif：有损压缩格式，靠损失图片的色彩数量来减小图片的体积，支持透明，支持动画，适用于颜色数量较少的图像;</li>
<li>png:有损压缩格式，损失图片的色彩数量来减小图片的体积，支持透明，不支持动画，是 fireworks的 源文件格式，适用于颜色数量较少的图像;</li>
<li>WebP 在各大互联网公司已经使用得很多了 WebP 格式，谷歌（google）开发的一种旨在加快图片加载速度的图片格式。图片压缩体积大约只有 JPEG 的2/3，并能节省大量的服务器带宽资源和数据空间。Facebook Ebay 等知名网站已经开始测试并使用 WebP 格式。但 WebP 是一种有损压缩。相较编码 JPEG 文件，编码同样质量的WebP文件需要占用更多的计算资源。</li>
</ul>
<p> 
3. 背景图片平铺属性 语法：<code>选择符&#123;background-repeat:no-repeat/repeat/repeat-x/repeat-y &#125;</code></p>
<p>4.背景图的固定 语法：选择符<code>&#123;background-attachment:scroll(滚动)/fixed(固定);&#125;</code></p>
<p>5.背景图片的位置 语法：选择符<code>&#123;background-position:left/center/right/数值     top/center/bottom/数值;&#125;</code></p>
<p>两个值 ：第一个值表示水平位置的值，第二个值：表示垂直的位置。
当两个值都是 center 的时候写一个值就可以代表的是水平位置和垂直位置。
说明：向右方向，向下方向是负值</p>
<ol start="6">
<li>背景属性缩写：<code>background:属性值1   属性值2   属性值3；background:url（背景图片的路径及全称） no-repeat center top；</code></li>
</ol>
<p><code>background</code> 的值的顺序是<code>background-color，background-image，background-repeat，background-attachment，background-position</code></p>
<p>背景还有一个很重要的应用场景就是：雪碧图</p>
<p><code>background-position</code>属性使用频率非常高，大量的网站为了减少 http 请求数，会将大量的图片图片合成一张雪碧图（Sprite）来使用。雪碧图的使用就是通过控制<code>background-position </code>属性值来确定图片呈现的位置，不得不说它的作用非常重要，当然除了在使用雪碧图的场景外，别的某些场景也常常会使用到这个属性。</p>
<h2 data-id="heading-8">CSS3新增内容</h2>
<ol>
<li>属性选择器：语法 <code>[att*=val]</code> 属性值包含 val 例：[class*=“div” ]`  意思是 class 属性包含 div 字符</li>
</ol>
<p>语法 <code>[att^=val] </code>属性值以 val 开始 例：<code>[class^=“div” ]  </code>意思是 class 属性以 div 开头
语法 <code>[att$=val]</code> 属性值以 val 结尾 例：<code>[class$=“div” ] </code> 意思是 class 属性以 div 结束</p>
<ol start="2">
<li>伪类选择器：</li>
</ol>
<ul>
<li>找到第一个 <code>li:first-child&#123;  &#125;</code></li>
<li>找到最后一个<code> li:last-child&#123;  &#125;</code></li>
<li>找到同级下的第 n 个<code> li:nth-child(n)&#123;  &#125;</code></li>
<li>反向找到第 n 个 <code>li:nth-last-child&#123;  &#125;</code></li>
<li>找到偶数<code> li:nth-child(even)&#123;  &#125;</code></li>
<li>找到奇数 <code>li:nth-child(odd)&#123;  &#125;</code></li>
</ul>
<ol start="3">
<li>伪元素选择器：</li>
</ol>
<ul>
<li>像选择元素的第一行文字使用样式 <code>p:first-line &#123;   &#125;</code></li>
<li>像选择元素的第一个字符使用样式 <code>p:first-letter &#123;   &#125;</code></li>
<li>在选择元素的之前添加新元素 <code>p:before&#123;   &#125;</code></li>
<li>在选择元素的之后添加新元素 <code>p:after&#123;   &#125;</code></li>
</ul>
<p>总结一下：以上是一些基础的简单的 CSS 样式和我们 CSS 选择器，有了这些选择器可以帮助我们更好的去找到页面上的元素，通过这些我们可以简单的去还原一些小的效果，怎么样是不是感觉好复杂，人生就是这样起起落落落落落落落落落落...别担心，反正我也帮不了你</p></div>  
</div>
            