
---
title: '如何结合整洁架构和MVP模式提升前端开发体验（三） - 项目工程化配置、规范篇'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=6158'
author: 掘金
comments: false
date: Tue, 06 Sep 2022 17:04:43 GMT
thumbnail: 'https://picsum.photos/400/300?random=6158'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>我报名参加金石计划1期挑战——瓜分10万奖池，这是我的第2篇文章，<a href="https://s.juejin.cn/ds/jooSN7t" title="https://s.juejin.cn/ds/jooSN7t" target="_blank">点击查看活动详情</a></p>
<h1 data-id="heading-0">工程化配置</h1>
<p>还是开发体验的问题，跟开发体验有关的项目配置无非就是使用 eslint、prettier、stylelint 统一代码风格</p>
<h2 data-id="heading-1">formatting and lint</h2>
<p>eslint、prettier、stylelint 怎么配这里就不说了，网上文章太多了。想说的是eslint rule <code>'prettier/prettier': 'error'</code>一定要开启，以及 stylelint rule <code>'prettier/prettier': true</code> 也一定要开启。</p>
<p>虽然配置了eslint、prettier、stylelint，但是可能你队友的编辑器并没有装相应的插件，格式化用的也不是 prettier，然后他修改一行代码顺便把整个文件格式化了一遍。所以还得配置 husky + lint-staged，提交代码的时候按规范格式化回去，不符合规范的代码不允许提交。</p>
<p>如果公司的电脑配置还行的话，可以开发阶段就做相应的 lint， 把错误抛出来，中断编译。webpack 可以使用 eslint-loader，stylelint-webpack-plugin；vite 可以使用 vite-plugin-eslint，vite-plugin-stylelint；vue-cli 配置几个参数就可以开启，具体看文档。</p>
<h2 data-id="heading-2">ts-check</h2>
<p>什么是 ts-check？举个例子，有一个后端接口的某个字段名称变了，由 user_name 改为了 userName，如果没有配置开发阶段进行 ts-check 并把错误抛出来，那么只能全局查找调用接口的地方去修改，如果改漏了，那就喜提一个 BUG。</p>
<p>ts-check 可以开发阶段就做，也可以提交代码的时候做。开发阶段 webpack 安装 fork-ts-checker-webpack-plugin ，vite 也是找相应的插件（暂时没找到用的比较多的）。提交代码的时候，结合 husky 做一次全量的 check (比较耗时)，react 项目执行 tsc --noEmit --skipLibCheck，vue 项目执行 vue-tsc --noEmit --skipLibCheck</p>
<p>ts-check 能好用的前提是你的项目是 TS 写的，接口返回值有具体的类型定义，而不是 any。</p>
<h1 data-id="heading-3">代码规范</h1>
<p>主要讲讲 model，service，presenter，view 这几层的代码规范，之前的文章也有简单提到过，这里做个归纳。</p>
<h2 data-id="heading-4">model</h2>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; reactive, ref &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">import</span> &#123; <span class="hljs-title class_">IFetchUserListResult</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./api"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> <span class="hljs-title function_">useModel</span> = (<span class="hljs-params"></span>) => &#123;
  <span class="hljs-keyword">const</span> userList = reactive<&#123; <span class="hljs-attr">value</span>: <span class="hljs-title class_">IFetchUserListResult</span>[<span class="hljs-string">"result"</span>][<span class="hljs-string">"rows"</span>] &#125;>(&#123;
    <span class="hljs-attr">value</span>: [],
  &#125;);
 
  <span class="hljs-keyword">return</span> &#123;
    userList,
  &#125;;
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">type</span> <span class="hljs-title class_">Model</span> = <span class="hljs-title class_">ReturnType</span><<span class="hljs-keyword">typeof</span> useModel>;

<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>每一个字段都要声明类型，不要因为字段多就用 <code>Object</code>，<code>[k: string]: string | number | boolean</code>，<code>Record<string, string></code> 之类的来偷懒。</li>
<li>可以包含一些简单逻辑的方法，比如重置 state。</li>
<li>vue 中字段声明可以移到 useModel 外面，达到状态共享的作用，在 useModel 中 return 出去使用。</li>
</ol>
<h2 data-id="heading-5">service</h2>
<ol>
<li>react 技术栈，presenter 层调用的时候使用单例方法，避免每次re-render 都生成新的实例。</li>
<li>service 要尽量保持“整洁”，不要直接调用特定环境，端的 API，尽量遵循 <strong>依赖倒置原则</strong>。比如 fetch，WebSocket，cookie，localStorage 等 web 端原生 API 以及 APP 端 JSbridge，不建议直接调用，而是抽象，封装成单独的库或者工具函数，保证是可替换，容易 mock 的。Taro，uni-app 等框架的 API 也不要直接调用，可以放到 presenter 层。组件库提供的命令式调用的组件，也不要使用。</li>
<li>service 方法的入参要合理，不要为了适配组件库而声明不合理的参数，比如某个组件返回 string[] 类型的数据，实际只需要数组第一个元素，参数声明为 string 类型即可。2个以上参数改为使用对象。</li>
<li>业务不复杂可以省略 service 层。</li>
</ol>
<p>service 保证足够的“整洁”，model 和 service 是可以直接进行单元测试的，不需要去关心是 web 环境还是小程序环境。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; <span class="hljs-title class_">Model</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./model'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-keyword">class</span> <span class="hljs-title class_">Service</span> &#123;
  <span class="hljs-keyword">private</span> <span class="hljs-keyword">static</span> <span class="hljs-attr">_indstance</span>: <span class="hljs-title class_">Service</span> | <span class="hljs-literal">null</span> = <span class="hljs-literal">null</span>;

  <span class="hljs-keyword">private</span> <span class="hljs-attr">model</span>: <span class="hljs-title class_">Model</span>;

  <span class="hljs-keyword">static</span> <span class="hljs-title function_">single</span>(<span class="hljs-params">model: Model</span>) &#123;
    <span class="hljs-keyword">if</span> (!<span class="hljs-title class_">Service</span>.<span class="hljs-property">_indstance</span>) &#123;
      <span class="hljs-title class_">Service</span>.<span class="hljs-property">_indstance</span> = <span class="hljs-keyword">new</span> <span class="hljs-title class_">Service</span>(model);
    &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-title class_">Service</span>.<span class="hljs-property">_indstance</span>;
  &#125;

  <span class="hljs-title function_">constructor</span>(<span class="hljs-params">model: Model</span>) &#123;
    <span class="hljs-variable language_">this</span>.<span class="hljs-property">model</span> = model;
  &#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">presenter</h2>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; message, <span class="hljs-title class_">Modal</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'antd'</span>;
<span class="hljs-keyword">import</span> &#123; useModel &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./model'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-title class_">Service</span> <span class="hljs-keyword">from</span> <span class="hljs-string">'./service'</span>;

<span class="hljs-keyword">const</span> <span class="hljs-title function_">usePresenter</span> = (<span class="hljs-params"></span>) => &#123;
  <span class="hljs-keyword">const</span> model = <span class="hljs-title function_">useModel</span>();
  <span class="hljs-keyword">const</span> service = <span class="hljs-title class_">Service</span>.<span class="hljs-title function_">single</span>(model);

  <span class="hljs-keyword">const</span> <span class="hljs-title function_">handlePageChange</span> = (<span class="hljs-params">page: <span class="hljs-built_in">number</span>, pageSize: <span class="hljs-built_in">number</span></span>) => &#123;
    service.<span class="hljs-title function_">changePage</span>(page, pageSize);
  &#125;;

  <span class="hljs-keyword">return</span> &#123;
    model,
    handlePageChange,
  &#125;;
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> usePresenter;

<span class="copy-code-btn">复制代码</span></code></pre>
<ol>
<li>处理 view 事件的方法以 handle 或 on 开头。</li>
<li>不要出现过多的逻辑。</li>
<li>生成 jsx 片段的方法以 render 开头，比如 renderXXX。</li>
<li>不管是 react 还是 vue 不要解构 model，直接 model.xxxx 的方式使用。</li>
</ol>
<h2 data-id="heading-7">view</h2>
<ol>
<li>组件 props 写完整类型。</li>
<li>jsx 不要出现嵌套的三元运算。</li>
<li>尽量所有的逻辑都放到 presenter 中。</li>
<li>不要解构 presenter 以及 model，以 presenter.xxx，model.xxxx 方式调用。</li>
</ol>
<h2 data-id="heading-8">store</h2>
<ol>
<li>不要在外层去使用内层的 store。</li>
</ol>
<h2 data-id="heading-9">接口请求方法</h2>
<ol>
<li>封装的接口请求方法支持泛型</li>
</ol>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> axios, &#123; <span class="hljs-title class_">AxiosRequestConfig</span> &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"axios"</span>;
<span class="hljs-keyword">import</span> &#123; message &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"ant-design-vue"</span>;

<span class="hljs-keyword">const</span> instance = axios.<span class="hljs-title function_">create</span>(&#123;
  <span class="hljs-attr">timeout</span>: <span class="hljs-number">30</span> * <span class="hljs-number">1000</span>,
&#125;);

<span class="hljs-comment">// 请求拦截</span>
instance.<span class="hljs-property">interceptors</span>.<span class="hljs-property">request</span>.<span class="hljs-title function_">use</span>(
  <span class="hljs-function">(<span class="hljs-params">config</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> config;
  &#125;,
  <span class="hljs-function">(<span class="hljs-params">error</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-title class_">Promise</span>.<span class="hljs-title function_">reject</span>(error);
  &#125;,
);

<span class="hljs-comment">// 响应拦截</span>
instance.<span class="hljs-property">interceptors</span>.<span class="hljs-property">response</span>.<span class="hljs-title function_">use</span>(
  <span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-title class_">Promise</span>.<span class="hljs-title function_">resolve</span>(res.<span class="hljs-property">data</span>);
  &#125;,
  <span class="hljs-function">(<span class="hljs-params">error</span>) =></span> &#123;
    message.<span class="hljs-title function_">error</span>(error.<span class="hljs-property">message</span> || <span class="hljs-string">"网络异常"</span>);
    <span class="hljs-keyword">return</span> <span class="hljs-title class_">Promise</span>.<span class="hljs-title function_">reject</span>(error);
  &#125;,
);

<span class="hljs-keyword">type</span> <span class="hljs-title class_">Request</span> = <T = unknown>(config: AxiosRequestConfig) => Promise<T>;

export const request = instance.request as Request;

<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>具体接口的请求方法，入参及返回值都要声明类型，参数量最多两个，body 数据命名为 data，非 body 数据命名为 params，都是对象类型。</li>
<li>参数类型及返回值类型都声明放在一起，不需要用单独的文件夹去放，觉得代码太多不好看可以用 region 注释块折叠起来（vscode 支持）。</li>
<li>接口请求方法以 fetch，del，submit，post 等单词开头。</li>
<li>建议接口请求方法直接放在组件同级目录里，建一个 api.ts 的文件。很多人都习惯把接口请求统一放到一个 servcies 的文件夹里，但是复用的接口又有几个呢，维护代码的时候在编辑器上跨一大段距离来回切换文件夹真的是很糟糕的开发体验。</li>
</ol>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// #region 编辑用户</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> <span class="hljs-title class_">IEditUserResult</span> &#123;
  <span class="hljs-attr">code</span>: <span class="hljs-built_in">number</span>;
  <span class="hljs-attr">msg</span>: <span class="hljs-built_in">string</span>;
  <span class="hljs-attr">result</span>: <span class="hljs-built_in">boolean</span>;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> <span class="hljs-title class_">IEditUserParams</span> &#123;
  <span class="hljs-attr">id</span>: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> <span class="hljs-title class_">IEditUserData</span> &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
  <span class="hljs-attr">age</span>: <span class="hljs-built_in">number</span>;
  <span class="hljs-attr">mobile</span>: <span class="hljs-built_in">string</span>;
  address?: <span class="hljs-built_in">string</span>;
  tags?: <span class="hljs-built_in">string</span>[];
&#125;

<span class="hljs-comment">/**
 * 编辑用户
 * http://yapi.smart-xwork.cn/project/129987/interface/api/1796964
 * <span class="hljs-doctag">@author</span> 划水摸鱼糊屎工程师
 *
 * <span class="hljs-doctag">@param</span> &#123;<span class="hljs-type">IEditUserParams</span>&#125; <span class="hljs-variable">params</span>
 * <span class="hljs-doctag">@param</span> &#123;<span class="hljs-type">IEditUserData</span>&#125; <span class="hljs-variable">data</span>
 * <span class="hljs-doctag">@returns</span>
 */</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">function</span> <span class="hljs-title function_">editUser</span>(<span class="hljs-params">params: IEditUserParams, data: IEditUserData</span>) &#123;
  <span class="hljs-keyword">return</span> request<<span class="hljs-title class_">IEditUserResult</span>>(<span class="hljs-string">`<span class="hljs-subst">$&#123;env.API_HOST&#125;</span>/api/user/edit`</span>, &#123;
    <span class="hljs-attr">method</span>: <span class="hljs-string">'POST'</span>,
    data,
    params,
  &#125;);
&#125;

<span class="hljs-comment">// #endregion</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码是工具生成的，下篇说说提升开发效率及体验的工具。</p></div>  
</div>
            