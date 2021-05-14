
---
title: 'android进阶篇04、MVC、MVP、MVVM架构简析'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=6923'
author: 掘金
comments: false
date: Tue, 11 May 2021 00:54:23 GMT
thumbnail: 'https://picsum.photos/400/300?random=6923'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">一、设计模式六大原则</h2>
<p>在讲解架构设计之前，先讲解一下设计模式的六大原则，虽然是设计模式的六大原则，但我们在进行架构设计的时候也应该尽量遵循这些原则；</p>
<p>六大原则如果仅看概念会比较抽象，而且也不容易理解。这里我们举一个生活中的例子：汽车是基类；轿车是汽车的一个子类；汽车都是在路上跑的，所以我们把公路抽象成一个接口，让汽车实现此接口；汽车都可以用来载人，所以我们把人抽象成一个接口，让汽车实现此接口；汽车也可以载鸡鸭鱼，不过需要通过人来携带上去，因此把鸡鸭鱼放入人的接口中；</p>
<p>下面对每一个原则给处官方解释，然后结合汽车这个例子去理解；</p>
<h3 data-id="heading-1">1、单一职责原则</h3>
<p>就一个类而言，应该仅有一个引起它变化的原因；</p>
<p>这里我们设计的汽车类就符合单一职责，它的单一职责就是在路上跑；</p>
<h3 data-id="heading-2">2、开放封闭原则</h3>
<p>类、模块、函数应该是可以扩展的，但不可修改；</p>
<p>这里我们对汽车就是采取的开放封闭原则，轿车通过继承汽车扩展功能，并且没有修改基类汽车；</p>
<h3 data-id="heading-3">3、依赖倒置原则</h3>
<p>高层模块不应依赖底层模块，两者都应该依赖于抽象，抽象不应该依赖于细节，细节应该依赖于抽象；</p>
<p>本例中我们的汽车类是实现了公路接口，也就是依赖于抽象；公路接口就是一个抽象；</p>
<h3 data-id="heading-4">4、接口隔离原则</h3>
<p>一个类对另一个类的依赖应该建立在最小的接口上；</p>
<p>我们这里汽车实现了公路和人两个接口，每个接口都负责特有的方面，即接口隔离；</p>
<h3 data-id="heading-5">5、里氏替换原则</h3>
<p>所有引用基类的地方必须能透明的使用其子类的对象；</p>
<p>本例中所有需要汽车的地方，传入轿车也没有问题；但是需要轿车的地方就不能传入汽车；</p>
<h3 data-id="heading-6">6、迪米特原则</h3>
<p>一个软件实体应当尽可能少的与其他实体发生作用；</p>
<p>本例中我们的汽车可以载鸡鸭鱼，但是鸡鸭鱼需要通过人来携带，因此我们并没有为鸡鸭鱼单独抽象出接口，而是将其放入人的接口中，汽车也就尽可能少的与其他实体发生作用；</p>
<h2 data-id="heading-7">二、架构介绍</h2>
<p>如果我们在进行开发时不使用架构思想，那么所有的代码会一股脑的放在activity或者fragment中，业务需求复杂多变，并且需要经常去修改；数据、视图、逻辑都放在一起会显得混乱，维护起来及其困难，出现错误很难排查；介绍三大架构之前先介绍一下几个概念；</p>
<p>数据model：数据包括数据本身以及对数据操作的逻辑，数据本身独有的操作逻辑，不牵扯视图；</p>
<p>视图view：不同的架构模式view代表的部分也不相同，下面单独介绍；</p>
<p>控制逻辑：不同的架构模式控制部分也不相同；</p>
<h3 data-id="heading-8">1、MVC</h3>
<p>mvc模式下的view主要是指xml文件和activity中与视图相关联的部分，例如findViewById等操作；而mvc模式中的c是指controller，其实也就是activity或者fragment，在activity中进行逻辑的控制，让数据和视图进行交互；</p>
<p>mvc模式抽离了model层，让activity减轻了一点负担，但是仍然很复杂，因为需要在activity中进行逻辑控制，并且数据和视图的交互也需要放在activity中；</p>
<h3 data-id="heading-9">2、MVP</h3>
<p>mvp模式中的v代表视图层，主要包括xml文件和activity，在activity中进行与视图相关的操作；</p>
<p>mvp模式中的p代表presenter控制层，主要进行逻辑的控制，让数据层和视图层进行交互；既然是数据和视图进行交互，那么presenter中就要持有数据和视图，数据好说，直接持有数据类的对象即可；视图如何持有？一般的方式是定义视图IView接口，在接口中定义改变视图需要的方法，让activity实现接口，然后在activity中去实现方法具体的逻辑；这样在presenter中持有接口对象，然后在构造函数中给接口对象赋值，此时我们在activity中实例化presenter时就可以将自身传进去，因此自身实现了IView接口；这样我们就可以在presenter中操作接口中的方法，也就实现了视图与数据交互；</p>
<p>mvp的优点是将控制部分分离到presenter中，将数据和视图彻底分离；缺点就是需要定义较多的接口，而且接口中添加或者修改了方法，需要去多个地方修改；</p>
<h3 data-id="heading-10">3、MVVM</h3>
<p>我怕理解的MVVM分两种情况，一种是使用dataBinding；一种是不使用dataBinding；</p>
<h4 data-id="heading-11">不使用dataBinding：</h4>
<p>如下所示，UI控制层可以表示Activity、Fragment；ViewModel层就可以使用jetpack中的ViewModel实现，里面一般定义多个待观察的LiveData；仓库层用于判断是从本地数据源存取数据还是从网络数据源存取数据；如果是从本地数据源可以使用SP、数据库等容器；如果是从网络数据源，我们可以借助Retrofit、Okhttp等三方框架实现；</p>
<pre><code class="hljs language-mermaid" lang="mermaid">graph TD
UI控制层 --> ViewModel层
ViewModel层 --> 仓库层
仓库层 --> 本地数据源model
仓库层 --> 网络数据源model
本地数据源model --> 持久化文件
网络数据源model --> WebService
</code></pre>
<h4 data-id="heading-12">使用dataBinding：</h4>
<p>使用dataBinding的情况就是将视图xml变成dataBinding实现的视图，将视图与数据关联，自动更新；</p>
<p>mvvm模式下m仍然是代表model数据层；v代表view视图层，主要包括xml文件和activity；vm代表viewmodel层，一般在viewmodel中定义dabaBinding中的可观察容器，然后逻辑中修改这些容器，然后在xml视图中引入viewmodel的对象，然后在具体的视图中观察viewmodel中的可观察容器，这样在viewModel中对容器进行了修改，则在视图中会同步更新；</p>
<p>mvvm实现了数据、视图和逻辑的分离，并且不产生冗余接口；修改起来方便，数据和视图相互观察；缺点就是需要在xml文件中写少量代码。</p></div>  
</div>
            