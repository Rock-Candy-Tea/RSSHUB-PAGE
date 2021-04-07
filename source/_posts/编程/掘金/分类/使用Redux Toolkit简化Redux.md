
---
title: '使用Redux Toolkit简化Redux'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d78afac005ed44d59f0427a77e28b44a~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Tue, 06 Apr 2021 08:47:53 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d78afac005ed44d59f0427a77e28b44a~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:2;font-weight:400;font-size:15px;overflow-x:hidden;color:#333;letter-spacing:1.2px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1:first-child,.markdown-body h2:first-child,.markdown-body h3:first-child,.markdown-body h4:first-child,.markdown-body h5:first-child,.markdown-body h6:first-child&#123;margin-top:-1.5rem;margin-bottom:1rem&#125;.markdown-body h1:before,.markdown-body h2:before,.markdown-body h3:before,.markdown-body h4:before,.markdown-body h5:before,.markdown-body h6:before&#123;content:"#";display:inline-block;color:#3eaf7c;padding-right:.23em&#125;.markdown-body h1&#123;position:relative;font-size:2.5rem;margin-bottom:5px&#125;.markdown-body h1:before&#123;font-size:2.5rem&#125;.markdown-body h2&#123;padding-bottom:.5rem;font-size:2.2rem;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:1.5rem;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.25rem&#125;.markdown-body h5&#123;font-size:1rem&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body strong&#123;color:#3eaf7c&#125;.markdown-body img&#123;max-width:100%;border-radius:2px;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #3eaf7c;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;overflow-x:auto;padding:.2rem .5rem;margin:0;color:#3eaf7c;font-size:.85em;background-color:rgba(27,31,35,.05);border-radius:3px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border:.5rem solid #3eaf7c&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;font-weight:500;text-decoration:none;color:#3eaf7c;margin:0 5px&#125;.markdown-body a:active,.markdown-body a:hover&#123;text-decoration:none;border-bottom:1.5px solid #3eaf7c&#125;.markdown-body a[href^=http]:after&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTQiIGhlaWdodD0iMTQiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04MzIgMTI4SDY0MHY2NGgxNDYuNzUyTDUyMS4zNzYgNDU3LjM3Nmw0NS4yNDggNDUuMjQ4TDgzMiAyMzcuMjQ4VjM4NGg2NFYxMjh6IiBmaWxsPSIjM2VhZjdjIi8+PHBhdGggZD0iTTc2OCA4MzJIMTkyVjI1NmgzNTJ2LTY0SDE2MGEzMiAzMiAwIDAwLTMyIDMydjY0MGEzMiAzMiAwIDAwMzIgMzJoNjQwYTMyIDMyIDAgMDAzMi0zMlY0ODBoLTY0djM1MnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");margin-left:2px&#125;.markdown-body a[href^="#"]:before&#123;content:"#"&#125;.markdown-body table&#123;display:inline-block!important;font-size:13px;width:auto;max-width:100%;overflow:auto;border:1px solid #3eaf7c;border-collapse:collapse&#125;.markdown-body thead&#123;background:#3eaf7c;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;padding:4px 8px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#7b7878;padding:1px 23px;border-left:.5rem solid;border-color:#42b983;background-color:rgba(66,184,131,.1);position:relative;margin:14px 8px 0&#125;.markdown-body blockquote:before&#123;display:inline-block;position:absolute;content:url("data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjUiIGhlaWdodD0iMjUiIHZpZXdCb3g9IjAgMCAyNyAyNyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxLjg2MiAxLjg2MikiIGZpbGwtcnVsZT0ibm9uemVybyIgZmlsbD0ibm9uZSI+PGNpcmNsZSBzdHJva2U9IiNGRkYiIHN0cm9rZS13aWR0aD0iMS43MjQiIGZpbGw9IiM0MkI5ODMiIGN4PSIxMS42MzgiIGN5PSIxMS42MzgiIHI9IjExLjYzOCIvPjxwYXRoIGQ9Ik0xNC45NzggNi4yN0E1LjAwNiA1LjAwNiAwIDAwNi42NyA5LjQ2OGE0LjkwMSA0LjkwMSAwIDAwMS43NzMgNC4zNjJjLjMyMy4yNTguNTE0LjY0Ny41MjIgMS4wNnYxLjA2YTIuNjg1IDIuNjg1IDAgMDA1LjM3IDB2LTEuMDA4Yy4wMDItLjM5OC4xNzMtLjc3Ny40Ny0xLjA0MmE1LjAyMyA1LjAyMyAwIDAwLjE3My03LjYzem0tMy4zMzcgMTAuOTY3YTEuMzA0IDEuMzA0IDAgMDEtMS4yODYtMS4yODd2LS4yNzhoMi41NzJ2LjI2MWMwIC43MTMtLjU3MyAxLjI5NC0xLjI4NiAxLjMwNHptMi4yNi00LjQxNWMtLjQ0LjM4My0uNzUuODkzLS44ODcgMS40NmgtMi43NDZhMi44NjggMi44NjggMCAwMC0uOTM4LTEuNTNoLS4wMThhMy40NzYgMy40NzYgMCAwMS0xLjI2OS0zLjE0NSAzLjYxNSAzLjYxNSAwIDAxNy4xOTYuNCAzLjY1IDMuNjUgMCAwMS0xLjMzOCAyLjgxNXoiIGZpbGw9IiNGRkYiLz48L2c+PC9zdmc+");width:25px;height:25px;left:-16px;top:12px&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #3eaf7c;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary::-webkit-details-marker&#123;color:#3eaf7c&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body ol li::marker&#123;color:#3eaf7c&#125;.markdown-body ul li&#123;list-style:none;padding-left:10px&#125;.markdown-body ul li::marker&#123;content:"•";color:#3eaf7c&#125;.markdown-body ul li.task-list-item:before&#123;content:"";margin-right:0&#125;.markdown-body input[type=checkbox]&#123;vertical-align:text-bottom;box-shadow:inset 0 0 0 10px #fff&#125;.markdown-body input[type=checkbox]:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTYiIGhlaWdodD0iMTYiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik04NzcuMDU2IDE0Ni45NDR2NzMwLjExMkgxNDYuOTQ0VjE0Ni45NDRoNzMwLjExMnptMC0xMDQuMjc3SDE0Ni45NDRjLTU3LjYyOCAwLTEwNC4yNzcgNDYuNjQ5LTEwNC4yNzcgMTA0LjI3N3Y3MzAuMTEyYzAgNTcuNjI4IDQ2LjY0OSAxMDQuMjc3IDEwNC4yNzcgMTA0LjI3N2g3MzAuMTEyYzU3LjYyOCAwIDEwNC4yNzctNDYuNjQ5IDEwNC4yNzctMTA0LjI3N1YxNDYuOTQ0YzAtNTcuNjI4LTQ2LjY0OS0xMDQuMjc3LTEwNC4yNzctMTA0LjI3N3oiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url("data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB3aWR0aD0iMTUiIGhlaWdodD0iMTUiPjxkZWZzPjxzdHlsZS8+PC9kZWZzPjxwYXRoIGQ9Ik05MTAuMjA4IDBIMTEzLjc2QTExNC4xMTIgMTE0LjExMiAwIDAwLS4wMzIgMTEzLjc5MlY5MTAuMjRjMCA2Mi41OTIgNTEuMiAxMTMuNzkyIDExMy43OTIgMTEzLjc5Mmg3OTYuNDQ4YzYyLjU5MiAwIDExMy43OTItNTEuMiAxMTMuNzkyLTExMy43OTJWMTEzLjc5MkMxMDI0IDUxLjIgOTcyLjggMCA5MTAuMjA4IDB6bS01MTIgNzk2LjQ0OEwxMTMuNzYgNTEybDc5LjY0OC03OS42NDggMjA0LjggMjA0LjhMODMwLjU2IDIwNC44bDc5LjY0OCA3OS42NDgtNTEyIDUxMnoiIGZpbGw9IiMzZWFmN2MiLz48L3N2Zz4=");position:relative;top:-2px;right:2px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>了解Redux Toolkit，这是用于高效Redux开发的经过验证的工具集。在本文中，你将看到为什么Redux Toolkit值得React社区更多的关注。</strong></p>
<p>React和Redux被认为是大规模React应用中管理状态的最佳组合。然而，随着时间的推移，Redux的受欢迎程度下降，原因是：</p>
<ul>
<li>配置Redux Store并不简单。</li>
<li>我们需要几个软件包来使Redux与React一起工作。</li>
<li>Redux需要太多样板代码。</li>
</ul>
<p>带着这些问题，Redux的创建者<strong>Dan Abramov</strong>发表了名为<a href="https://medium.com/@dan_abramov/you-might-not-need-redux-be46360cf367" target="_blank" rel="nofollow noopener noreferrer">《你可能不需要Redux》</a>的文章，建议人们只在需要的时候使用Redux，而在开发不那么复杂的应用时，要遵循其他方法。</p>
<h2 data-id="heading-0">Redux Toolkit解决的问题</h2>
<p>Redux Toolkit(之前称为Redux Starter Kit)提供了一些选项来配置全局store，并通过尽可能地抽象Redux API来更精简地创建动作和reducers。</p>
<h2 data-id="heading-1">它包括什么？</h2>
<p>Redux Toolkit附带了一些有用的软件包，例如Immer，Redux-Thunk和Reselect。它使React开发人员的工作变得更加轻松，允许他们直接更改状态（不处理不可变性），并应用Thunk之类的中间件（处理异步操作）。它还使用了Redux的一个简单的“选择器”库Reselect来简化reducer函数。</p>
<p><img alt="ReduxToolkit依赖项" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d78afac005ed44d59f0427a77e28b44a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">Redux Toolkit API的主要功能？</h2>
<p>以下是Redux Took Kit使用的API函数，它是现有Redux API函数的抽象。这些函数并没有改变Redux的流程，只是以更易读和管理的方式简化了它们。</p>
<ul>
<li><strong>configureStore</strong>：像从Redux中创建原始的createStore一样创建一个Redux store实例，但接受一个命名的选项对象并自动设置Redux DevTools扩展。</li>
<li><strong>createAction</strong>：接受一个Action类型字符串，并返回一个使用该类型的Action创建函数。</li>
<li><strong>createReducer</strong>：接受初始状态值和Action类型的查找表到reducer函数，并创建一个处理所有Action类型的reducer。</li>
<li><strong>createSlice</strong>：接受一个初始状态和一个带有reducer名称和函数的查找表，并自动生成action creator函数、action类型字符串和一个reducer函数。</li>
</ul>
<p>您可以使用上述API简化Redux中的样板代码，尤其是使用<strong>createAction</strong>和<strong>createReducer</strong>方法。然而，这可以使用createSlice进一步简化，它可以自动生成action creator和reducer函数。</p>
<h3 data-id="heading-3">createSlice有什么特别之处？</h3>
<p>它是一个生成存储片的助手函数。它接受片的名称、初始状态和reducer函数来返回reducer、action类型和action creators。</p>
<p>首先，让我们看看在传统的React-Redux应用程序中reducers和actions的样子。</p>
<p><strong>Actions</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;GET_USERS,CREATE_USER,DELETE_USER&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../constant/constants"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> GetUsers = <span class="hljs-function">(<span class="hljs-params">data</span>) =></span> <span class="hljs-function">(<span class="hljs-params">dispatch</span>) =></span> &#123;
 dispatch(&#123;
  <span class="hljs-attr">type</span>: GET_USERS,
  <span class="hljs-attr">payload</span>: data,
 &#125;);
&#125;;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> CreateUser = <span class="hljs-function">(<span class="hljs-params">data</span>) =></span> <span class="hljs-function">(<span class="hljs-params">dispatch</span>) =></span> &#123;
 dispatch(&#123;
  <span class="hljs-attr">type</span>: CREATE_USER,
  <span class="hljs-attr">payload</span>: data,
 &#125;);
&#125;;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> DeleteUser = <span class="hljs-function">(<span class="hljs-params">data</span>) =></span> <span class="hljs-function">(<span class="hljs-params">dispatch</span>) =></span> &#123;
 dispatch(&#123;
  <span class="hljs-attr">type</span>: DELETE_USER,
  <span class="hljs-attr">payload</span>: data,
 &#125;);
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>Reducers</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123;GET_USERS,CREATE_USER,DELETE_USER&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../constant/constants"</span>;
<span class="hljs-keyword">const</span> initialState = &#123;
 <span class="hljs-attr">errorMessage</span>: <span class="hljs-string">""</span>,
 <span class="hljs-attr">loading</span>: <span class="hljs-literal">false</span>,
 <span class="hljs-attr">users</span>:[]
&#125;;
<span class="hljs-keyword">const</span> UserReducer = <span class="hljs-function">(<span class="hljs-params">state = initialState, &#123; payload &#125;</span>) =></span> &#123;
<span class="hljs-keyword">switch</span> (type) &#123;
 <span class="hljs-keyword">case</span> GET_USERS:
  <span class="hljs-keyword">return</span> &#123; ...state, <span class="hljs-attr">users</span>: payload, <span class="hljs-attr">loading</span>: <span class="hljs-literal">false</span> &#125;;
<span class="hljs-keyword">case</span> CREATE_USER:
  <span class="hljs-keyword">return</span> &#123; ...state, <span class="hljs-attr">users</span>: [payload,...state.users],
 <span class="hljs-attr">loading</span>: <span class="hljs-literal">false</span> &#125;;
<span class="hljs-keyword">case</span> DELETE_USER:
  <span class="hljs-keyword">return</span> &#123; ...state, 
  <span class="hljs-attr">users</span>: state.users.filter(<span class="hljs-function">(<span class="hljs-params">user</span>) =></span> user.id !== payload.id),
, loading: <span class="hljs-literal">false</span> &#125;;
<span class="hljs-keyword">default</span>:
  <span class="hljs-keyword">return</span> state;
 &#125;
&#125;;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> UserReducer;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在，让我们看看如何使用<strong>createSlice</strong>简化并实现相同的功能。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createSlice &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@reduxjs/toolkit'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> initialState = &#123;
  <span class="hljs-attr">users</span>: [],
  <span class="hljs-attr">loading</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">error</span>: <span class="hljs-literal">false</span>,
&#125;;
<span class="hljs-keyword">const</span> userSlice = createSlice(&#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'user'</span>,
  initialState,
  <span class="hljs-attr">reducers</span>: &#123;
    <span class="hljs-attr">getUser</span>: <span class="hljs-function">(<span class="hljs-params">state, action</span>) =></span> &#123;
      state.users = action.payload;
      state.loading = <span class="hljs-literal">true</span>;
      state.error = <span class="hljs-literal">false</span>;
    &#125;,
    <span class="hljs-attr">createUser</span>: <span class="hljs-function">(<span class="hljs-params">state, action</span>) =></span> &#123;
      state.users.unshift(action.payload);
      state.loading = <span class="hljs-literal">false</span>;
    &#125;,
    <span class="hljs-attr">deleteUser</span>: <span class="hljs-function">(<span class="hljs-params">state, action</span>) =></span> &#123;
      state.users.filter(<span class="hljs-function">(<span class="hljs-params">user</span>) =></span> user.id !== action.payload.id);
      state.loading = <span class="hljs-literal">false</span>;
    &#125;,
  &#125;,
&#125;);
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> &#123; createUser, deleteUser, getUser &#125; = userSlice.actions;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> userSlice.reducer;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>正如你所看到的，现在所有的动作和reducer都在一个简单的地方，而在传统的redux应用中，你需要在reducer中管理每一个action和它对应的action，当使用createSlice时，你不需要使用开关来识别action。</p>
<p>当涉及到突变状态时，一个典型的Redux流程会抛出错误，你将需要特殊的JavaScript策略，如spread operator和Object assign来克服它们。由于Redux Toolkit使用Immer，因此您不必担心会改变状态。由于slice创建了<strong>actions</strong>和<strong>reducers</strong>，你可以导出它们，并在你的组件和Store中使用它们来配置Redux，而无需为<strong>actions</strong>和<strong>reducers</strong>建立单独的文件和目录，如下所示。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; configureStore &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@reduxjs/toolkit"</span>;
<span class="hljs-keyword">import</span> userSlice <span class="hljs-keyword">from</span> <span class="hljs-string">"./features/user/userSlice"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> configureStore(&#123;
 <span class="hljs-attr">reducer</span>: &#123;
  <span class="hljs-attr">user</span>: userSlice,
 &#125;,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个存储可以通过使用<strong>useSelector</strong>和<strong>useDispatch</strong>的redux api直接从组件中使用。请注意，您不必使用任何常量来标识操作或使用任何类型。</p>
<h2 data-id="heading-4">处理异步Redux流</h2>
<p>为了处理异步动作，Redux Toolkit提供了一个特殊的API方法，称为<strong>createAsyncThunk</strong>，它接受一个字符串标识符和一个payload创建者回调，执行实际的异步逻辑，并返回一个Promise，该Promise将根据你返回的Promise处理相关动作的调度，以及你的reducers中可以处理的action类型。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> axios <span class="hljs-keyword">from</span> <span class="hljs-string">"axios"</span>;
<span class="hljs-keyword">import</span> &#123; createAsyncThunk &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@reduxjs/toolkit"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> GetPosts = createAsyncThunk(
<span class="hljs-string">"post/getPosts"</span>, <span class="hljs-keyword">async</span> () => <span class="hljs-keyword">await</span> axios.get(<span class="hljs-string">`<span class="hljs-subst">$&#123;BASE_URL&#125;</span>/posts`</span>)
);
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> CreatePost = createAsyncThunk(
<span class="hljs-string">"post/createPost"</span>,<span class="hljs-keyword">async</span> (post) => <span class="hljs-keyword">await</span> axios.post(<span class="hljs-string">`<span class="hljs-subst">$&#123;BASE_URL&#125;</span>/post`</span>, post)
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>与传统的数据流不同，由<strong>createAsyncThunk</strong>处理的action将由分片内的<strong>extraReducers</strong>部分处理。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; createSlice &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@reduxjs/toolkit"</span>;
<span class="hljs-keyword">import</span> &#123; GetPosts, CreatePost &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../../services"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> initialState = &#123;
  <span class="hljs-attr">posts</span>: [],
  <span class="hljs-attr">loading</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">error</span>: <span class="hljs-literal">null</span>,
&#125;;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> postSlice = createSlice(&#123;
<span class="hljs-attr">name</span>: <span class="hljs-string">"post"</span>,
<span class="hljs-attr">initialState</span>: initialState,
<span class="hljs-attr">extraReducers</span>: &#123;
   [GetPosts.fulfilled]: <span class="hljs-function">(<span class="hljs-params">state, action</span>) =></span> &#123;
     state.posts = action.payload.data;
   &#125;,
   [GetPosts.rejected]: <span class="hljs-function">(<span class="hljs-params">state, action</span>) =></span> &#123;
    state.posts = [];
   &#125;,
   [CreatePost.fulfilled]: <span class="hljs-function">(<span class="hljs-params">state, action</span>) =></span> &#123;
   state.posts.unshift(action.payload.data);
   &#125;,
 &#125;,
&#125;);
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> postSlice.reducer;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>请注意，在<strong>extraReducers</strong>内部，您可以处理已解决（<strong>fulfilled</strong>）和已拒绝（<strong>rejected</strong>）状态。</p>
<p>通过这些代码片段，您可以看到此工具包在Redux中简化代码的效果如何。我创建了一个<a href="https://github.com/LMPerera/redux-toolkit" target="_blank" rel="nofollow noopener noreferrer">利用Redux Toolkit的REST示例</a>供您参考。</p>
<h2 data-id="heading-5">最后的想法</h2>
<p>根据我的经验，当开始使用Redux时，Redux Toolkit是一个很好的选择。它简化了代码，并通过减少模板代码来帮助管理Redux状态。</p>
<p>最后，就像Redux一样，Redux Toolkit并非仅为React构建。我们可以将其与其他任何框架（例如Angular）一起使用。</p>
<p>您可以通过参考<a href="https://redux-toolkit.js.org/" target="_blank" rel="nofollow noopener noreferrer">Redux Toolkit的文档</a>找到更多信息。</p>
<p>谢谢您的阅读！</p>
<hr>
<p>翻译自<a href="https://blog.bitsrc.io/simplifying-redux-with-redux-toolkit-6236c28cdfcb" target="_blank" rel="nofollow noopener noreferrer">blog.bitsrc.io</a>，作者：Madushika Perera</p>
<h2 data-id="heading-6">更多文章</h2>
<ul>
<li><a href="https://juejin.cn/post/6940225361900732430" target="_blank">Rust与Python：为什么Rust可以取代Python</a></li>
<li><a href="https://juejin.cn/post/6926408651758370830" target="_blank">使用RoughViz可视化Vue.js中的草绘图表</a></li>
<li><a href="https://juejin.cn/post/6924662947680059400" target="_blank">编程日历小程序，对小程序云开发和生成分享海报的实践</a></li>
<li><a href="https://juejin.cn/post/6939782564836016158" target="_blank">改善应用程序性能和代码质量：通过代理模式组合HTTP请求</a></li>
<li><a href="https://juejin.cn/post/6938020120698552356" target="_blank">[译]面向对象编程是计算机科学的最大错误</a></li>
<li><a href="https://juejin.cn/post/6936943306089693221" target="_blank">译|使HTML 5数字输入仅接受整数</a></li>
<li><a href="https://juejin.cn/post/6935430655761186846" target="_blank">13个顶级免费所见即所得文本编辑器工具</a></li>
</ul></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            