
---
title: '2021前端知识点之CSS、HTML5篇'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8794'
author: 掘金
comments: false
date: Sun, 11 Apr 2021 19:01:35 GMT
thumbnail: 'https://picsum.photos/400/300?random=8794'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">目录</h2>
<ol>
<li>
<p>两栏布局，右侧自适应，三栏布局，中间自适应</p>
</li>
<li>
<p>HTML5</p>
</li>
</ol>
<p>1.两栏布局，右侧自适应，三栏布局，中间自适应</p>
<pre><code class="copyable">   1.两栏布局，有边自适应
     (1)BFC里float，margin-left
     父级添加BFC，即overflow：hidden
     左边float，定宽：float:left;width:200px
     右边margin-left：210px
     (2)flex弹性布局
     父级设置display：flex
     左边定宽：width：200px
     右边：flex：1
   2.三栏布局，中间自适应
     (1)两边float，中间margin：
         父级BFC，设置overflow：hidden，解决高度没有的问题。
         左边左浮动，定宽：float：left，width：200px
         右边右浮动，定宽：float：right，width：100px
         中间margin：margin-left：210px；margin-right：110px
        `  <div class="container">
            <div class="left"></div>
            <div class="right"></div>
            <div class="middle"></div>
           </div>           `
     (2)两边absolute，中间margin(脱离文档流:根据最近已经定位的祖先元素定位，不考虑html)
         .left&#123;
             position:absolute;
             left:0;
             top:0;
             width:200px
         &#125;
         .right:&#123;
             position:absolute;
             right:0;
             top:0
             width:100
         &#125;
         .middle&#123;
             margin:0 110px 0 210px;
         &#125;
     (3)display：table；table-layout：flexd
        `  <div class="container">
            <div class="left"></div>
            <div class="middle"></div>
            <div class="right"></div>
           </div>      `
         父级.container&#123;
                 display：table；
                 table-layout：flexd；
                 width:100%；
                 text-align：center
             &#125;
             .left .right&#123;
                 display:table-cell;
                 width:100px
             &#125;
             .middle&#123;
                 width:100%;  //填充剩下的宽度
                 display:teble-cell
             &#125;
     (4)flex实现
         .container&#123;
             display：flex；
             justify-content: space-between  //项目平均分布
         &#125;
         .left .right&#123;
             width:100px
         &#125;
         .middle&#123;
             flex:1;  //填充剩下的宽度，或者用width:100%
         &#125;
     (5)grid实现
         .container&#123;
             display：grid；
             grid-template-columns: 300px auto 300px;
         &#125;
         
         
         
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.HTML5</p>
<pre><code class="copyable">   1.语义化标签：
       head、footer、nav、aside、section、article、dialog、main、figure
   2.表单：
      类型：input增加了type = color、email、range、number、date、datetime、month、search、url、tel。由于浏览器兼容问题，很多都不适用，一般用ElementUI封装好的
      属性：placeholder、maxlength、minlength、require、autofocus、autocomplete
   3.多媒体标签：audio、vedio  通过src
   4.canvas
   5.SVG绘图：xml的2D图形语言，矢量图标 <svg>标签 ，和canvas有点像
   6.地理定位：Geolocation
   7.拖放API：drag、drop
   8.webWorker
   9.webStorage:sessionStorage/localStorage:getItem/setItem/removeItem/clear/
   10.webSocket
   
      29.BFC

   1.BFC(Block Formatting Context)，即块级格式化上下文，是页面中的一块渲染区域。
   2.BFC的目的是形成一个相对于外界完全独立的空间，让内部的子元素不会影响到外部的元素。
   3.BFC有一套属于自己的渲染规则：
       1、内部的盒子会在垂直方向上一个接一个的放置
       2、对于同一个BFC的两个相邻的盒子的margin会发生重叠，与方向无关
       3、每个元素的左外边距与包含块的左边界相接触（从左到右），即使浮动元素也是如此，但是BFC的区域不会与float的元素区域重叠
       4、计算BFC的高度时，浮动子元素也参与计算
       5、BFC就是页面上的一个隔离的独立容器，容器里面的子元素不会影响到外面的元素，反之亦然。
   4.BFC的触发条件，包含不限于：
       1、根元素，即html元素
       2、浮动元素：float值为left、right
       3、overflow值不为visible，为auto、hidden、scroll
       4、display值为表格布局或弹性布局，如inline-block、table-cell、table-caption、table、inline-table、flex、inline-flex、grid、inline-grid
       5、绝对定位，position值为absolute、flxed
   
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">    (<span class="hljs-number">1</span>)解决元素间距问题：防止margin重叠(塌陷)，同一个BFC会引发margin重叠
    <style>
        p&#123;<span class="hljs-attr">background</span>:#fcc;width:200px;line-heigth:100px;margin:100px;text-algin:center&#125;
        .wrap&#123;overflow：hidden&#125;  <span class="hljs-comment">//根据触发规则3，形成新的BFC</span>
    </style>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>haha<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>hehe<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">body</span>></span></span>
    根据触发规则<span class="hljs-number">1</span>，根元素触发BFC，两个p元素的margin重叠，以最大的margin为准，根据渲染规则<span class="hljs-number">1</span>和<span class="hljs-number">2</span>，由于同一个BFC两个相邻的盒子的margin会发生重叠，所以解决方案是将p再裹一层容器，形成两个独立的BFC即可。
    <div <span class="hljs-class"><span class="hljs-keyword">class</span></span>=<span class="hljs-string">"wrap"</span>>
       <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>hehe<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
    </div>
    
    
    (<span class="hljs-number">2</span>)解决元素高度没了的问题：父级形成BFC可清除内部浮动，BFC内部有浮动元素时，可让它参与高度计算
    <style>
        .par&#123;<span class="hljs-attr">border</span>:5px solid #fcc;width:300px&#125;
        .child&#123;<span class="hljs-attr">border</span>:5px;width:100px;height:100px;float:left&#125;
    </style>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"par"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">child</span>"></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">child</span>"></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">body</span>></span></span>
    计算par高度时，高度为<span class="hljs-number">0</span>，没了，是因为子元素没有参与计算。
    解决：让par形成BFC，根据BFC渲染规则<span class="hljs-number">5</span>，浮动元素也会参与计算。
    解决方案：.par&#123;<span class="hljs-attr">overflow</span>:hidden&#125;  <span class="hljs-comment">//根据触发规则3，形成BFC</span>
    
    
    
    (<span class="hljs-number">3</span>)解决多栏布局不能自适应问题：自适应多栏布局
    <style>
        body&#123;<span class="hljs-attr">width</span>:300px;position:relative&#125;
        .aside&#123;<span class="hljs-attr">width</span>:100px;height:100px;float:left;background:#f66;&#125;
        .main&#123;<span class="hljs-attr">height</span>:200px;background:#fcc;&#125;
    </style>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">aside</span>"></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">main</span>"></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">body</span>></span></span>
    由于每个元素的左边距与包含块的左边界相接触，所以即使aside为浮动元素，main的左边依然会与包含块的左边相接触
    解决：根据BFC的渲染规则<span class="hljs-number">3</span>，BFC不会与浮动盒子重叠
    解决方案：.main&#123;<span class="hljs-attr">overflow</span>: hidden&#125; <span class="hljs-comment">//根据BFC触发规则3，形成BFC</span>
    
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">扩展：
IFC、GFC、FFC
IFC、GFC、FFC实际上都是BFC的细化。
1.IFC(Inline formatting contexts):内联格式上下文
    内联盒子的高度由其包含行内元素中最高的实际高度计算而来。
    触发：display:inline-block，根据BFC触发规则4
    作用：水平居中、垂直居中
2.GFC(GrideLayout formatting contexts):网格布局格式化上下文
    形成一个二维表格，拥有丰富的属性，控制行列、对齐
    触发：display：grid
    作用：二维表格渲染
3.FFC(Flex formatting contexts):自适应格式上下文
    形成一个伸缩容器
    触发：display：flex/inline-flex
    只有谷歌、火狐支持
    
    
<span class="copy-code-btn">复制代码</span></code></pre>
<p>30.实现元素的垂直水平居中</p>
<pre><code class="copyable">   1、利用定位 + margin：auto（脱离文档流）
       (1)父级设置为相对定位position：relative，子级绝对定位posittion：absolute
       (2)子级四个定位属性left、right、top、bottom都设置为0
       (3)子级设置margin：auto
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js">     <style>
        .father&#123;<span class="hljs-attr">width</span>:500px;height:300px;position:relative&#125;
        .son&#123;<span class="hljs-attr">width</span>:100px;height:40px;left:<span class="hljs-number">0</span>;top:<span class="hljs-number">0</span>;right:<span class="hljs-number">0</span>;bottom:<span class="hljs-number">0</span>;margin:auto;background:#f66;&#125;
    </style>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"father"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"son"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">body</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">   2、利用定位 + margin：负值（父元素高度变化仍然可实现，但是子元素宽高必须已知）
       (1)父级设置为相对定位position：relative，子级绝对定位posittion：absolute
       (2)子级四个定位属性left、top都设置为50%
       (3)子级设置margin-left:-(子级宽度的50%)，margin-top：-(子级高度的50%)
       
   3、利用定位 + transform （优点：父元素高度和子元素的宽高都不需要知道）transform：translate(x,y)，x和y表示的是x轴和y轴的值，起点是左上角，scale(n) 放大缩小比例，比如2.0和负值
       (1)父级设置为相对定位position：relative，子级绝对定位posittion：absolute
       (2)子级四个定位属性left、top都设置为50%
       (3)子级设置transform：translate(-50%,-50%) 
       
   4、table布局（未脱离文档流） table-cell
       其实是BFC/IFC内联格式化上下文的原理
       (1)父级设置display:table-cell，子级设置display：inline-block
       (2)父级设置vertical-align:middle，text-align:center
   5、flex布局（不定高，不定宽，常用）
       CSS3中的flex布局
       (1)父级设置display:flex
       (2)父级设置align-items：center,水平居中
       (1)父级设置justify-content: center，垂直居中
   6、grid布局（不定高、不定宽，兼容性相对较差）
       CSS3中的grid布局
       (1)父级设置display:grid
       (2)父级设置align-items：center,水平居中
       (1)父级设置justify-content: center，垂直居中
   
<span class="copy-code-btn">复制代码</span></code></pre>
<p>31.隐藏页面元素的方式</p>
<pre><code class="copyable">   1.display：none
       元素在页面彻底消失，元素本身占有的空间会被其他元素占有，导致浏览器的重排和重绘，自身绑定的事件不会触发，也不会有过渡效果。
       特点：元素不可见，不占据空间，无法响应点击事件
   2.visibility:hidden
       DOM结构存在，不会触发重排，但会触发重绘，绑定事件不触发
       特点：元素不可见，占据页面空间，无法响应点击事件
   3.opacity:0
       设置元素透明度为0后是不可见的，DOM结构存在，不引发重绘、重排
       特点：改变元素透明度，元素不可见，占据页面空间，可响应点击事件
   4.设置height和width模型属性为0
       将元素的margin、padding、border、width、height等属性设置为0，若元素内有子元素，则设置overflow：hidden。
       特点：元素不可见，不占据空间，无法响应点击事件，DOM不存在
   5.position：absolute
       将元素移出可视区域
       `.hide&#123;position:absolute;top:-9999px;left:-9999px&#125;           `
       特点：元素不可见，不影响页面布局
   6.clip-path
       通过裁剪的形式
       ` .hide&#123;clip-path:polygon(0px 0px 0px 0px 0px 0px 0px 0px)&#125;          `
       特点：元素不可见，占据页面空间，无法响应点击事件
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="32">
<li>
<p>em/px/rem/vh/vw的区别</p>
<pre><code class="copyable">1、px 绝对长度单位，页面按精确像素展示
2、em 相对长度单位，继承父级元素的字体大小font-size，若父级元素未设置，则用浏览器默认的字体尺寸16px，即1em=16px，整个页面的1em值不是一个固定的值
3、rem 相对长度单位，相对的只是HTML根元素font-size的值，一般在根元素html上加上html&#123;font-size:62.5%&#125;，之后1rem = 10px。rem集相对大小和绝地大小的优点于一身，故常用。
4、vw 根据窗口的宽度分成100等份，100vw就标识满宽，始终针对窗口的宽，vh针对窗口的高。窗口在PC端指浏览器的可视区域，在移动端指布局视口。%相对于的是父元素，不是窗口。
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p>33.CSS选择器</p>
<pre><code class="copyable"> 1.css选择器常用的有：
   1、id选择器
   2、类选择器
   3、标签选择器
   4、后代选择器(#id div)、
   5、子选择器(.class>.childClass)、
   6、相邻同胞选择器(.class+.brotherClass)、
   7、群组选择器(div,p)
   8、伪类选择器(:hover/:focus/:link/:active/:visited/:first-child)  CSS3
   9、伪元素选择器(:before/:after/:first-letter/:first-line)
   10、属性选择器(attribute) CSS3
   11、层次选择器(p~ul) CSS3
   
 2.选择器的优先级：
   
   !important > 内联 > ID选择器 > 类选择器 > 标签选择器 > * > 继承 > 默认
 
 3.选择器具有继承属性
 4.CSS选择器**解析顺序是从右往左**解析
 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>34.层叠上下文（stacking context）</p>
<pre><code class="copyable">  1.盒模型是三维的，平面画布的x轴、y轴，以及表示层叠的z轴，
  2.触发条件：
      (1)根元素 <html>本身即根层叠上下文
      (2)position属性，非static值，并设置z-index
      (3)CSS属性：flex(子元素z-index不为auto)、opacity(不为1)、transform(值不为none)、filter(值不为none)、will-change
  3.层叠顺序规则：
      (1)在同一层叠上下文中层叠等级才有意义
      (2)z-index的优先级最高
      (3)具体规则：background < (z-index<0)  <  block块级元素 < float浮动元素 < inline行内元素 < z-index=0/auto < (z-index>0)
      
<span class="copy-code-btn">复制代码</span></code></pre>
<p>35.CSS盒模型</p>
<pre><code class="copyable">   1.一般说IE8及其以上为W3C盒模型，IE8以下是IE怪异盒模型，不是所有的IE都是IE盒模型
   2.页面渲染时，DOM元素所采用的布局模型，可通过box-sizing进行设置，根据width的区别可分为
       (1)标准盒模型box-sizing：content-box。width指content部分的宽度
       (2)IE盒模型 box-sizing：border-box。width = content + padding + border
    
   3.css盒子包含四部分：内容content、内边距padding、边框border、外边距margin
   4.在w3c标准盒模型里，一个块block的总宽度= width + padding + border + margin
   5.在IE盒模型里，一个块block的总宽度 = width + margin
<span class="copy-code-btn">复制代码</span></code></pre>
<p>36.CSS的新属性</p>
<pre><code class="copyable">   1、布局：新增flex、grid
   2、选择器：新增first-of-type、nth-child
   3、盒模型：新增box-sizing，以选择IE的border-box和W3c的content-box
   4、动画：新增animation，2d变换，3d变换
   5、颜色：新增opacity、rbga
   6、字体：嵌入字体、字体阴影
   7、媒体查询@media
<span class="copy-code-btn">复制代码</span></code></pre>
<p>37.CSS预处理器(SASS/LESS/POSTCSS)</p>
<pre><code class="copyable">   常用功能：嵌套、变量、循环语句、条件语句、自动前缀、单位转换、mixin复用
   
<span class="copy-code-btn">复制代码</span></code></pre>
<p>38.清除浮动</p>
<pre><code class="copyable">   (1)clear：both
   (2)创建父级BFC，父级添加display：auto/hidden 属性
   (3)父级设置高度 
   (4)伪元素和IEhack
<span class="copy-code-btn">复制代码</span></code></pre></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            