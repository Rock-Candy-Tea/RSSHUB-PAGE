
---
title: 'graphql + apollo client + docker使用姿势'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6330'
author: 掘金
comments: false
date: Wed, 01 Sep 2021 20:28:50 GMT
thumbnail: 'https://picsum.photos/400/300?random=6330'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">为什么要学习graphl</h1>
<blockquote>
<p>文档地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgraphql.bootcss.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://graphql.bootcss.com/" ref="nofollow noopener noreferrer">graphql.bootcss.com/</a> 一种用于 <code>API 的查询语言</code></p>
</blockquote>
<p>使用graphql的优点</p>
<ul>
<li>接口聚合</li>
<li>字段按需加载，减少网络请求</li>
<li>和apollo结合，缓存数据，关注数据的使用而不是获取</li>
<li>技多不压身，提高职场竞争力，目前很多大公司都开始使用graphql当作<code>bff</code></li>
</ul>
<h1 data-id="heading-1">使用Apollo Server构建一个graphql服务</h1>
<blockquote>
<p>文档地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.apollographql.com%2Fdocs%2Fapollo-server%2Fgetting-started%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.apollographql.com/docs/apollo-server/getting-started/" ref="nofollow noopener noreferrer">www.apollographql.com/docs/apollo…</a></p>
</blockquote>
<p>step1，创建项目</p>
<pre><code class="copyable">mkdir graphql-server-example
cd graphql-server-example
npm init -y`
<span class="copy-code-btn">复制代码</span></code></pre>
<p>step2安装依赖</p>
<pre><code class="copyable">npm install apollo-server graphql
touch index.js
<span class="copy-code-btn">复制代码</span></code></pre>
<p>step3定义graphql schema</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> &#123; ApolloServer, gql &#125; = <span class="hljs-built_in">require</span>(<span class="hljs-string">'apollo-server'</span>);
<span class="hljs-keyword">const</span> typeDefs = gql<span class="hljs-string">`
  type Book &#123;
    title: String
    author: String
  &#125;

  type Query &#123;
    books: [Book]
  &#125;
`</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>step4定义解析函数</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> books =  &#123;
    <span class="hljs-attr">title</span>: <span class="hljs-string">'The Awakening'</span>,
    <span class="hljs-attr">author</span>: <span class="hljs-string">'Kate Chopin'</span>,
  &#125;,
  &#123;
    <span class="hljs-attr">title</span>: <span class="hljs-string">'City of Glass'</span>,
    <span class="hljs-attr">author</span>: <span class="hljs-string">'Paul Auster'</span>,
  &#125;,
];
<span class="hljs-keyword">const</span> resolvers = &#123;
  <span class="hljs-attr">Query</span>: &#123;
    <span class="hljs-attr">books</span>: <span class="hljs-function">() =></span> books,
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>step5初始化apolo server</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> server = <span class="hljs-keyword">new</span> ApolloServer(&#123; typeDefs, resolvers &#125;);

<span class="hljs-comment">// The `listen` method launches a web server.</span>
server.listen().then(<span class="hljs-function">(<span class="hljs-params">&#123; url &#125;</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`🚀  Server ready at <span class="hljs-subst">$&#123;url&#125;</span>`</span>);
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>step6启动服务</p>
<pre><code class="copyable">node index.js
🚀 Server ready at http://localhost:4000/
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-2">使用@apollo/client构建一个graphql客户端</h1>
<blockquote>
<p>官方文档：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.apollographql.com%2Fdocs%2Freact%2Fget-started%2F%25EF%25BC%258C%25E5%2585%25B7%25E4%25BD%2593%25E6%25AD%25A5%25E9%25AA%25A4%25E5%258F%25AF%25E4%25BB%25A5%25E6%259F%25A5%25E8%25AF%25A2%25E6%25AD%25A4%25E6%2596%2587%25E6%25A1%25A3" target="_blank" rel="nofollow noopener noreferrer" title="https://www.apollographql.com/docs/react/get-started/%EF%BC%8C%E5%85%B7%E4%BD%93%E6%AD%A5%E9%AA%A4%E5%8F%AF%E4%BB%A5%E6%9F%A5%E8%AF%A2%E6%AD%A4%E6%96%87%E6%A1%A3" ref="nofollow noopener noreferrer">www.apollographql.com/docs/react/…</a></p>
</blockquote>
<h1 data-id="heading-3">在nextjs中使用graphql和apollo（推荐）</h1>
<pre><code class="hljs language-bash copyable" lang="bash">git <span class="hljs-built_in">clone</span> https://github.com/vercel/next.js.git
<span class="hljs-built_in">cd</span> next.js/examples/api-routes-apollo-server-and-client
npm i
npm run build
npm run start
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">使用graphql查询数据</h1>
<p>为了了解apollo client中的数据缓存更新策略，让我们稍微修改下源码，<code>去掉user中的id字段</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 在apollo下的typedef.js中定义User和User</span>
<span class="hljs-keyword">import</span> &#123; gql &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@apollo/client'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> typeDefs = gql<span class="hljs-string">`
  type User &#123;
    name: String!
    status: String!
  &#125;

  type Query &#123;
    viewer: User
  &#125;
`</span>

<span class="hljs-comment">// 在apollo下的resolvers.js定义对应执行的方法</span>

<span class="hljs-keyword">let</span> user = &#123; <span class="hljs-attr">name</span>: <span class="hljs-string">'John Smith'</span>, <span class="hljs-attr">status</span>: <span class="hljs-string">'cached'</span> &#125;
<span class="hljs-keyword">const</span> resolvers = &#123;
  <span class="hljs-attr">Query</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">viewer</span>(<span class="hljs-params">_parent, _args, _context, _info</span>)</span> &#123;
      <span class="hljs-keyword">return</span> user
    &#125;,
  &#125;,
&#125;

<span class="hljs-comment">// 定义schema</span>
<span class="hljs-keyword">import</span> &#123; typeDefs &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./type-defs'</span>
<span class="hljs-keyword">import</span> &#123; resolvers &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./resolvers'</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> schema = makeExecutableSchema(&#123;
  typeDefs,
  resolvers,
&#125;)

<span class="hljs-comment">// 在前端页面调用</span>
<span class="hljs-keyword">import</span> &#123; gql, useQuery &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@apollo/client'</span>;
<span class="hljs-keyword">const</span> ViewerQuery = gql<span class="hljs-string">`
  query ViewerQuery &#123;
    viewer &#123;
      name
      status
    &#125;
  &#125;
`</span>

<span class="hljs-keyword">const</span> Index = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> &#123;
    <span class="hljs-attr">data</span>: &#123; viewer &#125;,
  &#125; = useQuery(ViewerQuery)

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
      You're signed in as &#123;viewer.name&#125; and you're &#123;viewer.status&#125; goto&#123;' '&#125;
      <span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"/about"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">a</span>></span>static<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">Link</span>></span>&#123;' '&#125;
      page.
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>apollo在请求完成graphql数据时，通过内部集成redux，会将数据保存在apollo客户端中。当请求相同的graphql服务时，会优先使用缓存的数据，当然你可以使用不同的cache策略来修改这一行为。文档链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.apollographql.com%2Fdocs%2Freact%2Fdata%2Fqueries%2F%23supported-fetch-policies" target="_blank" rel="nofollow noopener noreferrer" title="https://www.apollographql.com/docs/react/data/queries/#supported-fetch-policies" ref="nofollow noopener noreferrer">www.apollographql.com/docs/react/…</a></p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 总是使用网络请求返回的数据</span>
<span class="hljs-keyword">const</span> &#123; loading, error, data &#125; = useQuery(ViewerQuery, &#123;
  <span class="hljs-attr">fetchPolicy</span>: <span class="hljs-string">"network-only"</span> <span class="hljs-comment">// Doesn't check cache before making a network request</span>
&#125;);
fetchPolicy: <span class="hljs-string">"network-only"</span>,   <span class="hljs-comment">// Used for first execution</span>
<span class="hljs-attr">nextFetchPolicy</span>: <span class="hljs-string">"cache-first"</span> <span class="hljs-comment">// Used for subsequent executions</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-5">使用mutation修改数据</h1>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 在apollo/type-defs.js中增加type</span>
type Mutation &#123;
    modifyUser(newname: <span class="hljs-built_in">String</span>): User
&#125;

<span class="hljs-comment">// 在apollo/resolver.js中增加对modifyUser的解析函数</span>
<span class="hljs-keyword">const</span> resolvers = &#123;
  ....
  <span class="hljs-attr">Mutation</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">modifyUser</span>(<span class="hljs-params">_parent, _args, _context, _info</span>)</span> &#123;
      user.name = _args.newname
      <span class="hljs-keyword">return</span> user
    &#125;,
  &#125;
&#125;

<span class="hljs-comment">// 在页面中调用</span>
<span class="hljs-keyword">const</span> MODIFY_USERS = gql<span class="hljs-string">`
  mutation modifyUser($newname: String) &#123;
    modifyUser(newname: $newname) &#123;
      name
      status
    &#125;
  &#125;
`</span>; 
<span class="hljs-keyword">const</span> Index = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-keyword">const</span> &#123;
    <span class="hljs-attr">data</span>: &#123; viewer &#125;,
  &#125; = useQuery(ViewerQuery)
    <span class="hljs-keyword">const</span> [modifyUser] = useMutation(MODIFY_USERS);
    <span class="hljs-keyword">const</span> onClick = <span class="hljs-function">() =></span> &#123;
        modifyUser(&#123;
        <span class="hljs-attr">variables</span>: &#123;
            <span class="hljs-attr">newname</span>: <span class="hljs-string">'Foo Bar'</span>,
        &#125;,
        &#125;).catch(<span class="hljs-function">(<span class="hljs-params">err</span>) =></span> &#123;
            <span class="hljs-built_in">console</span>.log(err)
        &#125;)
    &#125;
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;onClick&#125;</span>></span>修改用户<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            You're signed in as &#123;viewer.name&#125; and you're &#123;viewer.status&#125; goto&#123;' '&#125;
            <span class="hljs-tag"><<span class="hljs-name">Link</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"/about"</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">a</span>></span>static<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">Link</span>></span>&#123;' '&#125;
            page.
        <span class="hljs-tag"></></span></span>
    ) 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>点击修改数据按钮，打开页面的<code>network</code>发现，发现前端向<code>graphql服务端</code>发送了一条graphql的网络请求，修改了服务端数据，<code>但是前端页面的展示没有变化</code>，这是因为graphql并不会<code>主动修改当前客户端的数据</code>，如果想要在更新服务端数据的同时也更新前端数据要怎么办呢？</p>
</blockquote>
<h2 data-id="heading-6">声明式通过<code>__typename和id</code>自动更新</h2>
<p>apollo内部通过<code>__typename:id</code>生成唯一的<code>key</code>来保存数据，当接口返回的数据存同时存在<code>__typename和id</code>时，apollo将自动合并接口的数据到客户端的缓存数据中去，并保留其他现有字段。
在前端创建<code>ApolloClient</code>时，apollo通过<code>addTypename</code>字段为<code>每个对象</code>都创建一个<code>__typename</code>,详细文档：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.apollographql.com%2Fdocs%2Freact%2Fcaching%2Fcache-configuration%2F%23addtypename" target="_blank" rel="nofollow noopener noreferrer" title="https://www.apollographql.com/docs/react/caching/cache-configuration/#addtypename" ref="nofollow noopener noreferrer">addtypename</a>，所以我们想自动更新数据当前用户的姓名就要做两件事情</p>
<ol>
<li>返回的数据包含更新后的姓名（完成）</li>
<li>为需要更新的对象生成唯一id
<ul>
<li>可以在代码中硬编码，为每个user<code>生成唯一的id</code>，比如在graphql服务端拿到数据时，执行</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">  user.id = <span class="hljs-number">1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>通过<code>defaultDataIdFromObject</code>函数，为每个对象生成<code>唯一的id</code>并返回，文档地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.apollographql.com%2Fdocs%2Freact%2Fcaching%2Fcache-configuration%2F%23customizing-identifier-generation-globally" target="_blank" rel="nofollow noopener noreferrer" title="https://www.apollographql.com/docs/react/caching/cache-configuration/#customizing-identifier-generation-globally" ref="nofollow noopener noreferrer">defaultDataIdFromObject</a><code>defaultDataIdFromObject</code>函数生成唯一id</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">     <span class="hljs-keyword">import</span> &#123; defaultDataIdFromObject &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@apollo/client'</span>;

     <span class="hljs-keyword">const</span> cache = <span class="hljs-keyword">new</span> InMemoryCache(&#123;
       <span class="hljs-function"><span class="hljs-title">dataIdFromObject</span>(<span class="hljs-params">responseObject</span>)</span> &#123;
         <span class="hljs-keyword">switch</span> (responseObject.__typename) &#123;
           <span class="hljs-keyword">case</span> <span class="hljs-string">'viewer'</span>: <span class="hljs-keyword">return</span> <span class="hljs-string">`User:<span class="hljs-subst">$&#123;responseObject.name&#125;</span>`</span>;
           <span class="hljs-keyword">default</span>: <span class="hljs-keyword">return</span> defaultDataIdFromObject(responseObject);
         &#125;
       &#125;
     &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>通过<code>typePolicies</code>自动生成<code>id</code>文档地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.apollographql.com%2Fdocs%2Freact%2Fcaching%2Fcache-configuration%2F%23customizing-cache-ids" target="_blank" rel="nofollow noopener noreferrer" title="https://www.apollographql.com/docs/react/caching/cache-configuration/#customizing-cache-ids" ref="nofollow noopener noreferrer">typePolicies</a>其中<code>User</code>指的是上述graphql为每一个对象生成的__typename（graphql查询的名字）</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">  cache: <span class="hljs-keyword">new</span> InMemoryCache(&#123;
      <span class="hljs-attr">typePolicies</span>: &#123;
        <span class="hljs-attr">User</span>: &#123;
          <span class="hljs-attr">keyFields</span>: [<span class="hljs-string">"name"</span>],
        &#125;,
      &#125;,
  &#125;),
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol>
<p>如果每条数据都能返回一个<code>id</code>是最好的了，不可以的话也可以能通过上面三种方法来生成id。当然了，除了通过<code>自动生成</code>id来自动更新<code>client中的cache</code>数据之外，apollo还提供了其他两种更新数据方式</p>
<h2 data-id="heading-7">自动更新query</h2>
<p>重新请求需要更新的query,官方文档：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.apollographql.com%2Fdocs%2Freact%2Fdata%2Fmutations%2F%23refetching-queries" target="_blank" rel="nofollow noopener noreferrer" title="https://www.apollographql.com/docs/react/data/mutations/#refetching-queries" ref="nofollow noopener noreferrer">Refetching queries</a></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// Refetches two queries after mutation completes</span>
<span class="hljs-keyword">const</span> [addTodo, &#123; data, loading, error &#125;] = useMutation(ADD_TODO, &#123;
  <span class="hljs-attr">refetchQueries</span>: [ViewerQuery]
 &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">执行update函数，文档地址：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.apollographql.com%2Fdocs%2Freact%2Fdata%2Fmutations%2F%23the-update-function" target="_blank" rel="nofollow noopener noreferrer" title="https://www.apollographql.com/docs/react/data/mutations/#the-update-function" ref="nofollow noopener noreferrer">update</a></h2>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-keyword">const</span> [addUser, addRes] = useMutation(MODIFY_USERS, &#123;
    <span class="hljs-attr">update</span>: <span class="hljs-function">(<span class="hljs-params">cache, data </span>) =></span> &#123;
      <span class="hljs-keyword">const</span> &#123; viewer = &#123;&#125; &#125; = cache.readQuery(&#123; <span class="hljs-attr">query</span>: ViewerQuery &#125;) <span class="hljs-comment">// 如果需要可以之前的数据，可以通过cache.readQuery获得</span>
      <span class="hljs-keyword">const</span> modifyUser = data?.data?.modifyUser
      cache.writeQuery(&#123;
        <span class="hljs-attr">query</span>: ViewerQuery,
        <span class="hljs-attr">data</span>: &#123;
          <span class="hljs-attr">viewer</span>: modifyUser
        &#125;
      &#125;)
    &#125;
  &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里的<code>cache.writeQuery</code>，文档地址<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.apollographql.com%2Fdocs%2Freact%2Fcaching%2Fcache-interaction%2F%23using-cachemodify" target="_blank" rel="nofollow noopener noreferrer" title="https://www.apollographql.com/docs/react/caching/cache-interaction/#using-cachemodify" ref="nofollow noopener noreferrer">cache.writeQuery</a>也可以用<code>cache.modify</code>代替，他们之间的区别是</p>
<ol>
<li>cache.modify只能修改在<code>缓存中已经存在的数据</code></li>
<li>modify绕过了您定义的任何合并函数，这意味着字段总是被您指定的值完全覆盖。</li>
</ol>
<p>从官网的例子能猜出大概，因为需要<code>唯一的id</code>，缓存中<code>没有对应的数据肯定也不存在唯一的id</code>，也就无法<code>通过id</code>更新，所以cache.modify只能<code>修改在缓存中已经存在的数据</code>，指定字段通过<code>field</code>中的<code>函数</code>修改，例如comments</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> idToRemove = <span class="hljs-string">'abc123'</span>;

cache.modify(&#123;
  <span class="hljs-attr">id</span>: cache.identify(myPost),
  <span class="hljs-attr">fields</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">comments</span>(<span class="hljs-params">existingCommentRefs, &#123; readField &#125;</span>)</span> &#123;
      <span class="hljs-keyword">return</span> existingCommentRefs.filter(
        <span class="hljs-function"><span class="hljs-params">commentRef</span> =></span> idToRemove !== readField(<span class="hljs-string">'id'</span>, commentRef)
      );
    &#125;,
  &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>我的结论是：通过<code>id和__typename自动更新client中的cache</code>数据是最好的，其次是使用<code>update函数</code>，最后是<code>重新发起query请求</code>，因为重新发起请求<code>可能会有延时</code>，导致页面<code>刷新不及时</code>。优点就是<code>简单方便</code>。关于网络延时，apollo还支持<code>乐观更新</code>，也就是说先将用户的行为展示在页面上，然后在网络请求成功时修改本地的状态。就像我们在进行微信聊天时，点击发送按钮，输入框的消息会立马出现在聊天面板上，如果网络请求成功则不做任何处理，如果失败就会展现红的感叹号！</p>
</blockquote>
<h2 data-id="heading-9">本地数据处理</h2>
<p>apollo不光能管理你的网络数据，也可以管理你的本地数据。管理本地数据大概分为两种方法，文档地址<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.apollographql.com%2Fdocs%2Freact%2Flocal-state%2Flocal-resolvers" target="_blank" rel="nofollow noopener noreferrer" title="https://www.apollographql.com/docs/react/local-state/local-resolvers" ref="nofollow noopener noreferrer">local-resolvers</a></p>
<ol>
<li>直接调用<code>client.writeQuery</code>就行数据写入</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> &#123; gql, useQuery &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@apollo/client"</span>;

<span class="hljs-keyword">import</span> Link <span class="hljs-keyword">from</span> <span class="hljs-string">"./Link"</span>;

<span class="hljs-keyword">const</span> GET_VISIBILITY_FILTER = gql<span class="hljs-string">`
  query GetVisibilityFilter &#123;
    visibilityFilter @client // client标示查询本地数据而不是发起一个网络请求
  &#125;
`</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">FilterLink</span>(<span class="hljs-params">&#123; filter, children &#125;</span>) </span>&#123;
  <span class="hljs-keyword">const</span> &#123; data, client &#125; = useQuery(GET_VISIBILITY_FILTER);
  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Link</span>
      <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;()</span> =></span> client.writeQuery(&#123;
        query: GET_VISIBILITY_FILTER,
        data: &#123; visibilityFilter: filter &#125;,
      &#125;)&#125;
      active=&#123;data.visibilityFilter === filter&#125;
    >
      &#123;children&#125;
    <span class="hljs-tag"></<span class="hljs-name">Link</span>></span></span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>通过resolver函数就行本地修改，这也是官方较为推荐的方法。和正常的查询数据写法基本上是一致，这里就不多做介绍，详情可以参考上述文档</li>
</ol>
<h1 data-id="heading-10">部署</h1>
<p>关于部署，这里推荐<code>docker</code>，可以和<code>nextjs</code>一起使用</p>
<ol>
<li>通过<code>dockerfile</code>文件将当前项目打包成一份<code>docker image</code>文件</li>
</ol>
<pre><code class="hljs language-yml copyable" lang="yml"><span class="hljs-string">FROM</span> <span class="hljs-string">node:12-alpine</span>
<span class="hljs-string">RUN</span> <span class="hljs-string">mkdir</span> <span class="hljs-string">-p</span> <span class="hljs-string">/usr/src/nodejs/</span>
<span class="hljs-string">COPY</span> <span class="hljs-string">.</span> <span class="hljs-string">/usr/src/nodejs/</span>
<span class="hljs-string">WORKDIR</span> <span class="hljs-string">/usr/src/nodejs/</span>
<span class="hljs-string">RUN</span> <span class="hljs-string">npm</span> <span class="hljs-string">i</span>
<span class="hljs-string">RUN</span> <span class="hljs-string">npm</span> <span class="hljs-string">run</span> <span class="hljs-string">build</span>
<span class="hljs-string">EXPOSE</span> <span class="hljs-number">3000</span>
<span class="hljs-string">CMD</span> [<span class="hljs-string">"npm"</span>, <span class="hljs-string">"start"</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>通过<code>ci/cd工具</code>或手动，将<code>docker image</code>文件上传到<code>私有镜像仓库</code>，这里以<code>阿里云镜像库</code>为例子,当然你也可以搭建自己的<code>私有docker仓库</code>，如果能配合<code>k8s</code>最好</li>
</ol>
<pre><code class="hljs language-javascript copyable" lang="javascript">docker login --username=xxx -p=xxx registry.cn-hangzhou.aliyuncs.com
docker build --tag graphql:<span class="hljs-number">0.0</span><span class="hljs-number">.1</span> .
docker tag studydocker:<span class="hljs-number">0.0</span><span class="hljs-number">.1</span> registry.cn-hangzhou.aliyuncs.com/xxx/xxx001:<span class="hljs-number">0.0</span><span class="hljs-number">.1</span>
docker push registry.cn-hangzhou.aliyuncs.com/xxx/xxx001:<span class="hljs-number">0.0</span><span class="hljs-number">.1</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>在静态仓库中直接部署，这里可以手动部署，在对应的服务器先将对应的<code>image文件下载下来</code>在启动生成<code>容器文件</code></li>
</ol>
<p>拉取镜像文件，docker pull registry.cn-hangzhou.aliyuncs.com/qwelpcyy/xxx001:[镜像版本号]
通过docker-compose启动服务,以下就是我的<code>docker-compose.yml</code>文件</p>
<pre><code class="copyable">version: '3'
services:
  mydocker:
    container_name: graphqlContainer
    image: registry.cn-hangzhou.aliyuncs.com/xxxx/xxx001:0.0.1
    ports:
      - '3000:3000'
    restart: 'always'
    
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-11">总结</h1>
<ul>
<li>我们可以通过<code>useQuery</code>和<code>useMutition</code>进行<code>graphql</code>数据的查询和修改</li>
<li>apollo会将请求好的数据<code>缓存在client中</code>，我们使用<code>fetchPolicy</code>可以通过制定不同的策略来修改这一行为,比如
<ul>
<li>fetchPolicy: "network-only"</li>
<li>fetchPolicy: "cache-only"</li>
<li>...</li>
</ul>
</li>
<li>当使用<code>useMutition</code>进行数据修改时，<code>只会修改服务端数据</code>，<code>本地状态</code>并不会自动修改，可以通过以下三种方式就行修改
<ul>
<li><code>__typename和id（_id）</code>生成<code>唯一key值</code></li>
<li>使用<code>update</code>函数，手动修改逻辑</li>
<li>使用<code>refetchQueries</code>，<code>重新请求</code>需要更新的数据</li>
</ul>
</li>
<li>可以使用@client来标示本地数据，修改本地数据的方式
<ul>
<li>直接修改<code>client.writeQuery</code></li>
<li>使用本地<code>resolver</code></li>
</ul>
</li>
<li>可以结合<code>nextjs</code>一起使用，简单方便，支持<code>SSR</code>，<code>SSG(静态资源生成)</code></li>
<li>可以通过<code>docker docker-compose</code>来进行nodejs服务的部署</li>
</ul></div>  
</div>
            