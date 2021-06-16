
---
title: '面试：event Loop和防抖节流'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e70c26c765f4abdbebeb028200a5c85~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 15 Jun 2021 03:28:22 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e70c26c765f4abdbebeb028200a5c85~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><ul>
<li>杭州前端岗</li>
</ul>
<h3 data-id="heading-0">人事面</h3>
<ul>
<li>换工作原因</li>
<li>到岗时间</li>
<li>个人职业规划</li>
</ul>
<hr>
<h4 data-id="heading-1">JavaScript 相关</h4>
<h5 data-id="heading-2">一、闭包</h5>
<ul>
<li>背景：Javascript语言中，函数内部可以直接读取外部或全局变量</li>
<li>闭包优点
<ul>
<li>可以读取函数内部的变量</li>
<li>让这些变量的值始终保持在内存中（结合内存回收中的标记清除表述）</li>
</ul>
</li>
<li>闭包缺点
<ul>
<li>内存消耗大，容易造成内存泄漏引起性能问题</li>
</ul>
</li>
</ul>
<h5 data-id="heading-3">二、原型链</h5>
<blockquote>
<p>当访问一个对象的属性时，如果该对象内部不存在这个属性，那么就会去它的__proto__属性所指向的那个对象（父对象）里找，一直找，直到__proto__属性的终点null，然后返回undefined，通过__proto__属性将对象连接起来的这条链路即我们所谓的原型链。</p>
</blockquote>
<ul>
<li>联系红宝书，关联<code>prototype(原型)</code>及<code>constructor</code>表述</li>
<li>__proto__和constructor属性是对象所独有的；</li>
<li>prototype属性是函数所独有的</li>
<li>函数也是对象，所以函数（箭头函数没有）也拥有__proto__和constructor属性</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Person</span>(<span class="hljs-params"></span>)</span>&#123;
  &#125;
  <span class="hljs-keyword">var</span> person=<span class="hljs-keyword">new</span> Person();
  
  <span class="hljs-keyword">var</span> x=[]  
  x.constructor===<span class="hljs-built_in">Array</span>
  <span class="hljs-comment">/**
   * person.constructor===Person
   * person.__proto__===Person.prototype
   * person.constructor===Person
   
  */</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-4">三、 <code>event Loop</code>事件循环</h5>
<blockquote>
<p>Event Loop即事件循环，是指浏览器或Node的一种解决javaScript单线程运行时不会阻塞的一种机制，也就是我们经常使用异步的原理。</p>
</blockquote>
<ul>
<li>宿主环境无论是Node、还是浏览器都是多线程</li>
<li>但js是单线程语言，浏览器只分配给js一个主线程,一次只能执行一个任务</li>
<li>为提高执行效率为http请求，浏览器的定时及事件监听等异步开辟另外的线程（任务队列）</li>
<li>只要主线程执行完，就会读取‘任务队列’</li>
<li>在JS中，任务分两种，<code>宏任务（MacroTask）</code>也叫Task，<code>微任务（MicroTask）</code></li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e70c26c765f4abdbebeb028200a5c85~tplv-k3u1fbpfcp-watermark.image" alt="MacroTaskOrMicroTask.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>任务队列在栈空的时候被调入的优先级是<strong>微观任务队列优于宏观任务队列</strong>
<ul>
<li>补充：Promise 执行器中的代码会被同步调用，但是回调是基于微任务的</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">/**
  * Microtask Queue 微任务队列 
  * Message Queue 消息队列
  * call stack 调用栈
  
  宏任务典型的：整个JavaScript代码，setTimeout、setInterval、DOM事件
  微任务典型的：Process.nextTick（Node独有）、Promise、async/await
 */</span>
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'task1'</span>);
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'taskPlus1'</span>);
  &#125;)
  <span class="hljs-built_in">Promise</span>.resolve().then(<span class="hljs-function">()=></span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'taskPlus2'</span>);
  &#125;)
  <span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">()=></span>&#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'taskPlus3'</span>);
  &#125;)
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'task2'</span>);
<span class="hljs-comment">// task1  task2 taskPlus2 taskPlus1 taskPlus3</span>
<span class="hljs-comment">/**
  *  首先浏览器执行js第一个宏任务进入主线程
  * 遇到 console.log() 直接执行         所以先输出 --- task1
  * 遇到 setTimeout  分发到宏任务Event Queue中
  * 遇到 Promise，执行then 被分发到微任务Event Queue中
  * 遇到 setTimeout  分发到宏任务Event Queue中
  * 遇到 console.log() 直接执行           再输出   ---task2
  * 第一轮宏任务执行结束，执行微任务Promise 再输出------'taskPlus2' 
  * 微任务全部执行完毕，执行第二轮宏事件setTimeout，输出 --'taskPlus1'
  * 执行微服务，没有微服务，执行第三轮宏事件setTimeout，输出--'taskPlus3'
 */</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>可以看出Promise确实会比setTimeout()先执行。</li>
<li>因为Promise定义之后便会立即执行，其后的.then( ) 是异步里面的微任务。</li>
</ul>
<h5 data-id="heading-5">四、 防抖和节流</h5>
<ul>
<li>防抖
<ul>
<li>概念：利用setTimeout，在一定时间间隔内，将多次触发变为一次触发</li>
<li>前置条件：必须熟知JS中<strong>this指向</strong>问题，及函数内类数组对象<code>arguments</code></li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">    btn.addEventListener(<span class="hljs-string">'click'</span>,debounce(submit,<span class="hljs-number">3000</span>))
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">submit</span>(<span class="hljs-params">e</span>)</span>&#123;
        <span class="hljs-comment">// Do something</span>
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'---'</span>);
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">debounce</span>(<span class="hljs-params">cbk,wait</span>)</span>&#123;
        <span class="hljs-keyword">let</span> timer=<span class="hljs-literal">null</span>;
        <span class="hljs-keyword">return</span><span class="hljs-function">(<span class="hljs-params">...args</span>)=></span>&#123;
            <span class="hljs-comment">//如果定时器存在就清除上一个，避免多次执行</span>
            <span class="hljs-keyword">if</span>(timer) <span class="hljs-built_in">clearTimeout</span>(timer)
            <span class="hljs-comment">//必须使用箭头函数，避免函数自身污染外部arguments</span>
            timer=<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
              timer=<span class="hljs-literal">null</span> ;
              cbk.apply(<span class="hljs-built_in">this</span>,args)
            &#125;, wait);
        &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>节流
<ul>
<li>概念：借助flag元素和setTimeout实现在一定时间内，只执行一次方法</li>
<li>着重点间隔的判断及时间戳更新</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">    btn.addEventListener(<span class="hljs-string">'click'</span>,throttle(submit,<span class="hljs-number">3000</span>))
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">submit</span>(<span class="hljs-params">e</span>)</span>&#123;
      <span class="hljs-comment">// Do something</span>
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'---'</span>);
    &#125;
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">throttle</span>(<span class="hljs-params">cbk,delay</span>)</span>&#123;
      <span class="hljs-comment">// 设置初始值</span>
      <span class="hljs-keyword">var</span> begin=<span class="hljs-number">0</span>;
      <span class="hljs-keyword">return</span><span class="hljs-function">(<span class="hljs-params">...args</span>)=></span>&#123;
          <span class="hljs-comment">// 当前点击的时间戳</span>
          <span class="hljs-keyword">var</span> cur=<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>().getTime();
          <span class="hljs-comment">//每次点击的时间和上次的时间大于定义间隔则执行</span>
          <span class="hljs-keyword">if</span>(cur-begin>delay)&#123;
              cbk.apply(<span class="hljs-built_in">this</span>,args)
              <span class="hljs-comment">//更新初始值</span>
              begin=cur;
          &#125;
      &#125;
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<h5 data-id="heading-6">四、 ES6新语法 ？</h5>
<ul>
<li>变量声明中的let、const
<ul>
<li>块级作用域：二者只在当前声明下的大括号下可见</li>
<li>重复声明：二者均不支持同作用域重复声明</li>
<li>调用：二者不属于全局对象属性，也不支持全局this调用</li>
<li>变量提升：二者与var不同，不存在变量提升，提前使用报错</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-built_in">console</span>.log(potato);<span class="hljs-comment">//undefined</span>
  <span class="hljs-built_in">console</span>.log(tomato);<span class="hljs-comment">//ReferenceError: tomato is not defined</span>
  <span class="hljs-keyword">var</span> potato=<span class="hljs-string">'YES'</span>;
  <span class="hljs-keyword">let</span> tomato=<span class="hljs-string">'NO'</span>;
  <span class="hljs-keyword">const</span> cucumber=<span class="hljs-string">'LIKE'</span>
  ------------------
  <span class="hljs-built_in">this</span>.potato <span class="hljs-comment">// "YES"</span>
  <span class="hljs-built_in">this</span>.tomato <span class="hljs-comment">// undefined </span>
  <span class="hljs-built_in">this</span>.cucumber <span class="hljs-comment">// Identifier 'cucumber' has already been declared</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>模板字符串[ <strong>`</strong> ]
<ul>
<li>结合<code>$&#123;&#125;</code>引入变量，更便于字符拼接</li>
</ul>
</li>
<li>唯一值定义 <code>Symbol</code>
<ul>
<li>通过Symbol函数生成的值都是独一无二，且其类型为<code>"symbol"</code></li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-keyword">var</span> fruit1=<span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'apple'</span>)
  <span class="hljs-keyword">var</span> fruit2=<span class="hljs-built_in">Symbol</span>(<span class="hljs-string">'apple'</span>)
  <span class="hljs-keyword">var</span> fruit3=<span class="hljs-string">'apple'</span>;
  <span class="hljs-keyword">typeof</span> fruit2 <span class="hljs-comment">// "symbol"</span>
  <span class="hljs-keyword">typeof</span> fruit3 <span class="hljs-comment">// "string"</span>
  fruit1==fruit2 <span class="hljs-comment">//false</span>
  fruit1==fruit3 <span class="hljs-comment">//false</span>
  fruit1===fruit2 <span class="hljs-comment">//false</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>箭头函数 <code>=></code>
<ul>
<li>使用它本质是为了避免函数中this的管理过于混乱
<ul>
<li>箭头函数不会创建自己的this,会从自己的作用域链的上一层继承this</li>
<li>箭头函数没有自己的<strong>this</strong>及<strong>arguments</strong></li>
<li>不支持call/apply改变this指向，见下</li>
</ul>
</li>
<li>普通函数中this指向大多和自身所处环境及被引用有关
<ul>
<li>箭头函数中this指向在定义时就被固定</li>
<li>通过 call() 或 apply() 方法调用一个函数时，只能传递参数（不能绑定this---译者注）</li>
</ul>
</li>
</ul>
</li>
<li>解构赋值 <code>[ ]</code>或者展开运算符 <code>...</code>
<ul>
<li>常用于简化数据交互及赋值操作，或者二者搭配进行数据解析</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-keyword">let</span> first=[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>];
  <span class="hljs-keyword">let</span> last=[<span class="hljs-number">6</span>,<span class="hljs-number">7</span>,<span class="hljs-number">8</span>];
  <span class="hljs-keyword">let</span> concat=[...first,...last]
  concat <span class="hljs-comment">// [1, 2, 3, 6, 7, 8]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>Set数据结构
<ul>
<li>Set数据容器，这是一个能够存储无重复值的有序列表。
<ul>
<li>可以利用它的无重复特性，进行数组去重</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-keyword">var</span> unique=[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">5</span>,<span class="hljs-number">5</span>,<span class="hljs-number">6</span>,<span class="hljs-number">6</span>,<span class="hljs-number">8</span>];
  <span class="hljs-comment">// Set对象非数组，利用展开运算符转数组</span>
 [...unique]=<span class="hljs-keyword">new</span> <span class="hljs-built_in">Set</span>(unique);
 <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">Array</span>.isArray(unique));<span class="hljs-comment">// true</span>
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>Promise 对象
<ul>
<li>状态有三种，pending（进行中）、fulfilled（已成功）和rejected（已失败）。</li>
<li>状态有不可逆性
<ul>
<li>pending变为fulfilled（成功）</li>
<li>pending变为rejected（失败）</li>
</ul>
</li>
<li>创建：利用关键字 new 进行生成</li>
<li>参数：对象接收两个函数，分别是resolve和reject。
<ul>
<li>异步操作成功，结果会传入resolve( )</li>
<li>异步操作失败，错误会传入reject( )</li>
<li>无论哪种，状态都会发生变化</li>
</ul>
</li>
<li>调用：当<strong>Promise状态为fulfilled时</strong>，会调用实例的<code>.then</code>方法
<ul>
<li>实例的<code>.then</code>其实是继承于Promise.prototype上的方法</li>
<li><code>.then(value)</code>获取的参数是resolve(params)中传递过来的</li>
</ul>
</li>
<li>Promise.all异步请求并行操作
<ul>
<li>当所有结果成功返回时按照请求顺序返回成功;</li>
<li>当其中有一个失败方法时，则进入失败方法;</li>
</ul>
</li>
</ul>
</li>
</ul>
<h5 data-id="heading-7">五、 数组方法</h5>
<ul>
<li><code>filter</code> ：过滤返回数组中符合条件的值</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">let</span> numbers=[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">3</span>,<span class="hljs-number">2</span>,<span class="hljs-number">1</span>]
    <span class="hljs-keyword">let</span> result=numbers.filter(<span class="hljs-function"><span class="hljs-params">item</span>=></span>&#123;
      <span class="hljs-keyword">return</span> item!=<span class="hljs-number">2</span>;
   &#125;)
  <span class="hljs-built_in">console</span>.log(result);<span class="hljs-comment">//[1, 3, 4, 3, 1]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li><code>map</code>：回一个新数组，数组中的元素为原始数组元素调用函数处理后的值
<ul>
<li>map() 不会对空数组进行检测，不会改变原始数组。</li>
<li>map()方法会得到一个新的数组并返回。</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">let</span> numbers=[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">3</span>,<span class="hljs-number">2</span>,<span class="hljs-number">1</span>]
    <span class="hljs-keyword">let</span> result=numbers.map(<span class="hljs-function"><span class="hljs-params">item</span>=></span>&#123;
      <span class="hljs-keyword">return</span> item!=<span class="hljs-number">2</span>;
    &#125;)
    <span class="hljs-keyword">let</span> process=numbers.map(<span class="hljs-function"><span class="hljs-params">item</span>=></span>&#123;
      <span class="hljs-keyword">return</span> item+=<span class="hljs-number">1</span>;
    &#125;)
  <span class="hljs-built_in">console</span>.log(result);<span class="hljs-comment">// [true, false, true, true, true, false, true]</span>
  <span class="hljs-built_in">console</span>.log(process);<span class="hljs-comment">//[2, 3, 4, 5, 4, 3, 2]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>map返回对当前元素调用函数后的结果，filter 会将符合条件的元素存到新的数组中并返回。</p>
</blockquote>
<ul>
<li><code>forEach</code>:类似于for循环遍历数组中每一项，但不支持break，无法终止循环
<ul>
<li>forEach()会修改原来的数组</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">let</span> numbers=[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">3</span>,<span class="hljs-number">2</span>,<span class="hljs-number">1</span>]
      numbers.forEach(<span class="hljs-function">(<span class="hljs-params">item,index,data</span>)=></span>&#123;
          data[index]+=<span class="hljs-number">1</span>
        &#125;)
   <span class="hljs-built_in">console</span>.log(numbers);<span class="hljs-comment">//[2, 3, 4, 5, 4, 3, 2]</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>map有返回值且是新数组，forEach没有返回值且改变原数组。</p>
</blockquote>
<ul>
<li><code>reduce</code>:用于计算数组元素相加后的总和</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <span class="hljs-keyword">let</span> numbers=[<span class="hljs-number">1</span>,<span class="hljs-number">2</span>,<span class="hljs-number">3</span>,<span class="hljs-number">4</span>,<span class="hljs-number">3</span>,<span class="hljs-number">2</span>,<span class="hljs-number">1</span>]
    <span class="hljs-keyword">var</span> sum = numbers.reduce(<span class="hljs-function">(<span class="hljs-params">prev, cur</span>)=></span> &#123;<span class="hljs-keyword">return</span> prev + cur &#125;);
   <span class="hljs-built_in">console</span>.log(sum);<span class="hljs-comment">//16</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>for of遍历的是数组元素值
<ul>
<li>for..of适用遍历数/数组对象/字符串/map/set等拥有迭代器对象的集合.但是<strong>不能遍历对象</strong></li>
<li>可正确响应break、continue和return语句</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-keyword">let</span> numbers=[<span class="hljs-number">1</span>,<span class="hljs-number">3</span>,<span class="hljs-number">3</span>,<span class="hljs-number">2</span>]
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> index <span class="hljs-keyword">of</span> numbers) &#123;
  <span class="hljs-built_in">console</span>.log(index);<span class="hljs-comment">//  1 3 3 2 元素值</span>
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>for in遍历的是数组的索引（即键名）
<ul>
<li>for in也可以循环数组但是特别适合遍历对象</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">  <span class="hljs-keyword">let</span> numbers=[<span class="hljs-number">1</span>,<span class="hljs-number">3</span>,<span class="hljs-number">3</span>,<span class="hljs-number">2</span>]
  <span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> index <span class="hljs-keyword">in</span> numbers) &#123;
  <span class="hljs-built_in">console</span>.log(index);<span class="hljs-comment">// 0 1 2 3 索引</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ul>
<blockquote>
<p>for in遍历的是数组的索引（即键名），而for of遍历的是数组元素值。</p>
</blockquote>
<h4 data-id="heading-8">Vue相关</h4>
<h5 data-id="heading-9">一、 Vue组件及组件嵌套的生命周期钩子函数</h5>
<blockquote>
<p>之前写过，点击 → <a href="https://juejin.cn/post/6963095749538086942" target="_blank">Vue生命周期及嵌套</a></p>
</blockquote>
<h5 data-id="heading-10">二、 vue的computed和watch的区别</h5>
<ul>
<li>computed计算属性的作用
<ul>
<li>变量可不在 data中定义，定义在computed中，写法跟写方法一样，有返回值</li>
<li>在页面模板中渲染直接写函数名，不用加括号调用</li>
<li>根据传入的变量的变化，进行结果的更新</li>
<li>性能方面
<ul>
<li>methods中每调用一次就会重新计算，为了进行不必要的资源消耗</li>
<li>值未发生变化时，计算属性调用的是缓存数据，提高性能</li>
</ul>
</li>
</ul>
</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript">    <div id=<span class="hljs-string">"app"</span>>
    &#123;&#123; getMoney &#125;&#125; <span class="hljs-comment">// 展示总额</span>
    </div>
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    vm = newVue(&#123;
    <span class="hljs-attr">el</span>: <span class="hljs-string">"#app"</span>,
    <span class="hljs-attr">data</span>:&#123;
      <span class="hljs-attr">myGoodsCount</span>:<span class="hljs-number">3</span>,
      <span class="hljs-attr">price</span>:<span class="hljs-string">'25'</span>
    &#125;,
    <span class="hljs-attr">computed</span>:&#123;
      <span class="hljs-function"><span class="hljs-title">getMoney</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.myGoodsCount*<span class="hljs-built_in">this</span>.price;
        &#125;
      &#125;
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>watch 监听属性
<ul>
<li>watch是在值发生改变的时候才会触发。</li>
<li>当有些数据需要随着其它数据变动而联动时</li>
<li>或数据变化时执行异步时，可以使用 watch。</li>
</ul>
</li>
<li>二者的区别
<ul>
<li>计算属性变量在computed中定义，watch属性监听在data中定义</li>
<li>computed支持数据缓存，watch不支持数据缓存</li>
<li>computed值多个值变化影响当前值（多对一），watch是当前一个值变化影响多个值（一对多）</li>
<li>计算属性是声明一个值依赖其他值，依赖的值改变后重新计算结果更新DOM视图</li>
<li>属性监听的是data定义的变量，当定义的值发生变化时，执行相对应的函数</li>
</ul>
</li>
</ul>
<h5 data-id="heading-11">三、vue路由模式</h5>
<ul>
<li>路由的两种模式
<ul>
<li>hash模式 ：默认模式，通过路径中的hash值来控制路由跳转，路径带有#号</li>
<li>history模式：H5新增的 history API，不会显示#号，但是必须服务器端进行配置</li>
</ul>
</li>
<li>重要补充
<ul>
<li>hash模式下，前端路由修改的是#中的信息，刷新没有问题</li>
<li>history模式下，刷新由于发起了服务请求，因此会报404，所以需求服务端给路由到初始页面</li>
<li>APP端，不支持#号，因此不支持hash模式</li>
</ul>
</li>
<li><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>r</mi><mi>o</mi><mi>u</mi><mi>t</mi><mi>e</mi><mtext>和</mtext></mrow><annotation encoding="application/x-tex">route和</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">o</span><span class="mord mathnormal">u</span><span class="mord mathnormal">t</span><span class="mord mathnormal">e</span><span class="mord cjk_fallback">和</span></span></span></span></span>router的区别
<ul>
<li>$route为当前router跳转对象里面可以获取name、path、query、params等</li>
<li><span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>r</mi><mi>o</mi><mi>u</mi><mi>t</mi><mi>e</mi><mi>r</mi><mtext>为</mtext><mi>V</mi><mi>u</mi><mi>e</mi><mi>R</mi><mi>o</mi><mi>u</mi><mi>t</mi><mi>e</mi><mi>r</mi><mtext>实例，包含路由的跳转方法，钩子函数等，如导航到不同</mtext><mi>U</mi><mi>R</mi><mi>L</mi><mtext>，用</mtext></mrow><annotation encoding="application/x-tex">router为VueRouter实例，包含路由的跳转方法，钩子函数等，如导航到不同URL，用</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">o</span><span class="mord mathnormal">u</span><span class="mord mathnormal">t</span><span class="mord mathnormal">e</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord cjk_fallback">为</span><span class="mord mathnormal" style="margin-right:0.22222em;">V</span><span class="mord mathnormal">u</span><span class="mord mathnormal">e</span><span class="mord mathnormal" style="margin-right:0.00773em;">R</span><span class="mord mathnormal">o</span><span class="mord mathnormal">u</span><span class="mord mathnormal">t</span><span class="mord mathnormal">e</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord cjk_fallback">实</span><span class="mord cjk_fallback">例</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">包</span><span class="mord cjk_fallback">含</span><span class="mord cjk_fallback">路</span><span class="mord cjk_fallback">由</span><span class="mord cjk_fallback">的</span><span class="mord cjk_fallback">跳</span><span class="mord cjk_fallback">转</span><span class="mord cjk_fallback">方</span><span class="mord cjk_fallback">法</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">钩</span><span class="mord cjk_fallback">子</span><span class="mord cjk_fallback">函</span><span class="mord cjk_fallback">数</span><span class="mord cjk_fallback">等</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">如</span><span class="mord cjk_fallback">导</span><span class="mord cjk_fallback">航</span><span class="mord cjk_fallback">到</span><span class="mord cjk_fallback">不</span><span class="mord cjk_fallback">同</span><span class="mord mathnormal" style="margin-right:0.10903em;">U</span><span class="mord mathnormal" style="margin-right:0.00773em;">R</span><span class="mord mathnormal">L</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">用</span></span></span></span></span>router.push</li>
</ul>
</li>
</ul>
<h4 data-id="heading-12">HTML及CSS相关</h4>
<h5 data-id="heading-13">一、样式优先级</h5>
<ul>
<li>优先级关系：内联样式 > ID 选择器 > 类选择器 = 属性选择器 = 伪类选择器 > 标签选择器 = 伪元素选择器</li>
<li>图示如下，来源互联网
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2616ae8a43e46949c78470e31b5d307~tplv-k3u1fbpfcp-watermark.image" alt="CSSImportant.jpg" loading="lazy" referrerpolicy="no-referrer"></li>
</ul>
<h5 data-id="heading-14">二、盒模型</h5>
<ul>
<li>W3C的标准盒模型
<ul>
<li>标准盒模型中元素的width=content</li>
</ul>
</li>
<li>IE怪异盒模型
<ul>
<li>IE怪异盒模型中元素的width=content+padding+border</li>
</ul>
</li>
<li>切换当前盒模型
<ul>
<li>box-sizing: content-box 是W3C盒子模型</li>
<li>box-sizing: border-box 是IE怪异盒模型</li>
</ul>
</li>
</ul>
<blockquote>
<p>知乎链接，讲解更详细——>，<a href="https://zhuanlan.zhihu.com/p/74817089" target="_blank" rel="nofollow noopener noreferrer">知乎</a></p>
</blockquote>
<h5 data-id="heading-15">三、 垂直居中</h5>
<ul>
<li>使用绝对定位来实现（子绝父相），同时利用 transform</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css">
<span class="hljs-selector-class">.parent</span>&#123;
    <span class="hljs-attribute">position</span>: relative;<span class="hljs-comment">/*父相*/</span>


    <span class="hljs-attribute">height</span>: <span class="hljs-number">360px</span>;
&#125;
<span class="hljs-selector-class">.son</span>&#123;
    <span class="hljs-attribute">position</span>: absolute; <span class="hljs-comment">/*子绝*/</span>
    <span class="hljs-attribute">left</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">top</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">transform</span>: <span class="hljs-built_in">translate</span>(-<span class="hljs-number">50%</span>,-<span class="hljs-number">50%</span>); 
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用flex布局会更加的方便</li>
</ul>
<pre><code class="hljs language-css copyable" lang="css"><span class="hljs-selector-class">.parent</span>&#123;
  <span class="hljs-attribute">display</span>: flex;
  <span class="hljs-attribute">height</span>: <span class="hljs-number">360px</span>;
  <span class="hljs-attribute">background</span>:hotpink;
&#125;
<span class="hljs-selector-class">.son</span>&#123;
    <span class="hljs-attribute">margin</span>: auto;
    <span class="hljs-attribute">background</span>: rosybrown;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">HTTP相关</h4>
<blockquote>
<p>之前总结过，点击 → <a href="https://juejin.cn/post/6963095749538086942" target="_blank">HTTP状态码及请求头</a></p>
</blockquote>
<p>一、 跨域解决方案</p>
<blockquote>
<p>跨域原因：为了浏览器安全采取的同源策略，指"协议+域名+端口"三者相同。</p>
</blockquote>
<ul>
<li>jsonp
<ul>
<li>动态添加一个<script>标签，而script标签的src属性是没有跨域的限制的。</li>
</ul>
</li>
<li>Ajax中设置dataType
<ul>
<li>dataType: 'jsonp', //请求方式为jsonp</li>
</ul>
</li>
<li>跨域资源共享（CORS）</li>
</ul>
<pre><code class="copyable">- 服务端设置Access-Control-Allow-Origin即可
  ```javascript
  res.header("Access-Control-Allow-Origin", "*"); //设置请求来源不受限制
  ```
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>nginx代理</li>
</ul>
<hr>
<h4 data-id="heading-17">拓展</h4>
<h5 data-id="heading-18">一、API设计规范？比如RESTful API</h5>
<ul>
<li><a href="https://www.ruanyifeng.com/blog/2014/05/restful_api.html" target="_blank" rel="nofollow noopener noreferrer">阮一峰老师RESTful API 设计规范</a></li>
</ul>
<h5 data-id="heading-19">二、工作中Git的使用</h5>
<ul>
<li>冲突如何解决，以及如何选用多个commit的其中几个
<ul>
<li>cherry-pick</li>
</ul>
</li>
</ul>
<h5 data-id="heading-20">三、拓展内容</h5>
<ul>
<li>平时通过哪些渠道获取技术信息，学习习惯</li>
</ul>
<h5 data-id="heading-21">想了解的东西？</h5>
<ul>
<li>公司目前的业务方向。</li>
</ul></div>  
</div>
            