
---
title: 'Angular依赖注入'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1440'
author: 掘金
comments: false
date: Wed, 18 Aug 2021 00:22:26 GMT
thumbnail: 'https://picsum.photos/400/300?random=1440'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">依赖注入概念：</h4>
<p>维基百科对依赖注入的解释：在软件工程中，依赖注入是实现控制反转的一种软件设计模式，一个依赖是一个被其他对象(client)调用的对象（服务）,注入则是将被依赖的对象(service)实例传递给依赖对象(client)的行为。将 被依赖的对象传给依赖者，而不需要依赖者自己去创建或查找所需对象是DI的基本原则。 依赖注入允许程序设计遵从依赖倒置原则（简单的说就是要求对抽象进行编程，不要对实现进行编程，这样就降低了客户与实现模块间的耦合） 调用者(client)只需知道服务的接口，具体服务的查找和创建由注入者(injector)负责处理并提供给client，这样就分离了服务和调用者的依赖，符合低耦合的程序设计原则。也是依赖注入的主要目的。</p>
<h4 data-id="heading-1">控制反转</h4>
<p>控制反转和依赖注入是相辅相成的。例子：classA依赖classB但是classA不主动创建classB的实例，通过参数的形式传递进来。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">A</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">construct</span>(<span class="hljs-params"><span class="hljs-keyword">private</span> b: B</span>)</span> &#123;&#125;
&#125;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">B</span> </span>&#123;&#125;
<span class="hljs-keyword">const</span> a: A = <span class="hljs-keyword">new</span> A(<span class="hljs-keyword">new</span> B());
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Angular依赖注入是实例化组件的时候，将服务的实例传递进来，形成了控制反转。</p>
<h4 data-id="heading-2">依赖注入</h4>
<p>Angular依赖注入使用的都是一个实例，也是Angular通过服务通信的一种方式。如果不适用依赖注入，多个实例，组件间通信也就无法使用服务了。
app.module.ts:</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; BrowserModule &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@angular/platform-browser'</span>;
<span class="hljs-keyword">import</span> &#123; NgModule, InjectionToken &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@angular/core'</span>;
<span class="hljs-keyword">import</span> &#123; AppComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./components/app/app.component'</span>;
<span class="hljs-keyword">import</span> &#123; SingleServiceService &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./service/single-service.service'</span>;
<span class="hljs-keyword">import</span> &#123; MyServiceService &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./service/my-service.service'</span>;
<span class="hljs-keyword">import</span> &#123; UseServiceService &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./service/use-service.service'</span>;
<span class="hljs-keyword">import</span> &#123; ValueServiceService &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./service/value-service.service'</span>;
<span class="hljs-keyword">import</span> &#123; ReactiveFormsModule, FormsModule &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@angular/forms'</span>;
<span class="hljs-keyword">import</span> &#123; HttpClientModule &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@angular/common/http'</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> AppConfig &#123;
    <span class="hljs-attr">title</span>: <span class="hljs-built_in">string</span>
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> CONFIG = <span class="hljs-keyword">new</span> InjectionToken<AppConfig>(<span class="hljs-string">'描述令牌的用途'</span>);

<span class="hljs-keyword">const</span> USE_Config = &#123;
    <span class="hljs-attr">title</span>: <span class="hljs-string">"非类的注入令牌"</span>
&#125;

<span class="hljs-meta">@NgModule</span>(&#123;
    <span class="hljs-attr">declarations</span>: [
        AppComponent
    ],
    <span class="hljs-attr">imports</span>: [
        BrowserModule,
        HttpClientModule,
        FormsModule,
        ReactiveFormsModule
    ],
    <span class="hljs-attr">providers</span>: [
        SingleServiceService,
        <span class="hljs-comment">// 完整形式</span>
        <span class="hljs-comment">// &#123;provide: SingleServiceService, useClass: SingleServiceService&#125;</span>
        <span class="hljs-comment">// provide 属性存有令牌，它作为一个 key，在定位依赖值和配置注入器时使用。</span>
        <span class="hljs-comment">// 属性二通知如何创建依赖，实际依赖的值可以是useClass、 useExisting、useValue 或 useFactory</span>
        <span class="hljs-comment">// useExisting起别名,依赖注入也可以注入组件</span>
        &#123;<span class="hljs-attr">provide</span>: MyServiceService, <span class="hljs-attr">useClass</span>: UseServiceService&#125;,
        <span class="hljs-comment">// useValue可以是字符串，对象等</span>
        &#123;<span class="hljs-attr">provide</span>: ValueServiceService, <span class="hljs-attr">useValue</span>: <span class="hljs-string">"依赖注入字符"</span>&#125;,
        <span class="hljs-comment">// 使用 InjectionToken 对象来为非类的依赖选择一个提供者令牌</span>
        &#123; <span class="hljs-attr">provide</span>: CONFIG, <span class="hljs-attr">useValue</span>: USE_Config &#125;
    ],
    <span class="hljs-attr">bootstrap</span>: [AppComponent],
    <span class="hljs-attr">entryComponents</span>: []
&#125;)
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">AppModule</span> </span>&#123; &#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>SingleServiceService:</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; Injectable &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@angular/core'</span>;

<span class="hljs-meta">@Injectable</span>()
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">SingleServiceService</span> </span>&#123;

<span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123; &#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>MyServiceService:</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; Injectable &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@angular/core'</span>;

<span class="hljs-meta">@Injectable</span>()
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">MyServiceService</span> </span>&#123;

    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123; &#125;

    getName(): <span class="hljs-built_in">string</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">"my-service"</span>;
    &#125;
    
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>UseServiceService:</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; Injectable &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@angular/core'</span>;

<span class="hljs-meta">@Injectable</span>()
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UseServiceService</span> </span>&#123;

    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123; &#125;

    getName(): <span class="hljs-built_in">string</span> &#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">"use-service"</span>;
    &#125;

&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>ValueServiceService:</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">import</span> &#123; Injectable &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@angular/core'</span>;

<span class="hljs-meta">@Injectable</span>()
<span class="hljs-keyword">export</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ValueServiceService</span> </span>&#123;

<span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params"></span>)</span> &#123; &#125;

&#125;

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            