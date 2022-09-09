
---
title: 'HTML+CSS+JS实现好看的风车屋'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d059235143dd4a11921b10793b533c3e~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Thu, 08 Sep 2022 22:25:21 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d059235143dd4a11921b10793b533c3e~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:30px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:60px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:24px 0 12px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li::marker,.markdown-body ul li::marker&#123;color:#a862ea&#125;.markdown-body ol li.task-list-item,.markdown-body ul li.task-list-item&#123;list-style:none&#125;.markdown-body ol li.task-list-item ol,.markdown-body ol li.task-list-item ul,.markdown-body ul li.task-list-item ol,.markdown-body ul li.task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body a,.markdown-body code,.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6,.markdown-body li,.markdown-body p&#123;opacity:.85;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body a:hover,.markdown-body code:hover,.markdown-body h1:hover,.markdown-body h2:hover,.markdown-body h3:hover,.markdown-body h4:hover,.markdown-body h5:hover,.markdown-body h6:hover,.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:1px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;transition:transform .2s ease 0s;background-color:#f8f5ff;box-shadow:0 0 10px #e7daff&#125;.markdown-body img:hover&#123;opacity:1;box-shadow:0 0 20px #e7daff;transform:translateY(-1px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:12px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:3px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body .math&#123;font-style:italic;margin:12px 0;padding:.5em 1em;background-color:#f8f5ff&#125;.markdown-body .math>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:18px;color:#383838;border-radius:2px;scroll-behavior:smooth;box-shadow:0 0 10px #e7daff&#125;.markdown-body pre>code:hover&#123;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;width:100%;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:.5em;border:1px solid #e7daff&#125;.markdown-body tr&#123;background-color:#f8f5ff&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>我正在参加「码上掘金挑战赛」详情请看：<a href="https://juejin.cn/post/7139728821862793223" title="https://juejin.cn/post/7139728821862793223" target="_blank">码上掘金挑战赛来了！</a></p>
<p>先来一睹为快最终的效果吧！如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d059235143dd4a11921b10793b533c3e~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="64d9b62cbf854548b87c31d89a3c4639.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>看到图，我们思路其实就很明确了，仅用css以及一些动画，就可以实现。大致就是先设置一个relative的视窗，然后里面的元素用absolute定位来画。圆形的大月亮，梯形带三角屋顶的风车房，利用transform: rotate(360deg)来旋转的风车骨架，天上随机改变opacity的闪烁的星星，box-shadow来形成灯光效果的门窗，以及translateX划过天空的流星。</p>
<p>是不是很简单，一副很美妙的图画，其实用到的都是我们耳熟能详的css属性。</p>
<p>这里我们略过最简单的月亮和圆形外框，先来说说天上闪烁的星星：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> fragment = <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">createDocumentFragment</span>();
      <span class="hljs-comment">// 创建30颗星星</span>
      <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < <span class="hljs-number">30</span>; i++) &#123;
        <span class="hljs-comment">// 生成随机位置</span>
        <span class="hljs-keyword">let</span> child = <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">createElement</span>(<span class="hljs-string">"div"</span>);
        child.<span class="hljs-property">className</span> = <span class="hljs-string">"star star-"</span> + (i + <span class="hljs-number">1</span>);
        child.<span class="hljs-property">style</span> = <span class="hljs-string">`left:<span class="hljs-subst">$&#123;randomNum(<span class="hljs-number">40</span>, <span class="hljs-number">300</span>)&#125;</span>px;top:<span class="hljs-subst">$&#123;randomNum(
          <span class="hljs-number">40</span>,
          <span class="hljs-number">200</span>
        )&#125;</span>px;`</span>;
        child.<span class="hljs-property">style</span>.<span class="hljs-title function_">setProperty</span>(<span class="hljs-string">"animation-duration"</span>, <span class="hljs-title function_">randomNum</span>(<span class="hljs-number">2</span>, <span class="hljs-number">5</span>) + <span class="hljs-string">"s"</span>);
        fragment.<span class="hljs-title function_">appendChild</span>(child);
      &#125;
      <span class="hljs-variable language_">document</span>.<span class="hljs-title function_">getElementById</span>(<span class="hljs-string">"stars"</span>).<span class="hljs-title function_">appendChild</span>(fragment);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>首先通过js来随机生成了30颗星星的位置，然后通过奇偶数赋予不同的闪烁时间，让它们模拟出天上真正繁星闪烁的样子。</p>
<pre><code class="hljs language-css copyable" lang="css">      <span class="hljs-comment">/* 星星 */</span>
      <span class="hljs-selector-class">.star</span> &#123;
        <span class="hljs-attribute">background</span>: white;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">2px</span>;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">2px</span>;
        <span class="hljs-attribute">position</span>: absolute;
        <span class="hljs-attribute">left</span>: <span class="hljs-number">100px</span>;
        <span class="hljs-attribute">top</span>: <span class="hljs-number">20px</span>;
        <span class="hljs-attribute">border-radius</span>: <span class="hljs-number">25%</span>;
        <span class="hljs-attribute">opacity</span>: <span class="hljs-number">0.5</span>;
      &#125;
      <span class="hljs-keyword">@keyframes</span> starOdd &#123;
        <span class="hljs-number">10%</span> &#123;
          <span class="hljs-attribute">opacity</span>: <span class="hljs-number">0.3</span>;
        &#125;
 
        <span class="hljs-number">90%</span> &#123;
          <span class="hljs-attribute">opacity</span>: <span class="hljs-number">0.7</span>;
        &#125;
      &#125;
      <span class="hljs-keyword">@keyframes</span> starEven &#123;
        <span class="hljs-number">10%</span> &#123;
          <span class="hljs-attribute">opacity</span>: <span class="hljs-number">0.1</span>;
        &#125;
 
        <span class="hljs-number">90%</span> &#123;
          <span class="hljs-attribute">opacity</span>: <span class="hljs-number">0.8</span>;
        &#125;
      &#125;
      <span class="hljs-selector-class">.star</span><span class="hljs-selector-pseudo">:nth-child</span>(odd) &#123;
        <span class="hljs-attribute">animation</span>: starOdd <span class="hljs-number">2.5s</span> ease-in infinite;
      &#125;
      <span class="hljs-selector-class">.star</span><span class="hljs-selector-pseudo">:nth-child</span>(even) &#123;
        <span class="hljs-attribute">animation</span>: starEven <span class="hljs-number">2.5s</span> ease-in infinite;
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>风车的骨架思路其实就像画画一样，长方形的主骨架，然后是一个个间隔开的横梁。只需要画出一个，剩下三个利用rotate旋转90、180、270度就行了：</p>
<pre><code class="hljs language-css copyable" lang="css">   <span class="hljs-selector-class">.fan-wing</span> &#123;
        <span class="hljs-attribute">width</span>: <span class="hljs-number">89px</span>;
        <span class="hljs-attribute">height</span>: <span class="hljs-number">16px</span>;
        <span class="hljs-attribute">border-bottom</span>: <span class="hljs-number">8px</span> solid <span class="hljs-number">#292f4c</span>;
        <span class="hljs-attribute">position</span>: relative;
        <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
        <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
      &#125;
      <span class="hljs-selector-class">.fan-1</span> &#123;
        <span class="hljs-attribute">left</span>: <span class="hljs-number">0</span>;
      &#125;
      <span class="hljs-selector-class">.fan-2</span> &#123;
        <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">90deg</span>);
        <span class="hljs-attribute">transform-origin</span>: <span class="hljs-number">102px</span> <span class="hljs-number">7px</span>;
      &#125;
      <span class="hljs-selector-class">.fan-3</span> &#123;
        <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">180deg</span>);
        <span class="hljs-attribute">transform-origin</span>: <span class="hljs-number">90px</span> -<span class="hljs-number">4px</span>;
      &#125;
      <span class="hljs-selector-class">.fan-4</span> &#123;
        <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">rotate</span>(<span class="hljs-number">270deg</span>);
        <span class="hljs-attribute">transform-origin</span>: <span class="hljs-number">52px</span> -<span class="hljs-number">17px</span>;
      &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其他的细节看看代码就行：
<span href="https://code.juejin.cn/pen/7141195748044963852" target="_blank" class="code-editor-container"><iframe class="code-editor-frame" data-code="code-editor-element" data-code-id="7141195748044963852" data-src="https://code.juejin.cn/pen/7141195748044963852" style="display: none" loading="lazy"></iframe></span></p>
<p>中秋快到了，祝大家佳节快乐哦~</p></div>  
</div>
            