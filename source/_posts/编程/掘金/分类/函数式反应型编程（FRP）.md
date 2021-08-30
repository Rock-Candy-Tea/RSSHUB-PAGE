
---
title: '函数式反应型编程（FRP）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9004345cefb4110a081ed49c75ec938~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 30 Aug 2021 01:04:39 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9004345cefb4110a081ed49c75ec938~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>当我们开始写项目的时候，总会遇到一些情景，比如定时任务，ajax请求，要求我们去请求大的文件或者图片这些，然后我们就发现，直接写代码，会出现加载缓慢，白屏这样的问题，众所周知，js是单线程的，所以js任务也是一个一个顺序执行的，就是同步执行，后一个任务必须等待前一个任务完成之后才能执行，就如前面所说的，如果前一个任务花费的时间很长，就会造成阻塞，给用户带来不好的体验，我们要解决这些问题，当我们等待但是又不要阻塞程序，所以就需要异步处理这些耗时间的任务。</p>
<h2 data-id="heading-1">1.处理异步的方法</h2>
<p>假设有多个异步任务，且任务有依赖关系，后一个任务必须拿到前一个任务的执行结果才可以执行</p>
<p>作为刚刚入门学习的小白，比如我，最先能想到的就是函数调用了</p>
<h3 data-id="heading-2">（1）回调：容易造成回调地狱</h3>
<p>回调是实现异步编程最简单的方法，我们可以在一个函数中调用其他函数，实现我们想要的逻辑</p>
<pre><code class="copyable">getData1(data1 => &#123;
  getData2(data1, data2 => &#123;
    getData3(data2, data3 => &#123;
      getData4(data3, data4 => &#123;
        getData5(data4, data5 => &#123;
          // 终于取到data5了
        &#125;)
      &#125;)
    &#125;)
  &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看见了你的代码，直接暴走。</p>
<p>为了让代码更具备可读性，Promise隆重登场。</p>
<h3 data-id="heading-3">（2）Promise:解决回调地狱</h3>
<p>依旧来解决上面的问题</p>
<pre><code class="copyable">getData1(data1)
.then(data1 => &#123;
   return getData2(data1);
&#125;)
.then(data2 => &#123;
   return getData3(data2);
&#125;)
.then(data3 => &#123;
   return getData4(data3);
&#125;)
.then(data4 => &#123;
   return getData(data4);
&#125;)
.catch(err => &#123;
    console.log(err);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们直接一路链式调用，看起来更清楚明了，但是感觉这样调用也不是个办法。</p>
<p>你的上级询问，那还能做的更优雅吗？这可难住了我，喔喔喔，但是不要怕，es5的回调让我陷入地狱，但是我爬起来了，es6的Promise让我得到夸奖，es7这不是又出了好方法吗？让我们接下来看看es7的async/await吧。</p>
<h3 data-id="heading-4">（3）async/await:简化了逻辑，但是损失了异步带来的性能优势（比如把并行变成串行,增加了时间开销）</h3>
<pre><code class="copyable">// 定义一个执行Async函数方法
async function getSSQ () &#123;
   let a = await getData1(data1)
   let b = await getData2(a)
   let c = await getData3(b)
   let d = await getData4(c)
   let e = await getData5(d)
   console.log(d);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>确实好用，也可以使用try..catch了,啊，这你想肯定能满足上级的要求了，又简单又优雅，小白一眼就看懂，async/await带着我走向了人生巅峰。</p>
<h3 data-id="heading-5">（4）各个方法优缺点总结</h3>

























<table><thead><tr><th>方法</th><th>优点</th><th>缺点</th></tr></thead><tbody><tr><td>回调</td><td>简单逻辑处理很方便</td><td>逻辑复杂时容易造成回调地狱</td></tr><tr><td>Promise</td><td>1.状态改变就不会再变，任何时候都能得到确切的结果 2.写法符合思维逻辑</td><td>1.一旦创建，立即执行，中途无法取消 2.处于pending状态时，无法得知状态3.不设置回调函数，内部错误无法反映到外部</td></tr><tr><td>Async/await</td><td>1. 做到了串行的同步写法 2.代码清晰明了</td><td>1.做不到并行，除非await不在一个函数里面 2.没有了promise的方法，比如race() 3.没有Promise的reject方法，得写在try...catch中</td></tr></tbody></table>
<p>代码非常简洁易读了，但是学海无涯，我发现现在有了一个新的技术，叫做FRP，看了一些文章，文章里面一直说<strong>有了FRP，就使用流来处理异步，把异步数据看成数据流来处理</strong>，会让事情更简单</p>
<p>那FRP到底是什么呢？</p>
<h2 data-id="heading-6">2.FRP是什么</h2>
<p>首先让我们先使用FRP直接实现上述的需求</p>
<pre><code class="copyable"> function getSSQ() &#123;
        let data1 = 1;
        return rxjs.from(getData(data1)).pipe(
            rxjs.operators.mergeMap(a =>
                rxjs.from(getData(a))
            ),
            rxjs.operators.mergeMap(b =>
                rxjs.from(getData(b))
            ),
            rxjs.operators.mergeMap(c =>
                rxjs.from(getData(c))
            ),
            rxjs.operators.tap(console.log),
            rxjs.operators.mergeMap(d =>
                rxjs.from(getData(d))
            ),
            rxjs.operators.tap(e => &#123;
            &#125;),
        );
    &#125;
    getSSQ().subscribe(&#123;
        // next(x) &#123; console.log('got value ' + x); &#125;,
        // error(err) &#123; console.error('something wrong occurred: ' + err); &#125;,
        complete() &#123; console.log('done'); &#125;
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看不懂吧，看不懂没关系，只需要知道from是建立流的，mergeMap()是操作流的，subscribe是订阅流的，最后直接输出结果就好了，我们先来了解一下什么是FRP及实际应用，重点是学习FRP不同的思维方式</p>
<h3 data-id="heading-7">（1）概念</h3>
<p>FRP(Functional Reactive Programming),也叫函数式响应式编程</p>
<p>函数反应式编程 = 函数式编程（Functional programming）+响应式编程（Reactive Programming）</p>
<p>如果不知道函数式编程的朋友，推荐看这个<a href="https://link.juejin.cn/?target=https%3A%2F%2Fllh911001.gitbooks.io%2Fmostly-adequate-guide-chinese%2Fcontent%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://llh911001.gitbooks.io/mostly-adequate-guide-chinese/content/" ref="nofollow noopener noreferrer">编程指南</a>，这边主要讲解响应式编程</p>
<pre><code class="copyable">响应式编程使用异步数据流编程，即将各种数据【包括http请求、DOM事件等】包装成流的形式，用操作符对流进行操作，能用同步方式处理异步数据
<span class="copy-code-btn">复制代码</span></code></pre>
<p>光看这个概念，我是完全没法看明白的，所以需要拆开来看</p>
<h3 data-id="heading-8">（2）数据流是什么？</h3>
<p>数据流是按时间排序的即将发生的事情的序列</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9004345cefb4110a081ed49c75ec938~tplv-k3u1fbpfcp-watermark.image" alt="image-20210824202121821.png" loading="lazy" referrerpolicy="no-referrer">
举个例子，我们写代码时，会对数据进行转换运算，比如先转成什么再转成什么再转成什么，转换这整个过程相当于一个流着数据的管道，数据以流的方式在这个管道中流通，这些数据转换我们会使用各种方法，相当于传入数据作为函数参数转换后得到新数据结果，最后的结果从管道中流出。</p>
<p>流转换的思想为将数据事件抽象成管道中流通的流体，转换成新的数据事件，这些事件还包含了基本的数据值，还可以进行相应的运算，这种运算让我们不需要花时间去进行事件监听什么的，我们只需要专注于数据的转换，也就是事件的使用,而不是直接操作数据。</p>
<p>所以我们在学习这章内容的时候，还应该学会转换思维。</p>
<p>总体思想：什么都可以是流，变量，用户输入，属性，高速缓存，数据结构等，将时间线上的数据建模成流</p>
<h3 data-id="heading-9">（2）响应式是什么？变化传递（跟着变化）</h3>
<p>vue就是响应式编程，我们只需要关注数据变化，不需要操作视图改变，因为视图会跟着改变</p>
<h3 data-id="heading-10">（3）观察者模式</h3>
<p>是一种设计模式，允许定义一种订阅机制，可以在对象事件发生时通知多个观察的该对象的其他对象</p>
<p>比如你花钱了之后银行会给你发消息，就是观察者模式，余额是被观察的对象，用户是观察者</p>
<h3 data-id="heading-11">（4）迭代器模式</h3>
<p>游标模式，挨着挨着一步一步运行</p>
<p>比如map,set,array都使用了迭代器模式</p>
<h2 data-id="heading-12">3.使用案例</h2>
<p>前端的FRP的库：Rxjs【比较多人使用】、Most，后续内容使用Rxjs</p>
<p>Rxjs中文文档：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.rx.js.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.rx.js.org/" ref="nofollow noopener noreferrer">cn.rx.js.org/</a></p>
<p>Rxjs英文文档：<a href="https://link.juejin.cn/?target=https%3A%2F%2Frxjs.dev%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://rxjs.dev/" ref="nofollow noopener noreferrer">rxjs.dev/</a></p>
<p>让我们学习几个小案例，来体会FRP的魅力吧~~</p>
<p>可引入也可以使用npm安装：</p>

<p>RxJS 是一个库，它通过使用 observable 序列来编写异步和基于事件的程序。它提供了一个核心类型 Observable，附属类型 (Observer、 Schedulers、 Subjects) 和操作符 (map、filter、reduce、every, 等等)，这些数组操作符可以把异步事件作为集合来处理。</p>
<p>基本概念：</p>
<ul>
<li><strong>Observable (可观察对象):</strong> 表示一个概念，这个概念是一个可调用的未来值或事件的集合。</li>
<li><strong>Observer (观察者):</strong> 一个回调函数的集合，它知道如何去监听由 Observable 提供的值。</li>
<li><strong>Subscription (订阅):</strong> 表示 Observable 的执行，主要用于取消 Observable 的执行。</li>
<li><strong>Operators (操作符):</strong> 采用函数式编程风格的纯函数 (pure function)，使用像 <code>map</code>、<code>filter</code>、<code>concat</code>、<code>flatMap</code> 等这样的操作符来处理集合。</li>
<li><strong>Subject (主体):</strong> 相当于 EventEmitter，并且是将值或事件多路推送给多个 Observer 的唯一方式。</li>
<li><strong>Schedulers (调度器):</strong> 用来控制并发并且是中央集权的调度员，允许我们在发生计算时进行协调，例如 <code>setTimeout</code> 或 <code>requestAnimationFrame</code> 或其他。</li>
</ul>
<p>借用官网第一个例子入门</p>
<p>注册事件监听器的常规写法如下</p>
<pre><code class="copyable">var button = document.querySelector('button');
button.addEventListener('click', () => console.log('Clicked!'));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用 RxJS 的话，创建一个 observable 来代替。</p>
<pre><code class="copyable">var button = document.querySelector('button');
Rx.Observable.fromEvent(button, 'click')
  .subscribe(() => console.log('Clicked!'));
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">（1）实现计数器</h3>
<p>a.以前实现计数器：</p>
<p>直接想实现方法，直接定义全局变量开始写实现细节,点击则全局变量+1然后打印，这是我们平时思考的正常思维</p>
<pre><code class="copyable">let counter = 0;
buttton.on("click", ()=>&#123;
    counter+=1;
    console.log(counter);
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>缺点：</p>
<p>使用了全局变量：容易被改变值，输入输出不确定性，后期维护困难等</p>
<p>b.有了FRP之后实现计数器：</p>
<ul>
<li>
<p>已知创建流的函数formEvent</p>
</li>
<li>
<p>已知操作流的函数：pipe、map、scan、subscribe</p>
<p>pipe:用于链接可观察的运算符</p>
</li>
</ul>
<p>map：类似于<strong>Array.prototypr.map()</strong> ，它把每个源值传递给转化函数以获得相应的输出值。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/880df2d300e24826abe160307cf39306~tplv-k3u1fbpfcp-watermark.image" alt="image-20210825103423821.png" loading="lazy" referrerpolicy="no-referrer">
scan:数组的 <strong>reduce</strong> 类似。它需要一个暴露给回调函数当参数的初始值。每次回调函数运行后的返回值会作为下次回调函数运行时的参数</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14dcfdd2ba864894b01b30c050e5a27a~tplv-k3u1fbpfcp-watermark.image" alt="image-20210825104008290.png" loading="lazy" referrerpolicy="no-referrer">
​subscribe:监听流，订阅流</p>
<p>我们先在api中找到了对应的方法，formEvent直接创建一个流->用pipe进行数据流的连接(在里面可以写事件的实现方法，我们只需要考虑怎么运用事件处理，而不需要直接去操作数据)->利用map进行初始化操作->scan进行数据相加操作->subscribe()方法订阅整个流，最后输出</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">rxjs.fromEvent(<span class="hljs-built_in">document</span>.querySelector(<span class="hljs-string">'.this'</span>), <span class="hljs-string">'click'</span>).pipe( <span class="hljs-comment">// 连接运算符</span>
        rxjs.operators.map(<span class="hljs-function">(<span class="hljs-params">_</span>) =></span> <span class="hljs-number">1</span>), <span class="hljs-comment">// 将原值全变为1，不用定义全局变量</span>
        rxjs.operators.scan(<span class="hljs-function">(<span class="hljs-params">sum, val</span>) =></span> &#123; <span class="hljs-comment">// 相加</span>
            <span class="hljs-keyword">return</span> sum + val;
        &#125;, <span class="hljs-number">0</span>)
    ).subscribe(<span class="hljs-function">(<span class="hljs-params">x</span>) =></span> &#123; <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'got value '</span> + x); &#125;); <span class="hljs-comment">//打印</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>​优点：</p>
<p>和直接操作数据相比，除了创建流之外，FRP不需要有全局变量，直接可操作</p>
<h3 data-id="heading-14">（2）实现双击</h3>
<p>例子：如果两次click之间的间隔时间小于等于250ms，为一次双击，否则为两次单击，请在单击、双击时分别log</p>
<p>以前实现双击：我们会考虑时间戳，判断点击事件的间隔时间是否小于等于250ms，然后进行判断，但是会出现问题，如果连点三次，判断上就会出现问题,或者设置标志位，但是不管哪种方式实现，都会有些困难</p>
<pre><code class="copyable"><input type="button" onclick="aa()" ondblclick="bb()" value="点我">  
<script language="javascript">  
var isdb;  //设置变量
function aa()&#123;  
    isdb=false;  //标志位
    window.setTimeout(cc, 250) //这里调用window
    function cc()&#123;  
        if(isdb!=false)return;  
        console.log("单击")  
    &#125;  
&#125;  
function bb()&#123;  
    isdb=true;  
    console.log("双击") 
&#125;  
</script>  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>FRP实现双击：</p>
<ul>
<li>已知操作流的函数：debounceTime、buffer、filter</li>
</ul>
<p>debounceTime：去抖动的作用，控制发送频率操作</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58fec4be85ad490b8d5d489abfbb8291~tplv-k3u1fbpfcp-watermark.image" alt="image-20210825110715526.png" loading="lazy" referrerpolicy="no-referrer">
buffer:将过往的值收集到一个数组中</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4670a70e7d648c193040c985a731f60~tplv-k3u1fbpfcp-watermark.image" alt="image-20210825111010619.png" loading="lazy" referrerpolicy="no-referrer">
filter:类似于 <strong>Array.prototype.filter()</strong>， 它只会发出符合标准函数的值。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b55264e239ff40208ebf4eb058b8b0ea~tplv-k3u1fbpfcp-watermark.image" alt="image-20210825111240904.png" loading="lazy" referrerpolicy="no-referrer">
双击事件也是操作api，有直接可以使用的去抖动方法debounceTime(),思考流程应该是点击事件创建流->然后这个流去抖动->收集去抖动的值->判断产生的每个数组长度，等于2就是双击，同理可得等于1就是单击</p>
<pre><code class="copyable">    var button = document.querySelector('.this');
    var clickStream = rxjs.fromEvent(button, 'click'); //创建流
​
    var doubleClickStream = clickStream.pipe(
        rxjs.operators.buffer( // 收集点击事件到数组中，
            clickStream.pipe(
                rxjs.operators.debounceTime(250)
            )
        ),
        rxjs.operators.map(function (list) &#123; return list.length; &#125;),//返回数组长度
        rxjs.operators.filter(function (x) &#123; //过滤出双击
            return x === 2;
        &#125;)
    );
    //同理 单击
    var singleClickStream = clickStream.pipe(
        rxjs.operators.buffer(
            clickStream.pipe(
                rxjs.operators.debounceTime(250)
            )
        ),
        rxjs.operators.map(function (list) &#123; return list.length; &#125;),
        rxjs.operators.filter(function (x) &#123; return x === 1; &#125;)
    );
    // 显示
    singleClickStream.subscribe(function (x) &#123;
        document.querySelector('h2').textContent = 'click';
    &#125;);
    doubleClickStream.subscribe(function (x) &#123;
        document.querySelector('h2').textContent = '' + x + 'x click';
    &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<hr>
<h3 data-id="heading-15">（3）实现拖动</h3>
<p>请使用mousedown、mousemove、mouseup事件来实现“鼠标拖动时，log：draging”</p>
<p>a.以前实现：<a href="https://link.juejin.cn/?target=http%3A%2F%2Fwww.phpzu.com%2Farticle%2F2014%2F05%2F27%2F407.html" target="_blank" rel="nofollow noopener noreferrer" title="http://www.phpzu.com/article/2014/05/27/407.html" ref="nofollow noopener noreferrer">js实现拖拽</a>，以前实现拖拽，起码是一两百行代码起步，而且逻辑判断上可能还会出现问题</p>
<p>b.现在FRP实现：</p>
<ul>
<li>
<p>已知操作流的函数：flatMap【现在已变成mergeMap】、takeUntil</p>
<p>flatmap:每个流进行运算然后合并输出</p>
</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df5629d1878e4f1bb2126b7b9d20e9de~tplv-k3u1fbpfcp-watermark.image" alt="image-20210825114601621.png" loading="lazy" referrerpolicy="no-referrer">
takeUntil:先发出一个流的值，直到第二个流发出值，就完成</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f8feb87e9a5341b6b83f1c0b80a32f6b~tplv-k3u1fbpfcp-watermark.image" alt="image-20210825133659532.png" loading="lazy" referrerpolicy="no-referrer">
但是当我们使用Rxjs实现的时候，代码实现就会变得很少，只需要几行就可以实现需求，如下所示【具体理解上可能会有些困难，学习具体的推荐从官方中文文档入手，比较详细】</p>
<pre><code class="copyable"> let mousedown = rxjs.fromEvent(document, 'mousedown');
   let mousemove = rxjs.fromEvent(document, 'mousemove');
    let mouseup = rxjs.fromEvent(document, 'mouseup');

mousedown.pipe(
        rxjs.operators.flatMap((_) => &#123;
            return mousemove.pipe(rxjs.operators.takeUntil(mouseup))
        &#125;)
    ).subscribe(() => &#123;
        console.log("draging");
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-16">4.为什么要使用FRP</h2>
<p>从处理异步的方法上，我们发现async/await并不擅长处理并行需求，虽然也可以处理，但是耗费时间多些，但是FRP操作符，对于并行串行都可以很适用</p>
<p>流处理方式的价值且远不止于此，对于事件处理也非常适用，响应式编程的思维方式也是非常有价值的一点</p>
<p>FRP的特性总结如下：</p>
<ul>
<li>
<h3 data-id="heading-17">纯净性 (Purity)</h3>
</li>
</ul>
<p>使得 RxJS 强大的正是它使用纯函数来产生值的能力。这意味着你的代码更不容易出错。</p>
<p>通常你会创建一个非纯函数，在这个函数之外也使用了共享变量的代码，这将使得你的应用状态一团糟。</p>
<ul>
<li>
<h3 data-id="heading-18">流动性 (Flow)</h3>
</li>
</ul>
<p>RxJS 提供了一整套操作符来帮助你控制事件如何流经 observables 。</p>
<h2 data-id="heading-19">5.总结</h2>
<h3 data-id="heading-20">（1）优点</h3>
<ul>
<li>
<p>抽象层面更高</p>
<p>FRP以流为单位，封装了时间序列和具体的数据，隐藏了“状态的同步”、“异步逻辑的具体实现”等底层细节。</p>
</li>
<li>
<p>和函数式编程配合使用</p>
<p>能够使用组合，像管道处理一样处理各种流，符合函数式编程的思维。</p>
</li>
<li>
<p>提供非阻塞、异步特性，便于处理异步情景，但是得是有非常复杂的异步情景时才适用，平时的简单异步请求，90%都是可以被async/await还有Promise解决的</p>
</li>
<li>
<p>避免模式混用，回调和promise混用、全局变量和局部变量混用，最后可能成为无尽的callback+Promise地狱</p>
</li>
<li>
<p>易于编写维护，及时响应</p>
</li>
</ul>
<p><strong>响应式编程可以加深你代码抽象的程度，让你可以更专注于定义与事件相互依赖的业务逻辑，而不是把大量精力放在实现细节上，同时，使用响应式编程还能让你的代码变得更加简洁。</strong></p>
<h3 data-id="heading-21">（2）缺点</h3>
<ul>
<li>学习成本高，需要转换思维，用流来思考</li>
</ul>
<p>最后的最后借用尤大大的一句话</p>
<pre><code class="copyable">我个人倾向于在适合 Rx 的地方用 Rx，但是不强求 Rx for everything。比较合适的例子就是比如多个服务端实时消息流，通过 Rx 进行高阶处理，最后到 view 层就是很清晰的一个 Observable，但是 view 层本身处理用户事件依然可以沿用现有的范式。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>FRP的思想和对事件操作的能力很不错，在需要使用的地方使用上会是锦上添花</p>
<h2 data-id="heading-22">6.参考文章</h2>
<p>1.<a href="https://juejin.cn/post/6844903885539147784" target="_blank" title="https://juejin.cn/post/6844903885539147784">Rxjs思想入门</a></p>
<p>2.<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmy.oschina.net%2Fu%2F2288602%2Fblog%2F359270" target="_blank" rel="nofollow noopener noreferrer" title="https://my.oschina.net/u/2288602/blog/359270" ref="nofollow noopener noreferrer">你一直都错过的反应型编程</a></p>
<p>3.<a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F104024245" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/104024245" ref="nofollow noopener noreferrer">Rxjs光速入门</a></p>
<p>4.<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwiki.jikexueyuan.com%2Fproject%2Fandroid-weekly%2Fissue-145%2Fintroduction-to-RP.html" target="_blank" rel="nofollow noopener noreferrer" title="https://wiki.jikexueyuan.com/project/android-weekly/issue-145/introduction-to-RP.html" ref="nofollow noopener noreferrer">响应式编程介绍</a></p></div>  
</div>
            