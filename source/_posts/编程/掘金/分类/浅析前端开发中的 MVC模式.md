
---
title: '浅析前端开发中的 MVC模式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://juejin.cn/post/6991766626618048542'
author: 掘金
comments: false
date: Mon, 02 Aug 2021 01:46:17 GMT
thumbnail: 'https://juejin.cn/post/6991766626618048542'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">MVC</h1>
<p>MVC 是常见的软件架构设计模式（Architectural Pattern），它通过分离关注点来改进代码的组织方式。不同于设计模式（Design Pattern），只是为了解决一类问题而总结出的抽象方法，一种架构模式往往使用了多种设计模式。</p>
<p>在没有了解到MVC之前，我们写项目的时候会把所有的内容都写到同一个JS文件中，在实现了多个页面后我们发现这些页面有很多重复的东西，而且每个页面内容十分冗杂，对后续的维护更新带来了比较大的麻烦。</p>
<p>为了解决上面的问题，前端开发者使用MVC架构模式对页面代码进行优化。</p>
<p>MVC，即Model-View-Controller，分别对应着一个页面的数据层，视图层，逻辑层。</p>
<ul>
<li>最简单的MVC通信方式：</li>
</ul>
<blockquote>
<ol>
<li>View传递信息给Controller。</li>
<li>Controller完成逻辑后，传递信息给Model改变数据。</li>
<li>Model将新的数据发送给View，修改界面。</li>
</ol>
</blockquote>
<ul>
<li>
<p>MVC架构模式在实际的使用中，有更加灵活的方式：</p>
<p>BackboneJS框架使用的就是MVC架构模式，但是它在MVC通信的方式上更加地灵活</p>
</li>
</ul>
<p><img src="https://juejin.cn/post/6991766626618048542" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<ol>
<li>用户可以向 View 发送指令（DOM 事件），再由 View 直接要求 Model 改变状态。</li>
<li>用户也可以直接向 Controller 发送指令（改变 URL 触发 hashChange 事件），再由 Controller 发送给 View。</li>
<li>Controller 非常薄，只起到路由的作用，而 View 非常厚，业务逻辑都部署在 View。所以，Backbone 索性取消了 Controller，只保留一个 Router（路由器） 。</li>
</ol>
</blockquote>
<h3 data-id="heading-1">MVC的特点</h3>
<h4 data-id="heading-2">优点</h4>
<ol>
<li>
<p>耦合性低</p>
<p>M、V、C三个模块相互之间的影响非常地小，当对其中一个模块进行维护升级、数据搬运等工作时，对其他的模块影响极小。</p>
</li>
<li>
<p>重用性高</p>
<p>MVC允许使用各种不同样式的视图来访问同一个服务器端的代码。只需要改变View的实现方式即可，而无需对数据层，逻辑层进行改动。</p>
</li>
<li>
<p>部署快、可维护性高</p>
<p>使用MVC模式使开发时间得到相当大的缩减。因为模块的分离，所以开发者可以主力攻坚其中一个模块，而不需要多头兼顾。而且由于分离了视图层和逻辑层，也更易于维护。</p>
</li>
</ol>
<h4 data-id="heading-3">缺点</h4>
<ol>
<li>
<p>定义模糊</p>
<p>MVC的概念非常模糊，每个开发者可能对它的理解都不尽相同。</p>
</li>
<li>
<p>不适合中小型规模项目</p>
<p>由于MVC整体比较复杂，对于中小型项目可能反而会使他们更加笨重。对于简单的界面，严格遵循MVC，使模型、视图与控制器分离，会增加结构的复杂性，并可能产生过多的更新操作，降低运行效率。</p>
</li>
</ol>
<h2 data-id="heading-4">Model&View</h2>
<p>这里有一个可以对数值进行加减操作的组件：上面显示数值，两个按钮可以对数值进行加减操作，操作后的数值会更新显示。</p>
<p><img src="https://juejin.cn/post/6991766626618048542" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们将依照这个“栗子”，尝试用JavaScript实现简单的具有MVC/MVP/MVVM模式的Web应用。</p>
<h3 data-id="heading-5">Model</h3>
<p>Model层用于封装和应用程序的业务逻辑相关的数据以及对数据的处理方法。这里我们把需要用到的数值变量封装在Model中，并定义了add、sub、getVal三种操作数值方法。
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d91d1adba6e423ba079ecc3d1cc9df7~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="copyable">var myapp = &#123;&#125;; // 创建这个应用对象

myapp.Model = function() &#123;
    var val = 0; // 需要操作的数据

    /* 操作数据的方法 */
    this.add = function(v) &#123;
        if (val < 100) val += v;
    &#125;;

    this.sub = function(v) &#123;
        if (val > 0) val -= v;
    &#125;;

    this.getVal = function() &#123;
        return val;
    &#125;;
&#125;;复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">View</h3>
<p>View作为视图层，主要负责数据的展示。</p>
<pre><code class="copyable">myapp.View = function() &#123;

    /* 视图元素 */
    var $num = $('#num'),
        $incBtn = $('#increase'),
        $decBtn = $('#decrease');

    /* 渲染数据 */
    this.render = function(model) &#123;
        $num.text(model.getVal() + 'rmb');
    &#125;;
&#125;;复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在通过Model&View完成了数据从模型层到视图层的逻辑。但对于一个应用程序，这远远是不够的，我们还需要响应用户的操作、同步更新View和Model。于是，在MVC中引入了控制器controller，让它来定义用户界面对用户输入的响应方式，它连接模型和视图，用于控制应用程序的流程，处理用户的行为和数据上的改变。</p>
<h2 data-id="heading-7">MVC</h2>
<blockquote>
<p>那时计算机世界天地混沌，浑然一体，然后出现了一个创世者，将现实世界抽象出模型形成model，将人机交互从应用逻辑中分离形成view，然后就有了空气、水、鸡啊、蛋什么的。<br>
——《前端MVC变形记》</p>
</blockquote>
<p>上个世纪70年代，<a href="https://link.juejin.cn/?target=http%3A%2F%2Fbaike.baidu.com%2Flink%3Furl%3Dux_43rkE1Ythy0RI6WZIB6NZpSbJYxOSzVk1W7LItMteveUBPdAgoegLc2j8zA8XRqZPS0tTwMAKtAXhZ9jTClBFGzj4GV2zstDqWP7kFC3" title="https://link.juejin.cn/?target=http%3A%2F%2Fbaike.baidu.com%2Flink%3Furl%3Dux_43rkE1Ythy0RI6WZIB6NZpSbJYxOSzVk1W7LItMteveUBPdAgoegLc2j8zA8XRqZPS0tTwMAKtAXhZ9jTClBFGzj4GV2zstDqWP7kFC3" target="_blank">美国施乐帕克研究中心</a>，就是那个发明图形用户界面(GUI)的公司，开发了<a href="https://link.juejin.cn/?target=http%3A%2F%2Fbaike.baidu.com%2Fitem%2FSmalltalk%2F1379989" title="https://link.juejin.cn/?target=http%3A%2F%2Fbaike.baidu.com%2Fitem%2FSmalltalk%2F1379989" target="_blank">Smalltalk</a>编程语言，并开始用它编写图形界面的应用程序。</p>
<p>到了Smalltalk-80这个版本的时候，一位叫Trygve Reenskaug的工程师为Smalltalk设计了MVC（Model-View-Controller）这种架构模式，极大地降低了GUI应用程序的管理难度，而后被大量用于构建桌面和服务器端应用程序。</p>
<p><img src="https://juejin.cn/post/6991766626618048542" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6daaefbae2014b3aba75f85daee2470f~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
如图，实线代表方法调用，虚线代表事件通知。</p>
<p>MVC允许在不改变视图的情况下改变视图对用户输入的响应方式，用户对View的操作交给了Controller处理，在Controller中响应View的事件调用Model的接口对数据进行操作，一旦Model发生变化便通知相关视图进行更新。</p>
<h3 data-id="heading-8">Model</h3>
<p>Model层用来存储业务的数据，一旦数据发生变化，模型将通知有关的视图。</p>
<pre><code class="copyable">myapp.Model = function() &#123;
    var val = 0;

    this.add = function(v) &#123;
        if (val < 100) val += v;
    &#125;;

    this.sub = function(v) &#123;
        if (val > 0) val -= v;
    &#125;;

    this.getVal = function() &#123;
        return val;
    &#125;;

    ／* 观察者模式 *／
    var self = this, 
        views = [];

    this.register = function(view) &#123;
        views.push(view);
    &#125;;

    this.notify = function() &#123;
        for(var i = 0; i < views.length; i++) &#123;
            views[i].render(self);
        &#125;
    &#125;;
&#125;;复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>Model和View之间使用了观察者模式，View事先在此Model上注册，进而观察Model，以便更新在Model上发生改变的数据。</p>
<h3 data-id="heading-9">View</h3>
<p>view和controller之间使用了策略模式，这里View引入了Controller的实例来实现特定的响应策略，比如这个栗子中按钮的 <code>click</code> 事件：</p>
<pre><code class="copyable">myapp.View = function(controller) &#123;
    var $num = $('#num'),
        $incBtn = $('#increase'),
        $decBtn = $('#decrease');

    this.render = function(model) &#123;
        $num.text(model.getVal() + 'rmb');
    &#125;;

    /*  绑定事件  */
    $incBtn.click(controller.increase);
    $decBtn.click(controller.decrease);
&#125;;复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>如果要实现不同的响应的策略只要用不同的Controller实例替换即可。</p>
<h3 data-id="heading-10">Controller</h3>
<p>控制器是模型和视图之间的纽带，MVC将响应机制封装在controller对象中，当用户和你的应用产生交互时，控制器中的事件触发器就开始工作了。</p>
<pre><code class="copyable">myapp.Controller = function() &#123;
    var model = null,
        view = null;

    this.init = function() &#123;
        /* 初始化Model和View */
        model = new myapp.Model();
        view = new myapp.View(this);

        /* View向Model注册，当Model更新就会去通知View啦 */
        model.register(view);
        model.notify();
    &#125;;

    /* 让Model更新数值并通知View更新视图 */
    this.increase = function() &#123;
        model.add(1);
        model.notify();
    &#125;;

    this.decrease = function() &#123;
        model.sub(1);
        model.notify();
    &#125;;
&#125;;复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们实例化View并向对应的Model实例注册，当Model发生变化时就去通知View做更新，这里用到了观察者模式。</p>
<p>当我们执行应用的时候，使用Controller做初始化：</p>
<pre><code class="copyable">(function() &#123;
    var controller = new myapp.Controller();
    controller.init();
&#125;)();复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以明显感觉到，MVC模式的业务逻辑主要集中在Controller，而前端的View其实已经具备了独立处理用户事件的能力，当每个事件都流经Controller时，这层会变得<strong>十分臃肿</strong>。而且MVC中View和Controller一般是一一对应的，捆绑起来表示一个组件，视图与控制器间的过于紧密的连接让Controller的复用性成了问题，如果想多个View共用一个Controller该怎么办呢？这里有一个解决方案，使用MVP</p>
<p>原文链接：<a href="https://juejin.cn/post/6844904022978068487%5C" target="_blank" title="https://juejin.cn/post/6844904022978068487%5C">juejin.cn/post/684490…</a></p></div>  
</div>
            