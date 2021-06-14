
---
title: '前端历史回顾：基石（万维网 & ECMAScript）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94bb5172d71444349b851678ad185a6c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 13 Jun 2021 07:57:15 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94bb5172d71444349b851678ad185a6c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第1天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<p>开发者专注于使用技术创造事物，在技术革新和产品迭代中奋勇前行；爱好者却拥有另一种视角，对行业的陌生反而激发起好奇心，想要试着把这东西从古至今的发展脉络摸索清楚。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94bb5172d71444349b851678ad185a6c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">万维网诞生</h1>
<blockquote>
<p>“我只要把超文本系统和<a href="https://zh.wikipedia.org/wiki/%E4%BC%A0%E8%BE%93%E6%8E%A7%E5%88%B6%E5%8D%8F%E8%AE%AE" target="_blank" rel="nofollow noopener noreferrer">传输控制协议</a>、<a href="https://zh.wikipedia.org/wiki/%E5%9F%9F%E5%90%8D%E7%B3%BB%E7%BB%9F" target="_blank" rel="nofollow noopener noreferrer">域名系统</a>结合在一起，然後─哒哒！─就有了万维网”</p>
</blockquote>
<p>经过70/80年代的飞速发展，个人计算机已经普及，人们在个人设备上编辑文档、绘图、游戏，享受着单机世界。虽然互联网早已出现，然而局限复杂的拨号流程、单调的使用场景，没能让它流行起来。</p>
<p>直到1991年，Tim Berners-Lee 发明万维网，创造出第一个浏览器以及第一个网页服务器。打开浏览器浏览网页，彻底颠覆人们使用互联网的方式。</p>
<p>网页中的文本和普通文本可不一样，它能包含链接，点击链接就能跳转到另一个网页，这种链接称为超链接（Hyperlink），这些超链接构成巨大的信息互联网络。听起来很厉害，这种能包含超链接的文本也有一个厉害的名字——超文本（Hypertext）。</p>
<p>要被超链接检索到，每个网页需要一个唯一的地址，这个地址叫“统一资源定位器”（URL），比如 <a href="https://juejin.cn/frontend" target="_blank">juejin.cn/frontend</a> 就是一个不错的URL；当你访问一个站点时，计算机首先会做 DNS 查找确定域名对应的 IP 地址，再由浏览器开启一个默认端口为80的 TCP 连接；通过 TCP 连接到目标地址的 Web 服务器之后，要告知服务器返回路径对应的页面，这就需要应用层协议出马了，于是 Tim 提出了 HTTP/1.0（HyperText Transfer Protocol）作为 Web 通信协议；服务器解析 HTTP 内容返回对应的页面，“请求-响应”完成。</p>
<p>浏览器获取到的只是使用 ASCII 或 UTF-8 编码的普通文本，如何区分文本中哪些是链接哪些是内容呢？必须得有一种标记方法，于是 Tim 开发了超文本标记语言 HTML（HyperText Markup Language）。浏览器解析 HTML 显示出内容，“渲染”完成。</p>
<p>万维网+浏览器+网页服务器，信息互联有了地基，互联网时代开启。</p>
<h1 data-id="heading-1">ECMAScript</h1>
<p>1995年，Netscape 的 Brendan Eich 接受公司指派耗时 10 天创造了 JavaScript 语言。一种<strong>简单易用</strong>的编程语言，它担负着「快速上手实现网页交互」的使命诞生。</p>
<p>它是如此不凡。C 语言教授它基本语法；Java 语言教育它“万物皆对象”，却没传授“面向对象”那一套武功心得，毕竟对这位追求简单的新朋友来说太过繁琐；Schema 语言告诉它函数要作为“第一等公民”；最后 Self 语言用“原型链实现继承”点拨它模拟面向对象编程。这样一来，它可以按顺序描述步骤，也可以把逻辑抽象到函数里重复调用，还可以搞定“封装、继承和多态”。是的，它是同时具有面向过程编程、面向对象编程、函数式编程基因的新语言。</p>
<p>它又是如此简单。无需指定变量类型，JavaScript解释器会灵活变通；不用了解内存分配和回收，JavaScript 解释器会搞定一切；融合面向对象编程，却不必了解类、泛型、重写、重载、接口等概念。JavaScript 解释器简化了大量工作，使用者得以专注于快速创造。</p>
<p>1997年，为了结束 Netscape 的 JavaScript，微软的 JScript 和 CEnvi 的 ScriptEase 三足鼎立无法互用的局面，ECMA 协调三方成立工作组，为网页交互语言确定统一标准：ECMA-262标准，并将标准语言称为 ECMAScript。</p>
<p>ECMAScript 首版于1997年6月发表；1999年发布的 ES3 增加大量语言特性如正则表达式、异常处理；2008年准备发布的 ES4 因改变过大难以统一各方意见最终胎死腹中；2009年发布的 ES5 增加严格模式，扩展原生对象（如加入getter/setter），澄清前一版本中模糊的规范；2011年 ES5.1 版本发布并成为 ISO 标准。</p>
<h2 data-id="heading-2">ECMAScript 2015</h2>
<p>2015年，里程碑来临。</p>
<p>ECMAScript 2015发布，它也被称为ES6，这一版本改变巨大：</p>
<ul>
<li>块作用域和 <code>const/let</code></li>
<li><code>Class</code></li>
<li><code>Module</code></li>
<li><code>Arrow Function</code></li>
<li><code>Iterator and for...of</code>，可迭代对象展开语法（Spread syntax）</li>
<li><code>Generator</code></li>
<li><code>Symbol</code></li>
<li><code>Promise</code></li>
<li><code>Proxy/Reflect</code></li>
<li>模板字符串（Template literals）</li>
<li>函数参数强化：剩余参数（Rest parameters），默认参数值（Default parameters）</li>
<li>解构赋值</li>
<li>集合<code>Map/Set/WeakMap/WeakSet</code></li>
<li>内置对象扩展</li>
<li>类型化数组（TypedArray）：二进制数据缓冲区</li>
<li>优化尾调用（然而大多数平台都没有实现）</li>
</ul>
<h2 data-id="heading-3">ECMAScript 版本制定流程</h2>
<p>2015 也是 ECMAScript 流程规范化的一个分水岭，从 2015 开始：</p>
<ul>
<li>TC39 组织（ECMA第39号技术委员会）负责  ECMAScript 规范的制定和发布，组织成员包括各大 JS 引擎厂商员工以及其他有名望的开发者</li>
<li>新版本以 “ECMAScript+年份” 命名</li>
<li>确定标准制定流程：
<ul>
<li>Stage 0: Strawman，以 PR 形式提交新特性描述到 <a href="https://github.com/tc39/ecma262" target="_blank" rel="nofollow noopener noreferrer">github.com/tc39/ecma26…</a>；</li>
<li>Stage 1: Proposal，初步编写标准并且实现 Demo 或 Polyfill；目的是确定解决方案以及潜在的难点；</li>
<li>Stage 2: Draft，初始化规范描述，并需要有两个实验性实现；目的是生成「使用正式语言准确描述的语法和语义」；</li>
<li>Stage 3: Candidate，完成规范描述并通过审查者和 ECMAScript 规范的编辑们确认；目的是优化和改进规范；</li>
<li>Stage4: Finished，完整的 Test262 测试，有至少两个实际的实现案例（比如在V8，JavaScriptCore或者SpiderMonkey中实现），提交 PR 到<a href="https://github.com/tc39/ecma262" target="_blank" rel="nofollow noopener noreferrer">tc39/ecma262</a>；目的是确认规范已准备好加入 ECMAScript 标准中。到达 Stage4 的提案基本确定会在未来的版本中出现，因此 Stage 4 提案集合也被称为 ES Next；</li>
<li>通过ECMA大会表决通过后提案正式加入标准</li>
</ul>
</li>
</ul>
<h2 data-id="heading-4">ECMAScript 版本迭代概览</h2>
<p>ECMAScript 2016，新增少量特性和语法：</p>
<ul>
<li>幂运算符 <code>2 ** 5</code></li>
<li><code>Array.prototype.includes</code></li>
</ul>
<p>ECMAScript 2017，新增少量特性和语法：</p>
<ul>
<li>增加 <code>async/await</code></li>
<li>增加<code>Object</code>静态方法<code>values/entries/getOwnPropertyDescriptors</code></li>
<li>增加<code>String padding</code>相关方法</li>
<li>移除<code>arguments.caller</code></li>
</ul>
<p>ECMAScript 2018，新增少量特性和语法：</p>
<ul>
<li>异步迭代器</li>
<li>对象属性<code>rest/spread</code></li>
<li><code>Promise.prototype.finally</code></li>
</ul>
<p>ECMAScript 2019，新增少量特性和语法：</p>
<ul>
<li><code>Array.prototype.&#123;flat,flatMap&#125;</code></li>
<li><code>Object.fromEntries</code></li>
<li>增加 <code>String trimming</code> 相关方法</li>
</ul>
<p>ECMAScript 2020，新增特性和语法：</p>
<ul>
<li>增加 BigInt 类型</li>
<li>可选链操作符（Optional changing operator <code>?.</code>）</li>
<li>空值合并操作符（nullish coalescing operator<code>??</code>）</li>
<li><code>String.prototype.matchAll</code></li>
<li><code>Promise.allSettled</code></li>
<li><code>globalThis</code></li>
</ul>
<p>ECMAScript 2021，新增特性和语法</p>
<ul>
<li>WeakReferences</li>
<li>Logical Assignment</li>
<li><code>String.prototype.replaceAll</code></li>
<li><code>Promise.any</code></li>
<li>numeric separators</li>
</ul>
<p>ECMAScript 2022</p>
<ul>
<li>增加类成员访问权限</li>
<li>顶层 await</li>
</ul>
<p><a href="https://github.com/tc39/proposals/blob/master/finished-proposals.md" target="_blank" rel="nofollow noopener noreferrer">proposals/finished-proposals.md</a> 包含 Stage 4 的所有提案，每一份提案都有关于提供动机、解决方案、使用方式、当前状态的描述，可以说是追踪 ES 更新的直接资源。</p>
<p>在 <a href="https://github.com/tc39/proposals" target="_blank" rel="nofollow noopener noreferrer">tc39/proposals</a> 中可以查询到当前所有提案。</p>
<h2 data-id="heading-5">Babel</h2>
<p>随着ES版本迭代，各JS运行平台也会跟进实现，然而平台的步调并非完全一致，用户对平台的更新也不一定及时，因此需要做代码兼容。</p>
<p><a href="https://kangax.github.io/compat-table/es6/" target="_blank" rel="nofollow noopener noreferrer">ECMAScript 6 compatibility table (kangax.github.io)</a> 是一个非常不错的开源项目，罗列 ES 各版本的功能点以及各平台支持情况，很棒的查询工具。</p>
<p><a href="https://github.com/babel/babel" target="_blank" rel="nofollow noopener noreferrer">Babel</a> 能够将用 ES6+ 写成的代码转换成等效的低版本代码，将代码解析成 AST 转译生成目标代码。Babel 可以转译语法但不会转译 API（内置对象及对象方法），这一部分需要配合 <code>core-js</code>和<code>regenerator-runtime</code> 提供的 polyfill 使用。</p>
<p>在 babel、core-js、regenerator 这些开源项目的贡献下，广大前端开发者能够用最新的语法和特性实现上层应用，而不必劳心于平台兼容问题。</p>
<h2 data-id="heading-6">现在和未来</h2>
<p>JavaScript 仍是一位 90 后青年，最初的他有着简单亲和的性格，被大众喜爱着，当然有些时候他也有一些怪异的行为，让人感叹他不如Java/C这些大哥成熟；随着时代发展，硬件能力飞速强大，JavaScript 需要有更强大的力量支撑起大型项目，于是他谦虚学习其他语言优秀的设计思想，同时努力强化自身的异步特性，有条不紊地贴近时代需求。这一切得益于规范的持续有序推进。</p>
<p>当然人们总期望他能做的更多，比如能做到类 Java 的面向对象支持、静态类型系统，于是就有了 TypeScript；比如能提高运行效率，解释器+JIT还不够快，能用编译器那是最好，于是就有了 WebAssembly。前端社区总是充满了热情的思考者和行动者，年轻但朝气蓬勃。</p>
<h1 data-id="heading-7">参考资料</h1>
<p><a href="http://www.ruanyifeng.com/blog/2011/06/birth_of_javascript.html" target="_blank" rel="nofollow noopener noreferrer">Javascript诞生记 - 阮一峰的网络日志 (ruanyifeng.com)</a></p>
<p><a href="https://es6.ruanyifeng.com/#docs/intro" target="_blank" rel="nofollow noopener noreferrer">ECMAScript 6 简介 - ECMAScript 6入门 (ruanyifeng.com)</a></p>
<p><a href="https://www.bilibili.com/video/BV1EW411u7th?p=30" target="_blank" rel="nofollow noopener noreferrer">【计算机科学速成课】- Crash Course Computer Science_哔哩哔哩_bilibili</a></p>
<p><a href="https://tc39.es/process-document/" target="_blank" rel="nofollow noopener noreferrer">The TC39 Process</a></p>
<p><a href="https://github.com/tc39/how-we-work/blob/master/champion.md" target="_blank" rel="nofollow noopener noreferrer">how-we-work/champion.md at master · tc39/how-we-work (github.com)</a></p></div>  
</div>
            