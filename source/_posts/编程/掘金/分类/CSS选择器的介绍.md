
---
title: 'CSS选择器的介绍'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9662'
author: 掘金
comments: false
date: Sat, 27 Mar 2021 03:40:21 GMT
thumbnail: 'https://picsum.photos/400/300?random=9662'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">元素选择符</h1>
<p>元素选择符通常是HTML元素，但也有例外。主要是在XML中，在CSS文档中什么都可以作为选择符，因为XML可以自己创建新标记语言。但是在HTML中书写CSS样式时，选择符则是HTML中预定的元素，例如p,h1,div等。
例：</p>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-tag">div</span> &#123;
    <span class="hljs-attribute">color</span>: red;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">群组选择符</h1>
<p>ok，群组选择符的应用是非常常用的，我们在开发中经常会遇到多个HTML元素应用同一种CSS样式，这时群组选择器则是最好的选择器之一了。</p>
<p>那我们来看看群组选择器的基本用法吧
例如，在HTML页面中有div和p元素都要用到color属性样式</p>
<pre><code class="hljs language-CSS copyable" lang="CSS">    <span class="hljs-selector-tag">div</span>, <span class="hljs-selector-tag">p</span> &#123;
            <span class="hljs-attribute">color</span>: red;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也就是选择符之间用逗号进行隔开；并且放在一起的选择符的数量是没有任何限制的，也就是你想放多少选择符就可以放多少选择符。
群组选择符可以在很大程度上压缩同类样式，这样得到的样式表更短，更加轻松。
例如如下普通写法：</p>
<pre><code class="hljs language-CSS copyable" lang="CSS">        <span class="hljs-selector-tag">h1</span> &#123;
            <span class="hljs-attribute">color</span>: red;
        &#125;
        <span class="hljs-selector-tag">h2</span> &#123;
            <span class="hljs-attribute">color</span>: red;
        &#125;
        <span class="hljs-selector-tag">h3</span> &#123;
            <span class="hljs-attribute">color</span>: red;
        &#125;
        <span class="hljs-selector-tag">h4</span> &#123;
            <span class="hljs-attribute">color</span>: red;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如下使用群组选择符的写法：</p>
<pre><code class="hljs language-css copyable" lang="css">        <span class="hljs-selector-tag">h1</span>, <span class="hljs-selector-tag">h2</span>, <span class="hljs-selector-tag">h3</span>, <span class="hljs-selector-tag">h4</span> &#123;
            <span class="hljs-attribute">color</span>: red;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以哪一种写起来更加轻松相信大家都一亩了然了吧。</p>
<h1 data-id="heading-2">通用选择符</h1>
<p>通用选择符是在CSS2中引入的选择符，用星号代替(*).
他的作用很明显，就是选中HTML页面中的所有元素，给它们编写同样的样式 <br>
例如，我想要让HTML页面的所有元素的背景变成红色</p>
<pre><code class="hljs language-cSS copyable" lang="cSS">        * &#123;
            <span class="hljs-attribute">background-color</span>: red;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>是不是感觉很简单呢？但是通用选择符（通配符选择器）在CSS中应用的很少。因为第一是它的CSS权重最低（到时候会出一篇文章讲解CSS权重的算法），第二是因为它的目标是所有的元素，所以应用的时候难免会出现意料之外的后果。</p>
<h1 data-id="heading-3">类选择符和ID选择符</h1>
<h2 data-id="heading-4">类选择符</h2>
<p>ok，先从类选择符开始说起。上面已经介绍了元素选择符，但是非常简单，难以满足现代网页错综复杂的样式需求。所以我们还需要更加特指和更加精准的CSS选择符。这时类选择符则是一个不二的选择。</p>
<p>例如：在一个HTML网页中，有很多段文落，现在有一个需求，就是需要在某一段文落中的某一组词进行特殊的样式处理，比如改变它的颜色。
例：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>我是老司机我是老司机我是老司机我是<span class="hljs-tag"><<span class="hljs-name">span</span>></span>老司机<span class="hljs-tag"></<span class="hljs-name">span</span>></span>我是老司机我是老司机我是老司机<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span>你是老司机你是老司机你是老司机你是老司机你是老司机<span class="hljs-tag"><<span class="hljs-name">span</span>></span>你是老司机你是老司机<span class="hljs-tag"></<span class="hljs-name">span</span>></span>你是老司机你是老司机<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span>我喜欢编程我喜欢编程我喜欢编程我喜欢编程我喜欢编程我喜欢编程，<span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"pr"</span>></span>我是中国人，我喜欢编程我喜欢编程我喜欢编程我喜欢编程，你呢？<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ok，现在我要将第三段中用span元素包裹的文字改变它的颜色，那么我们用元素选择符就达不到我们的目的了。那么我们用类选择符就能很轻松的达到我们的目的。</p>
<pre><code class="hljs language-CSS copyable" lang="CSS">        <span class="hljs-selector-class">.pr</span> &#123;
            <span class="hljs-attribute">color</span>: red;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样我们就很轻松并且很精准的就选择到了我们想要的那段文字，并添加了相应的样式。
当然，要让类选择符起作用及，必须先给元素的class属性一个类（属性值），而我们在CSS样式表中，需要将相应你要处理的元素的class属性值作为类选择符，并且在前面要用. + 相应的元素的class属性值。如上述代码所示</p>
<p>当然类选择符也是可以搭配任何其它类型的选择符，例：</p>
<pre><code class="hljs language-CSS copyable" lang="CSS">        <span class="hljs-selector-tag">span</span><span class="hljs-selector-class">.pr</span> &#123;
            <span class="hljs-attribute">color</span>: red;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样写更加的精准，权重会更高。表示只能选择span元素中有class属性的属性值为pr的元素，也能达到上述效果。
一个元素的class属性中不止一个属性值，可以是多个类，他们之间用逗号隔开：<br></p>
<p><code><p class="pr dr pg">我是老司机我是老司机我是老司机我是老司机我是老司机我是老司机我是老司机</p></code></p>
<h2 data-id="heading-5">ID选择符</h2>
<p>ID选择符类似于类选择符，但是它们之间也有不同之处。首先它们开头的符号不同，类选择符是. 开头，ID选择符是# 开头</p>
<pre><code class="hljs language-CSS copyable" lang="CSS">    <span class="hljs-selector-id">#container</span> &#123;
        <span class="hljs-attribute">display</span>: block;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二个区别是id选择符引用的是id属性的值，并不是class属性的值，这显而易见。
当然最重要的是一个HTML文档中只能出现一个相同值的id属性，而class则可以出现多个。这也是id选择符用的比较少的原因之一。当然也是因为这个原因，所以这个选择器用于精确选择非常好，所以经常用于HTML文档中划分区域的元素中。</p>
<pre><code class="hljs language-css copyable" lang="css">    <<span class="hljs-selector-tag">header</span> id="<span class="hljs-selector-tag">header</span>">
        <<span class="hljs-selector-tag">div</span>></<span class="hljs-selector-tag">div</span>>
        <<span class="hljs-selector-tag">div</span>></<span class="hljs-selector-tag">div</span>>
        <<span class="hljs-selector-tag">div</span>></<span class="hljs-selector-tag">div</span>>
    </<span class="hljs-selector-tag">header</span>>

    <<span class="hljs-selector-tag">nav</span> id="<span class="hljs-selector-tag">nav</span>">
        <<span class="hljs-selector-tag">div</span>></<span class="hljs-selector-tag">div</span>>
        <<span class="hljs-selector-tag">div</span>></<span class="hljs-selector-tag">div</span>>
        <<span class="hljs-selector-tag">div</span>></<span class="hljs-selector-tag">div</span>>
    </<span class="hljs-selector-tag">nav</span>>

    <<span class="hljs-selector-tag">div</span> id="container">
        <<span class="hljs-selector-tag">div</span>></<span class="hljs-selector-tag">div</span>>
        <<span class="hljs-selector-tag">div</span>></<span class="hljs-selector-tag">div</span>>
        <<span class="hljs-selector-tag">div</span>></<span class="hljs-selector-tag">div</span>>
    </<span class="hljs-selector-tag">div</span>>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-6">属性选择符</h1>
<p>前面我讲过的两个类选择符和id选择符，都是选择的属性的值。而属性选择器很显然是选择操作元素的属性进行选择和相应的操作。</p>
<p>属性选择符通常分为：<strong>简单属性选择符</strong>、<strong>精准属性值选择符</strong>、<strong>部分匹配属性值选择符</strong>、<strong>起始值属性选择符</strong>。</p>
<h2 data-id="heading-7">简单属性选择符</h2>
<p>如果你想选择具有某个属性的元素，不去考虑它的属性值是什么，可以使用简单属性选择符。比如我想找到所有具有class属性的div元素，例：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-tag">div</span><span class="hljs-selector-attr">[class]</span> &#123;
            <span class="hljs-attribute">color</span>: red;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"pr"</span>></span>hello World<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>hello World<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注：属性选择符都是写在[这里面写属性选择符]里面的。
当然它也是可以配合多种选择符来使用。</p>
<h2 data-id="heading-8">精准属性值选择符</h2>
<p>精准属性值选择符就是通过属性加属性值来更加精确的选择到某元素。
例如有两个a元素，分别是百度和淘宝，现在我要给百度这个链接一个文字颜色，则可以使用精准属性值选择符：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-tag">a</span><span class="hljs-selector-attr">[href=<span class="hljs-string">"http://www.baidu.com"</span>]</span> &#123;
            <span class="hljs-attribute">color</span>: red;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"http://www.baidu.com"</span>></span>百度<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"http://www.taobao.com"</span>></span>淘宝<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就可以选择到百度链接了。</p>
<p>也可以使用多个属性选择符进行元素选择，用只要在后面加上[]就可以多加属性。
例如：a[class="pr"][href="http://www.baidu.com"]。</p>
<h2 data-id="heading-9">根据部分属性值选择</h2>
<ol>
<li>根据属性选择符匹配字串</li>
</ol>





























<table><thead><tr><th>形式</th><th>说明</th></tr></thead><tbody><tr><td>[foo|="bar"]</td><td>选择的属性有foo属性，并且属性值是bar或者是以bar和一个英文破折号开头</td></tr><tr><td>[foo~="bar"]</td><td>选择的属性有foo属性，且其值是包含bar这一个词的一组词</td></tr><tr><td>[foo*="bar"]</td><td>选择的属性有foo属性，且其值是包含bar字串</td></tr><tr><td>[foo^="bar"]</td><td>选择的属性有foo属性，且其值以bar开头</td></tr><tr><td>[foo$="bar"]</td><td>选择的属性有foo属性，且其值以bar结尾</td></tr></tbody></table>
<p>具体作者就不在这里重复了。
详细可看W3school：<a href="https://www.w3school.com.cn/css/css_selector_attribute.asp" target="_blank" rel="nofollow noopener noreferrer">www.w3school.com.cn/css/css_sel…</a></p>
<p>注：属性选择符中的属性值可以不区分大小写，只要在中括号结尾前加上i就可以了。
a[href$="HTTP" i]</p>
<h1 data-id="heading-10">后代选择符</h1>
<p>首先了解后代选择符前先去了解以下HTML文档结构（树形结构）
后代选择符也叫上下文选择符。比如，我要选择h1元素中的span元素，然后给它添加字体颜色：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-tag">h1</span> <span class="hljs-selector-tag">span</span> &#123;
            <span class="hljs-attribute">color</span>: red;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>></span>hello World<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>后代选择符中每个选择符之间用空格进行分隔组成后代选择符。用后代选择符的前提是这个元素是某个元素的后代元素。比如上面的span就是h1的后代元素。
当然后代选择符组成部分不仅仅只可以元素选择符，也可以是id选择符、类选择符等等。</p>
<h1 data-id="heading-11">子元素选择符</h1>
<p>大家都知道，后代选择符的范围非常广，而如果我们只想选择某个元素的某个子元素，那么我们就可以使用子元素选择符。那么要使用子元素选择符，需要用>来连接
例如，我想选择div下的子元素span：</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-tag">div</span> > <span class="hljs-selector-tag">span</span> &#123;
            <span class="hljs-attribute">color</span>: red;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>></span>hello World<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h2</span>></span><span class="hljs-tag"><<span class="hljs-name">span</span>></span>great Father<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-12">相邻选择符</h1>
<p>它可以选择紧跟某个元素后面的元素，用 + 符号来表示，例如我想选择到标题元素的后面的div元素：</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-tag">h1</span> + <span class="hljs-selector-tag">div</span> &#123;
            <span class="hljs-attribute">color</span>: red;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>hello World<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>></span>hello World<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h2</span>></span><span class="hljs-tag"><<span class="hljs-name">span</span>></span>great Father<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-13">兄弟选择符</h1>
<p>兄弟选择符用~表示。它可以选择某一个元素同一级别的元素进行样式操作。比如我想选择h1同一级别的ol元素：</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-tag">h1</span> ~<span class="hljs-selector-tag">ol</span> &#123;
            <span class="hljs-attribute">background-color</span>: red;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>hello World<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">span</span>></span>hello World<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h2</span>></span><span class="hljs-tag"><<span class="hljs-name">span</span>></span>great Father<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">ol</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"><<span class="hljs-name">span</span>></span>11<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"><<span class="hljs-name">span</span>></span>21<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">li</span>></span><span class="hljs-tag"><<span class="hljs-name">span</span>></span>31<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">ol</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>hello World<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-14">伪类选择符</h1>
<p>伪类选择符真的是一个神器，它让css选择符变得更加有趣，有了伪类选择符，我们可以做到以前只能用JavaScript才能做到的事情。它主要是指元素的某种特定的状态，给其赋予幽灵类。所有的伪类都是:后面跟着伪类<br>
伪类有很多种，下面一一为大家介绍：</p>
<h2 data-id="heading-15">拼接伪类</h2>
<p>CSS是允许进行拼接伪类。比如，我想要鼠标悬停在未访问链接时链接变成红色：</p>
<pre><code class="hljs language-css copyable" lang="css">        <span class="hljs-selector-tag">a</span><span class="hljs-selector-pseudo">:link</span><span class="hljs-selector-pseudo">:hover</span> &#123;
            <span class="hljs-attribute">color</span>: red;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>拼接伪类不能是相互排斥的，比如不能是即未访问又即已访问的状态。例：a:link:visited，这样是不能选择到的。</p>
<h2 data-id="heading-16">结构伪类</h2>
<p>伪类大多数都是结构上的，伪类始终指代所依附的元素，根据其概念，这不难理解。比如想要选择爸妈的第一个孩子，那就必须是爸妈的第一个孩子，恰巧我是。#children:first-child。</p>
<h3 data-id="heading-17">选择根元素</h3>
<p>:root始终选择的是HTML文档的根元素，也就是html。
:root &#123;margin: 10px&#125;</p>
<h3 data-id="heading-18">选择空元素</h3>
<p>使用:empty可以选择没有任何子元素的目标元素，包括没有空白和任何文本节点。</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-tag">p</span><span class="hljs-selector-pseudo">:empty</span> &#123;
            <span class="hljs-attribute">display</span>: none;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span>

    <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span> <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">p</span>></span><span class="hljs-comment"><!-- hello world --></span><span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面可以选择到第一个和第四个p元素。</p>
<h3 data-id="heading-19">选择唯一的子代</h3>
<p>使用:only-child伪类，它选择的元素是另一个元素的唯一子元素。那么你可以选择所有带有a链接的图片，因为图片是a链接的唯一子元素 img:only-child ，就可以选择到a链接的图片了。</p>
<h3 data-id="heading-20">选择第一个和最后一个子代</h3>
<p>为一个元素的第一个或最后一个元素应用特殊的样式是常见的需求。
:first-child 伪类选择一个元素的第一个子元素，这个元素必须是父元素中的第一个子元素。
:last-child 伪类选择一个元素的最后一个子元素，这个元素必须是父元素中的最后一个子元素。<br></p>
<p>注：元素:first-child:last-child 放在一起相当于only-child伪类的效果。</p>
<h3 data-id="heading-21">选择第一个和最后一个某种元素</h3>
<p>:first-of-type和:last-of-type，会选择第一个或最后一个元素，并且这个元素在父元素中的其它相同元素中的第一个或最后一个元素，和:first-child，:last-child是有区别的。</p>
<h3 data-id="heading-22">选择每第n个子元素</h3>
<p>:nth-child(n),nth-last-child(n),n为自然数，从0开始，也可以为特定的数字，选择到的这个元素是父元素中的第n个元素。</p>
<h3 data-id="heading-23">选择每第n个某种元素</h3>
<p>:nth-of-type(n),nth-last-of-type(n).结合上面几种可以很轻松的理解，所以就不多说了。</p>
<h2 data-id="heading-24">动态伪类</h2>
<p>主要是在页面渲染之后根据页面的变化而变化。主要是以a链接为主</p>
<h3 data-id="heading-25">超链接伪类</h3>
<p>a:link 表示为访问状态,a:visited表示已访问状态。</p>
<h3 data-id="heading-26">UI状态伪类</h3>





























































<table><thead><tr><th>伪类</th><th>说明</th></tr></thead><tbody><tr><td>:enabled</td><td>指代启用的用户界面元素（例如表单元素），即接受输入的元素</td></tr><tr><td>:disabled</td><td>指代禁用的用户界面元素（例如表单元素），即不接受输入的元素</td></tr><tr><td>:checked</td><td>指代由用户或者文档默认选中的单选按钮或复选框</td></tr><tr><td>:indeterminate</td><td>指代即未选中也没有未选中的单选按钮或复选框，这个状态只能由DOM脚本控制</td></tr><tr><td>:default</td><td>指代默认选中的单选按钮或复选框、选项</td></tr><tr><td>:valid</td><td>指代满足所有数据有效性语义的输入框</td></tr><tr><td>:invalid</td><td>指代不满足所有数据有效性语义的输入框</td></tr><tr><td>:in-range</td><td>指代输入的值在最小值和最大值之间的输入框</td></tr><tr><td>:out-of-range</td><td>指代输入的值在空间允许的最小值和最大值之外的输入框</td></tr><tr><td>:required</td><td>指代必须输入值的输入框</td></tr><tr><td>:optional</td><td>指代无需输入值的输入框</td></tr><tr><td>:read-write</td><td>指代可由用户编辑的输入框</td></tr><tr><td>:read-only</td><td>指代不能由用户输入的输入框</td></tr></tbody></table>
<h2 data-id="heading-27">否定伪类</h2>
<p>也就是选择不满足条件的元素。选择符:not(条件)</p>
<h1 data-id="heading-28">伪元素选择符</h1>
<p>伪元素和伪类很像。都是实现特定的效果。它在文档中插入虚构的元素，用::加伪元素</p>
<h2 data-id="heading-29">装饰首字母</h2>
<p>::first-letter伪元素用于装饰任何非行内元素的首字母，或者是开头的标点符号。</p>
<h2 data-id="heading-30">装饰首行</h2>
<p>::first-line，用于装饰元素的首行文本</p>
<h2 data-id="heading-31">创建前置和后置内容元素</h2>
<p>::before,前置元素，::after，后置元素。这两个伪类元素的作用非常大，用的非常多。</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
        <span class="hljs-selector-tag">div</span><span class="hljs-selector-pseudo">::before</span> &#123;
            <span class="hljs-attribute">content</span>: <span class="hljs-string">"hello World"</span>;
            <span class="hljs-attribute">display</span>: block;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>

    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这是在div中最前面插入before元素。before元素默认是行内元素。</p>
<p>今天的文章就写到这里了。基本是把css中的所有选择器都讲完了。第一次写文章肯定写的不好，有什么错误可以提点以下，谢谢。我也是正在学习前端中。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            