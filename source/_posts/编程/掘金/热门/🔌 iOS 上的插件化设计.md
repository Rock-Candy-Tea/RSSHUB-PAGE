
---
title: '🔌 iOS 上的插件化设计'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/126a1c33edd54d2795896026c9e2aeb3~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 08:54:28 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/126a1c33edd54d2795896026c9e2aeb3~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>iOS 社区这两年底层向的文章比较多， 关于 <strong>工程化</strong> 相关讨论会少一点，底层并非不好，只是作为屠龙刀的角色，需要在特定场景去发挥出威力。</p>
<p>对于广大 iOS 开发者，工程和业务却是每天需要打交道的地方，拆分业务也属于必不可少的事项，插件化作为解耦手段之一，对于每个公司和团队，方案可能都略有不同。</p>
<p>业界关于此类的文章也较少，经过搜索只发现了一篇 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.infoq.cn%2Farticle%2Fejkw6sz5qouuhxgag5vy" target="_blank" rel="nofollow noopener noreferrer" title="https://www.infoq.cn/article/ejkw6sz5qouuhxgag5vy" ref="nofollow noopener noreferrer">《优酷 iOS 插件化页面架构方案》</a> ，现结合自己经验理解在此抛砖引玉。</p>
<h2 data-id="heading-1">效果演示</h2>
<p>目前暂不提供完整方案代码，后续可考虑把简单 Demo 放出来。</p>
<p>文章应该把思路和关键实现说得比较清楚，要自己实现应该也不太难。</p>
<p>虽然不能 show code ，但有图有真相，可以先看看插件化的实现效果。</p>
<h3 data-id="heading-2">增加插件</h3>
<p>直接编写好对应的 plugin.h/plugin.m ，就能无侵入地增加一个新插件和进行逻辑交互：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/126a1c33edd54d2795896026c9e2aeb3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-3">删除插件</h3>
<p>将要插件的实现文件直接删掉，就能无耦合的拔除插件：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f5770e530c84f4085605666b9511333~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">插件化是什么</h2>
<p>要理解插件化，就要先理解  <strong>插件</strong> 的概念。</p>
<p>稍微区别于 <em>组件</em>，插件的粒度会更小一些，如果说每一个组件是工程中的某一个模块，那每一个插件就可以是业务模块中的子功能。</p>
<p>作为插件来说，它的特点一定是 <strong>可拔插</strong> 的。</p>
<p>具体的表现就是，插件的引入和删除都是对现有业务无侵入的，或者微小侵入的，<strong>不会对现有业务造成影响</strong>。</p>
<p>插件的拆分上要满足 <strong>单一职责</strong>，通过各个不同的插件，来提供和完成不同的功能。</p>
<p>在命名上，可能有的叫 Widget，有的叫 Plugin 等等，这里暂把它称作 Plugin 。</p>
<p><strong>插件化</strong> 就是通过不同  <strong>插件</strong> 组织业务模块：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/01a5ef6a28e84e89aca3bc91cb1240aa~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210424100619149" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">插件化的由来</h2>
<p>关于为什么要做插件化，具体下来应该有 2 个问题：</p>
<p>首先是为什么要做 <strong>业务拆分</strong> 的问题 ，然后在此基础上，才是为什么业务拆分需要  <strong>插件化</strong> 的问题。</p>
<p>一个业务本来不需要拆分，那么也没有去做插件化的必要了，不用去做过度设计。</p>
<h4 data-id="heading-6">为什么要做业务拆分</h4>
<p>关于为什么要做业务拆分，我目前的理解是：<strong>业务复杂不是问题，业务复杂造成难以维护的结果才是问题</strong>。</p>
<p>对于一个复杂的业务，设计模式和架构的作用是去将它 <strong>有序</strong> 的组织起来，更好管理，<strong>脱离无序混乱</strong> 的组织状态，却不会减少项目本身的功能和交互。</p>
<p>想要解决问题，做到可维护性高，那么就要做到：</p>
<ul>
<li>减少依赖，互相间关系越简单越好</li>
<li>分工明确，便于专注某一功能的开发和测试</li>
<li>代码功能便于复用</li>
</ul>
<p>根据我有限的开发经验来说，首先需要整理依赖，先垂直上下分层，公用功能聚合下沉，业务逻辑上移。然后是去除横向依赖，这个过程又会有一次功能的的聚合与拆分。而各种设计模式和架构就是去帮助我们做到这些事情。</p>
<h4 data-id="heading-7">为什么业务拆分要用到插件化</h4>
<p>记得刚入行时，有不少与 <strong>UIViewController 瘦身</strong> 相关的讨论，比较有印象的是这篇 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.devtang.com%2F2015%2F11%2F02%2Fmvc-and-mvvm%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.devtang.com/2015/11/02/mvc-and-mvvm/" ref="nofollow noopener noreferrer">《被误解的 MVC 和被神化的 MVVM》</a> 。</p>
<p>除了有使用 Controller 分类 / 独立 UITablieView 的 DataSource 等手段，常见的手段就是用各种 <strong>Manager</strong> 专门管理某一个功能逻辑。随着项目逐渐迭代和复杂，尽管用了拆分手段，代码同样会越来越难维护。</p>
<p>最大问题往往还是 <strong>耦合</strong>，因为依赖太多，其它地方引入也会粘连到不必须的代码，本无复杂的功能，却需要继承很多不是必须要使用的代码，让项目的维护变困难。</p>
<p>常见的一种情况是 <strong>多重继承</strong> 带来的依赖和层级问题：开发人员想要复用功能，一般就会采用继承，当继承层级变多，对父类的修改又会影响子类及相关类，功能将出现问题。如果不想影响过多，就会直接 <strong>复制粘贴</strong> ，成为一个 CV 工程师 ( 不用问，问就是我也这么干过😂 )。</p>
<p>插件化要达到目的，就是在拆分模块业务的基础上，同时解决 <strong>耦合问题</strong> ，利用组合插件的方式管理业务模块。</p>
<h2 data-id="heading-8">插件化的设计思路</h2>
<p>下面开始进入插件化设计的实践部分。</p>
<h3 data-id="heading-9">插件化围绕某个业务对象进行</h3>
<p>插件逻辑都是围绕某个具体业务做拆分。</p>
<p>进行插件化改造，会有一个业务对象当作是 <strong>Container (容器)</strong>，是整个插件化业务的入口和中心。</p>
<p>如果是有组件化经验的同学，可以把 <strong>Container</strong> 当作在组件化中壳工程的角色。</p>
<p>插件化的工作目的，就是将业务进行拆分和组织，就如把集团拆分成事业群，各自独立管理自己的业务进行发展，同时也能协作。</p>
<p>在 iOS 日常工作中，Container 对象的类型基本都属于 UIViewController 或者 UIView，因为很多复杂的交互与逻辑都会写在它们当中（尤其是 UIViewController ），但是 <strong>并不代表 Container 就被限定在 UIViewController/UIView 二者的类型当中</strong>，其它的对象类型和业务也同样可以运用插件化的思想。</p>
<h3 data-id="heading-10">插件化机制的整体结构</h3>
<p>先说明整体的结构关系，来看看是如何利用插件把代码组织起来的：</p>
<ul>
<li>
<p>箭头从 A ->B，表示 A 被 B 引入依赖。</p>
</li>
<li>
<p>实线条，表示有物理文件的引入依赖。</p>
</li>
<li>
<p>虚线条，表示没有物理文件引入，但会使用到。</p>
</li>
<li>
<p>圆角矩形，代表实例对象</p>
</li>
<li>
<p>椭圆形，代表协议</p>
<p>结构关系如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f478bb8bdad34ca888036d579afd867a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<p>这里对有 5 个地方进行说明：</p>
<ul>
<li><strong>ContainnerProtocol</strong> ，作为容器对外提供的接口，它没有依赖其它地方，被 Container 和  ContainnerProtocol 所依赖。</li>
<li><strong>Container</strong> ，作为插件化的业务对象，Container 对象要实现 ContainnerProtocol 。</li>
<li><strong>PluginProtocol</strong> ，定义插件通用的方法，比如生命周期和注册事件等方法。</li>
<li><strong>PluginManager</strong>，作为插件管理器来对插件进行加载和管理，将具体的插件与 Container 连接起来。</li>
<li>各种 <strong>业务 Plugin</strong>，也就是写业务代码的地方。如果把虚线去掉，就会发现 <strong>业务 Plugin 是没有被其它地方依赖</strong> 的，业务方对于业务插件的迭代修改/扩展/删除都是非常简单的。</li>
</ul>
<h3 data-id="heading-11">插件化问题的难点 - 交叉依赖</h3>
<p>设计真正走到实施阶段，动作往往会变形。</p>
<p>前面有提到，我们的设想是通过 <strong>组装</strong> 的方式，直接将不同的插件合成一个模块，插件互相之间应该要没有依赖。</p>
<p>日常中多数的依赖问题都是依赖实例，根据 <strong>面向接口编程</strong> 的原则，在 OC 中常常利用协议来进行调用，达到 <strong>去除实体依赖</strong>  目的。</p>
<p>然而使用抽象协议代替实例后，仍会存在问题：</p>
<blockquote>
<p>用协议代替实例时，没有依赖实体对象，<strong>替换</strong> 的确会更加容易，但业务进行删除协议时，使用到协议的地方都要去找出并进行删改，也会带来不少成本。当我们要移除某一个插件，在关联方中删除它的工作量也是客观存在的。</p>
</blockquote>
<p>将实例改成利用协议来做逻辑，本质上还是要依赖于某个抽象，最后也无法避免下面的情况：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b0496aa500748ce966715dfdbd51dab~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>造成此类情况的原因很多，横向依赖不知不觉就产生了，或是因为没有一定的规约，或是因为业务开发执行问题。</p>
<p>而作为一个好用的插件来说，必须要做到 <strong>热拔插</strong> 的能力：</p>
<blockquote>
<p>要用的时候插电⚡️为我们提供功能，不用的时候直接拔走❌，增加/删除一个插件都不会对现行业务产生影响。</p>
</blockquote>
<p>因此对于插件化来说，首要做的就是 2  件事：</p>
<ul>
<li>插 - 无侵入增加业务插件</li>
<li>拔 - 无痛的删除业务插件（去除业务插件间交互的横向依赖）</li>
</ul>
<p>简单的说，我们要将上面搅成一团的混乱线缆拆开，使其变成有序的状态：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7058808f2b05426e89a9cae8498cab52~tplv-k3u1fbpfcp-zoom-1.image" alt="image-20210618223349433" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-12">插件注册</h3>
<p>对于无侵入增加业务插件，主要在插件注册生成时做文章。</p>
<p>插件注册通过 3 步顺序来进行介绍：</p>
<ol>
<li>PluginManager 如何与 Container 建立关联</li>
<li>PluginManager 如何对 Plugin 进行注册加载</li>
<li>如何增加一个新的业务 Plugin</li>
</ol>
<h5 data-id="heading-13">PluginManager 如何与 Container/Plugin 建立关联</h5>
<p>站在 <code>Container</code> / <code>PluginManager</code> /<code>业务Plugin</code>  3 个层面上看，插件化整体的启动与注册流程如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73a8f6eadac349039a0cc8d75ebdc786~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>整个流程里，PluginManager 和 业务 Plugin 都对 Container 对象做了持有，其实持有 Container 对象也不是必须的，只是日常往往会用到 Container 的实例或者方法，例如拆解 UIViewController 业务，业务 Plugin 会用到如 UIViewController.view 进行布局等。如果用不到，不持有也是可以的，实际当中可以灵活运用。</p>
<h5 data-id="heading-14">业务 Plugin 如何做到无侵入的注册加载</h5>
<p>前面说到了，增加 Plugin 最好要做到对业务无侵入。</p>
<p>PluginManager 在进行 Plugin 实例化时，没有直接引入业务 Plugin 相关的头文件，主要用到了 一个关键的手段：</p>
<blockquote>
<p>利用 Plist 文件来生成 Plugin 。</p>
</blockquote>
<p>在 PluginManager 注册加载业务 Plugin 的流程如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/797f0cc86f8d49acb4afe0d34d20337e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>业务 Plugin 生成的主要逻辑：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/895db8d203aa4f879689dcc13e2608f0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-15">如何增加新的业务插件</h5>
<p>要增加一个新的业务 Plugin 很简单，只需要 2 个步骤：</p>
<ol>
<li>实现业务 Plugin ( XXPlugin.h / XXPlugin.m )</li>
<li>Plist 新增一个 Plugin 对应的字典</li>
</ol>
<h6 data-id="heading-16">实现业务 Plugin</h6>
<p>在上面 <code>PluginManager</code>  的生成 plguin 代码中，声明的  plugin 是一个实现了 <code>IHZGameBasePlugin</code> 协议的对象，新增的业务 plugin 都需要去实现 <code>PluginProtocol</code>。</p>
<p>另外生成 plugin 利用到了  <code>BasePlugin</code> 中统一的类方法去创建实例对象，新增的业务 plugin 都需要继承 <code>BasePlugin</code>。</p>
<p>因此，实现业务 Plugin 要注意 2 点：</p>
<ul>
<li>新 Plugin 要实现统一遵守的 <code>PluginProtocol</code></li>
<li>新 Plugin 需要继承 BasePlugin</li>
</ul>
<p>一个新增业务 Plugin 的简单实现的示例：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c84f15c6a394b828a7013f0fadc3891~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h6 data-id="heading-17">Plist 文件里新增 Plugin 字典</h6>
<p>添加完 Plugin 的 <code>.h</code> 和 <code>.m</code> 文件，再去 Plist 文件的数组中，根据插件信息增加一个字典对象：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9392b4d7eb1b47febadcf89d7ba82fdf~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>示例中使用的是 Plist 文件，主要考虑在 Xcode 里可以有比较好的格式显示，更直观。</p>
<p>实际上也可以使用 json 或者另外方式，适合自己的方式才是最好的。</p>
<p>至此也就解决了插件化的第一个问题：<strong>无侵入增加业务插件</strong> 。</p>
<h3 data-id="heading-18">插件间的通讯 - 解决插件间横向依赖</h3>
<p>上面有说到使用协议代替实例，却仍旧做不到 <strong>无痛删除</strong> ，究其原因还是 <strong>业务上发生了耦合</strong> ，当调用代码被散落在各处，去除时也需要一个一个地找到。</p>
<p><strong>依赖抽象也是依赖</strong>，如果依赖的协议功能被删除，那么手动去删除关联代码也是不可避免的工作。</p>
<p>现在来看，利用 <strong>事件机制</strong> 能比较好地做到解耦工作，使用事件机制有 2 个明显的好处：</p>
<ul>
<li>解决耦合，插件之间也不用互相关心。例如插件  A 要触发插件 B 的逻辑，可以通过事件机制发出一个事件 EventX，而不是直接在 A 中调用 B 。</li>
<li>单独迭代，每个插件的业务方可以直接修改自己的逻辑。这样团队的协作也更有组织性，减少维护和沟通成本。</li>
</ul>
<h4 data-id="heading-19">事件机制的实现 - 观察者 or 订阅发布 ？</h4>
<p>关于实现事件机制，很容易想到使用  <strong>观察者</strong> 的设计模式，它有 3 个关键点：</p>
<ul>
<li>观察对象与观察者具有 <strong>一对多</strong> 的关系。</li>
<li>当观察对象发生改变，观察者（订阅者）就可以接收到改变。</li>
<li>观察者（订阅者）如何处理逻辑，观察对象无需关心，它们之间是松耦合的。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0cc19d11dbe34b91b382df615a3dc4c9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>然而在开发<code>复杂项目业务</code>时，往往还会使用 <strong>发布-订阅模式</strong> 的机制来做实现。</p>
<p>相对于观察者模式的实现，发布订阅模式多出一个 <strong>中介者</strong> ，有些类似中介者模式的思想，所有的订阅者和发布者，统一通过中介者进行订阅事件和派发事件:</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/49b292640a40412ea36e2437942a42cc~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>发布订阅模式</strong> 和 <strong>观察者模式</strong> 的主要区别是：</p>
<ul>
<li>从角色来说，发布订阅模式多出了一个中间者作为调度中心，来专门管理事件。</li>
<li>从耦合的角度看，观察者模式中的观察者/被观察者的关系是 <strong>松耦合</strong>，发布订阅模式中的发布者/订阅者是完全 <strong>无耦合</strong> 的。</li>
<li>从关注点出发，观察者模式是 2 者间直接交互，更关心 <strong>数据源</strong> ，发布订阅模式则更关心 <strong>事件</strong> 消息。</li>
</ul>
<p>综合当前业务场景，在插件化设计中，采用 <strong>发布订阅模式</strong> 是更合适的。</p>
<blockquote>
<p>Note：</p>
<p>关于观察者模式和发布订阅模式的具体差异，我个人认为是观察者模式在 <strong>处理复杂情况</strong> 的一种解决方式，加入一个中间层而已，不用过度纠结。</p>
<p>不是有这么一句话么：计算机科学领域的任何问题都可以通过增加一个间接的中间层来解决。</p>
</blockquote>
<h4 data-id="heading-20">事件机制具体实现</h4>
<p>利用 <code>发布订阅模式</code>来实现事件机制，主要工作是完成一个带有 <code>发布&订阅</code> 功能的中间者，先把它叫做 EventDispatcher。</p>
<p>EventDispatcher 需要对外提供的功能：</p>
<ul>
<li>订阅事件</li>
<li>发布事件</li>
<li>取消事件的订阅</li>
</ul>
<p>发布事件进行通知订阅对象时，一定需要知道 3 个关键的东西：</p>
<ul>
<li>事件</li>
<li>订阅对象</li>
<li>响应方法</li>
</ul>
<p>发布前就需要将 3 个关键要素存储起来，在进行订阅的动作时，也至少要保证传入这 3 个参数。</p>
<p>目前采用的是 NSMapTable 来做存储，它的一个特性就是可以弱引用对象作为 key/value，键值对的一方对象释放后就会被自动删除，对事件机制实现的存储结构如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f19c3395330046b480148269610f2b6f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>进行 <strong>事件订阅</strong> 的逻辑处理流程如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5a0b1b7ead88467d9ec30caf32db5066~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>进行 <strong>事件发布</strong> 的逻辑处理流程如下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b451f1a4a464c97947e57781e3fbd76~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-21">如何通过事件交互</h4>
<p>插件之间通过事件来进行交互，主要有 4 个步骤进行：</p>
<ul>
<li>声明事件</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0958387888cd497eb45e0e4b1c7ba520~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>订阅事件</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/971cf1534bb840f689067a7ca3a4dad8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>派发事件</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83435dbde4f9466b9c2cc4f688718d33~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>处理事件</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d8a471204ab4a54b8b7b6209a5576bd~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过事件机制，某一个插件本身不用去关心和依赖其它插件，插件发生变化直接把事件或者状态抛出去，由关心事件的订阅者自己去自行响应处理。</p>
<p>例如同样是一个涉及更新的动作，平常的方式可能是:</p>
<pre><code class="hljs language-objc copyable" lang="objc"> <span class="hljs-comment">//C.m</span>
 <span class="hljs-keyword">if</span> (needUpdate)&#123;
     [A update];
     [B update];
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>通过事件的方式则是：</p>
<pre><code class="hljs language-objc copyable" lang="objc"> <span class="hljs-comment">//C.m</span>
 <span class="hljs-keyword">if</span> (needUpdate)&#123;
     [<span class="hljs-keyword">self</span> dispatchEvent:kAllPluginNeedUpdate];
 &#125;
 
<span class="hljs-comment">// A.m</span>
- (<span class="hljs-keyword">void</span>)handlePluginUpdate
&#123;
   [<span class="hljs-keyword">self</span> update];
   <span class="hljs-comment">//doSomething</span>
&#125;

<span class="hljs-comment">// B.m</span>
- (<span class="hljs-keyword">void</span>)handlePluginUpdate
&#123;
   [<span class="hljs-keyword">self</span> update];
  <span class="hljs-comment">//doSomething</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>至此，插件间的横向依赖问题也解得到了解决，可以做到 <strong>无痛的删除插件</strong>，而不影响业务。</p>
<h2 data-id="heading-22">总结</h2>
<p>插件化设计最重要事情是解除耦合，而无侵入引入插件和无痛删除插件，都属于检验耦合程度的手段。</p>
<p>相对于性能优化，架构的升级总是相对滞后，无法通过数据去直接观察，也无法直观体现成果。想了一想，我觉得有一句话可以来形容好架构：</p>
<blockquote>
<p>善战者，无赫赫之功。</p>
</blockquote>
<p>没有完美的设计，只有合适的设计，希望大家可以多多提意见，互相学习。</p>
<h2 data-id="heading-23">参考</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fbaike.baidu.com%2Fitem%2F%25E4%25BA%258B%25E4%25BB%25B6%25E5%25A4%2584%25E7%2590%2586%25E6%259C%25BA%25E5%2588%25B6%2F22068672" target="_blank" rel="nofollow noopener noreferrer" title="https://baike.baidu.com/item/%E4%BA%8B%E4%BB%B6%E5%A4%84%E7%90%86%E6%9C%BA%E5%88%B6/22068672" ref="nofollow noopener noreferrer">事件处理机制</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fzhuanlan.zhihu.com%2Fp%2F51357583" target="_blank" rel="nofollow noopener noreferrer" title="https://zhuanlan.zhihu.com/p/51357583" ref="nofollow noopener noreferrer">《观察者模式 vs 发布订阅模式》</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.infoq.cn%2Farticle%2Fejkw6sz5qouuhxgag5vy" target="_blank" rel="nofollow noopener noreferrer" title="https://www.infoq.cn/article/ejkw6sz5qouuhxgag5vy" ref="nofollow noopener noreferrer">《优酷 iOS 插件化页面架构方案》</a></p></div>  
</div>
            