
---
title: 'Node 系列 - 003 - commander.js'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1acefece99b43f7a332a79b2e4537bf~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 14 Jun 2021 21:30:24 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1acefece99b43f7a332a79b2e4537bf~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>——————————☆☆☆——————————</p>
<p>Node 系列相应地址：</p>
<ul>
<li>代码仓库：<a href="https://github.com/LiangJunrong/all-for-one" target="_blank" rel="nofollow noopener noreferrer">github.com/LiangJunron…</a></li>
<li>文章仓库：<a href="https://github.com/LiangJunrong/document-library/tree/master/%E7%B3%BB%E5%88%97-%E5%89%8D%E7%AB%AF%E8%B5%84%E6%96%99/Node" target="_blank" rel="nofollow noopener noreferrer">github.com/LiangJunron…</a></li>
</ul>
<p>——————————☆☆☆——————————</p>
<p><code>commander.js</code> —— 完整的 <code>Node.js</code> 命令行解决方案。</p>
<p>本篇文章讲解如何通过 <code>commander.js</code> 溜达 Node.js 命令行。</p>

<h2 data-id="heading-0"><a name="user-content-chapter-one" id="user-content-chapter-one" href="https://juejin.cn/post/undefined"></a>一 目录</h2>
<p><strong>不折腾的前端，和咸鱼有什么区别</strong></p>









































<table><thead><tr><th>目录</th></tr></thead><tbody><tr><td><a href="https://juejin.cn/post/6973888151421108254#chapter-one">一 目录</a></td></tr><tr><td><a name="user-content-catalog-chapter-two" id="user-content-catalog-chapter-two" href="https://juejin.cn/post/undefined"></a><a href="https://juejin.cn/post/6973888151421108254#chapter-two">二 前言</a></td></tr><tr><td><a name="user-content-catalog-chapter-three" id="user-content-catalog-chapter-three" href="https://juejin.cn/post/undefined"></a><a href="https://juejin.cn/post/6973888151421108254#chapter-three">三 commander.js</a></td></tr><tr><td><a name="user-content-catalog-chapter-four" id="user-content-catalog-chapter-four" href="https://juejin.cn/post/undefined"></a><a href="https://juejin.cn/post/6973888151421108254#chapter-four">四 实践：文件重排功能</a></td></tr><tr><td> <a href="https://juejin.cn/post/6973888151421108254#chapter-four-one">4.1 实践目录</a></td></tr><tr><td> <a href="https://juejin.cn/post/6973888151421108254#chapter-four-two">4.2 编写 commander</a></td></tr><tr><td> <a href="https://juejin.cn/post/6973888151421108254#chapter-four-three">4.3 编写排序功能</a></td></tr><tr><td> <a href="https://juejin.cn/post/6973888151421108254#chapter-four-four">4.4 运行内容</a></td></tr><tr><td><a name="user-content-catalog-chapter-five" id="user-content-catalog-chapter-five" href="https://juejin.cn/post/undefined"></a><a href="https://juejin.cn/post/6973888151421108254#chapter-five">五 常用 commander 配置</a></td></tr><tr><td><a name="user-content-catalog-chapter-six" id="user-content-catalog-chapter-six" href="https://juejin.cn/post/undefined"></a><a href="https://juejin.cn/post/6973888151421108254#chapter-six">六 参考文献</a></td></tr><tr><td></td></tr></tbody></table>
<h2 data-id="heading-1"><a name="user-content-chapter-two" id="user-content-chapter-two" href="https://juejin.cn/post/undefined"></a>二 前言</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6973888151421108254#chapter-one">返回目录</a></p>
</blockquote>
<p>当一个 <code>Node.js</code> 程序运行时，会有许多存在内存中的全局变量。</p>
<p>其中 <code>process</code> 作为进程对象，它有一个 <code>argv</code> 属性，可以查看到指令。</p>
<p>我们随便建一个 <code>index.js</code> 举例，终端执行命令：<code>node index.js --name jsliang</code></p>
<blockquote>
<p>index.js</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">console</span>.log(process.argv);
<span class="hljs-comment">/*
  [
    'C:\\Program Files\\nodejs\\node.exe',
    'F:\\jsliang\\index.js',
    '--name',
    'jsliang'
  ]
*/</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看打印的数据：</p>
<ul>
<li><code>Node</code> 位置：<code>C:\\Program Files\\nodejs\\node.exe</code></li>
<li>当前代码路径：<code>F:\\jsliang\\index.js</code></li>
<li>参数 1：<code>--name</code></li>
<li>参数 2：<code>jsliang</code></li>
</ul>
<p>所以，在我们写命令行程序的时候，只需要对 <code>process.argv</code> 这个数组的第三个元素及其之后的参数进行解析即可。</p>
<p>如果不嫌麻烦，完全可以写出很多判断分支来做。</p>
<p>但是，有现成的为啥还要自己写，能偷懒就偷懒啊~</p>
<h2 data-id="heading-2"><a name="user-content-chapter-three" id="user-content-chapter-three" href="https://juejin.cn/post/undefined"></a>三 commander.js</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6973888151421108254#chapter-one">返回目录</a></p>
</blockquote>
<p><code>commander.js</code> 是 <code>tj</code> 写的一个工具包，作用是让 <code>Node</code> 命令行程序的制作更加简单：</p>
<ul>
<li><a href="https://github.com/tj/commander.js" target="_blank" rel="nofollow noopener noreferrer">GitHub：commander</a></li>
</ul>
<blockquote>
<p>懂你，中文 README 奉上：<a href="https://github.com/tj/commander.js/blob/master/Readme_zh-CN.md" target="_blank" rel="nofollow noopener noreferrer">github.com/tj/commande…</a></p>
</blockquote>
<p>下面我们开始操作：</p>
<ul>
<li>初始化 <code>package.json</code>：<code>npm init --yes</code>
<ul>
<li>！！【注】如果是按照 Node 系列顺序学习的，这个步骤可以省略</li>
<li>！！【注】下面代码可以建一个 <code>test</code> 空文件夹来耍耍</li>
</ul>
</li>
<li>安装包：<code>npm i commander</code></li>
<li>编写指令文件：</li>
</ul>
<blockquote>
<p>index.js</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> program = <span class="hljs-built_in">require</span>(<span class="hljs-string">'commander'</span>);

program
  .version(<span class="hljs-string">'0.0.1'</span>)
  .description(<span class="hljs-string">'小工具指令清单'</span>)
  .option(<span class="hljs-string">'-s, --sort <path>'</span>, <span class="hljs-string">'排序功能'</span>, <span class="hljs-string">''</span>)

program.parse(process.argv);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>package.json（自动生成）</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js">&#123;
  <span class="hljs-string">"name"</span>: <span class="hljs-string">"test"</span>,
  <span class="hljs-string">"version"</span>: <span class="hljs-string">"1.0.0"</span>,
  <span class="hljs-string">"description"</span>: <span class="hljs-string">""</span>,
  <span class="hljs-string">"main"</span>: <span class="hljs-string">"index.js"</span>,
  <span class="hljs-string">"scripts"</span>: &#123;
    <span class="hljs-string">"test"</span>: <span class="hljs-string">"echo \"Error: no test specified\" && exit 1"</span>
  &#125;,
  <span class="hljs-string">"keywords"</span>: [],
  <span class="hljs-string">"author"</span>: <span class="hljs-string">""</span>,
  <span class="hljs-string">"license"</span>: <span class="hljs-string">"ISC"</span>,
  <span class="hljs-string">"dependencies"</span>: &#123;
    <span class="hljs-string">"commander"</span>: <span class="hljs-string">"^7.2.0"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这份代码的逻辑是：</p>
<ol>
<li>引用 <code>commander</code></li>
<li>描述 <code>commander</code> 的 <code>version</code> 等参数</li>
<li>用 <code>commander</code> 掌控 <code>process.argv</code></li>
</ol>
<p>重点看看在这份代码中第 2 段的参数：</p>
<blockquote>
<p>参数什么的看起来很烦躁，但是不了解又不知道还可以怎么用</p>
</blockquote>
<ul>
<li><code>version</code>：版本
<ul>
<li>用法：<code>.version('x.y.z')</code></li>
</ul>
</li>
<li><code>description</code>：描述
<ul>
<li>用法：<code>.description('小工具指令清单')</code></li>
</ul>
</li>
<li><code>option</code>：选项
<ul>
<li>用法：<code>.option('-n, --name <name>', 'your name', 'jsliang')</code></li>
<li>第一个参数是选项定义，可以用 <code>|</code>，<code>,</code> 和 <code>' '</code> 空格连接</li>
<li>第二个参数为选项描述</li>
<li>第三个参数为选项参数默认值（可选）</li>
</ul>
</li>
</ul>
<p>所以下面我们可以查看到一些信息。</p>
<ul>
<li>执行命令：<code>node index.js -h</code></li>
</ul>
<p>得到下面结果：</p>
<pre><code class="copyable">Usage: index [options]

小工具指令清单

Options:
  -V, --version           output the version number
  -s, --sort <path>       排序功能 (default: "")
  -h, --help              display help for command
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样我们就完成了一些小指令，那么怎么操作呢？</p>
<ul>
<li>排序：<code>node index.js -s "jsliang"</code></li>
</ul>
<p>当然，这样感觉太怪了，能不能像日常开发一样，可以 <code>npm run dev</code>、<code>npm run xxx</code> 的方式执行？</p>
<p>当然是可以的！</p>
<h2 data-id="heading-3"><a name="user-content-chapter-four" id="user-content-chapter-four" href="https://juejin.cn/post/undefined"></a>四 实践：文件重排功能</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6973888151421108254#chapter-one">返回目录</a></p>
</blockquote>
<p>讲了那么多，做个小实践吧！</p>
<hr>
<p>对于 Markdown 编写的文档库来说，如果你不设置文档顺序，那么它就会按照系统的规则来读取目录：</p>
<ul>
<li>1.文章 1</li>
<li>10.文章 10</li>
<li>2.文章 2</li>
<li>……</li>
</ul>
<p>当一个文件夹内容过多的时候，我们希望按照自己的顺序让用户阅读，所以不能找系统的来，因此需要用 Node 写个小工具，读取的时候按照希望的排序来读取，这就是我们开发小工具的初衷。</p>
<p>当然，还有个很重要的功能，就是当我们希望在第 1 篇和第 2 篇文章中间插入一篇文章的时候，例如：</p>
<ul>
<li>1.文章 1</li>
<li>1-1.文章 1-1</li>
<li>2.文章 2</li>
<li>……</li>
</ul>
<p>我们还需要将这个目录结构进行重新排序，让新文章插入到指定位置。</p>
<h3 data-id="heading-4"><a name="user-content-chapter-four-one" id="user-content-chapter-four-one" href="https://juejin.cn/post/undefined"></a>4.1 实践目录</h3>
<blockquote>
<p><a href="https://juejin.cn/post/6973888151421108254#chapter-one">返回目录</a></p>
</blockquote>
<p>此时我们的目录为：</p>
<pre><code class="copyable">+ docs
  + 3.目录c
    - 1.目录c1.md
    - 1-1.目录c2.md
    - 2.目录c3.md
  - 1.文章a.md
  - 2.文章b.md
  - 10.文章d.md
+ src
  - config.ts
  - index.ts【已有】
  - sortCatalog.ts
- .eslintrc.js【已有】
- package.json【已有】
- tsconfig.json【已有】
<span class="copy-code-btn">复制代码</span></code></pre>
<p>该目录的 <code>.eslintrc.js</code>、<code>package-lock.json</code>、<code>package.json</code> 和 <code>tsconfig.json</code> 是自动创建的，TypeScript 的配置看前置文章，这里不做累述。</p>
<p><code>docs</code> 目录下创建几个空 Markdown 文件，文件名照抄即可。</p>
<blockquote>
<p>为了避免小伙伴误操作，还是截个图吧</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1acefece99b43f7a332a79b2e4537bf~tplv-k3u1fbpfcp-watermark.image" alt="commander-01.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5"><a name="user-content-chapter-four-two" id="user-content-chapter-four-two" href="https://juejin.cn/post/undefined"></a>4.2 编写 commander</h3>
<blockquote>
<p><a href="https://juejin.cn/post/6973888151421108254#chapter-one">返回目录</a></p>
</blockquote>
<p>加入 <code>commonder</code> 只需要往 <code>package.json</code> 和 <code>index.ts</code> 上配置即可。</p>
<ul>
<li>初始化 <code>package.json</code>：<code>npm init --yes</code>（之前已配置）</li>
<li>安装 <code>commander</code>：<code>npm i commander</code></li>
</ul>
<blockquote>
<p>package.json</p>
</blockquote>
<pre><code class="hljs language-json copyable" lang="json">&#123;
  <span class="hljs-attr">"name"</span>: <span class="hljs-string">"jsliang"</span>,
  <span class="hljs-attr">"version"</span>: <span class="hljs-string">"1.0.0"</span>,
  <span class="hljs-attr">"description"</span>: <span class="hljs-string">"FE-util"</span>,
  <span class="hljs-attr">"main"</span>: <span class="hljs-string">"index.js"</span>,
  <span class="hljs-attr">"scripts"</span>: &#123;
    <span class="hljs-attr">"sort"</span>: <span class="hljs-string">"ts-node ./src/index.ts sort"</span>
  &#125;,
  <span class="hljs-attr">"keywords"</span>: [],
  <span class="hljs-attr">"author"</span>: <span class="hljs-string">""</span>,
  <span class="hljs-attr">"license"</span>: <span class="hljs-string">"ISC"</span>,
  <span class="hljs-attr">"devDependencies"</span>: &#123;
    <span class="hljs-attr">"@types/node"</span>: <span class="hljs-string">"^15.0.2"</span>,
    <span class="hljs-attr">"@typescript-eslint/eslint-plugin"</span>: <span class="hljs-string">"^4.23.0"</span>,
    <span class="hljs-attr">"@typescript-eslint/parser"</span>: <span class="hljs-string">"^4.23.0"</span>,
    <span class="hljs-attr">"eslint"</span>: <span class="hljs-string">"^7.26.0"</span>,
    <span class="hljs-attr">"ts-node"</span>: <span class="hljs-string">"^9.1.1"</span>,
    <span class="hljs-attr">"typescript"</span>: <span class="hljs-string">"^4.2.4"</span>
  &#125;,
  <span class="hljs-attr">"dependencies"</span>: &#123;
    <span class="hljs-attr">"commander"</span>: <span class="hljs-string">"^7.2.0"</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意 <code>scripts</code> 改变了，记得复制过去</p>
</blockquote>
<p>然后简单写写 <code>index.ts</code> 里面内容</p>
<blockquote>
<p>src/index.ts</p>
</blockquote>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> program <span class="hljs-keyword">from</span> <span class="hljs-string">'commander'</span>;
<span class="hljs-keyword">import</span> &#123; sortCatalog &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./sortCatalog'</span>;

program
  .version(<span class="hljs-string">'0.0.1'</span>)
  .description(<span class="hljs-string">'工具库'</span>)

program
  .command(<span class="hljs-string">'sort <path>'</span>)
  .description(<span class="hljs-string">'文件排序功能。示例：npm run sort "docs" 或者 npm run sort " C:/code/jsliang/src/docs"'</span>)
  .action(<span class="hljs-function">(<span class="hljs-params">path: <span class="hljs-built_in">string</span></span>) =></span> &#123;
    sortCatalog(<span class="hljs-string">`../<span class="hljs-subst">$&#123;path&#125;</span>`</span>); <span class="hljs-comment">// 为了更便捷，先退一层到外边</span>
  &#125;);

program.parse(process.argv);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6"><a name="user-content-chapter-four-three" id="user-content-chapter-four-three" href="https://juejin.cn/post/undefined"></a>4.3 编写排序功能</h3>
<blockquote>
<p><a href="https://juejin.cn/post/6973888151421108254#chapter-one">返回目录</a></p>
</blockquote>
<p>准备好基础配置之后，只需要往 <code>sortCatalog.ts</code> 里面添加内容即可：</p>
<blockquote>
<p>src/sortCatalog.ts</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@name </span>文件排序功能
 * <span class="hljs-doctag">@time </span>2021-05-22 16:08:06
 * <span class="hljs-doctag">@description </span>规则
   1. 系统顺序 1/10/2/21/3，希望排序 1/2/3/10/21
   2. 插入文件 1/2/1-1，希望排序 1/2/3（将 1-1 变成 2，2 变成 3）
*/</span>
<span class="hljs-keyword">import</span> fs <span class="hljs-keyword">from</span> <span class="hljs-string">'fs'</span>;
<span class="hljs-keyword">import</span> path <span class="hljs-keyword">from</span> <span class="hljs-string">'path'</span>;
<span class="hljs-keyword">import</span> &#123; IGNORE_PATH &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./config'</span>;

<span class="hljs-keyword">const</span> recursion = <span class="hljs-function">(<span class="hljs-params">filePath: string, level = <span class="hljs-number">0</span></span>) =></span> &#123;
  <span class="hljs-keyword">const</span> files = fs.readdirSync(filePath);

  files
    .filter((<span class="hljs-function"><span class="hljs-params">item</span> =></span> !IGNORE_PATH.includes(item))) <span class="hljs-comment">// 过滤忽略文件/文件夹</span>
    .sort(<span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span>
      <span class="hljs-built_in">Number</span>((a.split(<span class="hljs-string">'.'</span>)[<span class="hljs-number">0</span>]).replace(<span class="hljs-string">'-'</span>, <span class="hljs-string">'.'</span>))
      - <span class="hljs-built_in">Number</span>((b.split(<span class="hljs-string">'.'</span>)[<span class="hljs-number">0</span>]).replace(<span class="hljs-string">'-'</span>, <span class="hljs-string">'.'</span>))
    ) <span class="hljs-comment">// 排序文件夹</span>
    .forEach(<span class="hljs-function">(<span class="hljs-params">item, index</span>) =></span> &#123; <span class="hljs-comment">// 遍历文件夹</span>
      <span class="hljs-comment">// 设置旧文件名称和新文件名称</span>
      <span class="hljs-keyword">const</span> oldFileName = item;
      <span class="hljs-keyword">const</span> newFileName = <span class="hljs-string">`<span class="hljs-subst">$&#123;index + <span class="hljs-number">1</span>&#125;</span>.<span class="hljs-subst">$&#123;oldFileName.slice(oldFileName.indexOf(<span class="hljs-string">'.'</span>) + <span class="hljs-number">1</span>)&#125;</span>`</span>;

      <span class="hljs-comment">// 设置旧文件路径和新文件路径</span>
      <span class="hljs-keyword">const</span> oldPath = <span class="hljs-string">`<span class="hljs-subst">$&#123;filePath&#125;</span>/<span class="hljs-subst">$&#123;oldFileName&#125;</span>`</span>;
      <span class="hljs-keyword">const</span> newPath = <span class="hljs-string">`<span class="hljs-subst">$&#123;filePath&#125;</span>/<span class="hljs-subst">$&#123;newFileName&#125;</span>`</span>;

      <span class="hljs-comment">// 判断文件格式</span>
      <span class="hljs-keyword">const</span> stat = fs.statSync(oldPath);

      <span class="hljs-comment">// 判断是文件夹还是文件</span>
      <span class="hljs-keyword">if</span> (stat.isFile()) &#123;
        fs.renameSync(oldPath, newPath); <span class="hljs-comment">// 重命名文件</span>
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (stat.isDirectory()) &#123;
        fs.renameSync(oldPath, newPath); <span class="hljs-comment">// 重命名文件夹</span>
        recursion(newPath, level + <span class="hljs-number">1</span>); <span class="hljs-comment">// 递归文件夹</span>
      &#125;
    &#125;);
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> sortCatalog = (filePath: string): <span class="hljs-function"><span class="hljs-params">boolean</span> =></span> &#123;
  <span class="hljs-comment">// 绝对路径</span>
  <span class="hljs-keyword">if</span> (path.isAbsolute(filePath)) &#123;
    recursion(filePath);
  &#125; <span class="hljs-keyword">else</span> &#123; <span class="hljs-comment">// 相对路径</span>
    recursion(path.join(__dirname, filePath));
  &#125;

  <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>有小伙伴看完肯定好奇 <code>config.ts</code> 是什么，其实就是全局配置而已：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/**
 * <span class="hljs-doctag">@name </span>默认的全局配置
 * <span class="hljs-doctag">@time </span>2021-05-22 16:12:21
 */</span>
<span class="hljs-keyword">import</span> path <span class="hljs-keyword">from</span> <span class="hljs-string">'path'</span>;

<span class="hljs-comment">// 基础目录</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> BASE_PATH = path.join(__dirname, <span class="hljs-string">'./docs'</span>);

<span class="hljs-comment">// 忽略目录</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> IGNORE_PATH = [
  <span class="hljs-string">'.vscode'</span>,
  <span class="hljs-string">'node_modules'</span>,
];
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当我们没有配置的时候，就给默认的配置。</p>
<h3 data-id="heading-7"><a name="user-content-chapter-four-four" id="user-content-chapter-four-four" href="https://juejin.cn/post/undefined"></a>4.4 运行内容</h3>
<blockquote>
<p><a href="https://juejin.cn/post/6973888151421108254#chapter-one">返回目录</a></p>
</blockquote>
<p>OK，准备完毕，就可以耍起来了。</p>
<p>当前 <code>docs</code> 下目录结构为：</p>
<pre><code class="copyable">- 1.文章a.md
- 10.文章d.md
- 2.文章b.md
- 3.目录c
  - 1-1.目录c2.md
  - 1.目录c1.md
  - 2.目录c3.md
<span class="copy-code-btn">复制代码</span></code></pre>
<p>而我们运行 <code>npm run sort "docs"</code> 后，新目录列表变成了：</p>
<pre><code class="copyable">- 1.文章a.md
- 2.文章b.md
- 3.目录c
  - 1.目录c1.md
  - 2.目录c2.md
  - 3.目录c3.md
- 4.文章d.md
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d1f7ae8d74284a0a9eca0bb010cf8f17~tplv-k3u1fbpfcp-watermark.image" alt="commander-02.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样，我们简单的案例就做好啦！是不是非常简单！</p>
<h2 data-id="heading-8"><a name="user-content-chapter-five" id="user-content-chapter-five" href="https://juejin.cn/post/undefined"></a>五 常用 commander 配置</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6973888151421108254#chapter-one">返回目录</a></p>
</blockquote>
<p>下面例举下我们非常不想看，但是正常使用又常见的 <code>commander</code> 配置：</p>
<ul>
<li><code>version</code>：版本。用来设置命令程序的版本号
<ul>
<li>用法：<code>.version('x.y.z')</code></li>
</ul>
</li>
<li><code>description</code>：描述。用来设置命令的描述
<ul>
<li>用法：<code>.description('小工具指令清单')</code></li>
</ul>
</li>
<li><code>option</code>：选项。
<ul>
<li>用法：<code>.option('-n, --name <name>', 'your name', 'jsliang')</code></li>
<li>第一个参数是选项定义，可以用 <code>|</code>，<code>,</code> 和 <code>' '</code> 空格连接，参数可以用 <code><></code>（必填）或者 <code>[]</code>（选填）修饰</li>
<li>第二个参数为选项描述</li>
<li>第三个参数为选项参数默认值（可选）</li>
</ul>
</li>
<li><code>command</code>：命令
<ul>
<li>用法：<code>.command('init <path>', 'description')</code></li>
<li><code>command</code> 用法稍微复杂，原则上接受 3 个参数，第一个为命令定义，第二个命令描述，第三个为命令辅助修饰对象</li>
<li>第一个参数可以使用 <code><></code> 或者 <code>[]</code> 修饰命令参数</li>
<li>第二个参数可选
<ul>
<li>当没有第二个参数时，<code>commander.js</code> 将返回 <code>Command</code> 对象</li>
<li>当带有第二个参数，将返回原型对象，并且没有显示调用 <code>action(fn)</code> 时，将会使用子命令模式</li>
<li>子命令模式：<code>./pm</code>、<code>./pm-install</code>、<code>./pm-search</code> 等，这些子命令跟主命令在不同的文件中</li>
</ul>
</li>
<li>第三个参数一般不同，他可以设置是否显示使用的子命令模式</li>
</ul>
</li>
<li><code>action</code>：动作。用来设置命令执行的相关回调
<ul>
<li>用法：<code>.action(fn)</code></li>
<li><code>fn</code> 可以接受命令的参数为函数形参，顺序与 <code>command()</code> 中定义的顺序一致</li>
</ul>
</li>
<li><code>parse</code>：解析 <code>process.argv</code>
<ul>
<li>用法：<code>program.parse(process.argv)</code></li>
<li>这个 API 一般在最后调用，用来解析 <code>process.argv</code></li>
</ul>
</li>
</ul>
<p>OK，<code>commander</code> 的简单介绍到此结束，我们下期见！</p>
<h2 data-id="heading-9"><a name="user-content-chapter-six" id="user-content-chapter-six" href="https://juejin.cn/post/undefined"></a>六 参考文献</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6973888151421108254#chapter-one">返回目录</a></p>
</blockquote>
<ul>
<li><a href="https://github.com/tj/commander.js/blob/master/Readme_zh-CN.md" target="_blank" rel="nofollow noopener noreferrer">Github：commander</a></li>
<li><a href="https://www.w3cschool.cn/xhwqi/xhwqi-4hyt24se.html" target="_blank" rel="nofollow noopener noreferrer">W3CSchool：使用commander.js做一个Nodejs命令行程序</a></li>
</ul>
<hr>
<blockquote>
<p>jsliang 的文档库由 <a href="https://github.com/LiangJunrong" target="_blank" rel="nofollow noopener noreferrer">梁峻荣</a> 采用 <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank" rel="nofollow noopener noreferrer">知识共享 署名-非商业性使用-相同方式共享 4.0 国际 许可协议</a> 进行许可。<br>基于 <a href="https://github.com/LiangJunrong/document-library" target="_blank" rel="nofollow noopener noreferrer">github.com/LiangJunron…</a> 上的作品创作。<br>本许可协议授权之外的使用权限可以从 <a href="https://creativecommons.org/licenses/by-nc-sa/2.5/cn/" target="_blank" rel="nofollow noopener noreferrer">creativecommons.org/licenses/by…</a> 处获得。</p>
</blockquote></div>  
</div>
            