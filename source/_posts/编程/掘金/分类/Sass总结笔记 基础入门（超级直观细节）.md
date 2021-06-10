
---
title: 'Sass总结笔记 基础入门（超级直观细节）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9580c92cb5a48649334b98f8758e6d6~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 08 Jun 2021 08:19:58 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9580c92cb5a48649334b98f8758e6d6~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第8天</p>
<h2 data-id="heading-0">一.什么是sass：</h2>
<ol>
<li>Sass 扩展了 CSS3，增加了规则、变量、混入、选择器、继承等等特性。Sass 生成良好格式化的 CSS 代码，易于组织和维护。</li>
<li>SASS是对CSS3(层叠样式表)的语法的一种扩充，它可以使用巢状、混入、选择子继承等功能，可以更有效有弹性的写出Stylesheet。Sass最后还是会编译出合法的CSS让浏览可以使用，也就是说它本身的语法并不太容易让浏览器识别(虽然它和CSS的语法非常的像，几乎一样)，因为它不是标准的CSS格式，在它的语法内部可以使用动态变量等，所以它更像一种极简单的动态语言。</li>
<li>工程越大，css文件越大，重复代码越来越多，会变得难以维护，借助Sass可以提高写css的效率。</li>
</ol>
<h2 data-id="heading-1">二. 安装：</h2>
<p>cmd打开本地命令控制窗口，输入下面字符串然后回车就装好了。</p>
<pre><code class="hljs language-html copyable" lang="html">npm install -g sass
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9580c92cb5a48649334b98f8758e6d6~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
<a href="https://sass-lang.com/install" target="_blank" rel="nofollow noopener noreferrer">更多安装方法可以点我Sass去官网。</a></p>
<h2 data-id="heading-2">三.编译.scss文件为.css文件：</h2>
<p>Sass使用.scss作为文件后缀名，不能直接在< link >标签里使用，需要编译为 .css文件。
<strong>演示：</strong></p>
<ol>
<li>建一个html文件，随便写个h1标签：</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ebd33260d97444d80b0cf21ae96deae~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
2. 建一个.scss后缀的文件，如input.scss，写点基本样式sass的语法：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/82efad6d4a4c40eab5fde63999443b99~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
3. 在html文件所在的路径下打开cmd命令控制符，输入：</p>
<pre><code class="hljs language-html copyable" lang="html">sass input.scss ouput.css
<span class="copy-code-btn">复制代码</span></code></pre>
<p>表示把名字为 input.scss 转换成名字为 ouput.css 的文件（名字自己随意起）。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87a2b4cdc4f3452d88aec8e55bc856d9~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
回车后，接下来发现就得到了css的文件。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c81bc210aa524dcca37e65ff0d416625~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
css文件内容如下，可以看出转换好了：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/82efc7d3c5f14d36bb9f58bc2f3446dc~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
接下来就是老操作了，在HTML里用 < link >标签把css文件引入就行。</p>
<ol start="4">
<li>但是不可能说写一句.scss语句就转换一次，太麻烦，所以可以自动转换，当我在.scss里写一句，.css就自动生成一句。在cmd输入以下：</li>
</ol>
<pre><code class="hljs language-html copyable" lang="html">sass --watch input.scss:ouput.css
<span class="copy-code-btn">复制代码</span></code></pre>
<p>表示监视变化，当input.scss一变化，output.css就变化:
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aa2ad2fb568a427bbaad95dd6508ce8c~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
5. 如果一个html文件里有多个css文件呢？那么可以直接监视文件夹变化：
如：</p>
<pre><code class="hljs language-html copyable" lang="html">sass  --watch  yuan:bian
<span class="copy-code-btn">复制代码</span></code></pre>
<p>表示：当名字为yuan这个文件夹里任意一个.scss后缀的文件变化时，就将其编译到名字bian这个文件夹里面（会自动生成相应的.css文件）</p>
<h2 data-id="heading-3">四.基础用法与功能：</h2>
<p><strong>目录：</strong></p>
<p>1.变量；
2.嵌套；
3.mixin；
4.继承；
5. import；
6. 计算；
7. 颜色函数；
8.  Interpolation；
9. if 判断；
10. for循环；
11. 列表循环；
12. while循环；
13.function自定义函数；
......待更新....</p>
<p><strong>详细用法</strong>：</p>
<h6 data-id="heading-4">1. <strong>变量</strong>（定义变量后，在选择器里可以直接引用）：</h6>
<p>如：我定义一个变量名为 $yanse，值为颜色rgb(223, 148, 148)</p>
<pre><code class="hljs language-css copyable" lang="css">$yanse: <span class="hljs-built_in">rgb</span>(<span class="hljs-number">223</span>, <span class="hljs-number">148</span>, <span class="hljs-number">148</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>直接在选择器引用：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">h1</span>&#123;
        <span class="hljs-attribute">color</span>: $yanse；
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然变量也可以套娃，比如我定义一个变量名为 <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>k</mi><mi>u</mi><mi>a</mi><mi>n</mi><mi>g</mi><mtext>，里面引用了</mtext></mrow><annotation encoding="application/x-tex">kuang，里面引用了 </annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="mord mathnormal" style="margin-right:0.03148em;">k</span><span class="mord mathnormal">u</span><span class="mord mathnormal">a</span><span class="mord mathnormal">n</span><span class="mord mathnormal" style="margin-right:0.03588em;">g</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">里</span><span class="mord cjk_fallback">面</span><span class="mord cjk_fallback">引</span><span class="mord cjk_fallback">用</span><span class="mord cjk_fallback">了</span></span></span></span></span>yanse</p>
<pre><code class="hljs language-css copyable" lang="css">$yanse: <span class="hljs-built_in">rgb</span>(<span class="hljs-number">223</span>, <span class="hljs-number">148</span>, <span class="hljs-number">148</span>);
$kuang: <span class="hljs-number">1px</span> solid $yanse;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后也直接用：</p>
<pre><code class="hljs language-css copyable" lang="css"> <span class="hljs-selector-tag">h1</span>&#123;
        <span class="hljs-attribute">border</span>: $kuang;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-5">2. <strong>嵌套</strong>（父选择器里可以嵌套子选择器）</h6>
<p>如：有以下标签</p>
<pre><code class="hljs language-html copyable" lang="html"> <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">ul</span>></span>     
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以直接这样写：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">div</span>&#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-selector-tag">ul</span>&#123;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">80px</span>;
        <span class="hljs-selector-tag">li</span>&#123;
           <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相当于：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">div</span> &#123;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
&#125;
<span class="hljs-selector-tag">div</span> <span class="hljs-selector-tag">ul</span> &#123;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">80px</span>;
&#125;
<span class="hljs-selector-tag">div</span> <span class="hljs-selector-tag">ul</span> <span class="hljs-selector-tag">li</span> &#123;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>若 li 有伪类选择器：hover可以这样写（里面添加&：hover&#123;&#125;）：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">div</span>&#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
    <span class="hljs-selector-tag">ul</span>&#123; 
        <span class="hljs-attribute">height</span>: <span class="hljs-number">80px</span>;
        <span class="hljs-selector-tag">li</span>&#123;
           <span class="hljs-attribute">height</span>: <span class="hljs-number">50px</span>;
           &<span class="hljs-selector-pseudo">:hover</span> &#123;
             <span class="hljs-attribute">color</span>: <span class="hljs-number">#000</span>;
           &#125;
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相当于又写了：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">div</span> <span class="hljs-selector-tag">ul</span> <span class="hljs-selector-tag">li</span><span class="hljs-selector-pseudo">:hover</span> &#123;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#000</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>不止选择器，属性里也可以嵌套，如这样写：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">div</span>&#123;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;

    <span class="hljs-attribute">font</span>: &#123;
        family: <span class="hljs-string">'fangsong'</span>;
        size: <span class="hljs-number">20px</span>;
        weight: <span class="hljs-number">700</span>;
    &#125;
    <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid red &#123;
       left: <span class="hljs-number">0</span>;
       <span class="hljs-attribute">top</span>: <span class="hljs-number">0</span>;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相当于：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">div</span> &#123;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">100px</span>;
  <span class="hljs-attribute">font-family</span>: <span class="hljs-string">"fangsong"</span>;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">20px</span>;
  <span class="hljs-attribute">font-weight</span>: <span class="hljs-number">700</span>;
  <span class="hljs-attribute">border</span>: <span class="hljs-number">1px</span> solid red;
  <span class="hljs-attribute">border-left</span>: <span class="hljs-number">0</span>;
  <span class="hljs-attribute">border-top</span>: <span class="hljs-number">0</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-6">3. <strong>mixin 混合</strong> （相当于预先写好了一组样式，其它地方直接引用）：</h6>
<p>基本语法：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@mixin</span> 名字（参数<span class="hljs-number">1</span>，参数<span class="hljs-number">2</span>，...）
&#123;
........样式.......

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如（无参数的，里面也可以嵌套，下面定义了一个名字为hunhe的mixin，然后在div这个选择器里通过（@include 名字）调用 ）：</p>
<pre><code class="hljs language-css copyable" lang="css">
<span class="hljs-keyword">@mixin</span> hunhe &#123;
     <span class="hljs-attribute">color</span>: red;
     <span class="hljs-selector-tag">a</span> &#123;
         <span class="hljs-attribute">font-size</span>: <span class="hljs-number">12px</span>;
     &#125;
&#125;

<span class="hljs-selector-tag">div</span>&#123;
    <span class="hljs-keyword">@include</span> hunhe;  
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相当于：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">div</span> &#123;
  <span class="hljs-attribute">color</span>: red;
&#125;
<span class="hljs-selector-tag">div</span> <span class="hljs-selector-tag">a</span> &#123;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">12px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有参数的（更灵活，参数相当于你要的数值，参数名前面要写$，调用时值的位置要对）：</p>
<p>如：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@mixin</span> hunhe($one,$two) &#123;
     <span class="hljs-attribute">color</span>: $one;
     <span class="hljs-selector-tag">a</span> &#123;
         <span class="hljs-attribute">color</span>: $one;
         <span class="hljs-attribute">font-size</span>: $two;
     &#125;
&#125;

<span class="hljs-selector-tag">div</span>&#123;
    <span class="hljs-keyword">@include</span> hunhe(red,<span class="hljs-number">15px</span>);  
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>*div也可以这样写,指定参数名，参数位置就可以随意变换：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">div</span>&#123;
    <span class="hljs-keyword">@include</span> hunhe($<span class="hljs-attribute">two</span>:<span class="hljs-number">15px</span>,$<span class="hljs-attribute">one</span>:red);  
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面相当于：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">div</span> &#123;
  <span class="hljs-attribute">color</span>: red;
&#125;
<span class="hljs-selector-tag">div</span> <span class="hljs-selector-tag">a</span> &#123;
  <span class="hljs-attribute">color</span>: red;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">15px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-7">4. <strong>继承/扩展</strong>（一个选择器可以继承另一个选择器的全部样式）</h6>
<p>如: .two类里继承了.one类的全部样式 （<strong>@extend  名字</strong>）；  <em>还不止.one的，跟.one相关的都继承了</em> ，具体如下：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.one</span>&#123;
    <span class="hljs-attribute">color</span>: <span class="hljs-number">#000</span>;
&#125;
<span class="hljs-selector-class">.one</span> <span class="hljs-selector-tag">a</span>&#123;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="hljs-selector-class">.two</span>&#123;
    <span class="hljs-keyword">@extend</span> .one;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#fff</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相当于：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.one</span>, <span class="hljs-selector-class">.two</span> &#123;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#000</span>;
&#125;

<span class="hljs-selector-class">.one</span> <span class="hljs-selector-tag">a</span>, <span class="hljs-selector-class">.two</span> <span class="hljs-selector-tag">a</span> &#123;
  <span class="hljs-attribute">font-size</span>: <span class="hljs-number">10px</span>;
&#125;

<span class="hljs-selector-class">.two</span> &#123;
  <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#fff</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-8">5. <strong>@import</strong> 引入一个.scss后缀的文件作为自己的一部分，被引入的那个文件并不会转换成.css格式的，所以此文件命名要注意以下划线开头，如：_base.scss ，引入它的时候不用写下划线。</h6>
<p>语法：@import: ".....路径";
如：
建立一个文件叫 _base.scss，里面写上一些选择器和样式，然后在一个正常的如one.scss文件里引入它,假如目录是同等级的：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@import</span>: <span class="hljs-string">"base.scss"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样.one.scss就有了_base.scss里的全部内容。</p>
<h6 data-id="heading-9">6. <strong>计算功能</strong> （SASS允许在代码中使用算式）如：</h6>
<pre><code class="hljs language-css copyable" lang="css">  $chang: <span class="hljs-number">20px</span>;
<span class="hljs-selector-tag">body</span>&#123;   
    <span class="hljs-attribute">margin</span>: (<span class="hljs-number">10px</span>*<span class="hljs-number">2</span>);
    <span class="hljs-attribute">left</span>: <span class="hljs-number">20px</span> + $chang;
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相当于：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">body</span> &#123;
  <span class="hljs-attribute">margin</span>: <span class="hljs-number">20px</span>;
  <span class="hljs-attribute">left</span>: <span class="hljs-number">40px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-10">7. <strong>颜色函数</strong>（SASS提供了一些内置的颜色函数，以便生成系列颜色。）</h6>
<p><strong>hsl（色相，饱和度，明度）;</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">body</span>&#123;   
   <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">hsl</span>(<span class="hljs-number">5</span>, <span class="hljs-number">20%</span>, <span class="hljs-number">20%</span>);
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相当于：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">body</span> &#123;
  <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#3d2b29</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>hsl（色相，饱和度，明度，不透明度）;</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">body</span>&#123;   
   <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">hsl</span>(<span class="hljs-number">5</span>, <span class="hljs-number">20%</span>, <span class="hljs-number">20%</span>,<span class="hljs-number">0.5</span>);
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相当于：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">body</span> &#123;
  <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">rgba</span>(<span class="hljs-number">61</span>, <span class="hljs-number">43</span>, <span class="hljs-number">41</span>, <span class="hljs-number">0.5</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>用来调整色相： adjust-hue(颜色，调整的度数)；</strong></p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">body</span>&#123;   
   <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">adjust-hue</span>(<span class="hljs-built_in">hsl</span>(<span class="hljs-number">0</span>,<span class="hljs-number">100</span>,<span class="hljs-number">50%</span>), <span class="hljs-number">100deg</span>);
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相当于：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">body</span> &#123;
  <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#55ff00</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>用来调整颜色明度：lighten让颜色更亮，darken让颜色更暗</strong>
如：lighten（颜色，增加亮度的百分比）；</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">body</span>&#123;   
   <span class="hljs-attribute">background-color</span>: <span class="hljs-built_in">lighten</span>(<span class="hljs-built_in">rgb</span>(<span class="hljs-number">228</span>, <span class="hljs-number">145</span>, <span class="hljs-number">145</span>),<span class="hljs-number">50%</span>);
   <span class="hljs-attribute">color</span>: <span class="hljs-built_in">darken</span>(<span class="hljs-built_in">rgb</span>(<span class="hljs-number">228</span>, <span class="hljs-number">145</span>, <span class="hljs-number">145</span>),<span class="hljs-number">50%</span>);
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相当于：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">body</span> &#123;
  <span class="hljs-attribute">background-color</span>: white;
  <span class="hljs-attribute">color</span>: <span class="hljs-number">#5f1717</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>用来调整颜色纯度 saturate让颜色更纯 ，desaturate让颜色不纯</strong>
saturate（颜色，百分比）；</p>
<h6 data-id="heading-11">8. <strong>Interpolation</strong> 把一个值插入到另一个值，具体用法如下 #&#123;变量&#125; 如：</h6>
<pre><code class="hljs language-css copyable" lang="css">$yanse: color;
<span class="hljs-selector-tag">body</span>&#123;   

   #&#123;$yanse&#125;:red;
   
&#125;  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相当于：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">body</span> &#123;
  <span class="hljs-attribute">color</span>: red;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="9">
<li><strong>if 判断（逻辑跟C语言差不多）：</strong></li>
</ol>
<p>语法：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@if</span> 判断条件 &#123;
.......执行语句...
&#125; <span class="hljs-keyword">@else</span> &#123;
  ..<span class="hljs-selector-class">.else</span>有就写没就不写....
&#125;
 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如：</p>
<pre><code class="hljs language-css copyable" lang="css">$jia: false;
<span class="hljs-selector-tag">body</span>&#123;   

   <span class="hljs-keyword">@if</span> false&#123;
       <span class="hljs-attribute">color</span>: red;
   &#125;
   <span class="hljs-keyword">@if</span> <span class="hljs-number">2</span>><span class="hljs-number">3</span> &#123;
       <span class="hljs-attribute">background-color</span>: white;
   &#125;<span class="hljs-keyword">@else</span>&#123;
       <span class="hljs-attribute">background-color</span>: black;
   &#125;
   
&#125;  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相当于：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">body</span> &#123;
  <span class="hljs-attribute">background-color</span>: black;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-12">10. <strong>for循环</strong></h6>
<p>语法：</p>
<pre><code class="hljs language-css copyable" lang="css">结束值不执行：
<span class="hljs-keyword">@for</span> 变量 from 开始值 through 结束值 &#123;
     ......
&#125;
结束值也执行：
<span class="hljs-keyword">@for</span> 变量 from 开始值 to 结束值 &#123;
     ......
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>例子：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@for</span> $i from <span class="hljs-number">1</span> to <span class="hljs-number">3</span> &#123;
    
    <span class="hljs-selector-class">.div</span>#&#123;$<span class="hljs-selector-tag">i</span>&#125;&#123;
       <span class="hljs-attribute">height</span>: $i*<span class="hljs-number">20px</span>;
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相当于：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.div1</span> &#123;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">20px</span>;
&#125;

<span class="hljs-selector-class">.div2</span> &#123;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">40px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-13">11. <strong>列表循环</strong>，能循环一遍一个列表的值，列表相当于数组；</h6>
<p>语法：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@each</span> 变量 in 列表&#123;
...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>例子：</p>
<pre><code class="hljs language-css copyable" lang="css">$yanse: red blue black;
<span class="hljs-keyword">@each</span> $i in $yanse &#123;
    
    <span class="hljs-selector-class">.div</span>#&#123;$<span class="hljs-selector-tag">i</span>&#125;&#123;
      <span class="hljs-attribute">color</span>: $i;
    &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相当于：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.divred</span> &#123;
  <span class="hljs-attribute">color</span>: red;
&#125;

<span class="hljs-selector-class">.divblue</span> &#123;
  <span class="hljs-attribute">color</span>: blue;
&#125;

<span class="hljs-selector-class">.divblack</span> &#123;
  <span class="hljs-attribute">color</span>: black;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-14">12. <strong>while循环</strong>，有判断条件更灵活。</h6>
<p>语法：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@while</span> 条件 &#123;
   ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>例子：</p>
<pre><code class="hljs language-css copyable" lang="css">$gao: <span class="hljs-number">1</span>;
<span class="hljs-keyword">@while</span> $gao<<span class="hljs-number">4</span> &#123;
    <span class="hljs-selector-class">.div</span>#&#123;$gao&#125;&#123;
        <span class="hljs-attribute">height</span>: $gao*<span class="hljs-number">10px</span>;
    &#125;
   $gao : $gao+<span class="hljs-number">1</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相当于：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.div1</span> &#123;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">10px</span>;
&#125;

<span class="hljs-selector-class">.div2</span> &#123;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">20px</span>;
&#125;

<span class="hljs-selector-class">.div3</span> &#123;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">30px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h6 data-id="heading-15">13.<strong>自定义函数 function</strong>,自己定义的函数可以调用；</h6>
<p>语法：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@function</span> 名字(参数<span class="hljs-number">1</span>，参数<span class="hljs-number">2</span>，..)&#123;
....
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>例子：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-keyword">@function</span> ziji ($bian)
&#123;
    <span class="hljs-keyword">@return</span> $bian+<span class="hljs-number">10px</span>;
&#125;

<span class="hljs-selector-tag">div</span>&#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-built_in">ziji</span>(<span class="hljs-number">5px</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相当于：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">div</span> &#123;
  <span class="hljs-attribute">width</span>: <span class="hljs-number">15px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">总结：</h2>
<p><strong>有帮助的话就点个赞吧~</strong></p>
<p>其它文章：
<a href="https://blog.csdn.net/luo1831251387/article/details/112974745" target="_blank" rel="nofollow noopener noreferrer">响应式卡片悬停效果 html+css</a>
<a href="https://blog.csdn.net/luo1831251387/article/details/111714413" target="_blank" rel="nofollow noopener noreferrer">水波加载动画 html+css</a>
<a href="https://blog.csdn.net/luo1831251387/article/details/111601962" target="_blank" rel="nofollow noopener noreferrer">导航栏滚动渐变效果 html+css+js</a>
<a href="https://blog.csdn.net/luo1831251387/article/details/111398881?spm=1001.2014.3001.5502" target="_blank" rel="nofollow noopener noreferrer">书本翻页 html+css</a>
<a href="https://blog.csdn.net/luo1831251387/article/details/111032274?spm=1001.2014.3001.5502" target="_blank" rel="nofollow noopener noreferrer">3D立体相册 html+css</a>
<a href="https://blog.csdn.net/luo1831251387/article/details/111162570?spm=1001.2014.3001.5502" target="_blank" rel="nofollow noopener noreferrer">炫彩流光按钮 html+css</a>
等等等.....</p></div>  
</div>
            