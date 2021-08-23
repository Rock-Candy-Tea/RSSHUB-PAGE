
---
title: '8月更文挑战 _ 前端Js手写题汇总（二）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5424'
author: 掘金
comments: false
date: Sun, 22 Aug 2021 08:13:21 GMT
thumbnail: 'https://picsum.photos/400/300?random=5424'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第7天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h3 data-id="heading-0">复习一下上一篇文章的一些代码</h3>
<ul>
<li>防抖：<code>最后一次</code>触发事件<code>N秒</code>内<code>未重新触发</code>才执行程序，否则<code>重新计时</code></li>
<li>节流：<code>N秒</code>内仅触发一次事件</li>
<li>简单判断类型：<code>typeof</code>无法正常判断<code>null</code>且引用类型仅能正确判断<code>Function</code>，<code>instancof</code>仅能正常判断引用类型，最佳方法：<code>Object.prototype.toString.call(arg)</code></li>
<li>浅拷贝：完整拷贝某个对象的所有属性，对于拷贝后的基础数据类型，不会因为被拷贝对象属性的修改而受影响，而对于拷贝后的引用数据类型，会因为被拷贝对象属性的修改而受影响</li>
<li>深拷贝：完整拷贝某个对象的所有属性，对于拷贝后的引用数据类型，会开辟一个新的内存空间用于存储，因此不会因为拷贝对象属性的修改而受到影响</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//防抖</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">debounce</span>(<span class="hljs-params">func,wait</span>)</span>&#123;
    <span class="hljs-keyword">let</span> timer = <span class="hljs-literal">null</span>;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">if</span>(!timer) <span class="hljs-built_in">clearTimeout</span>(timer);
        timer = <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
            func.call(<span class="hljs-built_in">this</span>,<span class="hljs-built_in">arguments</span>)
        &#125;,wait)
    &#125;
&#125;
<span class="hljs-comment">//节流</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">throttle</span>(<span class="hljs-params">func,delay</span>)</span>&#123;
    <span class="hljs-keyword">let</span> canRun = <span class="hljs-literal">true</span>
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">if</span>(!canRun) <span class="hljs-keyword">return</span>;
        canRun = <span class="hljs-literal">false</span>;
        <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
            func.call(<span class="hljs-built_in">this</span>,<span class="hljs-built_in">arguments</span>);
            canRun = <span class="hljs-literal">true</span>;
        &#125;,delay)
    &#125;
&#125;
<span class="hljs-comment">//节流新</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">throttle</span>(<span class="hljs-params">func,wait</span>)</span>&#123;
    <span class="hljs-keyword">let</span> pre = <span class="hljs-number">0</span>;
    <span class="hljs-keyword">return</span> <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">let</span> now = <span class="hljs-built_in">Date</span>.now();
        <span class="hljs-keyword">if</span>(now-pre>wait)&#123;
            func.call(<span class="hljs-built_in">this</span>,<span class="hljs-built_in">arguments</span>)
            pre = now;
        &#125;
    &#125;
&#125;
<span class="hljs-comment">//简单判断类型</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">getType</span>(<span class="hljs-params">arg</span>)</span>&#123;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.prototype.toString.call(arg).slice(<span class="hljs-number">8</span>,-<span class="hljs-number">1</span>).toLowerCase();
&#125;
<span class="hljs-comment">/*
    拷贝
*/</span>
<span class="hljs-keyword">var</span> person = &#123;
    <span class="hljs-string">"name"</span>:<span class="hljs-string">"tony"</span>,
    <span class="hljs-string">"age"</span>:<span class="hljs-number">21</span>,
    <span class="hljs-string">"tech"</span>:&#123;
        <span class="hljs-string">"react"</span>:<span class="hljs-literal">false</span>
    &#125;
&#125;
<span class="hljs-comment">//浅拷贝</span>
<span class="hljs-keyword">let</span> personCopy1 = <span class="hljs-built_in">Object</span>.assign(&#123;&#125;,person)  <span class="hljs-comment">//Object.assign方法</span>
<span class="hljs-keyword">let</span> personCopy2 = &#123;...person&#125;  <span class="hljs-comment">//ES6展开法</span>
<span class="hljs-comment">//深拷贝</span>
<span class="hljs-keyword">let</span> personCopy3 = <span class="hljs-built_in">JSON</span>.parse(<span class="hljs-built_in">JSON</span>.stringify(person)) <span class="hljs-comment">//JSON.parse(JSON.stringify(obj))方法</span>
<span class="hljs-comment">//递归深拷贝法</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">deepClone</span>(<span class="hljs-params">obj</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(<span class="hljs-keyword">typeof</span>(obj) !== <span class="hljs-string">'object'</span>) <span class="hljs-keyword">return</span>;
    <span class="hljs-keyword">var</span> newObj = obj <span class="hljs-keyword">instanceof</span> <span class="hljs-built_in">Array</span> ? []:&#123;&#125;;
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> key <span class="hljs-keyword">in</span> obj)&#123;
        <span class="hljs-keyword">if</span>(obj.hasOwnProperty(key))&#123;
            newObj[key] = <span class="hljs-keyword">typeof</span> obj[key] === <span class="hljs-string">'object'</span> ? deepClone(obj[key]) : obj[key];
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> newObj;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">第二篇内容</h3>
<h4 data-id="heading-2"><strong>1.继承</strong></h4>
<p>常用的两个继承方式：</p>
<ul>
<li>组合继承（原型链继承+构造函数继承）</li>
<li>寄生式组合继承（组合继承的改进，）</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
    方法一：组合继承
*/</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span>(<span class="hljs-params">age</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.age = age;
&#125;
Parent.prototype.sayAge = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.age);
&#125;
<span class="hljs-comment">//构造函数盗用,设置变量</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span>(<span class="hljs-params">age</span>)</span>&#123;
    Parent.call(<span class="hljs-built_in">this</span>,age)
&#125;
<span class="hljs-comment">//修改原型,继承方法</span>
Child.prototype = <span class="hljs-keyword">new</span> Parent();
<span class="hljs-comment">////////////////////////////////////////////////////////////</span>
<span class="hljs-comment">/*
    方法二：寄生式组合继承（组合继承的改进）
*/</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Parent</span>(<span class="hljs-params">age</span>)</span>&#123;
    <span class="hljs-built_in">this</span>.age = age;
&#125;
Parent.prototype.sayAge = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.age);
&#125;
<span class="hljs-comment">//构造函数盗用，设置变量</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Child</span>(<span class="hljs-params">age</span>)</span>&#123;
    Parent.call(<span class="hljs-built_in">this</span>,age);
&#125;
<span class="hljs-comment">//原型链修改</span>
<span class="hljs-keyword">const</span> prototype = object(Parent.prototype);
prototype.constructor = Child;
Child.prototype = prototype;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3"><strong>2.数组去重</strong></h4>
<p>方法：</p>
<ul>
<li>ES5 <code>filter</code></li>
<li>ES6 <code>Set</code></li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//ES5 filter</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">unique</span>(<span class="hljs-params">arr</span>)</span>&#123;
    <span class="hljs-keyword">var</span> res = arr.filter(<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">item,index,array</span>)</span>&#123;
        <span class="hljs-keyword">return</span> array.indexOf(item) === index
    &#125;)
    <span class="hljs-keyword">return</span> res;
&#125;
<span class="hljs-comment">//ES6 Set</span>
<span class="hljs-keyword">var</span> unique = <span class="hljs-function"><span class="hljs-params">arr</span> =></span> [...new <span class="hljs-built_in">Set</span>(arr)]
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4"><strong>3.数组扁平化</strong></h4>
<p>数组扁平化：将多维数组拍平成一维数组</p>
<p>方法：</p>
<ul>
<li>递归</li>
<li>ES6 array.some</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//ES5递归</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">flattern</span>(<span class="hljs-params">arr</span>)</span>&#123;
    <span class="hljs-keyword">var</span> array = [];
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i=<span class="hljs-number">0</span>;i<arr.length;i++)&#123;
        <span class="hljs-keyword">if</span>(arr[i].isArray)  array = array.concat( flattern(arr[i]) )
        <span class="hljs-keyword">else</span> array.push(arr[i])
    &#125;
    <span class="hljs-keyword">return</span> array
&#125;
<span class="hljs-comment">//ES6</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">flatten</span>(<span class="hljs-params">arr</span>) </span>&#123;
    <span class="hljs-keyword">while</span> (arr.some(<span class="hljs-function"><span class="hljs-params">item</span> =></span> <span class="hljs-built_in">Array</span>.isArray(item))) &#123;
        arr = [].concat(...arr);
    &#125;
    <span class="hljs-keyword">return</span> arr;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5"><strong>4.new</strong></h4>
<p>步骤：</p>
<ul>
<li>创建空对象</li>
<li>将对象原型进行指向</li>
<li>修改空对象上下文</li>
<li>返回空对象</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">newFunc</span>(<span class="hljs-params">Constructor,...args</span>)</span>&#123;
    <span class="hljs-keyword">var</span> obj = &#123;&#125;
    obj.__proto__ = Constructor.prototype
    Constructor.call(obj,args)
    <span class="hljs-keyword">return</span> obj
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            