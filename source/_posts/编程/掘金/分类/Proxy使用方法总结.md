
---
title: 'Proxy使用方法总结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1384'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 01:34:04 GMT
thumbnail: 'https://picsum.photos/400/300?random=1384'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">Proxy 可以对目标对象的读取、函数调用等操作进行代理拦截，然后进行操作处理。它不直接操作对象，而是像代理模式，通过对象的代理对象进行操作，在进行这些操作时，可以添加一些需要的额外操作。主要有这几种情况：</h4>
<ol>
<li>获取对象属性</li>
<li>设置对象属性值</li>
<li>遍历对象</li>
<li>判断对象是否有对应属性</li>
<li>删除对象属性</li>
<li>函数调用，call和apply的时候</li>
<li>new 命令</li>
</ol>
<h4 data-id="heading-1">基本用法</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> obj = &#123;<span class="hljs-attr">name</span>:<span class="hljs-string">'dylan'</span>&#125;
<span class="hljs-keyword">let</span> myproxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(obj,&#123;&#125;) 
<span class="hljs-comment">//两个参数，第一个是要代理的目标，如obj对象，第二个是一个对象，里面放需要进行的拦截操作，为空时表示不进行拦截操作</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">get(target, prop)</h4>
<p>当对象属性被获取时进行拦截，
在proxy的第二个参数对象里面添加get方法来进行拦截操作(后面的方法也是)，参数target表示代理的对象，prop表示传递的属性名(参数名可以自定义)</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> obj = &#123;<span class="hljs-attr">name</span> : <span class="hljs-string">'dylan'</span>&#125;
obj = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(obj,&#123; <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">target,prop</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(target,prop)   <span class="hljs-comment">//这里我们可以在对象被获取前写一些代码</span>
    <span class="hljs-keyword">return</span> target[prop]        <span class="hljs-comment">// return的值就是对象属性被获取的值，没有return值会报undefined</span>
&#125; &#125;)
 例如: 执行<span class="hljs-built_in">console</span>.log(obj.name)时，对象name属性就被获取，会执行proxy的get函数
 <span class="hljs-comment">//代理数组例子</span>
 <span class="hljs-keyword">let</span> arr = [<span class="hljs-number">5</span>,<span class="hljs-number">6</span>,<span class="hljs-number">7</span>]
 arr = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(arr,&#123;
      <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">target,prop</span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(target,prop)
        <span class="hljs-keyword">return</span> prop <span class="hljs-keyword">in</span> target ? target[prop] : <span class="hljs-string">'err'</span>
      &#125;
&#125;)
<span class="hljs-built_in">console</span>.log(arr[<span class="hljs-number">2</span>])
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">set(target, props, val)</h4>
<p>当对象属性值被设置的时拦截，target表示代理的对象，props表示属性名，val表示要设置的值。set需要返回一个布尔值。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> obj = &#123;<span class="hljs-attr">name</span> : <span class="hljs-string">'Dylan'</span>&#125;
obj = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(obj, &#123;
  <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">target, props,val</span>)</span>&#123;
    <span class="hljs-built_in">console</span>.log(target,props,val) <span class="hljs-comment">//target是obj对象,props是传递进来的'name'属性，val是'newName'</span>
    target[props] = val  <span class="hljs-comment">// 这里是对值的设置，如果设置成 target[props] = 'hhh',那么设置的也会是hhh</span>
    <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
  &#125;
&#125;)
obj.name = <span class="hljs-string">'newName'</span>  <span class="hljs-comment">// 对象属性值进行设置</span>
<span class="hljs-built_in">console</span>.log(obj.name)  <span class="hljs-comment">// 打印'newName' </span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-4">has(target, prop)</h4>
<p>判断对象是否有某个属性时进行的拦截操作。target、prop分别表示代理的对象和传递的属性名。需要返回一个布尔值。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> range = &#123;
  <span class="hljs-attr">start</span>:<span class="hljs-number">1</span>,
  <span class="hljs-attr">end</span>:<span class="hljs-number">5</span>
&#125;
range = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(range,&#123;
  <span class="hljs-function"><span class="hljs-title">has</span>(<span class="hljs-params">target,prop</span>)</span>&#123;
   <span class="hljs-keyword">return</span> prop >=target.start && prop <= target.end
  &#125;
&#125;)
<span class="hljs-built_in">console</span>.log(<span class="hljs-number">0</span> <span class="hljs-keyword">in</span> range)  <span class="hljs-comment">// 0不在1和5之间，返回false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">ownKeys(target)</h4>
<p>当对象被遍历时进行的拦截操作。target表示代理的对象，返回的是一个数组。当我们使用Object.getOwnPropertyNames()、Object.getOwnPropertySymbol()、
Object.keys()、for...in 这些方法进行遍历时都会触发ownKeys方法。</p>
<pre><code class="hljs language-js copyable" lang="js">假如我们不想让对象的某个属性被遍历
<span class="hljs-keyword">let</span> userinfo = &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'dylan'</span>,
    <span class="hljs-attr">_password</span>: <span class="hljs-string">'123'</span>   <span class="hljs-comment">//我们不想让这个下划线开头的密码被遍历</span>
 &#125;
userinfo = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(userinfo,&#123;
   <span class="hljs-function"><span class="hljs-title">ownKeys</span>(<span class="hljs-params">target</span>)</span>&#123;
     <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.keys(target).filter(<span class="hljs-function"><span class="hljs-params">key</span> =></span> !key.startWith(<span class="hljs-string">'_'</span>)) <span class="hljs-comment">//过滤下划线开头的属性</span>
   &#125;
&#125;)
<span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Object</span>.keys(userinfo)) <span class="hljs-comment">// 只输出['name']</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-6">deleteProperty(target, prop)</h4>
<p>当删除对象的属性时进行的拦截操作。接收两个参数target、prop,分别指代理的对象、要删除的属性。返回一个布尔值。</p>
<pre><code class="hljs language-js copyable" lang="js">假如我们不想让对象的带下划线开头的属性被删除
<span class="hljs-keyword">let</span> obj = &#123;
    <span class="hljs-attr">name</span> : <span class="hljs-string">'dylan'</span>,
    <span class="hljs-attr">_password</span>: <span class="hljs-string">'123'</span>
&#125;
obj = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(obj,&#123;
    <span class="hljs-function"><span class="hljs-title">deleteProperty</span>(<span class="hljs-params">target,prop</span>)</span>&#123;
      <span class="hljs-keyword">if</span>(prop.startWith(<span class="hljs-string">'_'</span>))&#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'不可删除'</span>)
      &#125;<span class="hljs-keyword">else</span>&#123;
        <span class="hljs-keyword">delete</span> target[prop]
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
      &#125;
    &#125;
&#125;)

<span class="hljs-keyword">try</span>&#123;
  <span class="hljs-keyword">delete</span> obj._password
 &#125;<span class="hljs-keyword">catch</span>(e)&#123; <span class="hljs-built_in">console</span>.log(e.message) &#125;   <span class="hljs-comment">//删除失败，会打印'不可删除'</span>



<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-7">apply(target, ctx, args)</h4>
<p>用于拦截函数的调用、call 和 reply 操作。target 表示目标对象，ctx 表示目标对象上下文，args 表示目标对象的参数数组。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">sub</span>(<span class="hljs-params">a, b</span>)</span>&#123;
    <span class="hljs-keyword">return</span> a - b;
&#125;
sub = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(sub,&#123;
  <span class="hljs-function"><span class="hljs-title">apply</span>(<span class="hljs-params">target,ctx,args</span>)</span>&#123;
   <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'apply'</span>)
   <span class="hljs-keyword">return</span>  target(...args)*<span class="hljs-number">2</span>;   <span class="hljs-comment">//例如代理后把函数执行结果乘2</span>
  &#125;
&#125;)
<span class="hljs-built_in">console</span>.log(sub(<span class="hljs-number">5</span>,<span class="hljs-number">2</span>))  <span class="hljs-comment">//打印6</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">construct(target, args)</h4>
<p>用于拦截 new 命令。返回值必须为对象。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Exam</span> </span>&#123; 
  <span class="hljs-title">constructor</span> (<span class="hljs-params">name</span>) &#123;  
      <span class="hljs-built_in">this</span>.name = name 
  &#125;
&#125;
<span class="hljs-keyword">let</span> ExamProxy = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(Exam, &#123;
  <span class="hljs-function"><span class="hljs-title">construct</span>(<span class="hljs-params">target, args, newTarget</span>)</span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'construct'</span>)
  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> target(...args) 
&#125;&#125;)
<span class="hljs-built_in">console</span>.log(<span class="hljs-keyword">new</span> ExamProxy(<span class="hljs-string">'dylan'</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">综合例子</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">let</span> obj = &#123;
   <span class="hljs-attr">name</span>:<span class="hljs-string">'dylan'</span>,
   <span class="hljs-attr">age</span>:<span class="hljs-number">18</span>,
   <span class="hljs-attr">_secret</span>:<span class="hljs-string">'123'</span>
&#125;
obj = <span class="hljs-keyword">new</span> <span class="hljs-built_in">Proxy</span>(obj, &#123;
   <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">target, prop</span>)</span>&#123; <span class="hljs-keyword">return</span> target[prop] &#125;,
   <span class="hljs-function"><span class="hljs-title">set</span>(<span class="hljs-params">target, prop, val</span>)</span>&#123; 
        target[prop] = val 
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span> 
       &#125;,
   <span class="hljs-function"><span class="hljs-title">has</span>(<span class="hljs-params">target,prop</span>)</span>&#123; <span class="hljs-keyword">return</span> prop <span class="hljs-keyword">in</span> target &#125;,
   <span class="hljs-function"><span class="hljs-title">ownKeys</span>(<span class="hljs-params">target</span>)</span>&#123; 
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">Object</span>.keys(target).filter(<span class="hljs-function"><span class="hljs-params">key</span> =></span> !key.startWith(<span class="hljs-string">'_'</span>)) &#125;)
   &#125;,
   <span class="hljs-function"><span class="hljs-title">deleteProperty</span>(<span class="hljs-params">target, prop</span>)</span>&#123;
        <span class="hljs-function"><span class="hljs-title">deleteProperty</span>(<span class="hljs-params">target,prop</span>)</span>&#123;
      <span class="hljs-keyword">if</span>(prop.startWith(<span class="hljs-string">'_'</span>))&#123;
        <span class="hljs-keyword">throw</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Error</span>(<span class="hljs-string">'不可删除'</span>)
      &#125;<span class="hljs-keyword">else</span>&#123;
        <span class="hljs-keyword">delete</span> target[prop]
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
      &#125;
   &#125;
&#125;)
<span class="hljs-built_in">console</span>.log(obj.name)       <span class="hljs-comment">// 触发get</span>
obj.age = <span class="hljs-number">17</span>                <span class="hljs-comment">// 触发set</span>
<span class="hljs-built_in">console</span>.log(<span class="hljs-string">'name'</span> <span class="hljs-keyword">in</span> obj)  <span class="hljs-comment">//触发has</span>
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> key <span class="hljs-keyword">in</span> obj) &#123;...&#125;   <span class="hljs-comment">// 触发ownKeys</span>
<span class="hljs-keyword">delete</span> obj.age              <span class="hljs-comment">// 触发deleteProperty</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            