
---
title: 'vue 项目大屏端适配方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9795'
author: 掘金
comments: false
date: Fri, 30 Jul 2021 00:41:03 GMT
thumbnail: 'https://picsum.photos/400/300?random=9795'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1.适配方式</h2>
<p><code>适配方案采用rem布局， 根据屏幕分辨率大小不同，调整根元素html的font-size， 从而达到每个元素宽高自动变化，适配不同屏幕</code></p>
<h2 data-id="heading-1">2.使用 postcss-px2rem-exclude 插件</h2>
<p>安装 <code>npm install postcss-px2rem-exclude --save-dev</code></p>
<p>在项目根目录创建 postcss.config.js 文件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">module</span>.exports = &#123;
  <span class="hljs-attr">plugins</span>: &#123;
    <span class="hljs-attr">autoprefixer</span>: &#123;&#125;,
    <span class="hljs-string">'postcss-px2rem-exclude'</span>: &#123;
      <span class="hljs-attr">remUnit</span>: <span class="hljs-number">192</span>
      <span class="hljs-comment">// exclude: /node_modules|folder_name/i,</span>
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">3.安装 flexible.js (建议放到本地)</h2>
<p>安装命令  <code>npm install lib-flexible</code></p>
<pre><code class="hljs language-js copyable" lang="js">(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">win, lib</span>) </span>&#123;
  <span class="hljs-keyword">var</span> doc = win.document
  <span class="hljs-keyword">var</span> docEl = doc.documentElement
  <span class="hljs-keyword">var</span> metaEl = doc.querySelector(<span class="hljs-string">'meta[name="viewport"]'</span>)
  <span class="hljs-keyword">var</span> flexibleEl = doc.querySelector(<span class="hljs-string">'meta[name="flexible"]'</span>)
  <span class="hljs-keyword">var</span> dpr = <span class="hljs-number">0</span>
  <span class="hljs-keyword">var</span> scale = <span class="hljs-number">0</span>
  <span class="hljs-keyword">var</span> tid
  <span class="hljs-keyword">var</span> flexible = lib.flexible || (lib.flexible = &#123;&#125;)

  <span class="hljs-keyword">if</span> (metaEl) &#123;
    <span class="hljs-built_in">console</span>.warn(<span class="hljs-string">'将根据已有的meta标签来设置缩放比例'</span>)
    <span class="hljs-keyword">var</span> match = metaEl
      .getAttribute(<span class="hljs-string">'content'</span>)
      <span class="hljs-comment">// eslint-disable-next-line no-useless-escape</span>
      .match(<span class="hljs-regexp">/initial\-scale=([\d\.]+)/</span>)
    <span class="hljs-keyword">if</span> (match) &#123;
      scale = <span class="hljs-built_in">parseFloat</span>(match[<span class="hljs-number">1</span>])
      dpr = <span class="hljs-built_in">parseInt</span>(<span class="hljs-number">1</span> / scale)
    &#125;
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (flexibleEl) &#123;
    <span class="hljs-keyword">var</span> content = flexibleEl.getAttribute(<span class="hljs-string">'content'</span>)
    <span class="hljs-keyword">if</span> (content) &#123;
      <span class="hljs-comment">// eslint-disable-next-line no-useless-escape</span>
      <span class="hljs-keyword">var</span> initialDpr = content.match(<span class="hljs-regexp">/initial\-dpr=([\d\.]+)/</span>)
      <span class="hljs-comment">// eslint-disable-next-line no-useless-escape</span>
      <span class="hljs-keyword">var</span> maximumDpr = content.match(<span class="hljs-regexp">/maximum\-dpr=([\d\.]+)/</span>)
      <span class="hljs-keyword">if</span> (initialDpr) &#123;
        dpr = <span class="hljs-built_in">parseFloat</span>(initialDpr[<span class="hljs-number">1</span>])
        scale = <span class="hljs-built_in">parseFloat</span>((<span class="hljs-number">1</span> / dpr).toFixed(<span class="hljs-number">2</span>))
      &#125;
      <span class="hljs-keyword">if</span> (maximumDpr) &#123;
        dpr = <span class="hljs-built_in">parseFloat</span>(maximumDpr[<span class="hljs-number">1</span>])
        scale = <span class="hljs-built_in">parseFloat</span>((<span class="hljs-number">1</span> / dpr).toFixed(<span class="hljs-number">2</span>))
      &#125;
    &#125;
  &#125;

  <span class="hljs-keyword">if</span> (!dpr && !scale) &#123;
    <span class="hljs-comment">// var isAndroid = win.navigator.appVersion.match(/android/gi);</span>
    <span class="hljs-keyword">var</span> isIPhone = win.navigator.appVersion.match(<span class="hljs-regexp">/iphone/gi</span>)
    <span class="hljs-keyword">var</span> devicePixelRatio = win.devicePixelRatio
    <span class="hljs-keyword">if</span> (isIPhone) &#123;
      <span class="hljs-comment">// iOS下，对于2和3的屏，用2倍的方案，其余的用1倍方案</span>
      <span class="hljs-keyword">if</span> (devicePixelRatio >= <span class="hljs-number">3</span> && (!dpr || dpr >= <span class="hljs-number">3</span>)) &#123;
        dpr = <span class="hljs-number">3</span>
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (devicePixelRatio >= <span class="hljs-number">2</span> && (!dpr || dpr >= <span class="hljs-number">2</span>)) &#123;
        dpr = <span class="hljs-number">2</span>
      &#125; <span class="hljs-keyword">else</span> &#123;
        dpr = <span class="hljs-number">1</span>
      &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-comment">// 其他设备下，仍旧使用1倍的方案</span>
      dpr = <span class="hljs-number">1</span>
    &#125;
    scale = <span class="hljs-number">1</span> / dpr
  &#125;

  docEl.setAttribute(<span class="hljs-string">'data-dpr'</span>, dpr)
  <span class="hljs-keyword">if</span> (!metaEl) &#123;
    metaEl = doc.createElement(<span class="hljs-string">'meta'</span>)
    metaEl.setAttribute(<span class="hljs-string">'name'</span>, <span class="hljs-string">'viewport'</span>)
    metaEl.setAttribute(<span class="hljs-string">'content'</span>, <span class="hljs-string">'initial-scale='</span> + scale + <span class="hljs-string">', maximum-scale='</span> + scale + <span class="hljs-string">', minimum-scale='</span> + scale + <span class="hljs-string">', user-scalable=no'</span>)
    <span class="hljs-keyword">if</span> (docEl.firstElementChild) &#123;
      docEl.firstElementChild.appendChild(metaEl)
    &#125; <span class="hljs-keyword">else</span> &#123;
      <span class="hljs-keyword">var</span> wrap = doc.createElement(<span class="hljs-string">'div'</span>)
      wrap.appendChild(metaEl)
      doc.write(wrap.innerHTML)
    &#125;
  &#125;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">refreshRem</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> width = docEl.getBoundingClientRect().width
    <span class="hljs-keyword">if</span> (width / dpr > <span class="hljs-number">540</span>) &#123;
      width = width * dpr
    &#125;
    <span class="hljs-keyword">var</span> rem = width / <span class="hljs-number">10</span>
    docEl.style.fontSize = rem + <span class="hljs-string">'px'</span>
    flexible.rem = win.rem = rem
  &#125;

  win.addEventListener(
    <span class="hljs-string">'resize'</span>,
    <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-built_in">clearTimeout</span>(tid)
      tid = <span class="hljs-built_in">setTimeout</span>(refreshRem, <span class="hljs-number">300</span>)
    &#125;,
    <span class="hljs-literal">false</span>
  )
  win.addEventListener(
    <span class="hljs-string">'pageshow'</span>,
    <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">e</span>) </span>&#123;
      <span class="hljs-keyword">if</span> (e.persisted) &#123;
        <span class="hljs-built_in">clearTimeout</span>(tid)
        tid = <span class="hljs-built_in">setTimeout</span>(refreshRem, <span class="hljs-number">300</span>)
      &#125;
    &#125;,
    <span class="hljs-literal">false</span>
  )

  <span class="hljs-keyword">if</span> (doc.readyState === <span class="hljs-string">'complete'</span>) &#123;
    doc.body.style.fontSize = <span class="hljs-number">12</span> * dpr + <span class="hljs-string">'px'</span>
  &#125; <span class="hljs-keyword">else</span> &#123;
    doc.addEventListener(
      <span class="hljs-string">'DOMContentLoaded'</span>,
      <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        doc.body.style.fontSize = <span class="hljs-number">12</span> * dpr + <span class="hljs-string">'px'</span>
      &#125;,
      <span class="hljs-literal">false</span>
    )
  &#125;

  refreshRem()

  flexible.dpr = win.dpr = dpr
  flexible.refreshRem = refreshRem
  flexible.rem2px = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">d</span>) </span>&#123;
    <span class="hljs-keyword">var</span> val = <span class="hljs-built_in">parseFloat</span>(d) * <span class="hljs-built_in">this</span>.rem
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> d === <span class="hljs-string">'string'</span> && d.match(<span class="hljs-regexp">/rem$/</span>)) &#123;
      val += <span class="hljs-string">'px'</span>
    &#125;
    <span class="hljs-keyword">return</span> val
  &#125;
  flexible.px2rem = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">d</span>) </span>&#123;
    <span class="hljs-keyword">var</span> val = <span class="hljs-built_in">parseFloat</span>(d) / <span class="hljs-built_in">this</span>.rem
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> d === <span class="hljs-string">'string'</span> && d.match(<span class="hljs-regexp">/px$/</span>)) &#123;
      val += <span class="hljs-string">'rem'</span>
    &#125;
    <span class="hljs-keyword">return</span> val
  &#125;
&#125;)(<span class="hljs-built_in">window</span>, <span class="hljs-built_in">window</span>[<span class="hljs-string">'lib'</span>] || (<span class="hljs-built_in">window</span>[<span class="hljs-string">'lib'</span>] = &#123;&#125;))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码与安装的flexible.js不同
修改了</p>
<pre><code class="hljs language-js copyable" lang="js">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">refreshRem</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> width = docEl.getBoundingClientRect().width
    <span class="hljs-keyword">if</span> (width / dpr > <span class="hljs-number">540</span>) &#123;
      width = width * dpr
    &#125;
    <span class="hljs-keyword">var</span> rem = width / <span class="hljs-number">10</span>
    docEl.style.fontSize = rem + <span class="hljs-string">'px'</span>
    flexible.rem = win.rem = rem
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在main.js中引入</p>
<p><code>import '路径/flexible.js'</code></p></div>  
</div>
            