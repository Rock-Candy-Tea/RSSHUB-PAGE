
---
title: '欲取代绝大多 JavaScript 工具链？Rome 尝鲜'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ebf27e6abbf432cb419a19c34534f01~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 26 May 2021 07:35:12 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ebf27e6abbf432cb419a19c34534f01~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace;letter-spacing:2px;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%;word-break:break-word;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1&#123;font-size:25px;margin-bottom:5px;border-left:5px solid #773098&#125;.markdown-body h1,.markdown-body h2&#123;display:inline-block;font-weight:700;padding-left:10px&#125;.markdown-body h2&#123;font-size:18px;border-left:5px solid #916dd5&#125;.markdown-body h3&#123;font-size:16px;font-weight:700;padding-left:10px;border-left:5px solid #d89cf6&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;border-radius:6px;display:block;margin:20px auto;object-fit:contain;box-shadow:2px 4px 7px #999&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;padding:.2em .5em;font-weight:700;font-size:1em;color:#916dd5;word-break:break-word;overflow-x:auto;background-color:none;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;font-size:12px;padding:16px 12px;margin:0;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#916dd5;font-weight:700;border-bottom:1px solid #916dd5&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#773098&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #916dd5&#125;.markdown-body thead&#123;background-color:#916dd5;color:#fff;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#d89cf6&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #d89cf6;background-color:#f4eeff&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0;line-height:26px&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px;list-style-type:circle&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body b,.markdown-body strong&#123;color:#916dd5;font-weight:700&#125;.markdown-body b:before,.markdown-body strong:before&#123;content:"「"&#125;.markdown-body b:after,.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em,.markdown-body i&#123;color:#916dd5&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本文差点难产而死。因为总结的过程中，多次怀疑本文是对官...</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5ebf27e6abbf432cb419a19c34534f01~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>一个包含希腊斯巴达头盔的罗马项目 Logo</p>
<blockquote>
<p>条条大路通 Rome。在 Rome 还没有发布 NPM 正式版之际。我们围绕 JavaScript 工具链为核心点，来看看前往 Rome 的路上都有什么；以及 Rome 本身，意味着什么？</p>
</blockquote>
<p>二月的最后一天，我在为 “<a href="https://github.com/ningowood/open-source-magazine" target="_blank" rel="nofollow noopener noreferrer">开源爱好者月刊</a>”搜寻本月最新的开源项目时，偶遇一个名叫 Rome 的仓库霸榜，眼前着实一亮。“一个实验性的 JavaScript 工具链”、“包括编译器、lint、格式化程序、捆绑器、测试框架等”以及 “旨在成为与 JavaScript 源码处理相关的所有功能的综合工具” 短短几句话展现了一个宏大的目标。现在，是时候入坑了解一波并在个人能力范围内作一个浅要的分享。</p>
<p>Rome 由就职于 Facebook 同时是 Babel 和 Yarn 作者的 Sebastian McKenzie 主导开源，开源之前，Rome 基本是他的个人项目，现在 Facebook 愿意付薪水让他潜心开发。截止现在（2020 年 04 月初），Rome 的提交记录已经从 70+ 到 600+，贡献者拓展到了 40+ 位，产生了 30+ issues 和 170+ Pull Request。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fcbf22bcf5f84ae0854fadcf1a2e86ca~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>此外，或许也能从侧面呼应我曾在月刊第三期中收录的一句关于 “创业公司和大公司开源出发点有何不同” 的话：大公司可能在一个项目的早期便开源，凭借其号召力希望更多人一起 “贡献” 迭代，初创团队则会在产品相对成熟的时候再开放，希望尽快吸引用户深度“使用”，注重完善产品在工业环境下的综合表现。</p>
<p>正文 & 背景 & 干货开始。</p>
<h2 data-id="heading-0">Rome：从个人项目到 Facebook 新开源</h2>
<p>从官网不难看出，Rome 旨在成为与 JavaScript 源代码处理相关的所有功能的综合工具，其中包括 “编译器、Linter、格式化程序、捆绑器、依赖管理器和测试框架” 等。Rome 源于对整个项目的扩展范围一致性的渴望。</p>
<p>同时，Rome 也来源于 Babel 作者本身对 Babel 的一些不满足而新创，就像 Deno 之于 Node 一样。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d66ecee2bc54b6dad0ad95878163ae3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>本节根据 README.md 和官网首页的介绍，来以问答形式展示 Rome 的背景和想要达到具体目标。</p>
<h3 data-id="heading-1">01、Rome 的一些来源？</h3>
<blockquote>
<p>在计算机科学中只有两件难事：缓存失效和命名。 ——Phil Karlton</p>
</blockquote>
<ul>
<li>立项来源：由 Babel and Yarn 的作者 Sebastian McKenzie 发起，是 React Native 团队的一个项目。</li>
<li>名称来源：因 “通向罗马的所有道路”，“罗马不是一天建成” 和“在罗马时要像罗马人一样”这样的谚语而得名。 这是指整个项目的扩展范围和对一致性的渴望，它始于一个办公室玩笑。</li>
<li>Logo 来源：一个古希腊斯巴达头盔。虽然它不是罗马字母，也不太相关，但看起来比 Galea （罗马士兵的头盔）酷。</li>
</ul>
<h3 data-id="heading-2">02、Rome 的编码架构？</h3>
<blockquote>
<p>在版本控制系统中，monorepo（单声道存储库的音节缩写）是一种软件开发策略，其中许多项目的代码存储在同一存储库中。 截至 2017 年，这种软件工程实践已有十多年的历史，但直到最近才被命名。——Monorepo，维基百科</p>
</blockquote>
<ul>
<li>完全使用 TypeScript 编写，很少使用松散类型。</li>
<li>支持处理 JSX 以及 Flow 和 TypeScript 代码。</li>
<li>self-hosted，可以自己编译自己。</li>
<li>不是现有工具的集合，所有组件都是自定义的，不使用第三方依赖项（对 JavaScript 生态系统进行了重新思考，对整个工具链采用了不依赖第三方库的大胆实现）。</li>
<li>是带有内部软件包的 monorepo 架构以便划定代码边界。</li>
</ul>
<h3 data-id="heading-3">03、Rome 的工作展望？</h3>
<ul>
<li>旨在成为与 JavaScript 源代码处理相关的所有功能的综合工具。</li>
<li>目标是替代许多现有的 JavaScript 工具，但也将提供为其他工具提供自身的集成方案，以根据需要随意使用——例如使用 Rome 编译器作为另一个捆绑程序的插件。</li>
<li>目前关注的领域是 Linter（用于分析源代码以标记编程错误，bug，样式错误和可疑结构的工具），这是将 Rome 变成最容易使用的工具链的目标里阻力最小的一个环节。</li>
</ul>
<h2 data-id="heading-4">微栏：回看 JavaScript 工具链</h2>
<blockquote>
<p>在学习一个工具之前，往往我们应该先去了解这个工具可以用来解决什么样的问题；同样的，当我们遇到一个问题的时候，我们也应该带着这个问题去找工具解决。</p>
<p>**——**阿里巴巴集团 高级前端工程师 叶俊星</p>
</blockquote>
<p>成熟的软件项目必然遵循的良好的开发规范，也拥有属于自身独特的软件开发生命周期，编程实践只占整个开发周期的很小一部分。当一个 JavaScript 软件被建立时通常还会遇到哪些需要解决的问题？这便涉及到了 JavaScript 项目的技术选型，而 JavaScript 生态圈的明星项目数不胜数，以下作一个纵览，不涉及各个工具的具体使用方式。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/42898eadaa214311aa57fea58cc27d2f~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>JavaScript 工具链示意图</p>
<ul>
<li><strong>JS 开发环境</strong>？有 V8、Node 甚至是 Deno 等；</li>
<li><strong>JS 前端框架</strong>？有 Angular、React、Vue、React Native、jQuery 等；</li>
<li><strong>JS 后端框架</strong>？有 Nest、Express、Koa 等；</li>
<li><strong>JS 脚手架</strong>？有 Vue CLI、Angular CLI、Create React App、Yeoman 等；</li>
<li><strong>JS 转译工具</strong>？有 Babel 等；</li>
<li><strong>JS 测试工具</strong>？围绕单元测试、集成测试，有 Mocha、Jasmine、Jest、Karma 等；</li>
<li><strong>JS 调试工具</strong>？有 Chrome DevTools/Firebug/Webkit inspector 等各大主流浏览器、VS Code/WebStorm 等各大编辑器 / IDE 等；</li>
<li><strong>JS 格式规范工具</strong>？有 JSLint、JSHint、ESLint、TSLint 等；</li>
<li><strong>JS 接口联调工具</strong>？有 Axios、Fetch 等；</li>
<li><strong>JS 包管理器</strong>？有 NPM、Yarn、Bower、PNPM 等；</li>
<li><strong>JS 模块加载器</strong>？有 RequireJS、SystemJS、StealJS、ES Module Loader 等；</li>
<li><strong>JS 任务管理工具</strong>？Grunt、Gulp、Webpack 监听文件变化，自动执行任务；</li>
<li><strong>JS 静态化支持</strong>？有 TypeScript、CoffeeScript、Flow、LiveScript 等；</li>
<li><strong>JS 代码后处理工具</strong>？围绕混淆器、缩小器、优化器诸多领域有各种各样的 loader 等；</li>
<li><strong>JS 打包工具</strong>？Webpack、Rollup、Parcel、Browserify 等；</li>
<li><strong>JS 模板引擎</strong>？有 handlebarsjs、etpl、templatejs 甚至各大前端框架内置的模板语法等；</li>
<li><strong>JS 非 Web 框架</strong>？在物联网、区块链、大数据等领域均有相关库支持，本文不涉及。</li>
<li><strong>JS 进程管理</strong>？有 Forever、PM2、StrongLoop Process Manager 等；</li>
<li><strong>......</strong>？甚至编辑器、IDE、CSS 预处理器、代码托管平台、团队开发模式 (纯前端、重后端、前后分离)、WebAssembly、Serverless、JS DevOps 等都可以加到项目的技术选型范围内。</li>
</ul>
<p>因此可以看出，技术选型便是针对能让项目成功运转各个环节寻找相应的解决方案；工作流（Workflow）是所有解决方案融合后的落实流程；而工具链（Toolchain）便是工作流下所有实现方式的汇总，同时一个工具也能代表一个解决方案。</p>
<p>简而言之，JavaScript 工具链便是 JavaScript 工程师在开发过程中会用到的一系列工具。</p>
<h2 data-id="heading-5">浅尝初试 Rome (v0.0.52)</h2>
<p>现在 Rome 并没有直接在 Github 上发布任何版本，但编译后生成的 rome.json 可以看出有一个 v0.0.52 的版本号，处于一个很早期的状态，项目简介也是 “一个实验性的 JavaScript 工具链”。</p>
<p>想要尝试 Rome，就得从以下步骤逐步展开（由于 Rome 没有发布正式版本，这里无需过多涉及如何整合在 package.json 的脚本中使用等工程化过程）。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b1943d853c34dc78713f7217788a248~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>帝国时代里的罗马大军</p>
<p>本章所有 Demo 均在 <a href="https://github.com/hylerrix/demos" target="_blank" rel="nofollow noopener noreferrer">@hylerrix/demos</a> 的 Rome 文件夹中。</p>
<h3 data-id="heading-6">01、git clone rome</h3>
<p>既然 Rome 没有正式发布版本，我们也无法直接从 NPM 上直接安装 Rome。现阶段，Rome 提供了本地安装的方式，只需要克隆到本地并本地编译和本地 NPM 安装即可使用。</p>
<blockquote>
<p>注：安装 Rome 前请确保本地已正常安装 Node 和 NPM</p>
</blockquote>
<h3 data-id="heading-7">02、rome init</h3>
<p>rome init 命令会在当前目录生成一个 rome.json 文件，使用推荐配置会初始化以下内容：</p>
<p>该文件告诉 Rome 至少应为 0.0.52 版本，以便与当前项目一起使用。具体使用文档还在开发中。</p>
<h3 data-id="heading-8">03、rome run index.ts</h3>
<p>rome run 命令将运行传递给它的任何文件，通常与项目的主文件一起使用。目前仍在开发中，可能无法正确处理所有源文件。此时我们为测试 rome run 成功运行，建立一个 index.ts 和 api.ts 文件，如下。</p>
<p>此时，运行如下命令便可以成功使用：</p>
<h3 data-id="heading-9">04、rome lint index.ts</h3>
<p>由于我真的不喜欢在 JavaScript 应用里面写分号，这与主流规范有些不同，所以 rome lint 命令刚好派上了用场：rome 默认需要在 JavaScript 语句结尾写分号。同时在 api.ts 中故意不导出一个 interface 且在 index.ts 中故意将其错误导入，重构后的有错误 index.ts 和 api.ts 以及 rome lint 后执行过程如下：</p>
<p>rome lint 命令在这里提示我们需要加分号并需要在 api.ts 中成功导出 interface。前者可以使用 rome lint index.ts --fix 直接来修理（不会在 api.ts 中添加分号）；后者需要手动修理，但是提供了十分完善的友好提示。</p>
<h3 data-id="heading-10">05、rome compile index.ts</h3>
<p>rome compile 命令将使用一组默认转换来编译文件。由于在开发中，当前此命令没有用于指定转换子集的选项。使用这条命令后，输出的结果已经没有了 interface 的存在。</p>
<h3 data-id="heading-11">06、rome parse index.ts</h3>
<p>rome parse 命令将解析文件并输出格式精美的 AST。</p>
<h3 data-id="heading-12">07、Rome 的更多命令</h3>
<p>除了官网展示的几个命令外，从源码可以看出还有很多内置的命令正在开发，可以从 rome --help 中寻找答案。</p>
<h2 data-id="heading-13">参考资料</h2>
<ul>
<li>[English] <a href="https://github.com/facebookexperimental/rome" target="_blank" rel="nofollow noopener noreferrer">Rome Github Project</a></li>
<li>[English] <a href="https://jasonformat.com/rome-javascript-toolchain/" target="_blank" rel="nofollow noopener noreferrer">Rome, a new JavaScript Toolchain</a></li>
<li>[English] <a href="https://twitter.com/sebmck/status/1232885861135421441" target="_blank" rel="nofollow noopener noreferrer">Rome Official Announcement</a></li>
<li>[English] <a href="https://twitter.com/sebmck/status/1108407803545214977" target="_blank" rel="nofollow noopener noreferrer">Rome Timeline</a></li>
<li>[English] <a href="https://www.infoq.com/news/2020/03/rome-experimental-js-toolchain/" target="_blank" rel="nofollow noopener noreferrer">Facebook Introduces Rome Experimental JavaScript Toolchain</a></li>
<li>[English] <a href="https://podcast.babeljs.io/rome/" target="_blank" rel="nofollow noopener noreferrer">01: Sebastian McKenzie on Babel and the Road to Rome - The Babel Podcast</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/23928404" target="_blank" rel="nofollow noopener noreferrer">前端工具链课（一）—— 包管理工具</a></li>
<li><a href="https://blog.csdn.net/qiwoo_weekly/article/details/104624223" target="_blank" rel="nofollow noopener noreferrer">Rome：Facebook 最新 JS 工具上手</a></li>
</ul>
<h2 data-id="heading-14">总结 & 订阅</h2>
<p>经过近几年的蓬勃发展，JavaScript 早已不再局限于 “前端开发” 的领域中。因此本篇写作的角度并不是仅仅以前端开发为主体探索，而是将 JavaScript 本身抽离出来，这也是自己逐步理清职业发展的一个重要改变。</p>
<p>本文通过学习和写作分享对 Rome 进行了简要的了解，但这还仅仅是入门。自己对 Babel 本身并不熟，还有很多学习过程中产生的疑惑都无法现在进行合适的解答，比如 “Rome 和 Babel 的具体异同”、“如何看待 Rome 仓库使用 Git 跟踪 Node Modules”、“Rome 替代现有工具或进行集成方案的具体原理” 以及 “Rome 的打包流程有何特点” 等，挖个坑可以一起交流。</p>
<p>无论最终是否使用 Rome，能引发对 JavaScript 工具链的重新思考也会很有收获。</p>
<p>最后，感谢你的阅读，公众号 (@ningowood) 及配套群聊欢迎加入，同时欢迎给如期更新了三期，即将支持线上 UI 界面浏览并提供更多拓展功能的 “开源爱好者月刊（<a href="https://github.com/ningowood/open-source-magazine" target="_blank" rel="nofollow noopener noreferrer">@ningowood/open-source-magazine</a>）” 仓库点个 Star 吧！（Github 好久没涨粉丝了，也欢迎关注我~）</p></div>  
</div>
            