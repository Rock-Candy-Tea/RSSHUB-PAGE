
---
title: '红宝书笔记——JavaScript 面向对象'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2822'
author: 掘金
comments: false
date: Tue, 31 Aug 2021 01:40:05 GMT
thumbnail: 'https://picsum.photos/400/300?random=2822'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">属性类型</h2>
<p>要修改对象的属性的默认的特性，必须使用Object.defineProperty() 方法。这个方法接受三个参数：属性所在的对象，属性的名字，一个描述符对象。<br>
描述符对象的属性必须是configurable,enumberable,writable,value。在不指定情况下，configurable,enumberable,writable这三个属性都是默认为false。<br>
configurable设置为false 表示不能从对象中删除属性。writable设置为false表示是只读的，不能对属性进行赋值。enumberable表示能否通过for-in循环返回属性。</p>
<h2 data-id="heading-1">访问器属性</h2>
<p>在读取访问器属性时，会调用getter函数；在写入访问器属性时，会调用setter函数并传入新值。
访问器属性不能直接定义，必须使用Object.defineProperty()来定义。</p>
<pre><code class="copyable">var book=&#123;
    _year:2004,
    edition:1
&#125;;
Object.defineProperty(book,"year",&#123;
    get:function()&#123;
        return this._year;
    &#125;,
    set:function(newValue)&#123;
        if(newValue>2004)&#123;
            this._year=newValue;
            this.edition+=newValue-2004;
        &#125;
    &#125;
&#125;);
book.year=2005;
alert(book.edition);//2
<span class="copy-code-btn">复制代码</span></code></pre>
<p>定义多个属性：Object.defineProperties()方法。<br>
读取属性的特征：Object.getOwnPropertyDescriptor()方法。</p>
<pre><code class="copyable">var book=&#123;
&#125;;
Object.defineProperties(book,&#123;
    _year:&#123;
        value:2004,
        writable: true//这个必须写，不然不能下面book.year没有启用而起作用弹出2007，不然就弹出2004
    &#125;,
    edition:&#123;
        value:1
    &#125;,
    year:&#123;
        get:function()&#123;
            return this._year;
        &#125;,
        set:function(newValue)&#123;
            if(newValue>2004)&#123;
                this._year=newValue;
                this.edition+=newValue-2004;
            &#125;
        &#125;,
    &#125;
&#125;);
var descriptor=Object.getOwnPropertyDescriptor(book,"_year");
alert(descriptor.value);//2004
alert(descriptor.configurable);//false
book.year=2007;
alert(book._year);//2007
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">创建对象</h2>
<p>1.工厂模式：</p>
<pre><code class="copyable">function createPerson(name,age,job)&#123;
    var o=new Object();
    o.name=name;
    o.age=age;
    o.job=job;
    o.sayName=function()&#123;
        alert(this.name);
    &#125;;
    return o;
&#125;
var person1=createPerson("Nick",29,"Engineer");
var person2=createPerson("Greg",27,"Doctor");
person1.sayName();//Nick
alert(person2.name);//Greg
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2.构造函数模式:</p>
<pre><code class="copyable">function Person(name,age,job)&#123;
    this.name=name;
    this.age=age;
    this.job=job;
    this.sayName=function()&#123;
        alert(this.name);
    &#125;
&#125;
var person1=new Person("Nick",29,"Engineer");
var person2=new Person("Greg",27,"Doctor");
person1.sayName();//Nick
alert(person2.name);//Greg
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3.原型模式</p>
<pre><code class="copyable">function Person()&#123;
&#125;
Person.prototype.name="Nike";
Person.prototype.age=29;
Person.prototype.job="Engineer";
Person.prototype.sayName=function()&#123;
    alert(this.name);
&#125;;
var person1=new Person();
person1.sayName();//Nike
var person2=new Person();
person2.sayName();//Nike
alert(person1.sayName==person2.sayName);//true
hasOwnProperty() 方法可以检测一个属性是否存在于实例中，还是存在于原型中。如果存在于对象实例中，则返回true。
hasPrototypeProperty() 方法可以检测一个属性是否存在于实例中，还是存在于原型中。如果存在于对象原型中，则返回true。
Object.keys() 方法接受一个对象作为参数，返回一个包含所有可枚举属性的字符串数组。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更简单的原型语法：</p>
<pre><code class="copyable">function Person()&#123;
&#125;
Person.prototype=&#123;
  name: "Nike",
  age: 29,
  job: "Engineer",
  sayName: function()&#123;
    alert(this.name);
  &#125;
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>原型对象的问题：</p>
<pre><code class="copyable">function Person()&#123;
&#125;
Person.prototype=&#123;
  constructor: Person,
  name: "Nike",
  job: "Engineer",
  friends: ["Shelby","Court"],
  sayName: function()&#123;
    alert(this.name);
  &#125;
&#125;;
var person1=new Person();
var person2=new Person();
person1.friends.push("Van");
alert(person1.friends);//Shelby,Court,Van
alert(person2.friends);//Shelby,Court,Van
alert(person1.friends==person2.friends);//true
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到当改变一个对象的friends时，其他的对象的friends也跟着改变friends数组存在于person.prototype中，而不是存在于person1中，所以当改变person1的friends时候，person2的friends也变化。</p>
<p>4.组合使用构造函数模式和原型模式：构造函数模式用于定义实例属性，而原型模式用于定义方法和共享的属性。</p>
<pre><code class="copyable">function Person(name,age,job)&#123;
  this.name=name;
  this.age=age;
  this.job=job;
  this.friends=["Shelby","Court"];
&#125;
Person.prototype=&#123;
  constructor: Person,
  sayName: function()&#123;
    alert(this.name);
  &#125;
&#125;
var person1=new Person("Nike",29,"Engineer");
var person2=new Person("Greg",27,"Doctor");
person1.friends.push("Van");
alert(person1.friends);//Shelby,Court,Van
alert(person2.friends);//Shelby,Court
alert(person1.friends==person2.friends);//false
alert(person1.sayName==person2.sayName);//true
<span class="copy-code-btn">复制代码</span></code></pre>
<p>5.动态原型模式<br>
可以通过检查某个应该存在的方法是否有效，来决定是否需要初始化原型。</p>
<pre><code class="copyable">function Person(name, age, job) &#123;
    this.name = name;
    this.age = age;
    this.job = job;
    if(typeof this.sayName != "function") &#123; //在sayName()方法不存在的情况下，才会将它添加到原型中。instanceof操作符也可以
        Person.prototype.sayName = function() &#123;
            alert(this.name);
        &#125;;
    &#125;
&#125;
var friend = new Person("Nike", 29, "Engineer");
friend.sayName();//Nike
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            