
---
title: 'ES6新增语法(二)——函数和参数'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=9915'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 22:36:15 GMT
thumbnail: 'https://picsum.photos/400/300?random=9915'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">箭头函数</h2>
<p>箭头函数：将原来函数的function关键字和函数名都删掉，并使用”=>”连接参数列表和函数体。</p>
<p>箭头函数语法：</p>
<p>(参数1,参数2)=>&#123;</p>
<p>函数体</p>
<p>&#125;</p>
<p>注意点：</p>
<ul>
<li>当参数有且只有一个，括号可以省略。没有参数或多个参数时，括号不能省略。</li>
<li>如果函数体有且只有一个表达式时，可以省略花括号。</li>
</ul>
<p>箭头函数使用实例：</p>
<pre><code class="copyable">window.onload = ()=>&#123;
 console.log('网页加载完成')
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参数只有一个时，省略掉括号。函数体只有一个表达式，花括号也省略。如：</p>
<pre><code class="copyable">let arr=[1,2,3,4]
arr.forEach((item)=>
 console.log('item',item)
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>This指向问题</strong></p>
<p>1、在全局环境下，this始终指向全局对象，无论是否严格模式。</p>
<p>2、普通函数内部的this分严格模式和非严格模式。</p>
<ul>
<li>严格模式下this为undefined。</li>
<li>非严格模式下，this指向全局对象window。</li>
</ul>
<p>3、箭头函数的 this 是上下文的this。</p>
<p>箭头函数相当于匿名函数，并且简化了函数定义，但箭头函数和匿名函数有个明显的差异，箭头函数内部的this是词法作用域，上下文的this值作为自己的this值。</p>
<ul>
<li>Call()、apply()、bind()方法对于箭头函数只是传入参数，对它的this毫无影响。</li>
<li>考虑到this是词法层面上的，严格模式中与this相关的规则都将被忽略。</li>
</ul>
<p>放在setTimeout中的两个箭头函数返回的this举例。</p>
<pre><code class="copyable">function Person(name,age)&#123;
 this.name = name;
 this.age = age;
 setTimeout(()=>&#123;
  console.log('this',this) //Person &#123;name: "倩倩", age: 18&#125;
 &#125;,100)
&#125;
let p = new Person('倩倩',18)
setTimeout(()=>&#123;
 console.log("this",this)//Window &#123;window: Window, self: Window, document: document, name: "", location: Location, …&#125;
&#125;,1000)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">函数参数的默认值</h2>
<p>在ES6之前，不能直接为函数的参数指定默认值，只能采取变通措施。</p>
<p>实例：普通函数给参数设置默认值</p>
<pre><code class="copyable">function sum(a,b)&#123;
 a = a | 12;
 b = b | 5;
 return a+b
&#125;
console.log('相加等于',sum())// 17
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ES6允许函数参数设置默认值，即直接写在参数定义的后面。如</p>
<pre><code class="copyable">function sum(a=12,b=5)&#123;
 return a+b
&#125;
console.log('相加等于',sum())
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>ES6默认参数优点：</strong></p>
<ul>
<li>简洁，适用于参数多的时候，方便设置默认值。</li>
<li>阅读代码的人可以看出哪些参数是可以省略的，不用查看函数体或文档。</li>
<li>有利于代码的优化，即使未来版本拿掉这个参数，以前代码也可以运行，还有参数变量是默认声明的，不能在函数体内部再进行声明。</li>
</ul>
<p>与解构赋值结合使用</p>
<pre><code class="copyable">function add(&#123;x=1,y=2&#125;=&#123;&#125;)&#123;
 return x+y
&#125;
console.log('相加等于',add(&#123;x:2&#125;)) // 相加等于 4
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">ES6函数不定参数和展开运算符</h2>
<p>不定参数：
语法：...
类型：数组
作用：指定多个各自独立的参数，通过整合后的数组来访问。
限制：</p>
<ul>
<li>最多只能声明一个</li>
<li>只能放在参数末尾</li>
</ul>
<p>实例：简单应用</p>
<pre><code class="copyable">function show( a, ...args)&#123;
 console.log('a',a)
 console.log('args',...args)
&#125;
show(1,2,3)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>展开运算符：</strong></p>
<p>语法：...
作用：指定数组或对象，将他们打散后作为各自独立的参数。</p>
<p>实例：使用展开运算符展开数组。</p>
<pre><code class="copyable">let arr = ['a','b','c']
let arr2 = []
arr2.push(...arr)
console.log('arr2',arr2)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>实例：使用展开运算符展开对象。</p>
<pre><code class="copyable">let person = &#123;
 name :'倩倩',
 age:18
&#125;
let worker = &#123;
 ...person,
 job:"打杂"
&#125;
console.log('worker',worker)//&#123;name:'倩倩',age:18,job:'打杂'&#125;
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            