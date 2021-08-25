
---
title: 'Android模块化开发实践'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6656f6bbb5d94065a2116a0a7c023a5c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 17:43:24 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6656f6bbb5d94065a2116a0a7c023a5c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一、前言</h1>
<p>随着业务的快速发展，现在的互联网App越来越大，为了提高团队开发效率，模块化开发已经成为主流的开发模式。正好最近完成了vivo官网App业务模块化改造的工作，所以本文就对模块化开发模式进行一次全面的介绍，并总结模块化改造经验，帮助兄弟项目避坑。</p>
<h1 data-id="heading-1">二、什么是模块化开发</h1>
<p>首先我们搞清两个概念，Android客户端开发目前有两种模式：<strong>单工程开发模式</strong>和<strong>模块化开发模式</strong>。</p>
<ul>
<li>
<p>**单工程开发模式：**早期业务少、开发人员也少，一个App对应一个代码工程，所有的代码都集中在这一个工程的一个module里。</p>
</li>
<li>
<p>**模块化开发模式：**简单来说，就是将一个App根据业务功能划分成多个独立的代码模块，整个App是由这些独立模块集成而成。</p>
</li>
</ul>
<p>在讲什么是模块化开发前，我们先定义清楚两个概念：组件和模块。</p>
<ul>
<li>
<p>**组件：**指的是单一的功能组件，比如登录组件、分享组件；</p>
</li>
<li>
<p>**模块：**广义上来说是指功能相对独立、边界比较清晰的业务、功能等，本文如果单独出现模块这个词一般是该含义。狭义上是指一个业务模块，对应产品业务，比如商城模块、社区模块。</p>
</li>
</ul>
<p>模块和组件的本质思想是一样的，都是为了业务解耦和代码重用，组件相对模块粒度更细。在划分的时候，模块是业务导向，划分一个个独立的业务模块，组件是功能导向，划分一个个独立的功能组件。</p>
<p>模块化开发模式又分为两种具体的开发模式：<strong>单工程多module模式</strong>和<strong>多工程模式</strong>。</p>
<p><strong>单工程多module模式</strong>：</p>
<p>所有代码位于一个工程中，模块以AndroidStudio的module形式存在，由一个App module和多个模块module组成。如图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6656f6bbb5d94065a2116a0a7c023a5c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>多工程模式</strong>：</p>
<p>每个模块代码位于一个工程中，整个项目由一个主模块工程和多个子模块工程组成。其中主模块工程只有一个App module，用于集成子模块，进行整体调试、编包。子模块工程由一个App module和一个Library module组成，App module中是调试、测试代码，Library module中是业务、功能代码。如下图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14128dc26a0a401bb802fb90506234b1~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/58123066b032411ba7428571ca33e0b9~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>下面我们来对比一下单工程多module模式和多工程模式的优缺点：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/64445ab2ca7241eca8e255a559bd3c20~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过上面的对比，我们可以看出来，多工程模式在代码管理、开发调试、业务并行等方面有明显优势，非常适合像vivo官网这种业务线多、工程大、开发人员多的App，所以vivo官网目前就采用的此模式。本文在讲解模块化开发时，一般也是指多工程模式。</p>
<p>单工程多module模式，更适合开发人员少、业务并行程度低的项目。但是多工程模式也有<strong>两个缺点：代码仓较多、开发时需要打开多个工程</strong>，针对这两个缺点，我们也有解决方案。</p>
<p><strong>代码仓较多的问题</strong></p>
<p>要求我们在拆分模块时粒度不能太细，当一个模块膨胀到一定程度时再进行拆分，在模块化带来的效率提升与代码仓管理成本增加间保持平衡。</p>
<p><strong>要打开多个工程开发的问题</strong></p>
<p>我们基于Gradle插件开发了代码管理工具，可以方便的切换通过代码依赖子模块或者maven依赖子模块，实际开发体验跟单工程多module模式一样，如下图；</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c500f142feb4d3db9137cd2c0d06f02~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>模块化开发的流程也很简单：</p>
<ul>
<li>
<p>版本前期，每个模块由特定的开发人员负责，各子模块分别独立开发、调试；</p>
</li>
<li>
<p>子模块开发完成后，集成到主模块工程进行整体调试；</p>
</li>
<li>
<p>集成调试成功后，进入测试。</p>
</li>
</ul>
<h1 data-id="heading-2">三、模块化开发</h1>
<h2 data-id="heading-3">3.1 我们为什么要做模块化开发呢？</h2>
<p>这里我们说说单一工程开发模式的一些痛点。</p>
<p><strong>团队协作效率低</strong></p>
<ul>
<li>
<p>项目早期业务少、开发人员也少，随着业务发展、团队扩张，由于代码都在同一个工程中，虽然各个人开发的功能不同，但是经常会修改同一处的代码，这时就需要相关开发人员沟通协调以满足各自需求，增加沟通成本；</p>
</li>
<li>
<p>提交代码时，代码冲突也要沟通如何合并（否则可能引起问题），增加合代码成本；</p>
</li>
<li>
<p>无法进行并行版本开发，或者勉强进行并行开发，代价是各个代码分支差异大，合并代码困难。</p>
</li>
</ul>
<p><strong>代码维护成本高</strong></p>
<ul>
<li>单一工程模式由于代码都在一起，代码耦合严重，业务与业务之间、业务与公共组件都存在很多耦合代码，可以说是你中有我、我中有你，任何修改都可能牵一发而动全身，随着版本的迭代，维护成本会越来越高。</li>
</ul>
<p><strong>开发调试效率低</strong></p>
<ul>
<li>任何一次的修改，即使是改一个字符，都需要编译整个工程代码，随着代码越来越多，编译也越来越慢，非常影响开发效率。</li>
</ul>
<h2 data-id="heading-4">3.2 如何解决问题</h2>
<p>说完单一工程开发模式的痛点，下面我们看看模块化开发模式怎么来解决这些问题的。</p>
<p><strong>提高团队协作效率</strong></p>
<ul>
<li>
<p>模块化开发模式下，根据业务、功能将代码拆分成独立模块，代码位于不同的代码仓，版本并行开发时，各个业务线只在各自的模块代码仓中进行开发，互不干扰，对自己修改的代码负责；</p>
</li>
<li>
<p>测试人员只需要重点测试修改过的功能模块，无需全部回归测试；</p>
</li>
<li>
<p>要求产品层面要有明确的业务划分，并行开发的版本必须是不同业务模块。</p>
</li>
</ul>
<p><strong>降低代码维护成本</strong></p>
<ul>
<li>
<p>模块化开发对业务模块会划分比较明确的边界，模块间代码是相互独立的，对一个业务模块的修改不会影响其他模块；</p>
</li>
<li>
<p>当然，这对开发人员也提出了要求，模块代码需要做到高内聚。</p>
</li>
</ul>
<p><strong>提高编译速度</strong></p>
<ul>
<li>
<p>开发阶段，只需要在自己的一个代码仓中开发、调试，无需集成完整App，编译代码量极少；</p>
</li>
<li>
<p>集成调试阶段，开发的代码仓以代码方式依赖，其他不涉及修改的代码仓以aar方式依赖，整体的编译代码量也比较少。</p>
</li>
</ul>
<p>当然模块化开发也不是说全都是好处，也存在一些缺点，比如：</p>
<blockquote>
<p>1）业务单一、开发人员少的App不要模块化开发，那样反而会带来更多的维护成本；</p>
<p>2）模块化开发会带来更多的重复代码；</p>
<p>3）拆分的模块越多，需要维护的代码仓越多，维护成本也会升高，需要在拆分粒度上把握平衡。</p>
</blockquote>
<p>总结一下，模块化开发就像我们管理书籍一样，一开始只有几本书时，堆书桌上就可以了。随着书越来越多，有几十上百本时，我们需要一个书橱，按照类别放在不同的格子里。对比App迭代过程，起步时，业务少，单一工程模式效率最高，随着业务发展，我们要根据业务拆分不同的模块。</p>
<p>所有这些目的都是为了方便管理、高效查找。</p>
<h1 data-id="heading-5">四、模块化架构设计</h1>
<p>模块化架构设计的思路，我们总结为<strong>纵向和横向两个维度</strong>。纵向上根据与业务的紧密程度进行分层，横向上根据业务或者功能的边界拆分模块。</p>
<p>下图是目前我们App的整体架构。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e069602b93a04bb485e97046e5069214~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-6">4.1 纵向分层</h2>
<p>先看纵向分层，根据业务耦合度从上到下依次是业务层、组件层、基础框架层。</p>
<ul>
<li>
<p>业务层：位于架构最上层，根据业务模块划分（比如商城、社区等），与产品业务相对应；</p>
</li>
<li>
<p>组件层：App的一些基础功能（比如登录、自升级）和业务公用的组件（比如分享、地址管理），提供一定的复用能力；</p>
</li>
<li>
<p>基础框架层：完全与业务无关、通用的基础组件（比如网络请求、图片加载），提供完全的复用能力。</p>
</li>
</ul>
<p>框架层级从上往下，业务相关性越来越低，代码稳定性越来越高，代码入仓要求越来越严格（可以考虑代码权限收紧，越底层的代码，入仓要求越高）。</p>
<h2 data-id="heading-7">4.2 横向分模块</h2>
<ul>
<li>
<p>在每一层上根据一定的粒度和边界，拆分独立模块。比如业务层，根据产品业务进行拆分。组件层则根据功能进行拆分。</p>
</li>
<li>
<p>大模块可以独立一个代码仓（比如商城、社区），小模块则多个模块组成一个代码仓（比如上图中虚线中的就是多个模块位于一个仓）。</p>
</li>
<li>
<p>模块要高内聚低耦合，尽量减少与其他模块的依赖。</p>
</li>
</ul>
<p>面向对象设计原则强调组合优于继承，平行模块对应组合关系，上下层模块对应继承关系，组合的优点是封装性好，达到高内聚效果。所以在考虑框架的层级问题上，我们更偏向前者，也就是拆分的模块尽量平行，减少层级。</p>
<p><strong>层级多的问题在于，下层代码仓的修改会影响更多的上层代码仓，并且层级越多，并行开发、并行编译的程度越低。</strong></p>
<p><strong>模块依赖规则：</strong></p>
<ul>
<li>
<p>只有上层代码仓才能依赖下层代码仓，不能反向依赖，否则可能会出现循环依赖的问题；</p>
</li>
<li>
<p>同一层的代码仓不能相互依赖，保证模块间彻底解耦。</p>
</li>
</ul>
<h1 data-id="heading-8">五、模块化开发需要解决哪些问题</h1>
<h2 data-id="heading-9">5.1 业务模块如何独立开发、调试？</h2>
<p>方式一：每个工程有一个App module和一个Library module，利用App module中的代码调试Library module中的业务功能代码。</p>
<p>方式二：利用代码管理工具集成到主工程中调试，开发中的代码仓以代码方式依赖，其他模块以aar方式依赖。</p>
<h2 data-id="heading-10">5.2 平行模块间如何实现页面跳转，包括Activity跳转、Fragment获取？</h2>
<p>根据模块依赖原则，平行模块间禁止相互依赖。隐式Intent虽然能解决该问题，但是需要通过Manifest集中管理，协作开发比较麻烦，所以我们选择了路由框架Arouter，Activity跳转和Fragment获取都能完美支持。另外Arouter的拦截器功能也很强大，比如处理跳转过程中的登录功能。</p>
<h2 data-id="heading-11">5.3 平行模块间如何相互调用方法？</h2>
<p>Arouter服务参考——<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Falibaba%2FARouter%25E3%2580%2582" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/alibaba/ARouter%E3%80%82" ref="nofollow noopener noreferrer">github.com/alibaba/ARo…</a></p>
<h2 data-id="heading-12">5.4 平行模块间如何传递数据、驱动事件？</h2>
<p>Arouter服务、EventBus都可以做到，视具体情况定。</p>
<h1 data-id="heading-13">六、老项目如何实施模块化改造</h1>
<p>老项目实施模块化改造非常需要耐心和细心，是一个循序渐进的过程。</p>
<p>先看一下我们项目的模块化进化史，从单一工程逐步进化成纺锤形的多工程模块化模式。下图是进化的四个阶段，从最初的单个App工程到现在的4层多仓结构。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c71f4aa0f634cfa82100e8c629769c9~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c70cac444f9044ffb2721fea6d32f483~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92c3f10c412844aa9d1ab089d5fe22fc~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>注：此图中每个方块表示一个代码仓，上层代码仓依赖下层代码仓。</p>
<p>早期项目都是采用单一工程模式的，随着业务的发展、人员的扩张，必然会面临将老项目进行模块化改造的过程。但是在模块化改造过程中，我们会面临很多问题，比如：</p>
<ul>
<li>
<p>代码逻辑复杂，缺乏文档、注释，不敢轻易修改，害怕引起功能异常；</p>
</li>
<li>
<p>代码耦合严重，你中有我我中有你，牵一发动全身，拆分重构难度大；</p>
</li>
<li>
<p>业务版本迭代与模块化改造并行，代码冲突频繁，影响项目进度；</p>
</li>
</ul>
<p>相信做模块化的人都会遇到这些问题，但是模块化改造势在必行，我们不可能暂停业务迭代，把人力都投入到模块化中来，一来业务方不可能同意，二来投入太多人反而会带来更多代码冲突。</p>
<p>所以需要一个可行的改造思路，我们总结为先<strong>自顶向下划分，再自底向上拆分</strong>。</p>
<p><strong>自顶向下</strong></p>
<ul>
<li>从整体到细节逐层划分模块，先划分业务线，业务线再划分业务模块，业务模块中再划分功能组件，最终形成一个树状图。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07d69133320148f499a644c6af05750b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>自底向上</strong></p>
<ul>
<li>
<p>当我们把模块划分明确、依赖关系梳理清楚后，我们就需要自底向上，从叶子模块开始进行拆分，当我们把叶子模块都拆分完成后，枝干模块就可以轻松拆分，最后完成主干部分的拆分。</p>
</li>
<li>
<p>另外整个模块化工作需要由专人统筹，整体规划，完成主要的改造工作，但是有复杂的功能也可以提需求给各模块负责人，协助完成改造。</p>
</li>
</ul>
<p>下面就讲讲我们在模块化改造路上打怪升级的一些经验。<strong>总的来说就是循序渐进，各个击破</strong>。</p>
<h2 data-id="heading-14">6.1 业务模块梳理</h2>
<p>这一步是自顶向下划分模块，也就是确定子模块代码仓。一个老项目必然经过多年迭代，经过很多人开发，你不一定要对所有的代码都很熟悉，但是你必须要基本了解所有的业务功能，在此基础上综合产品和技术规划进行初步的模块划分。</p>
<p>此时的模块划分可以粒度粗一点，比如根据业务线或者大的业务模块进行划分，但是边界要清晰。一个App一般会有多个业务线，每个业务线下又会有多个业务模块，这时，我们梳理业务不需要太细，保持2层即可，否则过度的拆分会大大增加实施的难度。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db0fc3bcb9074d6dbf3c1074b1ccc10a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-15">6.2 抽取公共组件</h2>
<p>划分完模块，但是如果直接按此来拆分业务模块，会有很大难度，并且会有很多重复代码，因为很多公共组件是每个业务模块都要依赖的（比如网络请求、图片加载、分享、登录）。所以模块化拆分的第一步就是要抽取、下沉这些公共组件。</p>
<p>在这一步，我们在抽取公共组件时会遇到两类公共组件，一类是完全业务无关的基础框架组件（比如网络请求、图片加载），一类是业务相关的公共业务组件（比如分享、登录）。</p>
<p>可以将这两类公共组件分成两层，便于后续的整体框架形成。比如我们的lib仓放的是基础框架组件和core仓放的是业务公共组件。如下图</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c5e00f3d4c04addb1da9fdd79885e2b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-16">6.3 业务模块拆分</h2>
<p>抽取完公共组件后，我们要准备进行业务模块的拆分，这一步耗时最长，但也是效果最明显的，因为拆完我们就可以多业务并行开发了。</p>
<p>确定要拆分的业务模块（比如下图的商城业务），先把代码仓拉出来，新功能直接在新仓开发。</p>
<p>那老功能该怎么拆分迁移呢？我们不可能一口吃成大胖子，想一次把一个大业务模块全部拆分出来，难度太大。这时我们就要对业务模块内部做进一步的梳理，找出所有的子功能模块（比如商城业务中的支付、选购、商详等）。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e4a616afb39426db5d995f9cba22299~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>按照功能模块的独立程度，从易到难逐个拆分，比如支付的订单功能比较独立，那就先把订单功能的代码拆分到新仓。</p>
<h2 data-id="heading-17">6.4 功能模块拆分</h2>
<p>在拆分具体功能时，我们依然使用Top-Down的逻辑来实施，首先找到入口类（比如Activity），迁移到新的代码仓中，此时你会发现一眼望去全是报红，就像拔草一样带出大量根须。依赖的布局、资源、辅助类等等都找不到，我们按照从易到难的顺序一个个解决，需要解决的依赖问题有以下几类：</p>
<blockquote>
<p><strong>1）简单的依赖，比如字符串、图片。</strong></p>
<p>这类是最容易解决，直接把资源迁移过来即可。</p>
<p><strong>2）较复杂的依赖，比如布局文件、drawable。</strong></p>
<p>这类相对来说也比较容易解决，逐级迁移即可。比如布局依赖各种drawable、字符串、图片，drawable又依赖其他的drawable等，自顶向下逐个迁移就能解决。</p>
<p><strong>3）更复杂的依赖，类似A->B->C->D。</strong></p>
<p>对于这类依赖有两种解决方式，如果依赖的功能没有业务特性或只是简单封装系统 API，那可以考虑直接copy一份；如果依赖的代码是多个功能模块公用的或者多个功能模块需要保持一致，可以考虑将该功能代码抽取下沉到下一层代码仓。</p>
<p><strong>4）一时难以解决的依赖。</strong></p>
<p>可以先暂时注释掉，保证可以正常运行，后续理清逻辑再决定是进行解耦还是重构。斩断依赖链非常重要，否则可能坚持不下去。</p>
</blockquote>
<h2 data-id="heading-18">6.5 代码解耦</h2>
<p>下面介绍一下常用的代码解耦方法：</p>
<blockquote>
<p><strong>公共代码抽取下沉</strong></p>
<p>比如：基础组件（eg.网络请求框架）、各模块需要保持功能一致的代码（eg.适配OS的动效）；</p>
</blockquote>
<blockquote>
<p><strong>简单代码复制一份</strong></p>
<p>比如简单封装系统api（eg.获取packageName）、功能模块自用的自定义view（eg.提示弹窗）；</p>
</blockquote>
<blockquote>
<p><strong>三个工具</strong></p>
<p>Arouter路由、Arouter服务、EventBus，能满足各种解耦场景。</p>
</blockquote>
<h2 data-id="heading-19">6.6 新老代码共存</h2>
<p>老项目模块化是一个长期的过程，新老代码共存也是一个长期的过程。经过上面改造后，一个功能模块就可以独立出来了，因为我们都是从老的App工程里拆分出来的，所以App工程依赖新仓后就可以正常运行。当我们持续从老工程中拆分出独立模块，最后老工程只需要保留一些入口功能，作为集成子模块的主工程。</p>
<h1 data-id="heading-20">七、总结</h1>
<p>本文从<strong>模块化的概念</strong>、<strong>模块化架构设计</strong>以及<strong>老项目如何实施模块化改</strong>造等几个方面介绍移动应用客户端模块化实践。当然模块化工作远不止这些，还包括模块aar管理、持续集成、测试、模块化代码管理、版本迭代流程等，本文就不一一赘述，希望这篇文章能给准备做模块化开发的项目提供帮助。</p>
<blockquote>
<p>​作者：vivo互联网客户端团队-Wang Zhenyu</p>
</blockquote></div>  
</div>
            