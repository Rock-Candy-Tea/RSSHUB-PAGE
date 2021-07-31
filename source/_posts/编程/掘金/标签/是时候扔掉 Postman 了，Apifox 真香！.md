
---
title: '是时候扔掉 Postman 了，Apifox 真香！'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9c7c2d3867f454e986a864b3938a137~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Fri, 30 Jul 2021 23:15:57 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9c7c2d3867f454e986a864b3938a137~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">是时候扔掉 Postman 了，Apifox 真香！</h1>
<blockquote>
<p>作为开软件开发从业者，接口调试是必不可少的一项技能，在这方面 Postman 做的非常出色。但是在整个软件开发过程中，接口调试只是其中的一部分，还有很多事情 Postman 无法完成，或者<code>无法高效完成</code>，比如：接口文档定义、Mock 数据、接口自动化测试等等。Apifox 就是为了解决这个问题而生的。</p>
</blockquote>
<h2 data-id="heading-1">接口管理现状</h2>
<h3 data-id="heading-2">一、常用解决方案</h3>
<ol>
<li>使用 Swagger 管理接口文档</li>
<li>使用 Postman 调试接口</li>
<li>使用 RAP 等工具 Mock 数据</li>
<li>使用 JMeter 做接口自动化测试</li>
</ol>
<h3 data-id="heading-3">二、存在的问题</h3>
<p>维护不同工具之间数据一致性非常困难、低效。并且这里不仅仅是工作量的问题，更大的问题是多个系统之间数据不一致，导致协作低效、频繁出问题，开发测试人员痛苦不堪。</p>
<ol>
<li>开发人员在 Swagger 定义好文档后，接口调试的时候还需要去 Postman 再定义一遍。</li>
<li>前端开发 Mock 数据的时候又要去 RAP 定义一遍，还需要手动设置 Mock 规则。</li>
<li>测试人员需要去 JMeter 再定义一遍。</li>
<li>前端根据 RAP Mock 出来的数据开发完，后端根据 Swagger 定义的接口文档开发完，各自都试测试通过了，本以为可以马上上线，结果一对接发现各种问题：
<ul>
<li>开发过程中接口变更了，只修改了 Swagger，但是没有及时同步修改 RAP。</li>
<li>后端开发的接口数据类型和文档不一致，肉眼难以发现问题。</li>
</ul>
</li>
<li>同样，测试在 JMeter 写好的测试用例，真正运行的时候也会发现各种不一致。</li>
<li>时间久了，各种不一致会越来越严重。</li>
</ol>
<h2 data-id="heading-4">Apifox 解决方案</h2>
<h3 data-id="heading-5">一、如何解决这些问题</h3>
<h4 data-id="heading-6">1、Apifox 定位</h4>
<p><code>Apifox = Postman + Swagger + Mock + JMeter</code></p>
<p>通过一套系统、一份数据，解决多个系统之间的数据同步问题。只要定义好接口文档，接口调试、数据 Mock、接口测试就可以直接使用，无需再次定义；接口文档和接口开发调试使用同一个工具，接口调试完成后即可保证和接口文档定义完全一致。高效、及时、准确！</p>
<h4 data-id="heading-7">2、Apifox 宗旨</h4>
<p>节省研发团队的每一分钟！</p>
<h4 data-id="heading-8">3、Apifox 功能</h4>
<ol>
<li><strong>接口设计</strong>：Apifox 接口文档遵循 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fopenapi.apifox.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://openapi.apifox.cn/" ref="nofollow noopener noreferrer">OpenApi</a> 3.0 (原 Swagger)、<a href="https://link.juejin.cn/?target=https%3A%2F%2Fjson-schema.apifox.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://json-schema.apifox.cn/" ref="nofollow noopener noreferrer">JSON Schema</a> 规范的同时，提供了非常好用的<code>可视化</code>文档管理功能，零学习成本，非常高效。并且支持在线分享接口文档。</li>
<li><strong>数据模型</strong>：可复用的数据结构，定义接口<code>返回数据结构</code>及<code>请求参数数据结构</code>（仅 JSON 和 XML 模式）时可直接引用。支持模型直接嵌套引用，直接 JSON/XML 智能导入，支持 oneOf、allOf 等高级组合模式。</li>
<li><strong>接口调试</strong>：Postman 有的功能，比如环境变量、前置/后置脚本、Cookie/Session 全局共享 等功能，Apifox 都有，并且比 Postman 更高效好用。接口运行完之后点击<code>保存为用例</code>按钮，即可生成<code>接口用例</code>，后续可直接运行接口用例，无需再输入参数，非常方便。自定义脚本 100% 兼容 Postman 语法，并且支持运行javascript、java、python、php、js、BeanShell、go、shell、ruby、lua等各种语言代码。</li>
<li><strong>接口用例</strong>：通常一个接口会有多种情况用例，比如<code>参数正确</code>用例、<code>参数错误</code>用例、<code>数据为空</code>用例、<code>不同数据状态</code>用例等等。运行接口用例时会自动校验数据正确性，用接口用例来调试接口非常高效。</li>
<li><strong>接口数据 Mock</strong>：内置 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fmockjs.com%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://mockjs.com/" ref="nofollow noopener noreferrer">Mock.js</a> 规则引擎，非常方便 mock 出各种数据，并且可以在定义数据结构的同时写好 mock 规则。支持添加“期望”，根据请求参数返回不同 mock 数据。最重要的是 Apifox <code>零配置</code> 即可 Mock 出非常人性化的数据，具体在本文后面介绍。</li>
<li><strong>数据库操作</strong>：支持读取数据库数据，作为接口请求参数使用。支持读取数据库数据，用来校验(断言)接口请求是否成功。</li>
<li><strong>接口自动化测试</strong>：提供接口集合测试，可以通过选择接口（或接口用例）快速创建测试集。目前接口自动化测试更多功能还在开发中，敬请期待！目标是： JMeter 有的功能基本都会有，并且要更好用。</li>
<li><strong>快捷调试</strong>：类似 Postman 的接口调试方式，主要用途为临时调试一些<code>无需文档化</code>的接口，无需提前定义接口即可快速调试。</li>
<li><strong>代码生成</strong>：根据接口及数据数据模型定义，系统自动生成<code>接口请求代码</code>、<code>前端业务代码</code>及<code>后端业务代码</code>。</li>
<li><strong>团队协作</strong>：Apifox 天生就是为团队协作而生的，接口云端实时同步更新，成熟的<code>团队/项目/成员权限</code>管理，满足各类企业的需求。</li>
</ol>
<h3 data-id="heading-9">二、Apifox 做的不仅仅是数据打通</h3>
<p>如果你认为 Apifox 只做了数据打通，来提升研发团队的效率，那就错了。Apifox 还做了非常多的创新，来提升开发人员的效率。</p>
<h4 data-id="heading-10">1、接口支持“用例管理”</h4>
<p>通常一个接口会有多种情况用例，比如 <code>正确用例</code> <code>参数错误用例</code> <code>数据为空用例</code> <code>不同数据状态用例</code>。定义接口的时候定义好这些不同状态的用例，接口调试的时候直接运行，非常高效。</p>
<h4 data-id="heading-11">2、“数据模型”定义、引用</h4>
<p>可以独立定义数据模型，接口定义时可以直接引用数据模型，数据模型之间也可以相互引用。同样的数据结构，只需要定义一次即可多处使用；修改的时候只需要修改一处，多处实时更新，避免不一致。</p>
<h4 data-id="heading-12">3、调试时“自动校验”数据结构</h4>
<p>使用 Apifox 调试接口的时候，系统会根据接口文档里的定义，自动校验返回的数据结构是否正确，无需通过肉眼识别，也无需手动写断言脚本检测，非常高效！</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a9c7c2d3867f454e986a864b3938a137~tplv-k3u1fbpfcp-zoom-1.image" alt="Apifox 自动校验数据结构" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-13">4、“可视化”设置断言</h4>
<p>设置断言：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e123ff65962645209d024f0f9709d57e~tplv-k3u1fbpfcp-zoom-1.image" alt="Apifox 设置断言" loading="lazy" referrerpolicy="no-referrer"></p>
<p>运行后，查看断言结果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/244fa3a7f038408198f27140ccc9feae~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-14">5、“可视化”设置提取变量</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/403260b25e92485b8c5653524bdadb14~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-15">6、支持数据库操作</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fa21deaf3682422db8ba8a6bc98d6ed1~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-16">7、“零配置”Mock 出非常人性化的数据</h4>
<p>先放一张图对比下 Apifox 和其他同类工具 <code>零配置</code> mock 出来的数据效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5f03f70c89bc49fca7ee0c822a1a2ea5~tplv-k3u1fbpfcp-zoom-1.image" alt="Apifox Mock 数据结果对比同类工具" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看出 Apifox <code>零配置</code> Mock 出来的数据和真实情况是非常接近的，前端开发可以直接使用，而无需再手动写 mock 规则。</p>
<p><strong>Apifox 如何做到<code>高效率</code>、<code>零配置</code>生成非常人性化的 mock 数据</strong></p>
<ol>
<li>Apifox 根据接口定义里的数据结构、数据类型，自动生成 mock 规则。</li>
<li>Apifox 内置智能 mock 规则库，根据字段名、字段数据类型，智能优化自动生成的 mock 规则。如：名称包含字符串<code>image</code>的<code>string</code>类型字段，自动 mock 出一个图片地址 URL；包含字符串<code>time</code>的<code>string</code>类型字段，自动 mock 出一个时间字符串；包含字符串<code>city</code>的<code>string</code>类型字段，自动 mock 出一个城市名。</li>
<li>Apifox 根据内置规则，可自动识别出图片、头像、用户名、手机号、网址、日期、时间、时间戳、邮箱、省份、城市、地址、IP 等字段，从而 Mock 出非常人性化的数据。</li>
<li>除了内置 mock 规则，用户还可以自定义规则库，满足各种个性化需求。支持使用 <code>正则表达式</code>、<code>通配符</code> 来匹配字段名自定义 mock 规则。</li>
</ol>
<h4 data-id="heading-17">8、代码自动生成</h4>
<p>根据接口模型定义，自动生成各种语言/框架（如 TypeScript、Java、Go、Swift、ObjectiveC、Kotlin、Dart、C++、C#、Rust 等）的业务代码（如 Model、Controller、单元测试代码等）和接口请求代码。目前 Apifox 支持 130 种语言及框架的代码自动生成。</p>
<p>更重要的是：你可以通过<code>自定义代码模板</code>来生成符合自己团队的架构规范的代码，满足各种个性化的需求。</p>
<h4 data-id="heading-18">9、导入、导出</h4>
<ol>
<li>支持导出 <code>OpenApi (Swagger)</code>、<code>Markdown</code>、<code>Html</code> 等数据格式，因为可以导出<code>OpenApi</code>格式数据，所以你可以利用 OpenApi (Swagger) 丰富的生态工具完成各种接口相关的事情。</li>
<li>支持导入 <code>OpenApi (Swagger)</code>、<code>Postman</code>、<code>HAR</code>、<code>RAML</code>、<code>RAP2</code>、<code>YApi</code>、<code>Eolinker</code>、<code>NEI</code>、<code>DOClever</code>、<code>ApiPost</code> 、<code>Apizza</code> 、<code>ShowDoc</code>、<code>API Blueprint</code>、<code>I/O Docs</code>、<code>WADL</code>、<code>Google Discovery</code>等数据格式，方便旧项目迁移。</li>
</ol>
<h3 data-id="heading-19">三、后续功能规划</h3>
<ol>
<li>接口文档公开对外发布。</li>
<li>接口性能测试支持（类似 JMeter）。</li>
<li>支持插件市场，可以自己开发插件。</li>
<li>支持更多接口协议，如<code>GraphQL</code>、<code>websocket</code>等。</li>
<li>支持离线使用，项目可选择在线同步（团队协作）还是仅本地存储（单机离线使用）。</li>
</ol>
<h3 data-id="heading-20">四、更多 Apifox 功能截图</h3>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/991c2de3c55040f18f58f9041945e3d1~tplv-k3u1fbpfcp-zoom-1.image" alt="接口调试" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1208c33bdfa947b0b221bdc4e7c48ecd~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3bcb0096f1634f75871dbb6c923fa205~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/618fc9853cc9452cac7553c495947cb0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/29288f024df94983b7da1392018faaa8~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b48e031fc004e528ccced8db5e551af~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/264b7c765fc8452691b2b7b9bb9f77c4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b62a5a37ba824b01ae909d5537fd0243~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6c39f32e4ea463a9e3704968a56445a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c997d9730834708a9ce1a2019ea220d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/49a5508a35884333b4788e7da8b70f51~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62792e7889f04989ab03e45efaec85b0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f44fbaab80504ee7be8ea93b0bd99b46~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6c9197b4caa64faf8e74b22e58d270ea~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d999bd07c9b4c27bcdc655b4a8262c3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c8b603d80fc24e6583a16a761ece711d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45670439fce2467ab0dd4a3c9539f80e~tplv-k3u1fbpfcp-zoom-1.image" alt="Apifox 多种主题色可选" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-21">五、 Apifox 下载地址</h3>
<p>请访问 Apifox 官网下载：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.apifox.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.apifox.cn/" ref="nofollow noopener noreferrer">www.apifox.cn/</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.apifox.cn%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://www.apifox.cn/" ref="nofollow noopener noreferrer">接口文档工具</a></p>
<blockquote>
<p>本文由博客一文多发平台 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fopenwrite.cn%3Ffrom%3Darticle_bottom" target="_blank" rel="nofollow noopener noreferrer" title="https://openwrite.cn?from=article_bottom" ref="nofollow noopener noreferrer">OpenWrite</a> 发布！</p>
</blockquote></div>  
</div>
            