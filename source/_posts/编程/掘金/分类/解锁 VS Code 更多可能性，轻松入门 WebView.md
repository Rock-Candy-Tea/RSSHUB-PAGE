
---
title: '解锁 VS Code 更多可能性，轻松入门 WebView'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/748fed89b8cd41919e0fab978da53cf7~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 31 Aug 2021 16:50:32 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/748fed89b8cd41919e0fab978da53cf7~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/748fed89b8cd41919e0fab978da53cf7~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>作者：HelloGitHub-小夏</p>
<p>说起 VS Code 大家普遍印象应该都差不多是这样：不就是个编辑器嘛，最主要的还是 coding 的快感咯。</p>
<p>里面很多功能都应该是围绕如何提高 coding 效率、减少 coding 出错率、解放 coder 小哥哥小姐姐的劳动力等等，至于代码以外的东西比如预览什么的，就交给浏览器咯。</p>
<p>所以可能很少有人会把 VS Code 和 WebView 联想到一起。</p>
<h2 data-id="heading-0">一、随处可见的 WebView</h2>
<p>但是我相信，你一定在很多“有名”的 VS Code 插件中接触过它（WebView）的身影。比如可以在  VS Code 中画流程图的 vscode-drawio：</p>
<blockquote>
<p>GitHub 地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fhediet%2Fvscode-drawio" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/hediet/vscode-drawio" ref="nofollow noopener noreferrer">github.com/hediet/vsco…</a></p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d1c9e877ee6d4f74981d100fb6c5579a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>上班摸鱼的同时还要继续提升自我来刷题的 vscode-leetcode：</p>
<blockquote>
<p>GitHub 地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FLeetCode-OpenSource%2Fvscode-leetcode" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/LeetCode-OpenSource/vscode-leetcode" ref="nofollow noopener noreferrer">github.com/LeetCode-Op…</a></p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/63f59242e8cc47a987d95c1a584d1844~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>还有上班摸鱼的同时还要关心能否从一颗“小韭菜”实现财富自由的「韭菜盒子」 leek-fund：</p>
<blockquote>
<p>GitHub 地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FLeekHub%2Fleek-fund" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/LeekHub/leek-fund" ref="nofollow noopener noreferrer">github.com/LeekHub/lee…</a></p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92a994b0975d42c2925e81514d3d39fa~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以你可以看到，有了 WebView 来拓展能力，插件市场才会变得“百花齐放”，能满足各类人各类摸鱼的需求。但是上面开源项目的成功，也不仅仅靠的是我们本文介绍的简单的 WebView 的能力，如果你对上面几个开源项目有深挖的兴趣，可以直接 <code>clone</code> 代码，一瞅到底，说不定下一个厉害的开源 VS Code 插件就是出自你手啦。</p>
<h2 data-id="heading-1">二、WebView 到底是什么</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2FOhHe1kyHzh90Utdtf2E-iw" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/OhHe1kyHzh90Utdtf2E-iw" ref="nofollow noopener noreferrer">前面</a> 有提过 VS Code 允许我们在它给的规则之下可以自定义很多功能，但是视图这一块，其实我们自定义的范围非常小，这就限制了程序员们天马行空的创造力。但是自由的灵魂不会被眼前的困难打败，同行之间的心心相惜所以有了 WebView 的诞生。</p>
<p>当然这都是小编自己内心 OS 的，不过可以确定的是 WebView API 的存在允许在 VS Code 中扩展创建完全可自定义的视图。例如：内置的 Markdown 扩展使用 webviews 来呈现 Markdown 预览。Webviews 还可用于构建超出 VS Code 的本机 API 支持的复杂用户界面。</p>
<p>你也可以简单的把 WebView 理解为 <strong>VS Code 内部的 iframe</strong>。WebView 可以在这个框架中渲染几乎所有的 HTML 内容，还可以使用消息传递与扩展进行通信。这种自由使得 webviews 非常强大，而且也拥有了一个全新的扩展范围。</p>
<h2 data-id="heading-2">三、创建一个简单的 WebView</h2>
<p>从第一点的例子你就应该可以体会到 WebView 的功能拓展有多强大，它不仅可以作为自定义编辑器的视图来扩展提供自定义 UI 以编辑工作区中的任何文件。还允许在侧边栏或面板区域的 WebView 中继续呈现 WebView 视图等等。</p>
<p>如果你感兴趣，可以去<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcode.visualstudio.com%2Fapi%2Fextension-guides%2Fwebview" target="_blank" rel="nofollow noopener noreferrer" title="https://code.visualstudio.com/api/extension-guides/webview" ref="nofollow noopener noreferrer">官网</a>继续学习。今天我们下文谈的主要还是最简单的一种方式：在编辑器中创建一个简单的 WebView 面板。</p>
<h3 data-id="heading-3">1、配置命令</h3>
<p>第一步首先肯定是配置命令啦，我们再次打开<code>package.json</code>文件，新配置一个<code>command</code>：</p>
<pre><code class="hljs language-json copyable" lang="json"><span class="hljs-string">"contributes"</span>: &#123;
<span class="hljs-attr">"commands"</span>: [
..., <span class="hljs-comment">// 省略其他命令</span>
&#123;
        <span class="hljs-attr">"command"</span>: <span class="hljs-string">"webview.start"</span>,
        <span class="hljs-attr">"title"</span>: <span class="hljs-string">"open a webview page"</span>,
        <span class="hljs-attr">"category"</span>: <span class="hljs-string">"HelloGitHub webview"</span>
      &#125;
],
  ... <span class="hljs-comment">// 省略其他配置项</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置完之后要把这个新的命令在 <code>extension.js</code> 中注册一下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">activate</span>(<span class="hljs-params">context</span>) </span>&#123;
  ... <span class="hljs-comment">// 省略其他命令注册</span>
  
<span class="hljs-keyword">const</span> webviewCommand = vscode.commands.registerCommand(<span class="hljs-string">'webview.start'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// 创建和展示一个 webview</span>
    <span class="hljs-keyword">const</span> panel = vscode.window.createWebviewPanel(
      <span class="hljs-string">'hgWebview'</span>, <span class="hljs-comment">// 定义 webview 的类型，用于内部</span>
      <span class="hljs-string">'HelloGitHub webview'</span>, <span class="hljs-comment">// 给用户展示的标题</span>
      vscode.ViewColumn.One, <span class="hljs-comment">// 在第几栏编辑器里展示这个 webview</span>
      &#123;&#125; <span class="hljs-comment">// 其他 Webview 配置.</span>
    );
  &#125;);

context.subscriptions.push(webviewCommand); <span class="hljs-comment">// 这里可以放多个，用,分隔即可</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置完之后看一眼效果，让我们运行起来我们的插件：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf4361b618704ba5a90eb53ff8d1d2f3~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>你可以看到这个标题就是我们上面在 <code>package.json</code> 上配置的“HelloGitHub webview”，或许有同学会对 <code>ViewColumn</code> 这个配置疑惑。</p>
<p>那我们来看一下这里到底都有些什么值：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae3bf791328840fc8c1fe8c4b6506370~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>看不懂？没关系，我们实操一下，修改上面在 <code>extension.js</code> 里的配置如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> webviewCommand = vscode.commands.registerCommand(<span class="hljs-string">'webview.start'</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> panel = vscode.window.createWebviewPanel(
    <span class="hljs-string">'hgWebview'</span>,
    <span class="hljs-string">'HelloGitHub webview'</span>,
    vscode.ViewColumn.Two, <span class="hljs-comment">// 从 One 改成 Two</span>
    &#123;&#125;
  );
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>效果如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d5bb72bacde48b78f96eed25e1424a8~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里多了一个 <code>js</code> 的文件其实没有什么意义，因为如果没有这个文件占编辑器的第一个 <code>ViewColumn</code> 的话，其实效果和上面的配置是一样的，有了这个文件之后，我们的 WebView 才会在第二栏打开。这些单词是不是非常简单易懂？</p>
<h3 data-id="heading-4">2、初始化内容</h3>
<p>现在我们就要切入最重要的部分啦，如何丰富 WebView 的内容呢？其实也很简单啦，把它看做一个 iframe 就好啦，那无非就是 HTML 的那些东西呗？so easy！</p>
<p>首先我们要有一个包含整个 HTML 内容的独立文件，为了好区分，我把它放在了这里：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e75b0c23dcd14237a974edcb53fcf73a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>配置了一个非常简单的网页内容，里面只有一个图片：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-string">`
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello GitHub</title>
</head>
<body>
    <img src="https://cdn.jsdelivr.net/gh/521xueweihan/img_logo@main/logo/readme.gif" width="300" />
</body>
</html>
`</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 <code>extension.js</code> 中引入文件并配置到我们的 WebView：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> hgWebview = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./webview/hello-github'</span>);

... 
<span class="hljs-keyword">const</span> webviewCommand = vscode.commands.registerCommand(<span class="hljs-string">'webview.start'</span>, <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> panel = vscode.window.createWebviewPanel(
      <span class="hljs-string">'hgWebview'</span>,
      <span class="hljs-string">'HelloGitHub webview'</span>,
      vscode.ViewColumn.One,
      &#123;&#125;
    );
    panel.webview.html = hgWebview; <span class="hljs-comment">// 对没错就是这里配置，非常简单</span>
  &#125;);
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看一下效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7077e238dcdd4704bd1436363d62983a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里要提醒大家的是，你配置的应该始终是一个完整的 HTML 文档。HTML 片段或格式错误的 HTML 可能会导致运行不成功，所以在进行复杂操作的时候一定要小心调试，多看控制栏哦。</p>
<h3 data-id="heading-5">3、更新内容</h3>
<p>是的，我们现在要从编辑器对这个 WebView 做更新操作了！比如我们给这个 WebView 加一行文字，然后在编辑器里面加一个定时器，动态的去修改它。首先，修改我们的 <code>html</code> 文件，它不在是一个静态的文本了，他要动起来就得接收一个变量，所以改成函数咯：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function">(<span class="hljs-params">txt</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">`
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hello GitHub</title>
    </head>
    <body>
        <img src="https://cdn.jsdelivr.net/gh/521xueweihan/img_logo@main/logo/readme.gif" width="300" />
        <div>
          <span class="hljs-subst">$&#123;txt&#125;</span> // 注意这里是接收变量的写法
        </div>
    </body>
    </html>
  `</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其次呢，我们要跟这个函数有互动，并将要展示的值传进去，并且这个值还是定时 1s 要进行修改的，所以就变成这样啦：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> hgWebviewFun = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./webview/hello-github'</span>);

<span class="hljs-comment">// 设置我们的文案</span>
<span class="hljs-keyword">const</span> webviewTxt = &#123;
  <span class="hljs-string">'descripton'</span>: <span class="hljs-string">'HelloGitHub 是一个热爱开源项目的开源组织。'</span>,
  <span class="hljs-string">'slogon'</span>: <span class="hljs-string">'我们虽然没有钱，但是我们有梦想！'</span>
&#125;;

...
<span class="hljs-keyword">const</span> webviewCommand = vscode.commands.registerCommand(<span class="hljs-string">'webview.start'</span>, <span class="hljs-function">() =></span> &#123;
<span class="hljs-keyword">const</span> panel = vscode.window.createWebviewPanel(
<span class="hljs-string">'hgWebview'</span>,
<span class="hljs-string">'HelloGitHub webview'</span>,
vscode.ViewColumn.One,
&#123;&#125;
);

<span class="hljs-keyword">let</span> iteration = <span class="hljs-number">0</span>;
<span class="hljs-keyword">const</span> updateWebview = <span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// 做一个简单的判断用于取值</span>
<span class="hljs-keyword">const</span> key = iteration++ % <span class="hljs-number">2</span> ? <span class="hljs-string">'descripton'</span> : <span class="hljs-string">'slogon'</span>;
panel.title = webviewTxt[key];
panel.webview.html = hgWebviewFun(webviewTxt[key]);
&#125;;

<span class="hljs-comment">// 设置初始化的内容</span>
updateWebview();

<span class="hljs-comment">// 设置一个简单的定时器，让他一秒内执行一次</span>
<span class="hljs-built_in">setInterval</span>(updateWebview, <span class="hljs-number">1000</span>);
&#125;);
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看一下我们的效果，是不是就变成一个动感十足的网页啦：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/095ae038eefa4afba9bfa7cf30b96e00~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是效果是实现了，你有没有发现我们实现的方法非常的“暴力”，是直接替换了整个 <code>html</code> 的内容，类似于重新加载 iframe。所以要是换到复杂的页面，性能肯定是个非常严重的问题，就会导致非常多令人头大的性能问题。而且当用户关闭 WebView 面板时，WebView 本身是会被销毁的。如果尝试使用销毁的 WebView 会引发异常，比如我们上面的 <code>setInterval</code> 会继续触发并更新 <code>panel.webview.html</code>。</p>
<p>所以我们要避免这种情况出现：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> webviewCommand = vscode.commands.registerCommand(<span class="hljs-string">'webview.start'</span>, <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> panel = vscode.window.createWebviewPanel(
    <span class="hljs-string">'hgWebview'</span>,
    <span class="hljs-string">'HelloGitHub webview'</span>,
    vscode.ViewColumn.One,
    &#123;&#125;
  );

  <span class="hljs-keyword">let</span> iteration = <span class="hljs-number">0</span>;
  <span class="hljs-keyword">const</span> updateWebview = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">const</span> key = iteration++ % <span class="hljs-number">2</span> ? <span class="hljs-string">'descripton'</span> : <span class="hljs-string">'slogon'</span>;
    panel.title = webviewTxt[key];
    panel.webview.html = hgWebviewFun(webviewTxt[key]);
  &#125;;

  updateWebview();
  <span class="hljs-keyword">const</span> interval = <span class="hljs-built_in">setInterval</span>(updateWebview, <span class="hljs-number">1000</span>);

  panel.onDidDispose(
    <span class="hljs-function">() =></span> &#123;
      <span class="hljs-comment">// 当关闭 webview 的时候去掉对 webview 有后续更新的操作</span>
      <span class="hljs-built_in">clearInterval</span>(interval);
    &#125;,
    <span class="hljs-literal">null</span>,
    context.subscriptions
  );
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">4、消息传递</h3>
<p>前面说过，你可以简单的把 WebView 理解成 iframe，那这也意味着它们都可以运行脚本。不过默认情况下 WebView 中禁用 JavaScript，你可以通过传入 <code>enableScripts: true</code> 来启用。不过官网建议 WebView 应始终使用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcode.visualstudio.com%2Fapi%2Fextension-guides%2Fwebview%23content-security-policy" target="_blank" rel="nofollow noopener noreferrer" title="https://code.visualstudio.com/api/extension-guides/webview#content-security-policy" ref="nofollow noopener noreferrer">内容安全策略</a>禁用内联脚本，所以我们这里就不做展开。但是这一点也不影响我们发挥 WebView 的巨大作用——消息传递。</p>
<h4 data-id="heading-7">WebView 调试</h4>
<p>在消息传递内容之前，我觉得有必要说一下这个调试工具命令 <code>Developer: Toggle Developer Tools</code>。你可以通过 <code>comand+p</code>（MacOS）唤起这个开发者调试命令，可以帮你在调试 WebView 的时候“如鱼得水”，轻松捕获异常并 fix</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d9d55a1ec0948e097a928cd9648dd6f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>当然你还可以在 <code>Elements</code> 里面查看 <code>dom</code> 的结构，简直就是太熟悉了~</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1566f11b3d2a4c18b625c6f7c8481c2c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">WebView 接收消息</h4>
<p>首先我们先来了解一下如何从我们的插件应用向我们的 webview 传递消息。聪明的你一定猜到了对不对？没错就是 <code>postMessage</code>！</p>
<p>修改我们的注册命令如下：</p>
<ul>
<li>
<p>把 <code>createWebviewPanel</code> 的变量存到一个新的变量上去</p>
</li>
<li>
<p>新增了一个用于消息传递的命令 <code>webview.doRefactor</code></p>
</li>
<li>
<p>同时因为在 HTML 内部需要监听 <code>message</code> 的传递，所以我们必须确保开启脚本，也就是上文说的 <code>enableScripts:true</code></p>
</li>
<li>
<p>为了确保我们不眼花缭乱，这里也去掉了之前的定时器 <code>setInterval</code></p>
</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">...
<span class="hljs-keyword">let</span> currentPanel; <span class="hljs-comment">// 重新定义一个变量用于多个命令之间的使用</span>
<span class="hljs-keyword">const</span> webviewCommand = vscode.commands.registerCommand(<span class="hljs-string">'webview.start'</span>, <span class="hljs-function">() =></span> &#123;
currentPanel = vscode.window.createWebviewPanel(
<span class="hljs-string">'hgWebview'</span>,
<span class="hljs-string">'HelloGitHub webview'</span>,
vscode.ViewColumn.One,
&#123;
<span class="hljs-attr">enableScripts</span>: <span class="hljs-literal">true</span> <span class="hljs-comment">// 开启 js 脚本权限</span>
&#125;
);

<span class="hljs-keyword">let</span> iteration = <span class="hljs-number">0</span>;
<span class="hljs-keyword">const</span> updateWebview = <span class="hljs-function">() =></span> &#123;
<span class="hljs-keyword">const</span> key = iteration++ % <span class="hljs-number">2</span> ? <span class="hljs-string">'descripton'</span> : <span class="hljs-string">'slogon'</span>;
currentPanel.title = webviewTxt[key];
currentPanel.webview.html = hgWebviewFun(webviewTxt[key]);
&#125;;

updateWebview();
<span class="hljs-comment">// const interval = setInterval(updateWebview, 1000); 去掉定时器</span>

currentPanel.onDidDispose(
<span class="hljs-function">() =></span> &#123;
<span class="hljs-comment">// clearInterval(interval); 去掉定时器</span>
currentPanel = <span class="hljs-literal">undefined</span>; <span class="hljs-comment">// 销毁 webview 的时候释放变量</span>
&#125;,
<span class="hljs-literal">null</span>,
context.subscriptions
);
&#125;);

 <span class="hljs-comment">// 注册一个新的命令</span>
<span class="hljs-keyword">const</span> webviewRefactorCommand = vscode.commands.registerCommand(<span class="hljs-string">'webview.doRefactor'</span>, <span class="hljs-function">() =></span> &#123;
<span class="hljs-keyword">if</span> (!currentPanel) &#123;
<span class="hljs-keyword">return</span>;
&#125;

<span class="hljs-comment">// 向 webview 发送消息</span>
<span class="hljs-comment">// 你可以发送任何 JSON 序列化的数据</span>
currentPanel.webview.postMessage(&#123; <span class="hljs-attr">command</span>: <span class="hljs-string">'refactor'</span>, <span class="hljs-attr">msg</span>: <span class="hljs-string">'请多关注我们~'</span> &#125;);
&#125;)
  
  context.subscriptions.push(webviewCommand, webviewRefactorCommand);
 ...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了防止有人在跟着敲的时候漏掉这一步，我决定还是再提醒一下~要在 <code>package.json</code> 里面加上新注册的这个命令哦：</p>
<pre><code class="hljs language-json copyable" lang="json">... 
      &#123;
        <span class="hljs-attr">"command"</span>: <span class="hljs-string">"webview.start"</span>,
        <span class="hljs-attr">"title"</span>: <span class="hljs-string">"open a webview page"</span>,
        <span class="hljs-attr">"category"</span>: <span class="hljs-string">"HelloGitHub webview"</span>
      &#125;,
&#123;
        <span class="hljs-attr">"command"</span>: <span class="hljs-string">"webview.doRefactor"</span>,
        <span class="hljs-attr">"title"</span>: <span class="hljs-string">"doRefactor a webview page"</span>,
        <span class="hljs-attr">"category"</span>: <span class="hljs-string">"HelloGitHub webview"</span>
      &#125;
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有了消息的发送，当然也需要有消息的接收啦！这才能完成通信嘛~所以我们要修改我们的 HTML 文件，加一个用于接收消息的监听：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function">(<span class="hljs-params">txt</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">`
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Hello GitHub</title>
    </head>
    <body>
      <img src="https://cdn.jsdelivr.net/gh/521xueweihan/img_logo@main/logo/readme.gif" width="300" />
      <h1 id="message-show">hello</h1>
      <div>
        <span class="hljs-subst">$&#123;txt&#125;</span>
      </div>
      <script>
        const box = document.getElementById('message-show');

        // 在这里监听消息的发送
        window.addEventListener('message', event => &#123;

            const message = event.data; // 我们插件发送的数据
            console.log(message) // 打印一下看看是什么样子

            switch (message.command) &#123;
                case 'refactor':
                    box.textContent = message.msg;
                    break;
            &#125;
        &#125;);
      </script>
    </body>
    </html>
  `</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的够简单吧，我们来看一下效果，记得打开开发者调试工具，首先是用 <code>webview.start</code> 命令打开 WebView：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4049be8374674d188be713af567055a6~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>运行 <code>webview.doRefactor</code> 之后，我们就把我们的值传到了 WebView 里去啦：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c6c986a6f7d48e8a6049a9bcb239a2c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-9">WebView 发送消息</h4>
<p>WebView 还可以将消息传递回我们的扩展程序。</p>
<p>这主要是通过使用 WebView 的 <code>postMessage</code> 内特殊的 VS Code API 对象上的函数来完成的。要访问 VS Code API 对象，需要在 WebView 内部调用 <code>acquireVsCodeApi</code> 这个函数每个会话只能调用一次。</p>
<p>而且<strong>必须</strong>保留此方法返回的 VS Code API 实例，并将其分发给任何其他需要使用它的函数。</p>
<p>我们可以使用 VS Code API 的 <code>postMessage</code> 方法在我们的插件中显示来自 WebView 的消息：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> vscode = acquireVsCodeApi(); <span class="hljs-comment">// 直接使用</span>

vscode.postMessage(&#123; <span class="hljs-comment">// 发送消息</span>
  <span class="hljs-attr">command</span>: <span class="hljs-string">'alert'</span>,
  <span class="hljs-attr">text</span>: <span class="hljs-string">'🚀 发送成功~感谢老铁~'</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们把这个事件触发绑在了一个新的 <code>button</code> 上，完整的代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">module</span>.exports = <span class="hljs-function">(<span class="hljs-params">txt</span>) =></span> &#123;
  <span class="hljs-keyword">return</span> <span class="hljs-string">`
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Hello GitHub</title>
    </head>
    <body>
      <img src="https://cdn.jsdelivr.net/gh/521xueweihan/img_logo@main/logo/readme.gif" width="300" />
      <h1 id="message-show">hello</h1>
      <div>
        <span class="hljs-subst">$&#123;txt&#125;</span>
      </div>
      <button id="btn_submit">点我发送🚀！</button>
      <script>
        const box = document.getElementById('message-show');
        const vscode = acquireVsCodeApi();

        window.addEventListener('message', event => &#123;

            const message = event.data;
            console.log(message)

            switch (message.command) &#123;
                case 'refactor':
                    box.textContent = message.msg;
                    break;
            &#125;
        &#125;);

        document.getElementById('btn_submit').addEventListener('click', function()&#123;
          vscode.postMessage(&#123;
            command: 'alert',
            text: '🚀 发送成功~感谢老铁~'
          &#125;)
        &#125;)


      </script>
    </body>
    </html>
  `</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>同时也需要在我们的插件代码里接收来自 WebView 的消息：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">...
currentPanel.webview.onDidReceiveMessage(
  <span class="hljs-function"><span class="hljs-params">message</span> =></span> &#123;
    <span class="hljs-keyword">switch</span> (message.command) &#123;
      <span class="hljs-keyword">case</span> <span class="hljs-string">'alert'</span>:
        vscode.window.showInformationMessage(message.text);
        <span class="hljs-keyword">return</span>;
    &#125;
  &#125;,
  <span class="hljs-literal">undefined</span>,
  context.subscriptions
);
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完整的代码如下，在打开 WebView 的时候就要将事件绑定都搞定：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">...
 <span class="hljs-keyword">const</span> webviewCommand = vscode.commands.registerCommand(<span class="hljs-string">'webview.start'</span>, <span class="hljs-function">() =></span> &#123;
currentPanel = vscode.window.createWebviewPanel(
<span class="hljs-string">'hgWebview'</span>,
<span class="hljs-string">'HelloGitHub webview'</span>,
vscode.ViewColumn.One,
&#123;
<span class="hljs-attr">enableScripts</span>: <span class="hljs-literal">true</span>
&#125;
);

<span class="hljs-keyword">let</span> iteration = <span class="hljs-number">0</span>;
<span class="hljs-keyword">const</span> updateWebview = <span class="hljs-function">() =></span> &#123;
<span class="hljs-keyword">const</span> key = iteration++ % <span class="hljs-number">2</span> ? <span class="hljs-string">'descripton'</span> : <span class="hljs-string">'slogon'</span>;
currentPanel.title = webviewTxt[key];
currentPanel.webview.html = hgWebviewFun(webviewTxt[key]);
&#125;;

updateWebview();
<span class="hljs-comment">// const interval = setInterval(updateWebview, 1000);</span>

currentPanel.onDidDispose(
<span class="hljs-function">() =></span> &#123;
<span class="hljs-comment">// clearInterval(interval);</span>
currentPanel = <span class="hljs-literal">undefined</span>;
&#125;,
<span class="hljs-literal">null</span>,
context.subscriptions
);

<span class="hljs-comment">// 处理来自 webview 的消息</span>
currentPanel.webview.onDidReceiveMessage(
<span class="hljs-function"><span class="hljs-params">message</span> =></span> &#123;
<span class="hljs-keyword">switch</span> (message.command) &#123;
<span class="hljs-keyword">case</span> <span class="hljs-string">'alert'</span>:
vscode.window.showInformationMessage(message.text);
<span class="hljs-keyword">return</span>;
&#125;
&#125;,
<span class="hljs-literal">undefined</span>,
context.subscriptions
);
&#125;);
...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接下来我们先看一下点击按钮前的样式：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0aed59ae7045490085d6d3dca4bb26b8~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>来看一下我们点击按钮会发生什么“神奇”的事情呢？</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/733f10ed9e2d4f00aec9abc987dfd285~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">四、总结</h2>
<p>那快乐的时光总是短暂的，又到了文章结束的时候啦。总的来说 WebView 就像是在 VS Code 里的 iframe，虽然可能在性能上有那么点弊端，但是却能够帮助我们实现很多丰富而又有趣的事情。</p>
<p>因此我们更要好好的利用这个功能，把它的力量发挥到极致。根据官网的描述，我们也要在使用的时候多注意以下几点：</p>
<ul>
<li>
<p>WebView 应该具有它所需的最少功能集。例如：如果不需要运行脚本，则不要设置 <code>enableScripts: true</code></p>
</li>
<li>
<p>WebView 严格遵从 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdevelopers.google.com%2Fweb%2Ffundamentals%2Fsecurity%2Fcsp%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://developers.google.com/web/fundamentals/security/csp/" ref="nofollow noopener noreferrer">内容安全策略</a>，所以在 WebView 中可加载和执行的内容都有一定的限制。例如：内容安全策略可以确保仅允许在 WebView 中运行的脚本列表，甚至告诉 WebView 只能加载 <code>https</code> 图像。</p>
</li>
<li>
<p>出于安全考虑 WebView 默认无法直接访问本地资源，它在一个孤立的上下文中运行，想要加载本地图片、js、css 等必须通过特殊的 <code>vscode-resource:</code> 协议，网页里面所有的静态资源都要转换成这种格式，否则无法被正常加载。</p>
</li>
<li>
<p>就像普通网页都要求的那样，在为 WebView 构建 HTML 时，必须清理所有用户输入。未能正确清理输入可能会导致内容注入，这可能会使你的用户面临安全风险。比如：文件内容、文件和文件夹路径、用户和工作区设置</p>
</li>
<li>
<p>WebView 有自己的生命周期，如果在有极致体验的场景下发挥他的最大作用，建议去官网更加深入的学习一下</p>
</li>
</ul>
<p>最后的最后，预告一下下一篇<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fmp%2Fappmsgalbum%3F__biz%3DMzA5MzYyNzQ0MQ%3D%3D%26action%3Dgetalbum%26album_id%3D2026845669264539658%26scene%3D173%26from_msgid%3D2247506651%26from_itemidx%3D1%26count%3D3%26nolastread%3D1%23wechat_redirect" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzA5MzYyNzQ0MQ==&action=getalbum&album_id=2026845669264539658&scene=173&from_msgid=2247506651&from_itemidx=1&count=3&nolastread=1#wechat_redirect" ref="nofollow noopener noreferrer">「VS Code」系列</a>文章，也就是本入门系列最后一篇文章将会带大家体验更综合性的东西，给小编多一点点时间努力研究一下，期待我们下次再见咯！</p></div>  
</div>
            