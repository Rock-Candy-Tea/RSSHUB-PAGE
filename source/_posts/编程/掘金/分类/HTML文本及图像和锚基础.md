
---
title: 'HTML文本及图像和锚基础'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'xxx.png'
author: 掘金
comments: false
date: Sat, 24 Jul 2021 04:27:00 GMT
thumbnail: 'xxx.png'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、HTML文本结构</h2>
<blockquote>
<p>浏览器通常会为其文本元素添加不同的样式，以区别于普通文本。例如 em 和 cite 元素中的文本都是斜体的。又如，code 元素专门用来格式化脚本或程序中的代码，该元素中的文本默认使用等宽字体。内容显示的样子与其使用的标记没有关系。因此不应该为了让文字变为斜体就使用 em 或 cite，添加样式是 css 的事情。相反，应该选择能描述内容的 HTML 元素。</p>
</blockquote>
<ol>
<li>
<p><strong>添加段落</strong>：要在网页中开始一个新的段落，使用 <strong>p元素</strong>。（通过 css 可以为段落添加样式，包括字体、字号、颜色等。以及控制内行间距，段落文本对齐方式等。）</p>
<pre><code class="copyable"> <p> Text </p>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><strong>指定细则</strong>：<strong>small元素</strong> 表示细则一类的旁注，通常是文本中的一小块。</p>
<pre><code class="copyable"><p> HTML <small> HyperText Markup Language </small> </p>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p>3.<strong>标记重要和强调文本</strong>：<strong>strong元素</strong> 表示内容的重要性，而 <strong>em元素</strong> 表示内容的着重点。</p>
<pre><code class="copyable">   <p> <strong> Warning:Do not approach the ... <em>
     under any... </em> </strong> just because... </p>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>浏览器通常将 strong 文本以粗体显示，em 文本以斜体显示。可以用 CSS 将任何文本变为粗体或斜体，也可以覆盖 strong 和 em 等元素的浏览器默认显示样式。</p>
<p>4.<strong>创建图</strong>：图可以是图表、照片、图形、插图、代码片段以及其他类似的独立内容。通过引入 <strong>figure 和 figcaption</strong>，figcaption 是 figure 的标题。</p>
<pre><code class="copyable"><figure>
<figcaption>
 [标题内容]
</figcaption>
 [插入内容]
<img src = "xxx.png" width = "180" height = "143" 
 alt = "Reveue chart:Clothing 42%,Toys 36%, Food 22%" />
</figure>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>figcaption 元素并不是必须的，但是只有包含它，就必须是 figure 元素内嵌的第一个或最后一个，且只能有一个。
5.<strong>指明引用或参考</strong>：使用 <strong>cite元素</strong> 可以指明对某内容源的引用或参考。默认以斜体显示（不因使用 cite 引用人名）</p>
<pre><code class="copyable"> <p> he Listend to <cite> Abbey Road </cite> </p>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>6.<strong>引述文本</strong>：有两个特殊的元素用以标记引述的文本。<strong>blockquote元素</strong> 表示单独存在的引述，其默认显示在新的一行。而 <strong>q元素</strong> 则用于短的引用，如句子里面的引述。由于q元素存在夸浏览器问题，应该避免使用，而是直接输入引号。</p>
<pre><code class="copyable"><blockquote>
 text...
</blockquote>
浏览器对应q元素中的文本自动加上语音的引号。
<p> And then she said,<q lang ="" > Have you read... </q> </p>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>7.<strong>指定时间</strong>：使用 <strong>time元素</strong> 标记时间、日期或时间段。输入 datetime="time" 指定格式日期，可以按照你希望的任何形式表示日期。</p>
<pre><code class="copyable"><time> 16:20 </time>  <time > 2021-07-24 </time>
<time datetime= "2021-07-24"> Ochtober 24,2021 </time>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>8.<strong>解释缩写词</strong>：使用 <strong>abbr元素</strong> 标记缩写词并解释其含义。（通常是使用括号提供缩写词的全称是解释缩写词最直接的方式）</p>
<pre><code class="copyable"><p> The <abbr title = "Notional Football league"> NFL </abbr> </p>
<p> But,that's ... <abbr> MLB </abbr> (Major league Baseball) ... </p>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>9.<strong>定义术语</strong>:在HTML中定义术语时，使用 <strong>dfn元素</strong> 对其作语义上的区分，首次定义术语通常会对其添加区别于其他文本格式，后续在使用术语时不再需要使用dfn对其进行标记。
（默认以斜体显示）</p>
<pre><code class="copyable">  <p> The contesttant ... <dfn> pleonasm </dfn> </p>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>10.<strong>创建上标和下标</strong>:比主体文本稍高或稍低的字母或数字分别成称为上标和下标。可以使用 <strong>sub元素</strong> 创建下标， <strong>sup元素</strong> 创建上标。上标和下标字符会轻微地扰乱行与行之间的均匀间距，但可以使用 CSS 修复这个问题。</p>
<pre><code class="copyable"><p> ... <a href = "#footnote-1" title = "REad footnote 1"> 
    Text   <sub> 1 </sub> </a> </p>
<p> ... <a href = "#footnote-1" title = "REad footnote 1">
    Text <sup> 1 </sup> </a> </p>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>11.<strong>添加作者联系方式</strong>: <strong>address元素</strong> 用以定于与 HTML 页面或页面一部分有关的作者、相关人士信息或组织联系信息，通常位于页面底部或相关部分内。</p>
<pre><code class="copyable"> <footer role = "contentinfo">
  <p> <small> &copy; 2021 The Paper of ... </small> </p>
 <address>
  Hava a question or ... <a href = "site-feedback.html"> Contact our </a>
  </address>
</footer>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>12.<strong>标注编辑和不再准确的文本</strong>:有时可能需要将在前一版本之后对页面的编辑标出来，或者对不再准确、不再相关的文本进行标记。有两种用于标注编辑的元素：代表添加内容的 <strong>ins元素</strong> 和标记已经删除内容的 <strong>del元素。</strong></p>
<pre><code class="copyable">  <li> <del> desks </del> </li>
  <li> <ins> bicycle </ins> </li>
  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通常对已删除的文本加上删除线，对插入的文本加入下划线。标记不再准确或不再相关的文本</p>
<pre><code class="copyable">  <li> <s> 5 p.m </s> SOLD </li>
  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>13.<strong>标记代码</strong>:如果你的内容包含代码示例或文件名，使用 <strong>code元素</strong>。</p>
<pre><code class="copyable"> <p> The <code> showPhoto() </code> ... <code> &lt ;ul 
 id = "thumbanil" &gt; </code> list </p>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>14.<strong>使用预格式化的文本</strong>：通常浏览器会将所有额外的回车和空格压缩，并根据窗口大小自动换行，预格式化的文本可以保持固有的换行和空格。<strong>pre元素</strong>。</p>
<pre><code class="copyable"><pre>
 <code>
  abbr[title] &#123;
    border-boottom: 1px dotted #000;
  &#125;
</code>
<span class="copy-code-btn">复制代码</span></code></pre>
  
 如果要显示包含 HTML 元素内容，应将包围元素名称的 < 和 > 分别改为对应的字符实体<和 >否则浏览器就会试着显示这些元素。大多数情况下推荐队 div 元素使用 white-space:pre 以替代 pre，因为空格可能对这些内容的语义非常重要。
<p>15.<strong>突出显示文本</strong>：类似文本中的荧光笔！HTML5 使用新的 <strong>mark元素</strong> 实现，引起读者对特定文本片段的注意。对原生支持的浏览器将对该元素文字默认加上黄色背景。</p>
<pre><code class="copyable"><p> GSL is <mark> YYDS! </mark>       
<span class="copy-code-btn">复制代码</span></code></pre>
<p>16.<strong>创建换行</strong>：当我们希望在文本中手动强制文字进行换行时，可以使用 <strong>br元素</strong> (空元素).</p>
<pre><code class="copyable"><p> 123 <br />
    456 <br />
</p>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>17.<strong>创建span</strong>：同 div 一样，<strong>span元素</strong> 是没有任何语义的，不同的是，span 只适合包围字词或短语内容，而 div 适合包含块级内容。</p>
<pre><code class="copyable"> <p> Gaudi's work was essentially useful.
 <span lang ="es"> La Casa Mila </span> is an ...
 </p>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>18.<strong>其他元素</strong>：</p>
<p><strong>U元素</strong>：用来为文本添加下划线。</p>
<p><strong>wbr元素</strong>：表示可换行处。让浏览器知道在哪里可以根据需要进行换行（存在跨版本问题）。</p>
<p><strong>ruby元素</strong>：旁注标记是一种惯用符号，通常用于表示生僻字的发音。</p>
<p><strong>bdi和bdo元素</strong>：如果某些页面中混合了从左至右书写的字符（如拉丁字符）和从右至左书写的字符（如阿拉伯语）, 就可能使用到bdi和bdo元素。</p>
<p><strong>meter元素</strong>：用 meter 元素表示分数的值或已知范围的测量结果。</p>
<pre><code class="copyable">  <p> Project completion status: <meter value="0.60">80% completed </meter> </p>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>progress元素</strong>:表示某项任务完成的进度，可用它表示一个进度条。不能与 meter 混在一起使用。</p>
<pre><code class="copyable"><p> Current progress: <progress max="100" value="30"> 30% saved </progress> </p>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">二、 HTML图片</h2>
<p>在页面插入图片：输入 <img src=image.url" /></p>
<pre><code class="copyable"><img src="xxx.jpg" alt="" />        
<span class="copy-code-btn">复制代码</span></code></pre>
<p>提供替代文本：在 img 标签内，src 属性及值的后面，输入 alt=""； 输入图像出于某种原因没有显示时应该出现的文本。指定图像的尺寸：在 img 标签内，src 属性后输入width="x", heigth="y"; 以像素为单位指定 x 和 y。</p>
<h2 data-id="heading-2">三、 HTML链接</h2>
<p>创建一个指向另一个网页的链接：</p>
<pre><code class="copyable">输入 <a href="URL"> 此处输入链接标签 </a>
    
<a href = "http://www.baidu.com"> 百度一下 </a>        
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建锚并链接到锚：
通常激活一个链接会将用户带到对应网页的顶端。如果想用户跳至网页特定区域，可以创建一个锚，并在链接中引用该锚。</p>
<p>1.创建锚： 输入 id="anchor-name",其中 name 是在内部用来标识网页中这部分内容的文字。</p>
<p>2.创建锚链接到特定锚链接：输入 <a href="#"anchor-name>，其中 anchor-name 是目标的 id 属性值。</p>
<p>3.输入标签文本（默认带下划线蓝色字体），用户激活该字体时将用户带到（1）步中引用的区域文本。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">``</span><span class="hljs-string">`<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>Creating and Linking to Anchors</title>
</head>
<body>

<article>
<header>
<h1>Frequently Asked Questions (FAQ)</h1>

<nav>
<ul>
<li><a href="#question-01">Can an id have more than one word?</a></li>
<li><a href="#question-02">Can visitors bookmark anchor links?</a></li>
<li><a href="#question-03">My anchor link isn't working. What am I doing wrong?</a></li>
<li><a href="#question-04">How do I link to a specific part of someone else's webpage?</a></li>
</ul>
</nav>
</header>

<h2 id="question-01">Can an id have more than one word?</h2>
<p>Yes, your ids can have more than one word as long as there are no spaces. Separate each word with a dash instead.</p>

<h2 id="question-02">Can visitors bookmark anchor links?</h2>
<p>Yes, they can! And when they visit that link, the browser will jump down to the anchor as expected. Visitors can share the link with others, too, so all the more reason to choose meaningful anchor names.</p>

<h2 id="question-03">My anchor link isn't working. What am I doing wrong?</h2>
<p>The problem could be a few things. First, double-check that you added an id (without "#") to the element your link should point to. Also, be sure that the anchor in your link <em>is</em> preceded by "#" and that it matches the anchor id.</p>

<h2 id="question-04">How do I link to a specific part of someone else's webpage?</h2>
<p>Although you obviously can't add anchors to other people's pages, you can take advantage of the ones that they have already created. View the source code of their webpage to see if they've included an id on the part of the page you want to link to. (For help viewing source code, consult "The Inspiration of Others" in Chapter 2.) Then create a link that includes the anchor.</p>
</article>

</body>
</html>
、
</span><span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            