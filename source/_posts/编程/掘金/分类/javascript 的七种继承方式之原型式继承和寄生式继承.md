
---
title: 'javascript 的七种继承方式之原型式继承和寄生式继承'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6820'
author: 掘金
comments: false
date: Tue, 10 Aug 2021 05:24:31 GMT
thumbnail: 'https://picsum.photos/400/300?random=6820'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第10天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h1 data-id="heading-0">原型式继承</h1>
<h3 data-id="heading-1">前言</h3>
<p>.前面我们已经介绍了JavaScript的三种继承方式：原型链，借用构造函数已经二者的组合继承。其中第三种组合继承最为常用。因为我们知道它结融合了原型链和借用构造函数的有点，隐藏了自己各自的缺点，最终实现了相对比较完美的继承方式。接下来我们要介绍js中的第四中继承方式——原型式继承。</p>
<h3 data-id="heading-2">原型式继承</h3>
<p>曾经有人提出了另一种实现继承的方法，这种方法并没有使用严格意义上的构造函数，而是借助原型可以基于已有的对象来创建一个新对象， 同时还不必因此创建自定义类型。下面我们来看一段代码</p>
<pre><code class="copyable">function object(o)&#123;
    function F()&#123;&#125;
    F.prototype = 0;
    return new F();
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上代码在object函数内部，先创建了一个临时的构造函数，然后将传入的对象作为该构造函数的原型，最后返回了这个临时类型的新实例。从本质上讲，object() 对传入其中的对象执行了一次浅复制。来看下面的例子</p>
<pre><code class="copyable">var person = &#123;
    name: 'Alvin',
    friends: ['Yannis','Ylu']
&#125;

var p1 = object(person);
p1.name = 'Bob';
p1.friends.push('Lucy');

var p2 = object(person);
p2.name = 'Lilei';
p2.friends.push('Hanmeimei');

console.log(person.friends);//Yannis, Ylu, Lucy, Hanmeimei
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种原型式继承要求必须有一个对象可以作为另一个对象的基础。如果有这么一个对象的话， 可以把它传递给object函数，然后再根据具体需求对得到的对象加以修改。在这个例子中可以作为另一个对象基础的是person对象，于是我们把它传入到object函数中，然后该函数就会返回一个新对象，这个新对象将person作为原型，所以它的原型中就包含了一个基本类型属性name和一个引用类型属性friends。这就意味着person.friends不仅属于person所有，而且也会被p1和p2共享。实际上就相当于创建了person对象的两个副本。</p>
<p>在ECMAScript5中新增了Object.create()方法，该方法规范了原型式继承。这个方法接收两个参数：一个用作新对象原型的对象，另一个是可选的，用于新对象定义额外的属性的对象。在只传入一个参数的情况下，Object.create()与上面的object()方法行为相同。看下面示例：</p>
<pre><code class="copyable">var person = &#123;
    name: 'Alvin',
    friends: ['Yannis','Ylu']
&#125;

var p1 = Object.create(person);
p1.name = 'Bob';
p1.friends.push('Lucy');

var p2 = Object.create(person);
p2.name = 'Lilei';
p2.friends.push('Hanmeimei');

console.log(person.friends);//Yannis, Ylu, Lucy, Hanmeimei
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Object.create()方法的第二个参数与Object.defineProperties()方法的第二个参数格式相同：每个属性都是通过自己的描述符定义。以 这种方式指定<strong>任何属性</strong>都会覆盖原型对象上的同名属性。如：</p>
<pre><code class="copyable">var person = &#123;
    name: 'Alvin',
    friends: ['Yannis','Ylu']
&#125;

var p1 = Object.create(person,&#123;
    name:&#123;
        value:'Lucy'
    &#125;
&#125;)

console.log(p1.name);//Lucy
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">使用场景</h3>
<p>在没有必要兴师动众的创建构造函数，而只想让一个对象与另一个对象保持类似的情况下，原型式继承是完全可以考虑的。当然同样的问题就是：包含的所有引用类型的属性始终都会共享相应的值。</p>
<h1 data-id="heading-4">寄生式继承</h1>
<p> 寄生式继承是与原型式继承紧密相关的一种思路。寄生式继承的思路与寄生构造函数和工程模式类似，即创建一个仅用于封装继承过程的函数，该函数的内部以某种方式来增强对象，最后再像真的是它做了所有工作一样返回对象。下面的代码示范了寄生式继承的模式</p>
<pre><code class="copyable">function object(o)&#123;
    function F()&#123;&#125;
    F.prototype = o;
    return new F();
&#125;

function createAnother(original)&#123;
    var clone = object(original);//通过调用函数创建一个新对象
    clone.sayHi = function()&#123;//以某种方式来增强这个对象
        console.log('hello')
    &#125;
    return clone;//返回这个对象
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在这个例子中createAnother函数接收了一个参数，也就是将要作为新对象基础的对象。然后，把这个对象传递给object()，将返回的结果赋值给clone，再为clone对象添加一个新的方法sayHi()，最后返回clone对象。可以像下面这样使用createAnother函数：</p>
<pre><code class="copyable">var person = &#123;
    name:"Alvin",
    friends:['Yannis',"Lucy"]
&#125;

var anotherPerson = createAnother(person);
anotherPerson.sayHi();//hello
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个例子中的代码基于person返回了一个新对象-anotherPerson。新对象不仅具有person的所有属性和方法，而且还有自己的sayHi()方法。</p>
<p>在主要考虑对象而不是自定义类型和构造函数的情况下，寄生式继承也是一种有用的模式。前面示范继承模式时使用的object()函数不是必须。任何能够返回新对象的函数都可以。</p>
<p>使用寄生式继承来为对象添加函数，会由于不能做到函数复用而降低效率；这点与构造函数模式类似。</p></div>  
</div>
            