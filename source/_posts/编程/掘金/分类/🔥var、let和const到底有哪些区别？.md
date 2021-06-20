
---
title: '🔥var、let和const到底有哪些区别？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d79dbd1dd9da44b5aa7da5bc4241ee95~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 18 Jun 2021 07:48:35 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d79dbd1dd9da44b5aa7da5bc4241ee95~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><hr>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d79dbd1dd9da44b5aa7da5bc4241ee95~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>这是我参与更文挑战的第18天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
</blockquote>
<hr>
<blockquote>
<p>面试官：知道const、let和var吧，说说他们的区别吧</p>
<p>我：...💥</p>
</blockquote>
<hr>
<h4 data-id="heading-0">前言</h4>
<blockquote>
<p>可以说这是银行我们面试遇到的最高频的一个问题，也是一个很基础的问题了。所以，我们定然在这个问题上，不能讲不清楚，那就当场发感谢信了。🚀  当然，除此之外深入的还需要去了解一下const和let的实现原理。</p>
</blockquote>
<h4 data-id="heading-1">let</h4>
<p>let 关键字用来声明变量，使用 let 声明的变量有几个特点：</p>
<ol>
<li><code>不允许重复声明</code>；</li>
<li><code>块儿级作用域（局部变量）</code>；</li>
<li><code>不存在变量提升</code>；</li>
<li><code>不影响作用域链</code>；</li>
</ol>
<h5 data-id="heading-2">示例</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// let关键字使用示例：</span>
<span class="hljs-keyword">let</span> a; <span class="hljs-comment">// 单个声明</span>
<span class="hljs-keyword">let</span> b,c,d; <span class="hljs-comment">// 批量声明</span>
<span class="hljs-keyword">let</span> e = <span class="hljs-number">100</span> ; <span class="hljs-comment">// 单个声明并赋值</span>
<span class="hljs-keyword">let</span> f = <span class="hljs-number">521</span> , g = <span class="hljs-string">'iloveyou'</span>, h = []; <span class="hljs-comment">// 批量声明并赋值</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-3">不允许重复声明</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> dog = <span class="hljs-string">"狗"</span>;
<span class="hljs-keyword">let</span> dog = <span class="hljs-string">"狗"</span>;
<span class="hljs-comment">// 报错：Uncaught SyntaxError: Identifier 'dog' has already been</span>
declared
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-4">块儿级作用域（局部变量）</h5>
<pre><code class="hljs language-js copyable" lang="js">&#123;
<span class="hljs-keyword">let</span> cat = <span class="hljs-string">"猫"</span>;
<span class="hljs-built_in">console</span>.log(cat);
&#125;
<span class="hljs-built_in">console</span>.log(cat);
<span class="hljs-comment">// 报错：Uncaught ReferenceError: cat is not defined</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-5">不存在变量提升</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 什么是变量提升：就是在变量创建之前使用（比如输出：输出的是默认值），let不存在，var存在；</span>

<span class="hljs-built_in">console</span>.log(people1); <span class="hljs-comment">// 可输出默认值</span>
<span class="hljs-built_in">console</span>.log(people2); <span class="hljs-comment">// 报错：Uncaught ReferenceError: people2 is not defined</span>
<span class="hljs-keyword">var</span> people1 = <span class="hljs-string">"大哥"</span>; <span class="hljs-comment">// 存在变量提升</span>
<span class="hljs-keyword">let</span> people2 = <span class="hljs-string">"二哥"</span>; <span class="hljs-comment">// 不存在变量提升</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-6">不影响作用域链：</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 什么是作用域链：很简单，就是代码块内有代码块，跟常规编程语言一样，上级代码块中的局部变量下级可用</span>
&#123;
            <span class="hljs-keyword">let</span> p = <span class="hljs-string">"大哥"</span>;
<span class="hljs-keyword">var</span> s;               <span class="hljs-comment">//p的作用域是块(花括号内)级的，而s的作用域为函数作用域全局</span>
            <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">fn</span>(<span class="hljs-params"></span>) </span>&#123;
                <span class="hljs-built_in">console</span>.log(p); <span class="hljs-comment">// 这里是可以使用的</span>
            &#125;
            fn();
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-7">应用场景</h5>
<p><code>以后声明变量使用 let 就对了</code>；</p>
<h5 data-id="heading-8">let案例：点击div更改颜色</h5>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-comment">// 获取div元素对象</span>
        <span class="hljs-keyword">let</span> items = <span class="hljs-built_in">document</span>.getElementsByClassName(<span class="hljs-string">'item'</span>);


        <span class="hljs-comment">//ES5错误解法</span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < items.length; i++) &#123;
            items[i].onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                items[i].style.background = <span class="hljs-string">'pink'</span>; 
                alert(<span class="hljs-string">'点击了'</span> + i + <span class="hljs-string">'个'</span>)
            &#125;
            <span class="hljs-comment">// 由于点击事件是异步的，i又是全局的，所以每个item用的i都是同一个i。</span>

        &#125;
        <span class="hljs-comment">//ES5解法1</span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < items.length; i++) &#123;
            items[i].onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                <span class="hljs-built_in">this</span>.style.background = <span class="hljs-string">'pink'</span>; <span class="hljs-comment">// 写法一：常规写法一般无异常</span>
                alert(<span class="hljs-string">'点击了'</span> + i + <span class="hljs-string">'个'</span>)
            &#125;
        &#125;
        <span class="hljs-comment">//ES5解法1</span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">0</span>; i < items.length; i++) &#123;
            <span class="hljs-comment">//使用闭包，控制作用域</span>
            (<span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">i</span>) </span>&#123;
                items[i].onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                    items[i].style.background = <span class="hljs-string">'pink'</span>; <span class="hljs-comment">// 写法二</span>
                    alert(<span class="hljs-string">'点击了'</span> + i + <span class="hljs-string">'个'</span>)
                &#125;
            &#125;)(i)
        &#125;
        
        <span class="hljs-comment">// ES6解法</span>
        <span class="hljs-keyword">for</span> (<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < items.length; i++) &#123;

            items[i].onclick = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                <span class="hljs-comment">// 修改当前元素的背景颜色</span>
                <span class="hljs-comment">// this.style.background = 'pink'; // 写法一：常规写法一般无异常</span>
                items[i].style.background = <span class="hljs-string">'pink'</span>; <span class="hljs-comment">// 写法二</span>
                <span class="hljs-comment">// 写法二：需要注意的是for循环内的i必须使用let声明 //点击事件是异步的</span>
                <span class="hljs-comment">// 如果使用var就会报错，因为var是全局变量，</span>
                <span class="hljs-comment">// 经过循环之后i的值会变成3，items[i]就会下标越界</span>
                <span class="hljs-comment">// let是局部变量</span>
                <span class="hljs-comment">// 我们要明白的是当我们点击的时候，这个i是哪个值</span>
                <span class="hljs-comment">// 下面的声明会将上面的覆盖掉，所以点击事件每次找到的都是3</span>
                <span class="hljs-comment">// 由于let声明的是局部变量，每一个保持着原来的值</span>
                <span class="hljs-comment">// 点击事件调用的时候拿到的是对应的i</span>
            &#125;

        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">const</h4>
<p>const 关键字用来声明 <strong>常量</strong> ，const 声明有以下特点：</p>
<ol>
<li><code>声明必须赋初始值</code>·；</li>
<li><code>标识符一般为大写（习惯</code>）；</li>
<li><code>不允许重复声明</code>；</li>
<li><code>值不允许修改</code>；</li>
<li><code>块儿级作用域（局部变量）</code>；</li>
</ol>
<p><code>注:</code>当常量为对象时，<code>值不允许修改</code>含义是指向的对象不能修改，但是可以改变对象内部的属性</p>
<h5 data-id="heading-10">示例</h5>
<pre><code class="hljs language-js copyable" lang="js">        <span class="hljs-comment">// const声明常量</span>
        <span class="hljs-keyword">const</span> DOG = <span class="hljs-string">"旺财"</span>;
        <span class="hljs-built_in">console</span>.log(DOG);
        <span class="hljs-comment">// 1. 声明必须赋初始值；</span>
        <span class="hljs-comment">// const CAT;</span>
        <span class="hljs-comment">// 报错：Uncaught SyntaxError: Missing initializer in const  declaration</span>
        
        <span class="hljs-comment">// 2. 标识符一般为大写（习惯）；</span>
        <span class="hljs-comment">// const dog = "旺财"; // 小写也不错</span>
        
        <span class="hljs-comment">// 3. 不允许重复声明；</span>
        <span class="hljs-comment">// const CAT = "喵喵";</span>
        <span class="hljs-comment">// const CAT = "喵喵";</span>
        <span class="hljs-comment">// 报错：Uncaught SyntaxError: Identifier 'CAT' has already been declared</span>
        
       <span class="hljs-comment">//  注意：对数组元素的修改和对对象内部的修改是可以的（数组和对象存的是引用地址）；</span>
        <span class="hljs-comment">// 4. 值不允许修改；</span>
        <span class="hljs-comment">// const CAT = "喵喵";</span>
        <span class="hljs-comment">// CAT = "咪咪";</span>
        <span class="hljs-comment">// 特例：const arr = ['55','66'];</span>
        <span class="hljs-comment">// arr.push('77');  //arr的中已经接上了‘77’ 这是因为arr指向的地址并没有发生改变</span>
        <span class="hljs-comment">// 报错：Uncaught TypeError: Assignment to constant variable.</span>
        
        <span class="hljs-comment">// 5. 块儿级作用域（局部变量）；</span>
        <span class="hljs-comment">// &#123;</span>
        <span class="hljs-comment">// const CAT = "喵喵";</span>
        <span class="hljs-comment">// console.log(CAT);</span>
        <span class="hljs-comment">// &#125;</span>
        <span class="hljs-comment">// console.log(CAT);</span>
        <span class="hljs-comment">// 报错：Uncaught ReferenceError: CAT is not defined</span>
  
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-11">应用场景：</h5>
<p><code>声明对象类型使用 const，非对象类型声明选择 let；</code></p>
<h4 data-id="heading-12">var、let和const的区别</h4>
<ol>
<li>
<p>var定义的变量，没有块的概念，可以<code>跨块访问</code>, <code>不能跨函数访问.</code> <code>并不是全局作用域</code></p>
</li>
<li>
<p>let定义的变量，只能在块作用域里访问，不能跨块访问，也不能跨函数访问。</p>
</li>
<li>
<p>const用来定义常量，使用时<code>必须初始化</code>(即必须赋值)，只能在块作用域里访问，而且不能修改。</p>
</li>
<li>
<p>var声明的变量存在<code>变量提升现象</code>，let和const声明的变量不存在变量提升现象（遵循：“先声明，后使用”的原则，否则会报错）。</p>
</li>
<li>
<p>var不存在暂时性死区，let和const存在暂时性死区。</p>
<p>解析：只要块级作用域内存在let命令，那么它所声明的变量就会绑定到这个区域，不再受外部的影响。</p>
</li>
<li>
<p>var允许重复声明同一个变量，let和const在同一作用域下不允许重复声明同一个变量。</p>
<p>解析：var允许重复声明变量，后一个变量会覆盖前一个变量，const和let会报错。</p>
</li>
</ol></div>  
</div>
            