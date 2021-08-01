
---
title: 'TS学习（二）--.d.ts声明文件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=90'
author: 掘金
comments: false
date: Sat, 31 Jul 2021 04:12:32 GMT
thumbnail: 'https://picsum.photos/400/300?random=90'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>最近在项目中需要在全局声明TS接口类型，需要使用到.d.ts文件进行声明，所以对这块的内容进行研究理解下。</p>
<h1 data-id="heading-1">前置概念</h1>
<h2 data-id="heading-2">命名空间</h2>
<p>随着接口类型的增多，为了避免都在全局命名空间产生命名冲突，我们可以将部分相关的接口放在一个命名空间，即namespaces中。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">namespace</span> Validation &#123;

    <span class="hljs-keyword">export</span> <span class="hljs-keyword">interface</span> StringValidator &#123;

        isAcceptable(s: <span class="hljs-built_in">string</span>): <span class="hljs-built_in">boolean</span>;

    &#125;
    
    ...

&#125;

<span class="hljs-keyword">let</span> validators: &#123; [s: <span class="hljs-built_in">string</span>]: Validation.StringValidator &#125; = &#123;&#125;;
...
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-3">常用声明</h1>
<p>针对不同的数据类型，声明文件的写法不同。这里介绍一些常用方法，更多细节可以参考<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Fdocs%2Fhandbook%2Fdeclaration-files%2Fby-example.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/docs/handbook/declaration-files/by-example.html" ref="nofollow noopener noreferrer">这里</a>。</p>
<h2 data-id="heading-4">全局变量</h2>
<p>全局变量指能在全局命名空间下访问的，比如说暴露出一个或多个全局变量，或者直接将变量写在<code>window</code>对象上。</p>
<p>简单的写法如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// main.js</span>
<span class="hljs-built_in">window</span>.name = <span class="hljs-string">'Tom'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// main.d.ts</span>
<span class="hljs-keyword">declare</span> <span class="hljs-keyword">const</span> name: <span class="hljs-built_in">string</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">全局函数</h2>
<p>全局函数和全局变量的写法类似：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// main.js</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">helloWorld</span>(<span class="hljs-params">s</span>) </span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-string">"Hello, "</span> + s;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// main.d.ts</span>
<span class="hljs-keyword">declare</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">helloWorld</span>(<span class="hljs-params">s: <span class="hljs-built_in">string</span></span>): <span class="hljs-title">string</span></span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当然，实际使用过程中，在库中我们声明的是一个对象，需要对其内部属性也进行声明。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// main.js</span>
<span class="hljs-keyword">const</span> result = myLib.makeGreeting(<span class="hljs-string">"hello, world"</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"The computed greeting is:"</span> + result);

<span class="hljs-keyword">const</span> count = myLib.numberOfGreetings;
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// main.d.ts</span>
<span class="hljs-keyword">declare</span> <span class="hljs-keyword">namespace</span> myLib &#123;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">makeGreeting</span>(<span class="hljs-params">s: <span class="hljs-built_in">string</span></span>): <span class="hljs-title">string</span></span>;
  <span class="hljs-keyword">let</span> numberOfGreetings: <span class="hljs-built_in">number</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">函数重载</h2>
<p>根据函数参数的不同，返回值的不同，声明多个函数接口。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> x: Widget = getWidget(<span class="hljs-number">43</span>);
<span class="hljs-keyword">let</span> arr: Widget[] = getWidget(<span class="hljs-string">"all of them"</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>声明：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-keyword">declare</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getWidget</span>(<span class="hljs-params">n: <span class="hljs-built_in">number</span></span>): <span class="hljs-title">Widget</span></span>;
<span class="hljs-keyword">declare</span> <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getWidget</span>(<span class="hljs-params">s: <span class="hljs-built_in">string</span></span>): <span class="hljs-title">Widget</span>[]</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-7">使用实例</h1>
<p>这里记录一些在项目中的常见使用场景，会不定时进行更新。</p>
<h2 data-id="heading-8">对模块的声明</h2>
<p>在ts文件中，可能会引入一些其他文件（比如png图片）。这时为了避免报错，需要对该文件进行一下声明：</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// index.d.ts</span>
<span class="hljs-keyword">declare</span> <span class="hljs-built_in">module</span> <span class="hljs-string">'*.svg'</span>;
<span class="hljs-keyword">declare</span> <span class="hljs-built_in">module</span> <span class="hljs-string">'*.png'</span>;

<span class="hljs-keyword">declare</span> <span class="hljs-built_in">module</span> <span class="hljs-string">'*.vue'</span> &#123;
    <span class="hljs-keyword">import</span> Vue <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
    <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Vue;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">声明全量变量</h2>
<p>有的时候会在window上声明一些全局变量。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// declarations.d.ts</span>
<span class="hljs-keyword">declare</span> <span class="hljs-keyword">interface</span> Window &#123;
  ...
  <span class="hljs-attr">__locals__</span>: <span class="hljs-built_in">any</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">声明通用接口</h2>
<p>这块直接在声明文件中添加即可。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// index.d.ts</span>
<span class="hljs-keyword">interface</span> BaseObject &#123;
  [key: <span class="hljs-built_in">string</span>]: <span class="hljs-built_in">any</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注：上面的<code>BaseObject</code>在项目中使用时，若添加的eslint校验，可能会产生错误：
<a href="https://link.juejin.cn/?target=https%3A%2F%2Feslint.org%2Fdocs%2Frules%2Fno-undef" target="_blank" rel="nofollow noopener noreferrer" title="https://eslint.org/docs/rules/no-undef" ref="nofollow noopener noreferrer"><code>'BaseObject' is not defined.eslint[no-undef]</code></a>。这时，可以在使用<code>BaseObject</code>的地方添加<code>// eslint-disable-next-line no-undef</code>，也可以在eslint配置文件中添加：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// .eslintrc.js</span>
<span class="hljs-built_in">module</span>.exports = &#123;
    ...
    <span class="hljs-attr">globals</span>: &#123;
        <span class="hljs-attr">BaseObject</span>: <span class="hljs-literal">true</span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">Vue额外方法声明</h2>
<p>在实际项目中，我们使用的是Vue，可能会在其中添加一些公共方法，比如接口调用等，这里需要对添加的这些方法添加额外的声明。</p>
<pre><code class="hljs language-ts copyable" lang="ts"><span class="hljs-comment">// vue 版本2.5.22</span>
<span class="hljs-keyword">declare</span> <span class="hljs-built_in">module</span> <span class="hljs-string">'vue/types/vue'</span> &#123;
  <span class="hljs-keyword">interface</span> Vue &#123;
    <span class="hljs-attr">$tools</span>: VueInstanceTools;
    $get: <span class="hljs-function">(<span class="hljs-params">url: <span class="hljs-built_in">string</span>, param: BaseObject, options?: RequestOptions</span>) =></span> <span class="hljs-built_in">any</span>;
    $post: <span class="hljs-function">(<span class="hljs-params">url: <span class="hljs-built_in">string</span>, param: BaseObject, options?: RequestOptions</span>) =></span> <span class="hljs-built_in">any</span>;
  &#125;
&#125;

<span class="hljs-comment">// vue3</span>
<span class="hljs-keyword">declare</span> <span class="hljs-built_in">module</span> <span class="hljs-string">'@vue/runtime-core'</span> &#123;
  <span class="hljs-keyword">interface</span> Vue &#123;
    <span class="hljs-attr">$tools</span>: VueInstanceTools;
    $get: <span class="hljs-function">(<span class="hljs-params">url: <span class="hljs-built_in">string</span>, param: BaseObject, options?: RequestOptions</span>) =></span> <span class="hljs-built_in">any</span>;
    $post: <span class="hljs-function">(<span class="hljs-params">url: <span class="hljs-built_in">string</span>, param: BaseObject, options?: RequestOptions</span>) =></span> <span class="hljs-built_in">any</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-12">第三方库的声明</h2>
<p>对于一些第三方npm包，可能未使用ts，那么可以单独引入<code>@types/xxx</code>用于声明其中的方法，这块网上很多，就不再过多叙述。</p>
<h1 data-id="heading-13">总结</h1>
<p>d.ts是对ts中变量、函数、第三方库等的声明，能更好的扩展我们使用ts的边界。</p>
<h1 data-id="heading-14">参考</h1>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.typescriptlang.org%2Fdocs%2Fhandbook%2Fdeclaration-files%2Ftemplates%2Fmodule-d-ts.html%23comparing-javascript-to-an-example-dts" target="_blank" rel="nofollow noopener noreferrer" title="https://www.typescriptlang.org/docs/handbook/declaration-files/templates/module-d-ts.html#comparing-javascript-to-an-example-dts" ref="nofollow noopener noreferrer">模块 .d.ts</a></li>
</ul></div>  
</div>
            