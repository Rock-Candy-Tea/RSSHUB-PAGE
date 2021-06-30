
---
title: '百度关于EMP的探索：落地生产可用的微前端架构'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a6ce43f9a4724838a7e345b934450483~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 28 Jun 2021 18:57:10 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a6ce43f9a4724838a7e345b934450483~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>导读</strong>：随着 Web 前端工程‬日趋复杂，也‬带来了更大的工程理治‬挑战，微前端在‬大型前端工架程‬构解决方案中成已‬为重要思路之一。本文详细描述 EMP 的诞生背景、使用场景、生态以及如何使用，可以帮助大家能更简单、更高效的构建生产可用微前端架构。</p>
<p><em>全文3740字，预计阅读时间9分钟。</em></p>
<h1 data-id="heading-0"><strong>一、EMP是什么</strong></h1>
<hr>
<p>EMP 是一个微前端架构解决方案集合，旨在帮助大家能更简单、更高效的构建生产可用微前端架构。<a href="https://github.com/efoxTeam/emp" target="_blank" rel="nofollow noopener noreferrer">github.com/efoxTeam/em…</a></p>
<p>2020年5月开始，我们团队开始探索微前端架构。调研从主流的 iframe、Single SPA 到那时刚刚问世的 module federation，最后选择性能和比较有前景的 module federation 作为基础技术进行架构 EMP 微前端解决方案。至今有一年多，已经 releases 53 个版本，解决 108 个 issues，同时具有一定程度生态，有 43 种使用场景的 Demo，支持 7 种 EMP UI 插件支持（包括但不限于 React、Vue、Angular、Preact），4 个编译器支持（babel、esbuild、swc、esm），1 个 Webpack Plugin，目前 EMP 已在服务的线上应用具有一定的稳定性和扩展性。</p>
<h1 data-id="heading-1"><strong>二、EMP 出现的背景</strong></h1>
<hr>
<p>随着 Web 应用的日渐强大，随之而来的是前端项目不断膨胀。业务需求不断叠加的情况下，巨石项目越来越难维护，编译时间越来越难等。具体来说是，可能会出现 几 MB 的 Bundle Size、十几甚至几十号前端开发人员、一个前端代码库（含 node_modules）会有几 GB。所以需要思考如何把庞大的 Web 项目分解成若干个项目，以便于团队分工协作。</p>
<p>业务开发中，不同项目之间会存在很多可复用的模块。通用的用户数据、UI架构风格、相似的业务逻辑都可以复用，例如一个时间戳转时间的函数就可以到处复用而无需重写甚至引库。所以需要思考如何可以让多个应用项目直接共享这些可复用的模块。当然拆成 NPM 包是一个不错的想法，也是最常用的。</p>
<h1 data-id="heading-2"><strong>三、EMP 的优势</strong></h1>
<hr>
<ul>
<li>
<p>巨型项目解耦。把巨型项目分解成多个小型项目，分团队开发维护。</p>
</li>
<li>
<p>快速封装可复用模块。无需单独拆包发布到 NPM，可直接暴露需要共享的模块。引入端仅需要简单配置输出端的地址即可在代码上使用该共享模块。</p>
</li>
<li>
<p>动态更新。把复用的业务模块放在同一个基站应用之中进行管理和维护，并且暴露出去可以给多个应用使用。如果业务模块需要更新逻辑的话，只需要发布部署基站应用，其他应用并不需要任何操作，只需要访问时刷新，即可使用最新业务模块。</p>
</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a6ce43f9a4724838a7e345b934450483~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>- 远端模块，由于引入端无需手动更新，远端模块的灵活维护和引入端可以自由组合，甚至可以运行时引入使用远端模块。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d9d87c7476f54d7f9e9fb4cc4afff3e5~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>- 加速构建。因为引入其他项目暴露的模块，不需要本地构建这些子模块的代码，减小了构建体积，提升整个应用的构建速度。- 减少单个项目 Bundle Size。因为引入其他项目暴露的模块，减少各个项目 Bundle Size。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19990d0e6e7a41ad83e76d25eab91ed5~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<p>- 下图时对旧项目改造使用了 EMP 微前端方案后带来的速度提升的实际数据</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10563f8f03bd41a4b309e2eb884d8402~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-3"><strong>四、EMP 架构设计</strong></h1>
<hr>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/acaa7781a1a64827a503ecf037002251~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-4"><strong>五、EMP 生态</strong></h1>
<hr>
<p>EMP 针对不同的UI框架和使用场景都有进行适配和优化。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe99b582834343b384f2ae79ff74b230~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-5"><strong>六、EMP 开箱即用</strong></h1>
<h4 data-id="heading-6">1.初始化</h4>
<pre><code class="copyable">npx @efox/emp-cli init

<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>
<p>可以选择以下模板项目进行初始化，推荐试用 React Typescript 模板</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/29b5c4cfa4804854a94d4d1a83a17501~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
<li>
<p>按提示执行 <code>cd my-emp && yarn && yarn dev</code> 之后，项目将会自动打开在浏览器。</p>
</li>
<li>
<p>React 基站：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a2afbe15ae346ff85170b2f2713e49e~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
</li>
</ul>
<p>+ React 项目：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6a49ac3e8e0945d9869a1fdbf9ea94e7~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>如果你想预先安装 <code>@efox/emp-cli</code>，可以通过全局安装 <code>npm install -g @efox/emp-cli</code> 或 <code>yarn global add @efox/emp-cli</code> 。</p>
</li>
<li>
<p>建议你卸载该包使用 <code>npm uninstall -g @efox/emp-cli</code> or <code>yarn global remove @efox/emp-cli</code> 确保 npx 使用的 <code>@efox/emp-cli</code> 是最新版本。</p>
</li>
</ul>
<h4 data-id="heading-7">2. EMP 唯一的配置文件 emp-config.js ,</h4>
<h5 data-id="heading-8">以 React 为例，解释配置核心：</h5>
<pre><code class="copyable">/**
 * @type &#123;import('@efox/emp-cli').EMPConfig&#125;
 */
module.exports = &#123;
  webpack() &#123;
    return &#123;
      devServer: &#123;
        /**
         * 设置 devServer
         */
        port: 8002,
      &#125;,
    &#125;
  &#125;,
  async moduleFederation() &#123;
    return &#123;
      /**
      * name: 对外暴露项目名,
      */
      name: 'demo',
      /**
      * filename: 对外暴露引用文件名,
      */
      filename: 'emp.js',
      /**
      * remotes 远程模块
      * remotes: &#123;
      * '引用别名': '远程模块项目名@远程模块的emp.js文件地址',
      * &#125;,
      */
      remotes: &#123;
        '@emp/demo1': 'demo1@http://localhost:8001/emp.js',
      &#125;,
      /**
      * exposes 暴露模块
      * exposes: &#123;
      * '对外暴露的相对路径': '当前项目相对路径',
      * &#125;,
      */
      exposes: &#123;
        './components/Hello': 'src/components/Hello',
        './helper': 'src/helper',
      &#125;,
      /**
      * shared 共享的第三方依赖
      * shared: ['依赖名'],
      */
      shared: ['react', 'react-dom'],
    &#125;
  &#125;,
&#125;


<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-9">以 Vue2 为例，解释配置核心：</h5>
<pre><code class="copyable">const withVue2 = require('@efox/emp-vue2')
module.exports = withVue2((&#123;config&#125;) => &#123;
  const projectName = 'vue2Project'
  const port = 8008
  config.output.publicPath(`http://localhost:$&#123;port&#125;/`)
  config.devServer.port(port)
  config.plugin('mf').tap(args => &#123;
    args[0] = &#123;
      ...args[0],
      ...&#123;
        /**
         * name: 对外暴露项目名,
         */
        name: projectName,
        /**
        * filename: 对外暴露引用文件名,
        */
        filename: 'emp.js',
        /**
         * remotes 远程模块
         * remotes: &#123;
         * '引用别名': '远程模块项目名@远程模块的emp.js文件地址',
         * &#125;,
         */
        remotes: &#123;
          '@v2b': 'vue2Base@http://localhost:8009/emp.js',
        &#125;,
        /**
        * exposes 暴露模块
        * exposes: &#123;
        * '对外暴露的相对路径': '当前项目相对路径',
        * &#125;,
        */
        exposes: &#123;
          './Content': './src/components/Content',
        &#125;,
        /**
        * shared 共享的第三方依赖
        * shared: ['依赖名'],
        */
        shared: ['vue/dist/vue.esm.js'],
      &#125;,
    &#125;
    return args
  &#125;)

  config.plugin('html').tap(args => &#123;
    args[0] = &#123;
      ...args[0],
      ...&#123;
        title: 'EMP Vue2 Project',
      &#125;,
    &#125;
    return args
  &#125;)
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-10"><strong>七、已有项目无痛升级到 EMP 微前端架构</strong></h1>
<hr>
<ul>
<li>
<p>@vue/cli Vue2 模版升级到微前端 EMP</p>
</li>
<li>
<p>React CRA 项目升级到微前端 EMP</p>
</li>
</ul>
<h1 data-id="heading-11"><strong>八、跨框架调用实现</strong></h1>
<hr>
<blockquote>
<p>EMP 不推荐大家跨框架调用，因为这样会增加维护成本和风险。但是我们还是支持：</p>
</blockquote>
<ul>
<li>
<p>Vue3 调用 Vue2 组件</p>
</li>
<li>
<p>Vue&React 互相调用</p>
</li>
</ul>
<h1 data-id="heading-12"><strong>九、对比 NPM 拆包</strong></h1>
<hr>
<ul>
<li>但是 npm 拆包有一定工作量：</li>
</ul>
<ol>
<li>
<p>需要把可复用模块从业务项目抽离到一个新的 package</p>
</li>
<li>
<p>搭建新的构建配置</p>
</li>
<li>
<p>单独建 repo</p>
</li>
<li>
<p>在原有业务项目重新引用</p>
</li>
<li>
<p>可能会因为封装，需要重新设计 API</p>
</li>
</ol>
<ul>
<li>但是业务模块抽离成 npm 包后,使用 npm 包的更新流程繁琐复杂：</li>
</ul>
<ol>
<li>
<p>更新 npm 包版本</p>
</li>
<li>
<p>更新 A 应用的npm包版本</p>
</li>
<li>
<p>重启 A 应用进行验证</p>
</li>
<li>
<p>发布部署 A 管理系统应用</p>
</li>
<li>
<p>对 B 和C 应用循环2和3、4步骤</p>
</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07f342b2a453430e91f1122a836ce026~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>但是 npm 包会拖慢构建速度：通过 npm 引入 n 个的业务模块后，在构建时相当于将n个业务模块的代码“复制”到了项目中，构建时需要同步去构建这些业务子模块，导致 bundle size 变大，构建时长会增加，开发体验变差，发布效率也会随之降低。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0a2735495fe1400bb06464237fd86fb6~tplv-k3u1fbpfcp-zoom-1.image" alt="图片" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-13"><strong>十、总结</strong></h1>
<ul>
<li>
<p>本文用较短的篇幅介绍了 EMP 的诞生背景、使用场景、生态以及如何无痛使用。</p>
</li>
<li>
<p>EMP 在不断迭代升级，同时生态日渐完善，欢迎各位来了解、使用 EMP 微前端解决方案。</p>
</li>
<li>
<p>期待大家一起探讨，欢迎来提issue或者新功能：</p>
<p><a href="https://github.com/efoxTeam/emp" target="_blank" rel="nofollow noopener noreferrer">github.com/efoxTeam/em…</a></p>
</li>
</ul>
<h1 data-id="heading-14"><strong>十一、QA</strong></h1>
<hr>
<ul>
<li>
<p>如果有问题的话，可以先来看看我们的 issue 哦。世界这么大，说不定你和别人遇到一样的问题：<a href="https://github.com/efoxTeam/emp/issues?q=is%3Aissue+is%3Aclosed" target="_blank" rel="nofollow noopener noreferrer">github.com/efoxTeam/em…</a></p>
</li>
</ul>
<p><strong>招聘信息：</strong></p>
<p>百度直播研发部招聘研发岗位，包括客户端-Android/iOS方向，服务端-Go/PHP方向。我们负责百度直播业务，对直播业务感兴趣欢迎加入我们。</p>
<p><strong>关注同名公众号百度Geek说，输入内推即可，我们期待你的加入！</strong></p>
<p><strong>推荐阅读：</strong></p>
<p><a href="https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247494399&idx=1&sn=0516ad01baf50442933865d33e88e1af&chksm=c03eda83f749539562f223c320c86ce0d8092e4c1d793994fd602fae7cc986c9129f2b77c0ab&token=1987775079&lang=zh_CN&scene=21#wechat_redirect" target="_blank" rel="nofollow noopener noreferrer">｜</a><a href="http://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247494896&idx=1&sn=1ad73deb5f2dfbb90e08793bc675cb12&chksm=c03edc8cf749559a547dd313a1a486b20bc7064afb4dd4a8b5b86425b832de10f1d727144e98&scene=21#wechat_redirect" target="_blank" rel="nofollow noopener noreferrer">百度C++工程师的那些极限优化（并发篇）</a></p>
<p><a href="https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247494399&idx=1&sn=0516ad01baf50442933865d33e88e1af&chksm=c03eda83f749539562f223c320c86ce0d8092e4c1d793994fd602fae7cc986c9129f2b77c0ab&token=1987775079&lang=zh_CN&scene=21#wechat_redirect" target="_blank" rel="nofollow noopener noreferrer">｜</a><a href="http://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247489076&idx=1&sn=748bf716d94d5ed2739ea8a9385cd4a6&chksm=c03d2648f74aaf5e11298cf450c3453a273eb6d2161bc90e411b6d62fa0c1b96a45e411af805&scene=21#wechat_redirect" target="_blank" rel="nofollow noopener noreferrer">百度C++工程师的那些极限优化（内存篇）</a></p>
<p><a href="https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247494399&idx=1&sn=0516ad01baf50442933865d33e88e1af&chksm=c03eda83f749539562f223c320c86ce0d8092e4c1d793994fd602fae7cc986c9129f2b77c0ab&token=1987775079&lang=zh_CN&scene=21#wechat_redirect" target="_blank" rel="nofollow noopener noreferrer">｜百度大规模Service Mesh落地实践</a></p>
<p><a href="https://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247494399&idx=1&sn=0516ad01baf50442933865d33e88e1af&chksm=c03eda83f749539562f223c320c86ce0d8092e4c1d793994fd602fae7cc986c9129f2b77c0ab&token=1987775079&lang=zh_CN&scene=21#wechat_redirect" target="_blank" rel="nofollow noopener noreferrer">｜</a><a href="http://mp.weixin.qq.com/s?__biz=Mzg5MjU0NTI5OQ==&mid=2247493116&idx=1&sn=90925b509f4d8bfedc7066f2317e3d9c&chksm=c03ed580f7495c9621068194b799dd7fcc9ebff535a6fa04aacf593eae549c8d500b06df57d1&scene=21#wechat_redirect" target="_blank" rel="nofollow noopener noreferrer">一种基于实时分位数计算的系统及方法</a></p>
<p>---------- END ----------</p>
<p>百度Geek说</p>
<p>百度官方技术公众号上线啦！</p>
<p>技术干货 · 行业资讯 · 线上沙龙 · 行业大会</p>
<p>招聘信息 · 内推信息 · 技术书籍 · 百度周边</p>
<p>欢迎各位同学关注</p></div>  
</div>
            