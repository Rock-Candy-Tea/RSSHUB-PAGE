
---
title: '3D酷炫扭动卡片 html+css+js'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d960948b340b4ae4ba36dcbb7c283bc4~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 29 Apr 2021 18:41:51 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d960948b340b4ae4ba36dcbb7c283bc4~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">看效果，动起来~：</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d960948b340b4ae4ba36dcbb7c283bc4~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">实现：</h2>
<p><strong>1. 定义标签，.card是底层盒子，.card2是呈现卡片效果的盒子，然后里面就是一些图片和文字，字体图标的标签了。：</strong></p>
<pre><code class="hljs language-html copyable" lang="html"> <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"card"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"card2"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"img/haha.gif"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"haha"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>北极光之夜<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"txt"</span>></span>The aurora borealis.<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"font"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span> <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span> <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span> <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2. 定义底层盒子.card的基本样式：</strong></p>
<pre><code class="hljs language-css copyable" lang="css"> <span class="hljs-selector-class">.card</span> &#123;
            <span class="hljs-attribute">position</span>: relative;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">250px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">300px</span>;
            <span class="hljs-attribute">transform-style</span>: preserve-<span class="hljs-number">3</span>d;
            <span class="hljs-attribute">cursor</span>: pointer;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>position: relative; 相对定位。
transform-style: preserve-3d; 其子元素获得3D位置。
cursor: pointer; 鼠标样式变为小手。</p>
<p><strong>3. 定义卡片盒子 .card2 的基本样式：</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.card2</span> &#123;
            <span class="hljs-attribute">position</span>: absolute;
            <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
            <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
            <span class="hljs-attribute">background-color</span>: transparent;
            <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">15px</span>;
            <span class="hljs-attribute">transition</span>: all <span class="hljs-number">0.2s</span>;
            <span class="hljs-attribute">transform-style</span>: preserve-<span class="hljs-number">3</span>d;
            <span class="hljs-attribute">box-shadow</span>: inset <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">30px</span> <span class="hljs-built_in">rgb</span>(<span class="hljs-number">83</span>, <span class="hljs-number">83</span>, <span class="hljs-number">82</span>);
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>position: absolute; 绝对定位。
background-color: transparent; 背景色为透明色。
border-radius: 15px; 边角的弧度。
transiton： all 0.2s；过渡效果。
transform-style：preserve-3d；子元素获得3D位置。
box-shadow： 内阴影。</p>
<p><strong>4. 定义头像图片得基本样式：</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.card2</span> <span class="hljs-selector-tag">img</span> &#123;
            <span class="hljs-attribute">position</span>: absolute;
            <span class="hljs-attribute">top</span>: <span class="hljs-number">30px</span>;
            <span class="hljs-attribute">left</span>: <span class="hljs-number">75px</span>;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
            <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateZ</span>(<span class="hljs-number">50px</span>);
            <span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">10px</span> <span class="hljs-built_in">rgb</span>(<span class="hljs-number">83</span>, <span class="hljs-number">83</span>, <span class="hljs-number">83</span>);
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>position：绝对定位。
transform：translateZ（50px）；图片向 Z 轴移动 50 px ，这样更有层次感和立体效果。
box-shadow: 0 0 10px rgb(83, 83, 83);  阴影。</p>
<p><strong>5. 标题的基本样式：</strong></p>
<pre><code class="hljs language-css copyable" lang="css"> <span class="hljs-selector-class">.card2</span> <span class="hljs-selector-tag">h2</span> &#123;
            <span class="hljs-attribute">font-family</span>: <span class="hljs-string">'Permanent Marker'</span>, cursive;
            <span class="hljs-attribute">position</span>: absolute;
            <span class="hljs-attribute">top</span>: <span class="hljs-number">150px</span>;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">28px</span>;
            <span class="hljs-attribute">font-size</span>: <span class="hljs-number">25px</span>;
            <span class="hljs-attribute">line-height</span>: <span class="hljs-number">28px</span>; 
            <span class="hljs-attribute">text-align</span>: center;
            <span class="hljs-attribute">text-shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">5px</span> <span class="hljs-built_in">rgb</span>(<span class="hljs-number">177</span>, <span class="hljs-number">174</span>, <span class="hljs-number">174</span>);
            <span class="hljs-attribute">color</span>: <span class="hljs-built_in">rgb</span>(<span class="hljs-number">33</span>, <span class="hljs-number">34</span>, <span class="hljs-number">34</span>);
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateZ</span>(<span class="hljs-number">50px</span>);
        &#125;     
<span class="copy-code-btn">复制代码</span></code></pre>
<p>font-family: 字体样式。
font-size：字体大小。
text-align：文本居中对齐。
text-shadow: 文字阴影。
transform: translateZ(50px);文字也向 Z 轴移动 50 px ，更有层次感和立体效果。</p>
<p><strong>6. 小标题基本样式：</strong></p>
<pre><code class="hljs language-css copyable" lang="css"> <span class="hljs-selector-class">.txt</span>&#123;
            <span class="hljs-attribute">font-family</span>: <span class="hljs-string">'Permanent Marker'</span>, cursive;
            <span class="hljs-attribute">position</span>: absolute;
              <span class="hljs-attribute">top</span>: <span class="hljs-number">180px</span>;
              <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
              <span class="hljs-attribute">line-height</span>: <span class="hljs-number">30px</span>;
              <span class="hljs-attribute">font-size</span>: <span class="hljs-number">16px</span>;
              <span class="hljs-attribute">text-align</span>: center;            
              <span class="hljs-attribute">text-shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">10px</span> <span class="hljs-built_in">rgb</span>(<span class="hljs-number">185</span>, <span class="hljs-number">187</span>, <span class="hljs-number">186</span>);
              <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateZ</span>(<span class="hljs-number">50px</span>);
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>font-family: 'Permanent Marker', cursive; 字体样式。<a href="http://www.googlefonts.cn/" target="_blank" rel="nofollow noopener noreferrer">字体样式大全</a>
line-height: 30px; 行间距。
...略...
<strong>7. 字体图标的基本样式，宽，高等：</strong></p>
<pre><code class="hljs language-css copyable" lang="css">  <span class="hljs-selector-class">.font</span>&#123;
          <span class="hljs-attribute">position</span>: absolute;
          <span class="hljs-attribute">top</span>: <span class="hljs-number">215px</span>;
          <span class="hljs-attribute">left</span>: <span class="hljs-number">50%</span>;
          <span class="hljs-attribute">width</span>: <span class="hljs-number">80%</span>;
          <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
          <span class="hljs-attribute">display</span>: flex;
          <span class="hljs-attribute">align-items</span>: center;
          <span class="hljs-attribute">justify-content</span>: space-around;
          <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateZ</span>(<span class="hljs-number">50px</span>) <span class="hljs-built_in">translateX</span>(-<span class="hljs-number">50%</span>);
        &#125;
        <span class="hljs-selector-class">.font</span> <span class="hljs-selector-tag">span</span>&#123;
            <span class="hljs-attribute">display</span>: inline-block;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">50px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
            <span class="hljs-attribute">line-height</span>: <span class="hljs-number">50px</span>;
            <span class="hljs-attribute">text-align</span>: center;
            <span class="hljs-attribute">font-size</span>: <span class="hljs-number">30px</span>;
            <span class="hljs-attribute">color</span>: white;
            <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
            <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">rgb</span>(<span class="hljs-number">61</span>, <span class="hljs-number">60</span>, <span class="hljs-number">60</span>);
            <span class="hljs-attribute">box-shadow</span>: inset <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">8px</span> white,
            inset <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">8px</span> white,
            inset <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">8px</span> white,
            <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">8px</span> black;        
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>display: flex;
align-items: center;
justify-content: space-around; flex布局，主轴平分空间对齐，侧轴居中对齐。
display: inline-block; 转为行内块元素。
box-shadow: 阴影，写多行可以让阴影效果更亮。
.....略...</p>
<p><strong>8. js部分，看注释，公式可以结合注释自己理解下：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><script>
         <span class="hljs-comment">/* 获取底层盒子标签*/</span>
        <span class="hljs-keyword">var</span> card = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.card'</span>);
        <span class="hljs-comment">/*获取卡片标签*/</span>
        <span class="hljs-keyword">var</span> card2 = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.card2'</span>);
        <span class="hljs-comment">/*给底层盒子添加鼠标经过mousemove事件*/</span>
        card.addEventListener(<span class="hljs-string">'mousemove'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
        <span class="hljs-comment">/* x为鼠标距离页面左侧距离减去底层盒子距离页面左侧距离*/</span>
            <span class="hljs-keyword">let</span> x = e.clientX - card.offsetLeft;
        <span class="hljs-comment">/* left为底层盒子宽度的一半*/</span>
            <span class="hljs-keyword">let</span> left = card.offsetWidth / <span class="hljs-number">2</span>;
         <span class="hljs-comment">/* rotateY 为卡片绕Y轴旋转的大小，旋转度看自己，我除以5，也可以大点或小点 */</span>
            <span class="hljs-keyword">let</span> rotateY = -(left - x) / <span class="hljs-number">5</span>;
           <span class="hljs-comment">/* y为鼠标距离页面顶侧距离减去底层盒子距离页面顶侧距离*/</span>
            <span class="hljs-keyword">let</span> y = e.clientY - card.offsetTop;
              <span class="hljs-comment">/* top为底层盒子高度的一半*/</span>
            <span class="hljs-keyword">let</span> top = card.offsetHeight / <span class="hljs-number">2</span>;
         <span class="hljs-comment">/* rotateX 为卡片绕X轴旋转的大小，旋转度看自己，我除以5，也可以大点或小点 */</span>     
            <span class="hljs-keyword">let</span> rotateX = (top - y) / <span class="hljs-number">5</span>;
           <span class="hljs-comment">/*为卡片添加transform属性 */</span>   
            card2.style.cssText = <span class="hljs-string">`
               transform: rotateX(<span class="hljs-subst">$&#123;rotateX&#125;</span>deg) rotateY(<span class="hljs-subst">$&#123;rotateY&#125;</span>deg); `</span>
        &#125;)
    <span class="hljs-comment">/*给底层盒子添加鼠标离开事件mouseout*/</span>
        card.addEventListener(<span class="hljs-string">'mouseout'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
        <span class="hljs-comment">/* 让卡片的transform属性的绕X，Y轴的rotate都是0deg*/</span>
            card2.style.cssText = <span class="hljs-string">`
               transform: rotateY(0deg) rotateX(0deg); `</span>
        &#125;)
    </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">完整代码：</h2>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"zh-CN"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"https://fonts.font.im/css?family=Dancing+Script"</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"https://fonts.font.im/css?family=Permanent+Marker"</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-keyword">@font-face</span> &#123;
            <span class="hljs-attribute">font-family</span>: <span class="hljs-string">'icomoon'</span>;
            <span class="hljs-attribute">src</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">'fonts/icomoon.eot?wr5es'</span>);
            <span class="hljs-attribute">src</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">'fonts/icomoon.eot?wr5es#iefix'</span>) <span class="hljs-built_in">format</span>(<span class="hljs-string">'embedded-opentype'</span>),
                <span class="hljs-built_in">url</span>(<span class="hljs-string">'fonts/icomoon.ttf?wr5es'</span>) <span class="hljs-built_in">format</span>(<span class="hljs-string">'truetype'</span>),
                <span class="hljs-built_in">url</span>(<span class="hljs-string">'fonts/icomoon.woff?wr5es'</span>) <span class="hljs-built_in">format</span>(<span class="hljs-string">'woff'</span>),
                <span class="hljs-built_in">url</span>(<span class="hljs-string">'fonts/icomoon.svg?wr5es#icomoon'</span>) <span class="hljs-built_in">format</span>(<span class="hljs-string">'svg'</span>);
            <span class="hljs-attribute">font-weight</span>: normal;
            <span class="hljs-attribute">font-style</span>: normal;
            <span class="hljs-attribute">font-display</span>: block;
        &#125;

        * &#123;
            <span class="hljs-attribute">font-family</span>: <span class="hljs-string">'icomoon'</span>;
            <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span>;
            <span class="hljs-attribute">padding</span>: <span class="hljs-number">0</span>;
            <span class="hljs-attribute">box-sizing</span>: border-box;
         
          
        &#125;

        <span class="hljs-selector-tag">body</span> &#123;
            <span class="hljs-attribute">min-height</span>: <span class="hljs-number">100vh</span>;
            <span class="hljs-attribute">display</span>: flex;
            <span class="hljs-attribute">justify-content</span>: center;
            <span class="hljs-attribute">align-items</span>: center;
            <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">linear-gradient</span>(<span class="hljs-number">120deg</span>,<span class="hljs-built_in">rgb</span>(<span class="hljs-number">255</span>, <span class="hljs-number">196</span>, <span class="hljs-number">0</span>) <span class="hljs-number">40%</span>,<span class="hljs-built_in">rgb</span>(<span class="hljs-number">31</span>, <span class="hljs-number">223</span>, <span class="hljs-number">175</span>),<span class="hljs-built_in">rgb</span>(<span class="hljs-number">0</span>, <span class="hljs-number">195</span>, <span class="hljs-number">255</span>),<span class="hljs-built_in">rgb</span>(<span class="hljs-number">183</span>, <span class="hljs-number">0</span>, <span class="hljs-number">255</span>) <span class="hljs-number">60%</span>);
        &#125;

        <span class="hljs-selector-class">.card</span> &#123;
            <span class="hljs-attribute">position</span>: relative;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">250px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">300px</span>;
            <span class="hljs-attribute">transform-style</span>: preserve-<span class="hljs-number">3</span>d;
            <span class="hljs-attribute">cursor</span>: pointer;

        &#125;
        <span class="hljs-selector-class">.card2</span> &#123;
            <span class="hljs-attribute">position</span>: absolute;
            <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
            <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">100%</span>;
            <span class="hljs-attribute">background-color</span>: transparent;
            <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">15px</span>;
            <span class="hljs-attribute">transition</span>: all <span class="hljs-number">0.2s</span>;
            <span class="hljs-attribute">transform-style</span>: preserve-<span class="hljs-number">3</span>d;
            <span class="hljs-attribute">box-shadow</span>: inset <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">30px</span> <span class="hljs-built_in">rgb</span>(<span class="hljs-number">83</span>, <span class="hljs-number">83</span>, <span class="hljs-number">82</span>);
        &#125;

        <span class="hljs-selector-class">.card2</span> <span class="hljs-selector-tag">img</span> &#123;
            <span class="hljs-attribute">position</span>: absolute;
            <span class="hljs-attribute">top</span>: <span class="hljs-number">30px</span>;
            <span class="hljs-attribute">left</span>: <span class="hljs-number">75px</span>;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">100px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
            <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateZ</span>(<span class="hljs-number">50px</span>);
            <span class="hljs-attribute">box-shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">10px</span> <span class="hljs-built_in">rgb</span>(<span class="hljs-number">83</span>, <span class="hljs-number">83</span>, <span class="hljs-number">83</span>);
        &#125;
        <span class="hljs-selector-class">.card2</span> <span class="hljs-selector-tag">h2</span> &#123;
            <span class="hljs-attribute">font-family</span>: <span class="hljs-string">'Permanent Marker'</span>, cursive;
            <span class="hljs-attribute">position</span>: absolute;
            <span class="hljs-attribute">top</span>: <span class="hljs-number">150px</span>;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">28px</span>;
            <span class="hljs-attribute">font-size</span>: <span class="hljs-number">25px</span>;
            <span class="hljs-attribute">line-height</span>: <span class="hljs-number">28px</span>; 
            <span class="hljs-attribute">text-align</span>: center;
            <span class="hljs-attribute">text-shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">5px</span> <span class="hljs-built_in">rgb</span>(<span class="hljs-number">177</span>, <span class="hljs-number">174</span>, <span class="hljs-number">174</span>);
            <span class="hljs-attribute">color</span>: <span class="hljs-built_in">rgb</span>(<span class="hljs-number">33</span>, <span class="hljs-number">34</span>, <span class="hljs-number">34</span>);
            <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateZ</span>(<span class="hljs-number">50px</span>);
        &#125;     
        <span class="hljs-selector-class">.txt</span>&#123;
            <span class="hljs-attribute">font-family</span>: <span class="hljs-string">'Permanent Marker'</span>, cursive;
            <span class="hljs-attribute">position</span>: absolute;
              <span class="hljs-attribute">top</span>: <span class="hljs-number">180px</span>;
              <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
              <span class="hljs-attribute">line-height</span>: <span class="hljs-number">30px</span>;
              <span class="hljs-attribute">font-size</span>: <span class="hljs-number">16px</span>;
              <span class="hljs-attribute">text-align</span>: center;            
              <span class="hljs-attribute">text-shadow</span>: <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">10px</span> <span class="hljs-built_in">rgb</span>(<span class="hljs-number">185</span>, <span class="hljs-number">187</span>, <span class="hljs-number">186</span>);
              <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateZ</span>(<span class="hljs-number">50px</span>);
        &#125;
        <span class="hljs-selector-class">.font</span>&#123;
          <span class="hljs-attribute">position</span>: absolute;
          <span class="hljs-attribute">top</span>: <span class="hljs-number">215px</span>;
          <span class="hljs-attribute">left</span>: <span class="hljs-number">50%</span>;
          <span class="hljs-attribute">width</span>: <span class="hljs-number">80%</span>;
          <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
          <span class="hljs-attribute">display</span>: flex;
          <span class="hljs-attribute">align-items</span>: center;
          <span class="hljs-attribute">justify-content</span>: space-around;
          <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translateZ</span>(<span class="hljs-number">50px</span>) <span class="hljs-built_in">translateX</span>(-<span class="hljs-number">50%</span>);
        &#125;
        <span class="hljs-selector-class">.font</span> <span class="hljs-selector-tag">span</span>&#123;
            <span class="hljs-attribute">display</span>: inline-block;
            <span class="hljs-attribute">width</span>: <span class="hljs-number">50px</span>;
            <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
            <span class="hljs-attribute">line-height</span>: <span class="hljs-number">50px</span>;
            <span class="hljs-attribute">text-align</span>: center;
            <span class="hljs-attribute">font-size</span>: <span class="hljs-number">30px</span>;
            <span class="hljs-attribute">color</span>: white;
            <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">50%</span>;
            <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">rgb</span>(<span class="hljs-number">61</span>, <span class="hljs-number">60</span>, <span class="hljs-number">60</span>);
         <span class="hljs-comment">/*    border: 1px solid rgb(173, 172, 172) ; */</span>
            <span class="hljs-attribute">box-shadow</span>: inset <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">8px</span> white,
            inset <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">8px</span> white,
            inset <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">8px</span> white,
            <span class="hljs-number">0</span> <span class="hljs-number">0</span> <span class="hljs-number">8px</span> black;        
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"card"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"card2"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"img/haha.gif"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"haha"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>北极光之夜<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"txt"</span>></span>The aurora borealis.<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"font"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span> <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span> <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">span</span>></span> <span class="hljs-tag"></<span class="hljs-name">span</span>></span>
                <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">

        <span class="hljs-keyword">var</span> card = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.card'</span>);
        <span class="hljs-keyword">var</span> card2 = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.card2'</span>);
        card.addEventListener(<span class="hljs-string">'mousemove'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
            <span class="hljs-keyword">let</span> x = e.clientX - card.offsetLeft;
            <span class="hljs-keyword">let</span> left = card.offsetWidth / <span class="hljs-number">2</span>;
            <span class="hljs-keyword">let</span> rotateY = -(left - x) / <span class="hljs-number">5</span>;
            <span class="hljs-keyword">let</span> y = e.clientY - card.offsetTop;
            <span class="hljs-keyword">let</span> top = card.offsetHeight / <span class="hljs-number">2</span>;
            <span class="hljs-keyword">let</span> rotateX = (top - y) / <span class="hljs-number">5</span>;
            card2.style.cssText = <span class="hljs-string">`
               transform: rotateX(<span class="hljs-subst">$&#123;rotateX&#125;</span>deg) rotateY(<span class="hljs-subst">$&#123;rotateY&#125;</span>deg); `</span>
        &#125;)
        card.addEventListener(<span class="hljs-string">'mouseout'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">e</span>) </span>&#123;
            card2.style.cssText = <span class="hljs-string">`
               transform: rotateY(0deg) rotateX(0deg); `</span>
        &#125;)
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">总结：</h2>
<p>这个效果拿来练习很不错~
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63cdb172cef445edb2b24b48e0c4ecce~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>CSDN的其它文章~：</strong>
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
......等等</p></div>  
</div>
            