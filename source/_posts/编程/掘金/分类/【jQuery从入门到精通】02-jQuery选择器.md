
---
title: '【jQuery从入门到精通】02-jQuery选择器'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/981c2bed242e40ba981cf164fe1a1c68~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 29 Aug 2021 00:05:48 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/981c2bed242e40ba981cf164fe1a1c68~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>@charset "UTF-8";@keyframes spin&#123;0%&#123;transform:rotate(0)&#125;to&#123;transform:rotate(1turn)&#125;&#125;.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#36ace1;background-image:linear-gradient(90deg,rgba(217,234,251,.25) 3%,transparent 0),linear-gradient(1turn,rgba(217,234,251,.25) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;color:#36ace1&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"";display:block;position:absolute;left:0;top:0;bottom:0;margin:auto;background-image:url(data:image/png;base64,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);animation:spin 2s linear 1s infinite&#125;.markdown-body h1&#123;position:relative;font-size:30px;padding:12px 38px;margin:30px 0&#125;.markdown-body h1:before&#123;width:30px;height:30px;background-size:30px 30px&#125;.markdown-body h2&#123;position:relative;font-size:24px;padding:12px 36px;margin:28px 0&#125;.markdown-body h2:before&#123;width:28px;height:28px;background-size:28px 28px&#125;.markdown-body h3&#123;position:relative;font-size:18px;padding:4px 32px;margin:26px 0&#125;.markdown-body h3:before&#123;width:24px;height:24px;background-size:24px 24px&#125;.markdown-body h4&#123;position:relative;padding:4px 28px;font-size:16px;margin:22px 0&#125;.markdown-body h4:before&#123;width:20px;height:20px;background-size:20px 20px&#125;.markdown-body h5&#123;position:relative;padding:4px 26px;font-size:15px;margin:20px 0&#125;.markdown-body h5:before&#123;width:18px;height:18px;background-size:18px 18px&#125;.markdown-body h6&#123;position:relative;padding:4px 22px;font-size:14px;margin:16px 0&#125;.markdown-body h6:before&#123;width:16px;height:16px;background-size:16px 16px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;border:none;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#36ace1,#dff0fe,#36ace1);overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:50px;height:24px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAAEgElEQVRIS72Va0xbZRjH/z2FcimbchEQFDYRCIRAAWFQ2MaCXBwmUxYDLGGEcRFkH9wmk04zG0Bo2dwNIisERANqhjqdEmhd4nRbuwpsXDYWLLoRgeG4Chu9QHvMOQ0dpTAKH3y/tDnv8/5/z/Oc//scBv6nxdgoJ14gVYPEuITHdTdHY12gRIH0T0KljlqwthqUFHGtzAEsxqwLtPvkdc+FeeI3BgMeAMEhdOqR1mM7xswBrgmKE8pfIUhtm7fbZsft/i7wc98MtrUFxmbU6ByYgFwxjtFp5Q+WpF1mCy9wajXoqqD4E91saOf603e+5B7t99xTkyZJEiKJAl2DE9Xio1HvrBS8IuhVwVUP503swdJ9QWAw1izaoDs6pQT/655BMS9yy3KYiUoM/7adu7NmtnQfx5zWm8Q8Ui3gyGcddyU8rv/STRNQouDGP5/mhTubX4dpPv3DMzh1qS9LwuPWr+i63WVyn5QYj/4d/i4bqmbpoQ+auvBlQYghX6PE4wTSOzV5EUYlb5Q4MDqLk9/3cMRF27spDSNQamUnWZ4ebNB+OKNCyYVeFCZ5wZ5tiePN/UiP2YoQL0cUX+iFt4sNUiLdcaVvHJLecQiWnKVE8s5LvxAXRWeYgHLre0hecgAN0sxr0XBZgbJUP6OiLnaM4ivZCBrzOWBZEIY9rY5E8pl2nM0KMzzLq5aPiXmRzgbQm2VyR8KGGK/ICAFB6IusbvsDwhRf+n/jtSHc/nsGgjR9V6/1TyLa1wGU+FtnO1CbHQTHTSzIFJOYJ1jwcGLTccMTcyhp7oW4KFJ/SV4/IScrc55kQj07WNuOn94Lpw8kCm/Qv3W5HLjbWxsyfuNUO1TzWjAJBloKt2FBS+Jz6ShiA12NupBdLWugQcmn28lPMkONNql3U5cTSD9Lq+qEUqPFt++G0aKL687wDAqb+pAU7IKCuK2493AOPQ9UCNpib6T1tkg+RZ9KKJcNn8sJc1vac8o16jklLWLuOiDqwvHUIKPw7vtTON+iCDKkl/Cx9FeSYET5um1mHt6jN0Dz9ftwYjORudNjTdaBmi7kxvvA1d6Gjs0X/Q5Sp3tMEMSHre9HnDEZAPFCWUNVdliGJVPvqEP1Hbh4yPj9LadSY6fu6gPsCX+B3mq7NYLv2od8fj4aoViMNQGFijos/XVMTXGavgUisQIle71hwVx9KFEutLVjw8GORTuxoEbeJS7iPrmQyy/sIj2hQpqYHO7ZGs95nnZS4y8K8Pfqrb58UZ+IlKqbqNgfQm8da+pC9xjLqo8foFkau2qaCeXSyvzXfA9SDrp1bxJ/DU/jSJKXEWdBR2J/9U0UpwXTFZ/+8S76h/71FvO4A8sTeuqQThDKalOiPLN3BbhiYlaNsm964elkCztrC4xMqeDqYIus2JdB3cbS5l4MTag44qJt9GxbF4gKThRKY59lW13+KCUQ1pZMEwHKviKx4pFSqXzxCn/X9Gr2NO+zw+cTiTbxmUyCqH3GlsWg2kRNhOnHmhlrFkIvHTZt1borWvMCmRnwH4usn58STiycAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body del&#123;color:#36ace1&#125;.markdown-body code&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#282c34;color:#4ec9b0;padding:.24em .46em;margin:0 4px&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;font-size:12px;border-radius:10px;padding:15px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#4ec9b0;background:#282c34&#125;.markdown-body a&#123;text-decoration:none;color:#409eff;border-bottom:1px solid #409eff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#007bff;border-bottom:1px solid #007bff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;position:relative;padding:8px 26px;background-color:rgba(54,172,225,.75);margin:16px 0;border-left:4px solid #409eff;border-radius:5px&#125;.markdown-body blockquote:before&#123;content:"❝";top:10px;left:8px;color:#409eff;font-size:20px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:20px;position:absolute;right:8px;bottom:0;color:#409eff;opacity:.7&#125;.markdown-body blockquote>p&#123;color:#fff&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>笔记来源：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1ts411E7ag" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1ts411E7ag" ref="nofollow noopener noreferrer">尚硅谷jQuery教程(jquery从入门到精通)</a></p>
</blockquote>
<p>[TOC]</p>
<h1 data-id="heading-0">jQuery 选择器</h1>
<h2 data-id="heading-1">1、选择器</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/981c2bed242e40ba981cf164fe1a1c68~tplv-k3u1fbpfcp-watermark.image" alt="image-20210828192208382" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-2">说明</h3>
<p>选择器是<code>jQuery</code>学习的重中之重，也就是对<code>jQuery</code>核心函数的使用</p>
<ul>
<li>选择器本身只是一个有特定语法规则的字符串，没有实质用处</li>
<li>它的基本语法规则使用的就是 CSS 的选择器语法，并对基进行了扩展</li>
<li>只有调用<code>$()</code>，并将选择器作为参数传入才能起作用</li>
<li><code>$(selector)</code>作用：根据选择器规则在整个文档中查找所有匹配的标签的数组（伪数组），并封装成<code>jQuery</code>对象</li>
</ul>
<h3 data-id="heading-3">分类</h3>
<h4 data-id="heading-4">基本选择器</h4>
<ul>
<li>ID 选择器：<code>#id</code></li>
<li>标签选择器：<code>element</code></li>
<li>属性选择器：<code>.class</code></li>
<li>通用选择器：<code>*</code></li>
<li>并集选择器：<code>selector1,selector2,selectorN</code></li>
<li>交集选择器：<code>selector1selector2selectorN</code></li>
</ul>
<h4 data-id="heading-5">层次选择器</h4>
<ul>
<li>后代元素选择器：<code>ancestor descendant</code></li>
<li>子元素选择器：<code>parent > child</code></li>
<li>兄弟选择器：<code>prev + next</code>、<code>prev ~ siblings</code></li>
</ul>
<h4 data-id="heading-6">过滤选择器</h4>
<p>在原有选择器匹配的元素中进一步进行过滤的选择器</p>
<p>选择器语法中大部分是过滤选择器</p>
<ul>
<li>基本</li>
<li>内容</li>
<li>可见性</li>
<li>属性</li>
</ul>
<h4 data-id="heading-7">表单选择器</h4>
<ul>
<li>表单</li>
<li>表单对象属性</li>
</ul>
<p>下面，我们对其中 <em>常用的选择器</em> 进行一一学习</p>
<h2 data-id="heading-8">2、基本选择器</h2>





























<table><thead><tr><th align="left">基本选择器</th><th align="left">描述</th></tr></thead><tbody><tr><td align="left"><code>#id</code></td><td align="left">根据给定的ID匹配一个元素</td></tr><tr><td align="left"><code>element</code></td><td align="left">根据给定的元素名匹配所有元素</td></tr><tr><td align="left"><code>.class</code></td><td align="left">根据给定的类匹配元素</td></tr><tr><td align="left"><code>*</code></td><td align="left">匹配所有元素</td></tr><tr><td align="left"><code>selector1,selector2,selectorN</code></td><td align="left">将每一个选择器匹配到的元素合并后一起返回</td></tr></tbody></table>
<p>HTML 代码</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"div1"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>div1(class="box")<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"div2"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>div2(class="box")<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"div3"</span>></span>div3<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>span(class="box")<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"><<span class="hljs-name">br</span>></span>
<span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>AAAAA<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"hello"</span>></span>BBBBB(title="hello")<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>CCCCC(class="box")<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"hello"</span>></span>DDDDDD(title="hello")<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">ID 选择器</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 1.选择id为div1的元素</span>
$(<span class="hljs-string">'#div1'</span>).css(<span class="hljs-string">'background-color'</span>, <span class="hljs-string">'red'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/52ecfc76896943f3b3c5f529fe5a647f~tplv-k3u1fbpfcp-watermark.image" alt="image-20210828195718252" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">标签选择器</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 2.选择所有的div元素</span>
$(<span class="hljs-string">'div'</span>).css(<span class="hljs-string">'background-color'</span>, <span class="hljs-string">'red'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9cd6db640ab749849f87ca289706ae1f~tplv-k3u1fbpfcp-watermark.image" alt="image-20210828195737043" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-11">属性选择器</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 3.选择所有class属性为box的元素</span>
$(<span class="hljs-string">'.box'</span>).css(<span class="hljs-string">'background-color'</span>, <span class="hljs-string">'red'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26696ce65cd047ae939ab3e487cc5580~tplv-k3u1fbpfcp-watermark.image" alt="image-20210828195757323" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">并集选择器</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 4.选择所有的div和span元素</span>
$(<span class="hljs-string">'div,span'</span>).css(<span class="hljs-string">'background-color'</span>, <span class="hljs-string">'red'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3795b41466d54903a74f3e63025dc7aa~tplv-k3u1fbpfcp-watermark.image" alt="image-20210828195819970" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-13">交集选择器</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 5.选择所有class属性为box的div元素</span>
$(<span class="hljs-string">'div.box'</span>).css(<span class="hljs-string">'background-color'</span>, <span class="hljs-string">'red'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d49a77f754fa4beea7dea0d6a66d9224~tplv-k3u1fbpfcp-watermark.image" alt="image-20210828195847762" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14">通用选择器</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 6.选择所有元素</span>
$(<span class="hljs-string">'*'</span>).css(<span class="hljs-string">'background-color'</span>, <span class="hljs-string">'red'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c19b619d1a0544069b21084ab2007700~tplv-k3u1fbpfcp-watermark.image" alt="image-20210828195909083" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-15">3、层级选择器</h2>
<p>查找子元素，后代元素，兄弟元素的选择器</p>

























<table><thead><tr><th align="left">层级选择器</th><th align="left">描述</th></tr></thead><tbody><tr><td align="left"><code>ancestor descendant</code></td><td align="left">在给定的祖先元素下匹配所有的后代元素</td></tr><tr><td align="left"><code>parent > child</code></td><td align="left">在给定的父元素下匹配所有的子元素</td></tr><tr><td align="left"><code>prev + next</code></td><td align="left">匹配所有紧接在 prev 元素后的 next 元素</td></tr><tr><td align="left"><code>prev ~ siblings</code></td><td align="left">匹配 prev 元素之后的所有 siblings 元素</td></tr></tbody></table>
<p>HTML 代码</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span>></span>AAAAA<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>CCCCC<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"hello"</span>></span><span class="hljs-tag"><<span class="hljs-name">span</span>></span>BBBBB<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"hello"</span>></span><span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>DDDD<span class="hljs-tag"></<span class="hljs-name">span</span>></span><span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"><<span class="hljs-name">span</span>></span>EEEEE<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-16">后代元素选择器</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 1.选中ul下所有的span</span>
$(<span class="hljs-string">'ul span'</span>).css(<span class="hljs-string">'background'</span>, <span class="hljs-string">'red'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f64100290607403fab814f0b6adec57c~tplv-k3u1fbpfcp-watermark.image" alt="image-20210828200701777" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-17">子元素选择器</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 2.选中ul下所有的子元素span</span>
$(<span class="hljs-string">'ul > span'</span>).css(<span class="hljs-string">'background'</span>, <span class="hljs-string">'red'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3fa39f51e66c4894b9849c925adf5a24~tplv-k3u1fbpfcp-watermark.image" alt="image-20210828200751616" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-18">兄弟选择器</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 3.选中class为box的下一个li</span>
$(<span class="hljs-string">'.box + li'</span>).css(<span class="hljs-string">'background'</span>, <span class="hljs-string">'red'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d71da0ca88644421855a1876a213d1a3~tplv-k3u1fbpfcp-watermark.image" alt="image-20210828200849768" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 4.选中ul下li的class为box的元素后面的所有兄弟元素</span>
$(<span class="hljs-string">'ul .box ~ *'</span>).css(<span class="hljs-string">'background'</span>, <span class="hljs-string">'red'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8c79520ed8b9436199c86cb8df9d32ae~tplv-k3u1fbpfcp-watermark.image" alt="image-20210828201744815" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-19">4、过滤选择器</h2>
<p>在原有选择器匹配的元素中进行进一步过滤的选择器</p>









































































































<table><thead><tr><th align="left">分类</th><th align="left">过滤选择器</th><th align="left">描述</th></tr></thead><tbody><tr><td align="left">基本</td><td align="left"><code>:first</code></td><td align="left">获取第一个元素</td></tr><tr><td align="left"></td><td align="left"><code>:last</code></td><td align="left">获取最后一个元素</td></tr><tr><td align="left"></td><td align="left"><code>:eq(index)</code></td><td align="left">匹配一个给定索引值的元素</td></tr><tr><td align="left"></td><td align="left"><code>:gt(index)</code></td><td align="left">匹配所有大于给定索引值的元素</td></tr><tr><td align="left"></td><td align="left"><code>:lt(index)</code></td><td align="left">匹配所有小于给定索引值的元素</td></tr><tr><td align="left"></td><td align="left"><code>:even</code></td><td align="left">匹配所有索引值为偶数的元素，从 0 开始计数</td></tr><tr><td align="left"></td><td align="left"><code>:odd</code></td><td align="left">匹配所有索引值为奇数的元素，从 0 开始计数</td></tr><tr><td align="left"></td><td align="left"><code>:not(selector)</code></td><td align="left">去除所有与给定选择器匹配的元素</td></tr><tr><td align="left">内容</td><td align="left"><code>:contains(text)</code></td><td align="left">匹配包含给定文本的元素</td></tr><tr><td align="left"></td><td align="left"><code>:has(selector)</code></td><td align="left">匹配含有选择器所匹配的元素的元素</td></tr><tr><td align="left"></td><td align="left"><code>:empty</code></td><td align="left">匹配所有不包含子元素或者文本的空元素</td></tr><tr><td align="left"></td><td align="left"><code>:parent</code></td><td align="left">匹配含有子元素或者文本的元素</td></tr><tr><td align="left">可见性</td><td align="left"><code>:hidden</code></td><td align="left">匹配所有不可见元素，或者type为hidden的元素</td></tr><tr><td align="left"></td><td align="left"><code>:visible</code></td><td align="left">匹配所有的可见元素</td></tr><tr><td align="left">属性</td><td align="left"><code>[attribute]</code></td><td align="left">匹配包含给定属性的元素</td></tr><tr><td align="left"></td><td align="left"><code>[attribute=value]</code></td><td align="left">匹配给定的属性是某个特定值的元素</td></tr><tr><td align="left"></td><td align="left"><code>[attribute!=value]</code></td><td align="left">匹配所有不含有指定的属性，或者属性不等于特定值的元素</td></tr><tr><td align="left"></td><td align="left"><code>[attribute*=value]</code></td><td align="left">匹配给定的属性是以包含某些值的元素</td></tr><tr><td align="left"></td><td align="left"><code>[selector1][selector2][selectorN]</code></td><td align="left">复合属性选择器，需要同时满足多个条件时使用</td></tr></tbody></table>
<p>HTML 代码</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"div1"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>class为box的div1<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"div2"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>class为box的div2<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"div3"</span>></span>div3<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">span</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>class为box的span<span class="hljs-tag"></<span class="hljs-name">span</span>></span>
<span class="hljs-tag"><<span class="hljs-name">br</span>/></span>
<span class="hljs-tag"><<span class="hljs-name">ul</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span>></span>AAAAA<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"hello"</span>></span>BBBBB<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"box"</span>></span>CCCCC<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"hello"</span>></span>DDDDDD<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">title</span>=<span class="hljs-string">"two"</span>></span>BBBBB<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"display: none"</span>></span>我本来是隐藏的<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-20">:first</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 1.选择第一个div</span>
$(<span class="hljs-string">'div:first'</span>).css(<span class="hljs-string">'background'</span>, <span class="hljs-string">'red'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/25e8832a9196497690116100b070c6ea~tplv-k3u1fbpfcp-watermark.image" alt="image-20210828202449696" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-21">:last</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 2.选择最后一个class为box的元素</span>
$(<span class="hljs-string">'.box:last'</span>).css(<span class="hljs-string">'background'</span>, <span class="hljs-string">'red'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e1b604a54684f4ba47398a878a5aed7~tplv-k3u1fbpfcp-watermark.image" alt="image-20210828202621705" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-22">:not</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 3.选择所有class属性不为box的div</span>
$(<span class="hljs-string">'div:not(.box)'</span>).css(<span class="hljs-string">'background'</span>, <span class="hljs-string">'red'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/616d826102c04606b971ffba49ed997d~tplv-k3u1fbpfcp-watermark.image" alt="image-20210828202755645" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-23">:eq、:gt、:lt</h3>
<p>多个选择器是依次执行的，不是同时执行的</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 4.选择第二个和第三个li元素</span>
<span class="hljs-comment">// $('li:eq(1),li:eq(2)').css('background', 'red');</span>
<span class="hljs-comment">// $('li:gt(0):lt(2)').css('background', 'red');</span>
$(<span class="hljs-string">'li:lt(3):gt(0)'</span>).css(<span class="hljs-string">'background'</span>, <span class="hljs-string">'red'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/526eedb55b894d7aad123aa7fc7cfc1b~tplv-k3u1fbpfcp-watermark.image" alt="image-20210828202909014" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-24">:contains</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 5.选择内容为BBBBB的li</span>
$(<span class="hljs-string">'li:contains("BBBBB")'</span>).css(<span class="hljs-string">'background'</span>, <span class="hljs-string">'red'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b4e14de5dee4450824746965ae3293c~tplv-k3u1fbpfcp-watermark.image" alt="image-20210828203616059" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-25">:hidden</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 6.选择隐藏的li</span>
$(<span class="hljs-string">'li:hidden'</span>).show().css(<span class="hljs-string">'background'</span>, <span class="hljs-string">'red'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1571b020bc8e4dcc8d914322961dd78a~tplv-k3u1fbpfcp-watermark.image" alt="image-20210828203732811" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-26">[attribute]</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 7.送择有title属性的li元素</span>
$(<span class="hljs-string">'li[title]'</span>).css(<span class="hljs-string">'background'</span>, <span class="hljs-string">'red'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c524e53198f499090a8fe65e94d6c77~tplv-k3u1fbpfcp-watermark.image" alt="image-20210828203858256" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-27">[attribute=value]</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 8.选择所有属性title为hello的li元素</span>
$(<span class="hljs-string">'li[title=hello]'</span>).css(<span class="hljs-string">'background'</span>, <span class="hljs-string">'red'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4003c4876aaf40cfb3842634d1224de6~tplv-k3u1fbpfcp-watermark.image" alt="image-20210828203937555" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-28">:odd</h3>
<pre><code class="hljs language-js copyable" lang="js">$(<span class="hljs-string">'#data tbody > tr:odd'</span>).css(<span class="hljs-string">'backgroundColor'</span>, <span class="hljs-string">'#ccf'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b232223afc014bce97c5f6e5a08e9a32~tplv-k3u1fbpfcp-watermark.image" alt="image-20210828212102136" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-29">5、表单选择器</h2>
<p>表单和表单对象属性</p>





























































<table><thead><tr><th align="left">表单选择器</th><th align="left">描述</th></tr></thead><tbody><tr><td align="left"><code>:input</code></td><td align="left">匹配所有 input, textarea, select 和 button 元素</td></tr><tr><td align="left"><code>:text</code></td><td align="left">匹配所有的单行文本框</td></tr><tr><td align="left"><code>:password</code></td><td align="left">匹配所有密码框</td></tr><tr><td align="left"><code>:radio</code></td><td align="left">匹配所有单选按钮</td></tr><tr><td align="left"><code>:checkbox</code></td><td align="left">匹配所有复选框</td></tr><tr><td align="left"><code>:submit</code></td><td align="left">匹配所有提交按钮</td></tr><tr><td align="left"><code>:reset</code></td><td align="left">匹配所有重置按钮</td></tr><tr><td align="left"><code>:button</code></td><td align="left">匹配所有按钮</td></tr><tr><td align="left"><strong>表单对象属性</strong></td><td align="left"><strong>描述</strong></td></tr><tr><td align="left"><code>:enabled</code></td><td align="left">匹配所有可用元素</td></tr><tr><td align="left"><code>:disabled</code></td><td align="left">匹配所有不可用元素</td></tr><tr><td align="left"><code>:checked</code></td><td align="left">匹配所有选中的被选中元素(复选框、单选框等，不包括select中的option)</td></tr><tr><td align="left"><code>:selected</code></td><td align="left">匹配所有选中的option元素</td></tr></tbody></table>
<p>HTML代码</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">form</span>></span>
    用户名：<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span>/></span><span class="hljs-tag"><<span class="hljs-name">br</span>></span>
    密码：<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"password"</span>/></span><span class="hljs-tag"><<span class="hljs-name">br</span>></span>
    爱好：
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"checkbox"</span> <span class="hljs-attr">checked</span>=<span class="hljs-string">"checked"</span>/></span>篮球
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"checkbox"</span> <span class="hljs-attr">checked</span>=<span class="hljs-string">"checked"</span>/></span>足球
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"checkbox"</span> <span class="hljs-attr">checked</span>=<span class="hljs-string">"checked"</span>/></span>羽毛球<span class="hljs-tag"><<span class="hljs-name">br</span>></span>
    性别：
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"radio"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"sex"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">'male'</span>/></span>男
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"radio"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"sex"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">'female'</span>/></span>女<span class="hljs-tag"><<span class="hljs-name">br</span>></span>
    邮箱：<span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"email"</span> <span class="hljs-attr">disabled</span>=<span class="hljs-string">"disabled"</span>/></span><span class="hljs-tag"><<span class="hljs-name">br</span>></span>
    所在地：I
    <span class="hljs-tag"><<span class="hljs-name">select</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">option</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"1"</span>></span>北京<span class="hljs-tag"></<span class="hljs-name">option</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">option</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"2"</span> <span class="hljs-attr">selected</span>=<span class="hljs-string">"selected"</span>></span>天津<span class="hljs-tag"></<span class="hljs-name">option</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">option</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"3"</span>></span>河北<span class="hljs-tag"></<span class="hljs-name">option</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">select</span>></span><span class="hljs-tag"><<span class="hljs-name">br</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"submit"</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"提交"</span>/></span>
<span class="hljs-tag"></<span class="hljs-name">form</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-30">:text、:disabled</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 1.选择不可用的文本输入框</span>
$(<span class="hljs-string">':text:disabled'</span>).css(<span class="hljs-string">'background-color'</span>, <span class="hljs-string">'red'</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9664f08d7f54429ba7f9769dc6fcce26~tplv-k3u1fbpfcp-watermark.image" alt="image-20210828215100265" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-31">:submit、:checkbox、:checked</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 3.显示选择的城市名称</span>
$(<span class="hljs-string">':submit'</span>).click(<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
    alert($(<span class="hljs-string">'select>option:selected'</span>).html());
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80682888c8a54f048b4e7406985789da~tplv-k3u1fbpfcp-watermark.image" alt="image-20210828220129756" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            