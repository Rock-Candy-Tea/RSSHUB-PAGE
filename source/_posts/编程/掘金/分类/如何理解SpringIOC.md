
---
title: '如何理解SpringIOC'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2806292802a4c5886d7f8b89879f6a8~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 30 May 2021 19:41:41 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2806292802a4c5886d7f8b89879f6a8~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:25px;margin-bottom:5px;border-left:5px solid #773098&#125;.markdown-body h1,.markdown-body h2&#123;display:inline-block;font-weight:700;padding-left:10px&#125;.markdown-body h2&#123;font-size:18px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:16px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;border-radius:6px;display:block;margin:20px auto;object-fit:contain;box-shadow:2px 4px 7px #999&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-size:12px;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#d89cf6&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>SpringIOC 是 Spring Core 最核心的部分，要了解控制反转 (Inversion of Control)，我觉得有必要先了解软件设计的一个重要思想：依赖倒置原则。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2806292802a4c5886d7f8b89879f6a8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>SpringIOC 是 Spring Core 最核心的部分，要了解控制反转 (Inversion of Control)，我觉得有必要先了解软件设计的一个重要思想：依赖倒置原则。</p>
<p>1、高层模块不应该依赖底层模块，二者都应该依赖抽象<br>
2、抽象不应该依赖细节，细节应该依赖抽象。<br>
3、依赖倒置的中心思想是面向接口编程。<br>
4、依赖倒置原则是基于这样的设计理念：相对于细节的多变性，抽象的东西要稳定的多。以抽象为基础搭建的架构比以细节为基础搭建的架构要稳定的多。<br>
5、使用接口或抽象类的目的是指定好规范，而不涉及任何具体操作，展现细节的任务交给他们的实现类来完成。</p>
<h2 data-id="heading-0">依赖注入 DI</h2>
<p>现在假设我们需要设计一个行李箱，行李箱依赖于箱体，箱体依赖于底盘，底盘依赖于轮子。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/78c1353b8ad14c42ae307b1bc32748f6~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在假设轮子需要按尺寸需求更改，那么底盘也得改，箱体也得改，行李箱也要改。代码如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/496ac0a61e614c1a92cd97e33d4063fd~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>现在如果需要把轮子得大小改为动态可调整的，那么上层代码也得跟着变，由此我们可以看到，仅仅是为了修改轮子的构造函数，这种设计却需要修改整个上层所有类的构造函数！在软件工程中，这样的设计几乎是不可维护的——在实际工程项目中，有的类可能会是几千个类的底层，如果每次修改这个类，我们都要修改所有以它作为依赖的类，那软件的维护成本就太高了，这就是典型的上层建筑依赖下层建筑。</p>
<p>所以我们需要进行控制反转（IoC），及上层控制下层，而不是下层控制着上层。我们用依赖注入（Dependency Injection）这种方式来实现控制反转。所谓依赖注入，就是把底层类作为参数传入上层类，实现上层类对下层类的控制。这里我们用<strong>构造方法传递的依赖注入方式</strong> 重写各个类的构造函数：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7af63d7d01024beb86a0f7e119cd9039~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>依赖注入是如何解决这个问题的呢？我们可以先设计行李箱箱，根据行李箱设计箱体，根据箱体设计底盘，根据底盘设计轮子，如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7926654d0eb2488a89acf2ef77e9be27~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>所以，依赖注入即把底层类作为参数传递给上层类，实现上层对下层的控制。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/404ce8fae4c44f5d8e4a91e3aed79d9e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样即实现了底层类的更改不会影响到上层类的修改，增加了代码的可维护性。 这里我们是采用的构造函数传入的方式进行的依赖注入。其实还有另外三种方法：Setter 传递和接口传递和注解的方式。这里就不多讲了，核心思路都是一样的，都是为了实现控制反转。</p>
<h2 data-id="heading-1">IOC 与 DI、DL 的关系</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a13b5743b54c423d962fee9bca82027a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>EJB 即使用 DL 来实现的 IOC，DI 是当今 IOC 的主流实现。 DI 提供了 Setter 注入、接口注入、注解注入、构造器注入等多种注入方式。依赖倒置原则和 IOC 的关系是怎样的呢？</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fcfdc04503834d109c182304da8ce607~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>依赖倒置原则、IOC、DI、以及 spring IOC 容器，这四者的关系就是：依赖倒置原则上是一种思想，它主要含义是高层模块，不应该依赖于低层模块，两者都应该依赖其抽象。正是依赖倒置原则的指导，才有了 IOC 控制反转的思路，需要怎么实现这个思路呢？就离不开依赖注入之类的支撑，Spring 等框架，基于 IOC 才提出了容器的概念。对于 IOC 来说。最重要的就是容器把容器管理的 Bean 的生命周期进行控制依赖注入，那什么是控制反转容器 IOC container 呢？其实就是承载对象的容器，便于组装对象，避免在各处使用 new 来创建类，并且可以做到统一维护。</p>
<p>如果我们一步一步去 new 的话，就会是图中的上面的情况，需要根据构造函数一步一步来注入：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/737e1871b6d14c97af6e647febc64a7f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>而 ICO 容器注入的过程如图中下面的部分所示，先查找对象的依赖关系，然后自底向上进行注入。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5710c13a6c8f4e578f32ad1b8906aa31~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            