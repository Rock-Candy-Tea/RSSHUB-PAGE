
---
title: '使用 web-vitals 对项目的性能进行测试'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c3c98c27e484bbca67ac72812cef4cd~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 14 Jun 2021 00:55:35 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c3c98c27e484bbca67ac72812cef4cd~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">web-vitals是什么</h1>
<blockquote>
<p>web-vitals是Google发起的，旨在提供各种质量信号的统一指南，我们相信这些质量信号对提供出色的网络用户体验至关重要。 其可获取三个关键指标（CLS、FID、LCP）和两个辅助指标（FCP、TTFB）。</p>
</blockquote>
<p> 我们用create-react-app 创建的react  的项目里，就存在web-vitals 的身影，位于 src\index.js 中：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c3c98c27e484bbca67ac72812cef4cd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">web-vitals 使用</h1>
<p>1、通过npm 包的形式使用  </p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123;getLCP, getFID, getCLS&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'web-vitals'</span>;

getCLS(<span class="hljs-built_in">console</span>.log);
getFID(<span class="hljs-built_in">console</span>.log);
getLCP(<span class="hljs-built_in">console</span>.log);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、使用CDN 的形式</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><script>
(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">var</span> script = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'script'</span>);
  script.src = <span class="hljs-string">'https://unpkg.com/web-vitals'</span>;
  script.onload = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// When loading `web-vitals` using a classic script, all the public</span>
    <span class="hljs-comment">// methods can be found on the `webVitals` global namespace.</span>
    webVitals.getCLS(<span class="hljs-built_in">console</span>.log);
    webVitals.getFID(<span class="hljs-built_in">console</span>.log);
    webVitals.getLCP(<span class="hljs-built_in">console</span>.log);
  &#125;
  <span class="hljs-built_in">document</span>.head.appendChild(script);
&#125;())
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3、通过谷歌插件的形式进行使用 （需要科学上网）<br>
<a href="https://chrome.google.com/webstore/detail/web-vitals/ahfhijdlegdabablpippeagghigmibma" target="_blank" rel="nofollow noopener noreferrer">下载链接</a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/80d329aa0cd44bd18bf7f48ee40bca34~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>需要注意的点：</strong></p>
<ul>
<li>1、<strong>并不是所有的情况，都会报告具体的指标</strong></li>
</ul>
<p>a.如果用户从不与页面交互，则不会报告FID<br>
b.服务端渲染的页面，则不会报告FCP，FID和LCP</p>
<ul>
<li>2、<strong>部分指标会存在</strong></li>
</ul>
<p>a.每当页面visibilityState更改为hidden时，都应报告CLS<br>
b.使用浏览器前进后退时，会报告 CLS, FCP, FID, LCP</p>
<ul>
<li>3、报告每一次更改的值</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123;getCLS&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'web-vitals'</span>;

<span class="hljs-comment">// Logs CLS as the value changes.</span>
getCLS(<span class="hljs-built_in">console</span>.log, <span class="hljs-literal">true</span>);  <span class="hljs-comment">// 多加一个参数</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>4、允许只报告变化的量（当前值和上一次报告的值之间的差值）</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123;getCLS, getFID, getLCP&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'web-vitals'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">logDelta</span>(<span class="hljs-params">&#123;name, id, delta&#125;</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`<span class="hljs-subst">$&#123;name&#125;</span> matching ID <span class="hljs-subst">$&#123;id&#125;</span> changed by <span class="hljs-subst">$&#123;delta&#125;</span>`</span>);
&#125;

getCLS(logDelta);
getFID(logDelta);
getLCP(logDelta)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>5、性能数据可视化<br>
可以通过发送指标数据到 <a href="https://github.com/GoogleChromeLabs/web-vitals-report" target="_blank" rel="nofollow noopener noreferrer">性能数据可视化工具</a>  ，不过需要谷歌账号，通过谷歌账号去绑定</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bbecf677eb514e5a9c803a3889be18f9~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>6、API 的介绍</p>
<p>// 指标名称
name: 'CLS' | 'FCP' | 'FID' | 'LCP' | 'TTFB';</p>
<p>// 当前指标的具体值，毫秒级
value: number;</p>
<p>//当前值和上一次报告的值之间的差值。
//在第一个报告中，“ delta”和“ value”将始终相同。
delta: number;</p>
<p>//代表此特定指标的唯一ID，该ID特定于
//当前页面。分析工具可以使用此ID进行重复数据删除
//为同一个指标发送多个值，或者将多个增量 组合在一起//并计算总计。
id: string;</p>
<p>//指标值计算中使用的所有效果条目。
//注意，随着值的更改，条目将添加到数组中。
entries: (PerformanceEntry | FirstInputPolyfillEntry | NavigationTimingPolyfillEntry)[];</p>
<p>7、兼容性：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">getCLS(): Chromium,
getFCP(): Chromium, Safari Technology Preview
getFID(): Chromium, Firefox, Safari, Internet Explorer (<span class="hljs-keyword">with</span> the polyfill)
getLCP(): Chromium
getTTFB(): Chromium, Firefox, Safari, Internet Explorer
<span class="copy-code-btn">复制代码</span></code></pre>
<p>8、原文地址：<a href="https://github.com/GoogleChrome/web-vitals" target="_blank" rel="nofollow noopener noreferrer">github.com/GoogleChrom…</a></p></div>  
</div>
            