
---
title: '边框0.5px和解决1px的问题'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9891'
author: 掘金
comments: false
date: Mon, 16 Aug 2021 14:39:21 GMT
thumbnail: 'https://picsum.photos/400/300?random=9891'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>工作中遇到了一个产品需求，要求把列表分割线改成0.5px，直接写成border：0.5px solid #cccccc;是不符合规范的写法，会存在Android和IOS手机上的兼容问题，故，我们可以利用CSS3的transform特性，放缩边框宽度来实现这一效果。</p>
<pre><code class="hljs language-HTML copyable" lang="HTML"><span class="hljs-tag"><<span class="hljs-name">ul</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"mBasicBorder_box"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"mBasicBorder_scale_border"</span>></span>边框宽度0.5px<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"mBasicBorder_scale_border"</span>></span>边框宽度0.5px<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"mBasicBorder_scale_border"</span>></span>边框宽度0.5px<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">li</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"mBasicBorder_scale_border"</span>></span>边框宽度0.5px<span class="hljs-tag"></<span class="hljs-name">li</span>></span>
<span class="hljs-tag"></<span class="hljs-name">ul</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.mBasicBorder_box</span>&#123;
    <span class="hljs-attribute">padding</span>:<span class="hljs-number">15px</span>;
    <span class="hljs-attribute">max-width</span>: <span class="hljs-number">640px</span>;
    <span class="hljs-attribute">margin</span>: <span class="hljs-number">0</span> auto;
&#125;
<span class="hljs-selector-class">.mBasicBorder_scale_border</span>&#123;
    <span class="hljs-attribute">width</span>:<span class="hljs-number">100%</span>;
    <span class="hljs-attribute">height</span>:<span class="hljs-number">50px</span>;
    <span class="hljs-attribute">line-height</span>: <span class="hljs-number">50px</span>;
    <span class="hljs-attribute">position</span>: relative;
&#125;
<span class="hljs-selector-class">.mBasicBorder_scale_border</span>:after&#123;
    content: <span class="hljs-string">''</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">1px</span>;  //控制边框宽度
    <span class="hljs-attribute">width</span>: <span class="hljs-number">200%</span>;  //控制边框长度
    <span class="hljs-attribute">position</span>: absolute;
    <span class="hljs-attribute">left</span>: <span class="hljs-number">0px</span>;
    <span class="hljs-attribute">top</span>: auto;
    <span class="hljs-attribute">right</span>: auto;
    <span class="hljs-attribute">bottom</span>: <span class="hljs-number">0px</span>;
    <span class="hljs-attribute">background-color</span>: <span class="hljs-number">#eeeeee</span>;
    <span class="hljs-attribute">border</span>: <span class="hljs-number">0px</span> solid transparent;
    <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">0px</span>;
    -webkit-<span class="hljs-attribute">border-radius</span>: <span class="hljs-number">0px</span>;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scale</span>(<span class="hljs-number">0.5</span>);  //缩放宽度，达到<span class="hljs-number">0.5px</span>的效果
    -webkit-<span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scale</span>(<span class="hljs-number">0.5</span>);
    -moz-<span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scale</span>(<span class="hljs-number">0.5</span>);
    -ms-<span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scale</span>(<span class="hljs-number">0.5</span>);
    -o-<span class="hljs-attribute">transform</span>: <span class="hljs-built_in">scale</span>(<span class="hljs-number">0.5</span>);
    <span class="hljs-attribute">transform-origin</span>: top left;  //定义缩放基点
    -webkit-<span class="hljs-attribute">transform-origin</span>: top left;
    -moz-<span class="hljs-attribute">transform-origin</span>: top left;
    -ms-<span class="hljs-attribute">transform-origin</span>: top left;
    -o-<span class="hljs-attribute">transform-origin</span>: top left;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>把对应的class名写到需要添加边框的元素上。按需添加</p>
<pre><code class="copyable">h1 &#123;
  position: relative;
&#125;

h1:after &#123;
  content: '';
  display: block;
  width: 100%;
  height: 1px;
  position: absolute;
  left: 0;
  bottom: 0;
  background: red;
  transform: scaleY(1);
  transform-origin: 0 0;
&#125;

@media screen and (min-device-pixel-ratio: 2),
(-webkit-min-device-pixel-ratio: 2) &#123;
  h1:after &#123;
    transform: scaleY(0.5);
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            