
---
title: 'XDM，JS如何函数式编程？看这就够了！（四）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5171'
author: 掘金
comments: false
date: Wed, 16 Jun 2021 00:13:16 GMT
thumbnail: 'https://picsum.photos/400/300?random=5171'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;overflow:hidden;line-height:1.75;font-size:15px;background-image:linear-gradient(90deg,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0),linear-gradient(1turn,rgba(72,42,10,.05) 5%,rgba(72,42,10,0) 0);background-size:20px 20px;background-position:50%;padding-top:0!important&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;position:relative;display:flex;border-bottom:5px solid #6d4e00;line-height:35px;letter-spacing:1px;font-size:25px;padding-left:25px;color:#664900;text-shadow:1px 1px 1px #8a6200;padding-bottom:0&#125;.markdown-body h1:before&#123;content:"";display:flex;position:absolute;left:0;top:3px;bottom:0;margin:auto;width:20px;height:20px;background-size:20px 20px;background-image:url("data:image/png;base64,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")&#125;.markdown-body h2&#123;position:relative;padding:0 0 0 20px;font-size:20px;font-weight:700;color:#614500&#125;.markdown-body h2:before&#123;content:"";position:absolute;top:3px;bottom:0;left:0;background-image:url("data:image/png;base64,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");background-size:100% 100%;background-repeat:no-repeat;width:15px;height:15px;margin:auto&#125;.markdown-body h3&#123;width:100%;text-align:left;margin:20px 10px 0 0;font-size:18px;font-weight:700;display:inline-block;padding-left:10px;padding-bottom:0;border-left:5px solid #8f6600;color:#614500&#125;.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-weight:700;color:#a37400&#125;.markdown-body h4&#123;font-size:17px&#125;.markdown-body h5,.markdown-body h6&#123;display:flex;align-items:center&#125;.markdown-body h5:after,.markdown-body h6:after&#123;display:inline-block;border:2px solid #fff6e0;color:rgba(189,134,0,.5);border-radius:50%;text-align:center;margin-left:5px&#125;.markdown-body h5&#123;font-size:14px&#125;.markdown-body h5:after&#123;content:"5";width:15px;height:15px;line-height:15px;font-size:13px&#125;.markdown-body h6&#123;font-size:12px&#125;.markdown-body h6:after&#123;content:"6";width:13px;height:13px;line-height:13px;font-size:12px&#125;.markdown-body p&#123;color:#412c0c;letter-spacing:1px;font-weight:400&#125;.markdown-body img&#123;max-width:100%;display:block;margin:auto&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#755300;font-weight:400;border-bottom:1px solid #755300;font-weight:bolder;text-decoration:none&#125;.markdown-body table&#123;width:100%!important;margin:0;font-size:12px;width:auto;max-width:100%;overflow:auto;border-collapse:collapse;border-spacing:0&#125;.markdown-body table img&#123;box-shadow:none&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body thead tr th&#123;text-align:center&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px;box-sizing:border-box;border:1px solid rgba(72,42,10,.1)&#125;.markdown-body blockquote&#123;position:relative;text-size-adjust:100%;line-height:25px;font-weight:400;border-radius:10px;font-style:normal;text-align:left;box-sizing:inherit;border:1px solid #ffd87a;background-color:rgba(189,134,0,.5);margin:20px 0;padding:20px&#125;.markdown-body blockquote p&#123;color:#fff6e0;letter-spacing:2px;margin:0&#125;.markdown-body blockquote:after,.markdown-body blockquote:before&#123;position:absolute;color:#cc9100;font-size:34px;font-weight:700&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:5px&#125;.markdown-body blockquote:after&#123;content:"❞";right:5px;bottom:-5px&#125;.markdown-body strong&#123;color:#c28a00;font-weight:bolder&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;color:#c28a00&#125;.markdown-body em strong&#123;font-style:normal;color:#c28a00;background-color:#8a6200&#125;.markdown-body s&#123;color:#c28a00&#125;.markdown-body hr&#123;border-top:1px solid #805b00&#125;.markdown-body code,.markdown-body li code,.markdown-body p code&#123;color:#996d00;background-color:rgba(130,98,0,.3)&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit;color:#858585;font-family:bold;letter-spacing:1px&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection,.markdown-body img::selection&#123;color:rgba(189,134,0,.5);background-color:#fff&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body pre>code::selection&#123;background-color:rgba(189,134,0,.5)&#125;.markdown-body .math .math-inline::selection,.markdown-body blockquote::selection,.markdown-body ol::selection,.markdown-body p::selection,.markdown-body strong::selection,.markdown-body table::selection,.markdown-body ul::selection&#123;background-color:rgba(189,134,0,.5)&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>不知不觉，我们已经来到了《JS如何函数式编程》系列的【第四篇】。</p>
<p>前三篇传送门：</p>
<ul>
<li><a href="https://juejin.cn/post/6968259661304692750" target="_blank">《XDM，JS如何函数式编程？看这就够了！（一）》</a></li>
<li><a href="https://juejin.cn/post/6969016132741103624" target="_blank">《XDM，JS如何函数式编程？看这就够了！（二）》</a></li>
<li><a href="https://juejin.cn/post/6971260867300032525" target="_blank">《XDM，JS如何函数式编程？看这就够了！（三）》</a></li>
</ul>
<p>经过前几篇的历练，本瓜相信你的心中一定对函数编程有了基本的蓝图。</p>
<p>本篇会将这个蓝图再具象一下，谈谈函数编程中一个很重要的细节 —— <strong>“副作用”</strong>。</p>
<ul>
<li>点赞富三代👍👍👍评论美一生🎉🎉🎉</li>
</ul>
<p>维基上关于副作用的解释：</p>
<blockquote>
<p>函数内部有隐式（Implicit）的数据流，这种情况叫做副作用（Side Effect）。</p>
</blockquote>
<p>咱们前文也提到过：<strong>开发人员喜欢显式输入输出而不是隐式输入输出。</strong></p>
<p>所以我们将细致的看看副作用中【隐式】和【显式】的区别!</p>
<h2 data-id="heading-0">何为副作用？</h2>
<p>先来个小例子作开胃菜：</p>
<pre><code class="copyable">// 片段 1
function foo(x) &#123;
    return x * 2;
&#125;

var y = foo( 3 );

// 片段 2
function foo(x) &#123;
    y = x * 2;
&#125;

var y;

foo( 3 );
<span class="copy-code-btn">复制代码</span></code></pre>
<p>片段 1 和片段 2 实现的最终效果是一致的，即 y = 3 * 2 ，但是片段 1 是显示的，片段 2 是隐式的。</p>
<p>原因是：片段 2 在函数内引用了外部变量 y。</p>
<p>片段 2 ，当我们调用 <code>foo( 3 )</code> 时，并不知道其内部是否会修改外部变量 y。它的修改是隐式的，即产生了副作用！</p>
<p><strong>有副作用的函数可读性更低，我们需要更多的阅读来理解程序。</strong></p>
<p>再举一例：</p>
<pre><code class="copyable">var x = 1;

foo();

console.log( x );

bar();

console.log( x );

baz();

console.log( x );
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果每个函数内都引用了 x ，有可能对其赋值修改，那么我们很难知道每一步 x 的值是怎样的，要每一步去追踪！</p>
<p>选择在一个或多个函数调用中编写带有（潜在）副作用的代码，那么这意味着你代码的读者必须将你的程序完整地执行到某一行，逐步理解。</p>
<p>如果 <code>foo()</code>、<code>bar()</code>、和 <code>baz()</code> 这三个函数没有（潜在）副作用，x 的值一眼可见！</p>
<p>一定是修改外部变量才是产生副作用了吗？</p>
<pre><code class="copyable">function foo(x) &#123;
    return x + y;
&#125;

var y = 3;

foo( 1 ); 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这段代码中，我们没有修改外部变量 y ，但是引用了它，也是会产生副作用的。</p>
<pre><code class="copyable">y = 5;

// ..

foo( 1 );   
<span class="copy-code-btn">复制代码</span></code></pre>
<p>两次 foo( 1 ) 的结果却不一样，又增大了阅读的负担。相信我，这是个最简单抽象的例子，实际的影响将远大于此。</p>
<h2 data-id="heading-1">避免副作用？</h2>
<ol>
<li>const</li>
</ol>
<p>以上面的例子来说：这样写，foo( 1 ) 的结果当然是确定的，因为用到了 const 来固定外部变量。</p>
<pre><code class="copyable">const y = 5;

// ..

foo( 1 );
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>I/O</li>
</ol>
<p>一个没有 I/O 的程序是完全没有意义的，因为它的工作不能以任何方式被观察到。一个有用的程序必须最少有一个输出，并且也需要输入。输入会产生输出。</p>
<p>还记得 foo(..) 函数片段 2 吗？没有输出 return，这是不太可取的。</p>
<pre><code class="copyable">// 片段 2
function foo(x) &#123;
    y = x * 2;
&#125;

var y;

foo( 3 );
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>明确依赖</li>
</ol>
<p>我们经常会由于函数的异步问题导致数据出错；一个函数引用了另外一个函数的回调结果，当我们作这种引用时要特别注意。</p>
<pre><code class="copyable">var users = &#123;&#125;;
var userOrders = &#123;&#125;;

function fetchUserData(userId) &#123;
    ajax( "http://some.api/user/" + userId, function onUserData(userData)&#123;
        users[userId] = userData;
    &#125; );
&#125;

function fetchOrders(userId) &#123;
    ajax( "http://some.api/orders/" + userId, function onOrders(orders)&#123;
        for (let i = 0; i < orders.length; i++) &#123;
                // 对每个用户的最新订单保持引用
            users[userId].latestOrder = orders[i];
            userOrders[orders[i].orderId] = orders[i];
        &#125;
    &#125; );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>fetchUserData(..)</code> 应该在 <code>fetchOrders(..)</code> 之前执行，因为后者设置 <code>latestOrder</code> 需要前者的回调；</p>
<p><strong>写出有副作用/效果的代码是很正常的</strong>， 但我们需要谨慎和刻意地避免产生有副作用的代码。</p>
<ol start="4">
<li>运用幂等</li>
</ol>
<p>这是一个很新但重要的概念！</p>
<p>从数学的角度来看，幂等指的是在第一次调用后，如果你将该输出一次又一次地输入到操作中，其输出永远不会改变的操作。</p>
<p>一个典型的数学例子是 Math.abs(..)（取绝对值）。Math.abs(-2) 的结果是 2，和 Math.abs(Math.abs(Math.abs(Math.abs(-2)))) 的结果相同。</p>
<p>幂等在 js 中的表现：</p>
<pre><code class="copyable">// 例 1
var x = 42, y = "hello";

String( x ) === String( String( x ) );                // true

Boolean( y ) === Boolean( Boolean( y ) );            // true

// 例 2
function upper(x) &#123;
    return x.toUpperCase();
&#125;

function lower(x) &#123;
    return x.toLowerCase();
&#125;

var str = "Hello World";

upper( str ) == upper( upper( str ) );                // true

lower( str ) == lower( lower( str ) );                // true

// 例 3
function currency(val) &#123;
    var num = parseFloat(
        String( val ).replace( /[^\d.-]+/g, "" )
    );
    var sign = (num < 0) ? "-" : "";
    return `$&#123;sign&#125;$$&#123;Math.abs( num ).toFixed( 2 )&#125;`;
&#125;

currency( -3.1 );                                    // "-$3.10"

currency( -3.1 ) == currency( currency( -3.1 ) );    // true
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实际上，<strong>我们在 js 函数式编程中幂等有更加宽泛的概念，即只用要求：<code>f(x) === f(f(x))</code></strong></p>
<pre><code class="copyable">// 幂等的：
obj.count = 2; // 这里的幂等性的概念是每一个幂等运算（比如 obj.count = 2）可以重复多次
person.name = upper( person.name );

// 非幂等的：
obj.count++;
person.lastUpdated = Date.now();

// 幂等的：
var hist = document.getElementById( "orderHistory" );
hist.innerHTML = order.historyText;

// 非幂等的：
var update = document.createTextNode( order.latestUpdate );
hist.appendChild( update );
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们不会一直用幂等的方式去定义数据，但如果能做到，这肯定会减少意外情况下产生的副作用。这需要时间去体会，我们就先记住它。</p>
<h2 data-id="heading-2">纯函数</h2>
<p>你应该听说过纯函数的大名，<strong>我们把没有副作用的函数称为纯函数。</strong></p>
<p>例 1：</p>
<pre><code class="copyable">function add(x,y) &#123;
    return x + y;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>输入（x 和 y）和输出（return ..）都是直接的，没有引用自由变量。调用 add(3,4) 多次和调用一次是没有区别的。add(..) 是纯粹的编程风格的幂等。</p>
<p>例 2：</p>
<pre><code class="copyable">const PI = 3.141592;

function circleArea(radius) &#123;
    return PI * radius * radius;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>circleArea 也是纯函数。虽然它调用了外部变量 PI ，但是 PI 是 const 定义的常量，引用常量不会产生副作用；</p>
<p>例 3：</p>
<pre><code class="copyable">function unary(fn) &#123;
    return function onlyOneArg(arg)&#123;
        return fn( arg );
    &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>unary 也是纯函数。</p>
<p><strong>表达一个函数的纯度的另一种常用方法是：给定相同的输入（一个或多个），它总是产生相同的输出。</strong></p>
<p>不纯的函数是不受欢迎的！因为我们需要更多的精力去判断它的输出结果！</p>
<p>写纯函数需要更多耐心，比如我们操作数组的 push(..) 方法，或 reverse(..) 方法等，看起来安全，但实际上会修改数组本身。我们需要复制一个变量来解耦（深拷贝）。</p>
<p>函数的纯度是和自信是有关的。函数越纯洁越好。制作纯函数时越努力，当您阅读使用它的代码时，你的自信就会越高，这将使代码更加可读。</p>
<p>其实，关于函数纯度还有更多有意思的点：</p>
<p>思考一个问题，如果我们把函数和外部变量再封装为一个函数，外界无法直接访问其内部，这样，内部的函数算不算是一个纯函数？</p>
<blockquote>
<p>假如一棵树在森林里倒下而没有人在附近听见，它有没有发出声音？</p>
</blockquote>
<h2 data-id="heading-3">阶段小结</h2>
<ol>
<li>
<p>我们反复强调：<strong>开发人员喜欢显式输入输出而不是隐式输入输出。</strong></p>
</li>
<li>
<p>如果有隐式的输入输出，那么就有可能产生副作用。</p>
</li>
<li>
<p>有副作用的代码让我们的代码理解起来更加费劲！</p>
</li>
<li>
<p>解决副作用的方法有：定义常量、明确 I/O、明确依赖、运用幂等......</p>
</li>
<li>
<p>在 js 运用幂等是一个新事物，我们需要逐渐熟悉它。</p>
</li>
<li>
<p>没有副作用的函数就是纯函数，纯函数是我们追求编写的！</p>
</li>
<li>
<p>将一个不纯的函数重构为纯函数是首选。但是，如果无法重构，尝试封装副作用。（假如一棵树在森林里倒下而没有人在附近听见，它有没有发出声音？—— 有没有其实已经不重要了，反正听不到）</p>
</li>
</ol>
<p>以上，便是本次关于 JS 函数式编程 <strong>副作用</strong> 这个细节的讲解。</p>
<p>这个细节，真的很重要！</p>
<p>我是掘金安东尼，公众号【掘金安东尼】，输出暴露输入，技术洞见生活！</p></div>  
</div>
            