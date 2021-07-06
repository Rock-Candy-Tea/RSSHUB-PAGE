
---
title: 'Flutter x GraphQL'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/033d41cbb9294f3ab25bcaa4d35d7223~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 04 Jul 2021 23:18:42 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/033d41cbb9294f3ab25bcaa4d35d7223~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Flutter x GraphQL</h1>
<p><a href="https://dubydu.medium.com/?source=post_page-----a2dea05e6564--------------------------------" target="_blank" rel="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/033d41cbb9294f3ab25bcaa4d35d7223~tplv-k3u1fbpfcp-zoom-1.image" alt="DUBV" loading="lazy" referrerpolicy="no-referrer"></a></p>
<p><a href="https://dubydu.medium.com/?source=post_page-----a2dea05e6564--------------------------------" target="_blank" rel="nofollow noopener noreferrer">DUBV</a></p>
<p><a href="https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F4e439eaff2d3&operation=register&redirect=https%3A%2F%2Fitnext.io%2Fflutter-x-graphql-a2dea05e6564&user=DUBV&userId=4e439eaff2d3&source=post_page-4e439eaff2d3----a2dea05e6564---------------------follow_byline-----------" target="_blank" rel="nofollow noopener noreferrer">遵循</a></p>
<p><a href="https://itnext.io/flutter-x-graphql-a2dea05e6564?source=post_page-----a2dea05e6564--------------------------------" target="_blank" rel="nofollow noopener noreferrer">7月1日</a></p>
<p>- 4分钟阅读</p>
<p><a href="https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fa2dea05e6564&operation=register&redirect=https%3A%2F%2Fitnext.io%2Fflutter-x-graphql-a2dea05e6564&source=post_actions_header--------------------------bookmark_preview-----------" target="_blank" rel="nofollow noopener noreferrer"></a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/573d2e37240e401e9fc8d56ef4db2da5~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>作为一个前端开发员，我已经在很多使用<strong>REST API</strong>的项目上工作了很长时间，在与REST交互时，我注意到了一些低效率的问题。</p>
<ul>
<li>源代码中有很多端点，我需要处理这些端点。</li>
<li>即使我只想在我的<strong>用户界面</strong>上显示一个字段，但服务器可能会向我提供更多不必要的数据。</li>
<li>要花很多时间与后端团队沟通以澄清API文件。</li>
<li>请求对象的结构（前端方面）必须依赖于服务器方面。</li>
</ul>
<p>你是否曾经因为上述原因而浪费了大量的时间？好吧，如果你的回答是 "<strong>是</strong>"，那么GraphQL将为你节省时间。</p>
<h2 data-id="heading-1"><strong>那么，GraphQL究竟是什么？</strong></h2>
<blockquote>
<p>GraphQL是一种查询语言和应用程序接口（API）的服务器端运行时间，它优先为客户提供他们所要求的数据，而不是更多。</p>
<p>GraphQL旨在使API快速、灵活和对开发者友好。它甚至可以部署在一个被称为GraphiQL的集成开发环境（IDE）中。作为REST的替代方案，GraphQL让开发者构建请求，在一次API调用中从多个数据源中提取数据。</p>
<p>-<a href="http://redhat.com/" target="_blank" rel="nofollow noopener noreferrer">Redhat.com</a></p>
</blockquote>
<p>当你读到上面的定义时，我相信你会想到SQL（结构化查询语言），并回忆起大一的时候的 "传奇 "术语，如<strong>SELECT</strong>、<strong>INSERT</strong>、<strong>UPDATE</strong>、<strong>DELETE</strong> 和<strong>WHERE</strong>。</p>
<p>之后，这个定义让你想起了REST，我肯定你会想到另一个传奇的术语。<strong>C.R.U.D</strong>，对吗？</p>
<p>现在，如果我们得到的东西结合了所有这些传奇的流行语呢？是的，拯救我时间的人诞生了**--GraphQL。**</p>
<p>在本文的范围内，我们将从前端的角度开始介绍GraphQL的基本概念。</p>
<h1 data-id="heading-2"><strong>GraphQL操作</strong></h1>
<p>有三种主要的GraphQL操作类型。<strong>查询、突变、订阅。</strong></p>
<blockquote>
<p>让我们假设我们的模式中有一个模型<code>ticket</code> ，这个模型包含三个字段。<code>id, status, created_at</code></p>
</blockquote>
<h2 data-id="heading-3"><strong>查询（一个只读的取数</strong></h2>
<p><strong>1.取出多个条目</strong></p>
<p><strong>2.获取一个单独的条目</strong></p>
<h2 data-id="heading-4"><strong>变更（修改后再取）。</strong></h2>
<p><strong>1.增加一个单项</strong></p>
<p><strong>2.更新一个条目</strong></p>
<p><strong>3.删除一个条目</strong></p>
<h2 data-id="heading-5"><strong>订阅（一个实时数据的查询</strong></h2>
<h1 data-id="heading-6"><strong>现在，让我们把它应用于Flutter</strong></h1>
<p>首先，为了使用GraphQL，你需要一个服务器库（除非你有一个坚实的后台团队）。有很多支持的服务器库，但我衷心地建议你使用<a href="https://graphcms.com/" target="_blank" rel="nofollow noopener noreferrer">GraphCMS</a>。</p>
<p>其次，为了让你的Flutter项目能够使用GraphQL，你需要一个GraphQL客户端，以便与服务器进行通信，在<a href="https://pub.dev/" target="_blank" rel="nofollow noopener noreferrer">pub.dev</a>上有一些很棒的库，比如这个<a href="https://pub.dev/packages/graphql_flutter" target="_blank" rel="nofollow noopener noreferrer">graphql_flutter</a>和这个<a href="https://pub.dev/packages/ferry" target="_blank" rel="nofollow noopener noreferrer">渡口</a>。</p>
<h2 data-id="heading-7"><strong>编码时间!</strong></h2>
<p>以下所有的脚本和相关的东西都可以在这个 repo 中找到：<a href="https://github.com/dubydu/fluttour" target="_blank" rel="nofollow noopener noreferrer">fluttour</a>）。<strong>在你开始之前，请看一下README。</strong></p>
<p>下面是我们要做的事情。</p>
<ol>
<li>创建一个基本的GraphQLAPIClient。</li>
<li>创建一个异步函数，包含我们希望在扩展自GraphQLAPIClient的类中执行的_突变/查询/订阅_ 文件。然后，处理异常并从响应中解析数据。</li>
<li>在我们的提供者类中创建另一个异步函数，该类扩展自<strong>ChangeNotifier</strong>，调用步骤2的函数并开始数据处理。</li>
<li>通知监听器，来自服务器的数据可能已经改变。</li>
</ol>
<h2 data-id="heading-8"><strong>创建一个基本的GraphQLAPIClient</strong></h2>
<pre><code class="copyable">> api_client.dart
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这里，我们创建了一个私有的**_client**函数，返回一个GraphQLClient构造函数</p>
<ul>
<li><strong>cache。</strong> 要在数据存储中使用的初始缓存。</li>
<li><strong>链接。</strong> GraphQL文件将被解析成一个响应的链接。在这种情况下，我们使用的是<strong>HttpLink</strong>，我们将把它与 <a href="https://github.com/dubydu/fluttour/blob/6a2ed6f521665a2feaa3dae322807e4a9801cf22/lib/data/api/api_client.dart#L11" target="_blank" rel="nofollow noopener noreferrer"><strong>AuthLink</strong></a> ，以附加我们的<strong>GraphCMS</strong>公共标记。</li>
<li><strong>defaultPolicies。</strong> 为每个客户端动作设置的默认策略。</li>
</ul>
<p>之后，我们创建一个 <a href="https://github.com/dubydu/fluttour/blob/cd10d0f9cbc564645a26c1a7e5256a458ddd4e85/lib/data/api/api_client.dart#L37" target="_blank" rel="nofollow noopener noreferrer"><strong><em>查询</em></strong></a>函数来执行我们的查询。</p>
<pre><code class="copyable">Future<QueryResult> query(String queries) async &#123;  final WatchQueryOptions _options = WatchQueryOptions(    document: gql(queries),    pollInterval: Duration(seconds: 15),    fetchResults: true,  );  return await _client().query(_options);&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在我们创建一个 <a href="https://github.com/dubydu/fluttour/blob/cd10d0f9cbc564645a26c1a7e5256a458ddd4e85/lib/data/api/api_client.dart#L47" target="_blank" rel="nofollow noopener noreferrer"><strong><em>突变</em></strong></a>函数，将突变结果发送到服务器上。</p>
<pre><code class="copyable">Future<QueryResult> mutation(String queries) async &#123;  final MutationOptions _options = MutationOptions(    document: gql(queries),  );  return await _client().mutate(_options);&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>很酷吧？</p>
<h2 data-id="heading-9">创建一个请求</h2>
<p>在扩展自GraphQLAPIClient的类里面，我们创建一个请求函数，将<code>mutate/query/subscription</code> 到服务器。</p>
<pre><code class="copyable">Future<T> get() async &#123;  String your_query= """    query &#123;          /// write your query      &#125;  """;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于 <strong><em>突变</em></strong>，你所要做的就是把<code>this.query</code> 改为<code>this.mutation</code></p>
<h2 data-id="heading-10">在你的提供者类里面进行数据处理/通知监听器</h2>
<pre><code class="copyable">Future<void> get() async &#123;  final result = await this._request.get();  if (result != null) &#123; &#125; else &#123; &#125;  // handle data & notify the listeners here.  // there are a bunch of ways to notify the listeners,   // in this example, I'm using the delegation pattern and  // notifyListeners function.
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-11">陷阱</h1>
<p>1.为了运行这个项目，你需要在一个特定的环境下运行。</p>
<ul>
<li>开发。<code>flutter run -t lib/main_dev.dart</code></li>
<li>生产环境。<code>flutter run -t lib/main_prod.dart</code></li>
</ul>
<p>2.你需要一个个人访问令牌来验证GraphCMS服务器。要获得一个，请到<a href="https://graphcms.com/docs/authorization" target="_blank" rel="nofollow noopener noreferrer">graphcms.com/docs/author…</a>。</p>
<p>如果你不想浪费你的时间，你可以使用我的令牌，它可以在这个<a href="https://github.com/dubydu/fluttour" target="_blank" rel="nofollow noopener noreferrer">repo</a>中找到。</p>
<p><strong>最后</strong>，享受你的工作，看看GraphQL是多么的不可思议。</p>
<blockquote>
<p>这是我的第一篇文章，希望它对那些刚接触GraphQL和Flutter的人有用。🍻</p>
</blockquote></div>  
</div>
            