
---
title: 'CommonJS & AMD & ES6'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=515'
author: 掘金
comments: false
date: Sat, 28 Aug 2021 00:45:24 GMT
thumbnail: 'https://picsum.photos/400/300?random=515'
---

<div>   
<div class="markdown-body html cache"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>首先我们要清楚 <strong>模块化规范</strong> 和 <strong>模块化实现</strong> 的区别，规范是定义，比如规定 A 对象应该有 B 属性，实现则是参照这些规范来编写工具库。</p>
<p>一种规范可以有多个实现，CommonJS、AMD、ES6 这些都是模块化规范，而 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fnodejs.cn%2Fapi%2Fmodules.html%23modules_modules_commonjs_modules" target="_blank" rel="nofollow noopener noreferrer" title="http://nodejs.cn/api/modules.html#modules_modules_commonjs_modules" ref="nofollow noopener noreferrer">NodeJS Module</a>，<a href="https://link.juejin.cn/?target=https%3A%2F%2Frequirejs.org%2Fdocs%2Fstart.html" target="_blank" rel="nofollow noopener noreferrer" title="https://requirejs.org/docs/start.html" ref="nofollow noopener noreferrer">RequireJS</a>，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwebpack.js.org%2Fconcepts%2Fmodules%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://webpack.js.org/concepts/modules/" ref="nofollow noopener noreferrer">Webpack Module</a> 等是对这些模块化规范的实现，在这些实现的基础上，我们才能使用对应的模块化语法。</p>
<p>在开始之前，也建议读读 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fseajs%2Fseajs%2Fissues%2F588" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/seajs/seajs/issues/588" ref="nofollow noopener noreferrer">前端模块化开发那点历史</a> 这篇文章，和前面 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fseajs%2Fseajs%2Fissues%2F547" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/seajs/seajs/issues/547" ref="nofollow noopener noreferrer">前端模块化开发的价值</a> 是同一个作者，该作者编写了有名的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fseajs%2Fseajs" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/seajs/seajs" ref="nofollow noopener noreferrer">seajs</a> 库，seajs 可支持 JS 模块化开发，遵循的是 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fcmdjs%2Fspecification%2Fblob%2Fmaster%2Fdraft%2Fmodule.md" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/cmdjs/specification/blob/master/draft/module.md" ref="nofollow noopener noreferrer">CMD</a> 规范。</p>
<h2 data-id="heading-0">（1）CommonJS</h2>
<h3 data-id="heading-1">前言</h3>
<p>从 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.commonjs.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://www.commonjs.org/" ref="nofollow noopener noreferrer">CommonJS</a> 的官网上我们可以了解到这个项目的初衷：“官方的 JavaScript 规范定义了一些适用于浏览器端应用的 API，但是缺乏针对于更多场景（如服务器端应用、命令行工具、桌面应用等）的标准库声明。CommonJS API 将通过定义常见场景下的 API 来填补这个空缺，最终提供一个像 Python、Ruby、Java 那样丰富的标准库。”</p>
<blockquote>
<p>The official JavaScript specification defines APIs for some objects that are useful for building browser-based applications. However, the spec does not define a standard library that is useful for building a broader range of applications.</p>
<p>The CommonJS API will fill that gap by defining APIs that handle many common application needs, ultimately providing a standard library as rich as those of Python, Ruby and Java</p>
</blockquote>
<p>当时 Javascript 仅仅只运行在浏览器上，而 CommonJS 的愿景是让开发者使用标准的 CommonJS API，在未来通过兼容 CommonJS 的解释器或平台，<strong>使 Javascript 可以被用来编写任何应用</strong>。</p>
<p>所以准确来说，CommonJS 项目不仅仅是一个模块化规范，它包含了许多场景下的 Javascript API 规范定义，比如 I/O，文件系统（Filesystem），包管理（Package）等等，模块化规范只是它的一个部分。</p>
<h3 data-id="heading-2">CommonJS 模块规范</h3>
<p>在 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.commonjs.org%2Fspecs%2Fmodules%2F1.0%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://www.commonjs.org/specs/modules/1.0/" ref="nofollow noopener noreferrer">CommonJS Module 1.0</a> 规范中，定义了要支持模块化所需实现的最小特性。</p>
<ol>
<li>
<p>在一个模块中，应该有一个可直接使用的函数“require”</p>
<p>（1） <em>“require”函数接收一个模块标识符参数</em></p>
<p>（2） <em>“require”返回外部模块导出的 API</em></p>
<p>（3）<em>如果存在<strong>循环依赖</strong>（dependency cycle），“require”返回的对象应至少包含外部模块在调用引入本模块的代码之前的导出结果</em></p>
<p>（4）<em>如果被引入的模块无法返回，“require”必须抛出一个错误。</em></p>
</li>
<li>
<p>在一个模块中，应该有一个可直接使用的对象“exports”，在模块执行时将导出的 API 添加到这个对象中。</p>
</li>
<li>
<p>模块必须使用“exports”对象作为导出 API 的唯一方式。</p>
</li>
</ol>
<p><strong>循环依赖</strong> 是什么意思呢？我们可以通过下面的例子来帮助理解。“a.js”（模块A） 和 “b.js”（模块B），A 引入 B ，B 也引入了 A，这样就陷入了死循环，有点像操作系统的“死锁”。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// a.js</span>
<span class="hljs-keyword">const</span> b = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./b'</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Print b in module a =>'</span>, b);
<span class="hljs-built_in">exports</span>.name = <span class="hljs-string">'a'</span>;

<span class="hljs-comment">// b.js</span>
<span class="hljs-keyword">const</span> a = <span class="hljs-built_in">require</span>(<span class="hljs-string">'./a'</span>);
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'Print a in module b =>'</span>, a);
<span class="hljs-built_in">exports</span>.name = <span class="hljs-string">'b'</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也可以类比下面的例子：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">funcA</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> b = funcB();
  <span class="hljs-keyword">return</span> <span class="hljs-string">'a'</span> + b;
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">funcB</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">const</span> a = funcA();
  <span class="hljs-keyword">return</span> <span class="hljs-string">'b'</span> + a;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Node（v15.9.0）中运行上面的代码会报错，“RangeError: Maximum call stack size exceeded”，由于循环调用，最终栈溢出了。</p>
<p>所以，模块系统必须要解决循环依赖的问题。</p>
<p><strong>CommonJS 模块示例</strong> 如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// math.js</span>
<span class="hljs-built_in">exports</span>.add = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> sum = <span class="hljs-number">0</span>, i = <span class="hljs-number">0</span>, args = <span class="hljs-built_in">arguments</span>, l = args.length;
    <span class="hljs-keyword">while</span> (i < l) &#123;
        sum += args[i++];
    &#125;
    <span class="hljs-keyword">return</span> sum;
&#125;;

<span class="hljs-comment">// increment.js</span>
<span class="hljs-keyword">var</span> add = <span class="hljs-built_in">require</span>(<span class="hljs-string">'math'</span>).add;
<span class="hljs-built_in">exports</span>.increment = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">val</span>) </span>&#123;
    <span class="hljs-keyword">return</span> add(val, <span class="hljs-number">1</span>);
&#125;;

<span class="hljs-comment">// program.js</span>
<span class="hljs-keyword">var</span> inc = <span class="hljs-built_in">require</span>(<span class="hljs-string">'increment'</span>).increment;
<span class="hljs-keyword">var</span> a = <span class="hljs-number">1</span>;
inc(a); <span class="hljs-comment">// 2</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>总结而言，CommonJS 定义了一套模块导出和引入机制，每个模块互不干扰，只能通过“require” 和 “exports”进行交互，这样即解决了模块化开发的问题。</p>
<blockquote>
<p>一点历史：CommonJS 最开始叫 ServerJS，这点可以在官网上查到，可见它原本目的是想推广 JS 到服务端的，不过后来这个范围更广了，它也改名叫 CommonJS 了。Node.js 当时就是借鉴 CommonJS 规范来实现自身的模块系统的，并且取得了不错的效果。</p>
</blockquote>
<h2 data-id="heading-3">（2）AMD</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Famdjs%2Famdjs-api%2Fwiki%2FAMD" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/amdjs/amdjs-api/wiki/AMD" ref="nofollow noopener noreferrer">AMD</a> 全称是 Asynchronous Module Definition（异步模块定义），它制定了一种能使模块以及模块的依赖可以被 <strong>异步加载</strong> 的机制。</p>
<p>在有了 CommonJS 的情况下为何还需要 AMD 呢？<a href="https://link.juejin.cn/?target=https%3A%2F%2Frequirejs.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://requirejs.org/" ref="nofollow noopener noreferrer">RequireJS</a>（AMD的一种实现）的这两篇文章 <a href="https://link.juejin.cn/?target=https%3A%2F%2Frequirejs.org%2Fdocs%2Fwhy.html" target="_blank" rel="nofollow noopener noreferrer" title="https://requirejs.org/docs/why.html" ref="nofollow noopener noreferrer">WHY WEB MODULES?</a> ，<a href="https://link.juejin.cn/?target=https%3A%2F%2Frequirejs.org%2Fdocs%2Fwhyamd.html" target="_blank" rel="nofollow noopener noreferrer" title="https://requirejs.org/docs/whyamd.html" ref="nofollow noopener noreferrer">WHY AMD</a> 说出了他们的考虑。一言以蔽之：<strong>CommonJS 并不适合浏览器环境</strong>。</p></div>  
</div>
            