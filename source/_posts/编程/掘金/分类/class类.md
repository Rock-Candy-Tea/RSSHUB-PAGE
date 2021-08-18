
---
title: 'class类'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3463'
author: 掘金
comments: false
date: Tue, 17 Aug 2021 16:46:41 GMT
thumbnail: 'https://picsum.photos/400/300?random=3463'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>“<strong>这是我参与8月更文挑战的第12天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong>”</p>
<p><code>本文通过构造函数方法 与 class 进行对比来讲解，这样会更好理解点</code></p>
<h4 data-id="heading-0">1，定义</h4>
<p>class 的本质是 function，它可以看作一个语法糖，让对象原型的写法更加清晰、更像面向对象编程的语法</p>
<h4 data-id="heading-1">2，函数的使用（构造函数 与 class）</h4>
<p>1，新建</p>
<ul>
<li>构造函数创建实例</li>
</ul>
<p>**</p>
<pre><code class="copyable">function Person(name,age)&#123;
    this.name = name
    this.age = age
&#125;
const constructP = new Person('张小五',21) // &#123;name: "张小五"  age: 21&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>class 创建实例<br>
<code>constructor 是类的 构造器，每个类，都有构造器</code><br>
<code>程序员没有手动指定构造器，默认类内部有一个隐形的空构造器，类似于 constructor()&#123;&#125;</code><br>
<code>构造器作用：每当 new 这个类时候，必然会优先执行 构造器里的代码</code></li>
</ul>
<p>**</p>
<pre><code class="copyable">class Animal&#123;
  constructor(name,age)&#123;
        this.name = name
        this.age = age
  &#125;
&#125;
const classA = new Bnimal('张小五',10) // &#123;name: "张小五"  age: 10&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>2，静态属性 与 实例属性<br>
<code>静态属性：直接挂载给构造函数的属性</code><br>
<code>实例属性：通过new出来的实例，访问到的动态属性</code></p>
<p>**</p>
<pre><code class="copyable">// 构造函数 
constructP.name // 张小五 动态属性
constructP.info= '我是构造函数静态属性'

// class 类
classA.name // 张小五 动态属性
class Animal&#123;
  static info = '我是class类静态属性'
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>3，挂载的 静态方法 与 实例方法<br>
<code>静态方法：在函数原型上，添加一个静态方法</code><br>
<code>实例方法：在函数原型上，添加一个实例方法</code></p>
<ul>
<li>构造函数</li>
</ul>
<p>**</p>
<pre><code class="copyable">// 静态方法
 constructP.show = function () &#123;
    console.log('我是面向对象挂载的show静态方法')
&#125;

// 实例方法
constructP.prototype.say = function () &#123;
    console.log('我是面向对象挂载的say实例方法')
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>class 类<br>
<code>在class类 上添加一个【实例方法】</code><br>
<code>在class类 上，通过static 修饰的属性，添加一个【静态方法】</code></li>
</ul>
<p>**</p>
<pre><code class="copyable">class Bnimal&#123;
     ...... // 此处添加constructor属性
    say () &#123; // 在a的原型上，查看到该方法
         console.log('我是添加在class原型上的方法')
    &#125;
    static show () &#123; // 在class类 上，通过 static 修饰的属性，添加【静态方法】
         console.log('我是class挂载的show静态方法')
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>注：<code>类定义不会被提升，这意味着，必须在访问前对类进行定义，否则就会报错。</code><br>
<code>类中方法不需要 function 关键字；方法间不能加分号</code></p>
<p>4，继承</p>
<ul>
<li>class 类<br>
<code>通过 extends 来设置子类继承了父类元素</code><br>
<code>直接把子类的方法，添加在父类元素上，通过prototype来获取实例方法</code></li>
</ul>
<p>**</p>
<pre><code class="copyable">class PersonSet&#123;
   constructor(name,age)&#123;
       this.name = name
       this.age = age
   &#125;
   say()&#123; // 子类继承父类上的实例方法
       console.log('打声招呼呗')
  &#125;
&#125;

 // 子类继承了父类元素的属性
class American extends PersonSet &#123; &#125; 

const C = new Chinese('张小五',22)
console.log(C) // &#123;name: "张小五"  age: 22&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">3，constructor中的 super 使用</h4>
<p>1，为什么 里面要调用 super？<br>
答：如果子类通过 extends 关键字继承父类，子类的 constructor 构造函数中，必须优先调用 super()；</p>
<p>2，super 是什么东西？<br>
super 是一个函数，子类的 super 是父类构造器 constructor 构造器的一个引用</p>
<p>3，为什么调用之后，实例上 name 与 age 就变成了 undefined<br>
因为是父类构造器的引用，需要传值，不传的话，肯定是undefined</p>
<p>**</p>
<pre><code class="copyable">class PersonSet &#123;
     constructor(name,age)&#123;
          this.name = name
          this.age = age
     &#125;
&#125;

class American extends PersonSet &#123;
    constructor(name,age)&#123;
         super(name,age)
     &#125;
&#125;
const A = new American('jack',20)
console.log(A) // American &#123;age: 20,name: "jack"&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">4，为子类挂载独有的方法或者属性</h4>
<p>**</p>
<pre><code class="copyable">class PersonSet&#123;
     constructor(name,age)&#123;
          this.name = name
          this.age = age
     &#125;
&#125;

class Chinese extends PersonSet &#123;
    constructor(name,age,number)&#123;
         super(name,age)
         this.number = number
     &#125;
&#125;
const C = new Chinese ('jack',20,'3213221898xxxxxxxx')
console.log(C) // Chinese &#123;name: "jack",age: 20,number:'3213221898xxxxxxxx'&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><code>注：语法规范，在子类中，this 只能放到 super 之后使用</code><br>
<code>如果所有子类都共享的，就放到父类，否则直接放到子类中，即可</code></p></div>  
</div>
            