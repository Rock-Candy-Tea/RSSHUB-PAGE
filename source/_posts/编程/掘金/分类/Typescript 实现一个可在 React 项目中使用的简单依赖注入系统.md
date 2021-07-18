
---
title: 'Typescript 实现一个可在 React 项目中使用的简单依赖注入系统'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7064bfa74ce64996a90eb82be8539a1c~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 17 Jul 2021 23:00:10 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7064bfa74ce64996a90eb82be8539a1c~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">简介，什么是依赖注入</h1>
<p>在说依赖注入之前，我们发现有个概念叫做 “控制反转”经常一起出现，它们区别是：</p>
<ul>
<li>控制反转(Inversion of Control)是一种设计思想</li>
<li>依赖注入(Dependency Injection)是一种编程技巧，是控制反转的一种实现方式</li>
</ul>
<p>通过依赖注入，可以将对象的初始化的细节与使用者剥离开。</p>
<p>在 OO 体系内粗暴地来说，就是使用者不用通过 <code>new</code> 或其他方式显式创建依赖，而只要在构造函数中做出声明，就能直接使用在外部创建好的依赖实例。</p>
<p>不同的框架实现依赖注入的方式不尽相同，后端有 Java 的 Spring 框架，Node.js 的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.nestjs.com%2Fproviders" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.nestjs.com/providers" ref="nofollow noopener noreferrer">Nest.js</a> 服务端框架等等。对于前端来说，比较有名的是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fangular.io%2Fguide%2Fdependency-injection" target="_blank" rel="nofollow noopener noreferrer" title="https://angular.io/guide/dependency-injection" ref="nofollow noopener noreferrer">Angular</a> 框架中的依赖注入实现。</p>
<h2 data-id="heading-1">概念术语</h2>
<p>以 Angular 为例，它的 DI 系统里有几个概念。</p>
<p>基础概念:</p>
<ul>
<li>injectable: 可以被注入的一类对象，在业务系统中，我们希望声明一些 "可注入服务"(injectable service) 供其他地方使用。在 Angular 中，可注入的服务类(Service Class)需要用 <code>@Injectable</code> 装饰。其他的一些简单对象和常量，也可以被注入。</li>
<li>di token: 在 DI 过程中用于查找的标志，可以是任何原始类型或对象，不过一般为了避免冲突，会使用 symbol 或是 class 来作为标志。</li>
<li>injector: 注入器，在 DI 系统中能根据 token 查找到依赖项并传递给使用者的一类对象。在 Angular 中有<a href="https://link.juejin.cn/?target=https%3A%2F%2Fangular.io%2Fguide%2Fhierarchical-dependency-injection%23two-injector-hierarchies" target="_blank" rel="nofollow noopener noreferrer" title="https://angular.io/guide/hierarchical-dependency-injection#two-injector-hierarchies" ref="nofollow noopener noreferrer">不同的注入器实现</a>，没有研究过，不细讲。</li>
<li>provider: 供应者，运行时的依赖具体对象提供者。具有往 injector 中写入对应某 token 的实现的能力。</li>
</ul>
<h1 data-id="heading-2">在 TS/JS 中实现一个简单的依赖注入系统</h1>
<p>一个 DI 系统分为两个重要阶段：</p>
<ul>
<li>依赖收集</li>
<li>依赖初始化</li>
</ul>
<h2 data-id="heading-3">依赖收集</h2>
<p>根据方便程度，可以分成两种:</p>
<h3 data-id="heading-4">手动指定</h3>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// file1</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> USER_SERVICE_SYMBOL = <span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'UserService'</span>)

<span class="hljs-comment">// file2</span>
<span class="hljs-keyword">import</span> &#123;USER_SERVICE_SYMBOL&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'file1'</span>

<span class="hljs-meta">@Inject</span>(&#123;
  <span class="hljs-attr">dependencies</span>: [USER_SERVICE_SYMBOL],
&#125;)
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"><span class="hljs-keyword">private</span> userService: UserService</span>)</span> &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">自动收集</h3>
<p>能否优雅和方便地自动收集依赖，是一个 DI 系统令人心动的指标之一，如果每个类的依赖信息需要用户自行精密地提供，使用起来就有点累。</p>
<p>Typescript 从 1.5 开始就<a href="https://link.juejin.cn/?target=https%3A%2F%2Fjkchao.github.io%2Ftypescript-book-chinese%2Ftips%2Fmetadata.html" target="_blank" rel="nofollow noopener noreferrer" title="https://jkchao.github.io/typescript-book-chinese/tips/metadata.html" ref="nofollow noopener noreferrer">支持 metadata</a>，在编译的时候将编译的得到的元信息记录下来使用, 通过 <code>Reflect.getMetadata('design:paramtypes', target)</code> 就可以获取装饰器所装饰类的入参。比如:</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> UserService <span class="hljs-keyword">from</span> <span class="hljs-string">'./UserService'</span>

<span class="hljs-meta">@Inject</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"><span class="hljs-keyword">private</span> userService: UserService</span>)</span> &#123;&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>TSC 生成部分代码:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> __metadata = (<span class="hljs-built_in">this</span> && <span class="hljs-built_in">this</span>.__metadata) || <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">k, v</span>) </span>&#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Reflect</span> === <span class="hljs-string">"object"</span> && <span class="hljs-keyword">typeof</span> <span class="hljs-built_in">Reflect</span>.metadata === <span class="hljs-string">"function"</span>) <span class="hljs-keyword">return</span> <span class="hljs-built_in">Reflect</span>.metadata(k, v);
&#125;;

<span class="hljs-keyword">let</span> Component = <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">userService</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.userService = userService;
    &#125;
&#125;;
Component = __decorate([
    Inject,
    __metadata(<span class="hljs-string">"design:paramtypes"</span>, [UserService])
], Component);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>让 ts 能生成后面的 <code>__metadata</code> 调用的前提是提供了编译参数 <code>emitDecoratorMetadata</code>:</p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
    <span class="hljs-attr">"compilerOptions"</span>: &#123;
        <span class="hljs-attr">"experimentalDecorators"</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">"emitDecoratorMetadata"</span>: <span class="hljs-literal">true</span>,
    &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>若运行环境不支持 <code>Reflect.metadata</code>，可以安装和使用 polyfill <code>import 'reflect-metadata'</code>。</p>
<h2 data-id="heading-6">依赖注册和初始化</h2>
<p>有一些可以注意的点如下，具体例子见下一节的实现</p>
<ul>
<li>Injectable Service 可以在使用的时候才初始化。声明为 class 的话很自然地可以在 new 的时候做这个事情。当然也有其他的约定方式，视具体框架而定。</li>
<li>一些情况下我们希望对于一种服务，在 DI 系统中只有一个实例，这可以通过 injector 的一个 <code>providerInstanceMap</code> cache 来实现。</li>
</ul>
<h1 data-id="heading-7">实现一个在 React 组件中可以使用的 DI 系统</h1>
<h2 data-id="heading-8">示例代码和 Demo</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fstackblitz.com%2Fedit%2Ftypescript-di-demo%3Ffile%3Dindex.ts" target="_blank" rel="nofollow noopener noreferrer" title="https://stackblitz.com/edit/typescript-di-demo?file=index.ts" ref="nofollow noopener noreferrer">demo 可以去这里运行看看</a>。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// 简单的 Injector + Provider</span>
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Injection</span> </span>&#123;
  <span class="hljs-keyword">private</span> providerMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
  <span class="hljs-comment">/** 记录 provider 的实例，起到 cache 的作用 */</span>
  <span class="hljs-keyword">private</span> providerInstanceMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();
  <span class="hljs-comment">/** 记录 class constructor 参数的信息 */</span>
  <span class="hljs-keyword">private</span> typeInfoMap = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Map</span>();

  <span class="hljs-function"><span class="hljs-title">registerParamTypes</span>(<span class="hljs-params">token, paramTypes</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.typeInfoMap.set(token, paramTypes);
  &#125;

  <span class="hljs-function"><span class="hljs-title">registerProvider</span>(<span class="hljs-params">token, provider</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.providerMap.set(token, provider);
  &#125;

  <span class="hljs-function"><span class="hljs-title">getProviderInstance</span>(<span class="hljs-params">token</span>)</span> &#123;
    <span class="hljs-keyword">let</span> depInstance;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.providerInstanceMap.has(token)) &#123;
      depInstance = <span class="hljs-built_in">this</span>.providerInstanceMap.get(token);
    &#125; <span class="hljs-keyword">else</span> &#123;
      depInstance = <span class="hljs-keyword">new</span> (<span class="hljs-built_in">this</span>.providerMap.get(token))();
      <span class="hljs-built_in">this</span>.providerInstanceMap.set(token, depInstance);
    &#125;
    <span class="hljs-keyword">return</span> depInstance;
  &#125;
&#125;

<span class="hljs-keyword">const</span> injection = <span class="hljs-keyword">new</span> Injection();

<span class="hljs-comment">/**
 * Injectable 类装饰器
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Injectable</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">target</span>) </span>&#123;
    <span class="hljs-comment">// 下面考虑到 service 也许也会依赖其他的 service</span>
    <span class="hljs-keyword">const</span> shouldMakeSubClass = target.length > <span class="hljs-number">0</span>; <span class="hljs-comment">// constructor 有参数的话，就需要注入</span>

    <span class="hljs-keyword">let</span> injectableToRegiter;
    <span class="hljs-keyword">if</span> (shouldMakeSubClass) &#123;
      <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Injected</span> <span class="hljs-keyword">extends</span> (<span class="hljs-title">target</span> <span class="hljs-title">as</span> <span class="hljs-title">any</span>) </span>&#123;
        <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">...args</span>)</span> &#123;
          <span class="hljs-keyword">const</span> dependencyInstances = params.map(<span class="hljs-function"><span class="hljs-params">token</span> =></span>
            injection.getProviderInstance(token)
          );
          <span class="hljs-built_in">super</span>(...args, ...dependencyInstances);
        &#125;
      &#125;
      injectableToRegiter = Injected;
    &#125; <span class="hljs-keyword">else</span> &#123;
      injectableToRegiter = target;
    &#125;

    <span class="hljs-keyword">const</span> params: <span class="hljs-built_in">any</span>[] =
      <span class="hljs-built_in">Reflect</span>.getMetadata(<span class="hljs-string">"design:paramtypes"</span>, target) || [];
    injection.registerParamTypes(injectableToRegiter, params);

    <span class="hljs-comment">// 注册 provider</span>
    injection.registerProvider(target, injectableToRegiter);
    <span class="hljs-keyword">if</span> (target !== injectableToRegiter) &#123;
      injection.registerProvider(injectableToRegiter, injectableToRegiter);
    &#125;

    <span class="hljs-keyword">return</span> injectableToRegiter;
  &#125;;
&#125;

<span class="hljs-comment">/**
 * React.Component 的类装饰器
 */</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">InjectComponent</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span><<span class="hljs-title">T</span>>(<span class="hljs-params">target: T</span>) </span>&#123;
    <span class="hljs-comment">// React Component constructor 的前两个参数已固定，注入的服务只能在后面</span>
    <span class="hljs-keyword">const</span> params: <span class="hljs-built_in">any</span>[] =
      <span class="hljs-built_in">Reflect</span>.getMetadata(<span class="hljs-string">"design:paramtypes"</span>, target).slice(<span class="hljs-number">2</span>) || [];

    <span class="hljs-keyword">const</span> oldConstructor = target.constructor;

    <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">InjectedComponent</span> <span class="hljs-keyword">extends</span> (<span class="hljs-title">target</span> <span class="hljs-title">as</span> <span class="hljs-title">any</span>) </span>&#123;
      <span class="hljs-keyword">static</span> displayName = <span class="hljs-string">`<span class="hljs-subst">$&#123;(oldConstructor <span class="hljs-keyword">as</span> <span class="hljs-built_in">any</span>).displayName ||
        oldConstructor.name&#125;</span>)`</span>;
      <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">...args</span>)</span> &#123;
        <span class="hljs-keyword">const</span> dependencyInstances = params.map(<span class="hljs-function"><span class="hljs-params">token</span> =></span>
          injection.getProviderInstance(token)
        );
        <span class="hljs-built_in">super</span>(...args, ...dependencyInstances);
      &#125;
    &#125;

    <span class="hljs-keyword">return</span> (InjectedComponent <span class="hljs-keyword">as</span> unknown) <span class="hljs-keyword">as</span> T;
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面展示一个使用示例，</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-meta">@Injectable</span>()
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UserService</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">getUsers</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> [<span class="hljs-string">"Zhang San"</span>, <span class="hljs-string">"Li Si"</span>];
  &#125;
&#125;

<span class="hljs-meta">@Injectable</span>()
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">CartService</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"><span class="hljs-keyword">private</span> userService: UserService</span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"init Cart Service"</span>, <span class="hljs-built_in">this</span>.userService);
  &#125;

  <span class="hljs-function"><span class="hljs-title">inspect</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.userService.getUsers().map(<span class="hljs-function"><span class="hljs-params">name</span> =></span> &#123;
      <span class="hljs-keyword">return</span> <span class="hljs-string">`<span class="hljs-subst">$&#123;name&#125;</span> cart total value: <span class="hljs-subst">$&#123;<span class="hljs-built_in">Math</span>.random() * <span class="hljs-number">1000</span>&#125;</span>`</span>;
    &#125;).join(<span class="hljs-string">'\n'</span>);
  &#125;
&#125;

<span class="hljs-meta">@InjectComponent</span>()
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SomeComponent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props, context, <span class="hljs-keyword">private</span> cartService: CartService</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props, context);
  &#125;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> React.createElement(<span class="hljs-string">"div"</span>, &#123;&#125;, [<span class="hljs-built_in">this</span>.cartService.inspect()]);
  &#125;
&#125;

<span class="hljs-comment">// 开始渲染</span>
ReactDOM.render(React.createElement(SomeComponent, &#123;&#125;, []), <span class="hljs-built_in">document</span>.body);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">未实现的高级部分</h2>
<h3 data-id="heading-10">scope，命名空间或作用域</h3>
<p>以上示例中全局只有一个 <code>injection</code>，然而有时在不同场景（命名空间）下我们希望有不同的 provider 实例，甚至还有可能希望 provider 也有一个生命周期跟某个<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.nestjs.com%2Fproviders%23scopes" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.nestjs.com/providers#scopes" ref="nofollow noopener noreferrer">scope</a>绑定起来（在前端项目中，例如每个页面算一个 scope ?)，离开这个 scope 时 执行 <code>provider.dispose()</code> 之类的销毁逻辑。</p>
<h3 data-id="heading-11">Hierarchical injector，分层的注入器</h3>
<p>这个使用的是 Angular 里的术语，简单地说是 injector 是可以有多层的，每一层可以选择性地覆盖掉部分之前层的实现。一个很实用的场景就是在组件树中从某一个节点开始开始替换掉部分实现，实际查找的时候有一个 lookup 的过程，很灵活。详情见 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fangular.io%2Fguide%2Fhierarchical-dependency-injection%23elementinjector" target="_blank" rel="nofollow noopener noreferrer" title="https://angular.io/guide/hierarchical-dependency-injection#elementinjector" ref="nofollow noopener noreferrer">Angular 的 ElementInjector
说明</a> 。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7064bfa74ce64996a90eb82be8539a1c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-12">一些推荐工具库</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Finversify.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://inversify.io/" ref="nofollow noopener noreferrer">InversifyJS a powerful IoC container for JavaScript apps powered by TypeScript</a>。一个通用的 IoC 容器实现，功能强大。</li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FRobinBuschmann%2Freact.di" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/RobinBuschmann/react.di" ref="nofollow noopener noreferrer">RobinBuschmann/react.di: Dependency injection for react based upon inversify.</a>。有许多针对 React 体系的装饰器实现，可以参考学习。</li>
</ul>
<h1 data-id="heading-13">在 React 体系中还需要这套东西么？</h1>
<h2 data-id="heading-14">有 Context 呀</h2>
<p>React 中有一种概念是 <code>Context</code>，算是一种简单的 DI 实现，能够比较好地满足在组件树中共享状态或服务的需求。</p>
<p>不过当有多种 Context 的时候，Context.Provider 需要嵌套写，代码观感很差。</p>
<p>而且 Context 会深入参与 React 的 Reconciliation 过程，因此一般来说使用 Context 共享的都是一些像是 Theme/I18n 之类的对于视图有直接重要影响的数据和服务。其他的各种形式的服务都扔进 Context 的话，可能会导致处理复杂化，影响性能。</p>
<h2 data-id="heading-15">有 Redux 呀</h2>
<p><code>A Predictable State Container for JS Apps</code>，从标语上来看，redux 是一个状态容器，react-redux 体现的是 UI 编程中的关注点分离，将 View 仅作为消费 State 的展示层，同时对于 State 的操作和更改都有迹可循。</p>
<p>但一般在复杂的前端业务系统中，更多的是将 Redux 作为 View Data 的存储。</p>
<p>而怎么与后端交互、后端的数据模型如何转换成视图层模型等等我们称为 ==“业务逻辑”== 的代码，最好还是在一个单独的抽象层中，与视图层的选型隔离开来。而依赖注入，在业务逻辑的复用中，可以有一席之地。</p>
<h1 data-id="heading-16">参考文章</h1>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F113299696" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/113299696" ref="nofollow noopener noreferrer">详解 Angular 依赖注入 - 知乎</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fangular.io%2Fguide%2Fhierarchical-dependency-injection%23elementinjector" target="_blank" rel="nofollow noopener noreferrer" title="https://angular.io/guide/hierarchical-dependency-injection#elementinjector" ref="nofollow noopener noreferrer">Angular - Hierarchical injectors</a></li>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Frbuckton%2Freflect-metadata" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/rbuckton/reflect-metadata" ref="nofollow noopener noreferrer">rbuckton/reflect-metadata: Prototype for a Metadata Reflection API for ECMAScript</a></li>
</ul>
<h1 data-id="heading-17">关于我们</h1>
<p>飞书-字节跳动旗下企业协作平台，集视频会议、在线文档、移动办公、协同软件的一站式企业沟通协作平台。目前飞书业务正在飞速发展中，在北京、深圳等城市都有研发中心，前端、移动端、Rust、服务端、测试、产品等职位都有足够的HC，期待你的加入，和我们一起做有挑战的事情（请戳链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Ffuture.feishu.cn%2Frecruit%25EF%25BC%2589" target="_blank" rel="nofollow noopener noreferrer" title="https://future.feishu.cn/recruit%EF%BC%89" ref="nofollow noopener noreferrer">future.feishu.cn/recruit）</a></p>
<p>我们也欢迎和飞书的同学一起进行技术问题的交流，有兴趣的同学请点击 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fapplink.feishu.cn%2Fclient%2Fchat%2Fchatter%2Fadd_by_link%3Flink_token%3D850v2629-a47c-4f2c-ae70-04de11f260e2" target="_blank" rel="nofollow noopener noreferrer" title="https://applink.feishu.cn/client/chat/chatter/add_by_link?link_token=850v2629-a47c-4f2c-ae70-04de11f260e2" ref="nofollow noopener noreferrer">飞书技术交流群</a> 入群交流</p></div>  
</div>
            