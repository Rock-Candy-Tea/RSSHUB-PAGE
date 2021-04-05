
---
title: 'React+Koa文件上传的实现'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3234'
author: 掘金
comments: false
date: Mon, 05 Apr 2021 02:13:11 GMT
thumbnail: 'https://picsum.photos/400/300?random=3234'
---

<div>   
<div class="markdown-body"><style>.markdown-body .octicon&#123;display:inline-block;fill:currentColor;vertical-align:text-bottom&#125;.markdown-body .anchor&#123;float:left;line-height:1;margin-left:-20px;padding-right:4px&#125;.markdown-body .anchor:focus&#123;outline:none&#125;.markdown-body h1 .octicon-link,.markdown-body h2 .octicon-link,.markdown-body h3 .octicon-link,.markdown-body h4 .octicon-link,.markdown-body h5 .octicon-link,.markdown-body h6 .octicon-link&#123;color:#1b1f23;vertical-align:middle;visibility:hidden&#125;.markdown-body h1:hover .anchor,.markdown-body h2:hover .anchor,.markdown-body h3:hover .anchor,.markdown-body h4:hover .anchor,.markdown-body h5:hover .anchor,.markdown-body h6:hover .anchor&#123;text-decoration:none&#125;.markdown-body h1:hover .anchor .octicon-link,.markdown-body h2:hover .anchor .octicon-link,.markdown-body h3:hover .anchor .octicon-link,.markdown-body h4:hover .anchor .octicon-link,.markdown-body h5:hover .anchor .octicon-link,.markdown-body h6:hover .anchor .octicon-link&#123;visibility:visible&#125;.markdown-body h1:hover .anchor .octicon-link:before,.markdown-body h2:hover .anchor .octicon-link:before,.markdown-body h3:hover .anchor .octicon-link:before,.markdown-body h4:hover .anchor .octicon-link:before,.markdown-body h5:hover .anchor .octicon-link:before,.markdown-body h6:hover .anchor .octicon-link:before&#123;width:16px;height:16px;content:" ";display:inline-block;background-image:url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' aria-hidden='true'%3E%3Cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z'/%3E%3C/svg%3E")&#125;.markdown-body&#123;-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%;color:#24292e;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif,Apple Color Emoji,Segoe UI Emoji;font-size:16px;line-height:1.5;word-wrap:break-word&#125;.markdown-body details&#123;display:block&#125;.markdown-body summary&#123;display:list-item&#125;.markdown-body a&#123;background-color:initial&#125;.markdown-body a:active,.markdown-body a:hover&#123;outline-width:0&#125;.markdown-body strong&#123;font-weight:inherit;font-weight:bolder&#125;.markdown-body h1&#123;margin:.67em 0&#125;.markdown-body img&#123;border-style:none&#125;.markdown-body code,.markdown-body kbd,.markdown-body pre&#123;font-family:monospace,monospace;font-size:1em&#125;.markdown-body hr&#123;box-sizing:initial;overflow:visible&#125;.markdown-body input&#123;font:inherit;margin:0;overflow:visible&#125;.markdown-body [type=checkbox]&#123;box-sizing:border-box;padding:0&#125;.markdown-body *&#123;box-sizing:border-box&#125;.markdown-body input&#123;font-family:inherit;font-size:inherit;line-height:inherit&#125;.markdown-body a&#123;color:#0366d6;text-decoration:none&#125;.markdown-body a:hover&#123;text-decoration:underline&#125;.markdown-body strong&#123;font-weight:600&#125;.markdown-body hr&#123;height:0;margin:15px 0;overflow:hidden;background:transparent;border-bottom:1px solid #dfe2e5&#125;.markdown-body hr:after,.markdown-body hr:before&#123;display:table;content:""&#125;.markdown-body hr:after&#123;clear:both&#125;.markdown-body table&#123;border-spacing:0;border-collapse:collapse&#125;.markdown-body td,.markdown-body th&#123;padding:0&#125;.markdown-body details summary&#123;cursor:pointer&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin-top:0;margin-bottom:0&#125;.markdown-body h1&#123;font-size:32px&#125;.markdown-body h1,.markdown-body h2&#123;font-weight:600&#125;.markdown-body h2&#123;font-size:24px&#125;.markdown-body h3&#123;font-size:20px&#125;.markdown-body h3,.markdown-body h4&#123;font-weight:600&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:14px&#125;.markdown-body h5,.markdown-body h6&#123;font-weight:600&#125;.markdown-body h6&#123;font-size:12px&#125;.markdown-body p&#123;margin-top:0;margin-bottom:10px&#125;.markdown-body blockquote&#123;margin:0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:0;margin-top:0;margin-bottom:0&#125;.markdown-body ol ol,.markdown-body ul ol&#123;list-style-type:lower-roman&#125;.markdown-body ol ol ol,.markdown-body ol ul ol,.markdown-body ul ol ol,.markdown-body ul ul ol&#123;list-style-type:lower-alpha&#125;.markdown-body dd&#123;margin-left:0&#125;.markdown-body code,.markdown-body pre&#123;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px&#125;.markdown-body pre&#123;margin-top:0;margin-bottom:0&#125;.markdown-body input::-webkit-inner-spin-button,.markdown-body input::-webkit-outer-spin-button&#123;margin:0;-webkit-appearance:none;appearance:none&#125;.markdown-body :checked+.radio-label&#123;position:relative;z-index:1;border-color:#0366d6&#125;.markdown-body .border&#123;border:1px solid #e1e4e8!important&#125;.markdown-body .border-0&#123;border:0!important&#125;.markdown-body .border-bottom&#123;border-bottom:1px solid #e1e4e8!important&#125;.markdown-body .rounded-1&#123;border-radius:3px!important&#125;.markdown-body .bg-white&#123;background-color:#fff!important&#125;.markdown-body .bg-gray-light&#123;background-color:#fafbfc!important&#125;.markdown-body .text-gray-light&#123;color:#6a737d!important&#125;.markdown-body .pl-3,.markdown-body .px-3&#123;padding-left:16px!important&#125;.markdown-body .px-3&#123;padding-right:16px!important&#125;.markdown-body .f6&#123;font-size:12px!important&#125;.markdown-body .lh-condensed&#123;line-height:1.25!important&#125;.markdown-body .text-bold&#123;font-weight:600!important&#125;.markdown-body .pl-c&#123;color:#6a737d&#125;.markdown-body .pl-c1,.markdown-body .pl-s .pl-v&#123;color:#005cc5&#125;.markdown-body .pl-e,.markdown-body .pl-en&#123;color:#6f42c1&#125;.markdown-body .pl-s .pl-s1,.markdown-body .pl-smi&#123;color:#24292e&#125;.markdown-body .pl-ent&#123;color:#22863a&#125;.markdown-body .pl-k&#123;color:#d73a49&#125;.markdown-body .pl-pds,.markdown-body .pl-s,.markdown-body .pl-s .pl-pse .pl-s1,.markdown-body .pl-sr,.markdown-body .pl-sr .pl-cce,.markdown-body .pl-sr .pl-sra,.markdown-body .pl-sr .pl-sre&#123;color:#032f62&#125;.markdown-body .pl-smw,.markdown-body .pl-v&#123;color:#e36209&#125;.markdown-body .pl-bu&#123;color:#b31d28&#125;.markdown-body .pl-ii&#123;color:#fafbfc;background-color:#b31d28&#125;.markdown-body .pl-c2&#123;color:#fafbfc;background-color:#d73a49&#125;.markdown-body .pl-c2:before&#123;content:"^M"&#125;.markdown-body .pl-sr .pl-cce&#123;font-weight:700;color:#22863a&#125;.markdown-body .pl-ml&#123;color:#735c0f&#125;.markdown-body .pl-mh,.markdown-body .pl-mh .pl-en,.markdown-body .pl-ms&#123;font-weight:700;color:#005cc5&#125;.markdown-body .pl-mi&#123;font-style:italic;color:#24292e&#125;.markdown-body .pl-mb&#123;font-weight:700;color:#24292e&#125;.markdown-body .pl-md&#123;color:#b31d28;background-color:#ffeef0&#125;.markdown-body .pl-mi1&#123;color:#22863a;background-color:#f0fff4&#125;.markdown-body .pl-mc&#123;color:#e36209;background-color:#ffebda&#125;.markdown-body .pl-mi2&#123;color:#f6f8fa;background-color:#005cc5&#125;.markdown-body .pl-mdr&#123;font-weight:700;color:#6f42c1&#125;.markdown-body .pl-ba&#123;color:#586069&#125;.markdown-body .pl-sg&#123;color:#959da5&#125;.markdown-body .pl-corl&#123;text-decoration:underline;color:#032f62&#125;.markdown-body .mb-0&#123;margin-bottom:0!important&#125;.markdown-body .my-2&#123;margin-bottom:8px!important;margin-top:8px!important&#125;.markdown-body .pl-0&#123;padding-left:0!important&#125;.markdown-body .py-0&#123;padding-top:0!important;padding-bottom:0!important&#125;.markdown-body .pl-1&#123;padding-left:4px!important&#125;.markdown-body .pl-2&#123;padding-left:8px!important&#125;.markdown-body .py-2&#123;padding-top:8px!important;padding-bottom:8px!important&#125;.markdown-body .pl-3&#123;padding-left:16px!important&#125;.markdown-body .pl-4&#123;padding-left:24px!important&#125;.markdown-body .pl-5&#123;padding-left:32px!important&#125;.markdown-body .pl-6&#123;padding-left:40px!important&#125;.markdown-body .pl-7&#123;padding-left:48px!important&#125;.markdown-body .pl-8&#123;padding-left:64px!important&#125;.markdown-body .pl-9&#123;padding-left:80px!important&#125;.markdown-body .pl-10&#123;padding-left:96px!important&#125;.markdown-body .pl-11&#123;padding-left:112px!important&#125;.markdown-body .pl-12&#123;padding-left:128px!important&#125;.markdown-body hr&#123;border-bottom-color:#eee&#125;.markdown-body kbd&#123;display:inline-block;padding:3px 5px;font:11px SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;line-height:10px;color:#444d56;vertical-align:middle;background-color:#fafbfc;border:1px solid #d1d5da;border-radius:3px;box-shadow:inset 0 -1px 0 #d1d5da&#125;.markdown-body:after,.markdown-body:before&#123;display:table;content:""&#125;.markdown-body:after&#123;clear:both&#125;.markdown-body>:first-child&#123;margin-top:0!important&#125;.markdown-body>:last-child&#123;margin-bottom:0!important&#125;.markdown-body a:not([href])&#123;color:inherit;text-decoration:none&#125;.markdown-body blockquote,.markdown-body details,.markdown-body dl,.markdown-body ol,.markdown-body p,.markdown-body pre,.markdown-body table,.markdown-body ul&#123;margin-top:0;margin-bottom:16px&#125;.markdown-body hr&#123;height:.25em;padding:0;margin:24px 0;background-color:#e1e4e8;border:0&#125;.markdown-body blockquote&#123;padding:0 1em;color:#6a737d;border-left:.25em solid #dfe2e5&#125;.markdown-body blockquote>:first-child&#123;margin-top:0&#125;.markdown-body blockquote>:last-child&#123;margin-bottom:0&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin-top:24px;margin-bottom:16px;font-weight:600;line-height:1.25&#125;.markdown-body h1&#123;font-size:2em&#125;.markdown-body h1,.markdown-body h2&#123;padding-bottom:.3em;border-bottom:1px solid #eaecef&#125;.markdown-body h2&#123;font-size:1.5em&#125;.markdown-body h3&#123;font-size:1.25em&#125;.markdown-body h4&#123;font-size:1em&#125;.markdown-body h5&#123;font-size:.875em&#125;.markdown-body h6&#123;font-size:.85em;color:#6a737d&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:0;margin-bottom:0&#125;.markdown-body li&#123;word-wrap:break-all&#125;.markdown-body li>p&#123;margin-top:16px&#125;.markdown-body li+li&#123;margin-top:.25em&#125;.markdown-body dl&#123;padding:0&#125;.markdown-body dl dt&#123;padding:0;margin-top:16px;font-size:1em;font-style:italic;font-weight:600&#125;.markdown-body dl dd&#123;padding:0 16px;margin-bottom:16px&#125;.markdown-body table&#123;display:block;width:100%;overflow:auto&#125;.markdown-body table th&#123;font-weight:600&#125;.markdown-body table td,.markdown-body table th&#123;padding:6px 13px;border:1px solid #dfe2e5&#125;.markdown-body table tr&#123;background-color:#fff;border-top:1px solid #c6cbd1&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;.markdown-body img&#123;max-width:100%;box-sizing:initial;background-color:#fff&#125;.markdown-body img[align=right]&#123;padding-left:20px&#125;.markdown-body img[align=left]&#123;padding-right:20px&#125;.markdown-body code&#123;padding:.2em .4em;margin:0;font-size:85%;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body pre&#123;word-wrap:normal&#125;.markdown-body pre>code&#123;padding:0;margin:0;font-size:100%;word-break:normal;white-space:pre;background:transparent;border:0&#125;.markdown-body .highlight&#123;margin-bottom:16px&#125;.markdown-body .highlight pre&#123;margin-bottom:0;word-break:normal&#125;.markdown-body .highlight pre,.markdown-body pre&#123;padding:16px;overflow:auto;font-size:85%;line-height:1.45;background-color:#f6f8fa;border-radius:3px&#125;.markdown-body pre code&#123;display:inline;max-width:auto;padding:0;margin:0;overflow:visible;line-height:inherit;word-wrap:normal;background-color:initial;border:0&#125;.markdown-body .commit-tease-sha&#123;display:inline-block;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:90%;color:#444d56&#125;.markdown-body .full-commit .btn-outline:not(:disabled):hover&#123;color:#005cc5;border-color:#005cc5&#125;.markdown-body .blob-wrapper&#123;overflow-x:auto;overflow-y:hidden&#125;.markdown-body .blob-wrapper-embedded&#123;max-height:240px;overflow-y:auto&#125;.markdown-body .blob-num&#123;width:1%;min-width:50px;padding-right:10px;padding-left:10px;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px;line-height:20px;color:rgba(27,31,35,.3);text-align:right;white-space:nowrap;vertical-align:top;cursor:pointer;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none&#125;.markdown-body .blob-num:hover&#123;color:rgba(27,31,35,.6)&#125;.markdown-body .blob-num:before&#123;content:attr(data-line-number)&#125;.markdown-body .blob-code&#123;position:relative;padding-right:10px;padding-left:10px;line-height:20px;vertical-align:top&#125;.markdown-body .blob-code-inner&#123;overflow:visible;font-family:SFMono-Regular,Consolas,Liberation Mono,Menlo,monospace;font-size:12px;color:#24292e;word-wrap:normal;white-space:pre&#125;.markdown-body .pl-token.active,.markdown-body .pl-token:hover&#123;cursor:pointer;background:#ffea7f&#125;.markdown-body .tab-size[data-tab-size="1"]&#123;-moz-tab-size:1;tab-size:1&#125;.markdown-body .tab-size[data-tab-size="2"]&#123;-moz-tab-size:2;tab-size:2&#125;.markdown-body .tab-size[data-tab-size="3"]&#123;-moz-tab-size:3;tab-size:3&#125;.markdown-body .tab-size[data-tab-size="4"]&#123;-moz-tab-size:4;tab-size:4&#125;.markdown-body .tab-size[data-tab-size="5"]&#123;-moz-tab-size:5;tab-size:5&#125;.markdown-body .tab-size[data-tab-size="6"]&#123;-moz-tab-size:6;tab-size:6&#125;.markdown-body .tab-size[data-tab-size="7"]&#123;-moz-tab-size:7;tab-size:7&#125;.markdown-body .tab-size[data-tab-size="8"]&#123;-moz-tab-size:8;tab-size:8&#125;.markdown-body .tab-size[data-tab-size="9"]&#123;-moz-tab-size:9;tab-size:9&#125;.markdown-body .tab-size[data-tab-size="10"]&#123;-moz-tab-size:10;tab-size:10&#125;.markdown-body .tab-size[data-tab-size="11"]&#123;-moz-tab-size:11;tab-size:11&#125;.markdown-body .tab-size[data-tab-size="12"]&#123;-moz-tab-size:12;tab-size:12&#125;.markdown-body .task-list-item&#123;list-style-type:none&#125;.markdown-body .task-list-item+.task-list-item&#123;margin-top:3px&#125;.markdown-body .task-list-item input&#123;margin:0 .2em .25em -1.6em;vertical-align:middle&#125;</style><h1 data-id="heading-0">背景</h1>
<p>最近在写毕设的时候，涉及到了一些文件上传的功能，其中包括了普通文件上传，大文件上传，断点续传等等</p>
<h1 data-id="heading-1">服务端依赖</h1>
<ul>
<li>koa(node.js框架)</li>
<li>koa-router(Koa路由)</li>
<li>koa-body(Koa body 解析中间件，可以用于解析post请求内容)</li>
<li>koa-static-cache(Koa 静态资源中间件，用于处理静态资源请求)</li>
<li>koa-bodyparser(解析 request.body 的内容)</li>
</ul>
<h3 data-id="heading-2">后端配置跨域</h3>
<pre><code class="hljs language-js copyable" lang="js">app.use(<span class="hljs-keyword">async</span> (ctx, next) => &#123;
  ctx.set(<span class="hljs-string">'Access-Control-Allow-Origin'</span>, <span class="hljs-string">'*'</span>);
  ctx.set(
    <span class="hljs-string">'Access-Control-Allow-Headers'</span>,
    <span class="hljs-string">'Content-Type, Content-Length, Authorization, Accept, X-Requested-With , yourHeaderFeild'</span>,
  );
  ctx.set(<span class="hljs-string">'Access-Control-Allow-Methods'</span>, <span class="hljs-string">'PUT, POST, GET, DELETE, OPTIONS'</span>);
  <span class="hljs-keyword">if</span> (ctx.method == <span class="hljs-string">'OPTIONS'</span>) &#123;
    ctx.body = <span class="hljs-number">200</span>;
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-keyword">await</span> next();
  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">后端配置静态资源访问 使用 <code>koa-static-cache</code></h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 静态资源处理</span>
app.use(
  KoaStaticCache(<span class="hljs-string">'./pulbic'</span>, &#123;
    <span class="hljs-attr">prefix</span>: <span class="hljs-string">'/public'</span>,
    <span class="hljs-attr">dynamic</span>: <span class="hljs-literal">true</span>,
    <span class="hljs-attr">gzip</span>: <span class="hljs-literal">true</span>,
  &#125;),
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">后端配置requst body parse 使用 <code>koa-bodyparser</code></h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> bodyParser = <span class="hljs-built_in">require</span>(<span class="hljs-string">'koa-bodyparser'</span>);
app.use(bodyParser());

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">前端依赖</h1>
<ul>
<li>React</li>
<li>Antd</li>
<li>axios</li>
</ul>
<h1 data-id="heading-6">正常文件上传</h1>
<h3 data-id="heading-7">后端</h3>
<p>后端只需要使用 <code>koa-body</code> 配置好options，作为中间件，传入<code>router.post('url',middleware,callback)</code>即可</p>
<ul>
<li>
<p>后端代码</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">// 上传配置</span>
<span class="hljs-keyword">const</span> uploadOptions = &#123;
<span class="hljs-comment">// 支持文件格式</span>
  <span class="hljs-attr">multipart</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">formidable</span>: &#123;
    <span class="hljs-comment">// 上传目录 这边直接上传到public文件夹，方便访问 文件夹后面要记得加/</span>
    <span class="hljs-attr">uploadDir</span>: path.join(__dirname, <span class="hljs-string">'../../pulbic/'</span>),
    <span class="hljs-comment">// 保留文件扩展名</span>
    <span class="hljs-attr">keepExtensions</span>: <span class="hljs-literal">true</span>,
  &#125;,
&#125;;
router.post(<span class="hljs-string">'/upload'</span>, <span class="hljs-keyword">new</span> KoaBody(uploadOptions), <span class="hljs-function">(<span class="hljs-params">ctx, next</span>) =></span> &#123;
  <span class="hljs-comment">// 获取上传的文件</span>
  <span class="hljs-keyword">const</span> file = ctx.request.files.file;
  <span class="hljs-keyword">const</span> fileName = file.path.split(<span class="hljs-string">'/'</span>)[file.path.split(<span class="hljs-string">'/'</span>).length-<span class="hljs-number">1</span>];
  ctx.body = &#123;
      <span class="hljs-attr">code</span>:<span class="hljs-number">0</span>,
      <span class="hljs-attr">data</span>:&#123;
        <span class="hljs-attr">url</span>:<span class="hljs-string">`public/<span class="hljs-subst">$&#123;fileName&#125;</span>`</span>
      &#125;,
      <span class="hljs-attr">message</span>:<span class="hljs-string">'success'</span>

  &#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-8">前端</h3>
<p>  我这里使用的是formData传递的方式，前端通过<code><input type='file'/></code> 来访问文件选择器，通过<code>onChange事件 e.target.files[0]</code> 即可获取选择的文件，而后创建<code>FormData 对象</code>将获取的文件<code>formData.append('file',targetFile)</code>即可</p>
<ul>
<li>前端代码
<pre><code class="hljs language-js copyable" lang="js">     <span class="hljs-keyword">const</span> Upload = <span class="hljs-function">() =></span> &#123;
     <span class="hljs-keyword">const</span> [url, setUrl] = useState<string>(<span class="hljs-string">''</span>)
     <span class="hljs-keyword">const</span> handleClickUpload = <span class="hljs-function">() =></span> &#123;
         <span class="hljs-keyword">const</span> fileLoader = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'#btnFile'</span>) <span class="hljs-keyword">as</span> HTMLInputElement;
         <span class="hljs-keyword">if</span> (isNil(fileLoader)) &#123;
             <span class="hljs-keyword">return</span>;
         &#125;
         fileLoader.click();
     &#125;
     <span class="hljs-keyword">const</span> handleUpload = <span class="hljs-keyword">async</span> (e: any) => &#123;
         <span class="hljs-comment">//获取上传文件</span>
         <span class="hljs-keyword">const</span> file = e.target.files[<span class="hljs-number">0</span>];
         <span class="hljs-keyword">const</span> formData = <span class="hljs-keyword">new</span> FormData()
         formData.append(<span class="hljs-string">'file'</span>, file);
         <span class="hljs-comment">// 上传文件</span>
         <span class="hljs-keyword">const</span> &#123; data &#125; = <span class="hljs-keyword">await</span> uploadSmallFile(formData);
         <span class="hljs-built_in">console</span>.log(data.url);
         setUrl(<span class="hljs-string">`<span class="hljs-subst">$&#123;baseURL&#125;</span><span class="hljs-subst">$&#123;data.url&#125;</span>`</span>);
     &#125;
     <span class="hljs-keyword">return</span> (
         <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
             <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"file"</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"btnFile"</span> <span class="hljs-attr">onChange</span>=<span class="hljs-string">&#123;handleUpload&#125;</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;</span> <span class="hljs-attr">display:</span> '<span class="hljs-attr">none</span>' &#125;&#125; /></span>
             <span class="hljs-tag"><<span class="hljs-name">Button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;handleClickUpload&#125;</span>></span>上传小文件<span class="hljs-tag"></<span class="hljs-name">Button</span>></span>
             <span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">&#123;url&#125;</span> /></span>
         <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
     )
 &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>其他可选方法
<ul>
<li><code>input+form</code> 设置form的aciton为后端页面，enctype="multipart/form-data"，type=‘post’</li>
<li><code>使用fileReader读取文件数据进行上传</code> 兼容性不是特别好</li>
</ul>
</li>
</ul>
<h1 data-id="heading-9">大文件上传</h1>
<p>  文件上传的时候，可能会因为文件过大，导致请求超时，这时候就可以采取分片的方式,简单来说就是将文件拆分为一个个小块，传给服务器，这些小块标识了自己属于哪一个文件的哪一个位置，在所有小块传递完毕后，后端执行<code>merge</code> 将这些文件合并了完整文件，完成整个传输过程</p>
<h3 data-id="heading-10">前端</h3>
<ul>
<li>获取文件和前面一样，不再赘述</li>
<li>设置默认分片大小，文件切片，每一片名字为 <code>filename.index.ext</code>，递归请求直到整个文件发送完请求合并</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">const</span> handleUploadLarge = <span class="hljs-keyword">async</span> (e: any) => &#123;
          <span class="hljs-comment">//获取上传文件</span>
          <span class="hljs-keyword">const</span> file = e.target.files[<span class="hljs-number">0</span>];
          <span class="hljs-comment">// 对于文件分片</span>
          <span class="hljs-keyword">await</span> uploadEveryChunk(file, <span class="hljs-number">0</span>);
      &#125;
      <span class="hljs-keyword">const</span> uploadEveryChunk = <span class="hljs-function">(<span class="hljs-params">
          file: File,
          index: number,
      </span>) =></span> &#123;
          <span class="hljs-built_in">console</span>.log(index);
          <span class="hljs-keyword">const</span> chunkSize = <span class="hljs-number">512</span>; <span class="hljs-comment">// 分片宽度</span>
          <span class="hljs-comment">// [ 文件名, 文件后缀 ]</span>
          <span class="hljs-keyword">const</span> [fname, fext] = file.name.split(<span class="hljs-string">'.'</span>);
          <span class="hljs-comment">// 获取当前片的起始字节</span>
          <span class="hljs-keyword">const</span> start = index * chunkSize;
          <span class="hljs-keyword">if</span> (start > file.size) &#123;
              <span class="hljs-comment">// 当超出文件大小，停止递归上传</span>
              <span class="hljs-keyword">return</span> mergeLargeFile(file.name);
          &#125;
          <span class="hljs-keyword">const</span> blob = file.slice(start, start + chunkSize);
          <span class="hljs-comment">// 为每片进行命名</span>
          <span class="hljs-keyword">const</span> blobName = <span class="hljs-string">`<span class="hljs-subst">$&#123;fname&#125;</span>.<span class="hljs-subst">$&#123;index&#125;</span>.<span class="hljs-subst">$&#123;fext&#125;</span>`</span>;
          <span class="hljs-keyword">const</span> blobFile = <span class="hljs-keyword">new</span> File([blob], blobName);
          <span class="hljs-keyword">const</span> formData = <span class="hljs-keyword">new</span> FormData();
          formData.append(<span class="hljs-string">'file'</span>, blobFile);
          uploadLargeFile(formData).then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
              <span class="hljs-comment">// 递归分片上传</span>
              uploadEveryChunk(file, ++index);
          &#125;);
      &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">后端</h3>
<p>后端需要提供两个接口</p>
<h4 data-id="heading-12">上传</h4>
<p>将上传的每一个分块存储到对应<code>name</code> 的文件夹，便于之后合并</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> uploadStencilPreviewOptions = &#123;
<span class="hljs-attr">multipart</span>: <span class="hljs-literal">true</span>,
<span class="hljs-attr">formidable</span>: &#123;
  <span class="hljs-attr">uploadDir</span>: path.resolve(__dirname, <span class="hljs-string">'../../temp/'</span>), <span class="hljs-comment">// 文件存放地址</span>
  <span class="hljs-attr">keepExtensions</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">maxFieldsSize</span>: <span class="hljs-number">2</span> * <span class="hljs-number">1024</span> * <span class="hljs-number">1024</span>,
&#125;,
&#125;;

router.post(<span class="hljs-string">'/upload_chunk'</span>, <span class="hljs-keyword">new</span> KoaBody(uploadStencilPreviewOptions), <span class="hljs-keyword">async</span> (ctx) => &#123;
<span class="hljs-keyword">try</span> &#123;
  <span class="hljs-keyword">const</span> file = ctx.request.files.file;
  <span class="hljs-comment">// [ name, index, ext ] - 分割文件名</span>
  <span class="hljs-keyword">const</span> fileNameArr = file.name.split(<span class="hljs-string">'.'</span>);

  <span class="hljs-keyword">const</span> UPLOAD_DIR = path.resolve(__dirname, <span class="hljs-string">'../../temp'</span>);
  <span class="hljs-comment">// 存放切片的目录</span>
  <span class="hljs-keyword">const</span> chunkDir = <span class="hljs-string">`<span class="hljs-subst">$&#123;UPLOAD_DIR&#125;</span>/<span class="hljs-subst">$&#123;fileNameArr[<span class="hljs-number">0</span>]&#125;</span>`</span>;
  <span class="hljs-keyword">if</span> (!fse.existsSync(chunkDir)) &#123;
    <span class="hljs-comment">// 没有目录就创建目录</span>
    <span class="hljs-comment">// 创建大文件的临时目录</span>
    <span class="hljs-keyword">await</span> fse.mkdirs(chunkDir);
  &#125;
  <span class="hljs-comment">// 原文件名.index - 每个分片的具体地址和名字</span>
  <span class="hljs-keyword">const</span> dPath = path.join(chunkDir, fileNameArr[<span class="hljs-number">1</span>]);

  <span class="hljs-comment">// 将分片文件从 temp 中移动到本次上传大文件的临时目录</span>
  <span class="hljs-keyword">await</span> fse.move(file.path, dPath, &#123; <span class="hljs-attr">overwrite</span>: <span class="hljs-literal">true</span> &#125;);
  ctx.body = &#123;
    <span class="hljs-attr">code</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">message</span>: <span class="hljs-string">'文件上传成功'</span>,
  &#125;;
&#125; <span class="hljs-keyword">catch</span> (e) &#123;
  ctx.body = &#123;
    <span class="hljs-attr">code</span>: -<span class="hljs-number">1</span>,
    <span class="hljs-attr">message</span>: <span class="hljs-string">`文件上传失败:<span class="hljs-subst">$&#123;e.toString()&#125;</span>`</span>,
  &#125;;
&#125;
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">合并</h4>
<p>  根据前端传来合并请求，携带的<code>name</code>去临时缓存大文件分块的文件夹找到属于该<code>name</code>的文件夹，根据index顺序读取chunks后，合并文件<code>fse.appendFileSync(path,data)</code> (按顺序追加写即合并),然后删除临时存储的文件夹释放内存空间</p>
<pre><code class="hljs language-js copyable" lang="js">router.post(<span class="hljs-string">'/merge_chunk'</span>, <span class="hljs-keyword">async</span> (ctx) => &#123;
 <span class="hljs-keyword">try</span> &#123;
   <span class="hljs-keyword">const</span> &#123; fileName &#125; = ctx.request.body;
   <span class="hljs-keyword">const</span> fname = fileName.split(<span class="hljs-string">'.'</span>)[<span class="hljs-number">0</span>];
   <span class="hljs-keyword">const</span> TEMP_DIR = path.resolve(__dirname, <span class="hljs-string">'../../temp'</span>);
   <span class="hljs-keyword">const</span> static_preview_url = <span class="hljs-string">'/public/previews'</span>;
   <span class="hljs-keyword">const</span> STORAGE_DIR = path.resolve(__dirname, <span class="hljs-string">`../..<span class="hljs-subst">$&#123;static_preview_url&#125;</span>`</span>);
   <span class="hljs-keyword">const</span> chunkDir = path.join(TEMP_DIR, fname);
   <span class="hljs-keyword">const</span> chunks = <span class="hljs-keyword">await</span> fse.readdir(chunkDir);
   chunks
     .sort(<span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> a - b)
     .map(<span class="hljs-function">(<span class="hljs-params">chunkPath</span>) =></span> &#123;
       <span class="hljs-comment">// 合并文件</span>
       fse.appendFileSync(
         path.join(STORAGE_DIR, fileName),
         fse.readFileSync(<span class="hljs-string">`<span class="hljs-subst">$&#123;chunkDir&#125;</span>/<span class="hljs-subst">$&#123;chunkPath&#125;</span>`</span>),
       );
     &#125;);
   <span class="hljs-comment">// 删除临时文件夹</span>
   fse.removeSync(chunkDir);
   <span class="hljs-comment">// 图片访问的url</span>
   <span class="hljs-keyword">const</span> url = <span class="hljs-string">`http://<span class="hljs-subst">$&#123;ctx.request.header.host&#125;</span><span class="hljs-subst">$&#123;static_preview_url&#125;</span>/<span class="hljs-subst">$&#123;fileName&#125;</span>`</span>;
   ctx.body = &#123;
     <span class="hljs-attr">code</span>: <span class="hljs-number">0</span>,
     <span class="hljs-attr">data</span>: &#123; url &#125;,
     <span class="hljs-attr">message</span>: <span class="hljs-string">'success'</span>,
   &#125;;
 &#125; <span class="hljs-keyword">catch</span> (e) &#123;
   ctx.body = &#123; <span class="hljs-attr">code</span>: -<span class="hljs-number">1</span>, <span class="hljs-attr">message</span>: <span class="hljs-string">`合并失败:<span class="hljs-subst">$&#123;e.toString()&#125;</span>`</span> &#125;;
 &#125;
&#125;);

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-14">断点续传</h1>
<p>  大文件在传输过程中，如果刷新页面或者临时的失败导致传输失败，又需要从头传输对于用户的体验是很不好的。因此就需要在传输失败的位置，做好标记，下一次直接在这里进行传输即可，我采取的是在<code>localStorage</code>读写的方式</p>
<pre><code class="hljs language-js copyable" lang="js">   <span class="hljs-keyword">const</span> handleUploadLarge = <span class="hljs-keyword">async</span> (e: any) => &#123;
       <span class="hljs-comment">//获取上传文件</span>
       <span class="hljs-keyword">const</span> file = e.target.files[<span class="hljs-number">0</span>];
       <span class="hljs-keyword">const</span> record = <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-built_in">localStorage</span>.getItem(<span class="hljs-string">'uploadRecord'</span>) <span class="hljs-keyword">as</span> any);
       <span class="hljs-keyword">if</span> (!isNil(record)) &#123;
           <span class="hljs-comment">// 这里为了便于展示，先不考虑碰撞问题, 判断文件是否是同一个可以使用hash文件的方式</span>
           <span class="hljs-comment">// 对于大文件可以采用hash(一块文件+文件size)的方式来判断两文件是否相同</span>
           <span class="hljs-keyword">if</span>(record.name === file.name)&#123;
               <span class="hljs-keyword">return</span> <span class="hljs-keyword">await</span> uploadEveryChunk(file, record.index);
           &#125;
       &#125;
       <span class="hljs-comment">// 对于文件分片</span>
       <span class="hljs-keyword">await</span> uploadEveryChunk(file, <span class="hljs-number">0</span>);
   &#125;
   <span class="hljs-keyword">const</span> uploadEveryChunk = <span class="hljs-function">(<span class="hljs-params">
       file: File,
       index: number,
   </span>) =></span> &#123;
       <span class="hljs-keyword">const</span> chunkSize = <span class="hljs-number">512</span>; <span class="hljs-comment">// 分片宽度</span>
       <span class="hljs-comment">// [ 文件名, 文件后缀 ]</span>
       <span class="hljs-keyword">const</span> [fname, fext] = file.name.split(<span class="hljs-string">'.'</span>);
       <span class="hljs-comment">// 获取当前片的起始字节</span>
       <span class="hljs-keyword">const</span> start = index * chunkSize;
       <span class="hljs-keyword">if</span> (start > file.size) &#123;
           <span class="hljs-comment">// 当超出文件大小，停止递归上传</span>
           <span class="hljs-keyword">return</span> mergeLargeFile(file.name).then(<span class="hljs-function">()=></span>&#123;
               <span class="hljs-comment">// 合并成功以后删除记录</span>
               <span class="hljs-built_in">localStorage</span>.removeItem(<span class="hljs-string">'uploadRecord'</span>)
           &#125;);
       &#125;
       <span class="hljs-keyword">const</span> blob = file.slice(start, start + chunkSize);
       <span class="hljs-comment">// 为每片进行命名</span>
       <span class="hljs-keyword">const</span> blobName = <span class="hljs-string">`<span class="hljs-subst">$&#123;fname&#125;</span>.<span class="hljs-subst">$&#123;index&#125;</span>.<span class="hljs-subst">$&#123;fext&#125;</span>`</span>;
       <span class="hljs-keyword">const</span> blobFile = <span class="hljs-keyword">new</span> File([blob], blobName);
       <span class="hljs-keyword">const</span> formData = <span class="hljs-keyword">new</span> FormData();
       formData.append(<span class="hljs-string">'file'</span>, blobFile);
       uploadLargeFile(formData).then(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
           <span class="hljs-comment">// 传输成功每一块的返回后记录位置</span>
           <span class="hljs-built_in">localStorage</span>.setItem(<span class="hljs-string">'uploadRecord'</span>,<span class="hljs-built_in">JSON</span>.stringify(&#123;
               <span class="hljs-attr">name</span>:file.name,
               <span class="hljs-attr">index</span>:index+<span class="hljs-number">1</span>
           &#125;))
           <span class="hljs-comment">// 递归分片上传</span>
           uploadEveryChunk(file, ++index);
       &#125;);
   &#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-15">文件相同判断</h1>
<p>  通过计算文件MD5,hash等方式均可，当文件过大时，进行hash可能会花费较大的时间。
可取文件的一块<code>chunk</code>与文件的大小进行hash,进行局部的采样比对，
这里展示 通过 <code>crypto-js</code>库进行计算md5，FileReader读取文件的代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 计算md5 看是否已经存在</span>
     <span class="hljs-keyword">const</span> sign = tempFile.slice(<span class="hljs-number">0</span>, <span class="hljs-number">512</span>);
     <span class="hljs-keyword">const</span> signFile = <span class="hljs-keyword">new</span> File(
       [sign, (tempFile.size <span class="hljs-keyword">as</span> unknown) <span class="hljs-keyword">as</span> BlobPart],
       <span class="hljs-string">''</span>,
     );
     <span class="hljs-keyword">const</span> reader = <span class="hljs-keyword">new</span> FileReader();
     reader.onload = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">event</span>) </span>&#123;
       <span class="hljs-keyword">const</span> binary = event?.target?.result;
       <span class="hljs-keyword">const</span> md5 = binary && CryptoJs.MD5(binary <span class="hljs-keyword">as</span> string).toString();
       <span class="hljs-keyword">const</span> record = <span class="hljs-built_in">localStorage</span>.getItem(<span class="hljs-string">'upLoadMD5'</span>);
       <span class="hljs-keyword">if</span> (isNil(md5)) &#123;
         <span class="hljs-keyword">const</span> file = blobToFile(blob, <span class="hljs-string">`<span class="hljs-subst">$&#123;getRandomFileName()&#125;</span>.png`</span>);
         <span class="hljs-keyword">return</span> uploadPreview(file, <span class="hljs-number">0</span>, md5);
       &#125;
       <span class="hljs-keyword">const</span> file = blobToFile(blob, <span class="hljs-string">`<span class="hljs-subst">$&#123;md5&#125;</span>.png`</span>);
       <span class="hljs-keyword">if</span> (isNil(record)) &#123;
         <span class="hljs-comment">// 直接从头传 记录这个md5</span>
         <span class="hljs-keyword">return</span> uploadPreview(file, <span class="hljs-number">0</span>, md5);
       &#125;
       <span class="hljs-keyword">const</span> recordObj = <span class="hljs-built_in">JSON</span>.parse(record);
       <span class="hljs-keyword">if</span> (recordObj.md5 == md5) &#123;
         <span class="hljs-comment">// 从记录位置开始传</span>
         <span class="hljs-comment">//断点续传</span>
         <span class="hljs-keyword">return</span> uploadPreview(file, recordObj.index, md5);
       &#125;
       <span class="hljs-keyword">return</span> uploadPreview(file, <span class="hljs-number">0</span>, md5);
     &#125;;
     reader.readAsBinaryString(signFile);

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-16">总结</h1>
<p>  之前一直对于上传文件没有过太多的了解，通过毕设的这个功能，对于上传文件的前后端代码有了初步的认识，可能这些方法也只是其中的选项并不包括所有，希望未来的学习中能够不断的完善。<br>
  第一次在掘金写博客，在参加实习以后，发现自己的知识体量的不足，希望能够通过坚持写博客的方式，来梳理自己的知识体系，记录自己的学习历程，也希望各位大神在发现问题时不吝赐教，thx</p>
<p><code>即使最后没有人为你鼓掌，也要优雅的谢幕，感谢自己的认真付出</code></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            