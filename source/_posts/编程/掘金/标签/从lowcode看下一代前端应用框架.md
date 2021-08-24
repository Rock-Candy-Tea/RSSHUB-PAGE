
---
title: '从lowcode看下一代前端应用框架'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b676929bd23e4125a96b5be427d3c580~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 17:54:17 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b676929bd23e4125a96b5be427d3c580~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>导读</strong>：自从angular/react/vue的出现颠覆了前端开发者开发模式以来，虽然新的前端框架依然不断涌现，但是迟迟没有一个新的前端框架进入广大前端开发者的视野。本文会从近两年越来越火的lowcode/微前端出发，探讨在传统前端领域，下一代前端工程/框架的可能方向。</p>
<p><em>全文3166字，预计阅读时间 6分钟。</em></p>
<h1 data-id="heading-0"><strong>一、lowcode</strong></h1>
<p>lowcode 其实一点也不新，通过 GUI、配置化的方式代替传统的手写代码编程，从sql语句到dreamweaver,基于模型驱动的可视化的编程工具层出不穷。</p>
<p>而近两年lowcode的兴起，笔者认为主要有以下原因：</p>
<p>1.前端技术体系及工程化体系成熟，许多有追求的工程师渴望用新的轮子追求变革式的生产效率突破；<br>
2.前端开发者依旧稀缺；<br>
3.B端业务兴起，大厂提前布局，希望在未来能够商业化从中获利；</p>
<p>而和历史上诸多尝试相比，这次前端lowcode平台的兴起最大的不同: 大多数平台的目的是为了解决普通人的编程问题，而不再是开发者的编程效率问题。</p>
<hr>
<h2 data-id="heading-1"><strong>1.1 国内lowcode平台</strong></h2>
<p><strong>目前应用比较广泛的：</strong><br>
易企秀、淘宝天马 这样的基于页面模板搭建，开发人员开发模板（或者开发人员开发模块和模板），运营人员配置页面；阿里云凤蝶、百度爱速搭这样的组件配置平台（可以通过配置组件实现模板功能）。这些平台都一定程度满足了用户快速建站的需求，特别是时间紧、没有开发人力时。</p>
<h2 data-id="heading-2"><strong>1.2 lowcode可以解决所有问题吗？</strong></h2>
<p>lowcode平台是为了提升一部分交互简单的前端开发场景开发效率的，这也就是说对于使用者来说最大的问题在于使用场景及时机的判断上：</p>
<ul>
<li>
<p>谁来判断使用哪个lowcode的平台，研发还是产品经理？</p>
</li>
<li>
<p>找到平台后，谁来判断哪些业务可以使用平台搭建？</p>
</li>
<li>
<p>谁来搭建？</p>
</li>
<li>
<p>当平台只能满足99%需求时怎么办？</p>
</li>
</ul>
<p>所以很多时候，我们找到了平台，配置了页面，最后发现某个需求完成不了而不了了之。当然，许多平台支持开发人员开发定制模板或者自定义组件，但是，<strong>当你有了自定义组件需求时，基于平台开发还会比自行开发效率高吗？</strong></p>
<h2 data-id="heading-3"><strong>1.3 场景举例</strong></h2>
<p>我们孵化了一款新的APP，希望配置一个简单宣传页，页面内容就是一张背景图，一个下载按钮。<br>
我们使用平台配置好了页面，也配置好了按钮的下载链接，此时PM提出了新需求，当用户已经安装了APP时不再下载而是直接打开APP，我应该基于平台开发一个自定义的action还是自己线下开发下呢？？？</p>
<hr>
<h2 data-id="heading-4"><strong>1.4 serverless</strong></h2>
<p>当然，lowcode平台也提供了一些serverless的功能，但还是那个问题，谁来评估要不要用serverless？谁来使用？遇到不支持的问题该怎么办？</p>
<h1 data-id="heading-5"><strong>二、微前端要解决什么问题</strong></h1>
<p>微前端是一种从后端微服务借鉴过来的架构方式。市面上微前端的方案层出不穷，我就不列了，我们只需要明确下，微前端、前端微服务到底要解决什么问题：<strong>利用服务化、微服务的概念，有效的拆分应用，实现敏捷开发和部署，解决大型项目的管理问题。</strong></p>
<h2 data-id="heading-6"><strong>2.1 场景举例</strong></h2>
<p>两个不同团队的业务，需要合成一个：电商平台、视频PC发布平台，需要统一到同一个站点，让用户实现发布视频、挂接商品一条路径走通。</p>
<p>当业务简单时，可以让两个团队协助工作，但是当各自业务越来越复杂，会有越来多的问题出现：</p>
<ul>
<li>
<p>技术栈必须统一</p>
</li>
<li>
<p>开发、部署耦合</p>
</li>
<li>
<p>运行时一个业务的BUG可能带崩整个系统</p>
</li>
</ul>
<hr>
<h2 data-id="heading-7"><strong>2.2 为什么提到微前端</strong></h2>
<p>微前端的兴起，说明前端工程复杂度的提升，越来越多的人遇到类似的架构问题，说明我们需要一个更上层的应用框架来帮助我们解决类似应用拆分隔离这样的架构问题。</p>
<h1 data-id="heading-8"><strong>三、前端框架及前端工程化</strong></h1>
<h2 data-id="heading-9"><strong>3.1 前端框架</strong></h2>
<p>我们思考 jQuery/React/Vue 这几个划时代框架/类库的共性，会发现他们都是为了解决视图层的问题而诞生的。</p>
<p>这不难理解，传统前端的核心就是视图，如何更快的帮助前端开发者更好的完成视图开发工作，是大部分前端框架要解决的核心问题。</p>
<p>jQuery简化了视图层开发的DOM API，React/Vue 更是绕开了API，颠覆了页面的开发模式。这个过程中，随着前端技术的发展，工程化在框架应用中所占比重越来越大，大多数vue使用者创建项目都是通过vue cli创建。</p>
<hr>
<h2 data-id="heading-10"><strong>3.2 什么是前端工程化？</strong></h2>
<p>工程化是一种思想，主要目的是为了提效，即提高开发效率，减少不必要的重复工作。工程化常见的方向有模块化、组件化、规范化、自动化4个方面。</p>
<p>回顾前端框架的发展，会发现前端框架的发展其实和工程化发展相辅相成，绕开DOM API、通过工程化实现更低的上手成本 是vue/react成功的根本，而vue/react在代码运行侧已经解决了足够多的问题，前端框架后续的发展焦点需要更多的偏向工程化。</p>
<p>===</p>
<h1 data-id="heading-11"><strong>四、下一代前端应用框架</strong></h1>
<p>使用高度工程化的应用框架进一步推动组件化发展，再度重塑开发模式，这是我认为下一代前端应用框架需要做的事！</p>
<p>换句话说，它需要更容易的让开发者解决组件化、自动化、规范化等工程化的问题，可以快速让开发者实现一个lowcode、procode、微前端等平台或是架构。</p>
<h1 data-id="heading-12"><strong>五、我们在做的事</strong></h1>
<p>lowcode、微前端都是高度工程化的架构实践，我们将其中的架构思路抽离出来，开发了一个服务于开发者的前端框架，并基于框架开发了内部的lowcode平台：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b676929bd23e4125a96b5be427d3c580~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>它的实现分两部分</p>
<ul>
<li>
<p>数据驱动的前端应用框架，让开发者基于json配置组织页面</p>
</li>
<li>
<p>lowcode 平台（可视化配置平台）,将配置json映射成普通人可用的配置项</p>
</li>
</ul>
<p>组件数据：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/471f9aa025c945c9bcd2f0b300c6fd5f~tplv-k3u1fbpfcp-watermark.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>底层基于成熟ui层框架实现，上层通过工程化实践，将写页面变成写配置，让开发人员在写页面时，只需要写一份json配置。</p>
<p>前端工作变成了两部分：</p>
<ul>
<li>
<p>通用组件开发</p>
</li>
<li>
<p>页面配置开发</p>
</li>
</ul>
<p>简而言之，这个框架的作用是让开发者基于json配置组织页面。</p>
<h2 data-id="heading-13"><strong>5.1 一些框架细节</strong></h2>
<h3 data-id="heading-14">5.1.1 规范</h3>
<p>我们给出了组件属性名的命名规范，对于大多数组件（业务/通用）来说，他们有相同或相似的属性名,例：data/children/label。</p>
<ul>
<li>
<p>类似 useState 可以对特定属性名做校验、做测试,并且轻松实现预编译优化；</p>
</li>
<li>
<p>降低上手难度，对于大多数组件，只需要知道组件名就能轻松上手，利于组件推广。</p>
</li>
</ul>
<h3 data-id="heading-15"></h3>
<h3 data-id="heading-16">5.1.2 如何解决自定义开发问题</h3>
<p><strong>我们把自定义开发分为两类</strong>：</p>
<ul>
<li>
<p>自定义组件：主要是构建层，可以让自定义组件单独部署上线；</p>
</li>
<li>
<p>自定义action：类似发布订阅，指定触发类型（点击）、触发事件名（dispatch(type)）,所有action收归顶层管理。</p>
</li>
</ul>
<h3 data-id="heading-17"></h3>
<h3 data-id="heading-18">5.1.3 如何更快的和后端联系</h3>
<p><strong>框架推荐的数据交互方式：</strong><br>
1.编写action（可以使用通用action: getData 快速获取数据）<br>
2.组件触发action（init/click/scroll）<br>
3.数据获取并挂载<br>
4.组件订阅数据并更新</p>
<hr>
<h2 data-id="heading-19"><strong>5.2 他的优势是什么</strong></h2>
<ul>
<li>
<p>按照微服务的理念，样式、自定义组件、自定义的方法可以第三方npm、线上链接注入 => 更好的实现模块化和模块隔离；</p>
</li>
<li>
<p>开发页面变成开发组件和写页面配置 => 更方便实现自动化和规范化；</p>
</li>
<li>
<p>组件的开发有着通用、可扩展的规范 => 更好的实现组件化和规范化；</p>
</li>
<li>
<p>针对json配置的自动化测试，针对json配置的上线部署、热更新等等都会更有利于实现工程化；</p>
</li>
</ul>
<h1 data-id="heading-20"><strong>六、愿景</strong></h1>
<p>我们希望找到lowcode平台和普通前端开发的平衡点，既能提升传统前端开发的效率，又可以为lowcode的发展赋能。</p>
<p>我们更希望能孵化出下一代的应用框架，解决更多开发中、工程化实践遇到的架构问题。</p>
<p><strong>招聘信息</strong>：</p>
<p>百度直播研发部招聘研发岗位，包括客户端-Android/iOS方向，服务端-Go/PHP方向。我们负责百度直播业务，对直播业务感兴趣欢迎加入我们。</p>
<p>简历投递邮箱：<a href="https://link.juejin.cn/?target=mailto%3Ageektalk%40baidu.com" target="_blank" title="mailto:geektalk@baidu.com" ref="nofollow noopener noreferrer">geektalk@baidu.com</a> （投递备注【直播研发部】）</p>
<p><strong>推荐阅读</strong>：</p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg5MjU0NTI5OQ%3D%3D%26mid%3D2247497498%26idx%3D1%26sn%3D76aec4723a8ace1c62f84fa69ebd5865%26chksm%3Dc03ec766f7494e7018d15106466f3476ce992cdf87de7c063627762598c59b77337a5d3f6e48%26scene%3D21%23wechat_redirect" target="_blank" rel="nofollow noopener noreferrer" title="http://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247497498&idx=1&sn=76aec4723a8ace1c62f84fa69ebd5865&chksm=c03ec766f7494e7018d15106466f3476ce992cdf87de7c063627762598c59b77337a5d3f6e48&scene=21#wechat_redirect" ref="nofollow noopener noreferrer"><strong>｜</strong></a><a href="https://link.juejin.cn/?target=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg5MjU0NTI5OQ%3D%3D%26mid%3D2247498724%26idx%3D1%26sn%3D1d91c09c602330d3fef5df43ca65776c%26chksm%3Dc03ecb98f749428e900c0712006d1ec00adfa166adc8f8069e186f300b1c3c86bfeb82e8019c%26scene%3D21%23wechat_redirect" target="_blank" rel="nofollow noopener noreferrer" title="http://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247498724&idx=1&sn=1d91c09c602330d3fef5df43ca65776c&chksm=c03ecb98f749428e900c0712006d1ec00adfa166adc8f8069e186f300b1c3c86bfeb82e8019c&scene=21#wechat_redirect" ref="nofollow noopener noreferrer"><strong>短视频go研发框架实践</strong></a></p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg5MjU0NTI5OQ%3D%3D%26mid%3D2247497498%26idx%3D1%26sn%3D76aec4723a8ace1c62f84fa69ebd5865%26chksm%3Dc03ec766f7494e7018d15106466f3476ce992cdf87de7c063627762598c59b77337a5d3f6e48%26scene%3D21%23wechat_redirect" target="_blank" rel="nofollow noopener noreferrer" title="http://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247497498&idx=1&sn=76aec4723a8ace1c62f84fa69ebd5865&chksm=c03ec766f7494e7018d15106466f3476ce992cdf87de7c063627762598c59b77337a5d3f6e48&scene=21#wechat_redirect" ref="nofollow noopener noreferrer"><strong>｜</strong></a><a href="https://link.juejin.cn/?target=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg5MjU0NTI5OQ%3D%3D%26mid%3D2247498417%26idx%3D1%26sn%3Da3f0a0c312c58693b3623cab0f387df4%26chksm%3Dc03ecacdf74943db287e50e0249cb8ae14823bc84d6f22ddacd8ee3cf5bc8038c76faa4ed667%26scene%3D21%23wechat_redirect" target="_blank" rel="nofollow noopener noreferrer" title="http://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247498417&idx=1&sn=a3f0a0c312c58693b3623cab0f387df4&chksm=c03ecacdf74943db287e50e0249cb8ae14823bc84d6f22ddacd8ee3cf5bc8038c76faa4ed667&scene=21#wechat_redirect" ref="nofollow noopener noreferrer"><strong>千亿级模型在离线一致性保障方案详解</strong></a></p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg5MjU0NTI5OQ%3D%3D%26mid%3D2247497498%26idx%3D1%26sn%3D76aec4723a8ace1c62f84fa69ebd5865%26chksm%3Dc03ec766f7494e7018d15106466f3476ce992cdf87de7c063627762598c59b77337a5d3f6e48%26scene%3D21%23wechat_redirect" target="_blank" rel="nofollow noopener noreferrer" title="http://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247497498&idx=1&sn=76aec4723a8ace1c62f84fa69ebd5865&chksm=c03ec766f7494e7018d15106466f3476ce992cdf87de7c063627762598c59b77337a5d3f6e48&scene=21#wechat_redirect" ref="nofollow noopener noreferrer"><strong>｜</strong></a><a href="https://link.juejin.cn/?target=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg5MjU0NTI5OQ%3D%3D%26mid%3D2247498185%26idx%3D1%26sn%3D6abfb6a1bb9c3c78ca6f7a974174905d%26chksm%3Dc03ec9b5f74940a3c51744c44b39ab5c74967421389a7eaa2f596c3a9ec66e733e5d3d551215%26scene%3D21%23wechat_redirect" target="_blank" rel="nofollow noopener noreferrer" title="http://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247498185&idx=1&sn=6abfb6a1bb9c3c78ca6f7a974174905d&chksm=c03ec9b5f74940a3c51744c44b39ab5c74967421389a7eaa2f596c3a9ec66e733e5d3d551215&scene=21#wechat_redirect" ref="nofollow noopener noreferrer"><strong>如何快速定位程序Core？</strong></a></p>
<p>---------- END ----------</p>
<p><strong>百度Geek说</strong></p>
<p>百度官方技术公众号上线啦！</p>
<p>技术干货 · 行业资讯 · 线上沙龙 · 行业大会</p>
<p>招聘信息 · 内推信息 · 技术书籍 · 百度周边</p>
<p>欢迎各位同学关注</p></div>  
</div>
            