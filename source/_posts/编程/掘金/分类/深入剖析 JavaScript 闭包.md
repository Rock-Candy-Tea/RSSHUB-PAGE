
---
title: '深入剖析 JavaScript 闭包'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4769'
author: 掘金
comments: false
date: Wed, 24 Mar 2021 01:30:48 GMT
thumbnail: 'https://picsum.photos/400/300?random=4769'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">🌞 深入剖析 JavaScript 闭包</h2>
<h3 data-id="heading-1">💎导读目录</h3>
<blockquote>
<ul>
<li>
<p>什么是闭包</p>
</li>
<li>
<p>闭包的特性</p>
</li>
<li>
<p>闭包的优缺点</p>
</li>
<li>
<p>闭包的作用</p>
</li>
<li>
<p>闭包的注意点</p>
</li>
</ul>
</blockquote>
<h3 data-id="heading-2">💎什么是闭包？</h3>
<blockquote>
<p>一个函数和对其周围状态的引用捆绑在一起,这样的组合就是<strong>闭包</strong>.</p>
<p>通俗的说： 一个内层函数可以访问外层函数的作用域 就叫 <strong>闭包</strong>。</p>
<p>在 JavaScript 中，每当创建一个函数，闭包就会在函数创建的同时被创建出来。</p>
<h4 data-id="heading-3">闭包的形成与变量的作用域以及变量的生存周期密切相关。</h4>
</blockquote>
<h3 data-id="heading-4">💎闭包的特性</h3>
<blockquote>
<ol>
<li>
<p>函数嵌套函数</p>
</li>
<li>
<p>函数内部可以引用外部的参数和变量</p>
</li>
<li>
<p>参数和变量不会被垃圾回收机制回收</p>
</li>
</ol>
</blockquote>
<h3 data-id="heading-5">💎闭包的优缺点</h3>
<blockquote>
<p>优点：</p>
<blockquote>
<p>可以设计私有的方法和变量</p>
</blockquote>
<p><strong>缺点</strong></p>
<blockquote>
<p>常驻内存，会增大内存使用量，使用不当很容易造成内存泄露。</p>
</blockquote>
<p><strong>一般函数执行完毕后，局部活动对象就被销毁，内存中仅仅保存全局作用域。</strong></p>
</blockquote>
<h3 data-id="heading-6">💎关于 变量</h3>
<h4 data-id="heading-7">变量的作用域</h4>
<blockquote>
<p>变量的作用域： 变量的有效范围。</p>
<p>在实际开发中，我们经常遇到的是 <strong>函数中声明的变量作用域。</strong></p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> a = <span class="hljs-string">'闭包'</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getValue</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">var</span> a = <span class="hljs-string">'函数局部作用域'</span>
    <span class="hljs-built_in">console</span>.log(a)
&#125;

getValue()  <span class="hljs-comment">//函数局部作用域</span>

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>当在全局声明了一个同名变量，在函数内部也声明了一个同名变量，函数优先访问函数作用域中的变量。</p>
</blockquote>
<h4 data-id="heading-8">函数作用域</h4>
<blockquote>
<p>函数作用域： 在函数内部可以访问到函数外部变量，而在函数外部的变量不可以访问函数内部的变量。</p>
<h4 data-id="heading-9">为什么呢？</h4>
<p><strong>因为当在函数中搜索一个变量的时候，如果函数内部没有这个变量的声明，那么它会随着代码的执行环境创建的作用域往外层逐层搜索，直到搜索到全局变量为止。</strong></p>
<p>变量的搜索是从内到外搜索的。</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getData</span>(<span class="hljs-params"></span>) </span>&#123;
    <span class="hljs-keyword">var</span> str = <span class="hljs-string">"闭包练习"</span>;
    <span class="hljs-keyword">var</span> fun = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">var</span> innerStr = <span class="hljs-string">'内部变量'</span>
    &#125;
    <span class="hljs-built_in">console</span>.log(innerStr) 
     <span class="hljs-comment">//innerStr is not defined 函数外层是访问不到 函数内层变量的</span>
&#125;
getData()
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">变量的生存周期</h4>
<blockquote>
<p>对于 <strong>全局变量</strong>，它的生存周期是永久的的，除非主动销毁变量。</p>
<p>而对于 <strong>函数局部变量</strong> ，当函数执行完毕，局部变量也就销毁了。</p>
</blockquote>
<h5 data-id="heading-11">栗子 1</h5>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-meta"><!DOCTYPE <span class="hljs-meta-keyword">html</span>></span>
<span class="hljs-tag"><<span class="hljs-name">html</span> <span class="hljs-attr">lang</span>=<span class="hljs-string">"en"</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"UTF-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">http-equiv</span>=<span class="hljs-string">"X-UA-Compatible"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"IE=edge"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">name</span>=<span class="hljs-string">"viewport"</span> <span class="hljs-attr">content</span>=<span class="hljs-string">"width=device-width, initial-scale=1.0"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span>Document<span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>1<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>2<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>3<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>4<span class="hljs-tag"></<span class="hljs-name">div</span>></span>

    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
        <span class="hljs-keyword">var</span> nodes = <span class="hljs-built_in">document</span>.getElementsByTagName(<span class="hljs-string">'div'</span>)
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < nodes.length; i++) &#123;
                nodes[i].onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                    alert(i)
                &#125;
        &#125;
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>给每个 <code> div</code> 增加点击事件，当点击 div 时，弹出它对应的索引值。</p>
<p>现在无论点击哪个 <code> div</code> ,它 弹出的 都是 4 。</p>
<h4 data-id="heading-12">为什么呢？</h4>
<p><strong>因为 div 点击事件 是被 异步触发的，当事件被触发的时候，循环已经执行完，此时的 i 的 变量值 为 4。</strong></p>
<h4 data-id="heading-13">如何解决 点击每个div 弹出对应的i 值呢 ？</h4>
<p>**可以借用 闭包， 把每次循环的 i 保存起来，当执行点击事件时，它会从内到外 搜索变量的作用域，它会优先搜索到 闭包环境环境的 i **</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"> # 闭包解决办法   
<script>
        <span class="hljs-keyword">var</span> nodes = <span class="hljs-built_in">document</span>.getElementsByTagName(<span class="hljs-string">'div'</span>)
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < nodes.length; i++) &#123;
            (<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">i</span>) </span>&#123;
                nodes[i].onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                    alert(i)
                &#125;
            &#125;)(i)
        &#125;
 </script>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-14">栗子 2</h5>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> num = <span class="hljs-number">1</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getValue</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">var</span> num = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        num++
        <span class="hljs-built_in">console</span>.log(num)
    &#125;
&#125;

<span class="hljs-keyword">var</span> s = getValue()
s()
s()
<span class="hljs-comment">// 1 2 </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>按常理思路来： 函数执行完毕，num = 1 销毁，变为初始值 num = 0 ，变量在函数中作用域从内到外逐层搜索。</p>
<p>前面也说到了，当函数执行完，局部变量也跟着销毁了，那为什么会 输出 2 呢 ？</p>
<blockquote>
<p>这里 涉及到 垃圾回收机制引用计数问题</p>
<p><a href="https://blog.csdn.net/zhouziyu2011/article/details/61201613" target="_blank" rel="nofollow noopener noreferrer">[关于垃圾回收] </a>  <a href="https://blog.csdn.net/zhouziyu2011/article/details/61201613" target="_blank" rel="nofollow noopener noreferrer">blog.csdn.net/zhouziyu201…</a></p>
<p>简述：</p>
<p><strong>当声明了一个变量并将一个引用类型值赋给该变量时，则该值的引用次数就是1；如果同一个值又被赋给另一个变量，则该值的引用次数加1；如果包含对该值引用的变量又取得了另外一个值，则该值的引用次数减1。当该值的引用次数变为0时，则可以回收其占用的内存空间。当垃圾回收器下一次运行时，就会释放那些引用次数为0的值所占用的内存。</strong></p>
</blockquote>
<p><strong>解答</strong></p>
<blockquote>
<p>第一次执行 <code> s()</code> 时，num = 1</p>
<p>第二次 执行 <code> s()</code> 时， 由于 引用的时第一次 <code> s ()</code> 的变量num=1，num 没有被销毁，固然在 num = 1 的基础上 再 加 1 。</p>
</blockquote>
<hr>
<p><strong>注意</strong></p>
<p>如果没有使用同样引用的话，那么多次调用，都是同样的值，因为没有记录引用值。</p>
<p>函数在执行完毕，num = 1 被销毁掉了，初始为 0</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> num = <span class="hljs-number">1</span>;
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getValue</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">var</span> num = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        num++
        <span class="hljs-built_in">console</span>.log(num)
    &#125;
&#125;

getValue()()
getValue()()
<span class="hljs-comment">// 0 0</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-15">💎闭包的作用</h3>
<blockquote>
<p>闭包的注意作用为这两项：</p>
<ol>
<li><strong>可以读取函数内部的变量</strong></li>
<li><strong>可以变量的值始终保持在内存中</strong></li>
</ol>
</blockquote>
<h4 data-id="heading-16">栗子</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f2</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">let</span> num = <span class="hljs-number">0</span>;
    addNum = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        num++
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">f3</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(num)
    &#125;
    <span class="hljs-keyword">return</span> f3
&#125;

<span class="hljs-keyword">var</span> a = f2()
a()
addNum()
a()
<span class="hljs-comment">// 0  1 </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p><code> 结果为 0  1</code></p>
<p>函数在执行完毕，局部变量也跟着销毁, 结果 不应该是  0  0 吗 ？</p>
<p>其实a() 相当于 是 f3() 的闭包函数，它被执行了两次。</p>
<ul>
<li>第一次 执行 a() 时， 结果为 0 ， 很好理解。</li>
<li>第二次   执行的 <code> f2()</code> 函数内部的 <code> addNum</code> 函数，发现没这个匿名函数赋值给一个变量，而且这个变量没加  <code> var / let</code> ， 那么它此时的作用域为 <code> 全局</code> ,保存在内存当中。执行<code> addNum</code> 时它访问的 <code> f2()</code> 函数内部的局部变量 <code> num</code> , 此时，<code> addNum</code> 的存在依赖于 <code>f2</code>，因此<code>f2</code> 也在内存中，不会在调用结束后，被垃圾回收机制（garbage collection）回收。</li>
<li>第三此  执行 <code> a()</code> 时， 因为<code> num</code> 已存在内存中，而至值为1</li>
</ul>
<p>最终输出结果： 0 ， 1</p>
</blockquote>
<p>​</p>
<h3 data-id="heading-17">💎闭包注意</h3>
<blockquote>
<ol>
<li>由于闭包会使得函数中的变量都被保存在内存中，内存消耗很大，所以不能滥用闭包，否则会造成网页的性能问题，在IE中可能导致内存泄露。解决方法是，在退出函数之前，将不使用的局部变量全部删除。</li>
<li>闭包会在父函数外部，改变父函数内部变量的值。所以，如果你把父函数当作对象（object）使用，把闭包当作它的公用方法（Public Method），把内部变量当作它的私有属性（private value），这时一定要小心，不要随便改变父函数内部变量的值。</li>
</ol>
</blockquote>
<h3 data-id="heading-18">结语</h3>
<blockquote>
<p>❤️关注+点赞+收藏+评论+转发❤️，原创不易，鼓励笔者创作更好的文章<br><br>关注公众号 “前端自学社区”，即可获取更多前端高质量文章！<br><br>关注后回复关键词“加群”， 即可加入 “前端自学交流群”，共同学习进步。<br><br>关注后添加我微信拉你进技术交流群<br><br>欢迎关注公众号，更多精彩文章只在公众号推送</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            