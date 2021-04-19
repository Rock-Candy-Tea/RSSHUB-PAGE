
---
title: 'JavaScript基础—循环'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b08029453e8a472cae76a92126e839df~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 18 Apr 2021 18:17:23 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b08029453e8a472cae76a92126e839df~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1 - 循环</h2>
<h3 data-id="heading-1">1.1 for循环</h3>
<ul>
<li>
<p>语法结构</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span>(初始化变量; 条件表达式; 操作表达式 )&#123;
    <span class="hljs-comment">//循环体</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>





















<table><thead><tr><th>名称</th><th>作用</th></tr></thead><tbody><tr><td>初始化变量</td><td>通常被用于初始化一个计数器，该表达式可以使用 var 关键字声明新的变量，这个变量帮我们来记录次数。</td></tr><tr><td>条件表达式</td><td>用于确定每一次循环是否能被执行。如果结果是 true 就继续循环，否则退出循环。</td></tr><tr><td>操作表达式</td><td>用于确定每一次循环是否能被执行。如果结果是 true 就继续循环，否则退出循环。</td></tr></tbody></table>
<p>执行过程：</p>
<ol>
<li>初始化变量，初始化操作在整个 for 循环只会执行一次。</li>
</ol>
</li>
<li>
<p>执行条件表达式，如果为true，则执行循环体语句，否则退出循环，循环结束。</p>
</li>
</ul>
<ol>
<li>执行操作表达式，此时第一轮结束。</li>
<li>第二轮开始，直接去执行条件表达式（不再初始化变量），如果为 true ，则去执行循环体语句，否则退出循环。</li>
<li>继续执行操作表达式，第二轮结束。</li>
<li>后续跟第二轮一致，直至条件表达式为假，结束整个 for 循环。</li>
</ol>
<p>断点调试：</p>
<pre><code class="copyable">断点调试是指自己在程序的某一行设置一个断点，调试时，程序运行到这一行就会停住，然后你可以一步一步往下调试，调试过程中可以看各个变量当前的值，出错的话，调试到出错的代码行即显示错误，停下。断点调试可以帮助观察程序的运行过程
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-html copyable" lang="html">断点调试的流程：
1、浏览器中按 F12--> sources -->找到需要调试的文件-->在程序的某一行设置断点
2、Watch: 监视，通过watch可以监视变量的值的变化，非常的常用。
3、摁下F11，程序单步执行，让程序一行一行的执行，这个时候，观察watch中变量的值的变化。
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>for 循环重复相同的代码</p>
<p>比如输出10句“媳妇我错了”</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//  基本写法</span>
<span class="hljs-keyword">for</span>(<span class="hljs-keyword">var</span> i = <span class="hljs-number">1</span>; i <= <span class="hljs-number">10</span>; i++)&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'媳妇我错了~'</span>);
&#125;
<span class="hljs-comment">// 用户输入次数</span>
<span class="hljs-keyword">var</span> num = prompt(<span class="hljs-string">'请输入次数:'</span>)；
<span class="hljs-keyword">for</span> ( <span class="hljs-keyword">var</span> i = <span class="hljs-number">1</span> ; i <= num; i++) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'媳妇我错了~'</span>);
&#125; 
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>for 循环重复不相同的代码</p>
<p>例如，求输出1到100岁：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">//  基本写法</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">1</span>; i <= <span class="hljs-number">100</span>; i++) &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'这个人今年'</span> + i + <span class="hljs-string">'岁了'</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>例如，求输出1到100岁，并提示出生、死亡</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// for 里面是可以添加其他语句的 </span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">1</span>; i <= <span class="hljs-number">100</span>; i++) &#123;
 <span class="hljs-keyword">if</span> (i == <span class="hljs-number">1</span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'这个人今年1岁了， 它出生了'</span>);
 &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (i == <span class="hljs-number">100</span>) &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'这个人今年100岁了，它死了'</span>);
  &#125; <span class="hljs-keyword">else</span> &#123;
       <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'这个人今年'</span> + i + <span class="hljs-string">'岁了'</span>);
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>for循环因为有了计数器的存在，还可以重复的执行某些操作，比如做一些算术运算。</p>
</li>
</ul>
<h3 data-id="heading-2">1.2 双重for循环</h3>
<ul>
<li>
<p>双重 for 循环概述</p>
<p>循环嵌套是指在一个循环语句中再定义一个循环语句的语法结构，例如在for循环语句中，可以再嵌套一个for 循环，这样的 for 循环语句我们称之为双重for循环。</p>
</li>
<li>
<p>双重 for 循环语法</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span> (外循环的初始; 外循环的条件; 外循环的操作表达式) &#123;
    <span class="hljs-keyword">for</span> (内循环的初始; 内循环的条件; 内循环的操作表达式) &#123;  
       需执行的代码;
   &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>内层循环可以看做外层循环的循环体语句</li>
<li>内层循环执行的顺序也要遵循 for 循环的执行顺序</li>
<li>外层循环执行一次，内层循环要执行全部次数</li>
</ul>
</li>
<li>
<p>打印五行五列星星</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">var</span> star = <span class="hljs-string">''</span>;
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> j = <span class="hljs-number">1</span>; j <= <span class="hljs-number">3</span>; j++) &#123;
    <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">1</span>; i <= <span class="hljs-number">3</span>; i++) &#123;
      star += <span class="hljs-string">'☆'</span>
    &#125;
    <span class="hljs-comment">// 每次满 5个星星 就 加一次换行</span>
    star += <span class="hljs-string">'\n'</span>
&#125;
<span class="hljs-built_in">console</span>.log(star);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>核心逻辑：</p>
<p>1.内层循环负责一行打印五个星星</p>
<p>2.外层循环负责打印五行</p>
</li>
<li>
<p>for 循环小结</p>
<ul>
<li>for 循环可以重复执行某些相同代码</li>
<li>for 循环可以重复执行些许不同的代码，因为我们有计数器</li>
<li>for 循环可以重复执行某些操作，比如算术运算符加法操作</li>
<li>随着需求增加，双重for循环可以做更多、更好看的效果</li>
<li>双重 for 循环，外层循环一次，内层 for 循环全部执行</li>
<li>for 循环是循环条件和数字直接相关的循环</li>
</ul>
</li>
</ul>
<h3 data-id="heading-3">1.3 while循环</h3>
<p>while语句的语法结构如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">while</span> (条件表达式) &#123;
    <span class="hljs-comment">// 循环体代码 </span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行思路：</p>
<ul>
<li>1 先执行条件表达式，如果结果为 true，则执行循环体代码；如果为 false，则退出循环，执行后面代码</li>
<li>2 执行循环体代码</li>
<li>3 循环体代码执行完毕后，程序会继续判断执行条件表达式，如条件仍为true，则会继续执行循环体，直到循环条件为 false 时，整个循环过程才会结束</li>
</ul>
<p>注意：</p>
<ul>
<li>使用 while 循环时一定要注意，它必须要有退出条件，否则会成为死循环</li>
</ul>
<h3 data-id="heading-4">1.4 do-while循环</h3>
<p>do... while 语句的语法结构如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">do</span> &#123;
    <span class="hljs-comment">// 循环体代码 - 条件表达式为 true 时重复执行循环体代码</span>
&#125; <span class="hljs-keyword">while</span>(条件表达式);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行思路</p>
<ul>
<li>
<p>1 先执行一次循环体代码</p>
</li>
<li>
<p>2 再执行条件表达式，如果结果为 true，则继续执行循环体代码，如果为 false，则退出循环，继续执行后面代码</p>
<p>注意：先再执行循环体，再判断，do…while循环语句至少会执行一次循环体代码</p>
</li>
</ul>
<h3 data-id="heading-5">1.5 continue、break</h3>
<p>continue 关键字用于立即跳出本次循环，继续下一次循环（本次循环体中 continue 之后的代码就会少执行一次）。</p>
<p>例如，吃5个包子，第3个有虫子，就扔掉第3个，继续吃第4个第5个包子，其代码实现如下：</p>
<pre><code class="hljs language-js copyable" lang="js"> <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">1</span>; i <= <span class="hljs-number">5</span>; i++) &#123;
     <span class="hljs-keyword">if</span> (i == <span class="hljs-number">3</span>) &#123;
         <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'这个包子有虫子，扔掉'</span>);
         <span class="hljs-keyword">continue</span>; <span class="hljs-comment">// 跳出本次循环，跳出的是第3次循环 </span>
      &#125;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'我正在吃第'</span> + i + <span class="hljs-string">'个包子呢'</span>);
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行结果：</p>
<p><img alt="图片1.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b08029453e8a472cae76a92126e839df~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>break 关键字用于立即跳出整个循环（循环结束）。</p>
<p>例如，吃5个包子，吃到第3个发现里面有半个虫子，其余的不吃了，其代码实现如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">1</span>; i <= <span class="hljs-number">5</span>; i++) &#123;
   <span class="hljs-keyword">if</span> (i == <span class="hljs-number">3</span>) &#123;
       <span class="hljs-keyword">break</span>; <span class="hljs-comment">// 直接退出整个for 循环，跳到整个for下面的语句</span>
   &#125;
   <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'我正在吃第'</span> + i + <span class="hljs-string">'个包子呢'</span>);
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行结果：</p>
<p><img alt="图片2.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a780150b4366463492b32a6267f0c14c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">2 - 代码规范</h2>
<h3 data-id="heading-7">2.1 标识符命名规范</h3>
<ul>
<li>变量、函数的命名必须要有意义</li>
<li>变量的名称一般用名词</li>
<li>函数的名称一般用动词</li>
</ul>
<h3 data-id="heading-8">2.2 操作符规范</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 操作符的左右两侧各保留一个空格</span>
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">1</span>; i <= <span class="hljs-number">5</span>; i++) &#123;
   <span class="hljs-keyword">if</span> (i == <span class="hljs-number">3</span>) &#123;
       <span class="hljs-keyword">break</span>; <span class="hljs-comment">// 直接退出整个 for 循环，跳到整个for循环下面的语句</span>
   &#125;
   <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'我正在吃第'</span> + i + <span class="hljs-string">'个包子呢'</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">2.3 单行注释规范</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i = <span class="hljs-number">1</span>; i <= <span class="hljs-number">5</span>; i++) &#123;
   <span class="hljs-keyword">if</span> (i == <span class="hljs-number">3</span>) &#123;
       <span class="hljs-keyword">break</span>; <span class="hljs-comment">// 单行注释前面注意有个空格</span>
   &#125;
   <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'我正在吃第'</span> + i + <span class="hljs-string">'个包子呢'</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">2.4 其他规范</h3>
<pre><code class="copyable">关键词、操作符之间后加空格
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="图片3.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d68a886a7edf41629a71f23589aeb4ab~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            