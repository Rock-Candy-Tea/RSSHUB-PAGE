
---
title: 'Node 系列 - 008 - ShellJS'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9a9aca498a24dc7945532a5f7fe30f5~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 21 Jul 2021 17:10:02 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9a9aca498a24dc7945532a5f7fe30f5~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0"><a name="user-content-chapter-one" id="user-content-chapter-one" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a>一 目录</h2>
<p><strong>不折腾的前端，和咸鱼有什么区别</strong></p>









































<table><thead><tr><th>目录</th></tr></thead><tbody><tr><td><a href="https://juejin.cn/post/6987551621500633118#chapter-one" target="_blank" title="#chapter-one">一 目录</a></td></tr><tr><td><a name="user-content-catalog-chapter-two" id="user-content-catalog-chapter-two" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a><a href="https://juejin.cn/post/6987551621500633118#chapter-two" target="_blank" title="#chapter-two">二 前言</a></td></tr><tr><td><a name="user-content-catalog-chapter-three" id="user-content-catalog-chapter-three" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a><a href="https://juejin.cn/post/6987551621500633118#chapter-three" target="_blank" title="#chapter-three">三 Node 编写 bash 脚本的解决方案</a></td></tr><tr><td><a name="user-content-catalog-chapter-four" id="user-content-catalog-chapter-four" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a><a href="https://juejin.cn/post/6987551621500633118#chapter-four" target="_blank" title="#chapter-four">四 编程前置</a></td></tr><tr><td><a name="user-content-catalog-chapter-five" id="user-content-catalog-chapter-five" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a><a href="https://juejin.cn/post/6987551621500633118#chapter-five" target="_blank" title="#chapter-five">五 关闭端口</a></td></tr><tr><td><a name="user-content-catalog-chapter-six" id="user-content-catalog-chapter-six" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a><a href="https://juejin.cn/post/6987551621500633118#chapter-six" target="_blank" title="#chapter-six">六 删除文件/文件夹</a></td></tr><tr><td><a name="user-content-catalog-chapter-seven" id="user-content-catalog-chapter-seven" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a><a href="https://juejin.cn/post/6987551621500633118#chapter-seven" target="_blank" title="#chapter-seven">七 Git 操作</a></td></tr><tr><td> <a href="https://juejin.cn/post/6987551621500633118#chapter-seven-one" target="_blank" title="#chapter-seven-one">7.1 工作中常用 Git 指令</a></td></tr><tr><td> <a href="https://juejin.cn/post/6987551621500633118#chapter-seven-two" target="_blank" title="#chapter-seven-two">7.2 切换分支</a></td></tr><tr><td><a name="user-content-catalog-chapter-eight" id="user-content-catalog-chapter-eight" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a><a href="https://juejin.cn/post/6987551621500633118#chapter-eight" target="_blank" title="#chapter-eight">八 总结</a></td></tr><tr><td><a name="user-content-catalog-chapter-night" id="user-content-catalog-chapter-night" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a><a href="https://juejin.cn/post/6987551621500633118#chapter-night" target="_blank" title="#chapter-night">九 参考文献</a></td></tr></tbody></table>
<h2 data-id="heading-1"><a name="user-content-chapter-two" id="user-content-chapter-two" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a>二 前言</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6987551621500633118#chapter-one" target="_blank" title="#chapter-one">返回目录</a></p>
</blockquote>
<p>今天 <strong>jsliang</strong> 在工作中又爽了一把，开通了 VIP 通道：</p>
<ol>
<li>自动下载 Excel 文件</li>
<li>拷贝到指定目录</li>
<li>执行多语言导入操作</li>
<li>将导入的资源 <code>git push</code> 上去</li>
</ol>
<p>虽然看上去粗略的操作是这样，没有什么可讲的。</p>
<p>但是在操作中的时候，可能就比较繁琐了，例如单单导入资源后，进行的 <code>git</code> 操作：</p>
<ol>
<li>添加暂存区：<code>git add .</code></li>
<li>切换分支：<code>git checkout -b <branch></code></li>
<li>提交本地版本库：<code>git commit -m "feat: 「多语言」新资源 #master_0720"</code></li>
<li>提交远程分支：<code>git push --set-upstream origin <branch></code></li>
</ol>
<p>当然，不仅仅是这个，你提交前肯定还得校验下你的多语言资源添加完后，构建是否能顺利通过……</p>
<hr>
<p>所以，叨了那么多，其实单纯是为了引出 <code>bash</code> 指令的操作。</p>
<p>在工作中，你可能会碰到：</p>
<ul>
<li>Git 系列操作</li>
<li>关闭被占用的系统端口</li>
<li>删除指定文件/文件夹等</li>
<li>……</li>
</ul>
<p>但是，对于这些操作你可能一时半会又忘记它的指令，或者它的指令太繁琐了，所以 <strong>jsliang</strong> 觉得将这些内容装起来，岂不省事？</p>
<h2 data-id="heading-2"><a name="user-content-chapter-three" id="user-content-chapter-three" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a>三 Node 编写 bash 脚本的解决方案</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6987551621500633118#chapter-one" target="_blank" title="#chapter-one">返回目录</a></p>
</blockquote>
<p>其实关于这个解决方案，<strong>jsliang</strong> 还是嫌麻烦，所以直接上了 <code>ShellJS</code>：</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fshelljs%2Fshelljs" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/shelljs/shelljs" ref="nofollow noopener noreferrer">ShellJS - Unix shell commands for Node.js</a></li>
</ul>
<p>如果小伙伴觉得这样直接上方案有点唐突，希望有个参考对比，可以看：</p>
<ul>
<li><a href="https://juejin.cn/post/6979989936137043999" target="_blank" title="https://juejin.cn/post/6979989936137043999">Node.js 写 bash 脚本终极方案</a></li>
</ul>
<p>作者比对了 Node 自带的 <code>child_process</code> API、<code>ShellJS</code> 和 <code>zx</code>，最终采取了 <code>zx</code> 的方案。</p>
<p>当然，<strong>jsliang</strong> 工作中用的还是 <code>ShellJS</code>，不想那么累再探索同类库了，所以就安装 <code>ShellJS</code> 吧~</p>
<ul>
<li>安装：<code>npm i shelljs</code></li>
<li>安装 TS 编译：<code>npm i @types/shelljs -D</code></li>
</ul>
<p>安装完毕，开始折腾！</p>
<h2 data-id="heading-3"><a name="user-content-chapter-four" id="user-content-chapter-four" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a>四 编程前置</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6987551621500633118#chapter-one" target="_blank" title="#chapter-one">返回目录</a></p>
</blockquote>
<p>为了让代码不显得那么又臭又长。</p>
<p><strong>jsliang</strong> 写完文章后，通篇阅读 3 次以上，将下文中重复的代码和问题情况给整理到这里来了，所以小伙伴们拷贝代码前，最后仔细阅读这一章节内容，拜托啦~</p>
<blockquote>
<p>warn! please read the following carefully</p>
</blockquote>
<p>全文目录如下，小伙伴们记得提前新建好目录：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9a9aca498a24dc7945532a5f7fe30f5~tplv-k3u1fbpfcp-watermark.image" alt="shell-00.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后重复代码如下：</p>
<blockquote>
<p>src/common/index.ts</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; inquirer &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../base/inquirer'</span>;
<span class="hljs-keyword">import</span> &#123; Result &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../base/interface'</span>;

<span class="hljs-comment">// 系统操作</span>
<span class="hljs-keyword">import</span> &#123; sortCatalog &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../base/file/sortDir'</span>;
<span class="hljs-keyword">import</span> &#123; deleteDir &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../base/file/deleteDir'</span>;

<span class="hljs-comment">// 多语言</span>
<span class="hljs-keyword">import</span> &#123; downLoadExcel &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./language/download'</span>;
<span class="hljs-keyword">import</span> &#123; importLanguage &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./language/import'</span>;
<span class="hljs-keyword">import</span> &#123; exportLanguage &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./language/export'</span>;

<span class="hljs-comment">// shell 操作</span>
<span class="hljs-keyword">import</span> &#123; closePort &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../base/shell/closePort'</span>;
<span class="hljs-keyword">import</span> &#123; gitCheckout &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../base/shell/gitCheckout'</span>;

<span class="hljs-comment">// 问题记录器</span>
<span class="hljs-keyword">const</span> answers = &#123;
  <span class="hljs-attr">q0</span>: <span class="hljs-string">''</span>,
  <span class="hljs-attr">q1</span>: <span class="hljs-string">''</span>,
  <span class="hljs-attr">q2</span>: <span class="hljs-string">''</span>,
  <span class="hljs-attr">q3</span>: <span class="hljs-string">''</span>,
  <span class="hljs-attr">q4</span>: <span class="hljs-string">''</span>,
  <span class="hljs-attr">q5</span>: <span class="hljs-string">''</span>,
  <span class="hljs-attr">q6</span>: <span class="hljs-string">''</span>,
  <span class="hljs-attr">q7</span>: <span class="hljs-string">''</span>,
  <span class="hljs-attr">q8</span>: <span class="hljs-string">''</span>,
&#125;;

<span class="hljs-keyword">const</span> common = (): <span class="hljs-function"><span class="hljs-params">void</span> =></span> &#123;
  <span class="hljs-comment">// 问题路线：看 questionList.ts</span>
  <span class="hljs-keyword">const</span> questionList = [
    <span class="hljs-comment">// q0</span>
    &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'list'</span>,
      <span class="hljs-attr">message</span>: <span class="hljs-string">'请问需要什么服务？'</span>,
      <span class="hljs-attr">choices</span>: [<span class="hljs-string">'公共服务'</span>, <span class="hljs-string">'多语言'</span>],
    &#125;,
    <span class="hljs-comment">// q1</span>
    &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'list'</span>,
      <span class="hljs-attr">message</span>: <span class="hljs-string">'当前公共服务有：'</span>,
      <span class="hljs-attr">choices</span>: [<span class="hljs-string">'文件排序'</span>, <span class="hljs-string">'关闭端口'</span>, <span class="hljs-string">'删除文件夹'</span>, <span class="hljs-string">'Git 操作'</span>],
    &#125;,
    <span class="hljs-comment">// q2</span>
    &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'input'</span>,
      <span class="hljs-attr">message</span>: <span class="hljs-string">'需要排序的文件夹为？（绝对路径）'</span>,
    &#125;,
    <span class="hljs-comment">// q3</span>
    &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'list'</span>,
      <span class="hljs-attr">message</span>: <span class="hljs-string">'请问多语言需要什么支持？'</span>,
      <span class="hljs-attr">choices</span>: [
        <span class="hljs-string">'下载多语言资源'</span>,
        <span class="hljs-string">'导入多语言资源'</span>,
        <span class="hljs-string">'导出多语言资源'</span>,
      ],
    &#125;,
    <span class="hljs-comment">// q4</span>
    &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'input'</span>,
      <span class="hljs-attr">message</span>: <span class="hljs-string">'资源下载地址（HTTP）？'</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-string">'https://www.kdocs.cn/l/sdwvJUKBzkK2'</span>,
    &#125;,
    <span class="hljs-comment">// q5</span>
    &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'input'</span>,
      <span class="hljs-attr">message</span>: <span class="hljs-string">'你需要关闭的端口是？'</span>,
    &#125;,
    <span class="hljs-comment">// q6</span>
    &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'input'</span>,
      <span class="hljs-attr">message</span>: <span class="hljs-string">'你需要删除的路径是？（全路径）'</span>,
    &#125;,
    <span class="hljs-comment">// q7</span>
    &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'list'</span>,
      <span class="hljs-attr">message</span>: <span class="hljs-string">'请问 Git 需要什么支持？'</span>,
      <span class="hljs-attr">choices</span>: [
        <span class="hljs-string">'切换分支'</span>,
        <span class="hljs-comment">// More...</span>
      ],
    &#125;,
    <span class="hljs-comment">// q8</span>
    &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'inupt'</span>,
      <span class="hljs-attr">message</span>: <span class="hljs-string">'Git 分支名是？'</span>,
    &#125;,
  ];

  <span class="hljs-keyword">const</span> answerList = [
    <span class="hljs-comment">// q0 - 请问需要什么服务？</span>
    <span class="hljs-keyword">async</span> (result: Result, <span class="hljs-attr">questions</span>: any) => &#123;
      answers.q0 = result.answer;
      <span class="hljs-keyword">switch</span> (result.answer) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'公共服务'</span>:
          questions[<span class="hljs-number">1</span>]();
          <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'多语言'</span>:
          questions[<span class="hljs-number">3</span>]();
          <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">default</span>: <span class="hljs-keyword">break</span>;
      &#125;
    &#125;,
    <span class="hljs-comment">// q1 - 当前公共服务有：</span>
    <span class="hljs-keyword">async</span> (result: Result, <span class="hljs-attr">questions</span>: any) => &#123;
      answers.q1 = result.answer;
      <span class="hljs-keyword">switch</span> (result.answer) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'文件排序'</span>: questions[<span class="hljs-number">2</span>](); <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'关闭端口'</span>: questions[<span class="hljs-number">5</span>](); <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'删除文件夹'</span>: questions[<span class="hljs-number">6</span>](); <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'Git 操作'</span>: questions[<span class="hljs-number">7</span>](); <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">default</span>: <span class="hljs-keyword">break</span>;
      &#125;
    &#125;,
    <span class="hljs-comment">// q2 - 需要排序的文件夹为？（绝对路径）</span>
    <span class="hljs-keyword">async</span> (result: Result, <span class="hljs-attr">_questions</span>: any, <span class="hljs-attr">prompts</span>: any) => &#123;
      answers.q2 = result.answer;
      <span class="hljs-keyword">const</span> sortResult = <span class="hljs-keyword">await</span> sortCatalog(result.answer);
      <span class="hljs-keyword">if</span> (sortResult) &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'排序成功！'</span>);
        prompts.complete();
      &#125;
    &#125;,
    <span class="hljs-comment">// q3 - 请问多语言需要什么支持？</span>
    <span class="hljs-keyword">async</span> (result: Result, <span class="hljs-attr">questions</span>: any, <span class="hljs-attr">prompts</span>: any) => &#123;
      answers.q3 = result.answer;
      <span class="hljs-keyword">switch</span> (result.answer) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'下载多语言资源'</span>:
        <span class="hljs-keyword">case</span> <span class="hljs-string">'导入多语言资源'</span>:
          questions[<span class="hljs-number">4</span>]();
          <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'导出多语言资源'</span>:
          <span class="hljs-keyword">const</span> exportResult = <span class="hljs-keyword">await</span> exportLanguage();
          <span class="hljs-keyword">if</span> (exportResult) &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'导出成功！'</span>);
            prompts.complete();
          &#125;
        <span class="hljs-attr">default</span>: <span class="hljs-keyword">break</span>;
      &#125;
    &#125;,
    <span class="hljs-comment">// q4 - 资源下载地址（HTTP）？</span>
    <span class="hljs-keyword">async</span> (result: Result) => &#123;
      answers.q4 = result.answer;
      <span class="hljs-keyword">const</span> download = <span class="hljs-keyword">async</span> (): <span class="hljs-built_in">Promise</span><any> => &#123;
        <span class="hljs-keyword">const</span> downloadResult = <span class="hljs-keyword">await</span> downLoadExcel(result.answer);
        <span class="hljs-keyword">if</span> (downloadResult) &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'下载成功！'</span>);
          <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
        &#125;
      &#125;;
      <span class="hljs-keyword">switch</span> (answers.q3) &#123;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'下载多语言资源'</span>:
          <span class="hljs-keyword">await</span> download();
          <span class="hljs-keyword">break</span>;
        <span class="hljs-keyword">case</span> <span class="hljs-string">'导入多语言资源'</span>:
          <span class="hljs-keyword">await</span> download();
          <span class="hljs-keyword">const</span> importResult = <span class="hljs-keyword">await</span> importLanguage();
          <span class="hljs-keyword">if</span> (importResult) &#123;
            <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'导入完毕！'</span>);
          &#125;
        <span class="hljs-attr">default</span>:
          <span class="hljs-keyword">break</span>;
      &#125;
    &#125;,
    <span class="hljs-comment">// q5 - 你需要关闭的端口是？</span>
    <span class="hljs-keyword">async</span> (result: Result, <span class="hljs-attr">_questions</span>: any, <span class="hljs-attr">prompts</span>: any) => &#123;
      answers.q5 = result.answer;
      <span class="hljs-keyword">const</span> closeResult = <span class="hljs-keyword">await</span> closePort(result.answer);
      <span class="hljs-keyword">if</span> (closeResult) &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'关闭成功'</span>);
        prompts.complete();
      &#125;
    &#125;,
    <span class="hljs-comment">// q6 - 你需要删除的路径是？（全路径）</span>
    <span class="hljs-keyword">async</span> (result: Result, <span class="hljs-attr">_questions</span>: any, <span class="hljs-attr">prompts</span>: any) => &#123;
      answers.q6 = result.answer;
      <span class="hljs-keyword">const</span> deleteResult = <span class="hljs-keyword">await</span> deleteDir(result.answer);
      <span class="hljs-keyword">if</span> (deleteResult) &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'删除成功'</span>);
        prompts.complete();
      &#125;
    &#125;,
    <span class="hljs-comment">// q7 - 请问 Git 需要什么支持？</span>
    <span class="hljs-keyword">async</span> (result: Result, <span class="hljs-attr">questions</span>: any) => &#123;
      answers.q7 = result.answer;
      questions[<span class="hljs-number">8</span>]();
    &#125;,
    <span class="hljs-comment">// q8 - Git 分支名是？</span>
    <span class="hljs-keyword">async</span> (result: Result, <span class="hljs-attr">_questions</span>: any, <span class="hljs-attr">prompts</span>: any) => &#123;
      answers.q8 = result.answer;
      <span class="hljs-keyword">const</span> checkoutResult = <span class="hljs-keyword">await</span> gitCheckout(result.answer);
      <span class="hljs-keyword">if</span> (checkoutResult) &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'切换成功'</span>);
        prompts.complete();
      &#125;
    &#125;,
  ];

  inquirer(questionList, answerList);
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> common;

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>src/common/questionList.ts</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// common 板块的问题咨询路线</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> questionList = &#123;
  <span class="hljs-string">'公共服务'</span>: &#123; <span class="hljs-comment">// q0</span>
    <span class="hljs-string">'文件排序'</span>: &#123; <span class="hljs-comment">// q1</span>
      <span class="hljs-string">'需要排序的文件夹'</span>: <span class="hljs-string">'Work 工作'</span>, <span class="hljs-comment">// q2</span>
    &#125;,
    <span class="hljs-string">'关闭端口'</span>: &#123; <span class="hljs-comment">// q1</span>
      <span class="hljs-string">'需要关闭的端口'</span>: <span class="hljs-string">'Work 工作'</span>, <span class="hljs-comment">// q5</span>
    &#125;,
    <span class="hljs-string">'删除文件夹'</span>: &#123; <span class="hljs-comment">// q1</span>
      <span class="hljs-string">'需要删除的路径'</span>: <span class="hljs-string">'Work 工作'</span>, <span class="hljs-comment">// q6</span>
    &#125;,
    <span class="hljs-string">'Git 操作'</span>: &#123; <span class="hljs-comment">// q1</span>
      <span class="hljs-string">'切换分支'</span>: &#123; <span class="hljs-comment">// q7</span>
        <span class="hljs-string">'分支名'</span>: <span class="hljs-string">'Work 工作'</span>, <span class="hljs-comment">// q8</span>
      &#125;,
    &#125;,
  &#125;,
  <span class="hljs-string">'多语言'</span>: &#123; <span class="hljs-comment">// q0</span>
    <span class="hljs-string">'下载多语言资源'</span>: &#123; <span class="hljs-comment">// q3</span>
      <span class="hljs-string">'下载地址'</span>: <span class="hljs-string">'Work 工作'</span>, <span class="hljs-comment">// q4</span>
    &#125;,
    <span class="hljs-string">'导入多语言资源'</span>: &#123; <span class="hljs-comment">// q3</span>
      <span class="hljs-string">'下载地址'</span>: <span class="hljs-string">'Work 工作'</span>, <span class="hljs-comment">// q4</span>
    &#125;,
    <span class="hljs-string">'导出多语言资源'</span>: &#123; <span class="hljs-comment">// q3</span>
      <span class="hljs-string">'导出全量资源'</span>: <span class="hljs-string">'Work 工作'</span>,
      <span class="hljs-string">'导出单门资源'</span>: <span class="hljs-string">'Work 工作'</span>,
    &#125;
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>后面文章表明：</p>
<blockquote>
<p>更新 src/common/index.ts</p>
</blockquote>
<blockquote>
<p>更新 src/common/questionList.ts</p>
</blockquote>
<p>这种情况，小伙伴们就不用操作啦，本文有 3 个地方都有这种描述的。</p>
<p>同样，为了避免引用和运行代码的时候，报 TypeScript 错误，新增的 3 个文件开头也列一下：</p>
<blockquote>
<p>src/base/file/deleteDir.ts</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> shell <span class="hljs-keyword">from</span> <span class="hljs-string">'shelljs'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> deleteDir = <span class="hljs-keyword">async</span> (path: string): <span class="hljs-built_in">Promise</span><boolean> => &#123;
  <span class="hljs-built_in">console</span>.log(path)
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>src/base/shell/closePort.ts</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> shell <span class="hljs-keyword">from</span> <span class="hljs-string">'shelljs'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> closePort = <span class="hljs-keyword">async</span> (port: string): <span class="hljs-built_in">Promise</span><boolean> => &#123;
  <span class="hljs-built_in">console</span>.log(port);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>src/base/shell/gitCheckout.ts</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> shell <span class="hljs-keyword">from</span> <span class="hljs-string">'shelljs'</span>;

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@name </span>切换分支
 * <span class="hljs-doctag">@description </span>指令合并：
 * 1. git checkout $&#123;branch&#125;
 * 2. git pull
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> </span>branch 分支名
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> gitCheckout = (branch: string): <span class="hljs-function"><span class="hljs-params">boolean</span> =></span> &#123;
  <span class="hljs-built_in">console</span>.log(branch)
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>另外 <code>common</code> 下的 <code>sortCatalog.ts</code> 迁移到 <code>base/file</code> 目录下，并且改名为 <code>sortDir.ts</code> 了。</p>
</blockquote>
<p>那么，准备完毕，开始输出！</p>
<h2 data-id="heading-4"><a name="user-content-chapter-five" id="user-content-chapter-five" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a>五 关闭端口</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6987551621500633118#chapter-one" target="_blank" title="#chapter-one">返回目录</a></p>
</blockquote>
<p>在起一些神奇的服务时，会碰到端口被占用的场景，这时候就需要关闭端口：</p>
<ul>
<li>查看端口占用情况：<code>netstat -ano|findstr "端口号"</code></li>
</ul>
<pre><code class="copyable">PS F:\xxx> netstat -ano|findstr "3001"
  TCP    0.0.0.0:3001           0.0.0.0:0              LISTENING       33396
  TCP    10.13.144.170:63001    183.2.199.241:443      ESTABLISHED     28228
  TCP    [::]:3001              [::]:0                 LISTENING       33396
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>终止 PID：<code>taskkill -F -PID PID号</code></li>
</ul>
<pre><code class="copyable">PS F:\xxx> taskkill -F -PID 33396
成功: 已终止 PID 为 33396 的进程。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么到了 Node 工具库这边，肯定就不要自己去这样操作啦，搞个省事的方式吧：</p>
<blockquote>
<p>更新 src/common/index.ts</p>
</blockquote>
<blockquote>
<p>更新 src/common/questionList.ts</p>
</blockquote>
<p>然后编写 <code>closePort.ts</code>：</p>
<blockquote>
<p>src/base/shell/closePort.ts</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> shell <span class="hljs-keyword">from</span> <span class="hljs-string">'shelljs'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> closePort = <span class="hljs-keyword">async</span> (port: string): <span class="hljs-built_in">Promise</span><boolean> => &#123;
  <span class="hljs-keyword">await</span> shell.exec(<span class="hljs-string">`netstat -ano | findstr :<span class="hljs-subst">$&#123;port&#125;</span>`</span>);

  <span class="hljs-comment">// Windows 下会返回一个端口占用清单，需要自行删除</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'已找到上面清单列表，请执行指令删除端口：taskkill -F -PID PID号'</span>); 

  <span class="hljs-keyword">return</span> <span class="hljs-keyword">await</span> <span class="hljs-literal">true</span>;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注：Windows 打印结果最末尾的为 PID 号</p>
</blockquote>
<p>当然，因为 <code>3001</code> 可能会有好几个 <code>ip</code> 对应的端口，所以后面那个步骤我们仅做了提示，而不是关闭了所有 <code>3001</code> 的端口（需要用户手动操作）。</p>
<p>但是这样总好过我们去记忆这个指令（毕竟 Windows 和 Mac 等的操作指令还不通）</p>
<p>执行 <code>npm run jsliang</code>，运行结果如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/200e200085bf40b794651e0b91880d13~tplv-k3u1fbpfcp-watermark.image" alt="shell-01.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样我们就封装好了关闭端口的，因为不是一键彻底关闭，实用指数给到 ☆☆☆</p>
<h2 data-id="heading-5"><a name="user-content-chapter-six" id="user-content-chapter-six" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a>六 删除文件/文件夹</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6987551621500633118#chapter-one" target="_blank" title="#chapter-one">返回目录</a></p>
</blockquote>
<p>之前在公司为了研究 Windows 如何快速删除 <code>node_modules</code>，<strong>jsliang</strong> 还真翻了下资料找到 3 种删除文件/文件夹的方式：</p>
<ol>
<li><code>cmd.exe</code>：<code>rd /s /q <path></code></li>
<li><code>PowerShell</code>：<code>rd -r <path></code></li>
<li><code>Mac</code>：<code>rm -rf <path></code></li>
</ol>
<p>经过多次亲身体验，在公司中的 32G 内存，500 SSD 的台式电脑中，通过 <code>PowerShell</code> 的删除操作比 <code>cmd.exe</code> 的快（别问我为啥，反正就是快点，仅个人体验，不做科学支撑）。</p>
<p>然后看了下 <code>ShellJS</code>，是有删除方式的：</p>
<ul>
<li>ShellJS：<code>rm()</code> 删除文件，<code>rm('rf', <path>)</code> 删除文件夹</li>
</ul>
<p>当然！奔着探索精神，咱们看看它源码咋实现的：</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fshelljs%2Fshelljs%2Fblob%2Fmaster%2Fsrc%2Frm.js" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/shelljs/shelljs/blob/master/src/rm.js" ref="nofollow noopener noreferrer">GitHub：ShellJS - rm.js</a></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">rmdirSyncRecursive</span>(<span class="hljs-params">dir, force, fromSymlink</span>) </span>&#123;
  
  <span class="hljs-comment">// 1. 先删除目录中的所有文件</span>
  <span class="hljs-keyword">let</span> files = fs.readdirSync(dir);
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < files.length; i++) &#123;
    <span class="hljs-comment">// 1.1 如果是目录则递归调用 rmdirSyncRecursive()</span>
    <span class="hljs-comment">// 1.2 如果是文件则调用 fs.unlinkSync() 执行删除</span>
  &#125;

  <span class="hljs-comment">// 2. 再删除目录</span>
  fs.rmdirSync();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，里面有些细节还是写得不错的，这里就不展开详细讲解，感兴趣的小伙伴可以点击上面链接探索下源码。</p>
<p>所以，咱们就用 <code>ShellJS</code> 的方法吧！如果后面感觉不舒服再替换为系统指令。</p>
<blockquote>
<p>更新 src/common/index.ts</p>
</blockquote>
<blockquote>
<p>更新 src/common/questionList.ts</p>
</blockquote>
<p>然后开始编写 <code>deleteDir.ts</code>：</p>
<blockquote>
<p>src/base/file/deleteDir.ts</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> shell <span class="hljs-keyword">from</span> <span class="hljs-string">'shelljs'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> deleteDir = <span class="hljs-keyword">async</span> (path: string): <span class="hljs-built_in">Promise</span><boolean> => &#123;
  <span class="hljs-comment">/**
   * cmd.exe：rd /s /q <path>
   * PowerShell：rd -r <path>
   * Mac：rm -rf <path>
   * ShellJS：rm() 删除文件，rm('rf', <path>) 删除文件夹
   */</span>
  <span class="hljs-keyword">await</span> shell.rm(<span class="hljs-string">'-rf'</span>, path);
  <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行 <code>npm run jsliang</code>，打印内容如下：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96a58e91ddf64daeb1da638033aa85f1~tplv-k3u1fbpfcp-watermark.image" alt="shell-02.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>搞定，收工！因为不清楚 Node 操作和系统指令哪个比较快，所以暂定实用指数 ☆☆☆</p>
<h2 data-id="heading-6"><a name="user-content-chapter-seven" id="user-content-chapter-seven" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a>七 Git 操作</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6987551621500633118#chapter-one" target="_blank" title="#chapter-one">返回目录</a></p>
</blockquote>
<p>那么最后，来到重头 Git 操作。</p>
<p>想必有些小伙伴会跟 <strong>jsliang</strong> 一样懒？</p>
<ul>
<li><code>git add .</code></li>
<li><code>git commit -m "xxx"</code></li>
<li><code>git push</code></li>
</ul>
<p>已经到了麻木的状态了，<strong>jsliang</strong> 甚至开发了特定的 VS Code 插件：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/038ab7cd5f534d3a962fb0744f1bd6cc~tplv-k3u1fbpfcp-watermark.image" alt="shell-03.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>注：VS Code 也卷，更新太快了我插件接受不了（一定程度上最新 VS Code 用不了该插件），所以我的 VS Code 版本锁死 <code>v1.53.2</code>，啥时候有空操作再更新这个插件了</p>
</blockquote>
<p>在 VS Code 插件中，进行快速的提交操作。</p>
<p>所以在一些常规的 Git 操作我们还是希望能封装起来（不需要记指令，也不想点页面，让它自行跑起来吧）</p>
<h3 data-id="heading-7"><a name="user-content-chapter-seven-one" id="user-content-chapter-seven-one" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a>7.1 工作中常用 Git 指令</h3>
<blockquote>
<p><a href="https://juejin.cn/post/6987551621500633118#chapter-one" target="_blank" title="#chapter-one">返回目录</a></p>
</blockquote>
<p><strong>jsliang</strong> 在工作中经常使用，并记住了的对应指令：</p>
<ul>
<li><code>git pull</code>：拉取代码并自动合并，<strong>jsliang</strong> 这边还会用 <code>git pull --rebase origin master</code>，表明拉取远程分支并基于该分支进行改动</li>
<li><code>git checkout -b <newBranch></code>：从当前分支切新分支</li>
<li><code>git branch -D <branch></code>：根据分支名删除指定分支</li>
<li><code>git add <files></code>：提交到暂存区</li>
<li><code>git commit <description></code>：提交到本地版本库。如果你们仓库有 <code>eslint</code> 检查之类的，强烈推荐 <code>git commit -m "xxx" --no-verify</code>（有时候真不想搞啥检查）</li>
<li><code>git push</code>：提交到远程库。一般新分支操作为 <code>git push -- set upstream origin <branch></code></li>
<li><code>git cherry-pick <commitHash></code>：将指定的提交（<code>commit</code>）应用于其他分支</li>
<li><code>git stash</code>：暂存内容。将暂存区的内容存储到栈中（多次 <code>stash</code> 可以通过多次 <code>pop</code> 推出来）</li>
<li><code>git stash pop</code>：签出内容。将 <code>git stash</code> 中的内容推出来</li>
<li><code>git reset --soft HEAD^</code>：回退版本并保留内容。这个 <code>HEAD^</code> 是指上一个版本，也可以写成 <code>HEAD~1</code>（就是 commit id）</li>
</ul>
<hr>
<p>值得一提的是，<strong>jsliang</strong> 之前还尝试用过：<code>git worktree</code>，它可以同时修改多个版本。</p>
<blockquote>
<p>但是因为嫌麻烦（要记指令），所以就没用了</p>
</blockquote>
<p>同一个 Git 仓库，需要同时修改多个分支，或者需要在 A 分支上参照 B 分支的内容进行修改。</p>
<p>当然这种情况可以用 <code>git clone</code> 拷贝一个新仓库，但是如果你的仓库有点大（几 G 那种），那还是有点嫌麻烦的。</p>
<p>于是就有了 <code>git worktree</code>，指令如下：</p>
<pre><code class="hljs language-shell copyable" lang="shell"><span class="hljs-meta">#</span><span class="bash"> 将 abc 分支切出到另一个目录 jsliang 中</span>
<span class="hljs-meta">#</span><span class="bash"> 注意：这个目录不能在主仓库中</span>
git worktree add ../jsliang abc # git add [<选项>] <路径> [<提交>]
<span class="hljs-meta">
#</span><span class="bash"> 获取帮助</span>
git worktree -h
<span class="hljs-meta">
#</span><span class="bash"> 查看每个工作树的详细信息</span>
git worktree list
<span class="hljs-meta">
#</span><span class="bash"> 更完整的工作树信息</span>
<span class="hljs-meta">#</span><span class="bash"> git worktree list --porcelain</span>
<span class="hljs-meta">
#</span><span class="bash"> 锁定内容，防止被自动删除</span>
git worktree lock
<span class="hljs-meta">
#</span><span class="bash"> 解锁内容</span>
git worktree unlock
<span class="hljs-meta">
#</span><span class="bash"> 迁移到新目录</span>
git worktree move abc ../jsliang2
<span class="hljs-meta">
#</span><span class="bash"> 删除某条工作树</span>
git worktree remove ../jsliang
<span class="hljs-meta">
#</span><span class="bash"> 清除工作树信息</span>
git worktree prune
<span class="copy-code-btn">复制代码</span></code></pre>
<p>常用 <code>git worktree</code> 指令：</p>
<ul>
<li>切出分支：<code>git worktree add ../jsliang abc</code></li>
<li>常用操作：<code>git add .</code>、<code>git commit -m "xxx"</code>、<code>git push</code></li>
<li>关闭分支：<code>git worktree prune</code></li>
</ul>
<hr>
<p>当然，还有 Git 设置代理</p>
<p>科学上网情况下，有时候 Git 并没有生效，克隆或者 <code>push</code> 操作一样卡慢，就需要设置 Git 代理。</p>
<ul>
<li>设置代理</li>
</ul>
<ol>
<li><code>git config --global http.proxy 代理地址</code></li>
<li><code>git config --global https.proxy 代理地址</code></li>
</ol>
<ul>
<li>取消代理</li>
</ul>
<ol>
<li><code>git config --global --unset http.proxy</code></li>
<li><code>git config --global --unset https.proxy</code></li>
</ol>
<ul>
<li>查看已经设置的代理</li>
</ul>
<ol>
<li><code>git config --global --get http.proxy</code></li>
<li><code>git config --global --get https.proxy</code></li>
</ol>
<p>我拿现在用的科学上网代理软件，就设置了 <code>git config --global http.proxy http://127.0.0.1:10809</code>，Git 流畅度提升了挺多。</p>
<h3 data-id="heading-8"><a name="user-content-chapter-seven-two" id="user-content-chapter-seven-two" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a>7.2 切换分支</h3>
<blockquote>
<p><a href="https://juejin.cn/post/6987551621500633118#chapter-one" target="_blank" title="#chapter-one">返回目录</a></p>
</blockquote>
<p>吧啦吧啦说了一通，下面开始干点正活，咱们搞个简单的切换分支：</p>
<blockquote>
<p>更新 src/common/index.ts</p>
</blockquote>
<blockquote>
<p>更新 src/common/questionList.ts</p>
</blockquote>
<p>接着更新下 <code>gitCheckout.ts</code>：</p>
<blockquote>
<p>src/base/shell/gitCheckout.ts</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> shell <span class="hljs-keyword">from</span> <span class="hljs-string">'shelljs'</span>;

<span class="hljs-comment">/**
 * <span class="hljs-doctag">@name </span>切换分支
 * <span class="hljs-doctag">@description </span>指令合并：
 * 1. git checkout $&#123;branch&#125;
 * 2. git pull
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> </span>branch 分支名
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> gitCheckout = (branch: string): <span class="hljs-function"><span class="hljs-params">boolean</span> =></span> &#123;
  <span class="hljs-keyword">if</span> (!shell.which(<span class="hljs-string">'git'</span>)) &#123;
    shell.echo(<span class="hljs-string">'Error: 请先安装 Git！'</span>);
    shell.exit(<span class="hljs-number">1</span>);
  &#125;

  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'开始切换分支：'</span>);
  <span class="hljs-keyword">const</span> checkoutResult = shell.exec(<span class="hljs-string">`git checkout <span class="hljs-subst">$&#123;branch&#125;</span>`</span>);
  <span class="hljs-keyword">if</span> (checkoutResult.code !== <span class="hljs-number">0</span>) &#123;
    shell.echo(<span class="hljs-string">'Error: 切分支失败！'</span>);
    shell.exit(<span class="hljs-number">1</span>);
  &#125;

  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'开始拉取代码，请稍等：'</span>);
  <span class="hljs-keyword">const</span> pullResult = shell.exec(<span class="hljs-string">'git pull'</span>);
  <span class="hljs-keyword">const</span> &#123; stdout, stderr &#125; = pullResult;
  <span class="hljs-keyword">if</span> (pullResult.code === <span class="hljs-number">0</span>) &#123;
    <span class="hljs-keyword">if</span> (stdout.includes(<span class="hljs-string">'from the remote, but no such ref was fetched.'</span>)) &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'你的分支是最新的'</span>);
    &#125; 
  &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (pullResult.code === <span class="hljs-number">1</span>) &#123;
    <span class="hljs-keyword">if</span> (stderr.includes(<span class="hljs-string">'There is no tracking information for the current branch.'</span>)) &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'不存在远程分支'</span>);
    &#125;
  &#125;

  <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后运行：<code>npm run jsliang</code>，跟着指令输入分支名：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2f1d63f002643589bcf619184ebcd2c~tplv-k3u1fbpfcp-watermark.image" alt="shell-04.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时因为是我们随便输入的一个分支，所以它表明切换分支失败了。</p>
<p>当然，小伙伴们可以依据真实业务往里面装载更多的内容，这里就不展开详细讲解，仅做抛砖引玉先吧~</p>
<h2 data-id="heading-9"><a name="user-content-chapter-eight" id="user-content-chapter-eight" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a>八 总结</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6987551621500633118#chapter-one" target="_blank" title="#chapter-one">返回目录</a></p>
</blockquote>
<p>其实最近两天还有在通过汇总 <code>bash</code> 指令来压缩一些工作流程的事，但是碍于一时半会想不到更好的项目例子，所以就没有一一铺开讲解，所以小伙伴们碰到这种情况，欢迎来吐槽评论留言，衷心表示希望能和小伙伴们一起探讨。</p>
<p>那么，关于 <code>ShellJS</code> 咱们就铺垫那么一点了，后面 <strong>jsliang</strong> 在生活、工作中碰到一些有趣的知识点再添加进来吧~</p>
<p>So，下期再会！</p>
<h2 data-id="heading-10"><a name="user-content-chapter-night" id="user-content-chapter-night" target="_blank" ref="nofollow noopener noreferrer" href="https://link.juejin.cn/?target=undefined"></a>九 参考文献</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6987551621500633118#chapter-one" target="_blank" title="#chapter-one">返回目录</a></p>
</blockquote>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fshelljs%2Fshelljs" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/shelljs/shelljs" ref="nofollow noopener noreferrer">GitHub：ShellJS - Unix shell commands for Node.js</a></li>
<li><a href="https://juejin.cn/post/6979989936137043999" target="_blank" title="https://juejin.cn/post/6979989936137043999">掘金：👏 nodejs写bash脚本终极方案！</a></li>
<li><a href="https://link.juejin.cn/?target=http%3A%2F%2Feinverne.github.io%2Fpost%2F2019%2F03%2Fgit-worktree.html" target="_blank" rel="nofollow noopener noreferrer" title="http://einverne.github.io/post/2019/03/git-worktree.html" ref="nofollow noopener noreferrer">GitHub：Git worktree 作用及使用</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2Fffeb38d27f64" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/ffeb38d27f64" ref="nofollow noopener noreferrer">简书：git worktree 的使用</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F92906230" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/92906230" ref="nofollow noopener noreferrer">知乎：Git屠龙技：使用Git Worktree并行开发测试</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zoo.team%2Farticle%2Fhow-to-use-git" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zoo.team/article/how-to-use-git" ref="nofollow noopener noreferrer">政企云前端团队：我在工作中是如何使用 Git 的</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fa%2F1190000038508752" target="_blank" rel="nofollow noopener noreferrer" title="https://segmentfault.com/a/1190000038508752" ref="nofollow noopener noreferrer">SegmentFault：Git 屠龙技：使用 Git Worktree 并行开发测试</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fcode.iamhefang.cn%2Fcontent%2Fhow-to-make-git-auto-use-vpn.html" target="_blank" rel="nofollow noopener noreferrer" title="https://code.iamhefang.cn/content/how-to-make-git-auto-use-vpn.html" ref="nofollow noopener noreferrer">何方的编程之路：Git如何使用代理(VPN)</a></li>
<li><a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.ruanyifeng.com%2Fblog%2F2020%2F04%2Fgit-cherry-pick.html" target="_blank" rel="nofollow noopener noreferrer" title="http://www.ruanyifeng.com/blog/2020/04/git-cherry-pick.html" ref="nofollow noopener noreferrer">阮一峰：cherry-pick</a></li>
</ul>
<hr>
<blockquote>
<p>jsliang 的文档库由 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FLiangJunrong" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/LiangJunrong" ref="nofollow noopener noreferrer">梁峻荣</a> 采用 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fcreativecommons.org%2Flicenses%2Fby-nc-sa%2F4.0%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://creativecommons.org/licenses/by-nc-sa/4.0/" ref="nofollow noopener noreferrer">知识共享 署名-非商业性使用-相同方式共享 4.0 国际 许可协议</a> 进行许可。<br>基于 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FLiangJunrong%2Fdocument-library" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/LiangJunrong/document-library" ref="nofollow noopener noreferrer">github.com/LiangJunron…</a> 上的作品创作。<br>本许可协议授权之外的使用权限可以从 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fcreativecommons.org%2Flicenses%2Fby-nc-sa%2F2.5%2Fcn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://creativecommons.org/licenses/by-nc-sa/2.5/cn/" ref="nofollow noopener noreferrer">creativecommons.org/licenses/by…</a> 处获得。</p>
</blockquote></div>  
</div>
            