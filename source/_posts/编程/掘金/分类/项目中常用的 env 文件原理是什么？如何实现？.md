
---
title: '项目中常用的 .env 文件原理是什么？如何实现？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5788298dd8ef4cada073a1ed586f9aa3~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
author: 掘金
comments: false
date: Fri, 16 Sep 2022 04:07:33 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5788298dd8ef4cada073a1ed586f9aa3~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><ul>
<li><strong>本文参加了由</strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Flxchuan12.gitee.io" title="https://link.juejin.cn/?target=https%3A%2F%2Flxchuan12.gitee.io" target="_blank">公众号@若川视野</a> <strong>发起的每周源码共读活动，</strong>  <a href="https://juejin.cn/post/7079706017579139102" title="https://juejin.cn/post/7079706017579139102" target="_blank">点击了解详情一起参与。</a></li>
</ul>
<h1 data-id="heading-0">1. dotenv介绍</h1>
<p><code>Dotenv</code> 是一个零依赖模块，可将 <code>.env</code> 文件中的环境变量加载到 <code>process.env</code> 中。可以使用<code>dotenv-expand</code>来扩展。
还有dotenv-cli推荐使用。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//dotenv的使用：</span>
<span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> dotenv <span class="hljs-keyword">from</span> <span class="hljs-string">'dotenv'</span> 
dotenv.<span class="hljs-title function_">config</span>()
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-bash copyable" lang="bash">
//dotenv-cli配置不同的.<span class="hljs-built_in">env</span>文件，不同环境使用不同的脚本命令。
<span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"dev"</span>: <span class="hljs-string">"dotenv -e .local.env -e .env.dev react-app-rewired start"</span>,
    <span class="hljs-string">"build"</span>: <span class="hljs-string">"dotenv -e .env.prod react-app-rewired build"</span>,
    <span class="hljs-string">"dev:test"</span>: <span class="hljs-string">"dotenv -e .local.env -e .env.dev react-app-rewired start"</span>,
    <span class="hljs-string">"dev:prod"</span>: <span class="hljs-string">"dotenv -e .local.env -e .env.prod react-app-rewired start"</span>,
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">2.dotenv代码</h1>
<h2 data-id="heading-2">2.1 dotenv实现的主要流程</h2>
<pre><code class="hljs language-arduino copyable" lang="arduino"><span class="hljs-number">1.</span>读取env文件
<span class="hljs-number">2.</span>parse解析文件内容生成键值对的对象，返回解析的结果
<span class="hljs-number">3.</span> 合并配置到process.env
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">'fs'</span>)
<span class="hljs-keyword">const</span> path = <span class="hljs-built_in">require</span>(<span class="hljs-string">'path'</span>)
<span class="hljs-keyword">const</span> os = <span class="hljs-built_in">require</span>(<span class="hljs-string">'os'</span>)

<span class="hljs-keyword">const</span> <span class="hljs-variable constant_">LINE</span> = <span class="hljs-regexp">/(?:^|^)\s*(?:export\s+)?([\w.-]+)(?:\s*=\s*?|:\s+?)(\s*'(?:\\'|[^'])*'|\s*"(?:\\"|[^"])*"|\s*`(?:\\`|[^`])*`|[^#\r\n]+)?\s*(?:#.*)?(?:$|$)/mg</span>

<span class="hljs-comment">// Parser src into an Object</span>
<span class="hljs-keyword">function</span> <span class="hljs-title function_">parse</span> (src) &#123;
  <span class="hljs-keyword">const</span> obj = &#123;&#125;

  <span class="hljs-comment">// Convert buffer to string</span>
  <span class="hljs-keyword">let</span> lines = src.<span class="hljs-title function_">toString</span>()

  <span class="hljs-comment">// Convert line breaks to same format</span>
  lines = lines.<span class="hljs-title function_">replace</span>(<span class="hljs-regexp">/\r\n?/mg</span>, <span class="hljs-string">'\n'</span>)

  <span class="hljs-keyword">let</span> match
  <span class="hljs-keyword">while</span> ((match = <span class="hljs-variable constant_">LINE</span>.<span class="hljs-title function_">exec</span>(lines)) != <span class="hljs-literal">null</span>) &#123;
    <span class="hljs-comment">/**
     * match的数据结构
        0:
        'NAME="xxxxx"'
        1:
        'NAME'
        2:
        '"xxxxx"'
    */</span>
    <span class="hljs-keyword">const</span> key = match[<span class="hljs-number">1</span>]

    <span class="hljs-comment">// Default undefined or null to empty string</span>
    <span class="hljs-keyword">let</span> value = (match[<span class="hljs-number">2</span>] || <span class="hljs-string">''</span>)

    <span class="hljs-comment">// Remove whitespace</span>
    value = value.<span class="hljs-title function_">trim</span>()

    <span class="hljs-comment">// Check if double quoted</span>
    <span class="hljs-keyword">const</span> maybeQuote = value[<span class="hljs-number">0</span>]

    <span class="hljs-comment">// Remove surrounding quotes</span>
    value = value.<span class="hljs-title function_">replace</span>(<span class="hljs-regexp">/^(['"`])([\s\S]*)\1$/mg</span>, <span class="hljs-string">'$2'</span>)

    <span class="hljs-comment">// Expand newlines if double quoted</span>
    <span class="hljs-keyword">if</span> (maybeQuote === <span class="hljs-string">'"'</span>) &#123;
      value = value.<span class="hljs-title function_">replace</span>(<span class="hljs-regexp">/\\n/g</span>, <span class="hljs-string">'\n'</span>)
      value = value.<span class="hljs-title function_">replace</span>(<span class="hljs-regexp">/\\r/g</span>, <span class="hljs-string">'\r'</span>)
    &#125;

    <span class="hljs-comment">// Add to object</span>
    obj[key] = value
  &#125;

  <span class="hljs-keyword">return</span> obj
&#125;

<span class="hljs-keyword">function</span> <span class="hljs-title function_">_log</span> (message) &#123;
  <span class="hljs-variable language_">console</span>.<span class="hljs-title function_">log</span>(<span class="hljs-string">`[dotenv][DEBUG] <span class="hljs-subst">$&#123;message&#125;</span>`</span>)
&#125;

<span class="hljs-keyword">function</span> <span class="hljs-title function_">_resolveHome</span> (envPath) &#123;
    <span class="hljs-comment">// os.homedir()方法是os模块的内置应用程序编程接口，用于获取当前用户的主目录路径。</span>
  <span class="hljs-keyword">return</span> envPath[<span class="hljs-number">0</span>] === <span class="hljs-string">'~'</span> ? path.<span class="hljs-title function_">join</span>(os.<span class="hljs-title function_">homedir</span>(), envPath.<span class="hljs-title function_">slice</span>(<span class="hljs-number">1</span>)) : envPath
&#125;

<span class="hljs-comment">// Populates process.env from .env file</span>
<span class="hljs-keyword">function</span> <span class="hljs-title function_">config</span> (options) &#123;
  <span class="hljs-keyword">let</span> dotenvPath = path.<span class="hljs-title function_">resolve</span>(process.<span class="hljs-title function_">cwd</span>(), <span class="hljs-string">'.env'</span>)
  <span class="hljs-keyword">let</span> encoding = <span class="hljs-string">'utf8'</span>
  <span class="hljs-keyword">const</span> debug = <span class="hljs-title class_">Boolean</span>(options && options.<span class="hljs-property">debug</span>)
  <span class="hljs-keyword">const</span> override = <span class="hljs-title class_">Boolean</span>(options && options.<span class="hljs-property">override</span>)

  <span class="hljs-keyword">if</span> (options) &#123;
    <span class="hljs-keyword">if</span> (options.<span class="hljs-property">path</span> != <span class="hljs-literal">null</span>) &#123;
        <span class="hljs-comment">// 如果有配置path则获取新的path</span>
      dotenvPath = <span class="hljs-title function_">_resolveHome</span>(options.<span class="hljs-property">path</span>)
    &#125;
    <span class="hljs-keyword">if</span> (options.<span class="hljs-property">encoding</span> != <span class="hljs-literal">null</span>) &#123;
      encoding = options.<span class="hljs-property">encoding</span>
    &#125;
  &#125;

  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-comment">// Specifying an encoding returns a string instead of a buffer</span>
    <span class="hljs-keyword">const</span> parsed = <span class="hljs-title class_">DotenvModule</span>.<span class="hljs-title function_">parse</span>(fs.<span class="hljs-title function_">readFileSync</span>(dotenvPath, &#123; encoding &#125;))

    <span class="hljs-title class_">Object</span>.<span class="hljs-title function_">keys</span>(parsed).<span class="hljs-title function_">forEach</span>(<span class="hljs-keyword">function</span> (<span class="hljs-params">key</span>) &#123;
      <span class="hljs-comment">//判断key是否是process.env上的属性，如果不是则赋值，如果是，并且override === true，则覆盖原有的</span>
      <span class="hljs-keyword">if</span> (!<span class="hljs-title class_">Object</span>.<span class="hljs-property"><span class="hljs-keyword">prototype</span></span>.<span class="hljs-property">hasOwnProperty</span>.<span class="hljs-title function_">call</span>(process.<span class="hljs-property">env</span>, key)) &#123;
        process.<span class="hljs-property">env</span>[key] = parsed[key]
      &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">if</span> (override === <span class="hljs-literal">true</span>) &#123;
          process.<span class="hljs-property">env</span>[key] = parsed[key]
        &#125;
        <span class="hljs-comment">// debug模式下输入日志</span>
        <span class="hljs-keyword">if</span> (debug) &#123;
          <span class="hljs-keyword">if</span> (override === <span class="hljs-literal">true</span>) &#123;
            <span class="hljs-title function_">_log</span>(<span class="hljs-string">`"<span class="hljs-subst">$&#123;key&#125;</span>" is already defined in \`process.env\` and WAS overwritten`</span>)
          &#125; <span class="hljs-keyword">else</span> &#123;
            <span class="hljs-title function_">_log</span>(<span class="hljs-string">`"<span class="hljs-subst">$&#123;key&#125;</span>" is already defined in \`process.env\` and was NOT overwritten`</span>)
          &#125;
        &#125;
      &#125;
    &#125;)

    <span class="hljs-keyword">return</span> &#123; parsed &#125;
  &#125; <span class="hljs-keyword">catch</span> (e) &#123;
    <span class="hljs-keyword">if</span> (debug) &#123;
      <span class="hljs-title function_">_log</span>(<span class="hljs-string">`Failed to load <span class="hljs-subst">$&#123;dotenvPath&#125;</span> <span class="hljs-subst">$&#123;e.message&#125;</span>`</span>)
    &#125;

    <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">error</span>: e &#125;
  &#125;
&#125;

<span class="hljs-keyword">const</span> <span class="hljs-title class_">DotenvModule</span> = &#123;
  config,
  parse
&#125;

<span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span>.<span class="hljs-property">config</span> = <span class="hljs-title class_">DotenvModule</span>.<span class="hljs-property">config</span>
<span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span>.<span class="hljs-property">parse</span> = <span class="hljs-title class_">DotenvModule</span>.<span class="hljs-property">parse</span>
<span class="hljs-variable language_">module</span>.<span class="hljs-property">exports</span> = <span class="hljs-title class_">DotenvModule</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">2.2 parse方法返回的数据</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5788298dd8ef4cada073a1ed586f9aa3~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">2.3 正则的解析</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c1785ecbcbe341bc82549c0fefb9bb6e~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-5">小结</h1>
<p><code>dotenv</code>的实现简单流程就是读取.env文件，然后生成一个key/value对象，合并到<code>process.env</code>上。整个流程比较简单，跑几次代码就比较清楚了。正则这里比较难理解。</p></div>  
</div>
            