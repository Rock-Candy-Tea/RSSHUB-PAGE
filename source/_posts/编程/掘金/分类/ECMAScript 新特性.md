
---
title: 'ECMAScript 新特性'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c57772dd152741deabeb6f51ff77c4d1~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 14 Jun 2021 09:03:18 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c57772dd152741deabeb6f51ff77c4d1~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">ECMAScript 的概述</h2>
<ul>
<li>ECMAScript 是一本脚本语言，缩写为ES，通常看做为JAVAScript 的标准化规范，实际是 JAVAScript 是ECMAScript的扩展语言，因为在ECMAScript 当中只是提供了最基本的语法(就是约定了我们的代码该如何编写，例如：如何定义变量和函数...)只是停留在语言层面，并不能完成页面当中的实际功能开发。我们经常使用的JAVAScript它实现了ECMAScript语言的标准，并且在这个基础之上做了扩展，使得我们可以在浏览器上操作DOM，BOM，在node环境可以去做读写文件之类的一些操作。</li>
<li>总的来说在浏览器环境当中的JAVAScript，它就等于 ECMAScript + web提供的API(BOM,DOM )</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c57772dd152741deabeb6f51ff77c4d1~tplv-k3u1fbpfcp-watermark.image" alt="1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>在node环境当中所使用的JAVAScript =  ECMAScript + node提供的API</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/abe73e9d9bab4ca68049c5fa963de854~tplv-k3u1fbpfcp-watermark.image" alt="2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>JAVScript 中语言本身就是 ECMAScript。随着web这种模式深入的发展，从2015年开始 ES 保持着每年一个版本的迭代，很多新特性陆续出现。导致JAVAScript 这门语言的本身也就变得越来越高级，越来越便捷。</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ae5e7f9e42b4f01af36a2d8cdd0a9ac~tplv-k3u1fbpfcp-watermark.image" alt="3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">ES2015 概述</h2>
<ol>
<li>解决原有语法上的一些问题或者不足。例如：let和const提供的块级作用域。</li>
<li>对原有语法进行增强，使之变得更为便捷易用。例如：解构，展开，参数默认值，模板字符串...</li>
<li>全新的方法，全新的功能，全新的对象。例如：promise,proxy,Object.assign()。</li>
<li>全新的数据类型和数据解构。例如：Symbol,set,map...</li>
</ol>
<h3 data-id="heading-2">ES2015与let块级作用域</h3>
<ul>
<li>在ES2015之前，ES中只有两种作用域 (全局作用域,函数作用域)
<ul>
<li>全局作用域</li>
<li>函数作用域</li>
<li>块级作用域 (ES2015新增)</li>
</ul>
</li>
<li>以前块是没有单独的作用域的，在块中定义的成员，外部是可以访问到的。</li>
</ul>
<p>例如：</p>
<pre><code class="copyable">    if(true)&#123;
        var foo = 123
    &#125;
    console.log(foo)//123 
    //对于复杂代码是非常不利的也是不安全的
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用es2015新增的let</li>
</ul>
<pre><code class="copyable">    if(true)&#123;
        let foo = 123
    &#125;
    console.log(foo)//foo is not defined
    //在块级作用域内定义的成员，外部是无法访问的。
    
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">const</h3>
<ul>
<li>用来声明一个只读的常量(恒量)，特点是在let的基础上多了一个只读的特性。</li>
</ul>
<h3 data-id="heading-4">数组的结构</h3>
<ul>
<li>数组的结构是根据位置，因为数据中的元素有下标，它是有规则的。</li>
</ul>
<pre><code class="copyable">    const arr = [100,200,300,4]
    const [foo,bar,baz] = arr;
    console.log(foo,bar,baz)//100 200 300
    //-----------------------------------------
    const [foo,...reset] = arr;
    console.log(reset)// [ 200, 300, 4 ]
    // reset 从当前位置往后的所有成员，并把他们放到一个数组中。注意：只能在我们解构的最后一个位置用。
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">    //如果解构的个数小于被解构的数组长度，会按照从前到后的位置被提取。
    const arr = [100,200,300,4]
    const [foo] = arr;
    console.log(foo)//100
    //如果结构的个数大于被解构的数组长度，会显示undefined
    const [foo,bar,baz,boo,coo] = arr;
    console.log(coo)//undefined
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">对象的结构</h3>
<pre><code class="copyable">    const obj = &#123; name: "ykk", age:20 &#125;
    const &#123; name, phone = "123000"&#125; = obj
    console.log(phone)//123000  添加默认值
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">    const obj = &#123; name: "ykk", age:20 &#125;
    let name = "kee"
    const &#123; name: objName &#125; = obj
    console.log(objName)//ykk  如果对象的结构命名和外面的命名发生冲突，我们可以给他重命名 例如 objName
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">    const obj = &#123; name: "ykk", age:20 &#125;
    let name = "kee"
    const &#123; name: objName = "default value"&#125; = obj
    console.log(objName)//ykk  还可以给重命名添加默认值 
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">模板字符串</h3>
<pre><code class="copyable">    //传统的字符串并不支持换行，如果我们的字符串有换行符我们需要用\n字符来表示。
    //在最新的模板字符串中，他可以支持多行字符串可以在模板中直接进行换行
    const str = `hello es2015 
    this is a string`
    console.log(str)
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">    //通过插值表达式来嵌入字符串所对应的数值，不仅可以嵌入变量，还可以嵌入任何标准的js语句
    const name = "tom"
    const str = `HEY $&#123;name&#125;---$&#123;1+1&#125; ----$&#123;true?0:1&#125; --- $&#123;Math.random()&#125;`
    console.log(str)//HEY tom---2 ----0 --- 0.22368499859594526
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>带标签的模板字符串</li>
</ul>
<pre><code class="copyable">    //标签实际上是一个特殊的函数，添加这个标签就是调用这个函数
    const str = console.log`hello word`//[ 'hello word' ]

    const name = "tom"
    const gender = true
    function myTagFunc(strings,name,gender)&#123;
    // console.log(strings)//[ 'HEY, ', ' IS A ', '.' ] 按照表达式分割过后静态的内容,所以他是一个数组
    // console.log(name,gender)//tom true
    const sex = gender? "man" : "woman"
    return strings[0] + name +strings[1]+ sex + strings[2]
    &#125;

    const result = myTagFunc`HEY, $&#123;name&#125; IS A $&#123;gender&#125;.`
    console.log(result)
    //标签的函数还可以接受到所有这个模板字符串表达式的返回值，比如：name gender
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">ES2015 字符串的扩展方法</h3>
<pre><code class="copyable">    //字符串的扩展方法
    const message = "Error: foo is not defined"
    console.log(
        // message.startsWith("Error")//是否以Error开头
        // message.endsWith("defined")//是否以defined结尾
        // message.includes("foo")//是否包含foo
    )
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">参数默认值</h3>
<pre><code class="copyable">    //函数参数的默认值
    // function foo (enable)&#123;
    // //   enable = enable || true
    //     enable = enable === undefined ? true : enable
    //   console.log(enable)
    // &#125;
    // foo(false)
    function foo (enable = true)&#123;
        console.log(enable)//false
    &#125;
    foo(false)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">剩余数组</h3>
<pre><code class="copyable">    // function foo()&#123;
    //    console.log(arguments)
    // &#125;
    // foo(1,2,3,4)
    function foo(num,...args)&#123;
        //必须要放在最后一位,并且只能使用一次
        console.log(args) //[ 2, 3, 4 ]
    &#125;
    foo(1,2,3,4)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">展开数组</h3>
<pre><code class="copyable">    const arr = [1,2,3]
    console.log(...arr)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-11">箭头函数</h3>
<ul>
<li>箭头函数可以使我们的代码更简短，易读</li>
</ul>
<h3 data-id="heading-12">对象的字面量</h3>
<pre><code class="copyable">    //对象字面量
    const bar = 1
    const obj = &#123;
        bar,
        method1()&#123;
            console.log("11")
        &#125;,
        [bar]:123,
        [Math.random()]:456
    &#125;
    console.log(obj)
    obj.method1()
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-13">对象的扩展方法</h3>
<h4 data-id="heading-14">Object.assign()  将多个源对象的属性赋值到一个目标对象</h4>
<pre><code class="copyable">    const source1 = &#123;
        a:123,
        b:456
    &#125;
    const target = &#123;
        a:999,
        b:888
    &#125;
    const source2 = &#123;
        a:1000,
        c:666
    &#125;
    const result = Object.assign(target,source1,source2)//&#123; a: 1000, b: 456, c: 666 &#125;
    console.log(result === target)//true
    //如果源对象和目标对象有相同的属性，源对象会把目标对象覆盖，
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">    function func(obj)&#123;
        // obj.name = "ykk"
        //使用Object.assign()给他赋值给一个新的目标对象，这样就不会影响外面定义的obj对象了
        const result = Object.assign(&#123;&#125;,obj)
        result.name = "ykk"
        result.aa = "123"
    &#125;
    const obj = &#123; name: "uuu" &#125;
    func(obj)
    console.log(obj)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-15">Object.is() 用来判断两个值是否相等</h4>
<ul>
<li>两个等号的运算符，会在比较之前自动转换数据类型</li>
</ul>
<pre><code class="copyable">    console.log(
        0==false,//true
        0===false,//false
        NaN===NaN,//false
        +0 === -0,//true
        Object.is(+0 , -0),//false
        Object.is(NaN , NaN)//true
    )
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-16">Proxy</h4>
<ul>
<li>如果我们想要监视某个对象的读写，可以使用es5提供的Object.defineProperty。</li>
</ul>
<pre><code class="copyable">    const person = &#123;
        name:"uu",
        age:30
    &#125;

    const personProxy = new Proxy(person,&#123;
        get(target,property)&#123;
        return  property in target ? target[property] : undefined
        &#125;,
        set(target,property,value)&#123;
            target[property] = value
        &#125;
    &#125;)
    console.log(personProxy.xx)
    console.log(personProxy.age)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-17">Proxy VS Object.defineProperty()</h4>
<ul>
<li>Object.defineProperty()只能够监视属性的读写</li>
<li>Proxy优点
<ol>
<li>Proxy 能够监视更多对象的操作，例如delete操作，对对象当中方法的调用</li>
</ol>
<pre><code class="copyable">    const person = &#123;
        name:"uu",
        age:30
    &#125;
    const personProxy = new Proxy(person,&#123;
        deleteProperxy(target,property)&#123;
            console.log(target,property)
        delete target[property]
        &#125;
    &#125;)

    delete person.name
    console.log(person)//&#123; age: 30 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>Proxy 更好的支持数组对象的监视</li>
</ol>
<pre><code class="copyable">    const list = []
    const result = new Proxy(list,&#123;
        set (target,property,value)&#123;
        console.log('set',property,value)
        target[property] = value
        return true
        &#125;
    &#125;)
    result.push(100)
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>proxy是以非侵入的方式监管了对象的读写。一个定义好的对象不需要对对象做任何操作，就可以监视到他内部的读写。Object.defineProperty()就需要用特定的方式，单独去定义对象当中那些需要被监视的属性，对于一个已经存在的对象，需要对它做很多额外的操作。</li>
</ol>
</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/394a1318a6054271a9180085f711ea37~tplv-k3u1fbpfcp-watermark.image" alt="4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-18">Reflect 统一的对象操作API</h3>
<ul>
<li>reflect 是一个静态类，不能够通过 new Reflect().</li>
<li>Reflect 封装了一系列对对象的底层操作</li>
<li>Reflect 成员方法就是 Proxy 处理对象的默认实现</li>
</ul>
<pre><code class="copyable">    const person = &#123;
        name:"ykk",
        age:20
    &#125;

    const p = new Proxy(person,&#123;
        get(target,property)&#123;
        console.log("wtach log")
        return Reflect.get(target,property)
        &#125;
    &#125;)
    console.log(p.name)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>Reflect对象最大的意义是他提供了统一一套用于操作对象的API。因为之前操作对象的时候，有可能会使用Object的方法，也有 in 或者 delete 这样的操作符，对于一些新手来说太乱了，并没有什么规律。Reflect对象就很好的解决了这个问题，统一了对象的操作方式</li>
</ul>
<pre><code class="copyable">    const obj = &#123;
        name:"23",
        age:12
    &#125;
    // console.log("name" in obj) 是否存在某个属性
    // delete  obj["name"] 删除对象的某个属性
    // console.log(obj)
    // console.log(Object.keys(obj)) 获取对象的所有属性

    console.log(Reflect.has(obj,'name'))
    console.log(Reflect.deleteProperty (obj,'age'))
    console.log(Reflect.ownKeys(obj))
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-19">Promise</h3>
<ul>
<li>一种全新的异步编程解决方案，通过链式调用方式，解决了传统异步编程中回调函数嵌套过深的问题。</li>
</ul>
<h3 data-id="heading-20">class</h3>
<pre><code class="copyable">    // function Person(name)&#123;
    //     this.name = name
    // &#125;

    // Person.prototype.say = function ()&#123;
    //      console.log(`hi my name is $&#123;this.name&#125;`)
    // &#125;

    // let p = new Person("tom")

    // p.say()

    class Person&#123;
        constructor(name)&#123;
        this.name = name
        &#125;

        say()&#123;
            console.log(`hi my name is $&#123;this.name&#125;`)
        &#125;
    &#125;

    let p = new Person("jack")
    p.say()
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>这种独立定义的语法，相比较之前函数的方式更容易理解，结构更加清晰</li>
</ul>
<h3 data-id="heading-21">ES2015 静态方法</h3>
<pre><code class="copyable">    // static 方法
    class Person &#123;
        constructor(name)&#123;
            this.name = name
        &#125;

        say()&#123;
            console.log(this.name)
        &#125;
        // 给当前类型 person 去添加一个create 静态方法,用于创建 person类型的实例
        static create(name)&#123;
            return new Person(name)
        &#125;
    &#125;

    let p =Person.create("tom")
    p.say()
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>注意：因为静态方法是挂载到类型上面的，所以在静态方法内部他的this就不会指向某一个实例对象，而是当前的类型</li>
</ul>
<h3 data-id="heading-22">ES2015 类的继承</h3>
<ul>
<li>在es2015之前使用继承大多都是用原型的方式去实现继承。在2015中实现了一个专门实现类型继承的关键词 extends。</li>
<li>extends 相比于原型继承更方便，更清楚</li>
</ul>
<pre><code class="copyable">    class Person&#123;
    constructor(name)&#123;
        this.name = name
    &#125;

    say()&#123;
        console.log("person",this.name)
    &#125;
    &#125;
    //Student 继承 Person。Student类型当中就会有Person所有的成员了
    class Student extends Person&#123;
        constructor(name,number)&#123;
            //super对象始终指向父类，调用它就像调用父类的构造函数
            super(name)
            this.number = number
        &#125;

        hello()&#123;
            super.say()
            console.log("Student",this.number)
        &#125;
    &#125;

    let student = new Student("jack",2)
    student.hello()
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-23">ES2015 Set</h3>
<ul>
<li>set数据结构，可以理解为集合，与传统的数组比较相似，不过set内部的成员是不允许重复的，每一个值在同一个set中都是唯一的。</li>
</ul>
<pre><code class="copyable">    //set 数据结构

    let s = new Set()
    //add方法添加一些数据，因为这个方法返回集合本身，所以可以链式调用
    s.add(1).add(2).add(3).add(4).add(5)

    //通过size属性获取整合集合的长度，与数组中的length相同
    // console.log(s.size)

    // s.forEach(i=>console.log(i))
    // for(let val of s)&#123;
    //     console.log(val)
    // &#125;
    console.log(s.has(1))//是否存在某一个特定的值
    console.log(s.delete(1))//删除某一个值
    // s.clear()//清楚当前集合当中的全部内容
    // console.log(s)

    //数组去重

    let arr = [1,2,3,4,2,4,5]
    // let result = Array.from(new Set(arr))
    let result = [...new Set(arr)]

    console.log(result)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-24">ES2015 Map</h3>
<pre><code class="copyable">    //map 数据结构

    // let obj = &#123;&#125;
    // obj[true] = "value"
    // obj[123] = 1
    // obj[&#123;a:1&#125;] = "value"
    // obj['[object Object ]'] = "value"
    // console.log(obj)
    // &#123;
    //     true: 'value',
    //     '[object Object]': 'value',
    //     '[object Object ]': 'value'
    // &#125;
    // console.log(Object.keys(obj))//[ '123', 'true', '[object Object]', '[object Object ]' ]
    //对象的建只要不是字符串类型都会转化为字符串(进行toString)，每一个对象toString的结构默认都是一样的，并不能进行区分。为了解决这个问题，就有了map这样的数据结构，
    //map数据结构才是严格意义上的键值对集合，用来映射两个任意类型集合对应的关系。

    let map = new Map ()
    let tom = &#123; name: 'jack'&#125;
    map.set(tom,20)
    map.set(true,1).set("num","123")
    // console.log(map.has(tom))
    // console.log(map.delete(tom))
    // map.clear()
    map.forEach((value,key) =>&#123;
        console.log(value,key)
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>map与对象最大的不同就是他可以用任意类型的数据作为键，而对象实际上只能使用字符串作为键</li>
</ul>
<h3 data-id="heading-25">ES2015 Symbol</h3>
<ul>
<li>在ES2015之前对象的属性名都是字符串，而字符串有可能就会有重复的，重复的话就会产生冲突。</li>
<li>通过Symbol创建的每一个值都是唯一的，他永远不会重复</li>
</ul>
<pre><code class="copyable">    // const s = Symbol()
    // console.log(s)
    // console.log(typeof s)//symbol
    // 通过typeof 打印出来symbol，表示他确实是一种全新的数据类型。

    // console.log(
    //     Symbol() === Symbol() false
    // )
    //Symbol 类型最大的特点就是独一无二的，通过他创建的类型永远都不会重复

    // console.log(Symbol("foo"))
    // console.log(Symbol("bar"))
    // console.log(Symbol("baz"))

    // Symbol 可以传入一个字符串，作为这个值得描述文本，对于多次使用Symbol的情况，便于我们区分到底是那个对应的Symbol

    //从ES2015开始，对象就可以使用Symbol类型的值作为属性名，现在对象的属性名可以是两种类型，一种是字符串，一种是Symbol

    // const obj = &#123;&#125;
    // obj[Symbol()] = 123
    // obj[Symbol()] = 456
    // console.log(obj)
    //因为Symbol的值都是独一无二的，所以就不用担心可能会产生冲突的问题。

    //使用计算属性名的方式，在对象字面量当中去使用Symbol作为对象的属性名
    // const obj = &#123;
    //     [Symbol()] :123
    // &#125;
    // console.log(obj)

    //Symbol除了可以避免对象属性名重复产生的问题，我们还可以借助Symbol这种类型特点，去模拟对象的私有成员。
    //a.js==============================
    const name = Symbol()
    const person = &#123;
        [name]:123,
        say()&#123;
            console.log(this[name])
        &#125;
    &#125;
    //b.js==============================
    // console.log(person[name])//因为我们没有办法在创建一个完全相同的Symbol，所以我们就不能去访问到这个成员，只能去调用这个成员当中普通名称的成员
    person.say()
    //Symbol最主要的的作用就是为对象添加独一无二的属性名
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-26">ES2015 Symbol 补充</h3>
<pre><code class="copyable">    // console.log(
    //     Symbol() === Symbol(), //false
    //     Symbol("foo") === Symbol("foo")//false
    // )
    //通过Symbol函数创建的值都是唯一，不管我们的传入的描述文本是不是相同的，每次调用Symbol函数得到的结构都是全新的一个值。
    //假如我们想在全局去复用一个相同的Symbol值，我们可以使用全局变量的方式去实现或者使用Symbol类型提供的静态方法去实现。

    // for方法可以接受一个字符串作为参数，相同的字符串返回相同的Symbol类型的值。这个方法内部维护了一个全局的注册表，为字符串和Symbol值提供了一个一一对应的关系
    // const s1 =  Symbol.for("foo")
    // const s2 =  Symbol.for("foo")
    // console.log(
    //     s1 === s2 //true
    // )

    //注意： for方法内部维护的是字符串和Symbol对应的关系，如果我们传入的不是字符串，这个方法内部会把它转化为字符串。这样就会导致我们传入布尔值的true和字符串的 "true"结果拿到的是一样的。

    // console.log(
    //     Symbol.for(true) === Symbol.for("true")//true
    // )

    //在Symbol类型当中还提供了很多内置的Symbol常量，用来作为内部方法的标识。这些标识符可以让自定义对象实现一些js当中内置的接口
    // console.log(Symbol.iterator)
    // console.log(Symbol.hasInstance)

    //自定义对象的toString标签
    // const obj = &#123;
    //     //如果使用字符串标签去添加标识符，有可能会和内部的成员产生重复,ECMAScript要求我们使用Symbol去实现这个的一个接口
    //     [Symbol.toStringTag]:"xObject"
    // &#125;
    // console.log(obj.toString())//[object xObject] 

    const obj = &#123;
        [Symbol()]:"symbol value",
        foo:123
    &#125;
    for(let val in obj)&#123;
        console.log(val) //foo
    &#125;
    console.log(Object.keys(obj))//[ 'foo' ]
    console.log(JSON.stringify(obj))//&#123;"foo":123&#125;
    //使用Symbol值作为对象的属性名，通过传统的for in 循环和Object.keys是无法拿到的。通过JSON.stringify去序列化对象为一个JSON字符串Symbol属性也是会忽略掉。
    //通过以上三种方法都无法获取Symbol属性名，这些特性使得Symbol类型的属性特别适合作为对象的私有属性。

    //如果想获取对象的Symbol属性也不是没有办法，我们可以使用Object.getOwnPropertySymbols方法，类似于对象的Object.keys(）方法。
    //Object.keys()方法只能够获取到对象中所有的字符串属性名
    //Object.getOwnPropertySymbols()获取的是Symbol类型的属性名
    console.log(Object.getOwnPropertySymbols(obj))//[ Symbol() ]
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-27">for of 循环</h3>
<ul>
<li>在ECMAScript当中遍历数据有很多种方法，最基本的for循环，比较适用于遍历普通的数组，然后还有for in 循环 比较适合遍历键值对，还有一些函数式的遍历方法... 例如数组对象的forEach方法。各种各样的遍历数据方式都有一定的局限性。所以es2015借鉴了很多其他的语言，引入了一种全新的遍历方式 for of 循环。</li>
<li>for of 循环作为遍历所有数据结构的统一方式。</li>
</ul>
<pre><code class="copyable">    const arr = [ 100, 200, 300, 400 ]

    // for(let item of arr)&#123;
    //     console.log(item)
    // &#125;
    //for of 循环拿到的是数组的每一个元素，而不是对应的下标。

    for(let item of arr)&#123;
        console.log(item)
        if(item>100)&#123;
            break
        &#125;
    &#125;
    //for of 可以跳转循环，随时终止遍历
    // arr.forEach()//不能跳出循环
    // arr.some()返回true可以跳出循环
    // arr.every()返回false可以跳出循环

    // const s = new Set(['foo','bar'])
    // for(const item of s)&#123;
    //     console.log(item)
    // &#125;

    // const m = new Map()
    // m.set("foo",123).set("boo",456)
    // for(const [key,value] of m)&#123;
    //     console.log(key,value)
    // &#125;
    const obj = &#123; name:'kk', age: 19 &#125;

    for(const item of obj)&#123;
        console.log(item) //obj is not iterable
    &#125;
    //for of 循环可以作为遍历所以数据结构的统一方式，但是却连最基本的普通对象都无法遍历？为什么？
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-28">可迭代接口</h3>
<ul>
<li>for...of 循环是一种数据统一遍历方式，但是经过试验，发现它只能够遍历数组之类的数据结构，对于普通的对象如果直接遍历就会报出错误。</li>
<li>ES能够表示有结构的数据类型越来越多，从最早的数组，对象到现在新增了set和map。开发者还可以组合使用这些类型去定义符合自己业务需求的数据结构。为了提供一种统一的遍历方式，ES2015就提出了一种Iterable接口，可迭代的。</li>
<li>可迭代接口就是一种可以被for...of循环统一遍历访问的规格标准。只要这个数据他实现了可迭代接口，他就能够被for..of循环去遍历。之前尝试的set map，数组可以被for...of遍历的数据，是因为他们内部都已经实现了这个接口</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4bae8a891084351962df00c0feb409f~tplv-k3u1fbpfcp-watermark.image" alt="arr.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/81a5d41a62684dd1bacb46091afbfd2f~tplv-k3u1fbpfcp-watermark.image" alt="map.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc700f7002ce4b11be70d7aebadf9904~tplv-k3u1fbpfcp-watermark.image" alt="set.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">const set = new Set(["foo","bar","coo"])
let interator = set[Symbol.iterator]()

console.log(interator.next())
console.log(interator.next())
console.log(interator.next())
console.log(interator.next())
console.log(interator.next())
//打印如下：
// &#123; value: 'foo', done: false &#125;
// &#123; value: 'bar', done: false &#125;
// &#123; value: 'coo', done: false &#125;
// &#123; value: undefined, done: true &#125;
// &#123; value: undefined, done: true &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-29">实现可迭代接口</h3>
<pre><code class="copyable">    //实现可迭代接口

    // const obj = &#123;
    //     //iterable
    //     [Symbol.iterator]:function()&#123;
    //         //iterator 内部必须要有一个next方法
    //         return &#123;
    //             next:function()&#123;
    //                 //iterationResult 实现迭代结果的接口
    //                 //这个接口约定的是在这个对象内部必须要有一个value属性用来表示当前被迭代到的数据，值可以是任意类型。
    //                 //还需要有一个done的布尔值，用来表示迭代有没有结束
    //                 return &#123;
    //                     value: "ykk",
    //                     done: true
    //                 &#125;
    //             &#125;
    //         &#125;
    //     &#125;
    // &#125;
    const obj = &#123;
        store:["foo","bar","boo"],
        [Symbol.iterator]:function()&#123;
            let self = this
            let index = 0
            return &#123;
                next:function()&#123;
                    const result = &#123;
                        value: self.store[index],
                        done: index>=self.store.length
                    &#125;
                    index ++
                    return result
                &#125;  
            &#125;
        &#125;
    &#125;

    for(const item of obj)&#123;
        console.log(item)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-30">ES2015 迭代器模式</h3>
<pre><code class="copyable">    //迭代器设计模式

    //场景： 两人协同共同开一个任务清单

    // 小明的代码======================
    const todos = &#123;
        life:["逛淘宝","花钱","买衣服","吃小龙虾"],
        learn:["语文","数学","英语"],
        work:["喝茶"],
        each:function(callback)&#123;
            let arr = [].concat(this.life,this.learn,this.work)
            for(const item of arr)&#123;
                callback(item)
            &#125;
        &#125;,
        [Symbol.iterator]:function()&#123;
            const arr = [...this.life,...this.learn,...this.work]
            let index = 0
            return &#123;
                next:function()&#123;
                    const result = &#123;
                        value:arr[index],
                        done:index++>=arr.length
                    &#125;
                    return result
                &#125;
            &#125;
        &#125;
    &#125;

    // 小红的代码===========================

    // for(const item of todos.life)&#123;
    //     console.log(item)
    // &#125;
    // for(const item of todos.learn)&#123;
    //     console.log(item)
    // &#125;
    // for(const item of todos.work)&#123;
    //     console.log(item)
    // &#125;
    //如果数据结构发生变化，添加了一个全新的类目，但是目前小红的代码和小明的代码数据结构是严重耦合的，也需要跟着一起去变化

    //数据结构可以对外提供一个统一的遍历接口

    todos.each(function(item)&#123;
        console.log(item)
    &#125;)

    for(const item of todos)&#123;
        console.log("迭代器",item)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>迭代器他的核心意义就是对外提供统一遍历接口，外部不用去关系数据的内部结构是什么样的,ES2015迭代器实现的语言层面的迭代器模式，可以适用于任何数据结构，只需要你的代码实现iterator方法，以及他的迭代逻辑。</li>
</ul>
<h3 data-id="heading-31">ES2015 生成器</h3>
<ul>
<li>引入Generator生成器的目的就是为了能够在复杂的异步代码中减少回调函数嵌套产生的问题,提供更好的异步编程解决方案</li>
</ul>
<pre><code class="copyable">    // function *foo()&#123;
    //     console.log("log")
    //     return 100
    // &#125;
    // const result = foo()
    // console.log(result.next())//&#123; value: 100, done: true &#125;
    // next方法的返回值与迭代器方法的返回值有相同的结构,说明 generator 也实现了 iterator接口

    function * foo()&#123;
        console.log(11)
        yield 100
        console.log(22)
        yield 200
        console.log(33)
        yield 300
    &#125;

    const result = foo()
    console.log(result.next())
    console.log(result.next())
    console.log(result.next())
    console.log(result.next())

    // 生成器函数会自动返回生成器对象，调用这个对象的方法，函数体开始执行，执行过程中遇到 yield关键词暂停下来，yield后面的值会作为后面的结果返回，周而复始。
    // 生成器函数最大的特点就是惰性执行。
    
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>generator 应用</li>
</ul>
<pre><code class="copyable">    // 使用generator 函数实现 iterator方法
    const todos = &#123;
        life:["逛淘宝","花钱","买衣服","吃小龙虾"],
        learn:["语文","数学","英语"],
        work:["喝茶"],
        [Symbol.iterator]:function * ()&#123;
            const arr = [...this.life,...this.learn,...this.work]
            for (const item of arr)&#123;
                yield item
            &#125;
        &#125;
    &#125;

    for (const item of todos)&#123;
        console.log(item)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-32">ES2016 概述</h3>
<ul>
<li>与ES2015相比 ES2016只是一个小版本，仅包含两个小功能。</li>
</ul>
<pre><code class="copyable">    //ES2016
    // Array.prototype.includes----------------
    const arr = ["foo", NaN, false]

    console.log(arr.indexOf("foo"))
    console.log(arr.indexOf(NaN))//false
    console.log(arr.includes(NaN))//true

    // ES2015之前我们查看数组当中是否存在某个值使用的是indexOf方法，indexOf不能查找数组当中是否存在NaN。 

    //指数运算符---------------------------------

    console.log(Math.pow(2,10))

    console.log(2 ** 10)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-33">ES2017 概述</h3>
<pre><code class="copyable">    const obj = &#123;
        foo:"value1",
        bar:"value2"
    &#125;
    // Object.values()返回对象当中所有值组成的数组----------------------------
    // console.log(Object.values(obj))
    // Object.entries()是以数组的方式返回对象的键值对-------------------------
    // console.log(Object.entries(obj))// [ 'foo', 'value1' ], [ 'bar', 'value2' ] ]

    // for (const [key,value] of Object.entries(obj))&#123;
    //     console.log(key,value)
    // &#125;

    console.log(new Map(Object.entries(obj)))//Map(2) &#123; 'foo' => 'value1', 'bar' => 'value2' &#125;
    // Object.getOwnPropertyDescriptors----------------------------------

    // String.prototype.padEnd------------------------------------
    // String.prototype.padStart----------------------------------
    //Async/Await
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            