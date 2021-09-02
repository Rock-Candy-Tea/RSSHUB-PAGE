
---
title: 'JS数据类型检测那些事'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3dc974c8cd4e448cb9a567d80559076f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 01 Sep 2021 01:16:06 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3dc974c8cd4e448cb9a567d80559076f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">背景</h1>
<p>总所周知，js是一门动态的弱类型脚本语言，其采用<strong>动态</strong>的类型系统以及基于原型的继承方式。<br>
<strong>缺乏类型的静态约束</strong>，这意味着数据类型导致的程序错误并不能在<strong>编译阶段</strong>及时发现，要想写出健壮的代码，就必须在运行时各种的check&兼容，所以能够熟练准确的检测数据类型成为掌握这门语言最重要的基础之一。</p>
<h1 data-id="heading-1">判断数据类型的手段有哪些？</h1>
<p>总的来说大致有以下几种：<code>typeof、instanceof、Object.prototype.toString、constructor、鸭式类型、及针对特定类型的检测方法Array.isArray(),Number.isNaN()</code>，虽然方法很多，但他们的使用场景有所不同。</p>
<h2 data-id="heading-2">1. 用<code>typeof</code>判断<strong>基础数据类型</strong>：</h2>
<p>返回值有<code>undefined、string、number、boolean、object、function、symbol</code>七种。
<img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3dc974c8cd4e448cb9a567d80559076f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
可以看出，<code>typeof</code>作为官方提供的类型检测操作符，在检测<code>undefined、string、boolean、symbol</code>这些基本数据类型及<code>function</code>方面是十分靠谱的。表现拉垮的地方主要在于</p>
<pre><code class="copyable">1） 不能对具体对象类型（Array、Date、regExp）进行区分。
2） typeof null === 'object' // 竟然是true。。。。 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>缺陷 2）可以避免，在判断对象引用类型时多判断一句即可，<code>typeof x === 'object' &&  x !== null</code>。但是不能区分对象的具体类型，确实是个很大痛点。</p>
<h2 data-id="heading-3">2. 用<code>instanceof</code>判断对象数据类型</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eff95dede5524b9487b3018eaee99c15~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
此<strong>运算符</strong>用于检测某个构造函数的prototype是否出现在目标对象的原型链上。<br>
这是一种预测的检测方式，并不会像<code>typeof</code>一样直接将数据类型以字符串的方式进行返回，而是你需要预判对象类型的构造函数，最终返回一个boolean值。
检测规则其实从命名就可以看出，判断实例是否是由某个构造函数所创建的，那么知道了原理，现在动手实现一个属于自己的instanceof。</p>
<pre><code class="copyable">function myInstanceof(target,constructor)&#123;
  const baseType = ['string', 'number','boolean','undefined','symbol']
    if(baseType.includes(typeof(target))) &#123; return false &#125;
    //原型链其实就是个对象组成的链表，遍历这个链表，
  let prototype = Object.getPrototypeOf(target);
    while(prototype)&#123;
        //一旦链上有对象有符合，就返回true
      if(prototype === constructor.prototype)&#123;
        return true
      &#125;else&#123;
        prototype = Object.getPrototypeOf(prototype)
      &#125;
    &#125;
    return false
&#125;
console.log(myInstanceof([],Array))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在js里，可以从广义上认为<code>万物源于对象</code>，因为实例虽然是通过构造函数创建的，但是构造函数本身只是没有感情的生产机器，实例的灵魂和性格（公共属性和方法）都是共享自构造函数的prototype属性指向的那个原型对象，而且原型对象都是纯对象，纯对象又是由Object构造函数创建的，那么就会造成下边这种后果。<br>
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2624793739474bdb9e2dab14acbd46e7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
对于数组，遍历原型链上的对象,<code>Array.prototype</code> <code>Object.prototype</code>都会出现。
并且，对字面量方式创建的基本数据类型无法进行判断。比如<br>
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3655dd23fe8f4f52a2b375a1bd5522fe~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
如何弥补上边的缺陷呢，答案是可以在上边特殊的场景中采用下边的<code>constructor</code>代替instanceof。</p>
<h2 data-id="heading-4">3. 用<code>contructor</code>属性</h2>
<p>首先先明确。<code>constructor</code>是原型上的属性，实例继承自原型，所以实例上也能直接访问此属性。
首先看下<code>contructor</code>的通用性表现<br>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fdcc76f4bef544f8ad90b1ac5a0de202~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
意外的表现不错，除了<code>null、undefined</code>，有<code>contructor</code>属性的基础（包装）类型或者对象类型都能准确判断。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8736eb22cebf4696a4df6657a96dda6f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
能准确区分<code>Array</code>|<code>Object</code> 因为它没有<code>instanceof</code>那样会遍历整条原型链，只是在实例身上进行判断。但也有个致命的缺陷，实例上的这一属性太容易被修改了，一旦修改，这个方法就没有意义了。</p>
<h2 data-id="heading-5">4. <code>toString</code>方法</h2>
<p>首先，js的对象类型或者基础类型的包装对象都有一个<code>toString</code>方法。继承自<code>Object.prototype.toString()</code>，调用会返回对应类型的字符串标记"[object Type]"。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/271565c408e343c398ffeec4cb4f30b1~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
这个方法有种乱拳打死老师傅，无心插柳柳成荫的感觉，本来的作用只是得到一个<strong>表示该对象的字符串</strong>，现在用在js类型检测上，表现简直不要太好，针对基础类型及对象类型表现都非常不错，如果非要说个缺点，只能说返回的字符串有点复杂，使用不太方便，现在让我们动手简化一下。<br>
先写一个简版</p>
<pre><code class="copyable">function isType(type,value)&#123;
    return Object.prototype.toString.call(value) === `[object $&#123;type&#125;]`
&#125;
console.log(isType('Array',[]))
console.log(isType('Number',1))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样使用也不太方便，<code>‘Array’ ‘Number’</code>这样的类型参数，很容易拼写错误，所以希望方法可以预设参数，并且希望构造一个函数工厂，调用返回类似于<code>isArray</code>这样的函数。在IDE中函数名相比字符串会拥有更好的代码提示，不容易拼写错误。</p>
<pre><code class="copyable">function isType(type)&#123;
    return function(value)&#123;
        return Object.prototype.toString.call(value) === `[object $&#123;type&#125;]`
    &#125;
&#125;

const isArray = isType('Array')
const isNumber = isType('Number')
console.log(isArray([]),isNumber(1))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里运用了高阶函数的思想，保留参数+返回一个新的函数,那么可以想到js里bind除了可以绑定this，也有保留参数+返回新函数的功能，用在这里也很合适。</p>
<pre><code class="copyable">function isType(type,value)&#123;
    return Object.prototype.toString.call(value) === `[object $&#123;type&#125;]`
&#125;

const isArray = isType.bind(null,'Array')
const isNumber = isType.bind(null,'Number')
console.log(isArray([]),isNumber(1))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更进一步，用参数柯里化的思想改造一波</p>
<pre><code class="copyable">function isType(type,value)&#123;
    return Object.prototype.toString.call(value) === `[object $&#123;type&#125;]`
&#125;
function curring (fn,...args1)&#123;
    let len = fn.length;
    return function(...args2)&#123;
        const args = args1.concat(args2);
        if(args.length < len)&#123;
            return curring(fn,...args)
        &#125;else&#123;
            return fn(...args)
        &#125;
    &#125;
&#125;
const isArray = curring(isType,'Array')
const isNumber = curring(isType,'Number')
console.log(isArray([]),isNumber(1))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，丰富一下支持的类型，大功告成。</p>
<pre><code class="copyable">const types = [
    'Null',
    'Undefined',
    'String',
    'Number',
    'Boolean',
    'Object',
    'Array',
    'Date',
    'Function',
    'RegExp',
    'Symbol',
    'Math',
]
const checkTypeUtil = &#123;&#125;
types.forEach((type)=>&#123;
    checkTypeUtil[`is$&#123;type&#125;`] = curring(isType,type)
&#125;)
export &#123;
 checkTypeUtil
&#125;
console.log(checkTypeUtil.isArray([]))
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">5. 用<code>Array.isArray</code>判断数组</h2>
<p>上边提到 <code>instanceof</code>可以用来检测数组，但是这在iframe创建的多window环境中，因为window全局环境需要隔离，所以<code>Array</code>和<code>Array.prototype</code>在每个窗口中必须是不同的，所以<code>iframeA.Array.prototype ≠ iframeB.Array.prototype</code>，所以 <code>iframeA.arr instanceof iframeB.Array</code>必定是返回false，这是小概率的事件，但是在使用iframe的场景里，互相传值，也是非常可能发生的。使用ES6提供的<code>Array.isArray</code>就没有这个问题，可以准确判断数组。<br>
可以这样 <em>pollify</em></p>
<pre><code class="copyable">if (!Array.isArray) &#123;
  Array.isArray = function(x) &#123;
    return Object.prototype.toString.call(x) === '[object Array]';
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">6.区分<code>ArrayLike</code>与<code>Array</code></h2>
<p>类数组的定义是：</p>
<ul>
<li>拥有<code>length</code>属性，其它属性（索引）为非负整数（对象中的索引会被当做字符串来处理</li>
<li>不具有数组所具有的方法</li>
</ul>
<pre><code class="copyable">function isLikeArray(x)&#123;
    if(!(typeof x === 'object' && x !== null))&#123;
        return false
    &#125;
    return typeof x.length === 'number' && x.length >= 0 && !Array.isArray(x)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>类数组可以用<code>Array.from</code> <code>Array.prototype.slice.call(val)</code>来转换为真正的数组。</p>
<h2 data-id="heading-8">7.判断一个对象是否是纯对象（or普通对象）</h2>
<p>纯对象的定义：特指通过一下三种方式创建的对象</p>
<ul>
<li>new Object</li>
<li>对象字面量创建 &#123;&#125;</li>
<li>Object.create(null)</li>
</ul>
<p>jquery、lodash源码都是采用下边的方法来检测</p>
<pre><code class="copyable">const funcToString = Function.prototype.toString
const objectCtorString = funcToString.call(Object)

function isPlainObject(value)&#123;
    // 先用toString先排除其他数据类型
    if(!value || !Object.prototype.toString.call(value) === "[object Object]")&#123;
        return false
    &#125;
    const proto = Object.getPrototypeOf(value)
    if(proto === null)&#123;//兼容Object.create(null)这样创建的对象
        return true
    &#125;
    const Ctor = Object.prototype.hasOwnProperty.call(proto,'constructor') && proto.constructor;
    if(typeof Ctor !== 'function')&#123;
        return false
    &#125;
    // 这里通过字符串判断构造函数是否是Object，而不是直接使用instanceof，是为了避免上边提到的 多window环境Object不同的问题
    if(funcToString.call(Ctor) === objectCtorString)&#123;
        return true
    &#125;
    return false
&#125;
console.log(isPlainObject(Object.create(null)))
console.log(isPlainObject(new Object))
console.log(isPlainObject(&#123;a:1&#125;))
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">8. <code>NaN</code>如何检测，<code>Number.isNaN</code>与<code>isNaN</code>有啥区别</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3471d5f29c14415889b2f896901c176e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"><br>
结论：Number.isNaN会严格的判断传入的值是否是直接等于NaN。
isNaN则会先进行Number()转换，然后再进行是否是NaN的判断。</p>
<h2 data-id="heading-10">9. 鸭式类型检测法</h2>
<p>其实上边利用<code>constuctor</code>判断数据类型，就是采用了这种方法。判断一个动物是不是鸭子，那么通过看起来像鸭子，叫起来像鸭子这样简单的经验判断就可大致进行判断。
比如判断一个对象是不是一个<code>Promise</code>，就可以这样</p>
<pre><code class="copyable">function isPromise(x)&#123;
    if(!(x instanceof Promise))&#123;
        return false
    &#125;
    return typeof x.then === 'function'
&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            