
---
title: 'Js回顾（三）JavaScript中的原型和原型链'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2156'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 23:58:29 GMT
thumbnail: 'https://picsum.photos/400/300?random=2156'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">Js回顾（三）</h1>
<p>JavaScript中的原型和原型链</p>
<h3 data-id="heading-1">面向对象</h3>
<p>有许多的设计模式可以简化我们的代码，如工厂模式。
但在JavaScript中，我们想要用面向对象的思维去实现一种设计模式来简化我们的代码，仿造java中类的模式来实现类和继承是最好的.</p>
<p>然而在Es6以前是没有class和expend关键字来帮我们实现。</p>
<h3 data-id="heading-2">实现类</h3>
<p>在Es6出现以前，我们要用function模拟类
在原型上挂载方法</p>
<pre><code class="copyable">function Dog(name)&#123;
  this.name = name
&#125;
Dog.prototype.say = function() &#123;
    console.log("my name is" + this.name);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>模拟New：</p>
<pre><code class="copyable">function myNew(fn,...args)&#123;
    let obj=&#123;&#125;      //生成对象
    obj.__proto__=fn.prototype     //对象链接到构造函数原型上  
    fn.call(obj,...args)   //绑定this并执行构造函数
    return obj          //返回新对象
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">实现继承</h3>
<p>继承主要通过两种种方式实现</p>
<h4 data-id="heading-4">组合继承</h4>
<p>基于原型继承和构造函数继承两种方式，提出组合继承。既能继承原型，又能继承属性
这种方式成为了JavaScript中最常用的继承方式之一</p>
<pre><code class="copyable">function Child(value)&#123;
    Father.call(this,value)//构造函数继承 继承属性
&#125;
Child.prototype=new Father()//原型继承 继承方法
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">寄生组合继承</h4>
<p>寄生组合继承，最常用的继承模式</p>
<pre><code class="copyable">function inheritPrototype(son, father)&#123;
  var prototype = Object.create(father.prototype); // 创建父类原型的副本
  prototype.constructor = son;                    // 重写原型找回失去的默认的constructor 属性
  son.prototype = prototype;                      // 将新创建的对象赋给子类的原型
&#125;

// 父类初始化实例属性和原型属性
function father(name)&#123;
  this.name = name;
&#125;
father.prototype.sayName = function()&#123;
  alert(this.name);
&#125;;

// 借用构造函数传递增强子类实例属性（支持传参和避免篡改）
function son(name, age)&#123;
  father.call(this, name);
  this.age = age;
&#125;

// 将父类原型指向子类
inheritPrototype(son, father);

// 新增子类原型属性
son.prototype.sayAge = function()&#123;
  alert(this.age);
&#125;

var son1 = new son("xyc", 23);
//可以调用父类的sayName方法和子类的sayAge方法
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这种方法是ES6以前实现继承的主流方式之一</p>
<h4 data-id="heading-6">ES6的继承 extends</h4>
<p>extends关键字的作用与java中的相同，继承父类。
但是要注意的是，extends和class都不是从根本上实现了类和继承，而是封装好的“语法糖”,本质上也是一个函数。
extends要配合super使用，在this以前，super父类的构造函数。</p>
<pre><code class="copyable">class Book&#123;
    // constructor
    constructor(weigth) &#123;
        this.weight = weight;
    &#125;
    
    open() &#123;
        console.log("open the book")
    &#125;
&#125;
class EnglishBook extends Book&#123;     //英语书继承于书
    constructor(weight,pages)&#123;
        super (weight)
        this.pages=pages
    &#125;
    getPages()&#123;
        return this.pages
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>值得一提的是，extends的核心代码，与寄生组合继承如出一辙</p>
<p>Babel中的extends:</p>
<pre><code class="copyable">
function _possibleConstructorReturn (self, call) &#123; 
    // ...
    return call && (typeof call === 'object' || typeof call === 'function') ? call : self; 
&#125;

function _inherits (subClass, superClass) &#123; 
    // ...
    subClass.prototype = Object.create(superClass && superClass.prototype, &#123; 
        constructor: &#123; 
            value: subClass, 
            enumerable: false, 
            writable: true, 
            configurable: true 
        &#125; 
    &#125;); 
    if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; 
&#125;


var Parent = function Parent () &#123;
    // 验证是否是 Parent 构造出来的 this
    _classCallCheck(this, Parent);
&#125;;

var Child = (function (_Parent) &#123;
    _inherits(Child, _Parent);

    function Child () &#123;
        _classCallCheck(this, Child);
    
        return _possibleConstructorReturn(this, (Child.__proto__ || Object.getPrototypeOf(Child)).apply(this, arguments));
    &#125;

    return Child;
&#125;(Parent));
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这只是Bable中的部分代码，但我们观察_inherits函数还是可以发现，他的实现方式与寄生组合继承很像。
这也说明了寄生组合继承是现在最好的继承方式。</p>
<p>class不会变量提升，class内的方法没有原型</p>
<h3 data-id="heading-7">js中的原型链</h3>
<p>在我们使用js中的对象或数组时，有许多的方法和属性可以调用。但是我们从未定义过这些方法和属性。</p>
<p>打开控制台打印，可以看到每一个对象都有一个__proto__属性，这个属性指向了原型，最终指向“老祖宗”Object。</p>
<p>基于此，我们可以调用这些object的方法。</p>
<p>我们能够通过这个__proto__中的constructor构造函数中的prototype属性找到他的原型。
可是prototype中的对象与之前在__proto__中的对象基本一致。</p>
<p>这是怎么回事呢？</p>
<p>其实这个原型是他父类的原型，也就是说：
<code>father.prototype===son.prototype.__proto__</code></p>
<p>调用一个对象的属性或方法时，如果他本身没有，就会通过原型链，追溯到原型上查找方法，直到找到。</p></div>  
</div>
            