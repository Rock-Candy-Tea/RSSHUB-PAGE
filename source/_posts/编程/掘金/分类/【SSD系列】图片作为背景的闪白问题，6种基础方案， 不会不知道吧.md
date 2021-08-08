
---
title: '【SSD系列】图片作为背景的闪白问题，6种基础方案， 不会不知道吧'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a5fc4bbdcc14c45a3323042ba05c041~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 07 Aug 2021 18:48:25 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a5fc4bbdcc14c45a3323042ba05c041~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第8天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a>。</p>
<h2 data-id="heading-0">前言</h2>
<p>关于【SSD系列】：<br>
<strong>前端一些有意思的内容，旨在3-10分钟里， 500-1500字，有所获，又不为所累。</strong></p>
<p>某天，发现有背景图片的弹出框，会出现闪白现象，这，兄弟们，你们说能忍么？</p>
<p>答案：不能！</p>
<h2 data-id="heading-1">思路</h2>
<p>思路嘛，无非三种</p>
<ol>
<li>
<p>弹框时或者显示时，背景图片已经ready</p>
</li>
<li>
<p>背景色或者小图，先顶着，大背景图ready后切换</p>
</li>
<li>
<p>尽可能的快</p>
</li>
</ol>
<p><strong>这里暂且不考虑缓存，因为你无论如何逃不过第一次加载。</strong></p>
<h2 data-id="heading-2">方案</h2>
<p>可以到 <strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fxiangwenhu.github.io%2FTakeItEasy%2FbgWhithe%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://xiangwenhu.github.io/TakeItEasy/bgWhithe/" ref="nofollow noopener noreferrer">背景图片闪现空白解决方案</a></strong> 看到各种方案演示。</p>
<p>为了提升大家兴趣，先看<strong>个png, jpg渐进和png交错的加载效果动图</strong>：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a5fc4bbdcc14c45a3323042ba05c041~tplv-k3u1fbpfcp-watermark.image" alt="jpgpng.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>方便移动端观看，列一个演示清单：</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fxiangwenhu.github.io%2FTakeItEasy%2FbgWhithe%2Fbase64.html" target="_blank" rel="nofollow noopener noreferrer" title="https://xiangwenhu.github.io/TakeItEasy/bgWhithe/base64.html" ref="nofollow noopener noreferrer">背景图片闪现空白方案-base背景图片</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fxiangwenhu.github.io%2FTakeItEasy%2FbgWhithe%2Fprefetch.html" target="_blank" rel="nofollow noopener noreferrer" title="https://xiangwenhu.github.io/TakeItEasy/bgWhithe/prefetch.html" ref="nofollow noopener noreferrer">背景图片闪现空白方案-preferch</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fxiangwenhu.github.io%2FTakeItEasy%2FbgWhithe%2FhideImage.html" target="_blank" rel="nofollow noopener noreferrer" title="https://xiangwenhu.github.io/TakeItEasy/bgWhithe/hideImage.html" ref="nofollow noopener noreferrer">背景图片闪现空白方案-创建隐藏Img节点</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fxiangwenhu.github.io%2FTakeItEasy%2FbgWhithe%2FwaitingImg.html" target="_blank" rel="nofollow noopener noreferrer" title="https://xiangwenhu.github.io/TakeItEasy/bgWhithe/waitingImg.html" ref="nofollow noopener noreferrer">背景图片闪现空白方案-等待图片加载完毕再显示弹框</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fxiangwenhu.github.io%2FTakeItEasy%2FbgWhithe%2FbgColor.html" target="_blank" rel="nofollow noopener noreferrer" title="https://xiangwenhu.github.io/TakeItEasy/bgWhithe/bgColor.html" ref="nofollow noopener noreferrer">背景图片闪现空白方案-同时设置背景颜色和图片</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fxiangwenhu.github.io%2FTakeItEasy%2FbgWhithe%2Fprogress.html" target="_blank" rel="nofollow noopener noreferrer" title="https://xiangwenhu.github.io/TakeItEasy/bgWhithe/progress.html" ref="nofollow noopener noreferrer">png正常，png交错，jpg渐进</a></li>
</ul>
<h3 data-id="heading-3">方案1 base64</h3>
<p>如果背景图片相对小，或者你执意要这嘛做，图片转为bas464，存到css或者html里面。<br>
演示： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fxiangwenhu.github.io%2FTakeItEasy%2FbgWhithe%2Fbase64.html" target="_blank" rel="nofollow noopener noreferrer" title="https://xiangwenhu.github.io/TakeItEasy/bgWhithe/base64.html" ref="nofollow noopener noreferrer">背景图片闪现空白方案-base背景图片</a></p>
<p>不足： base64增加带宽成本，内容会比原本大至少1/3。 至于为什么可参见 <a href="https://juejin.cn/post/6989391487200919566" target="_blank" title="https://juejin.cn/post/6989391487200919566">前端Base64编码知识，一文打尽，探索起源，追求真相。</a></p>
<h3 data-id="heading-4">方案2 prefetch</h3>
<pre><code class="hljs language-js copyable" lang="js"><link rel=<span class="hljs-string">"prefetch"</span> ></link>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html">  <span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"prefetch"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"./img/bg-huoluo.jpg"</span>/></span>   


    .bg &#123;
        background-image:url("./img/bg-huoluo.jpg");
        background-size: contain;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>prefetch是对浏览器的暗示，暗示将来可能需要某些资源，但由浏览器决定是否加载以及什么时候加载这些资源。 优先级低。<br>
pre家族：preload, prefetch, dns-prefetch, preconnect, prerender。<br>
有人可能会问，干嘛不用preload。 呵呵， 你说呢？<br>
演示： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fxiangwenhu.github.io%2FTakeItEasy%2FbgWhithe%2Fprefetch.html" target="_blank" rel="nofollow noopener noreferrer" title="https://xiangwenhu.github.io/TakeItEasy/bgWhithe/prefetch.html" ref="nofollow noopener noreferrer">背景图片闪现空白方案-preferch</a></p>
<h3 data-id="heading-5">方案3 创建隐藏Img节点</h3>
<pre><code class="hljs language-html copyable" lang="html">   <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./img/bg-huoluo.jpg"</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">""</span> <span class="hljs-attr">title</span>=<span class="hljs-string">""</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"display: none"</span>/></span>

    .bg &#123;
        background-color: #2D2C27;
        background-image: url(./img/bg-huoluo.jpg);
        background-size: contain;
    &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这方案好理解，图片已经请求下载啦。 其实不能解决首屏背景图片的问题。<br>
演示：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fxiangwenhu.github.io%2FTakeItEasy%2FbgWhithe%2FhideImage.html" target="_blank" rel="nofollow noopener noreferrer" title="https://xiangwenhu.github.io/TakeItEasy/bgWhithe/hideImage.html" ref="nofollow noopener noreferrer">背景图片闪现空白方案-创建隐藏Img节点</a></p>
<h3 data-id="heading-6">方案4  等待图片加载完毕再显示弹框</h3>
<pre><code class="hljs language-js copyable" lang="js">        <span class="hljs-keyword">let</span> dg = <span class="hljs-literal">null</span>;
        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createDialog</span>(<span class="hljs-params"></span>) </span>&#123;

            onImageLoad(<span class="hljs-string">'./img/bg-huoluo.jpg'</span>).then(<span class="hljs-function"><span class="hljs-params">src</span> =></span> &#123;
                <span class="hljs-keyword">if</span> (!dg) &#123;
                    dg = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'div'</span>);
                    dg.className = <span class="hljs-string">"bg"</span>;
                    dg.style.backgroundImage = <span class="hljs-string">`url(<span class="hljs-subst">$&#123;src&#125;</span>)`</span>;
                    dg.id = <span class="hljs-string">"dialog"</span>;
                    dg.innerHTML = <span class="hljs-string">`
                <div class="content">我爱赫萝!!!!</div>
            `</span>
                    <span class="hljs-built_in">document</span>.body.appendChild(dg);
                &#125;
            &#125;)


        &#125;

        <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">onImageLoad</span>(<span class="hljs-params">src</span>) </span>&#123;
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function">(<span class="hljs-params">resolve, reject</span>) =></span> &#123;
                <span class="hljs-keyword">let</span> img = <span class="hljs-keyword">new</span> Image();
                img.src = src;
                img.onload = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                    resolve(src)
                &#125;
                img.onerror = reject
            &#125;)

        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然这是有明显问题的，你不能因为一个背景图片而让内容无法正常展现。<br>
当然你可以有修正方案。<br>
演示： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fxiangwenhu.github.io%2FTakeItEasy%2FbgWhithe%2FwaitingImg.html" target="_blank" rel="nofollow noopener noreferrer" title="https://xiangwenhu.github.io/TakeItEasy/bgWhithe/waitingImg.html" ref="nofollow noopener noreferrer">背景图片闪现空白方案-等待图片加载完毕再显示弹框</a></p>
<h3 data-id="heading-7">方案5 同时设置背景颜色和图片</h3>
<pre><code class="hljs language-css copyable" lang="css">        <span class="hljs-selector-class">.bg</span> &#123;
            <span class="hljs-attribute">background-color</span>:<span class="hljs-number">#433F34</span>;
            <span class="hljs-attribute">background-size</span>: contain;
        &#125;

        <span class="hljs-selector-class">.bg-new</span>&#123;
            <span class="hljs-attribute">background-image</span>: <span class="hljs-built_in">url</span>(<span class="hljs-string">./img/bg-huoluo.jpg</span>)
        &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样，背景图片加载上的时候，不会有明显的闪白效果。 当然要是背景图片，五颜六色，估计有点为难客官啦。</p>
<p>演示： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fxiangwenhu.github.io%2FTakeItEasy%2FbgWhithe%2FbgColor.html" target="_blank" rel="nofollow noopener noreferrer" title="https://xiangwenhu.github.io/TakeItEasy/bgWhithe/bgColor.html" ref="nofollow noopener noreferrer">背景图片闪现空白方案-同时设置背景颜色和图片</a></p>
<h3 data-id="heading-8">方案6 jpg使用渐进模式，png使用交错模式</h3>
<p>这两种模式共同的作用就是，你不必完整的下载完毕图片，就可以看到图片的内容了。</p>
<p><strong>打个比方， 1M的图片，你可能只需下载不到100Kb,就已经能相对清晰的看到图片了。</strong></p>
<p>演示： <a href="https://link.juejin.cn/?target=https%3A%2F%2Fxiangwenhu.github.io%2FTakeItEasy%2FbgWhithe%2Fprogress.html" target="_blank" rel="nofollow noopener noreferrer" title="https://xiangwenhu.github.io/TakeItEasy/bgWhithe/progress.html" ref="nofollow noopener noreferrer">png正常，png交错，jpg渐进</a></p>
<h3 data-id="heading-9">方案7 小图过度方案</h3>
<p>显示loading图片或者小图，完毕后再换大图。 这种方案常用语封面，商品图标等等场景，背景图也可以借鉴其思路。</p>
<h2 data-id="heading-10">其他可参考方案</h2>
<ul>
<li>webp格式，减少图片大小</li>
<li><strong>css spirte, 减少http开销，同时让其早被加载</strong><br>
css spirte + prefech 可以秀一波</li>
<li>jpg格式图片压缩</li>
<li>图片cdn</li>
<li>多域名</li>
<li>背景图片切割，能repeat就repeat</li>
</ul>
<h2 data-id="heading-11">小结</h2>
<p>是不是很简单，一切都看起来没那么难，这样，你才容易入坑啊。</p>
<h2 data-id="heading-12">写在最后</h2>
<p>写作不易，你的一赞一评就是我前行的最大动力。</p></div>  
</div>
            