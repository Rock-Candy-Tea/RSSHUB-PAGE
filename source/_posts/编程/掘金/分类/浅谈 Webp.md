
---
title: '浅谈 Webp'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/928aa556f1d54563be4847b92dc25dec~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 11 Apr 2021 19:01:31 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/928aa556f1d54563be4847b92dc25dec~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">什么是 Webp ？</h2>
<p>Webp 是由谷歌在 2010 年 9 月发布的一种用于 web 端支持有损和无损压缩的图片格式（同时也支持动态图片和透明度），设计这种图片格式的目的主要是为了创建出相对于 jpg, png 和 gif 更小或画质更好的图片，到 2021 年 3 月份，支持 webp 图片格式的浏览器已经占全球份额的 93 %。</p>
<h2 data-id="heading-1">为什么要使用 Webp ？</h2>
<p>在回答这个问题之前，需要限定一下问题的场景。webp 如其名，设计的初衷就是为了在 <strong>web 场景</strong>下对现有图片资源进行大小优化的图片格式，对于其他的场景，比如专业的设计领域，甚至可能只是壁纸的使用场景都不太适合（毕竟现在 windows 默认都是不支持预览 webp 格式的，mac 刚才试了一下是可以预览的）。
为什么在 web 场景下要使用 webp？因为相对于 png 或 gif 来说，webp 的体积更小，在 web 场景下能够节约用户网络流量，也能加速网页的打开，提升用户体验。下图是在实际项目中使用 webp 图片前后整体图片资源大小的对比（左图为优化前，右图为优化后）</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/928aa556f1d54563be4847b92dc25dec~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>👆 使用 webp 之后图片资源整体的传输大小从 2.6M 减少到了 1.0M。并且压缩后的图片与原图差异也很小，可以通过下图来看一下压缩前后图片的效果。</p>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd328f2dddd4413385115c8f48b4af11~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>具体压缩前后的大小及质量对比可以参考下面两个链接：<a href="https://link.zhihu.com/?target=https://isparta.github.io/compare-webp/index.html#12345" target="_blank" rel="nofollow noopener noreferrer">Webp 示例（PNG 转 Webp）</a> / <a href="https://link.zhihu.com/?target=https://isparta.github.io/compare-webp/index_a.html#12" target="_blank" rel="nofollow noopener noreferrer">Webp 示例（Animated Webp）</a>。</p>
<h2 data-id="heading-2">浏览器对 Webp 的支持程度</h2>
<p>根据维基百科的介绍，到 2021 年 3 月份，全球 93% 的浏览器份额已经支持 webp 图片格式，但如果你想要更详细的支持度信息，可以查看：<a href="https://caniuse.com/?search=webp" target="_blank" rel="nofollow noopener noreferrer">Can I use webp</a>?</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c349d60cd5214104abe7c0abe9d49f63~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>可以看到国内支持 webp 的浏览器占了 78.12% 的份额。所有浏览器版本中 IE 是完全不支持 webp 格式的，Safari 从 macOS 11 及之后版本才开始支持。移动端安卓对 webp 的支持程度倒是很好，加上移动端用系统自带浏览器的感觉不太多（特别是各手机厂商魔改之后的系统），所以基本上是没有任何问题的。而 IOS 端，IOS 14 之后才开始支持，<strong>值得注意的是，IOS 的第三方浏览器都是基于 自带的 Safari 浏览器的渲染引擎，所以基本 IOS 14 之前的版本任何浏览器都应该都是不支持 webp 的</strong>。<a href="https://webcache.googleusercontent.com/search?q=cache:y8szmdAr8Y0J:https://www.howtogeek.com/184283/why-third-party-browsers-will-always-be-inferior-to-safari-on-iphone-and-ipad/+&cd=11&hl=en&ct=clnk&gl=us" target="_blank" rel="nofollow noopener noreferrer">参考</a></p>
<h2 data-id="heading-3">如何判断当前用户浏览器是否支持 webp 格式？</h2>
<p>判断浏览器是否支持 webp 格式的方法有几种：</p>
<h3 data-id="heading-4">1. HTTP request header</h3>
<p>浏览器在请求图片资源的时候，会在请求头 accept 字段表明自身支持的图片格式：</p>
<div>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/727e5e28c939406ea2f9cbb1c775c5e8~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
</div>
<p>可以看到，在 accept 字段，如果当前使用的浏览器支持 webp 格式的话，就会带有 image/webp 字样，这时服务器就可以根据这个请求头来决定是否返回 webp 格式的图片。</p>
<h3 data-id="heading-5">2. 使用 js 加载一张 webp 图片</h3>
<p>在某些场景，如后端不具备动态的 webp 压缩能力，或使用 oss 的情况下，我们需要事先确定浏览器是否支持 webp 再请求对应的图片资源，就需要前端自己去判断浏览器的支持能力了。
其中最简单的方法就是使用浏览器加载欲判断格式的资源（比如用 Audio 标签加载 flac 无损音频），如果浏览器能够加载成功，那么就会触发标签对应的 onload 事件，反之则会触发 onerror。在此基础上，便可以在用户无感知的情况下，使用js动态加载一个 1px * 1px 的 webp 图片并通过其加载情况来确定浏览器是否支持，代码如下：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@function</span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;Promise<boolean>&#125;</span></span>
 * <span class="hljs-doctag">@description </span>检测当前设备是否支持 `webp`。
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">checkIfWebpSupported</span> (<span class="hljs-params"></span>): <span class="hljs-title">Promise</span><<span class="hljs-title">boolean</span>> </span>&#123;
    <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">window</span>) &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'非浏览器环境'</span>);
    &#125;
    
    <span class="hljs-keyword">const</span> &#123; Image &#125; = <span class="hljs-built_in">window</span>;

    <span class="hljs-keyword">if</span> (!Image) <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve(<span class="hljs-literal">false</span>); <span class="hljs-comment">// 无法判断是否支持 webp</span>

    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span><<span class="hljs-built_in">boolean</span>>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
        <span class="hljs-keyword">const</span> image = <span class="hljs-keyword">new</span> Image();
        image.onload = <span class="hljs-function">() =></span> &#123;
            <span class="hljs-keyword">if</span> (image.width === <span class="hljs-number">1</span> && image.height === <span class="hljs-number">1</span>) &#123;
                <span class="hljs-comment">// 能够获取到图片大小则当前浏览器支持 webp</span>
                resolve(<span class="hljs-literal">true</span>);
            &#125; <span class="hljs-keyword">else</span> &#123;
                resolve(<span class="hljs-literal">false</span>);
            &#125;
        &#125;;
        image.onerror = <span class="hljs-function">() =></span> &#123;
            resolve(<span class="hljs-literal">false</span>);
        &#125;;
        image.src = <span class="hljs-string">"data:image/webp;base64,UklGRh4AAABXRUJQVlA4TBEAAAAvAAAAAAfQ//73v/+BiOh/AAA="</span>;
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码返回一个 Promise，直接调用 <code>checkIfWebpSupported ().then (isSupported => &#123;&#125;);</code> 即可在 then 中得到判断结果。</p>
<h3 data-id="heading-6">3. 使用 canvas 生成 webp</h3>
<p>Canvas 可以使用 <code>toDataURL()</code> 方法将画布内容转换成 base64 编码的图片资源字符串，该方法接受两个参数，第一个参数是图片资源的类型（默认为 image/png），第二个参数为图片资源的质量。
支持 webp 格式的在调用这个方法时类型指定为 image/webp，则会返回带有 image/webp 字样的资源地址，而不支持 webp 的浏览器则会返回 image/png。我们可以利用这个特性来判断浏览器是否支持 webp：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@function</span>
 * <span class="hljs-doctag">@return <span class="hljs-type">&#123;boolean&#125;</span></span>
 * <span class="hljs-doctag">@description </span>检测当前设备是否支持 `webp`。
 */</span>
 <span class="hljs-keyword">export</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">checkIfWebpSupported</span> (<span class="hljs-params"></span>): <span class="hljs-title">boolean</span> </span>&#123;
     <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">document</span>) &#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'非浏览器环境'</span>);
    &#125;
    
    <span class="hljs-keyword">if</span> (!<span class="hljs-built_in">document</span>.createElement) <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>; 
    
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'canvas'</span>).toDataURL(<span class="hljs-string">'image/webp'</span>).indexOf(<span class="hljs-string">'image/webp'</span>) > -<span class="hljs-number">1</span>;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">总结</h2>
<p>Webp 压缩率高，图片质量与原图在视觉上没有太大差异的特点，让其很适合用在 web 网页这样的对图片多但对图片质量要求不是很高的场景。在实际使用中，我们可以在使用上述几种方法对浏览器 webp 的支持程度进行判断之后，替换网站图片资源为 webp 格式，对于不支持的浏览器，我们则请求原始图片作为 fallback，保证页面的正常显示。当然，针对 webp 支持的判断只需要一次，我们可以在首次获得判断结果之后将其缓存，在之后需要确保支持 webp 的地方取缓存中的结果即可。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            