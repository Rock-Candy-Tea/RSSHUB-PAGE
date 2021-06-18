
---
title: 'TypeScript ｜ 类型检查机制'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7331'
author: 掘金
comments: false
date: Thu, 17 Jun 2021 04:57:06 GMT
thumbnail: 'https://picsum.photos/400/300?random=7331'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>TypeScript 的类型检查机制都是为了让开发者在编译阶段就可以直观的发现代码书写问题，养成良好的代码规范从而避免很多低级错误。</p>
<p>TypeScript 类型检查机制包括 <code>类型推断</code>、<code>类型保护</code>、<code>类型兼容性</code></p>
<h3 data-id="heading-0">类型推断</h3>
<p>类型推断主要用于那些没有明确指出类型的地方帮助确定和提供类型</p>
<p>类型推断是有方向的，要注意区分从左向右和从右向左两种推断的不同应用</p>
<p>类型推断的含义是不需要指定变量类型或函数的返回值类型，TypeScript 可以根据一些简单的规则推断其的类型。</p>
<h4 data-id="heading-1">基础类型推断</h4>
<p>基础的类型推断发生在 <strong>初始化变量，设置默认参数和决定返回值时</strong>。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 初始化变量</span>
<span class="hljs-keyword">let</span> x = <span class="hljs-number">3</span>             <span class="hljs-comment">// let x: number</span>
<span class="hljs-keyword">let</span> y = <span class="hljs-string">'hello world'</span> <span class="hljs-comment">// let y: string</span>
<span class="hljs-keyword">let</span> z                 <span class="hljs-comment">// let z: any</span>

<span class="hljs-comment">//设置默认参数和决定返回值时</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">a:number, b:<span class="hljs-number">10</span></span>) </span>&#123; <span class="hljs-comment">// 参数 b 有默认值 10，被推断为 number 类型 ，返回值推断为 number</span>
  <span class="hljs-keyword">return</span> a + b
&#125;
<span class="hljs-keyword">const</span> obj = &#123;
  <span class="hljs-attr">a</span>: <span class="hljs-number">10</span>,
  <span class="hljs-attr">b</span>: <span class="hljs-string">'hello world'</span>
&#125;
obj.b = <span class="hljs-number">15</span> <span class="hljs-comment">// Error，Type '15' is not assignable to type 'string'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">最佳通用类型推断</h4>
<p>当需要从多个元素类型推断出一个类型时，TypeScript 会尽可能推断出一个兼容所有类型的通用类型。</p>
<p>比如声明一个数组：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> x = [<span class="hljs-number">1</span>, <span class="hljs-string">'imooc'</span>, <span class="hljs-literal">null</span>]
<span class="hljs-comment">//数组被推断为 let x: (string | number | null)[] 联合类型</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>是否兼容 null 类型可以通过 tsconfig.json 文件中属性 strictNullChecks 的值设置为 true 或 false 来决定</p>
</blockquote>
<h4 data-id="heading-3">上下文类型推断</h4>
<p><strong>前面两种都是根据从右向左流动进行类型推断，上下文类型推断则是从左向右的类型推断</strong></p>
<p>例如定义一个 Animal 的类作为接口使用：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span> </span>&#123;
  public species: string | <span class="hljs-literal">undefined</span>
  public weight: number | <span class="hljs-literal">undefined</span>
&#125;

<span class="hljs-keyword">const</span> simba: Animal = &#123;
  <span class="hljs-attr">species</span>: <span class="hljs-string">'lion'</span>,
  <span class="hljs-attr">speak</span>: <span class="hljs-literal">true</span>  <span class="hljs-comment">// Error, 'speak' does not exist in type 'Animal'</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">类型保护</h3>
<blockquote>
<p>类型保护是指缩小类型的范围，在一定的块级作用域内由编译器推导其类型，提示并规避不合法的操作，提高代码质量</p>
</blockquote>
<p>我们可以通过 <code>typeof</code>、<code>instanceof</code>、<code>in</code> 和 <code>字面量类型</code> 将代码分割成范围更小的代码块，在这一小块中，变量的类型是确定的</p>
<h4 data-id="heading-5">typeof</h4>
<p>通过 typeof 运算符判断变量类型:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">reverse</span>(<span class="hljs-params">target: string | number</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> target === <span class="hljs-string">'string'</span>) &#123;
    target.toFixed(<span class="hljs-number">2</span>) <span class="hljs-comment">// Error，在这个代码块中，target 是 string 类型，没有 toFixed 方法</span>
    <span class="hljs-keyword">return</span> target.split(<span class="hljs-string">''</span>).reverse().join(<span class="hljs-string">''</span>)
  &#125;
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> target === <span class="hljs-string">'number'</span>) &#123; 
    <span class="hljs-comment">//通过 typeof 关键字，将这个代码块中变量 target 的类型限定为 number 类型</span>
    target.toFixed(<span class="hljs-number">2</span>) <span class="hljs-comment">// OK</span>
    <span class="hljs-keyword">return</span> +[...target.toString()].reverse().join(<span class="hljs-string">''</span>)
  &#125;

  target.forEach(<span class="hljs-function"><span class="hljs-params">element</span> =></span> &#123;&#125;) <span class="hljs-comment">// Error，在这个代码块中，target 是 string 或 number 类型，没有 forEach 方法</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">instanceof</h4>
<p>instanceof 与 typeof 类似，区别在于 typeof 判断基础类型，instanceof 判断是否为某个对象的实例：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">User</span> </span>&#123;
  public nickname: string | <span class="hljs-literal">undefined</span>
  public group: number | <span class="hljs-literal">undefined</span>
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Log</span> </span>&#123;
  public count: number = <span class="hljs-number">10</span>
  public keyword: string | <span class="hljs-literal">undefined</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">typeGuard</span>(<span class="hljs-params">arg: User | Log</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (arg <span class="hljs-keyword">instanceof</span> User) &#123;
    arg.count = <span class="hljs-number">15</span> <span class="hljs-comment">// Error, arg 限定为User类型，无此属性</span>
  &#125;

  <span class="hljs-keyword">if</span> (arg <span class="hljs-keyword">instanceof</span> Log) &#123;
    arg.count = <span class="hljs-number">15</span> <span class="hljs-comment">// OK,arg 限定为Log类型</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">in</h4>
<p>in 操作符用于确定属性是否存在于某个对象上，这也是一种缩小范围的类型保护。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">User</span> </span>&#123;
  public nickname: string | <span class="hljs-literal">undefined</span>
  public groups!: number[]
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Log</span> </span>&#123;
  public count: number = <span class="hljs-number">10</span>
  public keyword: string | <span class="hljs-literal">undefined</span>
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">typeGuard</span>(<span class="hljs-params">arg: User | Log</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-string">'nickname'</span> <span class="hljs-keyword">in</span> arg) &#123;
    <span class="hljs-comment">// (parameter) arg: User，编辑器将推断在当前块作用域 arg 为 User 类型</span>
    arg.nickname = <span class="hljs-string">'imooc'</span>
  &#125;

  <span class="hljs-keyword">if</span> (<span class="hljs-string">'count'</span> <span class="hljs-keyword">in</span> arg) &#123;
    <span class="hljs-comment">// (parameter) arg: Log，编辑器将推断在当前块作用域 arg 为 Log 类型</span>
    arg.count = <span class="hljs-number">15</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">字面量类型保护</h4>
<pre><code class="hljs language-js copyable" lang="js">type Success = &#123;
  <span class="hljs-attr">success</span>: <span class="hljs-literal">true</span>,
  <span class="hljs-attr">code</span>: number,
  <span class="hljs-attr">object</span>: object
&#125;

type Fail = &#123;
  <span class="hljs-attr">success</span>: <span class="hljs-literal">false</span>,
  <span class="hljs-attr">code</span>: number,
  <span class="hljs-attr">errMsg</span>: string,
  <span class="hljs-attr">request</span>: string
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">test</span>(<span class="hljs-params">arg: Success | Fail</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (arg.success === <span class="hljs-literal">true</span>) &#123;
    <span class="hljs-built_in">console</span>.log(arg.object) <span class="hljs-comment">// OK</span>
    <span class="hljs-built_in">console</span>.log(arg.errMsg) <span class="hljs-comment">// Error, Property 'errMsg' does not exist on type 'Success'</span>
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-built_in">console</span>.log(arg.errMsg) <span class="hljs-comment">// OK</span>
    <span class="hljs-built_in">console</span>.log(arg.object) <span class="hljs-comment">// Error, Property 'object' does not exist on type 'Fail'</span>
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">类型兼容性</h3>
<p>类型兼容性用于确定一个类型是否能赋值给其他类型</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> address: string = <span class="hljs-string">'Baker Street 221B'</span>
<span class="hljs-keyword">let</span> year: number = <span class="hljs-number">2010</span>
address = year <span class="hljs-comment">// Error 类型 ‘number’ 不能赋值给类型 ‘string’</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">结构化</h4>
<p><strong>TypeScript 类型兼容性是基于结构类型的；结构类型只使用其成员来描述类型。</strong></p>
<p>TypeScript 结构化类型系统的基本规则是，如果 x 要兼容 y，那么 y 至少具有与 x 相同的属性。比如：</p>
<pre><code class="hljs language-js copyable" lang="js">interface User &#123;
  <span class="hljs-attr">name</span>: string,
  <span class="hljs-attr">year</span>: number
&#125;

<span class="hljs-keyword">let</span> protagonist = &#123;
  <span class="hljs-attr">name</span>: <span class="hljs-string">'Sherlock·Holmes'</span>,
  <span class="hljs-attr">year</span>: <span class="hljs-number">1854</span>,
  <span class="hljs-attr">address</span>: <span class="hljs-string">'Baker Street 221B'</span>
&#125;

<span class="hljs-keyword">let</span> user: User = protagonist <span class="hljs-comment">// OK</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>接口 User 中的每一个属性在 protagonist 对象中都能找到对应的属性，且类型匹配。另外，可以看到 protagonist 具有一个额外的属性 address，但是赋值同样会成功</p>
<h4 data-id="heading-11">比较两个函数</h4>
<p><strong>判断两个函数是否兼容，首先要看参数是否兼容，第二个还要看返回值是否兼容。</strong></p>
<h5 data-id="heading-12">函数参数</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> fn1 = <span class="hljs-function">(<span class="hljs-params">a: number, b: string</span>) =></span> &#123;&#125;
<span class="hljs-keyword">let</span> fn2 = <span class="hljs-function">(<span class="hljs-params">c: number, d: string, e: boolean</span>) =></span> &#123;&#125;

fn2 = fn1 <span class="hljs-comment">// OK</span>
fn1 = fn2 <span class="hljs-comment">// Error</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将 fn1 赋值给 fn2 成立是因为：</p>
<ol>
<li>fn1 的每个参数均能在 fn2 中找到对应类型的参数</li>
<li>参数顺序保持一致，参数类型对应</li>
<li>参数名称不需要相同</li>
</ol>
<p>将 fn2 赋值给 fn1 不成立，是因为 fn2 中的必须参数必须在 fn1 中找到对应的参数，显然第三个布尔类型的参数在 fn1 中未找到</p>
<p>参数类型对应即可，不需要完全相同：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> fn1 = <span class="hljs-function">(<span class="hljs-params">a: number | string, b: string</span>) =></span> &#123;&#125;
<span class="hljs-keyword">let</span> fn2 = <span class="hljs-function">(<span class="hljs-params">c: number, d: string, e: boolean</span>) =></span> &#123;&#125;

fn2 = fn1 <span class="hljs-comment">// OK</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-13">函数返回值</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> x = <span class="hljs-function">() =></span> (&#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'Alice'</span>&#125;)
<span class="hljs-keyword">let</span> y = <span class="hljs-function">() =></span> (&#123;<span class="hljs-attr">name</span>: <span class="hljs-string">'Alice'</span>, <span class="hljs-attr">location</span>: <span class="hljs-string">'Seattle'</span>&#125;)

x = y <span class="hljs-comment">// OK</span>
y = x <span class="hljs-comment">// Error 函数 x() 缺少 location 属性，所以报错</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>类型系统强制源函数的返回值类型必须是目标函数返回值类型的子类型。</p>
<p>如果目标函数的返回值类型是 void，那么源函数返回值可以是任意类型：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> x : <span class="hljs-function">() =></span> <span class="hljs-keyword">void</span>
<span class="hljs-keyword">let</span> y = <span class="hljs-function">() =></span> <span class="hljs-string">'imooc'</span>

x = y <span class="hljs-comment">// OK</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">枚举的类型兼容性</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//枚举与数字类型相互兼容:</span>
enum Status &#123;
  Pending,
  Resolved,
  Rejected
&#125;

<span class="hljs-keyword">let</span> current = Status.Pending
<span class="hljs-keyword">let</span> num = <span class="hljs-number">0</span>

current = num
num = current

<span class="hljs-comment">//不同枚举类型之间是不兼容的：</span>
enum Status &#123; Pending, Resolved, Rejected &#125;
enum Color &#123; Red, Blue, Green &#125;

<span class="hljs-keyword">let</span> current = Status.Pending
current = Color.Red <span class="hljs-comment">// Error</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">类的类型兼容性</h4>
<p><strong>比较两个类类型数据时，只有实例成员会被比较，静态成员和构造函数不会比较。</strong></p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span> </span>&#123;
  feet!: number
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: string, numFeet: number</span>)</span> &#123; &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Size</span> </span>&#123;
  feet!: number
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">numFeet: number</span>)</span> &#123; &#125;
&#125;

<span class="hljs-keyword">let</span> a: Animal
<span class="hljs-keyword">let</span> s: Size

a = s!  <span class="hljs-comment">// OK</span>
s = a  <span class="hljs-comment">// OK</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>类的私有成员和受保护成员会影响兼容性。 允许子类赋值给父类，但是不能赋值给其它有同样类型的类。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Animal</span> </span>&#123;
  protected feet!: number
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">name: string, numFeet: number</span>)</span> &#123; &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Dog</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">Animal</span> </span>&#123;&#125;

<span class="hljs-keyword">let</span> a: Animal
<span class="hljs-keyword">let</span> d: Dog

a = d! <span class="hljs-comment">// OK 子类可以赋值给父类。</span>
d = a <span class="hljs-comment">// OK 父类之所以能够给赋值给子类，是因为子类中没有成员</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Size</span> </span>&#123;
  feet!: number
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">numFeet: number</span>)</span> &#123; &#125;
&#125;

<span class="hljs-keyword">let</span> s: Size

a = s! <span class="hljs-comment">// Error 因为类 Animal 中的成员 feet 是受保护的，所以不能赋值成功</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">泛型的类型兼容性</h4>
<pre><code class="hljs language-js copyable" lang="js">interface Empty<T> &#123;&#125;

<span class="hljs-keyword">let</span> x: Empty<number>
<span class="hljs-keyword">let</span> y: Empty<string>

x = y! <span class="hljs-comment">// OK x 和 y 是兼容的，因为它们的结构使用类型参数时并没有什么不同</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当泛型被成员使用时：</p>
<pre><code class="hljs language-js copyable" lang="js">interface NotEmpty<T> &#123;
  <span class="hljs-attr">data</span>: T
&#125;
<span class="hljs-keyword">let</span> x: NotEmpty<number>
<span class="hljs-keyword">let</span> y: NotEmpty<string>

x = y! <span class="hljs-comment">// Error </span>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果没有指定泛型类型的泛型参数，会把所有泛型参数当成 any 类型比较:</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> identity = <span class="hljs-function"><span class="hljs-keyword">function</span><<span class="hljs-title">T</span>>(<span class="hljs-params">x: T</span>): <span class="hljs-title">void</span> </span>&#123;
  <span class="hljs-comment">// ...</span>
&#125;

<span class="hljs-keyword">let</span> reverse = <span class="hljs-function"><span class="hljs-keyword">function</span><<span class="hljs-title">U</span>>(<span class="hljs-params">y: U</span>): <span class="hljs-title">void</span> </span>&#123;
  <span class="hljs-comment">// ...</span>
&#125;

identity = reverse <span class="hljs-comment">// OK</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-17">学习链接</h3>
<ul>
<li><a href="http://www.imooc.com/wiki/typescriptlesson/typeinference.html" target="_blank" rel="nofollow noopener noreferrer">www.imooc.com/wiki/typesc…</a></li>
<li><a href="http://www.imooc.com/wiki/typescriptlesson/typeguard.html" target="_blank" rel="nofollow noopener noreferrer">www.imooc.com/wiki/typesc…</a></li>
<li><a href="http://www.imooc.com/wiki/typescriptlesson/typecompatibility.html" target="_blank" rel="nofollow noopener noreferrer">www.imooc.com/wiki/typesc…</a></li>
</ul></div>  
</div>
            