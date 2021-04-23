
---
title: '爱奇艺RND框架技术探索——架构与实现'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45275dba82c2468da66936bb2237740d~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 21 Apr 2021 02:47:46 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45275dba82c2468da66936bb2237740d~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>前言</p>
<p>RND，全称React Node Desktop，起源于RN在爱奇艺PC端的实现，采用<strong>React JS framework +Node.js runtime + native UI engine</strong>架构，目标是成为最轻量的JS开发桌面应用的跨平台方案。之前我们还分享了一篇关于RND的Native API注入技术的文章****，大家可以参考。</p>
<p>目前RND已经在爱奇艺PC客户端大量应用，在最新的爱奇艺客户端中，除了播放视窗和窗口边框等部分采用C++开发外，其余频道页均是基于RND框架采用Java Script开发的，RND无缝地将Native部分与Java Script开发的UI模块融合到一起，用户从体验上无法感知哪部分是C++开发，哪部分是Java Script开发的。RND的应用有效降低了开发难度和成本，提高了开发效率，同时也为产品迭代提供了更加多样化的解决方案。</p>
<p>下面是RND在爱奇艺客户端上应用的几个场景：</p>
<ul>
<li><strong>基于RND的频道页：</strong></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45275dba82c2468da66936bb2237740d~tplv-k3u1fbpfcp-zoom-1.image" alt="640?wx_fmt=png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>融合Native播放器的RND页面：</strong></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/adde4628690a4446894c349e87e35883~tplv-k3u1fbpfcp-zoom-1.image" alt="640?wx_fmt=png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li><strong>播放器侧边栏信息区：</strong></li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/776705ab6a554ea6b7a344a2325aa10b~tplv-k3u1fbpfcp-zoom-1.image" alt="640?wx_fmt=png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>本文接下来将从<strong>技术选型</strong>、<strong>线程模型</strong>、<strong>JS运行时</strong>、<strong>Bridge</strong>、<strong>资源管理</strong>、<strong>调试支持</strong>等几个方面对RND的实现作一个简单的梳理，以期能够让大家对RND在Windows上的实现方案有一个较全面的了解。</p>
<p>技术选型与架构设计</p>
<p>RN最核心的部件当然是JavaScript引擎，毋庸置疑V8是RND的首选。对于UI部分的实现，在移动端，无论是安卓还是iOS，RN对接的都是原生的UI组件，熟悉Windows客户端的开发者都知道，由于一些众所周知的原因，现在基于Windows的互联网产品的UI几乎不会选择原生的UI控件，很多大厂都开发了自己的UI库。爱奇艺也有自己的UI渲染引擎——，Lyra是一套十分优秀的异步渲染引擎，目前支持Windows和MAC OS两个平台，RND所有的UI渲染都是以Lyra作为基础，并且RND还整合了Yoga布局系统来实现UI Component的flex布局计算。</p>
<p>在Native能力方面，因RND集成了Node运行时，这使得基于RND的JS开发者拥有了Node强大的Native基础能力，开发者可以按需引入Node模块来扩展应用的Native能力；本地缓存方面，RND采用了高性能的本地存储系统LevelDB，LevelDB是一款性能十分优秀的Nosql数据库，支持key/value形式的数据存储；在调试方面，RND除了支持Chrome外，还支持VSCode、Electron调试，方便开发者按自己的需求进行调试。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/facac2da520d476a9e34d1358844f4b7~tplv-k3u1fbpfcp-zoom-1.image" alt="640?wx_fmt=png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>RND架构图</p>
<p>RND的线程模型</p>
<p>RND采用了UI线程和JS线程的双线程模式，其中渲染命令和布局都是在UI线程中完成的，RN JS的代码则是执行在JS线程中。RNJS框架生成渲染命令后，通过注入的交互函数发送到UI线程中，UI线程收到命令进行解析，完成JS组件的创建、布局和渲染。</p>
<p>当在UI线程中存在复杂任务时，RND的渲染仍然能保证界面绘制的流畅度，这要归功于UI采用的异步渲染引擎——Lyra，Lyra执行的双线程渲染模式，UI线程会将paint消息发送到独立的render线程执行，避免UI线程上的耗时计算阻塞界面绘制，因此，RND有着非常出色的渲染能力。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8b669776c54042fca06a7a2eb361371f~tplv-k3u1fbpfcp-zoom-1.image" alt="640?wx_fmt=png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>RND线程模型</p>
<p>JS运行时的实现</p>
<p>在Windows平台上，RND采用V8作为JavaScript引擎。JS运行时是对JS运行环境的抽象描述：隔离了不同平台JS引擎的接口差异，为上层提供了统一的访问接口，并向JS引擎注入了必要的Native API以支持RN的运行。同时，JS运行时还对外暴露了ReactJS的事件监听接口和Native API注入框架。</p>
<hr>
<p>封装V8</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f7e99dc49a3646a18c6b18de173b7870~tplv-k3u1fbpfcp-zoom-1.image" alt="640?wx_fmt=png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>RND对JS运行时的抽象和封装</p>
<p>考虑到内存与性能开销，在同一进程中，所有RootView实例共享V8的同一个Isolate对象，而每一个RootView独立拥有一个V8的Context，保证其运行环境的隔离。因共享Isolate的原因，所有的RootView共享同一个JS执行线程。共享线程也可以有效降低线程竞争。开发者也可以改变这一策略，根据实际资源使用情况来决定Isolate的数量。</p>
<p>Snapshot助力加速启动过程</p>
<p>V8还有一个非常有用的特性为RND所用——Snapshot运行模式：Snapshot是将V8运行期某一时刻的运行快照转储到磁盘文件中，当程序再次启动时可以直接从存储好的快照直接恢复到当时的运行状态，这一特性可以有效帮助RND提升应用的启动速度。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2bb4c1de6a904108b2cea208dfb9ce31~tplv-k3u1fbpfcp-zoom-1.image" alt="640?wx_fmt=png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>使用snapshot启动速度加快近300ms</p>
<p><strong>整合Node运行时，引入Node生态</strong></p>
<p>因为开源项目Node同样使用了V8引擎，这样我们做很少的工作就可以将Node引入到RND中了。RN开发者不但具有了本地文件、网络等基础Native访问能力，而且还可以将Node的开发包集成到开发环境中来。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/766611a7ea3c422ca429b6661f504118~tplv-k3u1fbpfcp-zoom-1.image" alt="640?wx_fmt=png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>RND同时支持RN和node的modules</p>
<p>一个典型的例子，在RND中Web Socket接口就是由Node来支持的。在Chrome、DevTools的调试实现中都用到了Web Socket。</p>
<p><strong>Bridge实现</strong>****</p>
<p>Bridge的实现大概是RN原理介绍相关的文章中读者最关心的部分了，与RN移动版本的实现不同，因RND基于C开发，而V8亦是以C向Native提供接口的，因此在实现Bridge时，RND不需要额外处理异构语言交互的问题。</p>
<p>交互实现</p>
<p>单接口、异步交互的模式是RN实现Bridge的最大特点。RND对Bridge部分作了一些改良和扩充，对于UI以外的处理，RND将其从messageQueue中“拆了出来”，提供了直接的API来完成，比如timer、本地缓存访问、网络请求等Native模块。这些接口在Native端基本都是异步接口，因此不会造成阻塞，但在执行逻辑处立刻调用会加速并发能力，以便定时器更加精确或网络请求更早将请求发送出去。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6ab92c42bd1f4614ae4e04ddb6281b79~tplv-k3u1fbpfcp-zoom-1.image" alt="640?wx_fmt=png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Bridge实现</p>
<p><strong>Yoga布局</strong></p>
<p>Lyra系统目前并不支持Flexbox布局规范，因此RND并没有使用Lyra的布局系统，而是与RN一样采用了Facebook的Yoga布局系统，Yoga支持Flexbox规范，是一款非常优秀的跨平台布局系统。相较于之前的版本，Yoga优化了Dirty算法，只对发生位置或大小变化的相关控件进行Dirty，大大提高了绘制效率。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/82ab2a3a7e2b4dfdbcc0bea99a4307f7~tplv-k3u1fbpfcp-zoom-1.image" alt="640?wx_fmt=png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>RND应用界面布局</p>
<p>RootView内部的控件接受Yoga布局，其自身则与其他Lyraui控件接受Lyra的布局。</p>
<p>RND的资源管理与热更新</p>
<p>模块化资源管理</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0e8248c47734a10bddc1ca1d7871dd1~tplv-k3u1fbpfcp-zoom-1.image" alt="640?wx_fmt=png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>RND资源管理</p>
<p>每一个Module对应了一个资源配置（ResourceConfig），这个资源配置映射了一个资源配置管理对象，通过这个资源配置管理对象便可获取到当前要使用的资源类型和资源内容。</p>
<p>进行资源模块化，其实是Lyra ui本身的使用要求，因此，RND的资源模块化实际上是使用了Lyra ui的资源管理策略。</p>
<p>RND中，JS业务代码，图片文件都被视为资源，在发布版本中，都被打包到zip中，在开发模式下，是以文件形式存放在代码目录中的，为了统一组织不同模式下的资源加载，RND抽象了ResLoader对象，负责加载不同类型的资源，同时，ResLoader还会调用热更新模块进行资源zip包的升级。</p>
<p>图片资源自动加载机制</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c158550637b647c78b0aad910c9c8920~tplv-k3u1fbpfcp-zoom-1.image" alt="640?wx_fmt=png" loading="lazy" referrerpolicy="no-referrer">图片加载与显示</p>
<p>  </p>
<p>RND UI组件的图片资源有3种来源：网络、本地缓存和zip资源包，存放在zip资源包的图片资源一般都是较少更新的、较固定的图片资源。大部分图片是动态更新的，JS通过URL的形式来设置图片资源属性，RND根据URL的格式来区别图片来自网络还是zip包，来自网络的图片URL是一个http的URL，而zip包中的图片则是一个文件名的形式。因此RND很容易区分这两种图片来源，当判断是来自网络时，RND会首先检查是否存在缓存文件，如果存在则直接读取缓存图片。</p>
<p>可灵活配置的热更新</p>
<p>RootView在初始化时ResLoader会通过ConfigManager获取资源更新对象，调用UpdateResource函数进行资源更新，当资源有更新时便会直接加载新的资源包执行，如果不存在更新则加载默认的资源包。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67030ea22f6c46ca96b61f3b88c1e322~tplv-k3u1fbpfcp-zoom-1.image" alt="640?wx_fmt=png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>RootView资源热更新</p>
<p>  </p>
<p>RND支持两种资源更新策略，一种直接通过URL携带请求参数的方式请求升级资源包，另一种则是先拉取一个升级策略文件，再通过读取升级策略进行升级，可以通过ConfigManager由宿主程序指定。</p>
<p>  </p>
<p>用户也可以实现自己的资源更新策略，在配置对象中指定，RND会优先使用自定义更新策略来更新资源。</p>
<p>调试支持</p>
<p>工欲善其事必先利其器，在调试方面，我们投入了大量的精力来完善增强RND的工具链，一方面我们比RN有更丰富的调试工具；另一方面，我们创新性地整合了调试与目标应用的JS运行时，调试环境就是运行环境，所有与Native的调用都是真实调用，而不是委托给Web Socket实现的“伪调用”，这完美解决了在调试模式下Native接口同步调用的问题，也提高了调试的便利性，开发者可以在JS代码中同步跟踪Native接口调用。</p>
<p>多样化调试支持</p>
<p>除了Chrome外，RND还整合了Electron、VSCode等调试工具，开发者可以按照不同的需求或喜好可以选择不同的调试工具，RND推荐使用Electron或VSCode来调试，Electron完全支持Chrome所有的调试和性能分析功能，而VSCode则是JS开发者首选的IDE，在开发中进行调试、热更新都非常的方便。用户可以通过调试配置文件选择使用哪一种调试工具作为默认调试器。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71af04005a7a46c4842ecb67bde35388~tplv-k3u1fbpfcp-zoom-1.image" alt="640?wx_fmt=png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>RND调试工具链</p>
<p><strong>Native接口同步调试支持</strong></p>
<hr>
<p>在Chrome调试模式下，RN JS并不是运行在自身的JS引擎中，而是被运行在Chrome的JS引擎中，对Native Api的调用也是通过Web Socket来代理实现的，因此，在这种场景下，如果想要执行同步Native Api的调用是无法实现的。在RND中，因RN JS需要同步获取宿主窗口位置大小等信息，Native提供了对应的同步接口，在调试模式下对这类同步接口的调试就无法实现了。</p>
<p>RND在Electron和VSCode调试模式中将JS运行时整合到了一起，让RN JS与宿主应用的Native部分运行在同一个进程中，这样就实现了Native API的同步调用，调试模式和运行模式的交互方式保持了一致。</p>
<p>调试效果图样</p>
<ul>
<li>通过<strong>DevTools</strong>查看页面布局：</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff896d2a7a7b4879803ec937db1fe3b8~tplv-k3u1fbpfcp-zoom-1.image" alt="640?wx_fmt=png" loading="lazy" referrerpolicy="no-referrer"></p>
<p> </p>
<ul>
<li>通过<strong>VSCode</strong>进行调试：</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/642cd41b5cb3483a929eeec81e3855ad~tplv-k3u1fbpfcp-zoom-1.image" alt="640?wx_fmt=png" loading="lazy" referrerpolicy="no-referrer"></p>
<p> </p>
<ul>
<li>通过<strong>Chrome</strong>进行调试：</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9b87667ffe24944ba03fdbfefc5974f~tplv-k3u1fbpfcp-zoom-1.image" alt="640?wx_fmt=png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>小结</p>
<p><strong>本文着重从Native框架的角度介绍了RND的技术选型和关键模块的实现原理</strong>，关于RN JS框架部分本文并未提及，后续会有专门的一篇文章《爱奇艺RND框架之JS Framework解析》来介绍，敬请关注。由于篇幅关系，RND的动画系统、性能分析系统等很多技术文中并未涉及，希望后续有时间能与大家一起分享。</p>
<p>RND在爱奇艺客户端的成功实践表明，RN同样适用于以运营内容为主的、迭代周期密集的互联网桌面应用，JS非常适合UI和业务逻辑的快速开发。随着各大JS引擎性能不断的优化，很多大厂都推出了基于JS语言的轻量级高性能App应用框架，<strong>可以预测在不久的将来，以内容运营为主的桌面产品上，JS很快会成为最受开发者欢迎的语言之一</strong>。</p>
<p> </p>
<p>end</p>
<p><strong>也许你还想看</strong></p>
<h2 data-id="heading-0"></h2>
<h2 data-id="heading-1"></h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16efe8fcc0954ea5a62b85c134d60215~tplv-k3u1fbpfcp-zoom-1.image" alt="640?wx_fmt=gif" loading="lazy" referrerpolicy="no-referrer"></p>
<p>扫一扫下方二维码，更多精彩内容陪伴你！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7515b8cef80f4cd58b20bf270202acc7~tplv-k3u1fbpfcp-zoom-1.image" alt="640?wx_fmt=other" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>爱奇艺技术产品团队</strong></p>
<p>简单想，简单做</p>
<p>\</p></div>  
</div>
            