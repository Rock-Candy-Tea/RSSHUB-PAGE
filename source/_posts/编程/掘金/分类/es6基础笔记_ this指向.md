
---
title: 'es6基础笔记_ this指向'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ffa563f1154406aab08845b7ebc27e3~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 12 Aug 2021 00:25:14 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ffa563f1154406aab08845b7ebc27e3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">1、class中的this</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7ffa563f1154406aab08845b7ebc27e3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>上图的点分析理解：</p>
<p>1、在logger这个实例对象中的printName方法的this自然的指向logger本身（又或者说指向其构造函数本身的内存空间（执行的上下文？）？）</p>
<p>2、从对象中取出来（以es6解构的形式或者以赋值的形式）的本质是，在当前执行上下文（比如说全局window类）中声明一个新的同名对象，再将原实例对象中的匿名函数的地址传给window对象（这么一看，window本质上也是一个巨大的[Window]类的实例的对象，因为它的很多特性都符合一个类的特性），然后，该匿名函数就被挂载到window下面了</p>
<p>3、"this指向该方法运行时所在的环境"，执行的该方法已经被挂载在新的实例对象上了，这时候执行的不再是原对象中方法，而是新的实例对象上的同名方法了</p>
<p>4、当上级方法已经被挂载到新的执行上下文后，其内部的执行语句中的this，这个变量在当前的执行上下文（比如说Window类）中并没有被定义，所以this本身是undefined的，我感觉此时和class的严格模式本质上没啥关系，因为"this.A"的这种语法中的this本身就是在调一个变量，这样子的话，区别在于，在Window这个全局类中，没有内置this变量，所以在这里执行主函数的时候，内部调用的this这个变量在当前作用域链上找不到，所以结果是未定义不存在的。那么由此也可以推理，Window全局类和class or function类的一个区别，在class or function类中内置了"this"这个变量，且为其储值为实例对象，而Window中没有？感觉this代指的不只是一个实例对象，更像是当前这个class的内部变量环境。</p>
<p>5、我理解this本身应该也是代指一块内存空间，this本身也是一个变量，这个变量存储的值是一个类的实例在内存中的地址字符串（如ox12fe）or一个基础类型数据（如number、string……）</p>
<h2 data-id="heading-1">2、class中的this指向固定在实例对象的处理方案</h2>
<h3 data-id="heading-2">1、构造方法中绑定<code>this</code>：</h3>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3049c90b6c9f4d7faa7c5029bda9e7e0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7868708b9a8f4746bf4b288be1ca830e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>图文解析：</p>
<p>1、bind函数内部，将该函数绑定在全局的变量fn中，再返回一个匿名函数，该匿名函数本身指向调用的上下文，即全局环境window，但是真正执行的目标函数fn指向（在apply中已经绑定在新的实例对象上了，比如说这里的当前构造函数的this），所以这么几个转手下来，<code>核心点还是apply中将同名函数直接挂载在当前构造函数的内部作用域内</code>，那么实际上全局解构or赋值得到同名函数变量执行的是外部包裹的匿名函数，但是这个匿名函数内部执行的是挂载在构造函数上的主函数，主函数已经挂载构造函数中（的实例对象上->这个替换一下也相当于其实是在class中定义了这个函数，才能体现在实例对象的调用链上），所以，实际上主函数的执行环境已经进入到构造函数内部了，在构造函数内部中this就是class内置的this变量，即实例本身 -> 这样的话，可不可以推理，class类就相当于是一个小型的封闭的执行上下文环境？所以主函数内部的this.A()中的this在作用域链上是可以找到的，A也是存在于当前环境变量中的，所以A就能顺利执行</p>
<p>所以这本质上，是不是一个执行上下文的替换？</p>
<p>需不需要和内存联系起来呢？这个暂时还想不到呢</p>
<p>2、在上文提到的"挂载到一个实例对象上" => "挂载到该实例对象的构造函数的内置变量this对象中" ，而一个函数内部，本身也是一个小型的执行上下文、执行环境，存在自己的作用域链，而且，与内存联系起来的话，一个函数也是一个对象，对象内部是一些执行语句，执行语句在内存中是写死的，只有当它们被压入执行栈中，才会根据作用域链去找对应的变量的值，包括在构造函数中定义的方法函数中的this，本质也是一个代码符号，也是一个变量，如果其被压入的执行环境中没有对应的this变量，那就会报错咯</p>
<p>3、那这样子的话，其他的在给显式的对象增加属性和方法，本质上，是在给该对象的构造函数中添加属性方法，调用该属性的方法（obj.abc()）时，会自发的首先在构造函数的作用域链内找变量，挂载在对象中的方法，虽然实际上也是挂载一个引用地址，但是执行的时候，还是会把引用地址指向的内存中的代码压入执行栈，这些代码，应该全部是"真·代码"。</p>
<p>4、那么这样想的话，对象这个数据类型，虽然表现为一个键值对的形式，但是其实它指向一个完整的构造函数的内部作用域！显式对象其实只是这个构造函数的输出结果，那每一次的赋值和解构赋值，都只是将内存地址从一个构造函数转移到另一个构造函数的内部作用域中。</p>
<h3 data-id="heading-3">2、使用箭头函数</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7229e3d0cc9546d982c780752e069543~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>图文解析；</p>
<p>1、箭头函数的特性 -> "箭头函数内部的this总是指向定义时所在的对象"，这句话的含义应该是指，箭头函数的内存地址只挂载在定义时的那个作用域中，并且不会被转移，所以，定义的时候，应该是将主函数使用箭头函数来定义，这样主函数内部调用的this.a()函数的this还是能找到的，这样的话，名义是引用的匿名函数，但是实际上是引用的obj.main，执行的时候也是执行的obj.main</p>
<h3 data-id="heading-4">3、使用proxy</h3>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c6b1381277e542eaa3918baa2f2c2ea5~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>图文解析：</p>
<p>1、我需要补充一下相关知识点 proxy和WeakMap</p>
<p>暂停</p></div>  
</div>
            