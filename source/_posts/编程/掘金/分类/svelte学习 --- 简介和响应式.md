
---
title: 'svelte学习 --- 简介和响应式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9222'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 06:31:05 GMT
thumbnail: 'https://picsum.photos/400/300?random=9222'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">简介</h2>
<blockquote>
<p>Svelte 与诸如 React 和 Vue 等 JavaScript 框架类似，都是用来构建<code>响应式用户界面</code>的</p>
</blockquote>
<h3 data-id="heading-1">特点</h3>
<ol>
<li>
<p>有一个关键的区别：Svelte 在 <em>构建/编译阶段</em> 将你的应用程序转换为理想的 JavaScript 应用，而不是在 <em>运行阶段</em> 解释应用程序的代码。这意味着你不需要为框架所消耗的性能付出成本，并且在应用程序首次加载时没有额外损失 ---- svelte更类似于编译器</p>
</li>
<li>
<p>可以使用 Svelte 构建整个应用程序，也可以逐步将其融合到现有的代码中。你还可以将组件作为独立的包（package）交付到任何地方，并且不会有传统框架所带来的额外开销 --- svelte是响应式的</p>
</li>
<li>
<p>Svelte 中，应用程序由一个或多个 <em>组件（components）</em> 构成。组件是一个可重用的、自包含的代码块，它将 HTML、CSS 和 JavaScript 代码封装在一起并写入 <code>.svelte</code> 后缀名的文件中。</p>
</li>
</ol>
<h3 data-id="heading-2">数据绑定</h3>
<p><code>绑定值</code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 声明状态和方法的区域 --></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">let</span> ctx = <span class="hljs-string">'Svelte'</span>
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-comment"><!-- 用户界面描述区域 --></span>
<span class="hljs-comment"><!-- 可以使用&#123;&#125;的方式绑定对象 --></span>
<span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Hello &#123;ctx&#125;!<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
<span class="hljs-comment"><!-- &#123;&#125;中支持所有合法的js表达式 --></span>
<span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Hello &#123;ctx.toUpperCase()&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>绑定属性</code></p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">let</span> src = <span class="hljs-string">'tutorial/image.gif'</span>;
  <span class="hljs-keyword">let</span> action = <span class="hljs-string">'dance'</span>
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-comment"><!--
在svelte中为了保证视力或行动受限的用户，或者没有强大硬件或良好互联网连接的用户具有良好的用户体验
svelte会通过警告的方式要求开发者尽可能提升标签的可访问性(Accessibility，缩写为 a11y),
例如此处的alt属性
--></span>

<span class="hljs-comment"><!-- 可以使用&#123;&#125;语法来绑定属性值 --></span>
<span class="hljs-comment"><!-- 可以是属性值整体为变量或者仅仅只是值的一部分 --></span>
<span class="hljs-tag"><<span class="hljs-name">img</span> <span class="hljs-attr">src</span>=<span class="hljs-string">&#123;src&#125;</span> <span class="hljs-attr">alt</span>=<span class="hljs-string">"a man &#123;action&#125;"</span>></span>

<span class="hljs-comment"><!-- 如果属性值和属性名一直，可以省略属性名直接使用属性值 --></span>
<span class="hljs-tag"><<span class="hljs-name">img</span> &#123;<span class="hljs-attr">src</span>&#125; <span class="hljs-attr">alt</span>=<span class="hljs-string">"a man &#123;action&#125;"</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">绑定样式</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 设置样式的部分 --></span>
<span class="hljs-comment"><!-- 在style中设置的样式，默认是局部样式，也就是尽在当前组件内部生效 --></span>
<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
  <span class="hljs-selector-tag">p</span> &#123;
    <span class="hljs-attribute">color</span>: blue;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="hljs-tag"><<span class="hljs-name">p</span>></span>This is a paragraph.<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">引入子组件</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-comment">// 引入组件，在svelte中，引入的组件不需要注册，直接就可以使用</span>
  <span class="hljs-keyword">import</span> Nested <span class="hljs-keyword">from</span> <span class="hljs-string">'./Nested.svelte'</span>
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">style</span>></span><span class="css">
  <span class="hljs-selector-tag">p</span> &#123;
    <span class="hljs-attribute">color</span>: purple;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">style</span>></span>

<span class="hljs-tag"><<span class="hljs-name">p</span>></span>This is a paragraph.<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="hljs-comment"><!-- 组件的首字母需要大写，以便于和一般HTML标签进行区分 --></span>
<span class="hljs-tag"><<span class="hljs-name">Nested</span> /></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">@html</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">let</span> string = <span class="hljs-string">`this string contains some <strong>HTML!!!</strong>`</span>;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-comment"><!-- @html只是对输出内容中html部分进行展示，对数据不会转换，所以可能会遇到XSS攻击 --></span>

<span class="hljs-comment"><!-- this string contains some <strong>HTML!!!</strong> --></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;string&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>

<span class="hljs-comment"><!-- @html === v-html  --></span>
<span class="hljs-comment"><!-- this string contains some HTML!!! --></span>
<span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;@html string&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">创建应用程序</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">'./App.svelte'</span>;

<span class="hljs-comment">// 编译器将每个组件转换为常规的 JavaScript 类,所以使用的时候，我们通过new来初始化对应的实例对象即可</span>
<span class="hljs-keyword">const</span> app = <span class="hljs-keyword">new</span> App(&#123;
  <span class="hljs-comment">// 挂载点</span>
<span class="hljs-attr">target</span>: <span class="hljs-built_in">document</span>.body,
<span class="hljs-attr">props</span>: &#123;
<span class="hljs-comment">// 传递给App组件的属性</span>
<span class="hljs-attr">answer</span>: <span class="hljs-number">42</span>
&#125;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">响应式</h2>
<blockquote>
<p>Svelete 的内核是一个强大的 <em>（反应性）reactivity</em> 系统，能够让 DOM 与你的应用程序状态保持同步</p>
<ol>
<li>状态发生改变的时候，自动更新界面</li>
<li>当界面对应的事件被触发的时候，自动去寻找预先声明好的方法，并执行对应的逻辑</li>
</ol>
</blockquote>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>;

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// 在svelte中，如果执行了赋值语句   </span>
    <span class="hljs-comment">// svelte会将对于的语句转换为一些特殊的代码，这些特殊的代码会通知svlete更新DOM </span>
    count += <span class="hljs-number">1</span>
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-comment"><!-- 使用on:事件名=&#123;事件处理函数&#125;的方式来绑定事件处理函数 --></span>
<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">on:click</span>=<span class="hljs-string">&#123;handleClick&#125;</span>></span>
  Clicked &#123;count&#125; &#123;count === 1 ? 'time' : 'times'&#125;
<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>;

  <span class="hljs-comment">// $：计算属性 = 对于的依赖关系表达式 </span>
  <span class="hljs-comment">// 这个依赖关系表达式中的外部依赖必须在响应式系统中，以便于svelte可以检测到外部依赖值的改变</span>
  <span class="hljs-comment">// 只有在外部依赖值改变的时候，计算属性才会改变，否则计算属性不会重新计算，直接使用之前已经计算出来的值</span>
  <span class="hljs-comment">// 计算属性会在组件被初始化的时候，就被调用  </span>
  $: doubled = count * <span class="hljs-number">2</span>

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>) </span>&#123;
    count += <span class="hljs-number">1</span>;
  &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">on:click</span>=<span class="hljs-string">&#123;handleClick&#125;</span>></span>
  add
<span class="hljs-tag"></<span class="hljs-name">button</span>></span>

<span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;count&#125; doubled is &#123;doubled&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>;
  <span class="hljs-comment">// svelte中不单单可以使用计算属性，还可以使用计算表达式 </span>
$: <span class="hljs-built_in">console</span>.log(count)

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>) </span>&#123;
count += <span class="hljs-number">1</span>;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">on:click</span>=<span class="hljs-string">&#123;handleClick&#125;</span>></span>
Clicked &#123;count&#125; &#123;count === 1 ? 'time' : 'times'&#125;
<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>;
  <span class="hljs-comment">// svelte中的计算属性可以是代码块</span>
$: &#123;
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'count'</span>, count)
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'doubled'</span>,count* <span class="hljs-number">2</span>)
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>) </span>&#123;
count += <span class="hljs-number">1</span>;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">on:click</span>=<span class="hljs-string">&#123;handleClick&#125;</span>></span>
Clicked &#123;count&#125; &#123;count === 1 ? 'time' : 'times'&#125;
<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>;
  <span class="hljs-comment">// 计算表达式后边甚至可以添加判断和循环依据</span>
$: <span class="hljs-keyword">if</span>(count %<span class="hljs-number">2</span> !== <span class="hljs-number">0</span>) &#123;
<span class="hljs-built_in">console</span>.log(count)
&#125;
  
 <span class="hljs-attr">$</span>: <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i< count; i++)&#123;
<span class="hljs-built_in">console</span>.log(i)
&#125;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>) </span>&#123;
count += <span class="hljs-number">1</span>;
&#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">on:click</span>=<span class="hljs-string">&#123;handleClick&#125;</span>></span>
Clicked &#123;count&#125; &#123;count === 1 ? 'time' : 'times'&#125;
<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">更新数组和对象</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">let</span> numbers = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>];

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addNumber</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// svelte中检测数据的变化触发响应式是通过赋值语句来执行的</span>
    <span class="hljs-comment">// 所以类似于push，pop，shift，unshift等方法会改变数组的值</span>
    <span class="hljs-comment">// 但是svelte无法通知界面更新DOM</span>
    numbers.push(numbers.length + <span class="hljs-number">1</span>);
  &#125;

  <span class="hljs-attr">$</span>: sum = numbers.reduce(<span class="hljs-function">(<span class="hljs-params">t, n</span>) =></span> t + n, <span class="hljs-number">0</span>);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;numbers.join(' + ')&#125; = &#123;sum&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>

<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">on:click</span>=<span class="hljs-string">&#123;addNumber&#125;</span>></span>
  Add a number
<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">let</span> numbers = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>];

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addNumber</span>(<span class="hljs-params"></span>) </span>&#123;
    numbers.push(numbers.length + <span class="hljs-number">1</span>);
    <span class="hljs-comment">// 解决方法1：将更新后的代码赋值给本身，以便于触发svelte的响应式系统</span>
    numbers = numbers
  &#125;

  <span class="hljs-attr">$</span>: sum = numbers.reduce(<span class="hljs-function">(<span class="hljs-params">t, n</span>) =></span> t + n, <span class="hljs-number">0</span>);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;numbers.join(' + ')&#125; = &#123;sum&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>

<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">on:click</span>=<span class="hljs-string">&#123;addNumber&#125;</span>></span>
  Add a number
<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">let</span> numbers = [<span class="hljs-number">1</span>, <span class="hljs-number">2</span>, <span class="hljs-number">3</span>, <span class="hljs-number">4</span>];

  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">addNumber</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-comment">// 这是更为通用的做法:</span>
    <span class="hljs-comment">// 原则是: 被更新的变量的名称必须出现在赋值语句的左侧</span>
    <span class="hljs-comment">// 赋值给数组和对象的属性（properties） </span>
    <span class="hljs-comment">//（例如，obj.foo += 1 或 array[i] = x）与对值本身进行赋值的方式相同</span>
    numbers = [...numbers, numbers.length + <span class="hljs-number">1</span>]
  &#125;

  <span class="hljs-attr">$</span>: sum = numbers.reduce(<span class="hljs-function">(<span class="hljs-params">t, n</span>) =></span> t + n, <span class="hljs-number">0</span>);
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;numbers.join(' + ')&#125; = &#123;sum&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>

<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">on:click</span>=<span class="hljs-string">&#123;addNumber&#125;</span>></span>
  Add a number
<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            