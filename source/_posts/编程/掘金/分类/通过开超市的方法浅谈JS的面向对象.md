
---
title: '通过开超市的方法浅谈JS的面向对象'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f3a5c5b9182453bbd9b2588426c9039~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 20 Apr 2021 21:42:04 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f3a5c5b9182453bbd9b2588426c9039~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>【前言】</strong></p>
<p>在Java中，我们通常用关键字class来定义一个类，但JavaScript在ES6之前并没有class关键字，它不通过class来定义一个类，而是用函数代替。JavaScript中的函数不仅能执行普通功能，还能当class使用。</p>
<p><strong>【正文】</strong></p>
<p>在Java中，我们在类里面写入不同的方法，以便于对象去调用它，这是很鲜明的面向对象方式，对象与方法之间可以说存在血缘关系。但JavaScript中是没有血缘关系的，JS是基于原型式的面向对象。首先让我们用构造函数创建一个类：</p>
<pre><code class="copyable">`function Cat(name,color)&#123;//类

    this.name = name
    this.color = color
&#125;`
<span class="copy-code-btn">复制代码</span></code></pre>
<p>JavaScript中一般不会在类里面写入方法函数，因为这会让我们在每定义一个新的实例对象时，都执行一遍类里的方法函数，这样会占用过大的内存，带来不必要的负荷。我们一般在类里设置属性，用于接收实例对象创建时传过来的参数。那么，我们的方法函数在JavaScript中的面向对象时，是怎么进行设置与调用的呢？</p>
<p>这里我们引入一个新属性prototype，JS给出的方法是在方法上添加一个prototype属性，挂载在这上面的方法，会在实例化的时候给到实例对象，例如我们想要实现猫说话的功能，就需向Cat.prototype添加说话的方法函数</p>
<pre><code class="copyable">`Cat.prototype.sayHello=function()&#123;
    console.log("喵喵喵");//对象的方法不是自己的，而是由原型提高的，独立的，

&#125;`
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过new关键字产生的实例对象都有类的prototype上的属性和方法，我们的实例对象此时就能够调用这段方法函数，我们定义一只白猫叫钉钉</p>
<pre><code class="copyable">> let cat1=new Cat('钉钉','白色');
> cat1.sayHello();//喵喵喵
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们发现，实例对象cat1通过调用方法函数sayHello（）可以输出相应的值，那么此时我们是不是就可以说实例对象拥有这个方法了呢？或许你在Java里面可以这么说，但是JavaScript中并不是这样的，JS是基于原型式的面向对象，它的实例对象与方法函数之间并没有血缘关系，在这里我们打印实例对象cat1可知它并没有方法函数：</p>
<pre><code class="copyable">> cat1
> Cat&#123;name:钉钉，color：白色&#125;
> 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么大家会很疑惑，我的实例对象cat1上并没有sayHello方法函数啊？为啥可以使用呢？这时让我们引入__proto__，它是每个对象都有的属性。当你访问的当前对象没有的方法时，实例对象会去__proto__中查找，其实__proto__就相当于父类中的prototype，也就是Cat.prototype，我们通过“===”可知</p>
<pre><code class="copyable">> 
> cat1.__proto__===Cat.prototype
> true
> 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于我们父类中的prototype中挂载了方法，所以实例对象可以通过__proto__找到方法函数并且调用，如果父类中也没有这个方法，那他会去Object.__proto__中查找，这里就涉及到了原型链的相关知识，恕我还在学习阶段，才疏学浅，在此不作多言，感兴趣的小伙伴可以自行了解。</p>
<p>在这里我简单的画一个图来表明实例对象与它父类之间跟方法函数的联系</p>
<p><img alt="QQ图片20210421133814.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9f3a5c5b9182453bbd9b2588426c9039~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我们可以理解为，图中的Cat构造函数相当于一个大超市，而他的属性prototype就是超市里的货架，那么很容易理解，方法函数就是货架上的商品了，放什么商品放多少商品，这取决于你自己本身。而实例对象cat1可以理解为是员工，它通过__proto__与货架连接，也就是prototype，通过__proto__我们的员工就可以拿到货架中的商品，也就是prototype中挂载的方法函数。员工虽然可以拿到货架上的商品，但你能说货架上的商品是你员工自己的么？那不管从什么逻辑层面来说，那显然都是不可以的。那么也就是说，咱们的实例对象虽然可以拿到方法函数，但方法函数并不属于实例对象本身，它本身并没有方法函数，它只是能够拿到货架上的商品而已。</p>
<p>注：其中思想学习自阮一峰</p>
<p><a href="http://www.ruanyifeng.com/blog/2010/05/object-oriented_javascript_encapsulation.html" target="_blank" rel="nofollow noopener noreferrer">www.ruanyifeng.com/blog/2010/0…</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            