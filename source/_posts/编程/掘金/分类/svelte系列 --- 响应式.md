
---
title: 'svelte系列 --- 响应式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=506'
author: 掘金
comments: false
date: Thu, 15 Jul 2021 02:38:29 GMT
thumbnail: 'https://picsum.photos/400/300?random=506'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>所谓响应式(反应性)，对应React的状态或Vue的 data</p>
<p>在Svelte中，声明响应式变量和我们声明一个普通变量没有差别</p>
<p>只要在Svelte中声明一个变量，这个变量会被自动被认为是“状态”</p>
<p><code>当你改变它的值，所有引用的地方都会自动更新</code></p>
<p>简单来说： Svelte 代替我们去关注数据应该如何更新，使开发者以十分简单的方式去更新和处理 UI 数据</p>
</blockquote>
<h3 data-id="heading-0">触发响应式 --- 赋值</h3>
<blockquote>
<p>Svelte 核心是功能强大的<code>响应式系统</code>，用于使 DOM 与你的应用程序状态保持同步</p>
<p>赋值 --- 是触发 Svelte 响应式的核心，Svelte 编译器根据赋值来确定是否需要更新相应的值</p>
</blockquote>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-comment">// 定义了一个变量； 会自动识别为svelte的状态，加入svelte的响应式系统中 </span>
  <span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>;

   <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>) </span>&#123;
       <span class="hljs-comment">// 当svelte的状态发生改变的时候, 所有引用这个状态的地方，都会自动更新</span>
       <span class="hljs-comment">// Svelte 会针对赋值生成一些代码，以便于在状态发生改变的时候告诉 DOM 什么地方需要更新</span>
        count += <span class="hljs-number">1</span>
    &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>

<span class="hljs-comment"><!-- svelte通过on:事件名的方式来绑定事件 --></span>
<span class="hljs-comment"><!--
     注意: svelte的属性 引号可以省略 
     on:click="&#123;handleClick&#125;" <=> on:click=&#123;handleClick&#125;
--></span>
<span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">on:click</span>=<span class="hljs-string">&#123;handleClick&#125;</span>></span>
    Clicked &#123;count&#125; &#123;count === 1 ? 'time' : 'times'&#125;
<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">响应式声明</h3>
<blockquote>
<p>在某些时候，svelte中有些状态是依赖于其它状态的</p>
<p>当依赖的状态发生改变的时候，需要重新计算，以得出当前状态的最新结果</p>
<p>(其实这和vue中的计算属性是十分相似的)</p>
</blockquote>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
  <span class="hljs-keyword">let</span> count = <span class="hljs-number">0</span>;

  <span class="hljs-comment">// 我们使用 $: 的方式来进行响应式声明</span>
  <span class="hljs-comment">// 当依赖的状态count发生改变的时候，svlete会自动计算并更新doubled的值</span>
  <span class="hljs-comment">/*
注意：
            1. 响应式声明只能定义在顶层, 在其余部分定义是会报错的
            2. 定义响应式声明的变量的时候，不需要加var|let|const (此时svelte会自动为该变量进行定义和赋值)
*/</span>
  $: doubled = count * <span class="hljs-number">2</span>;
  
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">handleClick</span>(<span class="hljs-params"></span>) </span>&#123;
count += <span class="hljs-number">1</span>;
        <span class="hljs-comment">// $: doubled = count * 2; => error</span>
   &#125;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 和vue不同的时候，svlete的响应式声明即可以是变量，也可以是语句</span>

<span class="hljs-comment">// 语句</span>
<span class="hljs-attr">$</span>: <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`the count is <span class="hljs-subst">$&#123;count&#125;</span>`</span>);

<span class="hljs-comment">// 代码块</span>
$: &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">`the count is <span class="hljs-subst">$&#123;count&#125;</span>`</span>);
    alert(<span class="hljs-string">`I SAID THE COUNT IS <span class="hljs-subst">$&#123;count&#125;</span>`</span>);
&#125;

<span class="hljs-comment">// 逻辑语句</span>
<span class="hljs-attr">$</span>: <span class="hljs-keyword">if</span> (count >= <span class="hljs-number">10</span>) &#123;
    alert(<span class="hljs-string">`count is dangerously high!`</span>);
    count = <span class="hljs-number">9</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">检测响应式数据更新</h3>
<blockquote>
<p>svelete的响应式是由`赋值触发的</p>
<p>所以诸如 <code>push</code>、<code>splice</code> 等数组方法， 虽然更新了状态，但是因为没有赋值操作，所以不会引起UI(界面)的自动更新。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 这种语句是不起作用的</span>
numbers.push(numbers.length + <span class="hljs-number">1</span>);

<span class="hljs-comment">// 解决方法，赋值 --- 更新变量的名称，必须出现在赋值的左侧</span>

<span class="hljs-comment">// 1. 手动赋值（会出现多余的一行代码）</span>
numbers.push(numbers.length + <span class="hljs-number">1</span>);
numbers = numbers;

<span class="hljs-comment">// 2. 为对象（普通对象或数组）的属性赋值</span>
<span class="hljs-comment">// 例如 obj.foo += 1 或 array[i] = x，其实与直接赋值给自身的方式是一样的。</span>
numbers[numbers.length] = numbers.length + <span class="hljs-number">1</span>

<span class="hljs-comment">// 3. 展开运算符 --- 常用 --- 可以使用类似的办法来替代 pop、shift、unshift 和 splice</span>
numbers = [...numbers, numbers.length + <span class="hljs-number">1</span>]
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// svelte触发响应式更新的核心规则: 更新变量的名称，必须出现在赋值的左侧</span>
<span class="hljs-keyword">const</span> foo = obj.foo; foo.bar = <span class="hljs-string">'baz'</span>; <span class="hljs-comment">// => error 不会触发ui的更新，除非后面加上 obj = obj</span>
obj.foo.bar = <span class="hljs-string">'baz'</span>; <span class="hljs-comment">// => success 会触发ui的更新</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            