
---
title: '搞懂JavaScript中的this'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/76edde8a05794acb9e04b085277c50fe~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 18 Apr 2021 22:49:16 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/76edde8a05794acb9e04b085277c50fe~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>最近在准备面试，同步用文字梳理一下比较重要的知识点：</strong></p>
<p>所有的函数在被调用时，都会创建一个执行上下文</p>
<ul>
<li>这个上下文中记录着函数的调用栈、函数的调用方式、传入的参数信息等；</li>
<li>this也是其中的一个属性；</li>
</ul>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/76edde8a05794acb9e04b085277c50fe~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ol>
<li>函数在调用时，JavaScript会默认给this绑定一个值；</li>
<li>this的绑定和定义的位置（编写的位置）没有关系；</li>
<li>this的绑定和调用方式以及调用的位置有关系；</li>
<li>this是在运行时被绑定的；</li>
</ol>
<h2 data-id="heading-0">一、this绑定规则</h2>
<h4 data-id="heading-1">案例一：普通函数调用</h4>
<ul>
<li>该函数直接被调用，并没有进行任何的对象关联；</li>
<li>这种独立的函数调用会使用默认绑定，通常默认绑定时，函数中的this指向全局对象（window）；</li>
</ul>
<h3 data-id="heading-2">1.1. 默认绑定</h3>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7109fa748d0949e88530c0d7fef6fe02~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">案例二：函数调用链（一个函数又调用另外一个函数）</h4>
<ul>
<li>所有的函数调用都没有被绑定到某个对象上；</li>
</ul>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/96239ab24f934bec97abfec907363dde~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">案例三：将函数作为参数，传入到另一个函数中</h4>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2aa68ceb35942048f20b673810dfd2c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>这里的结果依然是window，为什么呢？</li>
<li>原因非常简单，在真正函数调用的位置，并没有进行任何的对象绑定，只是一个独立函数的调用；</li>
</ul>
<h3 data-id="heading-5">1.1. 隐式绑定</h3>
<p>另外一种比较常见的调用方式是通过某个对象进行调用的：</p>
<ul>
<li>也就是它的调用位置中，是通过某个对象发起的函数调用。</li>
</ul>
<h4 data-id="heading-6">案例一：通过对象调用函数</h4>
<ul>
<li>foo的调用位置是obj.foo()方式进行调用的</li>
<li>那么foo调用时this会隐式的被绑定到obj对象上</li>
</ul>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/44c0e8a431514288bffd38686cee539a~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-7">案例二：案例一的变化</h4>
<ul>
<li>我们通过obj2又引用了obj1对象，再通过obj1对象调用foo函数；</li>
<li>那么foo调用的位置上其实还是obj1被绑定了this；</li>
</ul>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/15307839fe864e39aef065bd8b4d83de~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">案例三：隐式丢失</h4>
<ul>
<li>结果最终是window，为什么是window呢？</li>
<li>因为foo最终被调用的位置是bar，而bar在进行调用时没有绑定任何的对象，也就没有形成隐式绑定；</li>
<li>相当于是一种默认绑定；</li>
</ul>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6e3c4cef7cea40a28e8e6475b1c1acdd~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">1.3. 显示绑定</h2>
<p>隐式绑定有一个前提条件：</p>
<ul>
<li>必须在调用的对象内部有一个对函数的引用（比如一个属性）；</li>
<li>如果没有这样的引用，在进行调用时，会报找不到该函数的错误；</li>
<li>正是通过这个引用，间接的将this绑定到了这个对象上；</li>
</ul>
<p>如果我们不希望在 对象内部 包含这个函数的引用，同时又希望在这个对象上进行强制调用，该怎么做呢？</p>
<ul>
<li>JavaScript所有的函数都可以使用call和apply方法（这个和Prototype有关）。</li>
<li>它们两个的区别其实非常简单，第一个参数是相同的，后面的参数，apply为数组，call为参数列表；</li>
<li>这两个函数的第一个参数都要求是一个对象，这个对象的作用是什么呢？就是给this准备的。</li>
</ul>
<p>在调用这个函数时，会将this绑定到这个传入的对象上。
因为上面的过程，我们明确的绑定了this指向的对象，所以称之为 显示绑定。</p>
<h4 data-id="heading-10">1.3.1. call、apply</h4>
<p>通过call或者apply绑定this对象
显示绑定后，this就会明确的指向绑定的对象</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60bb59a159904be1bf048aa37bfff056~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-11">1.3.2. bind函数</h4>
<p>如果我们希望一个函数总是显示的绑定到一个对象上，可以怎么做呢？
<img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/845fbaf12b9d4c5cb2e0606a5c0f9428~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-12">2.3.3. 内置函数</h4>
<p>有些时候，我们会调用一些JavaScript的内置函数，或者一些第三方库中的内置函数。</p>
<ul>
<li>这些内置函数会要求我们传入另外一个函数；</li>
<li>我们自己并不会显示的调用这些函数，而且JavaScript内部或者第三方库内部会帮助我们执行；</li>
<li>这些函数中的this又是如何绑定的呢？</li>
</ul>
<p>案例一：setTimeout</p>
<ul>
<li>setTimeout中会传入一个函数，这个函数中的this通常是window</li>
</ul>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d237495ed1a74a3ab02d29c5a2ce82c4~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
案例二：数组的forEach</p>
<p>数组有一个高阶函数forEach，用于函数的遍历：</p>
<ul>
<li>在forEach中传入的函数打印的也是Window对象；</li>
<li>这是因为默认情况下传入的函数是自动调用函数（默认绑定）；</li>
</ul>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e3866995716b452baddf4049d27cab25~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-13">1.4. new绑定</h2>
<p>JavaScript中的函数可以当做一个类的构造函数来使用，也就是使用new关键字。</p>
<p>使用new关键字来调用函数时，会执行如下的操作：</p>
<ol>
<li>创建一个全新的对象；</li>
<li>这个新对象会被执行Prototype连接；</li>
<li>这个新对象会绑定到函数调用的this上（this的绑定在这个步骤完成）；</li>
<li>如果函数没有返回其他对象，表达式会返回这个新对象；</li>
</ol>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/935d293f810a4e45975eec77e5ecd209~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-14">1.5. 规则优先级</h2>
<p><strong>new绑定 > 显示绑定（bind）> 隐式绑定 > 默认绑定</strong></p>
<h2 data-id="heading-15">二. this规则之外</h2>
<h4 data-id="heading-16">2.1. 忽略显示绑定</h4>
<p>如果在显示绑定中，我们传入一个null或者undefined，那么这个显示绑定会被忽略，使用默认规则：</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5d4a93b7f9f346d9926f6da8c611c4b1~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-17">2.2. 间接函数引用</h4>
<p>另外一种情况，创建一个函数的 间接引用，这种情况使用默认绑定规则。</p>
<p>我们先来看下面的案例结果是什么？</p>
<p>(num2 = num1)的结果是num1的值；</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/166feb76dcd0478a936e8da80d61ed1b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
我们来下面的函数赋值结果：</p>
<ul>
<li>赋值(obj2.foo = obj1.foo)的结果是foo函数；</li>
<li>foo函数被直接调用，那么是默认绑定；</li>
</ul>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4a0a3e73a5074a9680bb2c40295b5a91~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-18">2.3. ES6箭头函数</h4>
<p>箭头函数不使用this的四种标准规则（也就是不绑定this），而是根据外层作用域来决定this。</p>
<pre><code class="copyable">    ——————————————内容参考《你不知道的JS》及coderwhy的文章
<span class="copy-code-btn">复制代码</span></code></pre></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            