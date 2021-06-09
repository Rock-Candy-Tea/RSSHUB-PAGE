
---
title: '基础的HTML5+CSS3 知识'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6201'
author: 掘金
comments: false
date: Wed, 09 Jun 2021 01:09:43 GMT
thumbnail: 'https://picsum.photos/400/300?random=6201'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1. HTML5</h1>
<h3 data-id="heading-1">meta标签</h3>
<pre><code class="hljs language-html copyable" lang="html"> <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"keywords"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"HTML5,前端,CSS3"</span>></span>
 <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"description"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"这是一个非常不错的网站"</span>></span>
  
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">语义化标签</h3>
<pre><code class="copyable"><!-- 
  标题标签:
 <h1>一级标题</h1>
 <h2>二级标题</h2>
 <h3>三级标题</h3>
 <h4>四级标题</h4>
 <h5>五级标题</h5>
 <h6>六级标题</h6>
 -->
<!-- 
    块元素（block element）
        - 在网页中一般通过块元素来对页面进行布局
    行内元素（inline element）
        - 行内元素主要用来包裹文字 <p></p>
 -->
 <!-- 
    布局标签（结构化语义标签）：

    header 表示网页的头部
    main 表示网页的主体部分(一个页面中只会有一个main)
    footer 表示网页的底部
    nav 表示网页中的导航
    aside 和主体相关的其他内容（侧边栏）
    article 表示一个独立的文章
    section 表示一个独立的区块，上边的标签都不能表示时使用section

    div 没有语义，就用来表示一个区块，目前来讲div还是我们主要的布局元素
    span 行内元素，没有任何的语义，一般用于在网页中选中文字

  -->
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">三种html列表</h3>
<pre><code class="copyable">    1、有序列表 
    2、无序列表
    3、定义列表
    
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"> <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span>结构<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span>表现<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span>行为<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">ol</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span>结构<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span>表现<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">li</span>></span>行为<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">ol</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">dl</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">dt</span>></span>结构<span class="hljs-tag"></<span class="hljs-name">dt</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">dd</span>></span>结构表示网页的结构，结构用来规定网页中哪里是标题，哪里是段落<span class="hljs-tag"></<span class="hljs-name">dd</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">dl</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">超链接、图片、内联框架、音视频</h3>
<pre><code class="hljs language-html copyable" lang="html">     <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"https://www.baidu.com"</span>></span>超链接<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
     <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./img/1.gif"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"松鼠"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">iframe</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"https://www.qq.com"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"800"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"600"</span> <span class="hljs-attr">frameborder</span>=<span class="hljs-string">"0"</span>></span><span class="hljs-tag"></<span class="hljs-name">iframe</span>></span>
<span class="hljs-comment"><!-- 除了通过src来指定外部文件的路径以外，还可以通过source来指定文件的路径 --></span>
    <span class="hljs-tag"><<span class="hljs-name">audio</span> <span class="hljs-attr">controls</span>></span>
        <span class="hljs-comment"><!-- 对不起，您的浏览器不支持播放音频！请升级浏览器！ --></span>
        <span class="hljs-tag"><<span class="hljs-name">source</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./source/audio.mp3"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">source</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./source/audio.ogg"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">embed</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./source/audio.mp3"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"audio/mp3"</span> <span class="hljs-attr">width</span>=<span class="hljs-string">"300"</span> <span class="hljs-attr">height</span>=<span class="hljs-string">"100"</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">audio</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">实体（转义字符）</h3>
<pre><code class="copyable">    &nbsp；   空格
    &gt ；  >
    &lt ；  <
    &copy ；  版权符号
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-6">2.  CSS3</h1>
<pre><code class="copyable">使用CSS来修改元素的样式（3种方法）：
1.内联样式（ 注意：开发时绝对不要使用内联样式） 
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"> <<span class="hljs-selector-tag">p</span> style="<span class="hljs-attribute">color</span>:red; <span class="hljs-attribute">font-size</span>: <span class="hljs-number">60px</span>;">少小离家老大回，乡音无改鬓毛衰</<span class="hljs-selector-tag">p</span>>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">2.内部样式表
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><style>
    <span class="hljs-selector-tag">p</span>&#123;
      <span class="hljs-attribute">color</span>: blue;
      <span class="hljs-attribute">font-size</span>: <span class="hljs-number">20px</span>;
    &#125;
  </style>
  <<span class="hljs-selector-tag">body</span>>
  <<span class="hljs-selector-tag">p</span>> 会当临绝顶，一览众山小</<span class="hljs-selector-tag">p</span>>
</<span class="hljs-selector-tag">body</span>>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">3.外部样式表（最佳实践）
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html">  <span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"./style.css"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">选择器</h2>
<h3 data-id="heading-8">复合选择器</h3>
<pre><code class="copyable">交集选择器：选择器1选择器2选择器3选择器n&#123;&#125; #b1.p1h1.red&#123;&#125;
并集选择器：选择器1,选择器2,选择器3,选择器n&#123;&#125; #b1,.p1,h1,span,div.red&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">关系选择器</h3>
<pre><code class="copyable">子元素选择器 ：父元素 > 子元素&#123;&#125;
后代元素选择器：祖先 后代&#123;&#125;
选择下一个兄弟：前一个 + 下一个&#123;&#125;
选择下边所有的兄弟：兄 ~ 弟&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">伪类选择器 a伪类</h3>
<pre><code class="copyable">  :first-child 第一个子元素
  :last-child 最后一个子元素
  :nth-child() 选中第n个子元素
  :nth-child(even)&#123;&#125; 选中偶数子元素
  :nth-child(odd)&#123;&#125;选中奇数子元素
  :not() 否定伪类
  
  a:link&#123;&#125; 
  a:visited&#123;&#125; 
  a:hover&#123;&#125;
  a:active&#123;&#125; 点击
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">伪元素，表示页面中一些特殊的并不真实的存在的元素（特殊的位置）</h3>
<pre><code class="copyable">  伪元素使用 
      ::before 元素的开始 
      ::after 元素的最后
 - before 和 after 必须结合content属性来使用   
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css">        <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">::before</span>&#123;
            <span class="hljs-attribute">content</span>: <span class="hljs-string">'abc'</span>;
            <span class="hljs-attribute">color</span>: red;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-12">选择器的权重</h3>
<pre><code class="copyable">            内联样式        1,0,0,0  
            id选择器        0,1,0,0  |#id名&#123;&#125;
            类和伪类选择器   0,0,1,0   |.class&#123;&#125;
            元素选择器       0,0,0,1  | p&#123;&#125; h1&#123;&#125;
            通配选择器       0,0,0,0  |*&#123;&#125;
            继承的样式       没有优先级
可以在某一个样式的后边添加 !important ，则此时该样式会获取到最高的优先级，甚至超过内联样式，注意：在开发中这个玩意一定要慎用！

class 是一个标签的属性，它和id类似，不同的是class可以重复使用
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">长度单位</h3>
<pre><code class="copyable">    像素
        - 屏幕（显示器）实际上是由一个一个的小点点构成的
        - 不同屏幕的像素大小是不同的，像素越小的屏幕显示的效果越清晰
        - 所以同样的200px在不同的设备下显示效果不一样

    百分比
        - 也可以将属性值设置为相对于其父元素属性的百分比
        - 设置百分比可以使子元素跟随父元素的改变而改变

    em
        - em是相对于元素的字体大小来计算的
        - 1em = 1font-size
        - em会根据字体大小的改变而改变

    rem
        - rem是相对于根元素的字体大小来计算
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            