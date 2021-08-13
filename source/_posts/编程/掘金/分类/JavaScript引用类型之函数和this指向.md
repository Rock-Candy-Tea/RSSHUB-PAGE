
---
title: 'JavaScript引用类型之函数和this指向'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7819'
author: 掘金
comments: false
date: Thu, 12 Aug 2021 19:48:45 GMT
thumbnail: 'https://picsum.photos/400/300?random=7819'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">一、函数的本质</h3>
<p><strong>函数的本质是对象，函数名是指向函数对象的指针 。基于此，函数有以下特征。</strong></p>
<p>1、函数没有重载，声明同名函数只是覆盖了函数的值 。</p>
<p>2、函数可以作为值传递给另一个函数，而且可以将一个函数作为另一个函数的结果返回。</p>
<h3 data-id="heading-1">二、函数调用方式</h3>
<p>函数定义后，被调用时才执行，函数共有4种调用方式</p>
<p>1、作为函数</p>
<p>2、作为方法</p>
<p>3、作为构造函数</p>
<p>4、通过函数的call()和apply()方法调用</p>
<p><strong>三、this的指向</strong></p>
<p><strong>this是函数的内部属性</strong>，this指向函数的调用上下文。函数的调用方式不同，this指向也会不同。</p>
<p>1、作为函数被调用（很重要）</p>
<p>非严格模式下，this指定window(全局对象），严格模式下，this指向undefined。</p>
<p>在react框架事件绑定中，事件触发后回调函数的执行不是实例调用的，而是作为函数调用的，而且开启了严格模式，默认回调函数中的this是undefined。</p>
<p>而且，无论函数作为值传递给另一个函数的参数，还是是作为另一个函数的结果返回，<strong>抑或是在函数（或方法）内嵌套调用</strong>，都可以认为this指向全局对象，如下所示。</p>
<pre><code class="copyable">var obj=&#123;
  m:function()&#123;
console.log('m',this);
f()
function f()&#123;
console.log('f',this);
&#125;
&#125;
&#125;
obj.m()
输出的this分别是：
&#123;m: ƒ&#125;
Window &#123;0: global, window: Window, self: Window, document: document, name: "", location: Location, …&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>要想在内嵌函数种能访问到对象,必须将this保存到和内嵌函数同一个作用域内，譬如这样：</p>
<pre><code class="copyable">var obj=&#123;
  m:function()&#123;
console.log('m',this);
var self=this;
f()
function f()&#123;
console.log('f',self);
&#125;
&#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2、作为方法</p>
<p>方法调用一般是在对象定义中定义了方法，对象实例调用方法，类似o.m()的形式。所以调用上下文（this指向）就是对象实例。</p>
<p>3、作为构造函数调用</p>
<p>函数作为构造函数调用时，this指向新创建的对象。</p>
<pre><code class="copyable">function Person(name,age)&#123;
this.name=name;
this.age=age;
&#125;
var p1=new Person("Alice",20)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上创建对象的代码经历4个步骤：</p>
<p>（1）创建一个新对象</p>
<p>（2）让这个新对象来调用构造函数，即将构造函数的调用上下文赋给新对象（因此this就指向这个新对象）</p>
<p>（3）执行构造函数中的代码（为这个新对象添加属性）</p>
<p>（4）返回新对象</p>
<p>3、通过函数的call()和apply()方法调用</p>
<p>（1）Function.prototype.apply()</p>
<p>apply() 方法指定函数运行时使用的 this ，并以数组形式提供参数。</p>
<p>（2）Function.prototype.call()</p>
<p>call() 方法指定函数运行时使用的 this ，单独给出的一个或多个参数作为函数参数。</p>
<p>这两个方法作用效果是一样的，都是显示指定函数调用时的this值，强大之处在于能够扩充函数赖以运行的作用域，使得对象不需要与方法有任何耦合关系。任何函数都可以作为任何对象的方法调用，哪怕这个函数不是那个对象的方法。</p>
<pre><code class="copyable">var color="yellow";
var obj=&#123;color:"blue"&#125;
sayColor()  //输出yellow
sayColor.bind(obj);  //输出blue
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除此之外，还有Function.prototype.bind()方法，这个方法创建一个新的函数，在 bind() 被调用时，这个新函数的 this 被指定为 bind() 的第一个参数，而其余参数将作为新函数的参数，供调用时使用。像apply方法和call方法，就像是一次性改变this工作，而bind，可以一次改变一直使用，不过就是返回了个新函数。</p>
<pre><code class="copyable">var color="yellow";
var obj=&#123;color:"blue"&#125;
let sayColor1=sayColor.bind(obj)
sayColor1()  //输出blues
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>三、箭头函数的this指向</strong></p>
<p><strong>箭头函数没有this这个内部属性，于是乎，箭头函数调用时，是沿着作用域链去寻找this属性，也就是说一直去找外层函数的this，直到找到为止。</strong></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.mozilla.org%2Fzh-CN%2Fdocs%2FWeb%2FJavaScript%2FReference%2FFunctions%2FArrow_functions" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Functions/Arrow_functions" ref="nofollow noopener noreferrer">developer.mozilla.org/zh-CN/docs/…</a></p>
<pre><code class="copyable">var id=21
function foo()&#123;
var id=12;
console.log("foo ",this.id);
setTimeout(()=>&#123;
console.log("setTimeout ",this.id)
&#125;)
&#125;
foo()
输出：
foo  21
setTimeout  21
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，定时器中箭头函数执行环境的作用域链是，箭头函数->setTimout->foo->全局。所以箭头函数的this沿着作用域链找到setTimeout函数的变量对象，this指向的正是window。所以输出的id值是21。又比如：</p>
<pre><code class="copyable">var obj = &#123;
  i: 10,
  b: () => console.log(this),
  c: function() &#123;
    console.log(this)
  &#125;
&#125;
obj.b()
输出Window全局对象
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上面代码中，箭头函数执行环境的作用域链是，箭头函数->全局，所以输出的是window。</p>
<p>再看下面的代码，是使用class定义的类，类中的方法是可以使用箭头函数的</p>
<pre><code class="copyable">class Animal &#123;
    constructor(type) &#123;
        this.type = type
    &#125;
    walk() &#123;
        console.log( 'walk ',this )
    &#125;
    say=()=>&#123;
console.log('say',this)
    &#125;
&#125;
let a=new Animal("cat")
a.walk()
输出a这个实例对象 Animal &#123;type: "cat", say: ƒ&#125;
a.say()
输出a这个实例对象 Animal &#123;type: "cat", say: ƒ&#125;

var walk1=a.walk
walk1()
输出this是undedined
var say1=a.say;
say1()
输出this是a这个实例对象 Animal &#123;type: "cat", say: ƒ&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>类中的方法默认开启了严格模式，this指向在严格模式下是undefined。</p>
<p>对象中walk()方法是非箭头函数定义的，say()方法是箭头函数定义的。</p>
<p>1、首先非箭头函数的this指向，是很容易理解的，a.walk()是对象实例调用的，指向对象实例，而walk1(）是在全局执行环境中调用的，是作为普通函数调用，指向全局对象也没毛病。</p>
<p>2、但是箭头函数的this指向，就很让人费解。<strong>为什么a.say()和say1()输出的this都是指向实例对象？而这点广泛用于react组件实例的简写中。</strong></p>
<p>且看a实例对象，输出如下所示，非箭头函数walk()是定义在原型上的，而箭头函数say()是定义在对象上的实例属性。</p>
<pre><code class="copyable">Animal &#123;type: "cat", say: ƒ&#125;
 1.say: ()=>&#123; console.log('say',this)     &#125;
 2.type: "cat"
 3.[[Prototype]]: Object
    constructor: class Animal
    walk: ƒ walk()
    [[Prototype]]: Object
<span class="copy-code-btn">复制代码</span></code></pre>
<p>凭借现有知识实在不明白class定义类时t箭头函数方法的指向。姑且认为在class定义类时，实例方法定义为箭头函数，this总是指向定义时所在的对象吧。而其他场景，则按照MDN上关于箭头函数this指向的说明，箭头函数没有this，沿着作用链查找this。</p></div>  
</div>
            