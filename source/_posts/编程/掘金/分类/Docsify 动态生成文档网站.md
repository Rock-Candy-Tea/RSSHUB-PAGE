
---
title: 'Docsify 动态生成文档网站'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03a0701453d6464e8dac1f4617910b45~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 19 Jul 2021 21:24:21 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03a0701453d6464e8dac1f4617910b45~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>一个神奇的文档网站生成工具。</p>
</blockquote>
<p>docsify 是一个动态生成文档网站的工具。不同于 GitBook、Hexo 的地方是它不会生成将 <code>.md</code> 转成 <code>.html</code> 文件，所有转换工作都是在运行时进行。</p>
<p>这将非常实用，如果只是需要快速的搭建一个小型的文档网站，或者不想因为生成的一堆 <code>.html</code> 文件“污染” commit 记录，只需要创建一个 <code>index.html</code> 就可以开始写文档而且直接<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocsify.js.org%2F%23%2Fzh-cn%2Fdeploy" target="_blank" rel="nofollow noopener noreferrer" title="https://docsify.js.org/#/zh-cn/deploy" ref="nofollow noopener noreferrer">部署在 GitHub Pages</a>。</p>
<p>查看 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocsify.js.org%2F%23%2Fzh-cn%2Fquickstart" target="_blank" rel="nofollow noopener noreferrer" title="https://docsify.js.org/#/zh-cn/quickstart" ref="nofollow noopener noreferrer">快速开始</a>了解详情。</p>
<h2 data-id="heading-0"><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocsify.js.org%2F%23%2Fzh-cn%2Fquickstart%3Fid%3D%25e5%2588%259d%25e5%25a7%258b%25e5%258c%2596%25e9%25a1%25b9%25e7%259b%25ae" target="_blank" rel="nofollow noopener noreferrer" title="https://docsify.js.org/#/zh-cn/quickstart?id=%e5%88%9d%e5%a7%8b%e5%8c%96%e9%a1%b9%e7%9b%ae" ref="nofollow noopener noreferrer">初始化项目</a></h2>
<p>如果想在项目的 <code>./docs</code> 目录里写文档，直接通过 <code>init</code> 初始化项目。</p>
<pre><code class="copyable">docsify init ./docs
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge,chrome=1"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width,initial-scale=1"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">link</span> <span class="hljs-attr">rel</span>=<span class="hljs-string">"stylesheet"</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"//cdn.jsdelivr.net/npm/docsify/themes/vue.css"</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>
<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-built_in">window</span>.$docsify = &#123;
      <span class="hljs-comment">//...</span>
    &#125;
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"//cdn.jsdelivr.net/npm/docsify/lib/docsify.min.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
</html
<span class="copy-code-btn">复制代码</span></code></pre>
<p>多页文档
例如创建一个 guide.md 文件，那么对应的路由就是 /#/guide。</p>
<p>启动项目</p>
<pre><code class="copyable">python -m SimpleHTTPServer 3000
# or
python3 -m http.server 3000
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">定制侧边栏</h2>
<p>为了获得侧边栏，您需要创建自己的_sidebar.md</p>
<pre><code class="copyable">* [首页](/)
* [后端用到](not_front/123)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>文件所在路径</p>
<pre><code class="copyable">README.md
not_front/123.md
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03a0701453d6464e8dac1f4617910b45~tplv-k3u1fbpfcp-watermark.image" alt="1662509-a0c04606c592a274.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>index.html 信息</p>
<pre><code class="copyable"><!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Document</title>
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
  <meta name="description" content="Description">
  <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
  <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/docsify/lib/themes/vue.css">
</head>
<body>
  <div id="app"></div>
  <script>
    window.$docsify = &#123;
      loadSidebar: '_sidebar.md',
      subMaxLevel: 3
    &#125;
  </script>
  <script src="//cdn.jsdelivr.net/npm/docsify/lib/docsify.min.js"></script>
</body>
</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">官方地址的压缩版</h2>
<p><strong>压缩版 css</strong></p>

<p><strong>压缩版 js</strong></p>

<p><strong>其他主题</strong></p>


<h2 data-id="heading-3">相关插件</h2>
<h3 data-id="heading-4">代码高亮</h3>
<p><strong>docsify</strong>内置的代码高亮工具是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FPrismJS%2Fprism" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/PrismJS/prism" ref="nofollow noopener noreferrer">Prism</a>。Prism 默认支持的语言如下：</p>
<ul>
<li>Markup - <code>markup</code>, <code>html</code>, <code>xml</code>, <code>svg</code>, <code>mathml</code>, <code>ssml</code>, <code>atom</code>, <code>rss</code></li>
<li>CSS - <code>css</code></li>
<li>C-like - <code>clike</code></li>
<li>JavaScript - <code>javascript</code>, <code>js</code></li>
</ul>
<p>添加额外的语法支持需要通过CDN添加相应的语法文件 :</p>
<pre><code class="copyable"><script src="//cdn.jsdelivr.net/npm/prismjs@1/components/prism-bash.min.js"></script>
<script src="//cdn.jsdelivr.net/npm/prismjs@1/components/prism-php.min.js"></script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">copy 插件</h3>
<pre><code class="hljs language-xml copyable" lang="xml">  <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-built_in">window</span>.$docsify = &#123;
  <span class="hljs-attr">copyCode</span>: &#123;
    <span class="hljs-attr">buttonText</span>: &#123;
  <span class="hljs-string">'/'</span>      : <span class="hljs-string">'点击复制'</span>
&#125;,
<span class="hljs-attr">errorText</span>: &#123;
  <span class="hljs-string">'/'</span>: <span class="hljs-string">'错误'</span>,
&#125;,
<span class="hljs-attr">successText</span>: &#123;
  <span class="hljs-string">'/'</span>      : <span class="hljs-string">'已复制'</span>
&#125;
  &#125;
    &#125;
  </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">字数统计</h3>
<p>这是一款为docsify提供文字统计的插件. <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2F827652549" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/827652549" ref="nofollow noopener noreferrer">@827652549</a>提供</p>
<p>它提供了统计中文汉字和英文单词的功能，并且排除了一些markdown语法的特殊字符例如*、-等</p>
<p><strong>Add JS</strong></p>
<pre><code class="copyable"><script src="//unpkg.com/docsify-count/dist/countable.js"></script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Add settings</strong></p>
<pre><code class="copyable">window.$docsify = &#123;
  count:&#123;
    countable:true,
    fontsize:'0.9em',
    color:'rgb(90,90,90)',
    language:'chinese'
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">docsify-themeable 主题的使用</h2>
<pre><code class="copyable"><!-- Theme: Simple (latest v0.x.x) -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/docsify-themeable@0/dist/css/theme-defaults.css">

<!-- Theme: Simple -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/docsify-themeable@0/dist/css/theme-simple.css">

<!-- Theme: Simple Dark -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/docsify-themeable@0/dist/css/theme-simple-dark.css">


<!-- docsify-themeable (latest v0.x.x) -->
<script src="https://cdn.jsdelivr.net/npm/docsify-themeable@0"></script>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            