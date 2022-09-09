
---
title: 'Flutter学习 - Bloc - 06 列表刷新与加载'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8c71ca621e642a2b68de62ccc0217ee~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
author: 掘金
comments: false
date: Fri, 19 Aug 2022 01:55:50 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8c71ca621e642a2b68de62ccc0217ee~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>携手创作，共同成长！这是我参与「掘金日新计划 · 8 月更文挑战」的第20天，<a href="https://juejin.cn/post/7123120819437322247" title="https://juejin.cn/post/7123120819437322247" target="_blank">点击查看活动详情</a></p>
<blockquote>
<p>本文主要下使用Bloc对列表进行加载和展示</p>
</blockquote>
<p>我们使用实现一个列表的上拉和下拉功能，最终效果如下。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d8c71ca621e642a2b68de62ccc0217ee~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="iShot_2022-08-19_17.42.46.gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>对于这个演示应用程序，我们将使用<a href="https://link.juejin.cn/?target=http%3A%2F%2Fjsonplaceholder.typicode.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://jsonplaceholder.typicode.com/" ref="nofollow noopener noreferrer">jsonplaceholder</a>作为我们的数据源。</p>
<p>在浏览器中打开一个新选项卡并访问<a href="https://link.juejin.cn/?target=https%3A%2F%2Fjsonplaceholder.typicode.com%2Fposts%3F_start%3D0%26_limit%3D2" target="_blank" rel="nofollow noopener noreferrer" title="https://jsonplaceholder.typicode.com/posts?_start=0&_limit=2" ref="nofollow noopener noreferrer">jsonplaceholder.typicode.com/posts?_star…</a>以查看 <code>API</code> 返回的内容。</p>
<pre><code class="hljs language-js copyable" lang="js">
[
  &#123;
    <span class="hljs-string">"userId"</span>: <span class="hljs-number">1</span>,
    <span class="hljs-string">"id"</span>: <span class="hljs-number">1</span>,
    <span class="hljs-string">"title"</span>: <span class="hljs-string">"sunt aut facere repellat provident occaecati excepturi optio reprehenderit"</span>,
    <span class="hljs-string">"body"</span>: <span class="hljs-string">"quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"</span>
  &#125;,
  &#123;
    <span class="hljs-string">"userId"</span>: <span class="hljs-number">1</span>,
    <span class="hljs-string">"id"</span>: <span class="hljs-number">2</span>,
    <span class="hljs-string">"title"</span>: <span class="hljs-string">"qui est esse"</span>,
    <span class="hljs-string">"body"</span>: <span class="hljs-string">"est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"</span>
  &#125;
]

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-0">1. 数据模型</h2>
<p>创建 Post 对象的模型。<code>Post</code>只是一个带有<code>id</code>,<code>title</code>和的类<code>body</code>。</p>
<pre><code class="hljs language-Dart copyable" lang="Dart"><span class="hljs-keyword">import</span> <span class="hljs-string">'package:equatable/equatable.dart'</span>;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Post</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Equatable</span> </span>&#123;

  <span class="hljs-keyword">final</span> <span class="hljs-built_in">int</span> id;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> title;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">String</span> body;
  <span class="hljs-keyword">const</span> Post(&#123;<span class="hljs-keyword">required</span> <span class="hljs-keyword">this</span>.id, <span class="hljs-keyword">required</span> <span class="hljs-keyword">this</span>.title, <span class="hljs-keyword">required</span> <span class="hljs-keyword">this</span>.body&#125;);
  <span class="hljs-meta">@override</span>
  <span class="hljs-built_in">List</span><<span class="hljs-built_in">Object</span>> <span class="hljs-keyword">get</span> props => [id, title, body];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们扩展<a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.dev%2Fpackages%2Fequatable" target="_blank" rel="nofollow noopener noreferrer" title="https://pub.dev/packages/equatable" ref="nofollow noopener noreferrer"><code>Equatable</code></a>以便我们可以比较<code>Posts</code>。如果没有这个，我们将需要手动更改我们的类以覆盖相等性和 hashCode，以便我们可以区分两个<code>Posts</code>对象之间的区别。</p>
<h2 data-id="heading-1">2. PostEvent</h2>
<p>在高层次上，它将响应用户输入（上拉）并获取更多帖子，以便表示层显示它们。让我们从创建我们的<code>Event</code>.</p>
<p>我们<code>PostBloc</code>只会回应一个事件；<code>PostLoad</code>每当需要更多帖子来呈现时，表示层将添加它。由于我们的<code>PostLoad</code>事件是一种类型，<code>PostEvent</code>我们可以像这样创建<code>bloc/post_event.dart</code>和实现事件。</p>
<pre><code class="hljs language-scala copyable" lang="scala">part of 'post_bloc.dart';

<span class="hljs-keyword">abstract</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PostEvent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Equatable</span> </span>&#123;
  const <span class="hljs-type">PostEvent</span>();
  <span class="hljs-meta">@override</span>
  <span class="hljs-type">List</span><<span class="hljs-type">Object</span>> get props => [];
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PostLoad</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">PostEvent</span> </span>&#123;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">3. PostState</h2>
<ul>
<li>
<p><code>PostInitial</code>- 将告诉表示层它需要在加载初始批次的帖子时呈现加载指示器</p>
</li>
<li>
<p><code>PostSuccess</code>- 将告诉表示层它有要渲染的内容</p>
</li>
<li>
<p><code>posts</code>- 将是<code>List<Post></code>将显示的</p>
</li>
<li>
<p><code>isLoadMore</code>- 将告诉表示层它是否可以加载更多</p>
</li>
<li>
<p><code>PostFailure</code>- 将告诉表示层在获取帖子时发生了错误</p>
</li>
</ul>
<p>我们现在可以<code>bloc/post_state.dart</code>像这样创建和实现它。</p>
<pre><code class="hljs language-Dart copyable" lang="Dart"><span class="hljs-keyword">part</span> of <span class="hljs-string">'post_bloc.dart'</span>;

<span class="hljs-keyword">enum</span> PostStatus &#123;initial, success, failure &#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PostState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Equatable</span> </span>&#123;
  <span class="hljs-keyword">final</span> PostStatus status;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">List</span><Post> posts;
  <span class="hljs-keyword">final</span> <span class="hljs-built_in">bool</span> isLoadMore;
  <span class="hljs-keyword">const</span> PostState(&#123;<span class="hljs-keyword">this</span>.status = PostStatus.initial,<span class="hljs-keyword">this</span>.posts = <span class="hljs-keyword">const</span> <Post>[], <span class="hljs-keyword">this</span>.isLoadMore = <span class="hljs-keyword">true</span>&#125;);
  <span class="hljs-comment">/// <span class="markdown">我们实现copyWith了这样我们可以PostSuccess方便地复制和更新零个或多个属性的实例</span></span>
  PostState copyWith(&#123;
    PostStatus? status,
    <span class="hljs-built_in">List</span><Post>? posts,
    <span class="hljs-built_in">bool?</span> isLoadMore,
  &#125;) &#123;
    <span class="hljs-keyword">return</span> PostState(
      status: status ?? <span class="hljs-keyword">this</span>.status,
      posts: posts ?? <span class="hljs-keyword">this</span>.posts,
      isLoadMore: isLoadMore ?? <span class="hljs-keyword">this</span>.isLoadMore,
    );
  &#125;
  <span class="hljs-meta">@override</span>
  <span class="hljs-built_in">List</span><<span class="hljs-built_in">Object</span>> <span class="hljs-keyword">get</span> props => [status, posts, isLoadMore];
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">4. Bolc</h2>
<p>我们实现下bloc中的逻辑，<code>PostBloc</code> 将 <code>PostEvents </code>作为输入并输出<code> PostStates</code>。</p>
<ul>
<li>请求</li>
</ul>
<p>首先我们实现下请求,这里就使用下<code>Dio</code>，简单</p>
<pre><code class="hljs language-Dart copyable" lang="Dart">Future<<span class="hljs-built_in">List</span><Post>> _loadPosts ([<span class="hljs-built_in">int</span> page = <span class="hljs-number">0</span> ]) <span class="hljs-keyword">async</span> &#123;

  <span class="hljs-keyword">var</span> response = <span class="hljs-keyword">await</span> Dio().<span class="hljs-keyword">get</span>(<span class="hljs-string">'https://jsonplaceholder.typicode.com/posts'</span>
      ,queryParameters: &#123;<span class="hljs-string">'_start'</span>:<span class="hljs-string">'<span class="hljs-subst">$page</span>'</span>, <span class="hljs-string">'_limit'</span>:<span class="hljs-string">'<span class="hljs-subst">$_pageCount</span>'</span>&#125;);

  <span class="hljs-keyword">if</span>(response.statusCode == <span class="hljs-number">200</span>) &#123;
    <span class="hljs-keyword">final</span> body = response <span class="hljs-keyword">as</span> <span class="hljs-built_in">List</span>;
    <span class="hljs-keyword">return</span> body.map((<span class="hljs-built_in">dynamic</span> json) &#123;
      <span class="hljs-keyword">final</span> map = json <span class="hljs-keyword">as</span> <span class="hljs-built_in">Map</span><<span class="hljs-built_in">String</span>, <span class="hljs-built_in">dynamic</span>>;
      <span class="hljs-keyword">return</span> Post(
        id: map[<span class="hljs-string">'id'</span>] <span class="hljs-keyword">as</span> <span class="hljs-built_in">int</span>,
        title: map[<span class="hljs-string">'title'</span>] <span class="hljs-keyword">as</span> <span class="hljs-built_in">String</span>,
        body: map[<span class="hljs-string">'body'</span>] <span class="hljs-keyword">as</span> <span class="hljs-built_in">String</span>,
      );
    &#125;).toList();

  &#125;

  <span class="hljs-keyword">throw</span> Exception(<span class="hljs-string">'error'</span>);


&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>loadPost</li>
</ul>
<p>我们需要注册一个事件处理程序来处理传入的<code>PostLoad</code>事件。为了响应<code>PostLoad</code>事件，我们将调用<code>_loadPosts</code>从 API 获取帖子。</p>
<pre><code class="hljs language-Dart copyable" lang="Dart">Future<<span class="hljs-keyword">void</span>> _onPostLoad(PostLoad event, Emitter<PostState> emit) <span class="hljs-keyword">async</span> &#123;
  <span class="hljs-keyword">if</span>(!state.isLoadMore) <span class="hljs-keyword">return</span>;
  <span class="hljs-keyword">try</span> &#123;
    <span class="hljs-keyword">if</span>(state.status == PostStatus.initial) &#123;
      <span class="hljs-keyword">final</span> posts = <span class="hljs-keyword">await</span> _loadPosts();
      <span class="hljs-keyword">return</span> emit(state.copyWith(
        status:  PostStatus.success,
        posts:  posts,
        isLoadMore: posts.length = _pageCount
      ));
    &#125;
    <span class="hljs-keyword">final</span> posts = <span class="hljs-keyword">await</span> _loadPosts(state.posts.length);
    emit(posts.isEmpty ? state.copyWith(isLoadMore: <span class="hljs-keyword">false</span>): state.copyWith(
      status: PostStatus.success,
      posts: <span class="hljs-built_in">List</span>.of(state.posts)..addAll(posts),

    ));
  &#125;<span class="hljs-keyword">catch</span> (_) &#123;
     emit(state.copyWith(status: PostStatus.failure));
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们<code>PostBloc</code>将通过事件处理程序<code>emit</code>中提供的新状态。<code>Emitter<PostState></code></p>
<p>现在每次<code>PostEvent</code>添加 a 时，如果它是一个<code>PostFetched</code>事件并且有更多帖子要获取，我们<code>PostBloc</code>将获取接下来的 20 个帖子。</p>
<p>如果我们尝试获取超过最大帖子数 (100)，API 将返回一个空数组，因此如果我们返回一个空数组，我们的 bloc 将<code>emit</code>是 currentState，除非我们设置<code>isLoadMore</code>为 true。</p>
<p>如果我们无法检索到这些帖子，我们会抛出一个异常并且<code>emit</code> <code>PostFailure()</code>.</p>
<p>如果我们可以检索到帖子，我们会返回<code>PostSuccess()</code>包含整个帖子列表的内容。</p>
<h2 data-id="heading-4">5. UI</h2>
<p>首先还是构建BlocProvider</p>
<pre><code class="hljs language-scala copyable" lang="scala">
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PostPage</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatelessWidget</span> </span>&#123;
  const <span class="hljs-type">PostPage</span>(&#123;<span class="hljs-type">Key</span>? key&#125;) : <span class="hljs-keyword">super</span>(key: key);

  <span class="hljs-meta">@override</span>
  <span class="hljs-type">Widget</span> build(<span class="hljs-type">BuildContext</span> context) &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-type">BlocProvider</span>(
      create: (_)=> <span class="hljs-type">PostBloc</span>()..add(const <span class="hljs-type">PostLoadMore</span>()),
      child: const <span class="hljs-type">PostsList</span>(),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们使用一个三方的刷新组件，提供上拉和下拉</p>
<pre><code class="hljs language-php copyable" lang="php"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">_PostsListState</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">State</span><<span class="hljs-title">PostsList</span>> </span>&#123;
  <span class="hljs-keyword">final</span> RefreshController _refreshController =
  <span class="hljs-title function_ invoke__">RefreshController</span>(<span class="hljs-attr">initialRefresh</span>: <span class="hljs-literal">false</span>);
  @override
  <span class="hljs-keyword">void</span> <span class="hljs-title function_ invoke__">initState</span>() &#123;
    super.<span class="hljs-title function_ invoke__">initState</span>();
    <span class="hljs-comment">// _scrollController.addListener(_onScroll);</span>
  &#125;

  @override
  Widget <span class="hljs-title function_ invoke__">build</span>(BuildContext context) &#123;
    <span class="hljs-keyword">return</span> BlocBuilder<PostBloc, PostState>(
      builder: (context, state) &#123;
        <span class="hljs-keyword">switch</span> (state.status) &#123;
          <span class="hljs-keyword">case</span> PostStatus.failure:
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">const</span> <span class="hljs-variable constant_">Center</span>(child: <span class="hljs-title function_ invoke__">Text</span>(<span class="hljs-string">'failed to fetch posts'</span>));
          <span class="hljs-keyword">case</span> PostStatus.success:
            <span class="hljs-keyword">if</span> (state.posts.isEmpty) &#123;
              <span class="hljs-keyword">return</span> <span class="hljs-keyword">const</span> <span class="hljs-variable constant_">Center</span>(child: <span class="hljs-title function_ invoke__">Text</span>(<span class="hljs-string">'no posts'</span>));
            &#125;
            <span class="hljs-keyword">return</span>  <span class="hljs-title function_ invoke__">Scaffold</span>(
              <span class="hljs-attr">appBar</span>: <span class="hljs-title function_ invoke__">AppBar</span>(<span class="hljs-attr">title</span>: <span class="hljs-keyword">const</span> <span class="hljs-title function_ invoke__">Text</span>(<span class="hljs-string">'Post'</span>),),
              <span class="hljs-attr">body</span>: <span class="hljs-title function_ invoke__">SmartRefresher</span>(
                <span class="hljs-attr">enablePullDown</span>: <span class="hljs-literal">true</span>,
                <span class="hljs-attr">enablePullUp</span>: <span class="hljs-literal">true</span>,
                <span class="hljs-attr">controller</span>: _refreshController,
                <span class="hljs-attr">onRefresh</span>: ()&#123;
                     context.read<PostBloc>().<span class="hljs-title function_ invoke__">add</span>(<span class="hljs-title function_ invoke__">PostRefresh</span>(<span class="hljs-attr">refreshController</span>: _refreshController));&#125;,
                onLoading:  ()&#123;context.read<PostBloc>().<span class="hljs-title function_ invoke__">add</span>(<span class="hljs-title function_ invoke__">PostLoadMore</span>(<span class="hljs-attr">refreshController</span>: _refreshController));&#125;,
                child:  ListView.<span class="hljs-title function_ invoke__">builder</span>(
                  <span class="hljs-attr">itemBuilder</span>: (BuildContext context, <span class="hljs-keyword">int</span> index) &#123;
                    <span class="hljs-keyword">return</span> <span class="hljs-title function_ invoke__">PostListItem</span>(<span class="hljs-attr">post</span>: state.posts[index]);
                  &#125;,
                  itemCount:state.posts.length
                )
              ),
            );
            
          <span class="hljs-keyword">case</span> PostStatus.initial:
            <span class="hljs-keyword">return</span> <span class="hljs-keyword">const</span> <span class="hljs-variable constant_">Center</span>(child: <span class="hljs-title function_ invoke__">CircularProgressIndicator</span>());
        &#125;
      &#125;,
    );
  &#125;

  
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们根据PostStatus来展示不同的页面，每当我们的<code>PostBloc</code>状态发生变化时，我们的 builder 函数都会被调用 new <code>PostState</code>。<br>
这里我们使用下<a href="https://link.juejin.cn/?target=https%3A%2F%2Fpub.dev%2Fpackages%2Fpull_to_refresh" title="https://link.juejin.cn/?target=https%3A%2F%2Fpub.dev%2Fpackages%2Fpull_to_refresh" target="_blank">pull_to_refresh: ^2.0.0</a> 感兴趣看下之前我的介绍 <a href="https://juejin.cn/post/7114649432460623886" target="_blank" title="https://juejin.cn/post/7114649432460623886">刷新组件-pull_to_refresh</a>。 因此我们修改下PostEvent</p>
<pre><code class="hljs language-scala copyable" lang="scala">part of 'post_bloc.dart';

<span class="hljs-keyword">abstract</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PostEvent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Equatable</span> </span>&#123;
 <span class="hljs-keyword">final</span> <span class="hljs-type">RefreshController</span>? refreshController;
  const <span class="hljs-type">PostEvent</span>(&#123;<span class="hljs-keyword">this</span>.refreshController&#125;);
  <span class="hljs-meta">@override</span>
  <span class="hljs-type">List</span><<span class="hljs-type">Object</span>> get props => [];
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PostLoadMore</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">PostEvent</span> </span>&#123;
  const <span class="hljs-type">PostLoadMore</span>(&#123;<span class="hljs-keyword">super</span>.refreshController&#125;);
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PostRefresh</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">PostEvent</span> </span>&#123;
  const <span class="hljs-type">PostRefresh</span>(&#123;<span class="hljs-keyword">super</span>.refreshController&#125;);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>之后把我们的行为拆分为刷新和加载更多，并添加on监听事件。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cabd4f83d29d4131a4354a90e60a41e7~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.image?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>实现下PostListItem</p>
<pre><code class="hljs language-Dart copyable" lang="Dart"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">PostListItem</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">StatelessWidget</span> </span>&#123;
  <span class="hljs-keyword">const</span> PostListItem(&#123;<span class="hljs-keyword">super</span>.key, <span class="hljs-keyword">required</span> <span class="hljs-keyword">this</span>.post&#125;);

  <span class="hljs-keyword">final</span> Post post;

  <span class="hljs-meta">@override</span>
  Widget build(BuildContext context) &#123;
    <span class="hljs-keyword">final</span> textTheme = Theme.of(context).textTheme;
    <span class="hljs-keyword">return</span> Material(
      child: ListTile(
        leading: Text(<span class="hljs-string">'<span class="hljs-subst">$&#123;post.id&#125;</span>'</span>, style: textTheme.caption),
        title: Text(post.title),
        isThreeLine: <span class="hljs-keyword">true</span>,
        subtitle: Text(post.body),
        dense: <span class="hljs-keyword">true</span>,
      ),
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">6. 小结</h2>
<p>尽管在这个应用程序中我们只有一个块，但在较大的应用程序中，很多块管理应用程序状态的不同部分是相当常见的。
我们可以通过创建不同的<code>BlocObservers</code>，每个状态变化都被记录下来，我们能够非常轻松地检测我们的应用程序并在一个地方跟踪所有<code>用户交互和状态变化</code>！
我们<code>PostsPage</code>不知道<code>Posts</code>它们来自哪里或如何检索它们。相反，我们<code>PostBloc</code>不知道如何<code>State</code>渲染，它只是将事件转换为状态。</p></div>  
</div>
            