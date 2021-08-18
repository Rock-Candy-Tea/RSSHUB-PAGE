
---
title: 'JavaScript中的实例属性、静态属性与原型属性，实例方法、静态方法与原型方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=6349'
author: 掘金
comments: false
date: Tue, 17 Aug 2021 23:42:08 GMT
thumbnail: 'https://picsum.photos/400/300?random=6349'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><ol>
<li>
<p>实例属性，静态属性与原型属性</p>
<p>实例属性定义在实例上，可以在构造函数的内部的this上进行定义，也可以在构造函数实例化以后的实例上进行定义。</p>
<p>静态属性，定义在构造函数之上的属性。可通过构造函数直接访问。</p>
<p>原型属性，定义在构造函数原型对象之上的属性。</p>
<pre><code class="copyable">function Person(name)&#123;
    // 在构造函数内部的this上进行定义实例属性
    this.name = name;
&#125;
// 在构造函数上定义静态属性
Person.sex = 'male';
// 在构造函数的原型对象上定义原型属性
Person.prototype.weight = 20
let person = new Person('wang');
// 在构造函数实例化以后的对象上进行定义实例属性
person.age = 23;
​
// 访问实例属性name
console.log(person.name) // wang
// 访问实例属性age
console.log(person.age) // 23
// 访问静态属性sex
console.log(Person.sex) // male
// 访问原型属性weight
console.log(person.weight) // 20
// 通过构造函数访问原型属性weight
console.log(Person.prototype.weight); // 20
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>实例方法，静态方法与原型方法</p>
<p>实例方法定义在实例上，可以在构造函数内部的this上进行定义，也可以在构造函数实例化以后的实例上进行定义。</p>
<p>静态属性，定义在构造函数之上的属性。可通过构造函数直接访问。</p>
<p>原型属性，定义在构造函数原型对象之上的属性。</p>
<pre><code class="copyable">function Person(name) &#123;
    this.name = name;
    // 在构造函数内部的this上进行定义实例属性
    this.sayIn = function() &#123;
        console.log('my name is ', this.name);
    &#125;
&#125;
// 在构造函数上定义静态方法
Person.eat = function()&#123;console.log('i can eat anything')&#125;;
// 在构造函数的原型对象上定义原型方法
Person.prototype.run =  function()&#123;console.log('i can run 100m in 9.88s')&#125;
let person = new Person('li');
// 在构造函数生成的实例上定义实例方法
person.sayOut = function()&#123;
    console.log('my name is out ', this.name);
&#125;
​
// 访问实例方法sayIn
person.sayIn();  // my name is li
// 访问实例方法sayOut
person.sayOut(); // my name is li
// 访问静态方法eat
Person.eat(); // i can eat anything
// 访问原型方法run
person.run(); // i can run 100m in 9.88s
// 通过构造函数访问原型方法
Person.prototype.run() // i can run 100m in 9.88s
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
<li>
<p>ES5与ES6中，静态方法，静态属性声明的区别？</p>
<pre><code class="copyable">class Person&#123;
    constructor(sex) &#123;
        this.sex = sex;
    &#125;
    // 使用static关键字声明静态方法
    static printSex()&#123;
        console.log('this is printSexMethod');
    &#125;
&#125;
// 静态属性只能通过 类.属性名 来声明
Person.age = 20;
// 通过 类.方法名 来声明静态方法
Person.printSexOut = () => &#123;
    console.log('this is printSexMethodOut')
&#125;
console.log('age', Person.age); // 20
Person.printSex(); // this is printSexMethod
Person.printSexOut(); // this is printSexMethodOut
<span class="copy-code-btn">复制代码</span></code></pre>
</li>
</ol></div>  
</div>
            