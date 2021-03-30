
---
title: '纯css实现图片在固定大小下的最大展示--img-fit实现'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6258'
author: 掘金
comments: false
date: Fri, 26 Mar 2021 05:05:38 GMT
thumbnail: 'https://picsum.photos/400/300?random=6258'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>我们经常会有这样一个需求，不可控的图片出现在一个指定方框内的最佳展示</p>
</blockquote>
<p>一般来说我们需要这样做（获取img大小，判断是width还是height比较大，根据比较大的一方设置最大值，其他的设置自适应）</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">AutoStretchBaseWidthOrHeightImg</span> (<span class="hljs-params">&#123; src, width, height &#125;</span>) </span>&#123;
  <span class="hljs-keyword">const</span> [imgWidth, setImgWidth] = useState(<span class="hljs-string">'auto'</span>)
  <span class="hljs-keyword">const</span> [imgHeight, setImgHeight] = useState(<span class="hljs-string">'auto'</span>)
  useEffect(<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> img = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'img'</span>)
    img.src = src
    <span class="hljs-built_in">document</span>.body.appendChild(img)
    <span class="hljs-keyword">const</span> imgRect = img.getBoundingClientRect()
    <span class="hljs-keyword">if</span> (imgRect.width > imgRect.height) &#123;
      setImgWidth(width + <span class="hljs-string">'px'</span>)
    &#125;
    <span class="hljs-keyword">if</span> (imgRect.width <= imgRect.height) &#123;
      setImgHeight(height + <span class="hljs-string">'px'</span>)
    &#125;
    <span class="hljs-built_in">document</span>.body.removeChild(img)
  &#125;, [width, height, src])
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">width:</span> `$&#123;<span class="hljs-attr">width</span>&#125;<span class="hljs-attr">px</span>`, <span class="hljs-attr">height:</span> `$&#123;<span class="hljs-attr">height</span>&#125;<span class="hljs-attr">px</span>` &#125;&#125; <span class="hljs-attr">className</span>=<span class="hljs-string">"flex flex-center-y flex-center-x"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">&#123;src&#125;</span> <span class="hljs-attr">width</span>=<span class="hljs-string">&#123;imgWidth&#125;</span> <span class="hljs-attr">height</span>=<span class="hljs-string">&#123;imgHeight&#125;</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span> /></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是这样会有一个问题，就是需要发起两个请求，这样导致服务器压力增大，或者对象存储多收钱，或者展示慢的问题。</p>
<p>这时候如果不依赖JS，那就很完美，比如<code>backgroundImage</code>实现，实现代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> AutoStretchBaseWidthOrHeightImgStyled = styled.div<span class="hljs-string">`
div&#123;
  background-repeat: no-repeat;
  background-size: contain;
  background-position: center;
&#125;
`</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">AutoStretchBaseWidthOrHeightImg</span> (<span class="hljs-params">&#123; src, width, height &#125;</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">AutoStretchBaseWidthOrHeightImgStyled</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">width:</span> `$&#123;<span class="hljs-attr">width</span>&#125;<span class="hljs-attr">px</span>`, <span class="hljs-attr">height:</span> `$&#123;<span class="hljs-attr">height</span>&#125;<span class="hljs-attr">px</span>`, <span class="hljs-attr">backgroundColor:</span> '<span class="hljs-attr">rgba</span>(<span class="hljs-attr">0</span>,<span class="hljs-attr">0</span>,<span class="hljs-attr">0</span>,<span class="hljs-attr">.03</span>)', <span class="hljs-attr">backgroundImage:</span> `<span class="hljs-attr">url</span>($&#123;<span class="hljs-attr">src</span>&#125;)` &#125;&#125;></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">AutoStretchBaseWidthOrHeightImgStyled</span>></span></span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时候是完成了，但是假如我们需要给图片不展示的时候出现一个默认图，怎么办？<code>backgroundImage</code>可没有<code>img</code>的<code>onError</code>.</p>
<p>于是这时候<code>object-fit</code>出场了</p>
<p><code>object-fit</code>是什么？</p>
<p>MDN这样说的<code>object-fit CSS 属性指定可替换元素的内容应该如何适应到其使用的高度和宽度确定的框</code></p>
<p>我们也不管啥意思，反正可以解决目前问题，具体查看<a href="https://developer.mozilla.org/zh-CN/docs/Web/CSS/object-fit" target="_blank" rel="nofollow noopener noreferrer">MDN objecr-fit</a></p>
<p>于是<code>backgroundImage</code>+<code>object-fit</code>+<code>onError</code> 就可以实现不可控的图片以最合适的位置展示在方框内，并可以设置黑边颜色，并可以设置图片加载异常的展示，下面看下代码吧。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> AutoStretchBaseWidthOrHeightImgStyled = styled.div<span class="hljs-string">`
div&#123;
  background-repeat: no-repeat;
  background-size: 63px;
  background-position: center;
  background-color: rgba(0, 0, 0, 1);
  img&#123;
    background-color: rgb(247, 247, 247);
    object-fit: contain;
  &#125;
&#125;
`</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">AutoStretchBaseWidthOrHeightImg</span> (<span class="hljs-params">&#123; src, width, height &#125;</span>) </span>&#123;
  <span class="hljs-keyword">const</span> [imgShow, setImgShow] = useState(<span class="hljs-literal">true</span>)
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">AutoStretchBaseWidthOrHeightImgStyled</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">width:</span> `$&#123;<span class="hljs-attr">width</span>&#125;<span class="hljs-attr">px</span>`, <span class="hljs-attr">height:</span> `$&#123;<span class="hljs-attr">height</span>&#125;<span class="hljs-attr">px</span>`, <span class="hljs-attr">backgroundImage:</span> `<span class="hljs-attr">url</span>($&#123;<span class="hljs-attr">errorImg</span>&#125;)` &#125;&#125;></span>
      &#123;imgShow && <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">width</span>=<span class="hljs-string">&#123;width&#125;</span> <span class="hljs-attr">height</span>=<span class="hljs-string">&#123;height&#125;</span> <span class="hljs-attr">src</span>=<span class="hljs-string">&#123;src&#125;</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span> <span class="hljs-attr">onError</span>=<span class="hljs-string">&#123;()</span> =></span> setImgShow(false)&#125; />&#125;
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">AutoStretchBaseWidthOrHeightImgStyled</span>></span></span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>--完--</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            