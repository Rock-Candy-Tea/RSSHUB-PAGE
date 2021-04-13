
---
title: '精通Vite2之插件开发指南'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/225cf28a6b904a0a935e7e2f638ad5da~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 12 Apr 2021 02:34:43 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/225cf28a6b904a0a935e7e2f638ad5da~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><img alt="img" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/225cf28a6b904a0a935e7e2f638ad5da~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<p>前几篇文章我写了一下Vite2在工程化和项目实践中的一些探索，受到了小伙伴们的喜爱，其中就有人提出想看看vite插件怎么写，我看了一下文档、vite-plugin-mock和vite-plugin-vue-i18n的源码，有一些收获，在这里分享给大家，本文内容如下：</p>
<ul>
<li>Vite2插件开发指南
<ul>
<li>Vite插件是什么</li>
<li>Vite插件的形式</li>
<li>插件钩子</li>
<li>插件顺序</li>
<li>插件编写实操</li>
<li>配套视频教程</li>
<li>配套源码</li>
<li>后续创作计划</li>
<li>支持我们</li>
</ul>
</li>
</ul>
<h3 data-id="heading-0">Vite插件是什么</h3>
<p>使用Vite插件可以扩展Vite能力，比如解析用户自定义的文件输入，在打包代码前转译代码，或者查找第三方模块。</p>
<p><img alt="image-20210216214524914" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9820ada7062945878203b017228e0c14~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-1">Vite插件的形式</h3>
<p><code>Vite</code>插件扩展自<code>Rollup</code>插件接口，只是额外多了一些<code>Vite</code>特有选项。</p>
<p><code>Vite</code>插件是一个<strong>拥有名称</strong>、<strong>创建钩子</strong>(build hook)或<strong>生成钩子</strong>(output generate hook)<strong>的对象</strong>。</p>
<img alt="image-20210219094649110" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8f92a792405a4483992243e4144074eb~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<p>如果需要配置插件，它的形式应该是一个接收插件选项，<strong>返回插件对象的函数</strong>。</p>
<img alt="image-20210219094755835" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e6989561c774bc6967d79f26d858a7f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
<h4 data-id="heading-2">范例：加载一个不存在的虚拟模块</h4>
<p>创建<code>vite-plugin-my-example.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myExample</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'my-example'</span>, <span class="hljs-comment">// 名称用于警告和错误展示</span>
    resolveId ( source ) &#123;
      <span class="hljs-keyword">if</span> (source === <span class="hljs-string">'virtual-module'</span>) &#123;
        <span class="hljs-keyword">return</span> source; <span class="hljs-comment">// 返回source表明命中，vite不再询问其他插件处理该id请求</span>
      &#125;
      <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>; <span class="hljs-comment">// 返回null表明是其他id要继续处理</span>
    &#125;,
    load ( id ) &#123;
      <span class="hljs-keyword">if</span> (id === <span class="hljs-string">'virtual-module'</span>) &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">'export default "This is virtual!"'</span>; <span class="hljs-comment">// 返回"virtual-module"模块源码</span>
      &#125;
      <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>; <span class="hljs-comment">// 其他id继续处理</span>
    &#125;
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">插件钩子</h3>
<h4 data-id="heading-4">通用钩子</h4>
<p>开发时，<code>Vite dev server</code>创建一个插件容器按照<code>Rollup</code>调用创建钩子的规则请求各个钩子函数。</p>
<p>下面钩子会在服务器启动时调用一次:</p>
<ul>
<li><a href="https://rollupjs.org/guide/en/#options" target="_blank" rel="nofollow noopener noreferrer"><code>options</code></a> 替换或操纵<code>rollup</code>选项</li>
<li><a href="https://rollupjs.org/guide/en/#buildstart" target="_blank" rel="nofollow noopener noreferrer"><code>buildStart</code></a> 开始创建</li>
</ul>
<p>下面钩子每次有模块请求时都会被调用:</p>
<ul>
<li><a href="https://rollupjs.org/guide/en/#resolveid" target="_blank" rel="nofollow noopener noreferrer"><code>resolveId</code></a> 创建自定义确认函数，常用语定位第三方依赖</li>
<li><a href="https://rollupjs.org/guide/en/#load" target="_blank" rel="nofollow noopener noreferrer"><code>load</code></a> 创建自定义加载函数，可用于返回自定义的内容</li>
<li><a href="https://rollupjs.org/guide/en/#transform" target="_blank" rel="nofollow noopener noreferrer"><code>transform</code></a> 可用于转换已加载的模块内容</li>
</ul>
<p>下面钩子会在服务器关闭时调用一次:</p>
<ul>
<li><a href="https://rollupjs.org/guide/en/#buildend" target="_blank" rel="nofollow noopener noreferrer"><code>buildEnd</code></a></li>
<li><a href="https://rollupjs.org/guide/en/#closebundle" target="_blank" rel="nofollow noopener noreferrer"><code>closeBundle</code></a></li>
</ul>
<h4 data-id="heading-5">Vite特有钩子</h4>
<ul>
<li>config: 修改Vite配置</li>
<li>configResolved：Vite配置确认</li>
<li>configureServer：用于配置dev server</li>
<li>transformIndexHtml：用于转换宿主页</li>
<li>handleHotUpdate：自定义HMR更新时调用</li>
</ul>
<h4 data-id="heading-6">范例：钩子调用顺序测试</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">myExample</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-comment">// 返回的是插件对象</span>
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'hooks-order'</span>, 
    <span class="hljs-comment">// 初始化hooks，只走一次</span>
    <span class="hljs-function"><span class="hljs-title">options</span>(<span class="hljs-params">opts</span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'options'</span>, opts);
    &#125;,
    <span class="hljs-function"><span class="hljs-title">buildStart</span>(<span class="hljs-params"></span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'buildStart'</span>);
    &#125;,
    <span class="hljs-comment">// vite特有钩子</span>
    <span class="hljs-function"><span class="hljs-title">config</span>(<span class="hljs-params">config</span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'config'</span>, config);
      <span class="hljs-keyword">return</span> &#123;&#125;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">configResolved</span>(<span class="hljs-params">resolvedCofnig</span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'configResolved'</span>);
    &#125;,
    <span class="hljs-function"><span class="hljs-title">configureServer</span>(<span class="hljs-params">server</span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'configureServer'</span>);
      <span class="hljs-comment">// server.app.use((req, res, next) => &#123;</span>
      <span class="hljs-comment">//   // custom handle request...</span>
      <span class="hljs-comment">// &#125;)</span>
    &#125;,
    <span class="hljs-function"><span class="hljs-title">transformIndexHtml</span>(<span class="hljs-params">html</span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'transformIndexHtml'</span>);
      <span class="hljs-keyword">return</span> html
      <span class="hljs-comment">// return html.replace(</span>
      <span class="hljs-comment">//   /<title>(.*?)<\/title>/,</span>
      <span class="hljs-comment">//   `<title>Title replaced!</title>`</span>
      <span class="hljs-comment">// )</span>
    &#125;,
    <span class="hljs-comment">// 通用钩子</span>
    resolveId ( source ) &#123;
      <span class="hljs-keyword">if</span> (source === <span class="hljs-string">'virtual-module'</span>) &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'resolvedId'</span>, source);
        <span class="hljs-keyword">return</span> source; 
      &#125;
      <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>; 
    &#125;,
    load ( id ) &#123;
      <span class="hljs-keyword">if</span> (id === <span class="hljs-string">'virtual-module'</span>) &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'load'</span>);
        <span class="hljs-keyword">return</span> <span class="hljs-string">'export default "This is virtual!"'</span>;
      &#125;
      <span class="hljs-keyword">return</span> <span class="hljs-literal">null</span>;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">transform</span>(<span class="hljs-params">code, id</span>)</span> &#123;
      <span class="hljs-keyword">if</span> (id === <span class="hljs-string">'virtual-module'</span>) &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'transform'</span>);
      &#125;
      <span class="hljs-keyword">return</span> code
    &#125;,
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">钩子调用顺序</h4>
<p><img alt="image-20210218192306617" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e229d9ff7880440bafcc5f188486defc~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">插件顺序</h3>
<ul>
<li>别名处理Alias</li>
<li>用户插件设置<code>enforce: 'pre'</code></li>
<li>Vite核心插件</li>
<li>用户插件未设置<code>enforce</code></li>
<li>Vite构建插件</li>
<li>用户插件设置<code>enforce: 'post'</code></li>
<li>Vite构建后置插件(minify, manifest, reporting)</li>
</ul>
<p><img alt="image-20210219092521002" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf65b1e604df4ff6903081128ee4e591~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-9">插件编写实操</h3>
<h4 data-id="heading-10">实现一个mock服务器vite-plugin-mock</h4>
<p>实现思路是给开发服务器实例(connect)配一个中间件，该中间件可以存储用户配置接口映射信息，并提前处理输入请求，如果请求的url和路由表匹配则接管，按用户配置的handler返回结果。</p>
<p><img alt="image-20210219094301985" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/151f2d664ebc4cee93c33dfefd2fa8ed~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>创建<code>plugins/vite-plugin-mock.js</code></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> path <span class="hljs-keyword">from</span> <span class="hljs-string">'path'</span>

<span class="hljs-keyword">let</span> mockRouteMap = &#123;&#125;;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">matchRoute</span>(<span class="hljs-params">req</span>) </span>&#123;
  <span class="hljs-keyword">let</span> url = req.url;
  <span class="hljs-keyword">let</span> method = req.method.toLowerCase();
  <span class="hljs-keyword">let</span> routeList = mockRouteMap[method];

  <span class="hljs-keyword">return</span> routeList && routeList.find(<span class="hljs-function">(<span class="hljs-params">item</span>) =></span> item.path === url);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createRoute</span>(<span class="hljs-params">mockConfList</span>) </span>&#123;
  mockConfList.forEach(<span class="hljs-function">(<span class="hljs-params">mockConf</span>) =></span> &#123;
    <span class="hljs-keyword">let</span> method = mockConf.type || <span class="hljs-string">'get'</span>;
    <span class="hljs-keyword">let</span> path = mockConf.url;
    <span class="hljs-keyword">let</span> handler = mockConf.response;
    <span class="hljs-keyword">let</span> route = &#123; path, <span class="hljs-attr">method</span>: method.toLowerCase(), handler &#125;;
    <span class="hljs-keyword">if</span> (!mockRouteMap[method]) &#123;
      mockRouteMap[method] = [];
    &#125;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'create mock api: '</span>, route.method, route.path);
    mockRouteMap[method].push(route);
  &#125;);
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">send</span>(<span class="hljs-params">body</span>) </span>&#123;
  <span class="hljs-keyword">let</span> chunk = <span class="hljs-built_in">JSON</span>.stringify(body);
  <span class="hljs-comment">// Content-Length</span>
  <span class="hljs-keyword">if</span> (chunk) &#123;
    chunk = Buffer.from(chunk, <span class="hljs-string">'utf-8'</span>);
    <span class="hljs-built_in">this</span>.setHeader(<span class="hljs-string">'Content-Length'</span>, chunk.length);
  &#125;
  <span class="hljs-comment">// content-type</span>
  <span class="hljs-built_in">this</span>.setHeader(<span class="hljs-string">'Content-Type'</span>, <span class="hljs-string">'application/json'</span>);
  <span class="hljs-comment">// status</span>
  <span class="hljs-built_in">this</span>.statusCode = <span class="hljs-number">200</span>;
  <span class="hljs-comment">// respond</span>
  <span class="hljs-built_in">this</span>.end(chunk, <span class="hljs-string">'utf8'</span>);
&#125;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">options = &#123;&#125;</span>) </span>&#123;
  options.entry = options.entry || <span class="hljs-string">'./mock/index.js'</span>;


  <span class="hljs-keyword">if</span> (!path.isAbsolute(options.entry)) &#123;
    options.entry = path.resolve(process.cwd(), options.entry);
  &#125;

  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">configureServer</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">&#123; app &#125;</span>) </span>&#123;
      <span class="hljs-keyword">const</span> mockObj = <span class="hljs-built_in">require</span>(options.entry);
      createRoute(mockObj);

      <span class="hljs-keyword">const</span> middleware = <span class="hljs-function">(<span class="hljs-params">req, res, next</span>) =></span> &#123;
        <span class="hljs-keyword">let</span> route = matchRoute(req);

        <span class="hljs-keyword">if</span> (route) &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'mock request'</span>, route.method, route.path);
          res.send = send;
          route.handler(req, res);
        &#125; <span class="hljs-keyword">else</span> &#123;
          next();
        &#125;
      &#125;;
      app.use(middleware);
    &#125;,
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">视频教程</h3>
<p>除了以上基础内容之外，我还录制了<code>vite-plugin-vue-i18n</code>源码学习视频，包括国际化插件的安装、使用、原理和手写实现，精彩异常，欢迎小伙伴们来捧场：
<a href="https://www.bilibili.com/video/BV1jb4y1R7UV" target="_blank" rel="nofollow noopener noreferrer">【备战2021】Vite2插件开发指南「持续更新中」</a></p>
<p>原创不易，欢迎各位小伙伴<strong>三连+关注</strong>，您的鼓励是我坚持下去的最大动力❤️</p>
<h3 data-id="heading-12">配套源码</h3>
<p>欢迎关注公众号<code>村长学前端</code>自取</p>
<h3 data-id="heading-13">后续创作计划</h3>
<p>Vite为什么这么快，它能不能顶替webpack现在在前端的地位哪？我想小伙伴们一定和我一样有这样的疑问，后续我打算搞一搞Vite原理的剖析，并最终手写一个我们自己的Vite来。大家<code>点个赞👍，关注一下</code>，以便后续学习。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            