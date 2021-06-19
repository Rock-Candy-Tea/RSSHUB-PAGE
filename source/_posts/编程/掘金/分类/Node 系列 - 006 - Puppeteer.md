
---
title: 'Node 系列 - 006 - Puppeteer'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d9bcecb002e4c8ebba51c90e12e5acc~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 18 Jun 2021 15:47:26 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d9bcecb002e4c8ebba51c90e12e5acc~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在前面的 5 篇文章打底下，咱们应该接入点接地气的业务了。</p>
<p>本篇开始将接触前端多语言功能，将讲解如何使用 Puppeteer 控制 Chrome/Chromium，从而达到下载文件的目的。</p>

<h2 data-id="heading-0"><a name="user-content-chapter-one" id="user-content-chapter-one" href="https://juejin.cn/post/undefined"></a>一 目录</h2>
<p><strong>不折腾的前端，和咸鱼有什么区别</strong></p>





























<table><thead><tr><th>目录</th></tr></thead><tbody><tr><td><a href="https://juejin.cn/post/6975282946638872584#chapter-one">一 目录</a></td></tr><tr><td><a name="user-content-catalog-chapter-two" id="user-content-catalog-chapter-two" href="https://juejin.cn/post/undefined"></a><a href="https://juejin.cn/post/6975282946638872584#chapter-two">二 前言</a></td></tr><tr><td><a name="user-content-catalog-chapter-three" id="user-content-catalog-chapter-three" href="https://juejin.cn/post/undefined"></a><a href="https://juejin.cn/post/6975282946638872584#chapter-three">三 Puppeteer</a></td></tr><tr><td> <a href="https://juejin.cn/post/6975282946638872584#chapter-three-one">3.1 抓取快照</a></td></tr><tr><td> <a href="https://juejin.cn/post/6975282946638872584#chapter-three-two">3.2 下载文件</a></td></tr><tr><td><a name="user-content-catalog-chapter-four" id="user-content-catalog-chapter-four" href="https://juejin.cn/post/undefined"></a><a href="https://juejin.cn/post/6975282946638872584#chapter-four">四 参考文献</a></td></tr><tr><td></td></tr></tbody></table>
<h2 data-id="heading-1"><a name="user-content-chapter-two" id="user-content-chapter-two" href="https://juejin.cn/post/undefined"></a>二 前言</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6975282946638872584#chapter-one">返回目录</a></p>
</blockquote>
<p>Puppeteer 是一个 Node 库，它提供了一个高级 API 来通过 DevTools 协议控制 Chromium 或 Chrome。</p>
<p>就跟它在 GitHub 简介中介绍的一样：你在浏览器中手动执行的绝大多数操作都可以使用 Puppeteer 来完成！</p>
<ul>
<li>抓取页面快照</li>
<li>生成页面 PDF</li>
<li>自动操作页面 DOM</li>
<li>……</li>
</ul>
<p>详细例子小伙伴可以翻看本文下方参考文献的 GitHub 或者中文文档，这里不一一举例（免得被吐槽复制 README.md）</p>
<h2 data-id="heading-2"><a name="user-content-chapter-three" id="user-content-chapter-three" href="https://juejin.cn/post/undefined"></a>三 Puppeteer</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6975282946638872584#chapter-one">返回目录</a></p>
</blockquote>
<ul>
<li>安装：<code>npm i puppeteer</code></li>
</ul>
<p>！<strong>jsliang</strong> 安装的时候报错：</p>
<ul>
<li><code>(node:7584) ExperimentalWarning: The fs.promises API is experimental</code></li>
</ul>
<p>我的 Node.js 版本是 <code>node@10.16.0</code>，所以需要升级 Node.js。</p>
<p>查了下资料有 2 种方法升级，一种是下载最新版覆盖安装，另一种是通过 <code>nvm/nvmw</code> 方式去管理。</p>
<p><strong>jsliang</strong> 网络还不错，直接下载个最新文档版吧：<a href="https://nodejs.org/zh-cn/" target="_blank" rel="nofollow noopener noreferrer">Node 官网</a></p>
<p>安装完毕后查看下最新版本：</p>
<ul>
<li><code>node -v</code>：<code>v14.17.1</code></li>
</ul>
<p>这时候再安装 Puppeteer，显示安装成功，<code>package.json</code> 显示：<code>"puppeteer": "^10.0.0"</code></p>
<blockquote>
<p>安装 Puppeteer 过程中可能会有各式各样的报错，考验小伙伴们网速的时候到了</p>
</blockquote>
<p>安装完毕，开始搞事~</p>
<h3 data-id="heading-3"><a name="user-content-chapter-three-one" id="user-content-chapter-three-one" href="https://juejin.cn/post/undefined"></a>3.1 抓取快照</h3>
<blockquote>
<p><a href="https://juejin.cn/post/6975282946638872584#chapter-one">返回目录</a></p>
</blockquote>
<p>我们拿抓取页面快照做个简单举例：</p>
<blockquote>
<p>src/index.ts</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> program <span class="hljs-keyword">from</span> <span class="hljs-string">'commander'</span>;
<span class="hljs-keyword">import</span> common <span class="hljs-keyword">from</span> <span class="hljs-string">'./common'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'./base/console'</span>;
<span class="hljs-keyword">import</span> puppeteer <span class="hljs-keyword">from</span> <span class="hljs-string">'puppeteer'</span>;

program
  .version(<span class="hljs-string">'0.0.1'</span>)
  .description(<span class="hljs-string">'工具库'</span>)

program
  .command(<span class="hljs-string">'jsliang'</span>)
  .description(<span class="hljs-string">'jsliang 帮助指令'</span>)
  .action(<span class="hljs-function">() =></span> &#123;
    common();
  &#125;);

program
  .command(<span class="hljs-string">'test'</span>)
  .description(<span class="hljs-string">'测试频道'</span>)
  .action(<span class="hljs-keyword">async</span> () => &#123;
    <span class="hljs-comment">// 启动浏览器</span>
    <span class="hljs-keyword">const</span> browser = <span class="hljs-keyword">await</span> puppeteer.launch(&#123;
      <span class="hljs-attr">headless</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 打开实体浏览器</span>
    &#125;);

    <span class="hljs-comment">// 创建新标签页并打开</span>
    <span class="hljs-keyword">const</span> page = <span class="hljs-keyword">await</span> browser.newPage();
    <span class="hljs-keyword">await</span> page.goto(<span class="hljs-string">'https://www.baidu.com/s?wd=jsliang'</span>);

    <span class="hljs-comment">// 获取快照并存储到本地</span>
    <span class="hljs-keyword">await</span> page.screenshot(&#123;
      <span class="hljs-attr">path</span>: <span class="hljs-string">'./src/baidu.png'</span>,
    &#125;);

    <span class="hljs-comment">// 关闭窗口</span>
    <span class="hljs-keyword">await</span> browser.close();
  &#125;);

program.parse(process.argv);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行完 <code>npm run test</code> 之后，<code>src</code> 文件夹里面会出现图片文件 <code>baidu.png</code>，打开展示如下：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d9bcecb002e4c8ebba51c90e12e5acc~tplv-k3u1fbpfcp-watermark.image" alt="puppeteer-01.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>实测 科学上网工具 或者 360 安全卫士会对这操作造成影响，为了防止你血压飙升，请确保这些软件的关闭</p>
</blockquote>
<p>这样我们就初步了解 Puppeteer 啦，当然它还可以导出 PDF 等，自行翻下文【参考文献】中的内容对 Puppeteer 进一步了解吧。</p>
<h3 data-id="heading-4"><a name="user-content-chapter-three-two" id="user-content-chapter-three-two" href="https://juejin.cn/post/undefined"></a>3.2 下载文件</h3>
<blockquote>
<p><a href="https://juejin.cn/post/6975282946638872584#chapter-one">返回目录</a></p>
</blockquote>
<p>既然我们可以获取到截图，那么我们能操作 DOM 也就不足为奇，咱们获取下线上的文件吧！</p>
<p>拿文档举例，咱们先创建一个 Excel 文件：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67e9c1d165ce4f79a3ea8465728ddb6c~tplv-k3u1fbpfcp-watermark.image" alt="puppeteer-02.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>创建方式可以自己去玩玩，就不做讲解了，文档地址：<code>https://www.kdocs.cn/</code></p>
<p>然后，我们下个环节就是需要将这个 Excel 下载下来（假设已经请人做好翻译工作了），就是这样的 Excel：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1eabe887407f4917a5ff67b654322819~tplv-k3u1fbpfcp-watermark.image" alt="puppeteer-03.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>该图片来源于网络，本次知识分享用以参考，侵权必删</p>
</blockquote>
<p>然后咱们搞个简单的吧：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c8d19571cd04972be9bbb0cbc86aea4~tplv-k3u1fbpfcp-watermark.image" alt="puppeteer-04.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>多语言咋样不重要，咱们目的是需要操作 Puppeteer 获取到这个 Excel 文件</p>
</blockquote>
<p>OK，文件有了，咱们怎样才能下载下来呢？现在情况是：</p>
<ul>
<li>试想一下如果我们通过 Puppeteer 打开，那是无头浏览器啊，跟无痕差不多了，如果正常登录的话，需要重新登录、进入链接，然后才是点击按钮，进行下载。</li>
</ul>
<p>所以，这里用到文档的免登录链接：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bd7804c3c9294041afbeb78bad124cd3~tplv-k3u1fbpfcp-watermark.image" alt="puppeteer-05.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>众所众知免登录就是不用登陆，虽然这个解释很弱智，但是我感觉很有必要……</p>
</blockquote>
<p>这里提供上面的 Demo 地址，小伙伴们可以拿来练习，但是不确保这个链接会不会哪天就被我删了，所以按照上面步骤自行设置一个吧！</p>
<ul>
<li>【文档 Excel 试用文件.xlsx】：<code>https://www.kdocs.cn/l/sdwvJUKBzkK2</code></li>
</ul>
<hr>
<p>OK，罗里吧嗦讲了那么多前置条件，下面咱们进入正题 —— 如何获取到线下文件：</p>
<ol>
<li>操作浏览器打开 <code>https://www.kdocs.cn/l/sdwvJUKBzkK2</code></li>
<li>睡眠 6.66s（确保浏览器打开链接并加载页面）</li>
<li>然后触发【更多菜单】按钮的点击</li>
<li>睡眠 2s（确保更多菜单按钮点击到）</li>
<li>设置下载路径（确保下载位置，要不然弹窗就不好处理）</li>
<li>最后触发【下载】按钮的点击</li>
<li>睡眠 10s（确保资源下载到）</li>
<li>关闭窗口</li>
</ol>
<p>上面唯一要关注的点是第 5 点，因为我们 Windows 点击下载是会有弹窗的（并不是默认下载），所以需要提前设置好下载路径（代码中会体现）。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1715e9bb242b4043b619ad0ba76e4a9a~tplv-k3u1fbpfcp-watermark.image" alt="puppeteer-06.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>那么，上代码！</p>
<blockquote>
<p>src/common/index.ts</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; inquirer &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../base/inquirer'</span>;
<span class="hljs-keyword">import</span> &#123; Result &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'../base/interface'</span>;
<span class="hljs-keyword">import</span> &#123; sortCatalog &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./sortCatalog'</span>;
<span class="hljs-keyword">import</span> &#123; downLoadExcel &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./downLoadExcel'</span>;

<span class="hljs-keyword">const</span> common = (): <span class="hljs-function"><span class="hljs-params">void</span> =></span> &#123;
  <span class="hljs-comment">// 问题路线：看 questionList.ts</span>
  <span class="hljs-keyword">const</span> questionList = [
    <span class="hljs-comment">// q0</span>
    &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'list'</span>,
      <span class="hljs-attr">message</span>: <span class="hljs-string">'请问需要什么服务？'</span>,
      <span class="hljs-attr">choices</span>: [<span class="hljs-string">'公共服务'</span>, <span class="hljs-string">'文件管理'</span>]
    &#125;,
    <span class="hljs-comment">// q1</span>
    &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'list'</span>,
      <span class="hljs-attr">message</span>: <span class="hljs-string">'当前公共服务有：'</span>,
      <span class="hljs-attr">choices</span>: [<span class="hljs-string">'文件排序'</span>]
    &#125;,
    <span class="hljs-comment">// q2</span>
    &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'input'</span>,
      <span class="hljs-attr">message</span>: <span class="hljs-string">'需要排序的文件夹为？（绝对路径）'</span>,
    &#125;,
    <span class="hljs-comment">// q3</span>
    &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'list'</span>,
      <span class="hljs-attr">message</span>: <span class="hljs-string">'请问需要什么支持？'</span>,
      <span class="hljs-attr">choices</span>: [<span class="hljs-string">'多语言'</span>, <span class="hljs-string">'Markdown 转 Word'</span>],
    &#125;,
    <span class="hljs-comment">// q4</span>
    &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'list'</span>,
      <span class="hljs-attr">message</span>: <span class="hljs-string">'请问需要什么支持？'</span>,
      <span class="hljs-attr">choices</span>: [
        <span class="hljs-string">'下载多语言资源'</span>,
        <span class="hljs-string">'导入多语言资源'</span>,
        <span class="hljs-string">'导出多语言资源'</span>,
      ],
    &#125;,
    <span class="hljs-comment">// q5</span>
    &#123;
      <span class="hljs-attr">type</span>: <span class="hljs-string">'input'</span>,
      <span class="hljs-attr">message</span>: <span class="hljs-string">'资源下载地址（HTTP）？'</span>,
      <span class="hljs-attr">default</span>: <span class="hljs-string">'https://www.kdocs.cn/l/sdwvJUKBzkK2'</span>,
    &#125;
  ];

  <span class="hljs-keyword">const</span> answerList = [
    <span class="hljs-comment">// q0</span>
    <span class="hljs-keyword">async</span> (result: Result, <span class="hljs-attr">questions</span>: any) => &#123;
      <span class="hljs-keyword">if</span> (result.answer === <span class="hljs-string">'公共服务'</span>) &#123;
        questions[<span class="hljs-number">1</span>]();
      &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (result.answer === <span class="hljs-string">'文件管理'</span>) &#123;
        questions[<span class="hljs-number">3</span>]();
      &#125;
    &#125;,
    <span class="hljs-comment">// q1</span>
    <span class="hljs-keyword">async</span> (result: Result, <span class="hljs-attr">questions</span>: any) => &#123;
      <span class="hljs-keyword">if</span> (result.answer === <span class="hljs-string">'文件排序'</span>) &#123;
        questions[<span class="hljs-number">2</span>]();
      &#125;
    &#125;,
    <span class="hljs-comment">// q2</span>
    <span class="hljs-keyword">async</span> (result: Result, <span class="hljs-attr">_questions</span>: any, <span class="hljs-attr">prompts</span>: any) => &#123;
      <span class="hljs-keyword">const</span> sortResult = <span class="hljs-keyword">await</span> sortCatalog(result.answer);
      <span class="hljs-keyword">if</span> (sortResult) &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'排序成功！'</span>);
        prompts.complete();
      &#125;
    &#125;,
    <span class="hljs-comment">// q3</span>
    <span class="hljs-keyword">async</span> (result: Result, <span class="hljs-attr">questions</span>: any) => &#123;
      <span class="hljs-keyword">if</span> (result.answer === <span class="hljs-string">'多语言'</span>) &#123;
        questions[<span class="hljs-number">4</span>]();
      &#125;
    &#125;,
    <span class="hljs-comment">// q4</span>
    <span class="hljs-keyword">async</span> (result: Result, <span class="hljs-attr">questions</span>: any) => &#123;
      <span class="hljs-keyword">if</span> (result.answer === <span class="hljs-string">'下载多语言资源'</span>) &#123;
        questions[<span class="hljs-number">5</span>]();
      &#125;
    &#125;,
    <span class="hljs-comment">// q5</span>
    <span class="hljs-keyword">async</span> (result: Result, <span class="hljs-attr">_questions</span>: any, <span class="hljs-attr">prompts</span>: any) => &#123;
      <span class="hljs-keyword">if</span> (result.answer) &#123;
        <span class="hljs-keyword">const</span> downloadResult = <span class="hljs-keyword">await</span> downLoadExcel(result.answer);
        <span class="hljs-keyword">if</span> (downloadResult) &#123;
          <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'下载成功！'</span>);
          prompts.complete();
        &#125;
      &#125;
    &#125;,
  ];

  inquirer(questionList, answerList);
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> common;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>看到上面的代码我后悔了，为啥 <code>Inquirer.ts</code> 被我改造的那么恶心，弄得 <strong>jsliang</strong> 还需要特地写个文件来表明问题序列然后才捋顺问题顺序：</p>
<blockquote>
<p>src/common/questionList.ts</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// common 板块的问题咨询路线</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> questionList = &#123;
  <span class="hljs-string">'公共服务'</span>: &#123; <span class="hljs-comment">// q0</span>
    <span class="hljs-string">'文件排序'</span>: &#123; <span class="hljs-comment">// q1</span>
      <span class="hljs-string">'需要排序的文件夹'</span>: <span class="hljs-string">'Work 工作'</span>, <span class="hljs-comment">// q2</span>
    &#125;,
  &#125;,
  <span class="hljs-string">'文件管理'</span>: &#123; <span class="hljs-comment">// q0</span>
    <span class="hljs-string">'多语言'</span>: &#123; <span class="hljs-comment">// q3</span>
      <span class="hljs-string">'下载多语言资源'</span>: &#123; <span class="hljs-comment">// q4</span>
        <span class="hljs-string">'下载地址'</span>: <span class="hljs-string">'Work 工作'</span>, <span class="hljs-comment">// q5</span>
      &#125;,
      <span class="hljs-string">'导入多语言资源'</span>: &#123; <span class="hljs-comment">// q4</span>
        <span class="hljs-string">'导入地址'</span>: <span class="hljs-string">'Work 工作'</span>,
      &#125;,
      <span class="hljs-string">'导出多语言资源'</span>: &#123; <span class="hljs-comment">// q4</span>
        <span class="hljs-string">'导出全量资源'</span>: <span class="hljs-string">'Work 工作'</span>,
        <span class="hljs-string">'导出单门资源'</span>: <span class="hljs-string">'Work 工作'</span>,
      &#125;
    &#125;,
    <span class="hljs-string">'Markdown 转 Word'</span>: <span class="hljs-string">'暂未支持'</span>, <span class="hljs-comment">// q3</span>
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>写完后转入写功能上：</p>
<blockquote>
<p>src/common/downLoadExcel.ts</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> puppeteer <span class="hljs-keyword">from</span> <span class="hljs-string">'puppeteer'</span>;
<span class="hljs-keyword">import</span> path <span class="hljs-keyword">from</span> <span class="hljs-string">'path'</span>;
<span class="hljs-keyword">import</span> fs <span class="hljs-keyword">from</span> <span class="hljs-string">'fs'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> downLoadExcel = <span class="hljs-keyword">async</span> (link: string): <span class="hljs-built_in">Promise</span><boolean> => &#123;
  <span class="hljs-comment">// 启动浏览器</span>
  <span class="hljs-keyword">const</span> browser = <span class="hljs-keyword">await</span> puppeteer.launch(&#123;
    <span class="hljs-attr">headless</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 打开实体浏览器</span>
    <span class="hljs-attr">devtools</span>: <span class="hljs-literal">true</span>, <span class="hljs-comment">// 打开开发模式</span>
  &#125;);

  <span class="hljs-comment">// 1. 创建新标签页并打开</span>
  <span class="hljs-keyword">const</span> page = <span class="hljs-keyword">await</span> browser.newPage();
  <span class="hljs-keyword">await</span> page.goto(link);

  <span class="hljs-comment">// 2. 睡眠 6.66s - 确保页面正常打开</span>
  <span class="hljs-keyword">await</span> page.waitForTimeout(<span class="hljs-number">6666</span>);

  <span class="hljs-comment">// 3. 触发【更多菜单】按钮的点击</span>
  <span class="hljs-keyword">const</span> moreBtn = <span class="hljs-keyword">await</span> page.$(<span class="hljs-string">'.header-more-btn'</span>);
  moreBtn?.click();

  <span class="hljs-comment">// 4. 睡眠 1s - 确保按钮点击到</span>
  <span class="hljs-keyword">await</span> page.waitForTimeout(<span class="hljs-number">2000</span>);

  <span class="hljs-comment">// 5. 设置下载路径</span>
  <span class="hljs-keyword">const</span> dist = path.join(__dirname, <span class="hljs-string">'./dist'</span>);
  <span class="hljs-keyword">if</span> (!fs.existsSync(dist)) &#123;
    fs.mkdirSync(dist);
  &#125;
  <span class="hljs-keyword">await</span> (page <span class="hljs-keyword">as</span> any)._client?.send(<span class="hljs-string">'Page.setDownloadBehavior'</span>, &#123;
    <span class="hljs-attr">behavior</span>: <span class="hljs-string">'allow'</span>,
    <span class="hljs-attr">downloadPath</span>: dist,
  &#125;);

  <span class="hljs-comment">// 6. 触发【下载】按钮的点击</span>
  <span class="hljs-keyword">const</span> elements = <span class="hljs-keyword">await</span> page.$$(<span class="hljs-string">'.header-menu-item'</span>);
  <span class="hljs-keyword">let</span> downloadBtn;
  <span class="hljs-keyword">if</span> (elements.length) &#123;
    downloadBtn = elements[<span class="hljs-number">8</span>];
  &#125;
  <span class="hljs-keyword">if</span> (!downloadBtn) &#123;
    <span class="hljs-built_in">console</span>.error(<span class="hljs-string">'没找到下载按钮'</span>);
    <span class="hljs-keyword">await</span> browser.close();
  &#125;
  <span class="hljs-keyword">await</span> downloadBtn?.click();

  <span class="hljs-comment">// 7. 睡眠 10s - 确保资源下载到</span>
  <span class="hljs-keyword">await</span> page.waitForTimeout(<span class="hljs-number">10000</span>);

  <span class="hljs-comment">// 8. 关闭窗口</span>
  <span class="hljs-keyword">await</span> browser.close();

  <span class="hljs-keyword">return</span> <span class="hljs-keyword">await</span> <span class="hljs-literal">true</span>;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样子运行之后，如果控制台不报错，那么 VS Code 展示为：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58614c6ac7e945cdaf0f6ca3abff9cda~tplv-k3u1fbpfcp-watermark.image" alt="puppeteer-07.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到 <code>common</code> 目录下的确有 <code>dist/Excel 试用文件.xlsx</code> 了，咱们就可以接入 <code>node-xlsx</code> 这个库来操作 Excel 啦~</p>
<p>下期见！</p>
<h2 data-id="heading-5"><a name="user-content-chapter-four" id="user-content-chapter-four" href="https://juejin.cn/post/undefined"></a>四 参考文献</h2>
<blockquote>
<p><a href="https://juejin.cn/post/6975282946638872584#chapter-one">返回目录</a></p>
</blockquote>
<ul>
<li><a href="https://github.com/puppeteer/puppeteer" target="_blank" rel="nofollow noopener noreferrer">Github: Puppeteer</a></li>
<li><a href="https://zhaoqize.github.io/puppeteer-api-zh_CN/" target="_blank" rel="nofollow noopener noreferrer">Puppeteer</a></li>
<li><a href="https://www.cnblogs.com/mingme/p/14013325.html" target="_blank" rel="nofollow noopener noreferrer">puppeteer 前端利器</a></li>
<li><a href="https://blog.fundebug.com/2017/11/01/guide-to-automating-scraping-the-web-with-js/" target="_blank" rel="nofollow noopener noreferrer">Puppeteer 之爬虫入门</a></li>
</ul>
<hr>
<blockquote>
<p>jsliang 的文档库由 <a href="https://github.com/LiangJunrong" target="_blank" rel="nofollow noopener noreferrer">梁峻荣</a> 采用 <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/" target="_blank" rel="nofollow noopener noreferrer">知识共享 署名-非商业性使用-相同方式共享 4.0 国际 许可协议</a> 进行许可。<br>基于 <a href="https://github.com/LiangJunrong/document-library" target="_blank" rel="nofollow noopener noreferrer">github.com/LiangJunron…</a> 上的作品创作。<br>本许可协议授权之外的使用权限可以从 <a href="https://creativecommons.org/licenses/by-nc-sa/2.5/cn/" target="_blank" rel="nofollow noopener noreferrer">creativecommons.org/licenses/by…</a> 处获得。</p>
</blockquote></div>  
</div>
            