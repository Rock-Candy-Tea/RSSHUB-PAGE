
---
title: '从【if...else...】到【责任链】再到【composeAOP】，顺带把【传参】解决了~'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://s3.jpg.cm/2021/08/14/Icu1LE.md.jpg'
author: 掘金
comments: false
date: Sun, 15 Aug 2021 16:09:33 GMT
thumbnail: 'https://s3.jpg.cm/2021/08/14/Icu1LE.md.jpg'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:24px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 40px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-top:6px solid #2f845e&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:4px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body del&#123;color:#2f845e&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">🐛嵌套毛毛虫</h2>
<p>我猜你一定见过这样的代码：</p>
<pre><code class="copyable">if(condition1 === A1)&#123;
    if(condition2 === A2)&#123;
        ...
    &#125;else if(condition2 === B2)&#123;
        ...
    &#125;else if(condition2 === C2)&#123;
        ...
    &#125;else&#123;
        ...
    &#125;
&#125;esle if(condition1 === B1)&#123;
    ...
    ...
    ...
&#125;else if(condition1 === C1)&#123;
    ...
    ...
    ...
&#125;else if(condition1 === D1)&#123;
    ...
    ...
    ...
&#125;else&#123;
    ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>讲真，并不是说这个代码有多坏，但是每次看到的时候都会引起本瓜不适。</p>
<p>感觉它就像是一只毛毛虫。。。</p>
<p>为了形象的表达这一点，本瓜诚邀灵魂画师 <a href="https://juejin.cn/user/3245414492684568" target="_blank" title="https://juejin.cn/user/3245414492684568">守护安东尼</a> 作示意图一张，salute！！（￣︶￣）↗　</p>
<p><img src="https://s3.jpg.cm/2021/08/14/Icu1LE.md.jpg" alt="Icu1LE.md.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><sup>* 图片来源：守护安东尼，未经允许，随意转载。</sup></p>
<p>这样写，总是会伴随着各种各样的逻辑判断、隐式输入、输出，还真不太敢动它，担心它直接“死”给你看！</p>
<h2 data-id="heading-1">🌴责任链竹节</h2>
<p>镜头转向【责任链】，它是 23 种设计模式之一，属于行为型模式，关注对象之间的交互、通信；</p>
<p>参数输入到一个初始函数中，如果不满足当前函数条件，则传递到下一函数中进行处理，满足停止，不满足再传递，这样 one by one 向后进行，直至满足条件或传递结束。</p>
<p>一个个元函数就像是一节节竹节，独立可拆卸、再任意组装；</p>
<p>闲话少说，实现它的代码大致是这样的：</p>
<pre><code class="copyable">function A1(condition1)&#123;
    chainA2.next(chainB2).next(chainC2);
    return condition1 === A1 ? chainA2.setParam(condition2) : 'doNext'
&#125;

function B1(condition1)&#123;
    return condition1 === B1 ? ... : 'doNext'
&#125;

function C1(condition1)&#123;
   return condition1 === C1 ? ... : 'doNext'
&#125;

function D1(condition1)&#123;
   return condition1 === D1 ? ... : 'doNext'
&#125;

...

function A2(condition2)&#123;
    return condition2 === A2 ? ... : 'doNext'
&#125;

function B2(condition2)&#123;
   return condition2 === B2 ? ... : 'doNext'
&#125;

function C2(condition2)&#123;
   return condition2 === C2 ? ... : 'doNext'
&#125;

chainA1.next(chainB1).next(chainC1).next(chainD1)

chainA1.setParam(condition1)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>整体感官上，是不是像竹子一样？每一节（函数输入、输出）特别清晰。关键是，它解耦了，组装起来也超级方便~</p>
<p><img src="https://s3.jpg.cm/2021/08/15/IcHbcQ.md.jpg" alt="IcHbcQ.md.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><sup>* 图片来源：守护安东尼，未经允许，随意转载。</sup></p>
<p><strong>核心的</strong>，生成 Chain 的代码如下：</p>
<p>Chain 函数是高级函数，入参是一个函数。这里通过原型链的方式给它加了 next、setParam 两个属性。next 的入参也是 fn，用于设置下一个处理函数，setParam 用于传递原始入参；</p>
<pre><code class="copyable">var Chain = function( fn )&#123;
  this.fn = fn;
  this.successor = null;
&#125;;
Chain.prototype.next = function( successor )&#123;
  return this.successor = successor;
&#125;;
Chain.prototype.setParam = function()&#123;
  var ret = this.fn.apply( this, arguments );
  if ( ret === 'doNext' )&#123;
    return this.successor && this.successor.setParam.apply( this.successor, arguments );
  &#125;
  return ret;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">🍜函数特性AOP</h2>
<p>实际上，利用 JavaScript 的函数式特性，还有一种更加方便的方法来创建责任链 —— 即 AOP。</p>
<p>面向切面编程（AOP：Aspect Oriented Program）思想的简单理解：<strong>动态地将代码切入到类的指定方法、指定位置上的编程思想就是面向切面的编程。</strong></p>
<p>代码如下：</p>
<pre><code class="copyable">/**
 * 函数交织（AOP）
 * @param &#123;*&#125; fn
 * @returns
 */

Function.prototype.before = function(fn) &#123;
  const self = this
  return function(...args) &#123;
    const result = fn.apply(null, args)
    return self.call(null, result)
  &#125;
&#125;

Function.prototype.after = function(fn) &#123;
  const self = this
  return function(...args) &#123;
    const result = self.apply(null, args)
    return fn.call(null, result)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>调用示例:</p>
<pre><code class="copyable">fn1 = step2.before(init).after(step3).after(step4)

//fn1 = init -> step2 -> step3 -> step4
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们可以任意指定、搭配函数的执行先后关系；</p>
<h2 data-id="heading-3">🥂composeAOP</h2>
<p>还记得<a href="https://juejin.cn/post/6989020415444123662" target="_blank" title="https://juejin.cn/post/6989020415444123662">《感谢 compose 函数，让我的代码屎山💩逐渐美丽了起来~》</a>这篇文章吗？compose 其实有很多种写法！我们可以借助上面的 before 和 after 函数实现这一版的 composeAOP ~</p>
<pre><code class="copyable">const composeAOP = function(...args) &#123;
  const before = args.pop()
  const start = args.pop()
  if (args.length) &#123;
    return args.reduce(function(f1, f2) &#123;
      return f1.after(f2)
    &#125;, start.before(before))
  &#125;
  return start.before(before)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对了，回答之前有不少人问为啥 compose 是从右至左执行？？</p>
<pre><code class="copyable">const compose = function(...args) &#123;
  if (args.length) &#123;
    return args.reverse().reduce(function(f1, f2) &#123;
      return f1.after(f2)
    &#125;)
  &#125;
&#125;

compose(step4,step3,step2,step1,init)("start")
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里说一下：原因是它模拟了通常情况下函数逐层调用，层层包裹的顺序，像剥洋葱一样，从外而内，从右至左去解析：</p>
<pre><code class="copyable">step4(step3(step2(step1(init(...args))))) // 一层层括号像极了洋葱皮
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果你喜欢从左至右，或换 <code>pop()</code> 为 <code>shift()</code> ，或去掉那层 <code>reverse()</code> 即可，或改 <code>after</code> 为 <code>before</code>......顺序问题，无关好坏，<strong>全凭喜好~</strong></p>
<h2 data-id="heading-4">🎯传参问题！！</h2>
<p>如果你有心在控制台试试以上代码，不难发现其中的一个很严重的传参问题！！这个问题在《compose 优化屎山》那篇文章实际上也存在，也有细心的掘友反馈。</p>
<pre><code class="copyable">function init(...args)&#123;
    console.log(args)
    return [...args,"init"]
&#125;
function step1(...args)&#123;
    console.log(args)
    return [...args,"step1"]
&#125;
function step2(...args)&#123;
    console.log(args)
    return [...args,"step2"]
&#125;
function step3(...args)&#123;
    console.log(args)
    return [...args,"step3"]
&#125;

compose(step3,step2,step1,init)("start")
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>随着参数的传递，args 数组的维度在不断上升。</strong></p>
<p><img src="https://s3.jpg.cm/2021/08/15/IcSSVw.md.png" alt="IcSSVw.md.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果我们使用 <code>flat(Infinity)</code> 拉平数组，传参就变成了这样：</p>
<p><img src="https://s3.jpg.cm/2021/08/15/IcSB8R.md.png" alt="IcSB8R.md.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样做有一个很大的问题就是：需要对照数组的传参顺序！这是很头疼的，因为保不定哪天就要增删改流程参数。</p>
<p>所以，期望是能换成对象作传参，<strong>消除按顺序传参的桎梏</strong>。比如：</p>
<pre><code class="copyable">&#123;start:"start",init:"init",step1:"step1"......&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>直接动手试试：</p>
<pre><code class="copyable">function init(...args)&#123;
    console.log(JSON.stringify(args))
    return &#123;args:args,init:"init"&#125;
&#125;
function step1(...args)&#123;
    console.log(JSON.stringify(args))
    return &#123;args:args,step1:"step1"&#125;
&#125;
function step2(...args)&#123;
    console.log(JSON.stringify(args))
    return &#123;args:args,step2:"step2"&#125;
&#125;
function step3(...args)&#123;
    console.log(JSON.stringify(args))
    return &#123;args:args,step3:"step3"&#125;
&#125;

compose(step3,step2,step1,init)("start")
<span class="copy-code-btn">复制代码</span></code></pre>
<p>得到：
<img src="https://s3.jpg.cm/2021/08/15/Icr8nW.md.png" alt="Icr8nW.md.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>显然这不是我们想要的，我们得再不断打印寻找规律：</p>
<p><img src="https://s3.jpg.cm/2021/08/15/Ics52e.md.png" alt="Ics52e.md.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>哇噢~</p>
<p>在 <code>step3</code> 中想获取 <code>step1</code>，就要 2 个 <code>.args[0]</code>；</p>
<p><img src="https://s3.jpg.cm/2021/08/15/Icse45.md.png" alt="Icse45.md.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在 <code>step2</code> 中想获取 <code>step1</code>，只要 1 个 <code>.args[0]</code>；</p>
<p><img src="https://s3.jpg.cm/2021/08/15/IcslDC.md.png" alt="IcslDC.md.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们基本可以推出：<strong>想获得前 N 步的参数，只需带 N 个 <code>.args[0]</code></strong></p>
<p>于是乎，我们可以尝试写一个 <code>getCountStepAttr()</code> 函数，用于在某个函数步骤中，获得前第 N 步的入参，通过调用对象属性的方式！</p>
<p>来吧，展翅~</p>
<pre><code class="copyable">function getCountStepAttr(args,N)&#123;
    // 需要前第几（N）步的参数
    N = N -1
    let resObj = args[0]
    for(let i =0;i<N;i++)&#123;
        resObj = resObj.args[0]
    &#125;
    return resObj
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>直接就可以测试使用了：</p>
<p><img src="https://s3.jpg.cm/2021/08/15/Icshuy.md.png" alt="Icshuy.md.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">🖖完整代码</h2>
<p>贴下完整代码，你可以拷贝在控制台玩一玩看看，本瓜相信你一定会有所收获！！</p>
<pre><code class="copyable">Function.prototype.after = function(fn) &#123;
  const self = this
  return function(...args) &#123;
    let result = self.apply(null, args)
    return fn.call(null,result)
  &#125;
&#125;
const compose = function(...args) &#123;
  if (args.length) &#123;
    return args.reverse().reduce(function(f1, f2) &#123;
      return f1.after(f2)
    &#125;)
  &#125;
&#125;
const getCountStepAttr = function(args,N)&#123;
    // 获取前 N 步的入参；
    N = N -1
    let resObj = args[0]
    for(let i =0;i<N;i++)&#123;
        resObj = resObj.args[0]
    &#125;
    return resObj
&#125;
function init(...args)&#123;
    console.log("【在 init 中调用原始传参】：",getCountStepAttr(args,1))
    return &#123;args:args,init1:"init1",init:"init"&#125;
&#125;
function step1(...args)&#123;
    return &#123;args:args,step1:"step1"&#125;
&#125;
function step2(...args)&#123;
    return &#123;args:args,step2:"param-step2",step2Add:"param-step2-add"&#125;
&#125;
function step3(...args)&#123;
    console.log("【在 step3 中调用 step2 的传参】：",getCountStepAttr(args,1).step2 , getCountStepAttr(args,1).step2Add)
    console.log("【在 step3 中调用 init 的传参】：",getCountStepAttr(args,3).init , getCountStepAttr(args,3).init1)
    console.log("【在 step3 中调用原始传参】：",getCountStepAttr(args,4))
    return &#123;args:args,step3:"step3"&#125;
&#125;
compose(step3,step2,step1,init)("start")
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">🐵小结展望</h2>
<p>本篇在讲什么？</p>
<p>其实还是那金光闪闪的五个大字：<strong>函数式编程</strong>。</p>
<p>我们将过程中的命令式代码用一个个简单的纯函数进行封装，最后组合成各种丰富的功能。</p>
<p>你可以在这个过程中，或任意拆卸、或增添补充、或重构设计，真的不用太担心隐藏的逻辑错漏或耦合造成的复杂业务难梳理！</p>
<p>我们用函数的输入、输出表达映射关系，用函数名表达函数内的功能实现，用参数的传递表达业务逻辑，用封闭的作用域环境构造干净的代码~</p>
<p>当然，你或许还有很多好的想法，<strong>代码的干净之路</strong> 还有很长一段要走！高山仰止，景行行止，虽不能至，心向往之。再说，能不能“至”还真不一定呢！</p>
<p>都看到这里，不如点个赞吧 👍👍👍 撰文不易，多谢鼓励 👏👏👏</p>
<p>欢迎点赞、收藏、评论~</p>
<blockquote>
<p>我是掘金安东尼，公众号同名，输出暴露输入，技术洞见生活，再会~</p>
</blockquote></div>  
</div>
            