
---
title: '基于OPENAPI v3 的前后端集成与分析'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0f0a66277b746f89a0219e133c7dd20~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 17 Jul 2021 09:08:14 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0f0a66277b746f89a0219e133c7dd20~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>基于OPENAPI v3 的前后端集成与分析</strong></p>
<h2 data-id="heading-0">什么是OAS</h2>
<p>OpenAPI Specification(简称OAS）为 RESTful API 定义了一个标准的、与语言无关的接口，它允许人类和计算机在不访问源代码、文档或通过网络流量检查的情况下发现和理解服务的功能。正确定义后，消费者可以使用最少的实现逻辑理解远程服务并与之交互，然后，文档生成工具可以使用 OpenAPI 定义来显示 API，代码生成工具可以使用各种编程语言、测试工具和许多其他用例来生成服务器和客户端<sup>[^1]</sup>，截止目前版本3.1.0。</p>
<p>换句话说就是定义一个规范用来描述基于RESTful风格的API，基于API可以对其进行测试，自动生成等其他功能，也就是服务和服务之间的一种“契约”形式。</p>
<h2 data-id="heading-1">OAS 历史</h2>
<p>OAS也被称为Swagger Specification，在2016年后从Swagger Framework中独立出来成为Linux开源项目<sup>[^2]</sup>。</p>
<p>历史时间线：</p>
<ul>
<li>2011年8月11日，Swagger 1.0 首次发布 </li>
<li>2014年9月8日，Swagger 2.0 发布</li>
<li>2015年11月，Swagger拥有者SmartBear Software将Swagger规范捐献给OpenAPI组织，同时还有一个规范的竞争者RAML<sup>[^3]</sup>和API Blueprint<sup>[^4]</sup></li>
<li>2016年1月1日，Swagger Specification名称变更为OpenAPI Specification</li>
<li>2017年7月26日，OpenAPI发布3.0.0版本。</li>
<li>2021年2月17日，OpenAPI发布3.1.0版本。</li>
</ul>
<p>最新参考OAI - <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2FOAI%2Fopenapi-specification%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/OAI/openapi-specification/" ref="nofollow noopener noreferrer">Github Release Note</a></p>
<h2 data-id="heading-2">前后端分离的痛处</h2>
<p>对于前后端分离的原因和技术不做讨论，但是为了更好的讲解痛处，请参考如下内容：</p>
<ol>
<li>为什么要前后端分离： 《<a href="https://link.juejin.cn/?target=https%3A%2F%2Finsights.thoughtworks.cn%2Ffrontend-backend%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://insights.thoughtworks.cn/frontend-backend/" ref="nofollow noopener noreferrer">前、后端分离，谁值得拥有？</a>》</li>
<li>如何进行前后端分离： 《<a href="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fa%2F1190000009329474%3F_ea%3D2038402" target="_blank" rel="nofollow noopener noreferrer" title="https://segmentfault.com/a/1190000009329474?_ea=2038402" ref="nofollow noopener noreferrer">前后端分离实践</a>》</li>
</ol>
<p>言归正传，前后端分离解决了团队分工协作问题，让两端可以只关注自我领域内的知识和内容，减少相互依赖，但同时也带来“沟通”成本上升和如何保证系统之间稳定性的问题。</p>
<p>一个比较常见的场景是，前端团队的工程师和后端团队的工程师拿着笔记本，对着IDE开始商讨API接口实现的功能，路由地址，输入和返回参数，稍微负责任一些的工程师还会约定一些异常场景等，最终达成“口头”协议，待前后端开发完成后进行联调测试，大概率还会在处理/修改一些“细枝末节”的问题。某一天，前端界面一功能请求响应失败，发现原因是后端接口变动导致请求异常但未通知到前端工程师修改相应代码，异或是在接口变动后负责测试的人员，没有考虑到一些特殊的情况。这里暂且称之为前后端分离1.0场景。随着时间的发展，越来越多的人开始对如何保证前后端分离之后的软件质量进行思考，以Martin Fowler等人提出契约测试来使用自动化测试保证API接口的稳定性，同时集成CI/CD进行全生命周期的集成和监控，做到了API监控的自动化<sup>[^5]</sup>。其中衍生出了消费者驱动测试开发（Consumer Driven Contract）和Pact等契约测试框架工具进行实践<sup>[^6]</sup>，这里暂且称之为前后端分离2.0场景。</p>
<p>对于前后端分离有几个技术关键点：</p>
<ul>
<li>选用那种“契约”来描述API接口，是Swagger Spec，RAML Spec，还是以Pact框架为基础的Pact Spec<sup>[^7]</sup>。</li>
<li>如何保证“契约”的约定效力，是基于口头约定的Swagger-UI展现还是基于自动化测试的Pact测试框架。</li>
<li>如何保证“契约”的实时效应，是基于持续集成平台/工具的实时输出，还是团队之前达成默契保持人员沟通顺畅。</li>
</ul>
<p>对于情绪化人的行为不可控的前提下，选择“机器”是不二法则，当然，“制造”复杂而又完美的机器也是要有成本的。</p>
<h2 data-id="heading-3">基于OpenApi Spec + CodeGen + Typescript的一种解决方案</h2>
<p>虽然对于完美实现需求的Pact测试框架来讲，已经能满足目前需要的各种场景和功能。对于一些“小而美”的项目而言，即使在社区提供各种不同语言客户端和服务端之后还是显得略微重了一些，同时增加测试的成本也会给小项目带来不少的负担。所以，有没有一种既能保证一定程度的契约有效性或者说保证契约“部分”正确性的前提下，减少一些开发量？</p>
<p>这里给出一些经验总结：</p>
<ul>
<li>不可缺舍：基于一种规范的API描述，正所谓无规矩不成方圆。</li>
<li>可取舍：基于契约的完备测试，测试的数量往往决定对业务功能覆盖的范围大小，牺牲一部分对业务功能的约束能力。</li>
</ul>
<p>在这里提出一个组合假设：使用OpenAPI规范+Typescript增强Javascript的类型约束和智能感知，来保证API路由和参数的稳定性，不保证业务稳定性，不增加对接口的测试。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f0f0a66277b746f89a0219e133c7dd20~tplv-k3u1fbpfcp-watermark.image" alt="OpenAPI+Typescript.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>步骤1：以SpringBoot作为后端服务启动，并增加SwaggerUI依赖，启动服务后即可登录到SwaggerUI界面来获得最新的接口文档。
<br>
步骤2：使用Swagger官方提供的代码转换工具，将OpenAPI Specification转换为基于Typescript的前端API库。
<br>
步骤3：将前端API库导入到前端项目中，结合Axios或者其他HTTP库使用。</p>
<h2 data-id="heading-4">方案的一些不足之处</h2>
<p>首先，强依赖后端对接口描述的完整性，如对于PathParameter必须强制在Controller中标明。
其次，由于OpenAPI规范中使用Controller其中的方法名作为API路由的唯一值Id，并且是全局唯一，如果在不同的Controller中存在相同名称就可能导致OperationId带有数字后缀，可能导致使用不同的API错误，包括多次编译/重新部署后可能Id相同但实际的API并不形同的问题。
再次，Code Generation工具基于Java以及Java JVM可能对纯前端开发并不友好。</p>
<p>最后，由于没有对API的业务逻辑进行覆盖，缺少了一部分API的稳定性保障，可是尝试使用Pact的方案，请参见文章《<a href="https://link.juejin.cn/?target=https%3A%2F%2Finsights.thoughtworks.cn%2Fabout-contract-test%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://insights.thoughtworks.cn/about-contract-test/" ref="nofollow noopener noreferrer">聊一聊契约测试</a>》，文章中难免有不足之处，欢迎留言指正。</p>
<h2 data-id="heading-5">引用</h2>
<p>[^1]<a href="https://link.juejin.cn/?target=https%3A%2F%2Fswagger.io%2Fspecification%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://swagger.io/specification/" ref="nofollow noopener noreferrer"> Swagger官网介绍</a>
<br>
[^2]<a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FOpenAPI_Specification%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/OpenAPI_Specification/" ref="nofollow noopener noreferrer"> Wiki关于OAS的历史</a>
<br>
[^3]<a href="https://link.juejin.cn/?target=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FRAML_(software)%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://en.wikipedia.org/wiki/RAML_(software)/" ref="nofollow noopener noreferrer"> RESTful API Modeling Language</a>
<br>
[^4]<a href="https://link.juejin.cn/?target=https%3A%2F%2Fapiblueprint.org%2Fdocumentation%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://apiblueprint.org/documentation/" ref="nofollow noopener noreferrer"> Blueprint</a>
<br>
[^5]<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmartinfowler.com%2Fbliki%2FContractTest.html" target="_blank" rel="nofollow noopener noreferrer" title="https://martinfowler.com/bliki/ContractTest.html" ref="nofollow noopener noreferrer"> 契约测试</a>
<br>
[^6]<a href="https://link.juejin.cn/?target=https%3A%2F%2Finsights.thoughtworks.cn%2Fabout-contract-test%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://insights.thoughtworks.cn/about-contract-test/" ref="nofollow noopener noreferrer"> 聊一聊契约测试</a>
<br>
[^7]<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fpact-foundation%2Fpact-specification" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/pact-foundation/pact-specification" ref="nofollow noopener noreferrer"> Pact规范</a>
<br></p></div>  
</div>
            