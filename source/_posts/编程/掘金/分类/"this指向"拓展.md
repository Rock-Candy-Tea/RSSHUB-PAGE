
---
title: '"this指向"拓展'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec15e9cad8634bfcbc03820bf067174e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 12 Aug 2021 21:28:54 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec15e9cad8634bfcbc03820bf067174e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>昨天的时候想到，this可能指向一个构造函数内部作用域内，但是今天回顾了一下构造函数本体，构造函数本质也还是一个函数对象，所以根据this的特性，我认为this本质是构造函数内的一个内置变量，只不过没有被显式声明，其值应该是保存的实例对象的堆内存地址</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ec15e9cad8634bfcbc03820bf067174e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>this作为一个变量，其特性和其他普通var/let/const 定义or声明的变量是一样，而函数，无论是普通函数还是构造函数，其基本特性都是一样：本质也是一个引用类型的对象，每一个构造函数对象的本体，应该是在堆内存中的一块存储了静态执行代码的内存空间，而其静态执行代码中this，无论是在constructor中的"this.x = x\this.y = y"，还是方法toString中调用到的"this.x"，本质上都属于调用这个构造函数的内部作用域内的this这个变量（这个变量没有显式声明，我默认是内置，而且是顶级的）</p>
<p>那么无论是匿名函数还是命名函数，都认为是在堆内存中存储的静态执行代码，这些执行代码是静态的，也就是说其本身是静态不变的，就算其内部有一个this，当这个函数的代码处于堆内存中时没有任何意义和指代，就算定义的时候定义可能有错误的代码，也不影响其在堆内存中的状态，这一块堆内存地址被赋值给任何对象的属性，都不影响堆内存中的静态执行代码的状态和值，本身在堆内存中的所有代码都是没有状态的</p>
<p>那么函数中的代码执行是发生在何时呢？当函数执行，静态被压入执行栈，静态代码会自发的调用当前执行栈中的变量，比如说上图中的toString函数，其内部的静态代码中有this变量，但是这个this在堆内存中的时候是没有任何指向的，只有在调用的时候，才会自发的在调用它的作用域中去找this变量，比如说如果接下来：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db98851a4a5f47bdbf0d4c0280f8bd4c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>1、执行到point.toString()的时候， toString这个函数是挂载在Point这个构造函数内的同名toSting变量上的，所以执行的时候，也会在Point这个构造函数内部作用域内去找this变量，在Point构造函数内部的this是存在的（值的内容指向实例对象的堆内存地址），所以其值能输出</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6bf5b8b68c064f86bdfe8132bfb6b3ff~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7bd3f4b50ae4444e82b0a0356c6129e2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>2、执行到全局中的obj1()，即window.obj1()时，由于当前处于严格模式下，全局环境也就是说[Window]这个构造函数中，this === undefined(this这个变量未被显式定义)，把obj1这个变量的内存地址中的代码压入[Window]函数中的内部作用域中时，执行到toString函数中的静态代码"this.x"时，在当前作用域(Window)中找到的this变量未被定义，即undefined，所以会报错</p>
<p>3、所以1和2本质的区别在于，1中函数中的代码压入的执行栈是Point函数的内部作用域，2中压入的是全局[Window]函数的内部作用域，只不过Window函数的内部作用域就是全局作用域，在 obj1 = point.toString，这个过程，只是把toString这个函数的堆内存地址又赋值给了window.obj1这个变量一遍而已，堆内存地址的值随便赋值，都不会改变内存中的函数的静态执行代码，<del>区别在代码被压入执行栈中时能不能在当前执行栈中找到对应的变量而已</del>（感觉这句话不够准确，因为函数的内存地址被赋值给一个实例对象的属性上，当它执行的时候（如下图以dyinh.toString()的形式执行），实际上是在构造函数（如下图中的Dyinh）内部执行toString()，所以首先会在构造函数的内部作用域链去找对应的变量）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b42da9beec1147d999bae11854945afa~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>总结：</p>
<p>1、为对象增加属性和方法，相当于在对象的构造函数添加属性和方法，在全局中声明or定义一个变量则相当于在全局环境[Window]中添加对应的属性很方法</p>
<p>2、执行dyinh.toString()，相当于在构造函数内部执行toString():</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9d1a5666d1e46e8bf8b4b8ad0aaabc3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            