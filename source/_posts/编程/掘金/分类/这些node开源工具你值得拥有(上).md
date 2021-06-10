
---
title: '这些node开源工具你值得拥有(上)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13cecaabad724fc48e3f4be25db9fd19~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 10 Jun 2021 03:27:05 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13cecaabad724fc48e3f4be25db9fd19~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13cecaabad724fc48e3f4be25db9fd19~tplv-k3u1fbpfcp-watermark.image" alt="图怪兽_1828c60beb9acefd1a469d3dc0dff57f_36412.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>前言：文章的灵感来源于，社群中某大佬分享一个自己耗时数月维护的github项目 <a href="https://github.com/huaize2020/awesome-nodejs/blob/main/README-zh-CN.md" target="_blank" rel="nofollow noopener noreferrer"><code>awesome-nodejs</code> </a>。或许你跟我一样会有一个疑惑，github上其实已经有个同类型的awesome-nodejs库且还高达41k⭐，重新维护一个新的意义何在？ 当你深入对比后，本质上还是有差别的，一个是分类体系粒度更细，其次是对中文更友好的翻译维护，也包括了对国内一些优秀的开源库的收录。最后我个人认为通过自己梳理，也能更好地做复盘和总结</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d994184d282948b4aaea12f156db4078~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>通过阅读 <a href="https://github.com/huaize2020/awesome-nodejs/blob/main/README-zh-CN.md" target="_blank" rel="nofollow noopener noreferrer"><code>awesome-nodejs</code> </a> 库的收录，我抽取其中一些应用场景比较多的分类，通过分类涉及的应用场景跟大家分享工具</p>
<h3 data-id="heading-0">1.Git</h3>
<h4 data-id="heading-1">1.1 应用场景1: 要实现git提交前 eslint 校验和 commit 信息的规范校验？</h4>
<p>可以使用以下工具：</p>
<ul>
<li><a href="https://github.com/typicode/husky" target="_blank" rel="nofollow noopener noreferrer"><code>husky</code></a> - 现代化的本地Git钩子使操作更加轻松</li>
<li><a href="https://github.com/observing/pre-commit" target="_blank" rel="nofollow noopener noreferrer"><code>pre-commit</code></a> - 自动在您的git储存库中安装git pre-commit脚本，该脚本在pre-commit上运行您的npm test。</li>
<li><a href="https://github.com/yyx990803/yorkie" target="_blank" rel="nofollow noopener noreferrer"><code>yorkie</code></a> 尤大改写的yorkie，yorkie实际是fork husky，让 Git 钩子变得简单(在 vue-cli 3x 中使用)</li>
</ul>
<h4 data-id="heading-2">1.2 应用场景2: 如何通过node拉取git仓库？（可用于开发脚手架）</h4>
<p>可以使用以下工具：</p>
<ul>
<li><a href="https://gitlab.com/flippidippi/download-git-repo" target="_blank" rel="nofollow noopener noreferrer"><code>download-git-repo</code></a> - 下载和提取Git仓库 (支持GitHub, GitLab, Bitbucket)。</li>
</ul>
<h4 data-id="heading-3">1.3 应用场景3: 如何在终端看git 流程图？</h4>
<p>可以使用以下工具：</p>
<ul>
<li><a href="https://github.com/nicoespeon/gitgraph.js/tree/master/packages/gitgraph-node" target="_blank" rel="nofollow noopener noreferrer"><code>gitgraph</code></a> -  在 Terminal 绘制 git 流程图（支持浏览器、React）。</li>
</ul>
<h4 data-id="heading-4">1.4 其他</h4>
<ul>
<li><a href="https://github.com/IonicaBizau/git-url-parse" target="_blank" rel="nofollow noopener noreferrer"><code>git-url-parse</code></a> - 高级别git解析。</li>
<li><a href="https://github.com/repo-utils/giturl" target="_blank" rel="nofollow noopener noreferrer"><code>giturl</code></a> - 将Git链接转化成Web链接。</li>
</ul>
<h3 data-id="heading-5">2.环境</h3>
<h4 data-id="heading-6">2.1 应用场景1: 如何根据不同环境写入不同环境变量？</h4>
<p>可以使用以下工具：</p>
<ul>
<li><a href="https://github.com/kentcdodds/cross-env" target="_blank" rel="nofollow noopener noreferrer"><code>cross-env</code></a> -   跨平台环境脚本的设置，你可以通过一个简单的命令（设置环境变量）而不用担心设置或者使用环境变量的平台。</li>
<li><a href="https://github.com/motdotla/dotenv" target="_blank" rel="nofollow noopener noreferrer"><code>dotenv</code></a> -    从 .env文件 加载用于nodejs项目的环境变量。</li>
<li><a href="https://cli.vuejs.org/zh/guide/mode-and-env.html#%E6%A8%A1%E5%BC%8F" target="_blank" rel="nofollow noopener noreferrer"><code>vue-cli --mode</code></a> -   可以通过传递 --mode 选项参数为命令行覆写默认的模式</li>
</ul>
<h3 data-id="heading-7">3.NPM</h3>
<h4 data-id="heading-8">3.1 应用场景1: 如何切换不同npm源？</h4>
<p>可以使用以下工具：</p>
<ul>
<li><a href="https://github.com/Pana/nrm" target="_blank" rel="nofollow noopener noreferrer"><code>nrm</code></a> -    快速切换npm注册服务商，如npm、cnpm、nj、taobao等，也可以切换到内部的npm源</li>
<li><a href="https://github.com/pnpm/pnpm" target="_blank" rel="nofollow noopener noreferrer"><code>pnpm</code></a> -  可比yarn，npm 更节省了大量与项目和依赖成比例的硬盘空间</li>
</ul>
<h4 data-id="heading-9">3.2 应用场景2: 如何读取package.json信息？</h4>
<p>可以使用以下工具：</p>
<ul>
<li><a href="https://github.com/sindresorhus/read-pkg-up" target="_blank" rel="nofollow noopener noreferrer"><code>read-pkg-up </code></a> -   读取最近的package.json文件。</li>
<li><a href="https://github.com/indexzero/node-pkginfo" target="_blank" rel="nofollow noopener noreferrer"><code>node-pkginfo </code></a> -  从package.json读取属性的简单方法。</li>
</ul>
<h4 data-id="heading-10">3.3 应用场景3：如何查看当前package.json依赖允许的更新的版本</h4>
<p>可以使用以下工具：</p>
<ul>
<li><a href="https://github.com/raineorshine/npm-check-updates" target="_blank" rel="nofollow noopener noreferrer"><code>npm-check-updates  </code></a> -   找当前package.json依赖允许的更新的版本。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/df95ef7e59274b0ab350a12f5db10e27~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-11">3.4 应用场景4：如何同时运行多个npm脚本</h4>
<blockquote>
<p>通常我们要运行多脚本或许会是这样<code>npm run build:css && npm run build:js</code> ，设置会更长通过<code>&</code>来拼接</p>
</blockquote>
<p>可以使用以下工具：</p>
<ul>
<li><a href="https://github.com/mysticatea/npm-run-all" target="_blank" rel="nofollow noopener noreferrer"><code>npm-run-all</code></a> -   命令行工具，同时运行多个npm脚本（并行或串行）</li>
</ul>
<p>npm-run-all提供了三个命令，分别是 npm-run-all run-s run-p，后两者是 npm-run-all 带参数的简写，分别对应串行和并行。而且还支持匹配分隔符，可以简化script配置</p>
<p>或者使用</p>
<ul>
<li><a href="https://github.com/kimmobrunfeldt/concurrently" target="_blank" rel="nofollow noopener noreferrer"><code>concurrently</code></a> -    并行执行命令，类似 npm run watch-js & npm run watch-less但更优。（不过它只能并行）</li>
</ul>
<h4 data-id="heading-12">3.5 应用场景5：如何检查NPM模块未使用的依赖。</h4>
<p>可以使用以下工具：</p>
<ul>
<li><a href="https://github.com/depcheck/depcheck" target="_blank" rel="nofollow noopener noreferrer"><code>depcheck</code></a> -  检查你的NPM模块未使用的依赖。</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/09f11af51fcc4579adcb2eb4941d0955~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-13">3.6 其他：</h4>
<ul>
<li><a href="https://github.com/npm/node-semver" target="_blank" rel="nofollow noopener noreferrer"><code>npminstall</code></a> - 使 npm install 更快更容易，cnpm默认使用</li>
<li><a href="https://github.com/repo-utils/giturl" target="_blank" rel="nofollow noopener noreferrer"><code>semver</code></a> - NPM使用的JavaScript语义化版本号解析器。</li>
</ul>
<p>关于npm包在线查询，推荐一个利器 <a href="https://npm.devtool.tech/" target="_blank" rel="nofollow noopener noreferrer"><code>npm.devtool.tech</code></a></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61085e432e534654a98dedb70db687ea~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-14">4.文档生成</h3>
<h4 data-id="heading-15">4.1 应用场景1：如何自动生成api文档？</h4>
<ul>
<li><a href="https://github.com/docsifyjs/docsify" target="_blank" rel="nofollow noopener noreferrer"><code>docsify</code></a> -   API文档生成器。</li>
<li><a href="https://github.com/jsdoc/jsdoc" target="_blank" rel="nofollow noopener noreferrer"><code>jsdoc </code></a> -  API文档生成器，类似于JavaDoc或PHPDoc。</li>
</ul>
<h3 data-id="heading-16">5.日志工具</h3>
<h4 data-id="heading-17">5.1 应用场景1：如何实现日志分类?</h4>
<ul>
<li><a href="https://github.com/log4js-node/log4js-node" target="_blank" rel="nofollow noopener noreferrer"><code>log4js-nodey</code></a> -  不同于Java log4j的日志记录库。</li>
<li><a href="https://github.com/nuxt/consola" target="_blank" rel="nofollow noopener noreferrer"><code>consola </code></a>  - 优雅的Node.js和浏览器日志记录库。</li>
<li><a href="https://github.com/winstonjs/winston" target="_blank" rel="nofollow noopener noreferrer"><code>winston </code></a> - 多传输异步日志记录库（古老）</li>
</ul>
<h3 data-id="heading-18">6.命令行工具</h3>
<h4 data-id="heading-19">6.1 应用场景1: 如何解析命令行输入？</h4>
<blockquote>
<p>我们第一印象会想到的是<code>process.argv</code>，那么还有什么工具可以解析吗？</p>
</blockquote>
<p>可以使用以下工具：</p>
<ul>
<li><a href="https://github.com/substack/minimist" target="_blank" rel="nofollow noopener noreferrer"><code>minimist </code></a> -   命令行参数解析引擎</li>
<li><a href="https://github.com/vercel/arg" target="_blank" rel="nofollow noopener noreferrer"><code>arg</code></a>  -  简单的参数解析</li>
<li><a href="https://github.com/npm/nopt" target="_blank" rel="nofollow noopener noreferrer"><code>nopt  </code></a> - Node/npm 参数解析</li>
</ul>
<h4 data-id="heading-20">6.2 应用场景2：如何让用户能与命令行进行交互？</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/388fc0301bd64d7da64647d3184b10c2~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以使用以下工具：</p>
<ul>
<li><a href="https://github.com/SBoudrias/Inquirer.js" target="_blank" rel="nofollow noopener noreferrer"><code>Inquirer.js </code></a> -  通用可交互命令行工具集合。</li>
<li><a href="https://github.com/terkelg/prompts" target="_blank" rel="nofollow noopener noreferrer"><code>prompts </code></a>  -  轻量、美观、用户友好的交互式命令行提示。</li>
<li><a href="https://github.com/enquirer/enquirer" target="_blank" rel="nofollow noopener noreferrer"><code>Enquirer  </code></a> -  用户友好、直观且易于创建的时尚CLI提示。</li>
</ul>
<h4 data-id="heading-21">6.3  应用场景3: 如何在命令行中显示进度条？</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/09aeaef53466421cb09b18d43d2174a4~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
可以使用以下工具：</p>
<ul>
<li><a href="https://github.com/visionmedia/node-progress" target="_blank" rel="nofollow noopener noreferrer"><code>progress</code></a> -   Node.js的灵活ascii进度条。</li>
<li><a href="https://github.com/bvaughn/progress-estimator" target="_blank" rel="nofollow noopener noreferrer"><code>progress-estimator  </code></a>  -   记录进度条并估计完成承诺所需的时间。</li>
</ul>
<h4 data-id="heading-22">6.4 应用场景4: 如何在命令行执行多任务？</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/331c54e9d89c4a61a92bd2ab515db26b~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以使用以下工具：</p>
<ul>
<li><a href="https://github.com/SamVerschueren/listr" target="_blank" rel="nofollow noopener noreferrer"><code>listr</code></a> -  命令行任务列表。</li>
</ul>
<h4 data-id="heading-23">6.5 应用场景5: 如何给命令行“锦上添花”？</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1715bfee3d9e4dbdba2a797800aa4c64~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以使用以下工具：</p>
<ul>
<li><a href="https://github.com/chalk/chalk" target="_blank" rel="nofollow noopener noreferrer"><code>chalk</code></a> -   命令行字符串样式美化工具。</li>
<li><a href="https://github.com/sindresorhus/ora" target="_blank" rel="nofollow noopener noreferrer"><code>ora </code></a>  -    优雅的命令行loading效果。</li>
<li><a href="https://github.com/Marak/colors.js" target="_blank" rel="nofollow noopener noreferrer"><code>colors.js</code></a>  -    获取Node.js控制台的颜色。</li>
<li><a href="https://github.com/gtanner/qrcode-terminal" target="_blank" rel="nofollow noopener noreferrer"><code>qrcode-terminal</code></a>  -    命令行中显示二维码。</li>
<li><a href="https://github.com/notatestuser/treeify" target="_blank" rel="nofollow noopener noreferrer"><code>treeify</code></a>  -     将javascript对象漂亮地打印为树。</li>
<li><a href="https://github.com/lukeed/kleur" target="_blank" rel="nofollow noopener noreferrer"><code>kleur</code></a>  -   最快的Node.js库，使用ANSI颜色格式化命令行文本。</li>
</ul>
<blockquote>
<p>感兴趣的童鞋可以参考树酱的<a href="https://juejin.cn/post/6844904137709060104" target="_blank"><code>从0到1开发简易脚手架</code></a>，其中有实践部分工具</p>
</blockquote>
<h3 data-id="heading-24">7.加解密</h3>
<blockquote>
<p>一般为了项目安全性考虑，我们通常会对账号密码进行加密，一般会通过MD5、AES、SHA1、SM，那开源社区有哪些库可以方便我们使用？</p>
</blockquote>
<p>可以使用以下工具：</p>
<ul>
<li><a href="https://github.com/brix/crypto-js" target="_blank" rel="nofollow noopener noreferrer"><code>crypto-js</code></a> -   JavaScript加密标准库。支持算法最多</li>
<li><a href="https://github.com/rzcoder/node-rsa" target="_blank" rel="nofollow noopener noreferrer"><code>node-rsa</code></a>  -    Node.js版Bcrypt。</li>
<li><a href="https://github.com/pvorb/node-md5" target="_blank" rel="nofollow noopener noreferrer"><code>node-md5</code></a>  -    一个JavaScript函数，用于使用MD5对消息进行哈希处理。</li>
<li><a href="https://github.com/ricmoo/aes-js" target="_blank" rel="nofollow noopener noreferrer"><code>aes-js </code></a>  -   AES的纯JavaScript实现。</li>
<li><a href="https://github.com/JuneAndGreen/sm-crypto" target="_blank" rel="nofollow noopener noreferrer"><code>sm-crypto</code></a>  -   国密sm2, sm3, sm4的JavaScript实现。</li>
<li><a href="https://github.com/crypto-browserify/sha.js" target="_blank" rel="nofollow noopener noreferrer"><code>sha.js </code></a>  -   使用纯JavaScript中的流式SHA哈希。</li>
</ul>
<h3 data-id="heading-25">8.静态网站生成 & 博客</h3>
<blockquote>
<p>一键生成网站不香吗~ 基于node体系快速搭建自己的博客网站，你值得拥有，也可以作为组件库文档展示</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e93ebb4fe4c49bba589d168e764741c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以使用以下工具：</p>
<ul>
<li><a href="https://github.com/hexojs/hexo" target="_blank" rel="nofollow noopener noreferrer"><code>hexo </code></a> -   使用Node.js的快速，简单，强大的博客框架。</li>
<li><a href="https://github.com/vuejs/vuepress" target="_blank" rel="nofollow noopener noreferrer"><code>vuepress </code></a>  -   极简的Vue静态网站生成工具。（基于nuxt SSR）</li>
<li><a href="https://github.com/netlify/netlify-cms" target="_blank" rel="nofollow noopener noreferrer"><code>netlify-cms</code></a>  -    基于Git的静态网站生成工具。</li>
<li><a href="https://github.com/vuejs/vitepress" target="_blank" rel="nofollow noopener noreferrer"><code>vitepress </code></a>  -  Vite & Vue.js静态网站生成工具。</li>
</ul>
<h3 data-id="heading-26">9.数据校验工具</h3>
<blockquote>
<p>数据校验，离我们最近的就是表单数据的校验，在平时使用的组件库比如element、iview等我们会看到使用了一个开源的校验工具<code>async-validator </code>, 那还有其他吗？</p>
</blockquote>
<p>可以使用以下工具：</p>
<ul>
<li><a href="https://github.com/validatorjs/validator.js" target="_blank" rel="nofollow noopener noreferrer"><code>validator.js </code></a> -    字符串校验库。</li>
<li><a href="https://github.com/hapijs/joi" target="_blank" rel="nofollow noopener noreferrer"><code>joi</code></a>  -   基于JavaScript对象的对象模式描述语言和验证器。</li>
<li><a href="https://github.com/yiminghe/async-validators" target="_blank" rel="nofollow noopener noreferrer"><code>async-validator </code></a>  -   异步校验。</li>
<li><a href="https://github.com/epoberezkin/ajv" target="_blank" rel="nofollow noopener noreferrer"><code>ajv </code></a>  - 最快的JSON Schema验证器</li>
<li><a href="https://github.com/ianstormtaylor/superstruct" target="_blank" rel="nofollow noopener noreferrer"><code>superstruct </code></a>  -  用简单和可组合的方式在JavaScript和TypeScript中校验数据。</li>
</ul>
<h3 data-id="heading-27">10.解析工具</h3>
<h4 data-id="heading-28">10.1应用场景1: 如何解析markdown？</h4>
<p>可以使用以下工具：</p>
<ul>
<li><a href="https://github.com/markedjs/marked" target="_blank" rel="nofollow noopener noreferrer"><code>marked </code></a> -   Markdown解析器和编译器，专为提高速度而设计。</li>
<li><a href="https://github.com/wooorm/remark" target="_blank" rel="nofollow noopener noreferrer"><code>remark</code></a>  -  Markdown处理工具。</li>
<li><a href="https://github.com/markdown-it/markdown-it" target="_blank" rel="nofollow noopener noreferrer"><code>markdown-it </code></a>  -支持100%通用Markdown标签解析的扩展&语法插件。</li>
</ul>
<h4 data-id="heading-29">10.2应用场景2: 如何解析csv？</h4>
<p>可以使用以下工具：</p>
<ul>
<li><a href="https://github.com/mholt/PapaParse" target="_blank" rel="nofollow noopener noreferrer"><code>PapaParse </code></a> -   快速而强大的 CSV（分隔文本）解析器，可以优雅地处理大文件和格式错误的输入。</li>
<li><a href="https://github.com/adaltas/node-csv" target="_blank" rel="nofollow noopener noreferrer"><code>node-csv</code></a>  - 具有简单api的全功能CSV解析器，并针对大型数据集进行了测试。</li>
<li><a href="https://github.com/mafintosh/csv-parser" target="_blank" rel="nofollow noopener noreferrer"><code>csv-parser</code></a>  -旨在比其他任何人都快的流式CSV解析器。</li>
</ul>
<h4 data-id="heading-30">10.3应用场景3: 如何解析xml？</h4>
<p>可以使用以下工具：</p>
<ul>
<li><a href="https://github.com/Leonidas-from-XIV/node-xml2js" target="_blank" rel="nofollow noopener noreferrer"><code>xml2js  </code></a> -   将XML转换为JavaScript对象的转换器。</li>
<li><a href="https://github.com/NaturalIntelligence/fast-xml-parser" target="_blank" rel="nofollow noopener noreferrer"><code>fast-xml-parser</code></a>  - 具验证&解析 XML。</li>
</ul>
<h3 data-id="heading-31">最后</h3>
<blockquote>
<p>如果你喜欢这个库，也给作者<code>huaize2020</code> 一个star 仓库地址：<a href="https://github.com/huaize2020/awesome-nodejs/blob/main/README-zh-CN.md" target="_blank" rel="nofollow noopener noreferrer">awesome-nodejs</a></p>
</blockquote>
<p>昨天看到一段话想分享给大家</p>
<p>对于一个研发测的日常：</p>
<ul>
<li>1.开始工作的第一件事，规划今日的工作内容安排 （建议有清晰的ToDolist，且按优先级排序）</li>
<li>2.确认工作量与上下游关联风险（如依赖他人的，能否按时提供出来）；有任何风险，尽早暴露</li>
<li>3.注意时间成本、不是任何事情都是值得你用尽所有时间去做的，分清主次关系</li>
<li>4.协作任务，明确边界责任，不要出现谁都不管，完成任务后及时同步给相关人</li>
<li>5.及时总结经验，沉淀技术产出实现能力复用，同类型任务，不用从零开始，避免重复工作</li>
</ul>
 <p>往期热门文章📖：</p>
<ul>
<li><a href="https://juejin.cn/post/6931708519976534029" target="_blank">从0到1开发可视化数据大屏（上）
</a></li>
<li><a href="https://juejin.cn/post/6959834710788800542" target="_blank">从0到1开发可视化数据大屏（下）
</a></li>
<li><a href="https://juejin.im/post/6855468132186882055" target="_blank" rel="nofollow noopener noreferrer">树酱的前端知识体系构建（上）
</a></li>
  <li><a href="https://juejin.im/post/6860018724221976584" target="_blank" rel="nofollow noopener noreferrer">树酱的前端知识体系构建（下）
</a></li>
<li><a href="https://juejin.im/post/6844904176330375181" target="_blank" rel="nofollow noopener noreferrer">聊聊前端开发日常的协作工具</a></li><li><a href="https://juejin.im/post/6863705400773083149" target="_blank" rel="nofollow noopener noreferrer">babel配置傻傻看不懂</a></li><li><a href="https://juejin.im/post/6844904154574356493" target="_blank" rel="nofollow noopener noreferrer">如何更好管理 Api 接口</a></li><li><a href="https://juejin.im/post/6844904177466867726" target="_blank" rel="nofollow noopener noreferrer">面试官问你关于node的那些事</a></li><li><a href="https://juejin.im/post/6844904132512317453" target="_blank" rel="nofollow noopener noreferrer">前端工程化那些事</a></li><li><a href="https://juejin.im/post/6844904185427673095" target="_blank" rel="nofollow noopener noreferrer">你学BFF和Serverless了吗</a></li><li><a href="https://juejin.im/post/6844904118020997128" target="_blank" rel="nofollow noopener noreferrer">前端运维部署那些事</a></li></ul>
<p>你好，我是🌲 树酱，请你喝杯🍵 记得三连哦～</p>
<p>1.阅读完记得点个赞哦，有👍 有动力</p>
<p>2.关注公众号前端那些趣事，陪你聊聊前端的趣事</p>
<p>3.文章收录在Github frontendThings 感谢Star✨</p></div>  
</div>
            