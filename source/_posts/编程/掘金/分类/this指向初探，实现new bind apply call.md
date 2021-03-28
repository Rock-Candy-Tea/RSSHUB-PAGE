
---
title: 'this指向初探，实现new bind apply call'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4664'
author: 掘金
comments: false
date: Sat, 27 Mar 2021 03:51:09 GMT
thumbnail: 'https://picsum.photos/400/300?random=4664'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;color:rgba(46,36,36,.87);overflow-x:hidden&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;margin-bottom:5px;font-size:30px;font-weight:500&#125;.markdown-body h1:before&#123;content:"#";margin-right:10px;color:#1976d2&#125;.markdown-body h2&#123;font-size:28px;font-weight:400;border-left:5px solid #454545;margin-top:20px;padding-left:10px;transition:all .3s ease-in-out&#125;.markdown-body h2:hover&#123;border-color:#1976d2&#125;.markdown-body h3&#123;font-size:24px;font-weight:400;margin-top:15px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:20px;font-weight:500&#125;.markdown-body h5&#123;font-size:16px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body h2:first-letter,.markdown-body h3:first-letter,.markdown-body p:first-letter&#123;text-transform:capitalize&#125;.markdown-body em&#123;text-emphasis:dot;text-emphasis-position:under&#125;.markdown-body img&#123;display:block;margin:0 auto!important;max-width:100%;border-radius:2px;box-shadow:0 2px 4px -1px rgba(0,0,0,.2),0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12)!important&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;border:none;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#ddd,#999,#ddd);overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;font-weight:900;word-break:break-word;border-radius:2px;overflow-x:auto;font-size:.87em;padding:.065em .4em;background-color:#fbe5e1;color:#c0341d&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;border-radius:0 4px&#125;.markdown-body pre>code&#123;font-weight:400;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;margin:0 4px;text-decoration:none;color:#027fff;transition:all .3s ease-in-out;padding-bottom:4px;border-bottom:2px solid transparent&#125;.markdown-body a:after&#123;content:"";display:inline-block;width:18px;height:18px;margin-left:4px;vertical-align:middle;background-image:url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMiIgaGVpZ2h0PSIyMiI+PGcgZmlsbD0ibm9uZSIgZmlsbC1ydWxlPSJldmVub2RkIiBzdHJva2U9IiMwMjdGRkYiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCI+PHBhdGggZD0iTTkuODE1IDYuNDQ4bDEuOTM2LTEuOTM2YzEuMzM3LTEuMzM2IDMuNTgtMS4yNTkgNS4wMTMuMTczIDEuNDMyIDEuNDMyIDEuNTEgMy42NzYuMTczIDUuMDEzbC0xLjQ1MiAxLjQ1Mi0uOTY4Ljk2OGMtMS4zMzcgMS4zMzYtMy41ODEgMS4yNTktNS4wMTMtLjE3MyIvPjxwYXRoIGQ9Ik0xMS4yNjcgMTUuMzY3bC0xLjkzNiAxLjkzNmMtMS4zMzYgMS4zMzctMy41OCAxLjI2LTUuMDEyLS4xNzMtMS40MzItMS40MzItMS41MS0zLjY3Ni0uMTczLTUuMDEybDEuNDUyLTEuNDUyLjk2OC0uOTY4YzEuMzM2LTEuMzM3IDMuNTgtMS4yNiA1LjAxMi4xNzMiLz48L2c+PC9zdmc+);background-size:cover;background-repeat:no-repeat&#125;.markdown-body a:hover&#123;border-color:#027fff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body a.footnote-backref:after,.markdown-body a.footnote-ref:after,.markdown-body sup a:after&#123;display:none!important&#125;.markdown-body table&#123;margin:0 auto 10px;font-size:12px;width:auto;max-width:100%;overflow:auto;border:2px solid #c6c6c6&#125;.markdown-body table img&#123;box-shadow:none!important&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body del&#123;color:rgba(0,0,0,.6)&#125;.markdown-body blockquote&#123;position:relative;color:#666;padding:5px 23px 1px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:hsla(0,0%,78.4%,.12);transition:all .2s ease-in-out&#125;.markdown-body blockquote:hover&#123;border-color:#1976d2&#125;.markdown-body blockquote:after,.markdown-body blockquote:before&#123;position:absolute;font-size:24px;font-weight:800;line-height:24px;color:#cbcbcb;opacity:.6&#125;.markdown-body blockquote:before&#123;content:"“";top:4px;left:6px&#125;.markdown-body blockquote:after&#123;content:"”";right:8px;bottom:-8px&#125;.markdown-body blockquote>p,.markdown-body blockquote blockquote&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details&#123;outline:none;border:none;border-left:4px solid #1976d2;padding-left:10px;margin-left:4px&#125;.markdown-body details summary&#123;cursor:pointer;border:none;outline:none;background:#fff;margin:0 -17px&#125;.markdown-body details summary:hover::-webkit-details-marker&#123;color:#1976d2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">前言</h3>
<p>this指向分为默认绑定，隐式绑定，显式绑定，new操作，箭头函数这几类，经常使用的改变this指向的方法就是call，apply， bind，这些我们经常用到的方法你是否对其实现方式好奇呢？其实搞懂这些并不难，我认为首先必须知道函数内部做了什么事情，他解决的是什么问题，然后我们才能针对性地去探索。</p>
<h3 data-id="heading-1">new</h3>
<p>首先是最常见的new，new并不是一个函数，是一个运算符，用于创建一个对象的实例，这应该是大家熟知的。用法，new后面跟一个构造函数：</p>
<pre><code class="copyable">new constructor[([arguments])]
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看一下MDN上的解释
new 关键字会进行如下的操作：</p>
<ol>
<li>创建一个空的简单JavaScript对象（即&#123;&#125;）；</li>
<li>链接该对象（设置该对象的constructor）到另一个对象 ；</li>
<li>将步骤1新创建的对象作为this的上下文 ；</li>
<li>如果该函数没有返回对象，则返回this。</li>
</ol>
<p>哟西，既然如此我们就围绕上面四点，动手肝一个myNew函数</p>
<pre><code class="copyable">function myNew() &#123;
  // 创建一个空的简单JavaScript对象（即&#123;&#125;）；
  let obj = new Object()
  // 链接该对象（设置该对象的constructor）到另一个对象 --> 就是改变obj原型的指向
  // arguments是一个类数组，所以要这么调shift
  let con = [].shift.call(arguments)
  obj.__proto__ = con.prototype
  // 将步骤1新创建的对象作为this的上下文 ；
  // 如果该函数没有返回对象，则返回this。
  let res = con.apply(obj, arguments)
  // 如果构造函数person return了一个对象类型，就取return的值
  return typeof res == 'object' ? res : obj
&#125;

function person(name) &#123;
  this.name = name
&#125;

let p = myNew(person, 'jack')
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>插播：为何箭头函数不能用作构造函数?</p>
</blockquote>
<ol>
<li>没有单独的this</li>
<li>不绑定arguments</li>
<li>箭头函数没有prototype属性</li>
</ol>
<p>结合上述的代码实现，是不是清晰了一些呢？</p>
<p>我们还可以对代码进行优化,使用这种方式来改变和继承属性是对性能影响非常严重的，还会影响到所有继承来自该<code>[[Prototype]]</code>的对象，更优的方案是： <code>Object.create()</code>方法创建一个新对象，使用现有的对象来提供新创建的对象的__proto__。</p>
<pre><code class="copyable">let obj = Object.create(con.prototype) //
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-2">instanceOf</h3>
<p>引用自mdn：</p>
<blockquote>
<p>instanceof 运算符用来检测 constructor.prototype 是否存在于参数 object 的原型链上</p>
</blockquote>
<p>instanceof的判断逻辑是： 从当前引用的proto一层一层顺着原型链往上找，能否找到对应的prototype。找到了就返回true。挺简单就可以实现一个简易的instanceof</p>
<pre><code class="copyable">/*obj 实例  con 构造函数*/
function _instanceOf(obj,con) &#123;
    let _obj = obj.__proto__
    let _con = con.prototype
    while(true) &#123;
        if(_obj === null) &#123;
            return false
        &#125;

        if(_obj === _con) &#123;
            return true
        &#125;

        _obj = _obj.__proto__
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>缺点： 不能完全精确的判断复杂类型的具体数据类型</p>
<ul>
<li>[] instanceof Array; //true</li>
<li>[] instanceof Object; //true</li>
</ul>
<h3 data-id="heading-3">Bind</h3>
<blockquote>
<p>bind() 方法创建一个新的函数，在 bind() 被调用时，这个新函数的 this 被指定为 bind() 的第一个参数，而其余参数将作为新函数的参数，供调用时使用。</p>
</blockquote>
<p>先看看官方的例子：</p>
<pre><code class="copyable">const module = &#123;
  x: 42,
  getX: function() &#123;
    return this.x;
  &#125;
&#125;;

const unboundGetX = module.getX;
console.log(unboundGetX()); // The function gets invoked at the global scope
// expected output: undefined

const boundGetX = unboundGetX.bind(module);
console.log(boundGetX());
// expected output: 42
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由上述例子我们可以知道，使用bind作用有二：</p>
<ol>
<li>返回一个新的函数，给函数添加运行时参数，能使一个函数拥有预设的初始参数，倒是有点像es6的默认参数的作用。</li>
<li>显示绑定this值 ，这解决了绑定隐式丢失问题， 即函数中的 this 丢失绑定对象。例如:使用setTimeout，常见情况时执行时this指向 window。当使用对象的方法时，需要 this 引用对象，你可能需要显式地把 this 绑定到回调函数以便继续使用对象。例如： <code>setInterval(obj.fn.bind(obj), 1000);</code></li>
</ol>
<p>基此，我们可以尝试实现一个简单的bind：</p>
<pre><code class="copyable">function _bind() &#123;
    let fn = this //需要绑定的函数
    let args = Array.from(arguments) //类数组 -> 数组
    let obj = args.shift() //绑定的对象

    return function () &#123;
        fn.apply(obj, Array.from(args).concat(Array.from(arguments)))
    &#125;
&#125;
Function.prototype._bind = _bind
function fn(a, b) &#123;
    console.log(this);  // obj
    console.log(a + b); // 3
&#125;
let obj = &#123;
    name: 'violetrosez'
&#125;
let _fn = fn._bind(obj, 1)
_fn(2)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述代码，看似满足了需求，但是当返回的函数被作为构造函数时，原函数调用的this指向了bind显示指定的对象，不能根据new的调用而绑定到new创建的对象。当被作为构造函数调用时，我们需要将绑定函数的作用域赋给新对象，并设置绑定函数继承目标函数的原型。修改后如下：</p>
<pre><code class="copyable">function _bind() &#123;
    let fn = this //函数
    if (typeof fn !== 'function') &#123;
        throw new TypeError('what is trying to be bound is not callable');
    &#125;
    let args = Array.from(arguments)
    let obj = args.shift()

    let fNOP = Object.create(fn.prototype)
    let fBound = function () &#123;
        //如果没有判断，构造函数test在执行时也指向obj，而不会指向新建的实例p，此时p.name == undefined
        fn.apply(this instanceof fn ? this : obj, Array.from(args).concat(Array.from(arguments)))
    &#125;
    //使fBound.prototype是fN的实例，返回的fBound若作为new的构造函数，新对象的__proto__就是fN的实例
    fBound.prototype = fNOP
    return fBound
&#125;

//测试
function test(name) &#123;
    this.name = name
&#125;
let obj = &#123;&#125;
let _fn = test._bind(obj)
_fn('violetrosez')
console.log(obj.name);  // violetrosez
let p = new _fn('zzzzz') 
console.log(obj.name); // violetrosez
console.log(p.name);  // zzzzz

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>参考：<a href="https://www.jianshu.com/p/9d75886102a7" target="_blank" rel="nofollow noopener noreferrer">bind方法的实现</a> <a href="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Function/bind" target="_blank" rel="nofollow noopener noreferrer">MDN-BIND</a></p>
</blockquote>
<h3 data-id="heading-4">call</h3>
<blockquote>
<p>call() 方法使用一个指定的 this 值和单独给出的一个或多个参数来调用一个函数.call() 允许为不同的对象分配和调用属于一个对象的函数/方法。</p>
</blockquote>
<p>已经有了上面的基础，我们再写这个有点得心应手了，过程都是一个思路，对参数进行处理</p>
<pre><code class="copyable">function _call(ctx, ...args) &#123;
    if (typeof this !== 'function') &#123;
        throw new TypeError('what is trying to be bound is not callable');
    &#125;
    ctx = ctx || window
    ctx.fn = this

    let res = ctx.fn(...args)
    delete ctx.fn //删除掉引用
    return res
&#125;

Function.prototype._call = _call
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面的做法其实是将 this 的默认绑定改为隐式绑定，ctx不存在的时候，我们使ctx指向全局对象，然后将函数作为要绑定的对象的一个方法执行，用完后删掉。这次我们使用es6剩余操作符处理参数，写法比上文更简洁了一些。</p>
<h3 data-id="heading-5">apply</h3>
<p>apply和call唯一不同的就是他的剩余参数接收的是一个数组，所以把上面的代码改造一下即可。之前一直记混哪个是接受数组，后面干脆把apply的首字母<code>a</code>当成<code>array</code>去记忆了..</p>
<pre><code class="copyable">function _apply(ctx, args = []) &#123;
    if (typeof this !== 'function') &#123;
        throw new TypeError('what is trying to be bound is not callable');
    &#125;
    if(args && !Array.isArray(args)) &#123;
        throw new TypeError('apply need accept array object');
    &#125;
    ctx = ctx || window
    ctx.fn = this

    let res = ctx.fn(...args)
    delete ctx.fn //删除掉引用
    return res
&#125;

Function.prototype._apply = _apply
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">后记</h3>
<p>至此，我们完成了实现call、apply 和 bind的过程，其实这些本质上都是要改变 this 的指向，在实现过程中一定要时刻搞清楚this的指向，写代码的过程中，什么时候可以用箭头函数，什么时候需要显示绑定this，一定要心中有数。理解了原理之后，就能明白 this 的绑定顺序为什么是 <strong>new > 显示绑定 > 隐式绑定 > 默认绑定</strong>。 如有疑问或者错误，请各位批评指正，共同进步。求点赞三连QAQ</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            