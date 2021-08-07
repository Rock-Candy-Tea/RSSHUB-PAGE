
---
title: 'webpack多页面打包配置方案'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a3ed439076f464399d0e95dd4ebd006~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 06 Aug 2021 19:20:37 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a3ed439076f464399d0e95dd4ebd006~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第7天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h1 data-id="heading-0">多页面应用打包方案</h1>
<p> </p>
<h3 data-id="heading-1">先来说说什么是单页面应用和多页面应用：</h3>
<ul>
<li>
<p>单页面应用（SPA），通俗一点说就是指只有一个主页面的应用，浏览器一开始要加载所有必须的 html, js, css。所有的页面内容都包含在这个所谓的主页面中。</p>
</li>
<li>
<p>多页面（MPA），就是指一个应用中有多个页面，页面跳转时是整页刷新。</p>
</li>
</ul>
<p> </p>
<h4 data-id="heading-2">单页面的优点和缺点：</h4>
<p><strong>优点</strong>：</p>
<ol>
<li>
<p>用户体验好，快，内容的改变不需要重新加载整个页面，对服务器压力较小。</p>
</li>
<li>
<p>前后端分离，比如vue项目</p>
</li>
<li>
<p>完全的前端组件化，前端开发不再以页面为单位，更多地采用组件化的思想，代码结构和组织方式更加规范化，便于修改和调整；</p>
</li>
</ol>
<p><strong>缺点</strong>：</p>
<ol>
<li>
<p>首次加载页面的时候需要加载大量的静态资源，这个加载时间相对比较长。</p>
</li>
<li>
<p>不利于 SEO优化，单页页面，数据在前端渲染，就意味着没有 SEO。多页面应用有利于SEO</p>
</li>
<li>
<p>页面导航不可用，如果一定要导航需要自行实现前进、后退。（由于是单页面不能用浏览器的前进后退功能，所以需要自己建立堆栈管理）</p>
</li>
</ol>
<p> </p>
<h4 data-id="heading-3">多页面应用优势：</h4>
<ol>
<li>页面之间解耦</li>
<li>有利于SEO</li>
</ol>
<p> 
 </p>
<h1 data-id="heading-4">多页面应用打包基本思路</h1>
<p>每个页面对应一个entry，一个html-webpack-plugin
缺点：每次新增挥着删除页面都需要更改webpack配置
比如：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">entry: &#123;
  <span class="hljs-attr">index</span>:<span class="hljs-string">'./src/index.js'</span>,
  <span class="hljs-attr">add</span>:<span class="hljs-string">'./src/add.js'</span>
&#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">优化</h4>
<p>可以过<strong>程序的思维</strong>，每次动态的获取某一个目录下面指定的入口文件（约定：所有目录都放在/src下面，每个页面的入口文件都约定为index.js比如 /src/index/index.js  或  /src/search/index.js）
<strong>项目目录</strong>：
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a3ed439076f464399d0e95dd4ebd006~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>可以使用 glob，用来匹配文件</strong>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/69245851fbc846df9ba480a17ef87c43~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-6">配置如下</h1>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> setMPA = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> entry = &#123;&#125;;
  <span class="hljs-keyword">const</span> htmlWebpackPlugins = [];

  <span class="hljs-keyword">const</span> entryFiles = glob.sync(path.join(__dirname, <span class="hljs-string">'./src/*/index.js'</span>));

  <span class="hljs-built_in">Object</span>.keys(entryFiles).map(<span class="hljs-function">(<span class="hljs-params">index</span>) =></span> &#123;
    <span class="hljs-comment">// 拿到路径名</span>
    <span class="hljs-keyword">const</span> entryFile = entryFiles[index];
    <span class="hljs-comment">// 匹配出文件名  /src 和 /  中间的内容</span>
    <span class="hljs-comment">// ！！！！ () 小括号表示分组</span>
    <span class="hljs-keyword">const</span> match = entryFile.match(<span class="hljs-regexp">/src\/(.*)\/index\.js/</span>);
    <span class="hljs-keyword">const</span> pageName = match && match[<span class="hljs-number">1</span>];
    entry[pageName] = entryFile;

    htmlWebpackPlugins.push(
      <span class="hljs-comment">// new 一次HtmlWebpackPlugin  就会生成一个html</span>
      <span class="hljs-keyword">new</span> HtmlWebpackPlugin(&#123;
        <span class="hljs-attr">template</span>: path.join(__dirname, <span class="hljs-string">`src/<span class="hljs-subst">$&#123;pageName&#125;</span>/index.html`</span>),
        <span class="hljs-attr">filename</span>: <span class="hljs-string">`<span class="hljs-subst">$&#123;pageName&#125;</span>.html`</span>,
        <span class="hljs-attr">chunks</span>: [pageName],
        <span class="hljs-attr">inject</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">minify</span>: &#123;
          <span class="hljs-comment">//移除空格</span>
          <span class="hljs-attr">collapseWhitespace</span>: <span class="hljs-literal">true</span>,
          <span class="hljs-comment">//移除注释</span>
          <span class="hljs-attr">removeComments</span>: <span class="hljs-literal">true</span>,
        &#125;,
      &#125;),
    );
    <span class="hljs-built_in">console</span>.log(htmlWebpackPlugins);
  &#125;);
  <span class="hljs-keyword">return</span> &#123;
    entry,
    htmlWebpackPlugins,
  &#125;;
&#125;;
<span class="hljs-keyword">const</span> &#123; entry, htmlWebpackPlugins &#125; = setMPA();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打包结果如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6bf9930d0dbf437dbe4b424c8b666873~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>webpack打包后的目录是很乱的，如果你入口文件的名字取为<strong>search</strong>,那么会在dist目录下直接生成一个<strong>search.xxxxx.js</strong>的文件。但是如果把名字取为src/search/index这样的，则会生成对应的目录结构。</p>
<p>如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a77a27cca7f4456f861f7c596845712f~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            