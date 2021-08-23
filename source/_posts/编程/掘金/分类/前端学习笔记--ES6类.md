
---
title: '前端学习笔记--ES6类'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2513'
author: 掘金
comments: false
date: Sun, 22 Aug 2021 05:38:30 GMT
thumbnail: 'https://picsum.photos/400/300?random=2513'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、基本语法</h1>
<h2 data-id="heading-1">1.简介</h2>
<p>传统JS中创建对象是通过**「构造函数」**，例如：</p>
<pre><code class="copyable">  // 通过构造函数创建对象
    function Person(name,age)&#123;
        this.name=name;
        this.age = age;
    &#125;
    // 创建实例
    let p1 = new Person("小红",18);
    console.log("p1:",p1)
    // Person的prototype和p1的__proto__指向同一个对象
    console.log(Person.prototype === p1.__proto__) // true
<span class="copy-code-btn">复制代码</span></code></pre>
<p>基本上，ES6 的 class 可以看作只是一个<code>语法糖</code>，它的绝大部分功能，ES5 都可以做到，新的 class 写法只是让对象原型的写法更加清晰、更像面向对象编程的语法而已。</p>
<p>用class的语法改写如下：</p>
<pre><code class="copyable">class PersonCopy&#123;
        constructor(name,age)&#123;
            this.name=name;
            this.age=age;
        &#125;
        run()&#123;
            console.log(this.name +" is running")
        &#125;
    &#125;
    let p2 = new PersonCopy("小明",12);
    console.log("p2:",p2)
    console.log(typeof PersonCopy); // function 
    console.log(PersonCopy.prototype.constructor===PersonCopy) //true
    p2.run();
    
    
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以得知：</p>
<ul>
<li>类的数据类型就是函数</li>
<li>类本身就指向构造函数</li>
</ul>
<p>而且：</p>
<ul>
<li>实例属性是添加到对象上的</li>
<li>方法是定义到原型对象prototype上的，各个实例共用同一个方法</li>
</ul>
<pre><code class="copyable">&#123;
    "name": "小明",
    "age": 12
    
    [[prototype]]:&#123;
     constructor:f()  class PersonCopy,
     run: f run()
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相当于：</p>
<pre><code class="copyable"> function PersonCopy(name,age)&#123;
        this.name = name;
        this.age =age;
    &#125;
    // 方法加到原型对象上，所有实例共用。这样就只会存在一个run函数对象
    // 而不会为每个对象都创建一个run函数对象
    PersonCopy.prototype.run = function()&#123;
        console.log(this.name +" is running")
    &#125;
    let p3 = new PersonCopy("小王",13)
    p3.run() // 小王 is running
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于类的方法都是定义在类的prototype上的，所以可以通过Object.assign()方法为类一次性添加多个方法：</p>
<pre><code class="copyable">Object.assign(PersonCopy.prototype,&#123;
        toString()&#123;&#125;,
        toValue()&#123;&#125;
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">2.constructor</h2>
<p><code>constructor</code> 方法是<code>类</code>的默认方法，通过 new 命令生成对象实例时，自动调用该方法。一个类必须有 constructor 方法，如果没有显式定义，一个空的 constructor 方法会被默认添加。</p>
<p>类必须使用 new 调用，否则会报错。这是它跟普通构造函数的一个主要区别，后者不用 new 也可以执行。</p>
<p>与 ES5 一样，实例的属性除非显式定义在其本身（即定义在 this 对象上），否则都是定义在原型上（即定义在 class 上）。</p>
<h2 data-id="heading-3">3.getter和setter</h2>
<pre><code class="copyable">  class Man&#123;
        constructor()&#123;&#125; // 可不写

        // 会给prototype上添加一个name属性
        get name()&#123;
            return this.nickname;
        &#125;
        set name(name)&#123;
            this.nickname = name;
        &#125;
    &#125;
    let m = new Man();
    console.log(m);
    m.name="hello";
    console.log(m.name) //hello
    console.log(m.nickname); //hello
    m.hasOwnProperty('name') // false
    m.hasOwnProperty('nickname')  //true
    Man.prototype.hasOwnProperty('name') // true
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">4.属性表达式</h2>
<p>类的属性名，可以采用表达式。属性和方法都可以用表达式。</p>
<pre><code class="copyable">    // 属性表达式
    let prop1 = "name";
    let prop2 = "run";
    class Course&#123;
        constructor(name)&#123;
            this[prop1] = name;
        &#125;
        [prop2]()&#123;
            console.log(prop2)
        &#125;
    &#125;
    let c = new Course("基础");
    console.log(c)
    console.log(c.name)
    c.run()
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">5.class表达式</h2>
<p>与函数一样，类也可以使用表达式的形式定义。</p>
<pre><code class="copyable">
    const A = class B&#123;
        getClassDeclareName()&#123;
            return B.name + A.name; // A.name也可以
        &#125;
    &#125;
    let a = new A();
   console.log( a.getClassDeclareName())
   console.log(A.name) // B
   console.log(B.name)  // error
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个类的名字是B，但是只能在类内部使用，在外部只能使用A。A在内部和外部都可以使用。</p>
<h2 data-id="heading-6">6.静态方法</h2>
<p>类相当于实例的原型，所有在类中定义的方法，都会被实例继承。如果在一个方法前，加上 static 关键字，就表示该方法不会被实例继承，而是直接通过类来调用，这就称为“静态方法”。</p>
<pre><code class="copyable">    class A&#123;
        constructor(name)&#123;
            this.name = name;
        &#125;

        run()&#123;
            console.log(this.name +" is running")
        &#125;
        static step()&#123;
            console.log(this.name +" is step") // 此处this指向类A
        &#125;
    &#125;
    let a1 = new A("小红");
    
    console.log("a1",a1)
    a1.run()
    A.step()
    a1.step(); //error 实例没有该方法
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>实例调用静态方法会报错</li>
<li>如果静态方法包含 this 关键字，这个 this 指的是类，而不是实例</li>
<li>静态方法和非静态方法可以重名，因为一个是实例的，一个是类的。如下:调用a1.step()就不会报错了，调用的是非静态方法step</li>
</ul>
<pre><code class="copyable">    class A&#123;
        constructor(name)&#123;
            this.name = name;
        &#125;
        run()&#123;
            console.log(this.name +" is running")
        &#125;
        step()&#123;
            console.log("实例方法step")
        &#125;
        static step()&#123;
            console.log(this.name +" is step") // 此处this指向类A
        &#125;
    &#125;
    let a1 = new A("小红");
    
    console.log("a1",a1)
    a1.run()
    A.step()
    a1.step(); // 实例方法step
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">7.实例属性的新写法</h2>
<p><code>实例属性</code>除了定义在<code>constructor()</code>方法里面的 this 上面，也可以定义在<code>类</code>的最顶层。</p>
<pre><code class="copyable">  class B&#123;
        name;
        age;
        getName()&#123;
            return this.name;
        &#125;
        setName(value)&#123;
            this.name = value;
        &#125;
    &#125;
    let b =new B();
    b.setName("hello")
    console.log(b)
    console.log(b.getName())
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">8.静态属性</h2>
<p><code>静态属性</code>指的是<code>Class</code>本身的属性，即 <code>Class.propName</code>，而不是定义在实例对象（ this ）上的属性。</p>
<pre><code class="copyable"> // 写法1
    class A&#123;

    &#125;
    A.foo=1;
    let a = new A();
    console.log(A.foo);  //1 
    console.log(a.foo) // undefined

    // 写法2
   class B&#123;
       static foo = 1;
   &#125;
   let b = new B();
   console.log(B.foo) //1 
   console.log(b.foo) // undifined
<span class="copy-code-btn">复制代码</span></code></pre>
<p>目前，只有写法1可行，因为 ES6 明确规定，<code>Class</code>内部只有<code>静态方法</code>，没有<code>静态属性</code>。</p>
<p>写法2只是提案。</p>
<h2 data-id="heading-9">9.私有方法和私有属性</h2>
<p>无</p>
<h2 data-id="heading-10">10.new.target</h2>
<p>略</p>
<h1 data-id="heading-11">二、继承</h1>
<h2 data-id="heading-12">1.简介</h2>
<p><code>Class</code> 可以通过<code>extends</code>关键字实现<code>继承</code>，这比 ES5 的通过修改原型链实现继承，要清晰和方便很多。</p>
<pre><code class="copyable">        class A&#123;
            constructor(username,password)&#123;
                this.username = username;
                this.password = password;
                console.log("A constructor")
            &#125;
            static run()&#123;
                console.log("run")
            &#125;
        &#125;
        class B extends A&#123;
            constructor(sex,username,password)&#123; 
                console.log("B constructor")
                super(username,password);
                this.sex = sex;
            &#125;
        &#125;
        let b = new B("男","admin","1234")
        console.log(b)
        B.run() // 继承父类的静态方法
<span class="copy-code-btn">复制代码</span></code></pre>
<p>子类必须在 constructor 方法中调用 super 方法，否则新建实例时会报错。这是因为子类自己的 this 对象，必须先通过父类的构造函数完成塑造，得到与父类同样的实例属性和方法，然后再对其进行加工，加上子类自己的实例属性和方法。如果不调用 super 方法，子类就得不到 this 对象。</p>
<ul>
<li>子类必须调用父类的构造方法</li>
<li>父类的构造方法必须在使用this关键字之前调用</li>
<li>父类的静态方法，也会被子类继承</li>
</ul>
<h2 data-id="heading-13">2.Object.getPrototypeOf()</h2>
<p><code>Object.getPrototypeOf</code> 方法可以用来从子类上获取父类。</p>
<pre><code class="copyable">console.log(Object.getPrototypeOf(B) === A) // true
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-14">3.super关键字</h2>
<ul>
<li>super()调用父类构造器</li>
<li>作为对象时，在普通方法中，指向父类的原型对象；在静态方法中，指向父类</li>
</ul></div>  
</div>
            