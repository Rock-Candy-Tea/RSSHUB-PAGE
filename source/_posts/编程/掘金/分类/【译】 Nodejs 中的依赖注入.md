
---
title: '【译】 Node.js 中的依赖注入'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0708d72caaad43ab94680d5aa97ffc63~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 13 Jun 2021 23:53:02 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0708d72caaad43ab94680d5aa97ffc63~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0"><a name="user-content-start" href="https://juejin.cn/post/undefined"></a> 引子</h2>
<p>在 <a href="https://github.com/XXHolic/blog/issues/89" target="_blank" rel="nofollow noopener noreferrer">Dependency Injection</a> 中了解了相关概念，接下来看看在 Node 中如何使用依赖注入。</p>
<p>原文：<a href="https://blog.risingstack.com/dependency-injection-in-node-js/" target="_blank" rel="nofollow noopener noreferrer">Dependency Injection in Node.js</a></p>
<ul>
<li><a href="https://github.com/XXHolic/blog/issues/js" target="_blank" rel="nofollow noopener noreferrer">Origin</a></li>
<li><a href="https://github.com/XXHolic" target="_blank" rel="nofollow noopener noreferrer">My GitHub</a></li>
</ul>
<h2 data-id="heading-1"><a name="user-content-main" href="https://juejin.cn/post/undefined"></a> 正文</h2>
<p>依赖注入是一种软件设计模式，其中一个或多个依赖项（或服务）被注入或通过引用传递到依赖对象中。</p>
<h2 data-id="heading-2"><a name="user-content-reason" href="https://juejin.cn/post/undefined"></a> 使用依赖注入的理由</h2>
<h3 data-id="heading-3">解耦</h3>
<p>依赖注入使你的模块耦合性降低，从而产生更易于维护的代码库。</p>
<h3 data-id="heading-4">便于单元测试</h3>
<p>你可以将它们传递到你想要使用的模块中，而不是使用硬编码的依赖项。在大多数情况下，你不必使用 <a href="https://www.npmjs.com/package/proxyquire" target="_blank" rel="nofollow noopener noreferrer">proxyquire</a> 这样的模块。</p>
<h3 data-id="heading-5">快速开发</h3>
<p>使用依赖注入，定义接口之后，就可以轻松地工作，不会出现任何合并冲突。</p>
<h2 data-id="heading-6"><a name="user-content-node" href="https://juejin.cn/post/undefined"></a> 如何使用 Node.js 依赖注入</h2>
<p>首先，让我们看看如何在不使用依赖注入的情况下编写你的应用程序，以及如何转换它。</p>
<h3 data-id="heading-7">没有使用依赖注入示例模块</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// team.js</span>
<span class="hljs-keyword">var</span> User = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./user'</span>);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getTeam</span>(<span class="hljs-params">teamId</span>) </span>&#123;
  <span class="hljs-keyword">return</span> User.find(&#123;<span class="hljs-attr">teamId</span>: teamId&#125;);
&#125;

<span class="hljs-built_in">module</span>.exports.getTeam = getTeam;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>一个简单的测试如下所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// team.spec.js</span>
<span class="hljs-keyword">var</span> Team = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./team'</span>);
<span class="hljs-keyword">var</span> User = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./user'</span>);

describe(<span class="hljs-string">'Team'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  it(<span class="hljs-string">'#getTeam'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>* (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> users = [&#123;<span class="hljs-attr">id</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">id</span>: <span class="hljs-number">2</span>&#125;];

    <span class="hljs-built_in">this</span>.sandbox.stub(User, <span class="hljs-string">'find'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
      <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve(users);
    &#125;);

    <span class="hljs-keyword">var</span> team = <span class="hljs-keyword">yield</span> team.getTeam();

    expect(team).to.eql(users);
  &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们在这里所做的是创建了一个名为 <code>team.js</code> 的文件，它可以返回属于单个团队的用户列表。为此，我们需要 <code>User</code> 模型，因此我们可以调用它的 <code>find</code> 方法，该方法返回一个用户列表。</p>
<p>看起来不错，对吧？但在测试时，我们必须要使用测试存根。</p>
<p>在测试文件中，我们还需要 <code>require</code> <code>User</code> 模型，这样就可以存根它的 <code>find</code> 方法。请注意，我们在这里使用的是沙盒特性，因此不必在测试运行后手动恢复原始函数。</p>
<h3 data-id="heading-8">使用依赖注入示例模块</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// team.js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Team</span>(<span class="hljs-params">options</span>) </span>&#123;
  <span class="hljs-built_in">this</span>.options = options;
&#125;

Team.prototype.getTeam = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">teamId</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.options.User.find(&#123;<span class="hljs-attr">teamId</span>: teamId&#125;)
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">create</span>(<span class="hljs-params">options</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Team(options);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>你可以使用以下测试用例测试此文件：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// team.spec.js</span>
<span class="hljs-keyword">var</span> Team = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./team'</span>);

describe(<span class="hljs-string">'Team'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
  it(<span class="hljs-string">'#getTeam'</span>, <span class="hljs-function"><span class="hljs-keyword">function</span>* (<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> users = [&#123;<span class="hljs-attr">id</span>: <span class="hljs-number">1</span>, <span class="hljs-attr">id</span>: <span class="hljs-number">2</span>&#125;];

    <span class="hljs-keyword">var</span> fakeUser = &#123;
      <span class="hljs-attr">find</span>: <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Promise</span>.resolve(users);
      &#125;
    &#125;;

    <span class="hljs-keyword">var</span> team = Team.create(&#123;
      <span class="hljs-attr">User</span>: fakeUser
    &#125;);

    <span class="hljs-keyword">var</span> team = <span class="hljs-keyword">yield</span> team.getTeam();

    expect(team).to.eql(users);
  &#125;);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好的，那么依赖注入的版本和上一个版本有何不同呢？你可以注意到的第一件事是<strong>工厂模式</strong>的使用：我们使用它向新创建的对象注入选项/依赖项—这是我们可以注入 <code>User</code> 模型的地方。</p>
<p>在测试文件中，我们必须创建一个表示 <code>User</code> 模型的<strong>假模型</strong>，然后我们只需通过将其传递给 <code>Team</code> 模型的 <code>create</code> 函数来注入这个模型。很简单，对吧？</p>
<h2 data-id="heading-9"><a name="user-content-project" href="https://juejin.cn/post/undefined"></a> 在实际项目中的依赖注入</h2>
<p>你可以在很多开源项目中找到依赖注入的例子。例如，你在日常工作中使用的大多数 Express/Koa 中间件都使用相同的方法。</p>
<h3 data-id="heading-10">Express 中间件</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> express = <span class="hljs-built_in">require</span>(<span class="hljs-string">'express'</span>);
<span class="hljs-keyword">var</span> app = express();
<span class="hljs-keyword">var</span> session = <span class="hljs-built_in">require</span>(<span class="hljs-string">'express-session'</span>);

app.use(session(&#123;
  <span class="hljs-attr">store</span>: <span class="hljs-built_in">require</span>(<span class="hljs-string">'connect-session-knex'</span>)()
&#125;));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码片段使用工厂模式的依赖注入：向 session 中间件传递 <code>connect-session-knex</code> 模块-它必须实现一个接口，<code>session</code> 模块将调用该接口。</p>
<p>在这个示例中，<code>connect-session-knex</code> 模块必须实现以下方法：</p>
<ul>
<li><code>store.destroy(sid, callback)</code></li>
<li><code>store.get(sid, callback)</code></li>
<li><code>store.set(sid, session, callback)</code></li>
</ul>
<h3 data-id="heading-11">Hapi 插件</h3>
<p>同样的概念也可以在 Hapi 中找到-下面的示例将 <code>handlebars</code> 模块作为视图引擎注入 Hapi 中使用。</p>
<pre><code class="hljs language-js copyable" lang="js">server.views(&#123;
  <span class="hljs-attr">engines</span>: &#123;
    <span class="hljs-attr">html</span>: <span class="hljs-built_in">require</span>(<span class="hljs-string">'handlebars'</span>)
  &#125;,
  <span class="hljs-attr">relativeTo</span>: __dirname,
  <span class="hljs-attr">path</span>: <span class="hljs-string">'templates'</span>
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12"><a name="user-content-reference" href="https://juejin.cn/post/undefined"></a> 参考资料</h2>
<ul>
<li><a href="https://blog.risingstack.com/dependency-injection-in-node-js/" target="_blank" rel="nofollow noopener noreferrer">Dependency Injection in Node.js</a></li>
</ul>
<details>
<summary>wastebasket</summary>
<p>最近在断断续续的看<a href="https://movie.douban.com/subject/11577091/" target="_blank" rel="nofollow noopener noreferrer">《浴血黑帮》</a>，这让我想起很早之前看的黑帮剧集<a href="https://movie.douban.com/subject/1760516/" target="_blank" rel="nofollow noopener noreferrer">《黑道家族》</a>，风格很不一样。</p>
<p>一小部分人利用各种手段，拥有这么大的权势，法律什么的似乎形同虚设。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0708d72caaad43ab94680d5aa97ffc63~tplv-k3u1fbpfcp-zoom-1.image" alt="85-poster" loading="lazy" referrerpolicy="no-referrer"></p>
</details></div>  
</div>
            