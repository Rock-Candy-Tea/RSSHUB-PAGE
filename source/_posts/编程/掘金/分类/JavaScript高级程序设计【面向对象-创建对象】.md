
---
title: 'JavaScript高级程序设计【面向对象-创建对象】'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=1588'
author: 掘金
comments: false
date: Mon, 26 Jul 2021 16:42:27 GMT
thumbnail: 'https://picsum.photos/400/300?random=1588'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><pre><code class="copyable"><pre name="code" class="javascript">function createPerson(name,age)&#123;
  var o=new Object();
  o.name=name;
  o.age=age;
  o.sayName=function()&#123;
    alert(this.name);
  &#125;;
  return o;
&#125;
 
var person1=createPerson("name",32);
var person2=createPerson("name2",34);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>工厂模式抽象了创建具体对象的过程，用函数来封装以特定接口创建对象的细节。但是没有解决对象识别问题。</p>
<pre><code class="copyable">function Person(name,age)&#123;
  this.name=name;
  this.age=age;
  this.sayName=function()&#123;
    alert(this.name);
  &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>var person1=new Person("name",32);
var person2=new Person("name2",34);
构造函数模式 没有显示的创建对象，直接将属性和方法赋给了this对象，没有return语句；要创建Person的新实例，必须使用new关键字，构造函数实际上会经历4个步骤：创建一个新对象，将构造函数的作用域赋给新对象（因此this就指向了这个对象），执行构造函数的代码（为这个新对象添加属性），返回新对象。在前面的例子最后，person1和person2分别保存着一个person的不同的实例。这两个对象都有一个constructor属性，该属性指向Person，如：</p>
<pre><code class="copyable">
alert(person1.constructor==Person); //true

alert(person2.constructor==Person); //true
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们在这个例子中创建的对象，既是Object的实例，又是Person的实例。如：</p>
<pre><code class="copyable">alert(person1 instanceof Object);//true

alert(person1 instanceof Person);//true

alert(person2 instanceof Object);//true

alert(person2 instanceof Person);//true
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建自定义的构造函数意味着将来可以将它的实例标识为一种特定的类型。</p>
<p>任何函数，用new来调用，那他就可以是构造函数。</p>
<p>构造函数的问题在于：每定义一个函数，也就是实例化了一个对象。从逻辑角度讲，此时的构造函数也可以这样定义：</p>
<pre><code class="copyable">function Person(name,age)&#123;
  this.name=name;
  this.age=age;
  this.sayName=new Function("alert(this.name);");
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从这个角度上来看构造函数，更容易明白每个Person实例都包含有一个不同的Function实例的本质。以这种方式创建函数，会导致不同的作用域链和标识符解析，但是创建Function实例的机制相同，因此不同实例上的同名函数是不相等的。
alert(person1.sayName==person2.sayName); //false</p>
<p>但是创建两个完成同样任务的Function实例的确没有必要，况且有this对象在，根本不用再执行代码前就把函数绑定到特定对象上面。</p>
<pre><code class="copyable">function Person(name,age)&#123;
  this.name=name;
  this.age=age;
  this.sayName=sayName;
&#125;
function sayName&#123;
  alert(this.name);
&#125;
var person1=new Person("name",32);
var person2=new Person("name2",34);

function Person()&#123;
        &#125;
        
        Person.prototype.name = "Nicholas";
        Person.prototype.age = 29;
        Person.prototype.job = "Software Engineer";
        Person.prototype.sayName = function()&#123;
            alert(this.name);
        &#125;;
        //在这里写一个alert(Person.name);会返回一个Person，去试试吧~，不过这个name不是定义的name
        var person1=new Person();
        person1.sayName();//"Nicholas"
        var person2=new　Person();
        person2.sayName();//"Nicholas"
        alert(person1.sayName==person2.sayName);//true
        
<span class="copy-code-btn">复制代码</span></code></pre>
<p>原型模式 我们创建的每个函数都有一个prototype属性，这个属性是一个指针，指向一个对象，而这个对象的用途是包含可以由特定类型的所有实例共享的属性和方法。prototype就是通过调用构造函数而创建的那个对象的原型对象。使用原型对象的好处是可以让所有的对象实例共享它所包含的属性和方法。不必再构造函数中定义对象实例的信息，而是可以将这些信息直接添加到原型对象中。
在此，我们将sayName()方法和所有属性直接添加到了Person的prototype属性中，构造函数变成了空函数。即使如此，也仍然可以通过调用构造函数来创建新对象，而且新对象还会具有相同的属性和方法。但是与构造函数模式不同的是，新对象的这些属性和方法是由所有实例共享的。</p>
<p>使用Object.getPrototypeOf()可以方便的取得一个对象的原型，而这在利用原型实现继承的情况下是非常重要的。</p>
<p>每当代码读取每个对象的某个属性时，都会执行一次搜索，目标是具有给定名字的属性。搜索首先从对象实例本身开始。试过在实例中找到了具有给定名字的属性，则返回该属性的值，如果没有找到，则继续搜索指针指向的原型对象，在原型对象中查找具有给定名字的属性。如果在原型对象中找到了这个属性，则返回该属性的值。</p>
<pre><code class="copyable">person1.name="Greg";

alert(person1.name);//Greg--来自实例

alert(person2.name);//Nicholas--来自原型

使用delete可以完全删除实例属性

delete person1.name;

alert(person1,name); //Nicholas--来自原型


使用hasOwnProperty()方法可以检测一个属性时存在于实例中还是存在于原型中。

alert(person1.hasOwnProperty("name"))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>来自实例则返回true，来自原型则返回false</p>
<pre><code class="copyable">alert("name" in person1);//true

<span class="copy-code-btn">复制代码</span></code></pre>
<p>不管属性在原型中还是在实例中，都会返回true。</p>
<p>还有一种更简单的原型语法，</p>
<pre><code class="copyable">function Person()&#123;&#125;
 
Person.prototype=&#123;
  name:"nicholas",
  age:29;
  sayName:function()&#123;
    alert(this.name);
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在上面的代码中，我们将Person.prototype设置为等于一个以字面量形式创建的新对象。最终结果相同，但是有一个例外：constructor属性不再指向Person了。每创建一个函数，就会同时创建它的prototype对象，这个对象也会自动获得constructor属性。而我们在这里使用的语法，本质上完全重写了默认的prototype对象，因此constructor属性也就变成了新对象的constructor属性（指向Object构造函数），不再指向Person函数。</p>
<pre><code class="copyable">var friend=new Person();

alert(friend.constructor==Person); //false

alert(friend.constructor==Object);//true

<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果constructor值很重要可以把它设置回来：</p>
<pre><code class="copyable">function Person()&#123;&#125;
 
Person.prototype=&#123;
  constructor:Person,
  name:"nicholas",
  age:29;
  sayName:function()&#123;
    alert(this.name);
  &#125;
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>利用原型，还可以重写原生对象。</p>
<pre><code class="copyable">String.prototype.startsWith=function(text)&#123;
  //

&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<p>原型模式省略了为构造函数传递初始化参数这一环节，结果所有的实例在默认情况下都取得相同的属性值。</p>
<p>原型中所有属性是被很多实例共享的，但是对于包含引用类型值的属性来说，问题就比较突出了。</p>
<pre><code class="copyable">        function Person()&#123;
        &#125;
        
        Person.prototype = &#123;
            constructor: Person,
            name : "Nicholas",
            age : 29,
            job : "Software Engineer",
            friends : ["Shelby", "Court"],
            sayName : function () &#123;
                alert(this.name);
            &#125;
        &#125;;
        
        var person1 = new Person();
        var person2 = new Person();
        
        person1.friends.push("Van");
        
        alert(person1.friends);    //"Shelby,Court,Van"
        alert(person2.friends);    //"Shelby,Court,Van"
        alert(person1.friends === person2.friends);  //true
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            