
---
title: 'web自动化测试(1)_再谈UI发展史与UI、功能自动化测试'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e50666709792429dae30fd139fab82b8~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 02:36:01 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e50666709792429dae30fd139fab82b8~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言（废话）</h2>
<p>行文前，安利下文章：《<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhoulujun.cn%2Fhtml%2Fdesign%2Fui%2F2017_0330_7970.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhoulujun.cn/html/design/ui/2017_0330_7970.html" ref="nofollow noopener noreferrer">图形界面操作系统发展史——计算机界面发展历史回顾</a>》、《<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhoulujun.cn%2Fhtml%2Ftheory%2Fmodel%2F7823.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhoulujun.cn/html/theory/model/7823.html" ref="nofollow noopener noreferrer">再谈MV*(MVVM MVP MVC)模式的设计原理—封装与解耦</a>》</p>
<p>1973年4月，Xerox PARC (施乐公司帕洛阿尔托研究中心)研发出了第一台使用Alto操作系统的个人电脑，其中Alto是第一个把计算机所有元素结合到一起的图形界面操作系统。Xerox PARC还开发了一种名为Smalltalk的程序语言和环境，它拥有自己的GUI环境（包括了弹出菜单、视窗、图标）。</p>
<p>《乔布斯传》里，Jobs就是看到施乐开发中的实验性GUI以后，回去马上开始搞，还从施乐挖了一波人。然后微软有在苹果公开的东西上面模仿。接着就是一部波澜壮阔的GUI发展史。</p>
<p>从CS架构到BS架构。互联网发展如火如荼，推荐看下《<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhoulujun.cn%2Fhtml%2Fwebfront%2Fbrowser%2Fwebkit%2F2019_0615_8140.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhoulujun.cn/html/webfront/browser/webkit/2019_0615_8140.html" ref="nofollow noopener noreferrer">浏览器史话中chrome霸主地位的奠定与国产浏览器的割据混战</a>》，本人13年从Java入坑H5，但是前端的UI测试，除了前端工程师的 mocha karma jasmine 门后，就是给测试人员点点的感觉。前端UI如何自动化测试呢？</p>
<h2 data-id="heading-1">什么是自动化测试</h2>
<p>自动化测试：把人为驱动的测试转化为机器执行的一种过程，重点在于持续集成这个概念；</p>
<p>selenium 官网给出的测试类型有：</p>
<h3 data-id="heading-2">Types of testing</h3>
<p>测试分类，我的印象是：单元测试(Unit Testing)、集成测试(Integration Testing)、端到端测试(E2E Testing)</p>
<ul>
<li>
<p>Acceptance testing：验收测试、接收测试。测试产品功能是否完全。这个一般让产品把关。</p>
</li>
<li>
<p>Functional testing：功能测试，测试功能是否可用。</p>
</li>
<li>
<p>Regression testing：回归测试，是指修改了旧代码或加入新功能，重新进行测试以确认修改没有引入新的错误或导致其他代码产生错误</p>
</li>
<li>
<p>Performance testing：性能测试，测试程序是否稳定可靠</p>
</li>
<li>
<p>load testing：负载测试，不限制软件的运行资源，测试软件的数据吞吐量上限，以发现设计上的错误或验证系统的负载能力。<strong>负载测试的目标是确定并确保系统在超出最大预期工作量的情况下仍能正常运行</strong>。此外，负载测试还要评估性能特征。例如，响应时间、事务处理速率和其他与时间相关的方面。负载测试是测试的一个方法，通过不断调试并发数获取性能瓶颈。比如80个并发，这个叫80用户负载测试。通过80—>180这样的并发数变化过程，就叫做性能测试。也就是说，性能测试是通过不同的负载测试来实现的。</p>
</li>
<li>
<p>Stress testing：压力测试/强度测试，压力测试是对系统不断施加压力的测试，是通过确定一个系统的瓶颈或者不能接收的性能点，来获得系统能提供的最大服务级别的测试。压力测试是个高压力下的性能测试。</p>
</li>
</ul>
<p>负载测试与压力测试的区别：压力测试，就是高负载的情况下进行的，目的不是为了获取性能指标，而是想要了解系统是否稳定。这时候服务器的指标一般不超过90%。压力测试通过长时间的运行较性能测试更能容易发现内存泄露的问题。负载测试是个方法，性能测试是一个过程。</p>
<h2 data-id="heading-3">自动化测试分层</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e50666709792429dae30fd139fab82b8~tplv-k3u1fbpfcp-zoom-1.image" alt="测试分层" title="测试分层" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-4">单元自动化测试（数据处理层）：</h3>
<p><strong>单元测试（unit testing）</strong>：是指对软件中的最小可测试单元进行检查和验证。</p>
<p><strong>单元的含义</strong>：单元就是人为规定的最小的被测功能模块。单元测试是在软件开发过程中要进行的最低级别的测试活动，<strong>软件的独立单元将在与程序的其他部分相隔离的情况下进行测试</strong>，如C语言中单元指一个函数，Java里单元指一个类，图形化的软件中可以指一个窗口或一个菜单等。</p>
<p>单元自动化测试一般需要借助单元测试框架，如java的Junit、TestNG，python的unittest，常见的手段是code review等；</p>
<h4 data-id="heading-5">前端单元测试框架：</h4>
<ul>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fjasmine.github.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://jasmine.github.io/" ref="nofollow noopener noreferrer"><strong>Jasmine</strong></a>： 自带断言（assert）,mock功能</p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmochajs.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://mochajs.org/" ref="nofollow noopener noreferrer"><strong>Mocha</strong></a>： 框架不带断言和mock功能，需要结合其他工具，像chai。由tj大神开发</p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Ffacebook.github.io%2Fjest%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://facebook.github.io/jest/" ref="nofollow noopener noreferrer"><strong>Jest</strong></a>： 由Facebook出品的测试框架，在Jasmine测试框架上演变开发而来，集成了 Mocha,chai,jsdom,sinon等功能。</p>
</li>
</ul>
<h4 data-id="heading-6">前端断言库</h4>
<p>断言库提供了很多语义化的方法来对值做各种各样的判断。</p>
<ul>
<li>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fchaijs.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://chaijs.com/" ref="nofollow noopener noreferrer"><strong>chai</strong></a>: 目前比较流行的断言库，支持 TDD（assert），BDD（expect、should）两种风格</p>
</li>
<li>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fshouldjs.github.io%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://shouldjs.github.io/" ref="nofollow noopener noreferrer"><strong>should.js</strong></a>：也是tj大神所写</p>
</li>
</ul>
<p>前端集成管理工具</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fkarma-runner.github.io%2F2.0%2Findex.html" target="_blank" rel="nofollow noopener noreferrer" title="https://karma-runner.github.io/2.0/index.html" ref="nofollow noopener noreferrer">karma</a>：负责自动化执行测试脚本，批量处理脚本，统计测试。Google Angular 团队写的，功能很强大，有很多插件。可以连接真实的浏览器跑测试用例。能够用一些测试覆盖率统计的工具统计一下覆盖率；或是能够加入持续集成，提交代码后自动跑测试用例。</li>
</ul>
<h3 data-id="heading-7">接口自动化测试（业务逻辑层）：</h3>
<p><strong>接口测试</strong>：接口测试是对系统或组件之间的接口进行测试，主要是校验数据的交换，传递和控制管理过程，以及相互逻辑依赖关系。其中接口协议分为HTTP,WebService,Dubbo,Thrift,Socket等类型，测试类型又主要分为功能测试，性能测试，稳定性测试，安全性测试等。</p>
<p>主要检查验证模块间的调用返回以及不同系统、服务间的数据交换，常见的接口测试工具有postman、jmeter、loadrunner等；</p>
<p>这里我是强烈推荐Rap，一款开源免费的接口自动化、MOCK数据自动生成、自动化测试，企业级Web接口管理工具(阿里妈妈MUX团队出品)。RAP通过GUI工具帮助WEB工程师更高效的管理接口文档，同时通过分析接口结构自动生成Mock数据、校验真实接口的正确性，使接口文档成为开发流程中的强依赖。有了结构化的API数据，可避免更多重复劳动。</p>
<p>安利下自己的文章：《<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhoulujun.cn%2Fhtml%2Ftheory%2Fmodel%2F8026.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhoulujun.cn/html/theory/model/8026.html" ref="nofollow noopener noreferrer">前后端分离API设计指南</a> 》</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f5e10ad27b704e55a42081c214c92490~tplv-k3u1fbpfcp-zoom-1.image" alt="接口测试用例" title="接口测试用例" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>接口自动化测试收益大</strong>：因为容易实现，维护成本低，有着更高的投入产出比，是每个公司开展自动化测试的首选。</p>
<h3 data-id="heading-8">UI自动化测试（GUI界面层）：</h3>
<p>UI层是用户使用产品的入口，所有功能通过这一层提供给用户，测试工作大多集中在这一层，常见的测试工具有UFT、Robot Framework、Selenium、Appium等；</p>
<h2 data-id="heading-9">什么样的项目适合自动化测试</h2>
<p>性价比：按照测试金字塔模型以及投入/产出比，越向下，回报率越高；</p>
<p>Google的自动化分层投入占比：</p>
<ul>
<li>
<p>小测试（Unit）：占比70%；</p>
</li>
<li>
<p>中测试（Service）：占比20%；</p>
</li>
<li>
<p>大测试（UI）：占比10%；</p>
</li>
</ul>
<p>自动化测试面临的挑战：面临的最大挑战就是变化，因为变化会导致测试用例运行失败，所以需要对自动化脚本不断debug，如何控制成本、降低成本是对自动化测试工具以及人员能力的挑战。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1cfe0bec019e49eaa6869438508d6b5f~tplv-k3u1fbpfcp-zoom-1.image" alt="适合自动化测试的项目" title="适合自动化测试的项目" loading="lazy" referrerpolicy="no-referrer"></p>
<p>像那种做短平快而收钱的项目，自动化测试完全是扯蛋。</p>
<h2 data-id="heading-10">功能测试为什么要做自动化？</h2>
<ul>
<li>
<p>功能测试存在大量的回归测试、大数据量测试。</p>
</li>
<li>
<p>自动化测试更高效、更严格。</p>
</li>
</ul>
<h3 data-id="heading-11">功能自动化测试的条件：</h3>
<ul>
<li>
<p>需求相对稳定</p>
</li>
<li>
<p>冒烟测试通过</p>
</li>
<li>
<p>测试周期长</p>
</li>
</ul>
<h3 data-id="heading-12">PC端常用的功能自动化测试工具</h3>
<ul>
<li>
<p>Selenium：开源工具集，用于**回归功能测试或者系统用例说明，**也可浏览器的兼容性。支持JavaScript、java、C等主流语言</p>
</li>
<li>
<p>Monkey：安装自带的UI测试工具，主要用来对设备上的程序进行压力测试，检测程序多久的时间会发生异常。monkey命令</p>
</li>
<li>
<p>Loadrunner：商业性能测试工具，收费，功能强大，适合做复杂场景的性能测试。java编写测试用例</p>
</li>
<li>
<p>QTP（=》UFT）:商业收费软件，支持web，桌面自动化测试。主要是用于回归测试和测试同一软件的新版本，支持VBScript</p>
</li>
<li>
<p>WinRunner</p>
</li>
<li>
<p>QARun</p>
</li>
<li>
<p>Robot</p>
</li>
</ul>
<p>下篇介绍selenium：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhoulujun.cn%2Fhtml%2FOperation%2Ftest%2F2017_0518_8312.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhoulujun.cn/html/Operation/test/2017_0518_8312.html" ref="nofollow noopener noreferrer">web自动化测试(2):选择selenium优势？与PhantomJS/QTP/Monkey对比</a></p>
<p>同行相关文章推荐：</p>
<p>前端自动化测试 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fwebyouxuan%2Farticle%2Fdetails%2F100668081" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/webyouxuan/article/details/100668081" ref="nofollow noopener noreferrer">blog.csdn.net/webyouxuan/…</a></p>
<p>大前端的自动化工厂（5）—— 基于Karma+Mocha+Chai的单元测试和接口测试 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.51cto.com%2F13869008%2F2175983" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.51cto.com/13869008/2175983" ref="nofollow noopener noreferrer">blog.51cto.com/13869008/21…</a></p>
<p>转载<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhoulujun.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhoulujun.cn/" ref="nofollow noopener noreferrer">本站</a>文章《<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhoulujun.cn%2Fhtml%2FOperation%2Ftest%2F2017_0517_8310.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhoulujun.cn/html/Operation/test/2017_0517_8310.html" ref="nofollow noopener noreferrer">web自动化测试(1):再谈UI发展史与UI、功能自动化测试</a>》,<br>
请注明出处：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.zhoulujun.cn%2Fhtml%2FOperation%2Ftest%2F2017_0517_8310.html" target="_blank" rel="nofollow noopener noreferrer" title="https://www.zhoulujun.cn/html/Operation/test/2017_0517_8310.html" ref="nofollow noopener noreferrer">www.zhoulujun.cn/html/Operat…</a></p></div>  
</div>
            