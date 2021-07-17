
---
title: '为你的VuePress博客添加GitTalk评论'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4706e968f90416a940cc1f1655b5197~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 16 Jul 2021 06:49:52 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4706e968f90416a940cc1f1655b5197~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1. 创建一个 OAuth Apps</h2>
<blockquote>
<p>在 Github 设置中找到<code> Settings / Developer settings / OAuth Apps / new OAuth Apps</code>, 创建一个应用
创建成功有 Client ID 和 Client Secret ，保存下来，后面我们会用到。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4706e968f90416a940cc1f1655b5197~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">2  创建评论组件</h2>
<blockquote>
<p>Vuepress 默认<code>.vuepress / components</code>文件夹下的组件会全局注册, 因此我们创建一个 <code>comment 组件gittalk.css</code>代码如下</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"gitalk-container"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"gitalk-container"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'comment'</span>,
  <span class="hljs-function"><span class="hljs-title">data</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> &#123;&#125;;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">let</span> body = <span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.gitalk-container'</span>);
    <span class="hljs-keyword">let</span> script = <span class="hljs-built_in">document</span>.createElement(<span class="hljs-string">'script'</span>);
    script.src = <span class="hljs-string">'https://cdn.jsdelivr.net/npm/gitalk@1/dist/gitalk.min.js'</span>;
    body.appendChild(script);
    script.onload = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-keyword">const</span> commentConfig = &#123;
        <span class="hljs-attr">clientID</span>: <span class="hljs-string">'你的clientID'</span>,
        <span class="hljs-attr">clientSecret</span>: <span class="hljs-string">'你的clientSecret'</span>,
        <span class="hljs-attr">repo</span>: <span class="hljs-string">'你的仓库名称'</span>,
        <span class="hljs-attr">owner</span>: <span class="hljs-string">'你的用户名'</span>,
        <span class="hljs-comment">// 这里接受一个数组，可以添加多个管理员，可以是你自己</span>
        <span class="hljs-attr">admin</span>: [<span class="hljs-string">'管理用户名'</span>],
        <span class="hljs-comment">// id 用于当前页面的唯一标识，一般来讲 pathname 足够了，</span>
        <span class="hljs-comment">// 但是如果你的 pathname 超过 50 个字符，GitHub 将不会成功创建 issue，此情况可以考虑给每个页面生成 hash 值的方法.</span>
        <span class="hljs-attr">id</span>: location.pathname,
        <span class="hljs-attr">distractionFreeMode</span>: <span class="hljs-literal">false</span>,
      &#125;;
      <span class="hljs-keyword">const</span> gitalk = <span class="hljs-keyword">new</span> Gitalk(commentConfig);
      gitalk.render(<span class="hljs-string">'gitalk-container'</span>);
    &#125;;
  &#125;,
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
<span class="hljs-keyword">@import</span> <span class="hljs-string">'../css/gittalk.css'</span>;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">3. 使用评论组件</h2>
<blockquote>
<p>理论上，我们在每个 markdown 文件里直接加入这个组件即可，但是每次都添加有点麻烦，还是让 node 来帮我们吧,根目录创建 build 文件夹, 创建三个文件 addComponents.js, delComponents.js, findMarkdown.js, 分别代码如下：</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// addComponents.js</span>
<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">"fs"</span>);
<span class="hljs-keyword">const</span> findMarkdown = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./findMarkdown"</span>);
<span class="hljs-keyword">const</span> rootDir = <span class="hljs-string">"./docs"</span>;

findMarkdown(rootDir, writeComponents);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">writeComponents</span>(<span class="hljs-params">dir</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (!<span class="hljs-regexp">/README/</span>.test(dir)) &#123;
        fs.appendFile(dir, <span class="hljs-string">`\n \n <comment/> \n `</span>, <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
            <span class="hljs-keyword">if</span> (err) <span class="hljs-keyword">throw</span> err;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`add components to <span class="hljs-subst">$&#123;dir&#125;</span>`</span>);
        &#125;);
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// delComponents.js</span>
<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">"fs"</span>);
<span class="hljs-keyword">const</span> findMarkdown = <span class="hljs-built_in">require</span>(<span class="hljs-string">"./findMarkdown"</span>);
<span class="hljs-keyword">const</span> rootDir = <span class="hljs-string">"./docs"</span>;

findMarkdown(rootDir, delComponents);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">delComponents</span>(<span class="hljs-params">dir</span>) </span>&#123;
    fs.readFile(dir, <span class="hljs-string">"utf-8"</span>, <span class="hljs-function">(<span class="hljs-params">err, content</span>) =></span> &#123;
        <span class="hljs-keyword">if</span> (err) <span class="hljs-keyword">throw</span> err;

        fs.writeFile(
            dir,
            content.replace(<span class="hljs-regexp">/\n \n <comment\/> \n /g</span>, <span class="hljs-string">""</span>),
            <span class="hljs-function"><span class="hljs-params">err</span> =></span> &#123;
                <span class="hljs-keyword">if</span> (err) <span class="hljs-keyword">throw</span> err;
                <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`del components from <span class="hljs-subst">$&#123;dir&#125;</span>`</span>);
            &#125;
        );
    &#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// findMarkdown.js</span>
<span class="hljs-keyword">const</span> fs = <span class="hljs-built_in">require</span>(<span class="hljs-string">"fs"</span>);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">findMarkdown</span>(<span class="hljs-params">dir, callback</span>) </span>&#123;
    fs.readdir(dir, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err, files</span>) </span>&#123;
        <span class="hljs-keyword">if</span> (err) <span class="hljs-keyword">throw</span> err;
        files.forEach(<span class="hljs-function"><span class="hljs-params">fileName</span> =></span> &#123;
            <span class="hljs-keyword">let</span> innerDir = <span class="hljs-string">`<span class="hljs-subst">$&#123;dir&#125;</span>/<span class="hljs-subst">$&#123;fileName&#125;</span>`</span>;
            <span class="hljs-keyword">if</span> (fileName.indexOf(<span class="hljs-string">"."</span>) !== <span class="hljs-number">0</span>) &#123;
                fs.stat(innerDir, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">err, stat</span>) </span>&#123;
                    <span class="hljs-keyword">if</span> (stat.isDirectory()) &#123;
                        findMarkdown(innerDir, callback);
                    &#125; <span class="hljs-keyword">else</span> &#123;
                        <span class="hljs-comment">// 跳过readme 文件，当然你也可以自行修改</span>
                        <span class="hljs-keyword">if</span> (<span class="hljs-regexp">/\.md$/</span>.test(fileName) && !<span class="hljs-regexp">/README/</span>.test(fileName))
                            callback(innerDir);
                    &#125;
                &#125;);
            &#125;
        &#125;);
    &#125;);
&#125;
<span class="hljs-built_in">module</span>.exports = findMarkdown;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>修改 package.json 的 scripts, 先为每个 md 文件添加组件，然后打包，最后再一一删除 markdown 中的 comment 组件</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-string">"build"</span>: <span class="hljs-string">"node ./builds/addComponents.js && vuepress build docs && node ./builds/delComponents.js"</span>,
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">4 效果预览</h2>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fourlang.github.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://ourlang.github.io/" ref="nofollow noopener noreferrer">我的项目</a></p></div>  
</div>
            