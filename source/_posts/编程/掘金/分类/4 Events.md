
---
title: '4. Events'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2623'
author: 掘金
comments: false
date: Thu, 01 Jul 2021 22:18:08 GMT
thumbnail: 'https://picsum.photos/400/300?random=2623'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Event</h2>
<h3 data-id="heading-1">Tips:原型继承的几种方式</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> EventEmitter = <span class="hljs-built_in">require</span>(<span class="hljs-string">'events'</span>);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Girl</span>(<span class="hljs-params"></span>) </span>&#123;&#125;

<span class="hljs-comment">// 原型继承的几种方式</span>
Girl.prototype.__proto__ = EventEmitter.prototype;

<span class="hljs-built_in">Object</span>.setPrototypeOf(Girl.prototype, EventEmitter.prototype);

Girl.prototype = <span class="hljs-built_in">Object</span>.create(EventEmitter.prototype);

<span class="hljs-comment">// create的实现</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">create</span>(<span class="hljs-params">proto</span>) </span>&#123;
  <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Fn</span>(<span class="hljs-params"></span>) </span>&#123;&#125;

  Fn.prototype = proto;

  <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> Fn();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">node 中的发布订阅</h3>
<ul>
<li>
<p>on订阅 emit触发 once订阅一次 off取消订阅</p>
</li>
<li>
<p>node 中原型继承的实现： <code>util.inherits(Girl, EventEmitter)</code> (内部是通过 setPrototypeOf 实现的)</p>
</li>
<li>
<p>使用</p>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> EventEmitter = <span class="hljs-built_in">require</span>(<span class="hljs-string">'events'</span>);

<span class="hljs-keyword">const</span> util = <span class="hljs-built_in">require</span>(<span class="hljs-string">'util'</span>);

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Girl</span>(<span class="hljs-params"></span>) </span>&#123;&#125;

<span class="hljs-comment">// 原型继承 需要通过实例来调用继承的方法</span>
util.inherits(Girl, EventEmitter);

<span class="hljs-keyword">let</span> girl = <span class="hljs-keyword">new</span> Girl();

<span class="hljs-comment">// 订阅</span>
girl.on(<span class="hljs-string">'brokenheart'</span>, <span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'cry'</span>);
&#125;);
girl.on(<span class="hljs-string">'brokenheart'</span>, <span class="hljs-function">(<span class="hljs-params">a, b</span>) =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'eat'</span>);
&#125;);
<span class="hljs-comment">//触发</span>
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
  girl.emit(<span class="hljs-string">'brokenheart'</span>, <span class="hljs-string">'a'</span>, <span class="hljs-string">'b'</span>);
&#125;, <span class="hljs-number">1000</span>);

<span class="hljs-comment">// 订阅</span>
<span class="hljs-keyword">const</span> fn = <span class="hljs-function">() =></span> &#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'shopping'</span>);
&#125;;
girl.once(<span class="hljs-string">'brokenheart'</span>, fn);

<span class="hljs-comment">//触发</span>
<span class="hljs-built_in">setTimeout</span>(<span class="hljs-function">() =></span> &#123;
  <span class="hljs-comment">// 如果先移除绑定一次的事件，再执行，因为绑定的是one，移除的是fn，所以要给one上绑定原事件函数</span>
  girl.off(<span class="hljs-string">'brokenheart'</span>, fn);

  girl.emit(<span class="hljs-string">'brokenheart'</span>, <span class="hljs-string">'a'</span>, <span class="hljs-string">'b'</span>);
&#125;, <span class="hljs-number">1000</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">EventEmitter 的实现</h2>
<ul>
<li>要能手写</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">EventEmitter</span>(<span class="hljs-params"></span>) </span>&#123;
  <span class="hljs-built_in">this</span>._events = &#123;&#125;;
&#125;
EventEmitter.prototype.on = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">eventName, callback</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._events) &#123;
    <span class="hljs-comment">// this是girl的实例，要把_events绑定到girl上</span>
    <span class="hljs-built_in">this</span>._events = &#123;&#125;;
  &#125;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._events[eventName]) &#123;
    <span class="hljs-built_in">this</span>._events[eventName].push(callback);
  &#125; <span class="hljs-keyword">else</span> &#123;
    <span class="hljs-built_in">this</span>._events[eventName] = [callback];
  &#125;
&#125;;
EventEmitter.prototype.emit = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">eventName, ...args</span>) </span>&#123;
  <span class="hljs-built_in">this</span>._events[eventName].forEach(<span class="hljs-function">(<span class="hljs-params">fn</span>) =></span> fn(...args));
&#125;;
EventEmitter.prototype.off = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">eventName, callback</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>._events && <span class="hljs-built_in">this</span>._events[eventName]) &#123;
    <span class="hljs-built_in">this</span>._events[eventName] = <span class="hljs-built_in">this</span>._events[eventName].filter(
      <span class="hljs-function">(<span class="hljs-params">fn</span>) =></span> fn !== callback && fn.l !== callback
    );
  &#125;
&#125;;
EventEmitter.prototype.once = <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">eventName, callback</span>) </span>&#123;
  <span class="hljs-comment">// 执行完毕后移除</span>
  <span class="hljs-keyword">const</span> one = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-comment">// AOP</span>
    callback();
    <span class="hljs-built_in">this</span>.off(eventName, one);
  &#125;;
  one.l = callback; <span class="hljs-comment">// 关联上原始事件 用于事件移除时判断</span>

  <span class="hljs-built_in">this</span>.on(eventName, one);
&#125;;
<span class="hljs-built_in">module</span>.exports = EventEmitter;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">Buffer</h2>
<h3 data-id="heading-5">进制的概念</h3>
<ul>
<li>早期前端是无法直接读取文件操作文件的 （node 是使用在服务端）对文件和前端传递过来的数据进行处理</li>
<li>前端传递过来的是二进制数据</li>
<li>进制数据: 所有内容都是以二进制来存储</li>
<li>node 需要将这个数据读取出来，将数据存储到需要的位置（如硬盘），在内存中的表现都是以二进制来表现的
<blockquote>
<p>0.1 + 0.2 !== 0.3
最终数据都是以二进制来存储的，所以会出现不精准的情况</p>
</blockquote>
</li>
</ul>
<h3 data-id="heading-6">二进制和十进制的区别</h3>
<ul>
<li>
<p>十进制中最大的是 9</p>
</li>
<li>
<p>二进制中最大的是 1</p>
</li>
<li>
<p>以字节为单位存储数据 1024 字节 => 1k 1024k => 1m</p>
</li>
<li>
<p>一个字节由 8 个位组成，里面都是二进制数</p>
</li>
<li>
<p>其他进制转化为十进制：当前位的值 * 进制^当前所在位， 把每一位进行相加</p>
</li>
<li>
<p>所以一个字节最大就是 11111111（8 个 1）， 最大能表示的十进制数为 255， 0-255 就是一个字节的取值范围</p>
</li>
<li>
<p>将十进制转换成二进制：取余 倒着组合</p>
</li>
<li>
<p><strong><em>parseInt 可以将其他进制转换为十进制: parseInt('101', 2); 参数 2 用来表示前面的 101 是一个二进制的数</em></strong> 数</p>
</li>
<li>
<p><strong><em>0b 二进制 0x 十六进制</em></strong></p>
</li>
<li>
<p><strong><em>(0x64).toString(2) 十六进制转二进制 将任意进制转换成任意进制</em></strong> 字符串</p>
</li>
<li>
<p>小数也要转化成 2 进制</p>
<blockquote>
<p>10 进制中的 0.5 是 2 进制中的 0.1（因为 10 => 0.5 20 倍 所以 2 => 0.1 20 倍）
十进制小数转为二进制的方法：乘 2 取整法可以将一个小数转化成 2 进制数</p>
</blockquote>
</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 0.1 + 0.2的问题</span>

<span class="hljs-number">0.1</span> * <span class="hljs-number">2</span> = <span class="hljs-number">0.2</span> <span class="hljs-number">0</span>
<span class="hljs-number">0.2</span> * <span class="hljs-number">2</span> = <span class="hljs-number">0.4</span> <span class="hljs-number">0</span>
<span class="hljs-number">0.4</span> * <span class="hljs-number">2</span> = <span class="hljs-number">0.8</span> <span class="hljs-number">0</span>
<span class="hljs-number">0.8</span> * <span class="hljs-number">2</span> = <span class="hljs-number">1.6</span> <span class="hljs-number">1</span>
<span class="hljs-number">0.6</span> * <span class="hljs-number">2</span> = <span class="hljs-number">1.2</span> <span class="hljs-number">1</span>
<span class="hljs-number">0.1</span> * <span class="hljs-number">2</span> = <span class="hljs-number">0.2</span> <span class="hljs-number">0</span>
<span class="hljs-number">0.2</span> * <span class="hljs-number">2</span> = <span class="hljs-number">0.4</span> <span class="hljs-number">0</span>
<span class="hljs-number">0.4</span> * <span class="hljs-number">2</span> = <span class="hljs-number">0.8</span> <span class="hljs-number">0</span>
<span class="hljs-number">0.8</span> * <span class="hljs-number">2</span> = <span class="hljs-number">1.6</span> <span class="hljs-number">1</span>
<span class="hljs-number">0.6</span> * <span class="hljs-number">2</span> = <span class="hljs-number">1.2</span> <span class="hljs-number">1</span>

<span class="hljs-comment">// 0.1转为二进制是一个无穷尽的小数</span>
<span class="hljs-comment">// 0.1转为二进制进行存储的时候会稍微比0.1大一点</span>
<span class="hljs-comment">// 0.2也是这样</span>
<span class="hljs-comment">// 所以 0.1 + 0.2 会大于 0.3</span>

<span class="hljs-built_in">console</span>.log(<span class="hljs-number">0.1</span>+<span class="hljs-number">0.2</span>) <span class="hljs-comment">// 考察的是进制转化的问题</span>

<span class="hljs-comment">// js没有将小数转化成2进制方法</span>
<span class="hljs-comment">// 为什么 0.2+0.2 没有问题？</span>

<span class="hljs-comment">// 如果出现精度问题怎么解决？</span>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            