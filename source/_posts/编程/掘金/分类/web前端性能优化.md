
---
title: 'web前端性能优化'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: ''
author: 掘金
comments: false
date: Sat, 21 Aug 2021 01:41:26 GMT
thumbnail: ''
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">一、PC端优化策略</h4>
<p>      主要包括网络加载类、页面渲染类、CSS优化类、JavaScript执行类、缓存类、图片类、架构协议类等几类；</p>
<h5 data-id="heading-1">1、网络加载类</h5>
<p>（1）减少HTTP资源请求次数：</p>
<p>      在前端页面中，通常建议尽可能合并静态资源图片、JavaScript或CSS代码，减少页面请求数和资源请求消耗，这样可以缩短首屏加载时间，通过构建工具合并雪碧图、CSS、JavaScript文件等都是为了减少HTTP资源请求次数，另外也要尽量避免重复的资源，防止增加多余请求；</p>
<p>（2）减少HTTP请求大小：</p>
<p>      除了减少HTTP资源请求次数，也要尽量减少每个HTTP请求的大小，如减少没必要的图片、JavaScript、CSS 及 HTML 代码，对文件进行压缩优化，或者使用gzip压缩传输内容等都可以用来减少文件大小，缩短网络传输等待时延，使用构建工具来压缩静态图片资源以及移除代码中的注释并压缩，目的都是为了减少HTTP请求的大小；</p>
<p>（3）将CSS或JavaScript放到外部文件中，避免使用style或script标签直接引入：</p>
<p>      在HTML文件上引用外部资源可以有效利用浏览器的静态资源缓存，但有时候在移动端页面CSS或JavaScript比较简单的情况下为了减少请求，也会将CSS或JavaScript直接写到HTML里面，具体要根据CSS或JavaScript文件的大小和业务的场景来分析，如果CSS或JavaScript文件内容较多，业务逻辑较复杂，建议放到外部文件引入；</p>
<p>**</p>
<pre><code class="copyable"><link rel="stylesheet" href="/css/master.css">
<script type="text/javascript" src="//cdn.domain.com/path/main.js"></script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（4）避免页面中空的href和src：</p>
<p>      当标签的href属性为空，或
</p><p>**</p>
<pre><code class="copyable">  <!--不推荐-->
  <img src="" alt="photo" >
  <a href="">点击链接</a>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（5）为HTML指定Cache-Control或Expires：</p>
<p>      为HTML内容设置Cache-Control 或 Expires可以将HTML内容缓存起来，避免频繁向服务器端发送请求，在页面中的Cache-Control 或 Expires头部有效时，浏览器将直接从缓存中读取内容，不再向服务器端发送请求；</p>
<p>**</p>
<pre><code class="copyable">  <meta http-equiv="Cache-Control" content="max-age=7200">
  <meta http-equiv="Expires" content="Mon,20Jul201623:00:00GMT">
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（6）合理设置Etag和Last-Modified：</p>
<p>      合理设置Etag 和 Last-Modified使用浏览器缓存，对于未修改的文件，静态资源服务器会向浏览器端返回304，让浏览器从缓存中读取文件，减少Web资源下载的带宽消耗并降低服务器负载；</p>
<p>**</p>
<pre><code class="copyable"><meta http-equiv="last-modified" content="Sun,05 Nov 2017 13:45:57 GMT">
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（7）减少页面重定向：</p>
<p>      页面每次重定向都会延长页面内容返回的等待延时，一次重定向大约需要200毫秒不等的时间开销（无缓存），为了保证用户尽快看到页面内容，要尽量避免页面重定向；</p>
<p>（8）使用静态资源分域存放来增加下载并行数：</p>
<p>      浏览器在同一时刻向同一域名请求文件的并行下载数是有限的，因此可以利用多个域名的主机来存放不同的静态资源，增大页面加载时资源的并行下载数，缩短页面资源加载的时间，通常根据多个域名来分别存储JavaScript、CSS和图片文件；</p>
<p>**</p>
<pre><code class="copyable"><link rel="stylesheet" href="//cdn1.domain.com/path/main.css" >
<script src="//cdn2.domain.com/path/main.js"></script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（9）使用静态资源CDN来存储文件：<br>
如果条件允许，可以利用CDN网络加快同一个地理区域内重复静态资源文件的响应下载速度，缩短资源请求时间；</p>
<p>（10）使用CDN Combo下载传输内容：</p>
<p>      CDN Combo是在CDN服务器端将多个文件请求打包成一个文件的形式来返回的技术，这样可以实现HTTP连接传输的一次性复用，减少浏览器的HTTP请求数，加快资源下载速度，例如同一个域名CDN服务器上的a.js，b.js，c.js就可以按如下方式在一个请求中下载：</p>
<p>**</p>
<pre><code class="copyable"><script src="//cdn.domain.com/path/a.js,b.js,c.js"></script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（11）使用可缓存的AJAX：</p>
<p>      对于返回内容相同的请求，没必要每次都直接从服务端拉取，合理使用AJAX缓存能加快AJAX响应速度并减轻服务器压力；</p>
<p>**</p>
<pre><code class="copyable">$.ajax(&#123;
     url: url,
     type: 'get',
     cache: true, //推荐使用缓存
     data: &#123;&#125;,
     success() &#123;&#125;,
     error() &#123;&#125;
    &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（12）使用GET来完成AJAX请求：</p>
<p>      使用XMLHttpRequest时,浏览器中的POST方法会发起两次TCP数据包传输，首先会发送文件头，然后发送HTTP正文数据，而使用GET时只发送头部，所以在拉取服务端数据时使用GET请求效率更高；</p>
<p>**</p>
<pre><code class="copyable">$.ajax(&#123;
  url: url,
  type: 'get', //推荐使用get完成请求
  data: &#123;&#125;,
  success() &#123;&#125;,
  error() &#123;&#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（13）减少Cookie的大小并进行Cookie隔离：</p>
<p>      HTTP请求通常默认带上浏览器端的Cookie一起发送给服务器，所以在非必要的情况下，要尽量减少Cookie来减少HTTP请求的大小，对于静态资源，尽量使用不同的域名来存放，因为Cookie默认是不能跨域的，这样就做到了不同域名下静态资源请求的Cookie隔离；</p>
<p>（14）缩小favicon.ico并缓存：</p>
<p>      有利favicon.ico的重复加载，因为一般一个Web应用的favicon.ico是很少改变的；</p>
<p>（15）推荐使用异步JavaScript资源：</p>
<p>      异步的JavaScript资源不会阻塞文档解析，所以允许在浏览器中优先渲染页面，延后加载脚本执行，例如JavaScript的引用可以如下设置，也可以使用模块化加载机制来实现；其中使用async时，加载和渲染后续文档元素的过程和main.js的加载与执行是并行的；使用defer时，加载后续文档元素的过程和main.js的加载是并行的，但是main.js的执行要在页面所有元素解析完成之后才开始执行；</p>
<p>**</p>
<pre><code class="copyable"><script src="main.js" defer></script>
<script src="main.js" async></script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（16）消除阻塞渲染的CSS及JavaScript：</p>
<p>      对于页面中加载时间过长的CSS或JavaScript文件，需要进行合理拆分或延后加载，保证关键路径的资源能快速加载完成；</p>
<p>（17）避免使用CSS import引用加载CSS：</p>
<p>      CSS中的@import可以从另一个样式文件中引入样式，但应该避免这种用法，因为这样会增加CSS资源加载的关键路径长度，带有＠import的CSS样式需要在CSS文件串行解析到＠import时才会加载另外的CSS文件，大大延后CSS渲染完成的时间；</p>
<p>**</p>
<pre><code class="copyable"><!--不推荐-->
<style>
@import "path/main.css";
</style>

<!--推荐-->
<link rel="stylesheet" href="//cdn1.domain.com/path/main.css" >
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>2、页面渲染类</strong></p>
<p>（1）把CSS资源引用放到HTML文件顶部：</p>
<p>      一般推荐将所有CSS资源指定在HTML文档中，这样浏览器可以优先下载CSS并尽早完成页面渲染；</p>
<p>（2）JavaScript资源引用放到HTML文件底部：</p>
<p>      JavaScript资源放到HTML文档底部可以防止JavaScript的加载和解析执行对页面渲染造成阻塞，由于JavaScript资源默认是解析阻塞的，除非被标记为异步或者通过其他的异步方式加载，否则会阻塞HTML DOM解析和CSS渲染过程；</p>
<p>（3）尽量预先设定图片等大小：</p>
<p>      在加载大量的图片元素时，尽量预先限定图片的尺寸大小，否则在图片加载过程中会更新图片的排版信息，产生大量的重排；</p>
<p>（4）不要在HTML中直接缩放图片：</p>
<p>      在HTML中直接缩放图片会导致页面内容的重排重绘，此时可能会使页面中的其他操作产生卡顿，因此要尽量减少在页面中直接进行图片缩放；</p>
<p>（5）减少DOM元素数量和深度：</p>
<p>      HTML中标签元素越多，标签的层级越深，浏览器解析DOM并绘制到浏览器中所花的时间就越长，所以应尽可能保持DOM元素简洁和层级较少；</p>
<p>**</p>
<pre><code class="copyable"><!--不推荐-->

<div>
  <span>
      <a href="javascript:void(0);">
          <img src="./path/photo.jpg" alt="图片">
      </a>
   </span>
</div>

<!--推荐-->
<img src="./path/photo.jpg" alt="图片" >
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（6）尽量避免在选择器末尾添加通配符：</p>
<p>      CSS解析匹配到渲染树的过程是从右到左的逆向匹配，在选择器末尾添加通配符至少会增加一倍多计算量；</p>
<p>（7）减少使用关系型样式表的写法：</p>
<p>      直接使用唯一的类名即可最大限度的提升渲染引擎绘制渲染树的效率；</p>
<p>（8）尽量减少使用JS动画：</p>
<p>      JS直接操作DOM极容易引起页面的重排；</p>
<p>（9）CSS动画使用translate、scale代替top、height：</p>
<p>      尽量使用CSS3的translate、scale属性代替top、left和height、width，避免大量的重排计算；</p>
<p>（10）尽量避免使用<code><table></code>、<code><iframe></code>：</p>
<p>      <code><table></code>内容的渲染是将table的DOM渲染树全部生成完并一次性绘制到页面上的，所以在长表格渲染时很耗性能，应该尽量避免使用它，可以考虑使用列表元素</p><ul>代替；尽量使用异步的方式动态添加iframe，因为iframe内资源的下载进程会阻塞父页面静态资源的下载与CSS及HTML DOM的解析；<p></p>
<p>（11）避免运行耗时的JavaScript：</p>
<p>      长时间运行的JavaScript会阻塞浏览器构建DOM树、DOM渲染树、渲染页面，所以任何与页面初次渲染无关的逻辑功能都应该延迟加载执行，这和JavaScript资源的异步加载思路是一致的；</p>
<p>（12）避免使用CSS表达式或CSS滤镜：</p>
<p>      CSS表达式或CSS滤镜的解析渲染速度是比较慢的，在有其他解决方案的情况下应该尽量避免使用；</p>
<p>**</p>
<pre><code class="copyable">//不推荐
.opacity&#123;
    filter : progid : DXImageTransform.Microsoft.Alpha( opacity = 50 );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">二、移动端优化策略</h4>
<h5 data-id="heading-3">1、网络加载类</h5>
<p>（1）首屏数据请求提前，避免JavaScript文件加载后才请求数据：</p>
<p>      为了进一步提升页面加载速度，可以考虑将页面的数据请求尽可能提前，避免在JavaScript加载完成后才去请求数据，通常数据请求是页面内容渲染中关键路径最长的部分，而且不能并行，所以如果能将数据请求提前，可以极大程度缩短页面内容的渲染完成时间；</p>
<p>（2）首屏加载和按需加载，非首屏内容滚屏加载，保证首屏内容最小化：</p>
<p>      由于移动端网络速度相对较慢，网络资源有限，因此为了尽快完成页面内容的加载，需要保证首屏加载资源最小化，非首屏内容使用滚动的方式异步加载，一般推荐移动端页面首屏数据展示延时最长不超过3秒，目前中国联通3G的网络速度为338KB/s (2.71Mb/s)，所以推荐首屏所有资源大小不超过1014KB，即大约不超过1MB；</p>
<p>（3）模块化资源并行下载：</p>
<p>      在移动端资源加载中，尽量保证JavaScript资源并行加载，主要指的是模块化JavaScript资源的异步加载，例如AMD的异步模块，使用并行的加载方式能够缩短多个文件资源的加载时间；</p>
<p>（4）inline首屏必备的CSS和JavaScript：</p>
<p>      通常为了在HTML加载完成时能使浏览器中有基本的样式，需要将页面渲染时必备的CSS和JavaScript通过
</p><p>**</p>
<pre><code class="copyable"><!DOCTYPE html>

<head>
  <meta charset="UTF-8">
  <title>样例</title>
  <meta>
  <style>
    /*必备的首屏CSS*/
    html,
    body &#123;
      margin: 0;
      padding: 0;
      background-color: #ccc;
    &#125;
  </style>
</head>

<body>
</body>

</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（5）meta dns prefetch设置DNS预解析：</p>
<p>      设置文件资源的DNS预解析，让浏览器提前解析获取静态资源的主机IP，避免等到请求时才发起DNS解析请求，通常在移动端HTML中可以采用如下方式完成：</p>
<p>**</p>
<pre><code class="copyable"><!--cdn域名预解析-->
<meta http-equiv="x-dns-prefetch-control" content="on" >
<link rel="dns-prefetch" href="//cdn.domain.com" >
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（6）资源预加载：</p>
<p>      对于移动端首屏加载后可能会被使用的资源，需要在首屏完成加载后尽快进行加载，保证在用户需要浏览时已经加载完成，这时候如果再去异步请求就显得很慢；</p>
<p>（7）合理利用MTU策略：</p>
<p>      通常情况下，我们认为TCP网络传输的最大传输单元（Maximum Transmission Unit，MTU）为 1500B，即一个 RTT（Round-Trip Time，网络请求往返时间）内可以传输的数据量最大为1500字节，因此在前后端分离的开发模式中，尽量保证页面的HTML内容在1KB以内，这样整个HTML的内容请求就可以在一个RTT内请求完成，最大限度地提高HTML载入速度；</p>
<h5 data-id="heading-4">2、缓存类</h5>
<p>（1）合理利用浏览器缓存：</p>
<p>      除了上面所说的Cache-Control、Expires、Etag 和 Last-Modified来设置HTTP缓存外，在移动端还可以使用localStorage等来保存AJAX返回的数据，或者使用localStorage保存CSS或JavaScript静态资源内容，实现移动端的离线应用，尽可能减少网络请求，保证静态资源内容的快速加载；</p>
<p>（2）静态资源离线方案：</p>
<p>      对于移动端或Hybrid应用，可以设置离线文件或离线包机制让静态资源请求从本地读取，加快资源载入速度，并实现离线更新；</p>
<p>（3）尝试使用AMP HTML</p>
<p>      AMP HTML可以作为优化前端页面性能的一个解决方案，使用AMP Component中的元素来代替原始的页面元素进行直接渲染；</p>
<p>**</p>
<pre><code class="copyable"><!--不推荐-->
<video width="400" height="300" src="//www.domain.com/videos/myvideo.mp4"
poster="path/poster.jpg">
<div fallback>
    <p>Your browser doesn’t support HTML5 video</p>
</div>
<source type="video/mp4" src="foo.mp4">
<source type="video/webm" src="foo.webm">
</video>

<!--推荐-->
<amp-video width="400" height="300" src="//www.domain.com/videos/myvideo.mp4" poster="path/poster.jpg">
<div fallback>
   <p>Your browser doesn’t support HTML5 video</p>
</div>
<source type="video/mp4" src="foo.mp4">
<source type="video/webm" src="foo.webm">
</amp-video>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（4）尝试使用PWA模式：</p>
<p>      PWA（Progressive Web Apps）是 Google 提出的用前沿的 Web 技术为网页提供 App 般使用体验的一系列方案；</p>
<h5 data-id="heading-5">3、图片类</h5>
<p>（1）图片压缩处理：</p>
<p>      在移动端，通常要保证页面中一切用到的图片都是经过压缩优化处理的，而不是以原图的形式直接使用的，因为那样很消耗流量，而且加载时间更长；</p>
<p>（2）使用较小的图片，合理使用base64内嵌图片：</p>
<p>      在页面使用的背景图片不多且较小的情况下，可以将图片转化成base64编码嵌入到HTML页面或CSS文件中，这样可以减少页面的HTTP请求数，需要注意的是，要保证图片较小，一般图片大小超过2KB就不推荐使用base64嵌入显示了；</p>
<p>**</p>
<pre><code class="copyable">.class-name&#123;
    background-image : url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAALCAMAAABxsOwqAAAAYFBMVEWnxwusyQukxQudwQyZvgyhxAyfwgyxzAsUHQGOuA0aJAERGAFIXwSTugyEqgtqhghQZgUwQQIpOQKbuguVtQuKrAuCowp2kQlheghTbQZHWQU7SwVAVgQ6TgQlLwMeKwFOemyQAAAAVElEQVQI1y3JVRaAIAAF0UconXbvf5ei8HfPDIQQhBAAFE10iKig3SLRNN4SP/p+N08VC0YnfIlNWtqIkhg/TPYbCvhqdHAWRXPZSp3g3CWZvVLXC6OJA3ukv0AaAAAAAElFTkSuQmCC');
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（3）使用更高压缩比格式的图片：</p>
<p>      使用具有较高压缩比格式的图片，如webp（需要设计降级兼容方案）等，在同等图片画质的情况下，高压缩比格式的图片体积更小，能够更快完成文件传输，节省网络流量；</p>
<p>**</p>
<pre><code class="copyable"><img src="//cdn.domain.com/path/photo.webp" alt="webp格式图片" >
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（4）图片懒加载：</p>
<p>      为了保证页面内容的最小化，加速页面的渲染，尽可能节省移动端网络流量，页面中的图片资源推荐使用懒加载实现，在页面滚动时动态载入图片；</p>
<p>**</p>
<pre><code class="copyable"><img data-src="//cdn.domain.com/path/photo.jpg" alt="懒加载图片" >
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（5）使用MediaQuery 或 srcset根据不同屏幕加载不同大小图片：</p>
<p>      针对不同的移动端屏幕尺寸和分辨率，输出不同大小的图片或背景图能保证在用户体验不降低的前提下节省网络流量，加快部分机型的图片加载速度，这在移动端非常值得推荐；</p>
<p>（6）使用iconfont代替图片图标：</p>
<p>      在页面中尽可能使用iconfont来代替图片图标，这样做的好处有：使用iconfont体积较小，而且是矢量图，因此缩放时不会失真；可以方便地修改图片大小尺寸和呈现颜色；但是需要注意的是，iconfont引用不同webfont格式时的兼容性写法，根据经验推荐尽量按照以下顺序书写，否则不容易兼容到所有的浏览器上；</p>
<p>**</p>
<pre><code class="copyable">@font-face&#123;
   font-family:iconfont;
   src:url("./iconfont.eot");
   src:url("./iconfont.eot?#iefix") format("eot"),
   url("./iconfont.woff") format("woff"),
   url("./iconfont.ttf") format("truetype");
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（7）定义图片大小限制：</p>
<p>      加载的单张图片一般建议不超过30KB，避免大图片加载时间长而阻塞页面其他资源的下载，因此推荐10KB以内，如果用户上传的图片过大，建议设置告警系统，帮助我们观察了解整个网站的图片流量情况，做出进一步的改善；</p>
<p>（8）强缓存策略：</p>
<p>      对于一些永远不会变的图片可以使用强缓存的方式缓存在用户的浏览器上；</p>
<h5 data-id="heading-6">4、脚本类</h5>
<p>（1）尽量使用id：</p>
<p>      选择器选择页面DOM元素时尽量使用id选择器，因为id选择器速度最快；</p>
<p>（2）合理缓存DOM对象：</p>
<p>      对于需要重复使用的DOM对象，要优先设置缓存变量，避免每次使用时都要从整个DOM树中重新查找；</p>
<p>**</p>
<pre><code class="copyable">//不推荐
$('#mod.active').remove('active');
$('#mod.not-active').addClass('active');

//推荐
let $mod=$('#mod');
$mod.find('.active').remove('active');
$mod.find('.not-active').addClass('active');
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（3）页面元素尽量使用事件代理，避免直接事件绑定：</p>
<p>      使用事件代理可以避免对每个元素都进行绑定，并且可以避免出现内存泄露及需要动态添加元素的事件绑定问题，所以尽量不要直接使用事件绑定；</p>
<p>**</p>
<pre><code class="copyable">//不推荐
$('.btn').on('click',function(e)&#123;
   console.log(this);
&#125;);

//推荐
$('body').on('click','.btn',function(e)&#123;
   console.log(this);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（4）使用touchstart代替click：</p>
<p>      由于移动端屏幕的设计，touchstart事件和click事件触发时间之间存在300毫秒的延时，所以在页面中没有实现touchmove滚动处理的情况下，可以使用touchstart事件来代替元素的click事件，加快页面点击的响应速度，提高用户体验，但同时我们也要注意页面重叠元素touch动作的点击穿透问题；</p>
<p>**</p>
<pre><code class="copyable">//不推荐
$('body').on('click','.btn',function(e)&#123;
    console.log(this);
&#125;);

//推荐
$('body').on('touchstart','.btn',function(e)&#123;
    console.log(this);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（5）避免touchmove、scroll连续事件处理：</p>
<p>      需要对touchmove、scroll这类可能连续触发回调的事件设置事件节流，例如设置每隔16ms（60帧的帧间隔为16.7ms，因此可以合理地设置为16ms）才进行一次事件处理，避免频繁的事件调用导致移动端页面卡顿；</p>
<p>**</p>
<pre><code class="copyable">//不推荐
$('.scroller').on('touchmove','.btn',function(e)&#123;
  console.log(this);
&#125;);

//推荐
$('.scroller').on('touchmove','.btn',function(e)&#123;
  let self=this;
  setTimeout(function()&#123;
    console.log(self);
  &#125;,16);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（6）避免使用eval、with，使用join代替连接符+，推荐使用ECMAScript6的字符串模板，这些都是一些基础的安全脚本编写问题，尽可能使用较高效率的特性来完成这些操作，避免不规范或不安全的写法；</p>
<p>（7）尽量使用ECMAScript6+的特性来编程：</p>
<p>      ECMAScript6+一定程序上更加安全高效，而且部分特性执行速度更快，也是未来规范的需要，所以推荐使用ECMAScript6+的新特性来完成后面的开发；</p>
<h5 data-id="heading-7">5、渲染类</h5>
<p>（1）使用Viewport固定屏幕渲染，可以加速页面渲染内容：</p>
<p>      一般认为，在移动端设置Viewport可以加速页面的渲染，同时可以避免缩放导致页面重排重绘；</p>
<p>（2）避免各种形式重排重绘：</p>
<p>      页面的重排重绘很耗性能，所以一定要尽可能减少页面的重排重绘，例如页面图片大小变化，元素位置变化等这些情况都会导致重排重绘；</p>
<p>（3）使用CSS3动画，开启GPU加速：</p>
<p>      使用CSS3动画时可以设置transform:translateZ(0) 来开启移动设备浏览器的GPU图形处理加速，让动画过程更加流畅，但需要注意的是，在Native WebView 下 GPU 加速有几率产生 App Crash；</p>
<p>**</p>
<pre><code class="copyable">-webkit-transform:translateZ(0);
-ms-transform:translateZ(0);
-o-transform:translateZ(0);
transform:translateZ(0);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（4）合理使用Canvas 和 requestAnimationFrame：</p>
<p>      选择Canvas 或requestAnimationFrame等更高效的动画实现方式，尽量避免使用setTimeout、setInterval等方式来直接处理连续动画；</p>
<p>（5）SVG 代替图片：</p>
<p>      部分情况下可以考虑使用SVG 代替图片实现动画，因为使用SVG格式内容更小，而且SVG DOM结构方便调整；</p>
<p>（6）不滥用float：</p>
<p>      在DOM渲染树生成后的布局渲染阶段，使用float的元素布局计算比较耗性能，所以尽量减少float的使用，推荐使用固定布局或flex-box弹性布局的方式来实现页面元素布局；</p>
<p>（7）不滥用web字体或过多font-size声明：</p>
<p>      过多的font-size声明会增加字体的大小计算，而且也没有必要；</p>
<p>（8）做好脚本容错：</p>
<p>      脚本容错可以避免非正常环境的执行错误影响页面的加载和不相关功能的使用；</p>
<h5 data-id="heading-8">6、架构协议类</h5>
<p>（1）尝试使用 SPDY 和 HTTP2：</p>
<p>      在条件允许的情况下可以考虑使用 SPDY 协议来进行文件资源传输，利用连接复用加快传输过程，缩短资源加载时间，HTTP2 在未来也是可以考虑尝试的；</p>
<p>（2）使用后端数据渲染：</p>
<p>      使用后端数据渲染的方式可以加快页面内容的渲染展示，避免空白页面的出现，同时可以解决移动端页面 SEO 的问题，如果条件允许，后端数据渲染是一个很不错的实践思路；</p>
<p>（3）使用 NativeView 代替 DOM 的性能劣势：</p>
<p>      可以尝试使用 NativeView 的 MNV＊ 开发模式来避免 HTML DOM 性能慢的问题，目前使用 MNV＊ 的开发模式已经可以将页面内容渲染体验做到接近客户端 Native 应用的体验了，但需要避免 js Framework 和 native Framework 的频繁交互；</p></ul></div>  
</div>
            