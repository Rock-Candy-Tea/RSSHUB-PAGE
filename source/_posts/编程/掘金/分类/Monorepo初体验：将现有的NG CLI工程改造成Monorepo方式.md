
---
title: 'Monorepo初体验：将现有的NG CLI工程改造成Monorepo方式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f74049dabc1c4a07bf4f0ece127f9ef8~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 06 Jun 2021 16:23:32 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f74049dabc1c4a07bf4f0ece127f9ef8~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="https://devui.design/" target="_blank" rel="nofollow noopener noreferrer">DevUI</a> 是一款面向企业中后台产品的开源前端解决方案，它倡导<code>沉浸</code>、<code>灵活</code>、<code>至简</code>的设计价值观，提倡设计者为真实的需求服务，为多数人的设计，拒绝哗众取宠、取悦眼球的设计。如果你正在开发 <code>ToB</code> 的<code>工具类产品</code>，DevUI 将是一个很不错的选择！</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f74049dabc1c4a07bf4f0ece127f9ef8~tplv-k3u1fbpfcp-watermark.image" alt="Kagol.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-0">前言</h1>
<p>Monorepo 能够优雅地解决代码复用的问题，统一工作流，并且不影响构建、部署的效率。</p>
<p>目前开源社区已经有不少开源项目都是采用 Monorepo 的方式管理源码的，比如：Vue3，以下是它的部分源码结构：</p>
<pre><code class="copyable">vue-next
├── CHANGELOG.md
├── LICENSE
├── README.md
├── api-extractor.json
├── jest.config.js
├── package.json
├── packages // 每一个包在一个文件夹下，独立测试、独立构建、独立部署
|  ├── compiler-core
|  ├── compiler-dom
|  ├── compiler-sfc
|  ├── compiler-ssr
|  ├── global.d.ts
|  ├── reactivity
|  ├── runtime-core
|  ├── runtime-dom
|  ├── runtime-test
|  ├── server-renderer
|  ├── shared
|  ├── size-check
|  ├── template-explorer
|  └── vue
|     ├── README.md
|     ├── __tests__
|     ├── api-extractor.json
|     ├── examples
|     ├── index.js
|     ├── package.json
|     └── src
├── rollup.config.js
├── ...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们一起来看看如何将一个现有的NG CLI工程切换成Monorepo，并在Monorepo的工作空间里不断扩展新项目吧！</p>
<h1 data-id="heading-1">创建一个 NG CLI 项目</h1>
<p>我们先来创建一个CLI工程，并将其启动起来。</p>
<pre><code class="copyable">ng n my-portal --style=scss

cd my-portal

npm start
<span class="copy-code-btn">复制代码</span></code></pre>
<p>访问以下链接就能将项目启动起来：</p>
<p><a href="http://localhost:4200/" target="_blank" rel="nofollow noopener noreferrer">http://localhost:4200/</a></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1a6089df77834691b0aff1843c4b7785~tplv-k3u1fbpfcp-watermark.image" alt="初始工程.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">升级成 Monorepo</h1>
<p>我们已经有了一个 NG CLI，将其变成 Monorepo 工作空间非常简单，只需要一个命令：</p>
<pre><code class="copyable">ng add @nrwl/workspace
<span class="copy-code-btn">复制代码</span></code></pre>
<p>执行该命令后，我们的项目结构发生了一些改变，以下是主要的变化：</p>
<pre><code class="copyable">DELETE .browserslistrc
DELETE tsconfig.app.json
DELETE tsconfig.spec.json
DELETE tsconfig.json
RENAME src/app/app-routing.module.ts => apps/my-portal/src/app/app-routing.module.ts
RENAME src/app/app.component.html => apps/my-portal/src/app/app.component.html
RENAME src/app/app.component.scss => apps/my-portal/src/app/app.component.scss
RENAME src/app/app.component.spec.ts => apps/my-portal/src/app/app.component.spec.ts
RENAME src/app/app.component.ts => apps/my-portal/src/app/app.component.ts
RENAME src/app/app.module.ts => apps/my-portal/src/app/app.module.ts
RENAME src/assets/.gitkeep => apps/my-portal/src/assets/.gitkeep
RENAME src/environments/environment.prod.ts => apps/my-portal/src/environments/environment.prod.ts
RENAME src/environments/environment.ts => apps/my-portal/src/environments/environment.ts
RENAME src/favicon.ico => apps/my-portal/src/favicon.ico
RENAME src/index.html => apps/my-portal/src/index.html
RENAME src/main.ts => apps/my-portal/src/main.ts
RENAME src/polyfills.ts => apps/my-portal/src/polyfills.ts
RENAME src/styles.scss => apps/my-portal/src/styles.scss
RENAME src/test.ts => apps/my-portal/src/test.ts
RENAME e2e/src/app.e2e-spec.ts => apps/my-portal-e2e/src/app.e2e-spec.ts
RENAME e2e/src/app.po.ts => apps/my-portal-e2e/src/app.po.ts
RENAME e2e/protractor.conf.js => apps/my-portal-e2e/protractor.conf.js
RENAME e2e/tsconfig.json => apps/my-portal-e2e/tsconfig.json
CREATE apps/my-portal/.browserslistrc (703 bytes)
CREATE apps/my-portal/tsconfig.app.json (223 bytes)
CREATE apps/my-portal/karma.conf.js (1013 bytes)
CREATE apps/my-portal/tsconfig.spec.json (268 bytes)
CREATE tools/schematics/.gitkeep (0 bytes)
CREATE tools/tsconfig.tools.json (251 bytes)
CREATE nx.json (433 bytes)
CREATE libs/.gitkeep (0 bytes)
CREATE .vscode/extensions.json (144 bytes)
CREATE .prettierrc (26 bytes)
CREATE tsconfig.base.json (416 bytes)
CREATE decorate-angular-cli.js (2628 bytes)
UPDATE karma.conf.js (1016 bytes)
UPDATE package.json (2035 bytes)
UPDATE angular.json (4659 bytes)
UPDATE tslint.json (3491 bytes)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>比较明显的改变就是：</p>
<ul>
<li>将src和tsconfig的代码迁移到apps中</li>
<li>增加了nx.json配置文件</li>
</ul>
<p>这时我们重新执行<code>npm start</code>启动项目，并通过链接<code>http://localhost:4200/</code>访问页面。</p>
<blockquote>
<p>看起来和之前没有任何的不同，不过实质已发生巨大的变化。就像变成白袍巫师的甘道夫，穿上灰袍，看着还是以前的“灰袍巫师甘道夫”，不过早已经历了蜕变。</p>
</blockquote>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/18dc5a6ecde04cb58b5d1bae7db79357~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-3">增加一个 Angular 项目</h1>
<p>升级成 Monorepo 的 NG CLI 工程就像<code>变成白袍后的甘道夫</code>，拥有平行扩展的能力，可以增加任意的子项目，而不增加构建的成本。</p>
<p>比如我们想增加一个 Angular 项目，只需要执行以下命令：</p>
<pre><code class="copyable">npx nx g @nrwl/angular:app projectman-portal
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时apps目录下会新增一个projectman-portal目录：</p>
<pre><code class="copyable">├── apps
|  ├── my-portal
|  ├── projectman-portal // 新增的
<span class="copy-code-btn">复制代码</span></code></pre>
<p>新增加的子项目和之前的项目是完全独立的，不影响之前项目的本地启动、测试、构建、部署等。</p>
<p>启动子项目：</p>
<pre><code class="copyable">npx nx serve projectman-portal --port 4100
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b4b46dcd28a4b7c9580c6eb44691a0a~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>my-portal和projectman-portal启动时，会使用不同的端口号，本地开发互不影响。</p>
<h1 data-id="heading-4">公共部分 shared</h1>
<p>现在我们有一个主应用my-portal和一个子应用projectman-portal，如果这两个项目中有一个公共的模块：成员管理，我们要怎么实现模块复用呢？</p>
<h2 data-id="heading-5">新建公共模块</h2>
<p>可以在<code>apps</code>下新建一个<code>shared</code>文件夹，由于是Angular项目，再建一个<code>angular</code>子文件夹。</p>
<pre><code class="copyable">├── apps
|  ├── my-portal
|  |  ├── karma.conf.js
|  |  ├── src
|  |  ├── tsconfig.app.json
|  |  └── tsconfig.spec.json
|  ├── projectman-portal
|  |  ├── jest.config.js
|  |  ├── src
|  |  ├── tsconfig.app.json
|  |  ├── tsconfig.editor.json
|  |  ├── tsconfig.json
|  |  └── tsconfig.spec.json
|  └── shared
|     └── angular
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在angular下新建一个component文件夹，并使用 NG CLI 命令快速创建一个member模块：</p>
<pre><code class="copyable">cd apps/shared/angular/component

// 新建模块
ng g m member-list

// 在模块下新建组件
ng g c member-list
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">├── apps
|  └── shared
|     └── angular
|        └── component
|           └── member-list
|              ├── member-list.component.html
|              ├── member-list.component.scss
|              ├── member-list.component.spec.ts
|              ├── member-list.component.ts
|              └── member-list.module.ts
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">在业务中使用</h2>
<p>我们在my-portal和projectman-portal两个业务中都使用menber-list组件。</p>
<h3 data-id="heading-7">导入member模块</h3>
<p>apps/my-portal/src/app/app.module.ts</p>
<p>apps/projectman-portal/src/app/app.module.ts</p>
<pre><code class="copyable">import &#123; MemberListModule &#125; from '@component/member-list/member-list.module';

  imports: [
    MemberListModule,
  ],
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">使用member组件</h3>
<p>apps/my-portal/src/app/app.component.html</p>
<p>apps/projectman-portal/src/app/app.component.html</p>
<pre><code class="copyable"><app-member-list></app-member-list>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>由于有热加载，保存后马上就能实时看到页面效果</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a2af27e7e2bc43129ba9edc9285a84e0~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97a340b1617f4d96b2460dc46290d2d5~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">配置tsconfig</h2>
<p>为了引入方便，我们在tsconfig中配置了<code>@component</code>路径别名。</p>
<p>tsconfig.base.json</p>
<pre><code class="copyable">    "paths": &#123;
      "@shared/*": ["apps/shared/*"],
      "@component/*": ["apps/shared/angular/component/*"]
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样在业务中使用公共组件，就不用写很长的<code>../../</code>，直接使用<code>@component</code>别名即可：</p>
<pre><code class="copyable">import &#123; MemberListModule &#125; from '@component/member-list/member-list.module';
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-10">增加一个 React 项目</h1>
<p>除了Angular项目，我们还可以在 Monorepo 工作空间中增加别的框架的项目，比如：React。</p>
<p>增加React项目的方式和Angular类似，只是需要增加一个<code>@nrwl/react</code>依赖：</p>
<pre><code class="copyable">npm i -D @nrwl/react

npx nx g @nrwl/react:app workitem-portal
<span class="copy-code-btn">复制代码</span></code></pre>
<p>要不然会报以下错误：</p>
<pre><code class="copyable">Unable to resolve @nrwl/react:app.
Cannot find module '@nrwl/react/package.json'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>创建完会在apps目录下新增一个<code>workitem-portal</code>：</p>
<pre><code class="copyable">├── apps
|  ├── my-portal
|  ├── projectman-portal
|  ├── workitem-portal // 新增的
<span class="copy-code-btn">复制代码</span></code></pre>
<p>启动方式也是一样的：</p>
<pre><code class="copyable">npx nx serve workitem-portal --port 4200
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们注意到启动时报了一个错：</p>
<pre><code class="copyable">ERROR in /Users/kagol/Documents/Kagol/code/devcloud-portal/apps/workitem-portal/src/app/app.tsx(10,5):
TS17004: Cannot use JSX unless the '--jsx' flag is provided.
<span class="copy-code-btn">复制代码</span></code></pre>
<p>需要在<code>workitem-portal/tsconfig.json</code>中作相应的配置：</p>
<pre><code class="copyable">&#123;
  "compileOnSave": false,
  "compilerOptions": &#123;
    ...
    "jsx": "preserve", // "jsx": "react-jsx"
    ...
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>访问链接：</p>
<p><a href="http://localhost:4200/" target="_blank" rel="nofollow noopener noreferrer">http://localhost:4200/</a></p>
<p>可以看到我们的React项目也能正常启动：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/481720b5df074220adcce4ff9a431c35~tplv-k3u1fbpfcp-watermark.image" alt="图片.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>按照同样的步骤，我们可以扩展出很多子项目，它们之间共同同样的工作流，同样的公共代码，非常方便和高效，赶紧试试吧！</p>
<h2 data-id="heading-11">增加启动和构建脚本</h2>
<p>为了方便地启动和管理多个项目，可以在<code>package.json</code>中增加启动和构建的脚本：</p>
<pre><code class="copyable">"start": "npx nx serve devcloud-portal --port 4200 --open",
"start:projectman-portal": "npx nx serve projectman-portal --port 4210",
"start:workitem-portal": "npx nx serve workitem-portal --port 4220",

"build:devcloud-portal": "npx nx build devcloud-portal --prod",
"build:projectman-portal": "npx nx build projectman-portal --prod",
"build:workitem-portal": "npx nx build workitem-portal --prod",
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-12">小结</h1>
<p>本文先是与大家分享如何将一个现有的Angular CLI工程“变成”Monorepo工作空间，然后对其进行扩展，比如增加Angular项目、增加React项目，增加公共模块等，有了Monorepo，我们就可以将自己组织的所有项目代码统一到一个仓库里，共享同一套工作流，同一套规范，同一套公共基础库，大大地提升了团队协作和开发的效率。</p>
<p>如果觉得好用，不妨在你的组织尝试下吧！</p>
<p>欢迎加DevUI小助手微信：devui-official，一起讨论Angular技术和前端技术。</p>
<p>欢迎关注我们<a href="https://devui.design/" target="_blank" rel="nofollow noopener noreferrer">DevUI</a>组件库，点亮我们的小星星🌟：</p>
<p><a href="https://github.com/devcloudfe/ng-devui" target="_blank" rel="nofollow noopener noreferrer">github.com/devcloudfe/…</a></p>
<p>也欢迎使用DevUI新发布的<a href="https://devui.design/admin/" target="_blank" rel="nofollow noopener noreferrer">DevUI Admin</a>系统，开箱即用，10分钟搭建一个美观大气的后台管理系统！</p>
<h1 data-id="heading-13">加入我们</h1>
<p>我们是DevUI团队，欢迎来这里和我们一起打造优雅高效的人机设计/研发体系。招聘邮箱：<a href="mailto:muyang2@huawei.com">muyang2@huawei.com</a>。</p>
<p>文/DevUI Kagol</p>
<p>往期文章推荐</p>
<p><a href="https://juejin.cn/post/6968616701709516836" target="_blank">《今天是儿童节，整个贪吃蛇到编辑器里玩儿吧》</a></p>
<p><a href="https://juejin.cn/post/6968104416784171039" target="_blank">《如何将龙插入到编辑器中？》</a></p>
<p><a href="https://juejin.cn/post/6966993945973194765" target="_blank">《Quill富文本编辑器的实践》</a></p>
<p><a href="https://juejin.cn/post/6967931817215131656" target="_blank">《StepsGuide：一个像跟屁虫一样的组件》</a></p>
<p><a href="https://juejin.cn/post/6956155033410863134" target="_blank">《号外号外！DevUI Admin V1.0 发布啦！》</a></p></div>  
</div>
            