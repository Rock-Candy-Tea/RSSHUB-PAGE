
---
title: 'CSS的值与单位   em、rem详解'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/012a529f4d2b47459cb35e9ff79eae24~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 25 Aug 2021 01:42:00 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/012a529f4d2b47459cb35e9ff79eae24~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>绝对长度单位：</p>
<pre><code class="copyable">常用：px
不常用：cm、mm、in、pc、pt
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相对长度单位：</p>
<pre><code class="copyable">常用：em、rem、vw、vh
不常用：ex、ch、lh、vmin、vmax
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>em:在font-size中使用是相对父元素的字体大小，在其他属性中是相对于自身的字体大小，如width</strong></p>
<p>代码演示：</p>
<pre><code class="copyable"><div class="grand">
    <div class="parent">
        <div class="child"></div>
    </div>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">.grand &#123;
    font-size: 24px;
    width: 10em; /*240px*/
    height: 10em;
    background: #000;
&#125;
.parent &#123;
    font-size: 0.8em; /*19.2px(24x0.8)*/
    width: 5em; /*96px(19.2x5)*/
    height: 5em;
    background: #f00;
&#125;
.child &#123;
    font-size: 0.8em; /*15.36px(19.2x0.8)*/
    width: 4em; /*61.44px(15.36x15.36)*/
    height: 4em;
    background: #0f0;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果如图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/012a529f4d2b47459cb35e9ff79eae24~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可见font-size的单位为em时，只是相对于父级，其他属性则是相对于自身。
但是如果子级不设置font-size时，结果就不是如此了。</p>
<p>代码演示：</p>
<pre><code class="copyable"><div class="grand">
    <div class="parent">
        <div class="child"></div>
    </div>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">.grand &#123;
    font-size: 24px;
    width: 10em; /*240px*/
    height: 10em;
    background: #000;
&#125;
.parent &#123;
    width: 5em; /*120px(24x5)*/
    height: 5em;
    background: #f00;
&#125;
.child &#123;
    width: 4em; /*96px(24x4)*/
    height: 4em;
    background: #0f0;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>结果如图：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/20e606b7c6524cdd876f2508ff00ae1b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>rem:根元素的字体大小，rem中的r意思是root</strong></p>
<p>浏览器的默认字体是16px，1rem。如果某元素的某属性设置为10rem，换算成px就是160px</p>
<p><strong>vw:视窗宽度的1%</strong></p>
<p><strong>vh:视窗高度的1%</strong></p>
<p>height:100vh 理论上等于 height:100%;
但是有个好处是当元素没有内容时候，设置height:100%该元素不会被撑开，但是设置height:100vh，该元素会被撑开屏幕高度一致</p></div>  
</div>
            