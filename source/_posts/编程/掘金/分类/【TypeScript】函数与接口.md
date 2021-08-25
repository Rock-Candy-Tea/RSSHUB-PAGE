
---
title: '【TypeScript】函数与接口'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2876'
author: 掘金
comments: false
date: Tue, 24 Aug 2021 06:03:29 GMT
thumbnail: 'https://picsum.photos/400/300?random=2876'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第24天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></strong></p>
<hr>
<h3 data-id="heading-0">函数</h3>
<h4 data-id="heading-1">（1）定义</h4>
<ul>
<li>
<p>函数类型：定义函数类型时，需要为<strong>形参</strong>添加类型注解，需要为函数<strong>返回值</strong>添加类型注解</p>
<ul>
<li>如果没有返回值，则返回值类型为<code>void</code></li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// 命名函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fun1</span>(<span class="hljs-params">x: <span class="hljs-built_in">number</span>, y: <span class="hljs-built_in">number</span></span>): <span class="hljs-title">number</span> </span>&#123;
  <span class="hljs-keyword">return</span> x + y
&#125;

<span class="hljs-comment">// 匿名函数</span>
<span class="hljs-keyword">let</span> fun2 = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">x: <span class="hljs-built_in">number</span>, y: <span class="hljs-built_in">number</span></span>): <span class="hljs-title">number</span> </span>&#123; 
  <span class="hljs-keyword">return</span> x + y
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>所以<code>fun2</code>是没有类型的，它的类型是由右侧函数返回值推断出来的，所以可以手动添加类型</p>
<blockquote>
<p><code>=></code>表示：左边是输入函数的输入类型，右边表示函数的输出类型</p>
</blockquote>
<pre><code class="hljs language-typescript copyable" lang="typescript">
<span class="hljs-keyword">let</span> fun2: <span class="hljs-function">(<span class="hljs-params">x: <span class="hljs-built_in">number</span>, y: <span class="hljs-built_in">number</span></span>) =></span> <span class="hljs-built_in">number</span> = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">x: <span class="hljs-built_in">number</span>, y: <span class="hljs-built_in">number</span></span>): <span class="hljs-title">number</span> => </span>&#123;
    <span class="hljs-keyword">return</span> x + y
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
</li>
</ul>
<h4 data-id="heading-2">（2）参数</h4>
<ul>
<li>
<p><strong>可选参数</strong>：可以在参数名后面添加<code>?</code>标识符来标识这个参数是可选的</p>
</li>
<li>
<p><strong>默认参数</strong>：可以直接为参数赋值，让其有一个默认值</p>
</li>
<li>
<p><strong>剩余参数</strong>：可以通过省略号<code>...</code>来接收剩余参数，表示没有接收的参数数组</p>
<ul>
<li>剩余参数的参数名是<code>...</code>后面的名字，可以指定，它表示一个数组，可以在函数内使用这个数组</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// firstName的默认值为 A ， lastName参数是可选的</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">buildName</span>(<span class="hljs-params">first: <span class="hljs-built_in">string</span> = <span class="hljs-string">'R'</span>, last?: <span class="hljs-built_in">string</span></span>): <span class="hljs-title">string</span> </span>&#123;
    <span class="hljs-keyword">if</span> (last) &#123;
        <span class="hljs-keyword">return</span> first + <span class="hljs-string">'-'</span> + last
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">return</span> first
    &#125;
&#125;

<span class="hljs-comment">// 剩余参数 ... </span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">info</span>(<span class="hljs-params">x: <span class="hljs-built_in">string</span>, ...args: <span class="hljs-built_in">string</span>[]</span>): <span class="hljs-title">void</span> </span>&#123;
    <span class="hljs-built_in">console</span>.log(x, args)
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-3">（3）函数重载</h4>
<ul>
<li>
<p><strong>函数重载</strong>是指：函数名相同，而参数类型不同、参数个数不同，相应的，函数内部的处理也不同</p>
<ul>
<li>即，提供多个函数类型定义，当传入不同参数时，在函数重载列表中去查找对应的函数定义，并执行函数内响应的方法</li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">/* 
函数重载: 函数名相同, 而形参不同的多个函数
需求: 我们有一个add函数，它可以接收2个string类型的参数进行拼接，也可以接收2个number类型的参数进行相加 
*/</span>

<span class="hljs-comment">// 重载函数声明</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span> (<span class="hljs-params">x: <span class="hljs-built_in">string</span>, y: <span class="hljs-built_in">string</span></span>): <span class="hljs-title">string</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span> (<span class="hljs-params">x: <span class="hljs-built_in">number</span>, y: <span class="hljs-built_in">number</span></span>): <span class="hljs-title">number</span>
// 定义函数实现： 函数实现放在最后一个
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">add</span>(<span class="hljs-params">x: <span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span>, y: <span class="hljs-built_in">string</span> | <span class="hljs-built_in">number</span></span>): <span class="hljs-title">string</span> | <span class="hljs-title">number</span> </span>&#123;
    // 在实现上我们要注意严格判断两个参数的类型是否相等，而不能简单的写一个 <span class="hljs-title">x</span> + <span class="hljs-title">y</span>
    <span class="hljs-title">if</span> (<span class="hljs-params"><span class="hljs-keyword">typeof</span> x === <span class="hljs-string">'string'</span> && <span class="hljs-keyword">typeof</span> y === <span class="hljs-string">'string'</span></span>) </span>&#123;
        <span class="hljs-title">return</span> <span class="hljs-title">x</span> + <span class="hljs-title">y</span>
    &#125; <span class="hljs-title">else</span> <span class="hljs-title">if</span> (<span class="hljs-params"><span class="hljs-keyword">typeof</span> x === <span class="hljs-string">'number'</span> && <span class="hljs-keyword">typeof</span> y === <span class="hljs-string">'number'</span></span>) </span>&#123;
        <span class="hljs-keyword">return</span> x + y
    &#125;
&#125;

<span class="hljs-built_in">console</span>.log(add(<span class="hljs-number">1</span>, <span class="hljs-number">2</span>))
<span class="hljs-built_in">console</span>.log(add(<span class="hljs-string">'a'</span>, <span class="hljs-string">'b'</span>))
<span class="hljs-comment">// console.log(add(1, 'a')) // error</span>

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-4">关于<code>&#123;&#125;</code>、<code>object</code>、<code>Object</code></h3>
<ul>
<li>
<p><code>&#123;&#125;</code>表示非<code>null</code>、非<code>undefined</code>的<strong>任意类型</strong></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">let</span> obj: &#123;&#125;

obj = <span class="hljs-number">24</span>
obj = <span class="hljs-string">'Ruovan'</span>

<span class="hljs-comment">// 报错</span>
obj = <span class="hljs-literal">null</span>
obj = <span class="hljs-literal">undefined</span>

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><code>object</code>表示常规的<code>JavaScript</code>对象类型，<strong>非基础类型</strong></p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">let</span> obj: <span class="hljs-built_in">object</span>

obj = &#123;&#125;
obj = []

<span class="hljs-comment">// 报错</span>
obj = <span class="hljs-number">24</span>
obj = <span class="hljs-string">'Ruovan'</span>
obj = <span class="hljs-literal">null</span>
obj = <span class="hljs-literal">undefined</span>

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p><code>Object</code>表示同<code>&#123;&#125;</code>表现一致，区别是 <code>Object</code> 类型会对 <code>Object</code> 原型内置的方法（<code>toString/hasOwnPreperty</code>）进行校验</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">let</span> obj: <span class="hljs-built_in">Object</span>

obj = <span class="hljs-number">24</span>
obj = <span class="hljs-string">'Ruovan'</span>

<span class="hljs-comment">// 报错</span>
obj = <span class="hljs-literal">null</span>
obj = <span class="hljs-literal">undefined</span>

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h3 data-id="heading-5">接口</h3>
<h4 data-id="heading-6">（1）概念</h4>
<ul>
<li>
<p>使用接口<code>interface</code>来定义<strong>对象的类型</strong></p>
</li>
<li>
<p>接口是对象的<strong>状态</strong>（属性）和<strong>行为</strong>（方法）的<strong>抽象</strong>（描述）</p>
</li>
</ul>
<h4 data-id="heading-7">（2）写法</h4>
<ul>
<li>
<p>接口的首字母大写</p>
</li>
<li>
<p>定义的变量的属性类型<strong>必须和接口一致</strong>，否则就会报错</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// 定义一个接口，通常接口首字母大写</span>
<span class="hljs-keyword">interface</span> Person &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span>;
    age: <span class="hljs-built_in">number</span>;
&#125;

<span class="hljs-comment">// 定义一个变量，变量类型是 Person，且必须和 Person 内的类型一致</span>
<span class="hljs-keyword">let</span> person1: Person = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'Ruovan'</span>,
    <span class="hljs-attr">age</span>: <span class="hljs-number">24</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-8">（3）属性</h4>
<blockquote>
<p>当然，和接口不一致也是可以的，但是需要再对接口作一些额外的配置</p>
</blockquote>
<ul>
<li>
<p>确定属性：不需要添加标识符，且该属性必须有</p>
</li>
<li>
<p>可选属性：使用<code>?</code>标识符来定义可选属性，表示当前属性<strong>可有可无</strong></p>
</li>
<li>
<p>只读属性：使用<code>readonly</code>标识符来定义只读属性，表示当前属性<strong>只能在创建时</strong>赋值，且<strong>赋值后不可更改</strong></p>
</li>
<li>
<p>任意属性：使用<code>[propName: string]</code>定义任意属性，表示可以传递任何属性</p>
<ul>
<li>其中属性<code>key</code>类型为<code>string</code>，值<code>value</code>类型可以定义为<code>any</code></li>
<li>即：<code>[propName: string]: any</code>，可以接受任意类型的参数</li>
</ul>
<blockquote>
<p>注意：值<code>value</code>的类型需要同时符合<strong>确定属性和可选属性</strong>的类型，所以最好用<code>any</code>定义类型</p>
</blockquote>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// 定义接口： 属性名:类型</span>
<span class="hljs-keyword">interface</span> Person &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-built_in">string</span> <span class="hljs-comment">// 确定属性</span>
    sex?: <span class="hljs-built_in">string</span> <span class="hljs-comment">// 可选属性 ?</span>
    <span class="hljs-keyword">readonly</span> idCard: <span class="hljs-built_in">number</span> <span class="hljs-comment">// 只读属性 readonly</span>
    [propName: <span class="hljs-built_in">string</span>]: <span class="hljs-built_in">any</span> <span class="hljs-comment">// 任意属性 [propName]</span>
&#125;

<span class="hljs-comment">// 创建实例</span>
<span class="hljs-comment">// 类型检查器会查看对象内部的属性是否与Person接口描述一致, 如果不一致就会提示类型错误</span>
<span class="hljs-keyword">const</span> person1: Person = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'ruovan'</span>, <span class="hljs-comment">// 必须有</span>
    <span class="hljs-attr">sex</span>: <span class="hljs-string">'male'</span>, <span class="hljs-comment">// 可有可无</span>
    <span class="hljs-attr">idCard</span>: <span class="hljs-number">123</span>, <span class="hljs-comment">// 只读，无法更改</span>
    <span class="hljs-attr">age</span>: <span class="hljs-number">24</span>, <span class="hljs-comment">// 任意属性</span>
    <span class="hljs-attr">isDead</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-attr">address</span>: <span class="hljs-string">'earth'</span>
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h4 data-id="heading-9">（4）函数类型</h4>
<ul>
<li>
<p>接口也可以描述函数类型，需要给接口定义一个调用签名</p>
<ul>
<li>这个签名是一个<strong>只有参数列表</strong>和<strong>返回值类型</strong>的<strong>函数定义</strong></li>
<li>参数列表里的每个参数都需要<strong>名字和类型</strong></li>
</ul>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// 函数接口</span>
<span class="hljs-keyword">interface</span> SearchFunc &#123;
    (source: <span class="hljs-built_in">string</span>, <span class="hljs-attr">subString</span>: <span class="hljs-built_in">string</span>): <span class="hljs-built_in">boolean</span>
&#125;

<span class="hljs-comment">// 使用接口</span>
<span class="hljs-keyword">const</span> mySearch: SearchFunc = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">source: <span class="hljs-built_in">string</span>, sub: <span class="hljs-built_in">string</span></span>): <span class="hljs-title">boolean</span> </span>&#123;
    <span class="hljs-keyword">return</span> source.search(sub) > -<span class="hljs-number">1</span>
&#125;

<span class="hljs-built_in">console</span>.log(mySearch(<span class="hljs-string">'abcd'</span>, <span class="hljs-string">'bc'</span>))

<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<hr>
<p><del>本人前端小菜鸡，如有不对请谅解</del></p></div>  
</div>
            