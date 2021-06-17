
---
title: '3分钟实现霓虹灯绘画板效果 html+css+js'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a24a5c48c4c74b5f8ae81d6816d1d11f~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 15 Jun 2021 18:26:28 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a24a5c48c4c74b5f8ae81d6816d1d11f~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第15天</p>
<h2 data-id="heading-0">效果：</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a24a5c48c4c74b5f8ae81d6816d1d11f~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">实现：</h2>
<p><strong>1. 定义标签，.main是底层盒子，.txt是文字，.dot是图中的小圆圈，用js动态大量添加。</strong></p>
<pre><code class="hljs language-html copyable" lang="html"> <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"main"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"txt"</span>></span>北极光之夜<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"dot"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"--color: red;"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>      
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://blog.csdn.net/luo1831251387/article/details/113749113" target="_blank" rel="nofollow noopener noreferrer">style="- -color: red;" 这个是var函数的应用，点击链接文章的开头讲有。</a>
<strong>2. 底层盒子的基本样式：</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.main</span>&#123;
          <span class="hljs-attribute">position</span>: fixed;
          <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
          <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
          <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>; 
          <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
          <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">rgb</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
          <span class="hljs-attribute">display</span>: flex;
          <span class="hljs-attribute">justify-content</span>: space-around;
          <span class="hljs-attribute">flex-wrap</span>: wrap;
          <span class="hljs-attribute">align-content</span>: space-around;
          <span class="hljs-attribute">cursor</span>: pointer;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>position: fixed;
top: 0;
left: 0;
width: 100%;
height: 100%; 相对于浏览器窗口进行定位，然后跟窗口一样大。
display: flex; flex布局；
justify-content: space-around; 主轴子元素平分剩余空间排列。
flex-wrap: wrap; 定义多行。
align-content: space-around; 侧轴子元素平分剩余空间排列。
cursor: pointer; 鼠标样式为小手。</p>
<p><strong>3. 小圆圈的基本样式：</strong></p>
<pre><code class="hljs language-css copyable" lang="css"> <span class="hljs-selector-class">.dot</span>&#123;
            <span class="hljs-attribute">position</span>: relative;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">20px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">20px</span>;
           
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>position: relative; 相对定位。</p>
<p><strong>4. 用双伪类显示小圆圈：</strong></p>
<pre><code class="hljs language-css copyable" lang="css"> <span class="hljs-selector-class">.dot</span><span class="hljs-selector-pseudo">::before</span>&#123;
            <span class="hljs-attribute">content</span>: <span class="hljs-string">''</span>;
            <span class="hljs-attribute">position</span>: absolute;
            <span class="hljs-attribute">top</span>: <span class="hljs-number">1px</span>;
            <span class="hljs-attribute">left</span>: <span class="hljs-number">1px</span>;
            <span class="hljs-attribute">bottom</span>: <span class="hljs-number">1px</span>;
            <span class="hljs-attribute">right</span>: <span class="hljs-number">1px</span>;
            <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">rgba</span>(<span class="hljs-number">65</span>, <span class="hljs-number">64</span>, <span class="hljs-number">64</span>,.<span class="hljs-number">5</span>);       
            <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
            <span class="hljs-attribute">transition</span>: all <span class="hljs-number">120s</span> ease-out;            
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>position: absolute; 绝对定位
background-color: rgba(65, 64, 64,.5);  颜色
border-radius: 50%;角弧度
transition: all 120s ease-out; 过渡效果。</p>
<p><strong>5. 鼠标经过圆圈样式变化，颜色变，阴影变：</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.dot</span><span class="hljs-selector-pseudo">:hover</span><span class="hljs-selector-pseudo">::before</span>&#123;
            <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">var</span>(--color);
            <span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">2px</span> <span class="hljs-built_in">var</span>(--color),
            <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">4px</span> <span class="hljs-built_in">var</span>(--color),
            <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">6px</span> <span class="hljs-built_in">var</span>(--color),
             <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">8px</span> <span class="hljs-built_in">var</span>(--color); 
            <span class="hljs-attribute">transition</span>: all <span class="hljs-number">0s</span> ease-out;
        &#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://blog.csdn.net/luo1831251387/article/details/113749113" target="_blank" rel="nofollow noopener noreferrer">var(- -color);中的var函数的应用，点击链接的文章的开头讲有。</a>
box-shadow: 0 0 2px var(--color), 阴影。
transition: all 0s ease-out; 设置过渡效果为0秒。这样只有鼠标离开圆圈的时候才有过渡了。</p>
<p><strong>6. 文本的样式：</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.txt</span>&#123;           
            <span class="hljs-attribute">position</span>: absolute;
            <span class="hljs-attribute">left</span>: <span class="hljs-number">50%</span>;
            <span class="hljs-attribute">top</span>: <span class="hljs-number">50%</span>;           
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(-<span class="hljs-number">50%</span>,-<span class="hljs-number">50%</span>);
            <span class="hljs-attribute">font-family</span>: <span class="hljs-string">'fangsong'</span>;
            <span class="hljs-attribute">font-size</span>: <span class="hljs-number">80px</span>;
            <span class="hljs-attribute">color</span>: <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>,.<span class="hljs-number">6</span>); 
            <span class="hljs-attribute">letter-spacing</span>: <span class="hljs-number">10px</span>;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>position: absolute;
left: 50%;
top: 50%;<br>
transform: translate(-50%,-50%); 居中对齐。
letter-spacing: 10px; 字间距。</p>
<p><strong>7. js 部分，实现动态大量小圆圈铺满浏览器可视区，看注释：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <script>
        <span class="hljs-comment">/* 获取底层盒子main元素 */</span>
        <span class="hljs-keyword">var</span> main = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.main'</span>);
        <span class="hljs-comment">/* 得到main的宽度 */</span>
        <span class="hljs-keyword">let</span> width = main.offsetWidth;
        <span class="hljs-comment">/* 得到main的高度 */</span>
        <span class="hljs-keyword">let</span> height = main.offsetHeight;
         <span class="hljs-comment">/* 建一个颜色数组，放上几种颜色 */</span>
        <span class="hljs-keyword">let</span> color = [<span class="hljs-string">"#BBFF00"</span>,<span class="hljs-string">"#FF3333"</span>,<span class="hljs-string">"#FFFF77"</span>,<span class="hljs-string">"#0044BB"</span>,<span class="hljs-string">"#FF77FF"</span>,<span class="hljs-string">"#99FFFF"</span>,<span class="hljs-string">"#DDDDDD"</span>,<span class="hljs-string">"#FF44AA"</span>];
        <span class="hljs-comment">/*  计算一行需要多少的小圆圈，圆圈是20*20的 */</span>
        <span class="hljs-keyword">let</span> chuang = <span class="hljs-built_in">Math</span>.floor(width / <span class="hljs-number">20</span>);
        <span class="hljs-comment">/*  计算一列需要多少的小圆圈 */</span>
        <span class="hljs-keyword">let</span> kuan = <span class="hljs-built_in">Math</span>.floor(height / <span class="hljs-number">20</span>);
        <span class="hljs-comment">/* 圆圈的总数 */</span>
        <span class="hljs-keyword">let</span> zong = chuang*kuan;
       <span class="hljs-comment">/*   循环添加全部圆圈 */</span>
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">1</span>;i<zong;i++)
        &#123;
            <span class="hljs-comment">/* 创建div盒子 */</span>
            <span class="hljs-keyword">let</span> dot = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'div'</span>);
            <span class="hljs-comment">/* 给新建的盒子添加类名为.dot的选择器 */</span>
             dot.classList.add(<span class="hljs-string">'dot'</span>);
              <span class="hljs-comment">/* 给新建的盒子添加--color的值 */</span>
             dot.style.cssText=<span class="hljs-string">` --color: <span class="hljs-subst">$&#123;color[<span class="hljs-built_in">Math</span>.floor(<span class="hljs-built_in">Math</span>.random() * <span class="hljs-number">8</span>) ]&#125;</span>; `</span>
               <span class="hljs-comment">/* 给底层盒子main添加这个新建的div */</span>
            main.appendChild(dot);
        &#125;
    </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Math.floor()
返回小于或等于一个给定数字的最大整数。</strong>
Math.random() 函数返回一个浮点数,  伪随机数在范围从0到小于1，也就是说，从0（包括0）往上，但是不包括1（排除1），然后您可以缩放到所需的范围。实现将初始种子选择到随机数生成算法;它不能被用户选择或重置。
<strong>而Math.floor(Math.random() * (max - min + 1)) + min;
得到一个两数之间（min和max之间）的随机整数，包括两个数在内。</strong>
<a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Math/random" target="_blank" rel="nofollow noopener noreferrer">Math.random() 函数</a></p>
<h2 data-id="heading-2">完整代码：</h2>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"zh-CN"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"zh-CN"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        *&#123;
            <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
            <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
           
        &#125;
        <span class="hljs-selector-class">.main</span>&#123;
          <span class="hljs-attribute">position</span>: fixed;
          <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
          <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
          <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>; 
          <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
          <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">rgb</span>(<span class="hljs-number">0</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>);
          <span class="hljs-attribute">display</span>: flex;
          <span class="hljs-attribute">justify-content</span>: space-around;
          <span class="hljs-attribute">flex-wrap</span>: wrap;
          <span class="hljs-attribute">align-content</span>: space-around;
          <span class="hljs-attribute">cursor</span>: pointer;
        &#125;
        <span class="hljs-selector-class">.dot</span>&#123;
            <span class="hljs-attribute">position</span>: relative;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">20px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">20px</span>;
           
        &#125;
        <span class="hljs-selector-class">.dot</span><span class="hljs-selector-pseudo">::before</span>&#123;
            <span class="hljs-attribute">content</span>: <span class="hljs-string">''</span>;
            <span class="hljs-attribute">position</span>: absolute;
            <span class="hljs-attribute">top</span>: <span class="hljs-number">1px</span>;
            <span class="hljs-attribute">left</span>: <span class="hljs-number">1px</span>;
            <span class="hljs-attribute">bottom</span>: <span class="hljs-number">1px</span>;
            <span class="hljs-attribute">right</span>: <span class="hljs-number">1px</span>;
            <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">rgba</span>(<span class="hljs-number">65</span>, <span class="hljs-number">64</span>, <span class="hljs-number">64</span>,.<span class="hljs-number">5</span>);       
            <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
            <span class="hljs-attribute">transition</span>: all <span class="hljs-number">120s</span> ease-out;
            
        &#125;
        <span class="hljs-selector-class">.dot</span><span class="hljs-selector-pseudo">:hover</span><span class="hljs-selector-pseudo">::before</span>&#123;
            <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">var</span>(--color);
            <span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">2px</span> <span class="hljs-built_in">var</span>(--color),
            <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">4px</span> <span class="hljs-built_in">var</span>(--color),
            <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">6px</span> <span class="hljs-built_in">var</span>(--color),
             <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">8px</span> <span class="hljs-built_in">var</span>(--color); 
            <span class="hljs-attribute">transition</span>: all <span class="hljs-number">0s</span> ease-out;
        &#125; 
        <span class="hljs-selector-class">.txt</span>&#123;           
            <span class="hljs-attribute">position</span>: absolute;
            <span class="hljs-attribute">left</span>: <span class="hljs-number">50%</span>;
            <span class="hljs-attribute">top</span>: <span class="hljs-number">50%</span>;           
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(-<span class="hljs-number">50%</span>,-<span class="hljs-number">50%</span>);
            <span class="hljs-attribute">font-family</span>: <span class="hljs-string">'fangsong'</span>;
            <span class="hljs-attribute">font-size</span>: <span class="hljs-number">80px</span>;
            <span class="hljs-attribute">color</span>: <span class="hljs-built_in">rgba</span>(<span class="hljs-number">255</span>, <span class="hljs-number">255</span>, <span class="hljs-number">255</span>,.<span class="hljs-number">6</span>); 
            <span class="hljs-attribute">letter-spacing</span>: <span class="hljs-number">10px</span>;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
   <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"main"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"txt"</span>></span>北极光之夜<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"dot"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"--color: red;"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>      
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">

        <span class="hljs-comment">/* 获取底层盒子main元素 */</span>
        <span class="hljs-keyword">var</span> main = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.main'</span>);
        <span class="hljs-comment">/* 得到main的宽度 */</span>
        <span class="hljs-keyword">let</span> width = main.offsetWidth;
        <span class="hljs-comment">/* 得到main的高度 */</span>
        <span class="hljs-keyword">let</span> height = main.offsetHeight;
         <span class="hljs-comment">/* 建一个颜色数组，放上几种颜色 */</span>
        <span class="hljs-keyword">let</span> color = [<span class="hljs-string">"#BBFF00"</span>,<span class="hljs-string">"#FF3333"</span>,<span class="hljs-string">"#FFFF77"</span>,<span class="hljs-string">"#0044BB"</span>,<span class="hljs-string">"#FF77FF"</span>,<span class="hljs-string">"#99FFFF"</span>,<span class="hljs-string">"#DDDDDD"</span>,<span class="hljs-string">"#FF44AA"</span>];
        <span class="hljs-comment">/*  计算一行需要多少的小圆圈，圆圈是20*20的 */</span>
        <span class="hljs-keyword">let</span> chuang = <span class="hljs-built_in">Math</span>.floor(width / <span class="hljs-number">20</span>);
        <span class="hljs-comment">/*  计算一列需要多少的小圆圈 */</span>
        <span class="hljs-keyword">let</span> kuan = <span class="hljs-built_in">Math</span>.floor(height / <span class="hljs-number">20</span>);
        <span class="hljs-comment">/* 圆圈的总数 */</span>
        <span class="hljs-keyword">let</span> zong = chuang*kuan;
       <span class="hljs-comment">/*   循环添加全部圆圈 */</span>
        <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i=<span class="hljs-number">1</span>;i<zong;i++)
        &#123;
            <span class="hljs-comment">/* 创建div盒子 */</span>
            <span class="hljs-keyword">let</span> dot = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'div'</span>);
            <span class="hljs-comment">/* 给新建的盒子添加类名为.dot的选择器 */</span>
             dot.classList.add(<span class="hljs-string">'dot'</span>);
              <span class="hljs-comment">/* 给新建的盒子添加一个随机颜色 */</span>
             dot.style.cssText=<span class="hljs-string">` --color: <span class="hljs-subst">$&#123;color[<span class="hljs-built_in">Math</span>.floor(<span class="hljs-built_in">Math</span>.random() * <span class="hljs-number">8</span>) ]&#125;</span>; `</span>
               <span class="hljs-comment">/* 给底层盒子main添加这个新建的div */</span>
            main.appendChild(dot);
        &#125;


    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">总结：</h2>
<p>天空是蔚蓝色，窗外有千纸鹤~
敲代码听《MOM》这首歌贼有感觉~</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d25a8d52d5d34c4e89aca8c4ac26a818~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>其它文章：</strong>
<a href="https://blog.csdn.net/luo1831251387/article/details/113838748" target="_blank" rel="nofollow noopener noreferrer">炫彩流光文字 html+css</a>
<a href="https://blog.csdn.net/luo1831251387/article/details/113657124" target="_blank" rel="nofollow noopener noreferrer">气泡浮动背景特效 html+css</a>
<a href="https://blog.csdn.net/luo1831251387/article/details/113436552" target="_blank" rel="nofollow noopener noreferrer">简约时钟特效 html+css+js</a>
<a href="https://blog.csdn.net/luo1831251387/article/details/113360844" target="_blank" rel="nofollow noopener noreferrer">赛博朋克风格按钮 html+css</a>
<a href="https://blog.csdn.net/luo1831251387/article/details/112974745" target="_blank" rel="nofollow noopener noreferrer">响应式卡片悬停效果 html+css</a>
<a href="https://blog.csdn.net/luo1831251387/article/details/111714413" target="_blank" rel="nofollow noopener noreferrer">水波加载动画 html+css</a>
<a href="https://blog.csdn.net/luo1831251387/article/details/111601962" target="_blank" rel="nofollow noopener noreferrer">导航栏滚动渐变效果 html+css+js</a>
<a href="https://blog.csdn.net/luo1831251387/article/details/111398881?spm=1001.2014.3001.5502" target="_blank" rel="nofollow noopener noreferrer">书本翻页 html+css</a>
<a href="https://blog.csdn.net/luo1831251387/article/details/111032274?spm=1001.2014.3001.5502" target="_blank" rel="nofollow noopener noreferrer">3D立体相册 html+css</a>
<a href="https://blog.csdn.net/luo1831251387/article/details/111162570?spm=1001.2014.3001.5502" target="_blank" rel="nofollow noopener noreferrer">炫彩流光按钮 html+css</a>
<a href="https://blog.csdn.net/luo1831251387/article/details/111320280" target="_blank" rel="nofollow noopener noreferrer">记一些css属性总结（一）</a>
<a href="https://blog.csdn.net/luo1831251387/article/details/113179630" target="_blank" rel="nofollow noopener noreferrer">Sass总结笔记 </a>
......等</p></div>  
</div>
            