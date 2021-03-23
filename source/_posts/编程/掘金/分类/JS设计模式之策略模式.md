
---
title: 'JS设计模式之策略模式'
categories: 
    - 编程
    - 掘金
    - 分类

author: 掘金
comments: false
date: Mon, 22 Mar 2021 21:28:00 GMT
thumbnail: ''
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>不知道你有没有遇到过这样的情况，对不同的输入需要产生不同的输出，例如我现在需要根据员工的等级来发最后的年终奖，这时候最简便的方法莫过于写一大堆<code>if···else···</code>语句了。就像这样：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> calculateBonus = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"> level, salary </span>)</span>&#123; 
    <span class="hljs-keyword">if</span> ( level === <span class="hljs-string">'S'</span> )&#123; 
         <span class="hljs-keyword">return</span> salary * <span class="hljs-number">4</span>; 
    &#125; 
    <span class="hljs-keyword">if</span> ( level === <span class="hljs-string">'A'</span> )&#123; 
         <span class="hljs-keyword">return</span> salary * <span class="hljs-number">3</span>; 
    &#125; 
    <span class="hljs-keyword">if</span> ( level === <span class="hljs-string">'B'</span> )&#123; 
        <span class="hljs-keyword">return</span> salary * <span class="hljs-number">2</span>; 
    &#125; 
&#125;; 
calculateBonus( <span class="hljs-string">'B'</span>, <span class="hljs-number">20000</span> ); <span class="hljs-comment">// 输出：40000 </span>
calculateBonus( <span class="hljs-string">'S'</span>, <span class="hljs-number">6000</span> ); <span class="hljs-comment">// 输出：24000</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到这样写的确很简单，但是存在着显而易见的问题：</p>
<ol>
<li>整个calculateBouns函数太庞大了，包含了非常多的<code>if-else</code>语句，这些语句需要覆盖所有的语句。</li>
<li>违背了开放封闭原则。如果需要临时增加员工等级或者修改分配方式，那么只能直接去修改原来的代码，增加判断条件，这种侵入是很大的。</li>
<li>重用性低，这样的代码无法高效复用，只能无脑CV。</li>
</ol>
<p>这个时候，我们需要一种更好的代码组织方式。</p>
<h2 data-id="heading-1">策略模式</h2>
<p>什么是策略模式呢？策略模式就是<strong>定义一系列的算法，把它们一个个封装起来，并且使它们可以相互替换</strong>，那么这是比较官方的说法。代入我们这个计算奖金的例子里面来讲的话，每个if语句里面的逻辑就相当于算法，我们要把这些算法用一些手段封装起来，让它们之间独立，保持一个平等的关系也就相当于它们之间可以相互替换。</p>
<h3 data-id="heading-2">使用策略模式重构代码</h3>
<p>大概知道了策略模式大概是怎么回事。接下来，具体来探究如何使用策略模式。首先，策略模式至少由两部分组成，第一个是一组策略类，策略类封装了具体的算法，并负责具体的计算过程。第二个是Context（上下文），Context负责接收请求，之后把请求委托给某一个具体的策略类。<br>
其实很好理解，Context就相当于一个中转站，接收不同的计算请求，然后把具体的计算任务转发给某一个具体策略类。那么接下来就使用策略模式来讲上面讲的那个计算年终奖的例子来实现吧</p>
<h4 data-id="heading-3">定义一组策略类</h4>
<p>策略类往往都是指一个问题中可能会变化的部分。回到年终奖的例子中，计算年终奖的方式都不同，他的级别高一点，年终奖就高一点，她的级别可能低一点，年终奖可能就低一点。那么，计算年终奖的方式就是变化的，策略类的任务就是把这些不同的计算方式封装成一组一组的策略。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> LevelS = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125;; 
performanceS.prototype.calculate = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"> salary </span>)</span>&#123;
  <span class="hljs-keyword">return</span> salary * <span class="hljs-number">4</span>; 
&#125;;
<span class="hljs-keyword">let</span> LevelA = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125;; 
performanceA.prototype.calculate = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"> salary </span>)</span>&#123; 
  <span class="hljs-keyword">return</span> salary * <span class="hljs-number">3</span>; 
&#125;;
<span class="hljs-keyword">let</span> LevelB = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;&#125;; 
performanceB.prototype.calculate = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"> salary </span>)</span>&#123; 
  <span class="hljs-keyword">return</span> salary * <span class="hljs-number">2</span>; 
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的代码定义了三个构造函数，分别对应三种不同的等级并且在各自的原型上定义了<code>calculate</code>方法，这个方法用来计算年终奖。</p>
<h4 data-id="heading-4">实现中转站</h4>
<p>中转站就相当前面提到的策略模式的第二部分Context，其实它就是一个向外暴露的接口，根据不同的输入去调用不同的策略类，然后将结果返回。
实现的方式也很简单，这里还是使用类，先定义一个奖金类Bouns，它有两个原型方法,<code>setSalary</code>用来设置原始工资，<code>setStrategy</code>用来设置策略对象，最后，<code>getBouns</code>用来计算年终奖，Bouns类本身不具备计算能力，当调用getBouns方法的时候其实是将计算任务委派给了对应的策略类。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> Bouns = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>.salary = <span class="hljs-literal">null</span>;
  <span class="hljs-built_in">this</span>.strategy = <span class="hljs-literal">null</span>
&#125;
Bouns.prototype.setSalary = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">salary</span>) </span>&#123;
  <span class="hljs-comment">// 设置员工的原始工资</span>
  <span class="hljs-built_in">this</span>.salary = salary;
&#125;
Bouns.prototype.setStrategy = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">strategy</span>) </span>&#123;
  <span class="hljs-comment">// 设置策略对象</span>
  <span class="hljs-built_in">this</span>.strategy = strategy;
&#125;
Bouns.prototype.getBouns = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.strategy.calculate(<span class="hljs-built_in">this</span>.salary);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">实现策略模式年终奖计算</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> bouns = <span class="hljs-keyword">new</span> Bouns()
bouns.setSalary(<span class="hljs-number">20000</span>);
bouns.setStrategy(<span class="hljs-keyword">new</span> LevelS())
<span class="hljs-built_in">console</span>.log(bouns.getBouns())   <span class="hljs-comment">// 输出: 80000</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们先创建了一个<code>bouns</code>对象，然后给这个对象设置了一些基本的数据，基本工资和对应等级的策略对象，然后通过<code>getBouns</code>方法来计算年终奖。如果想计算其他等级的年终奖，只需要继续调用<code>setStrategy</code>方法设置其他的策略对象即可，不需要更改原来的代码。如果想增加等级就更简单了，直接新建一个策略类，然后调用<code>setStrategy</code>方法将新建的策略的对象传入就可以了。<br>
这样的代码是不是要比之前的<code>if-else</code>要好很多呢，变得更好维护了，重用性也高了。</p>
<h2 data-id="heading-6">JavaScript版本的策略模式</h2>
<p>看到这个标题是不是很不解，难道上面写的不是JavaScript？这是因为上面的策略模式是模仿一些传统的面向对象编程语言的策略模式的实现，而在JavaScript中对象不一定需要构造函数实例化，而且函数也是对象。完全可以将那一组组的策略类变成一个普通对象的属性，把中转站变成一个普通函数啊，这样岂不是更简单明了。</p>
<h3 data-id="heading-7">创建策略对象</h3>
<p>创建一个策略对象，这个策略对象里面包含了不同的计算策略，其实也就是对象的方法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> strategies = &#123;
  <span class="hljs-string">'S'</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">salary</span>) </span>&#123;
    <span class="hljs-keyword">return</span> salary * <span class="hljs-number">4</span>
  &#125;,
  <span class="hljs-string">'A'</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">salary</span>) </span>&#123;
    <span class="hljs-keyword">return</span> salary * <span class="hljs-number">3</span>
  &#125;,
  <span class="hljs-string">'B'</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">salary</span>) </span>&#123;
    <span class="hljs-keyword">return</span> salary * <span class="hljs-number">2</span>
  &#125;,
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们将不同的计算方法放到了一起作为对象的方法，就相当于把他们<strong>组合</strong>放置在一个篮子里，之后需要哪个就去拿哪个。</p>
<h3 data-id="heading-8">创建一个计算函数</h3>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">calculateBouns</span> (<span class="hljs-params">level, salary</span>) </span>&#123;
  <span class="hljs-keyword">return</span> strategies[level](salary);
&#125;
<span class="hljs-built_in">console</span>.log(calculateBouns(<span class="hljs-string">'S'</span>, <span class="hljs-number">20000</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>calculateBouns</code>函数接收等级和基础工资两个参数，然后去strategies对象中找到与等级相对应的方法求值。相比使用类的方式实现策略模式，这样更清晰明了。再相比最开始直接使用<code>if-else</code>的方法，省去了条件判断，增加了程序的”弹性“，易扩展。</p>
<h2 data-id="heading-9">总结</h2>
<p>策略模式其实也有体现出多态性，我们没有把和年终奖计算相关的逻辑放在一起，而是分布在各个策略对象中。而Context中转站没有计算能力，而是将具体的计算任务交给某个策略对象，然后策略对象返回不同的结果，这正是多态性的体现，也是它们之间可以相互替换的关键，替换Context中转站中保存的策略对象，就可以得到不同的计算结果。策略模式的优点很明显：</p>
<ol>
<li>可以有效地避免多重条件选择语句</li>
<li>代码复用性高，避免了很多粘贴复制的操作。</li>
<li>策略模式提供了对开放封闭原则的支持，将算法独立封装在strategies中，使得它们易于切换，易于扩展。</li>
</ol></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            