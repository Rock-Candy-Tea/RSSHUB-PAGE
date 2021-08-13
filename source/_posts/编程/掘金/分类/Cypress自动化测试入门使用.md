
---
title: 'Cypress自动化测试入门使用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f8f66aa31d44069befba12d1ed12512~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 12 Aug 2021 04:33:30 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f8f66aa31d44069befba12d1ed12512~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">起因</h2>
<p>在一次埋点需求过程中，为了方便测试删了官网的下载功能，忘了改回来就上线了。因为没有功能性的开发，涉及的页面比较多也只是让产品玩玩埋点上报，没有经过测试所以也没有人发现。</p>
<p>官网的业务比较简单，存在的意义就是介绍产品，提供地址让用户下载产品，介绍产品的目的也是为了让用户去下载使用，小小的下载功能一旦罢工，就直接意味着客户的流失。为了确保这些核心但是简单不引起测试同事注意的功能在迭代过程中不丢失不出问题，我们决定在项目中引入自动化测试。</p>
<h2 data-id="heading-1">为什么选择Cypress</h2>
<p>Cypress就是前端E2E测试框架，E2E就是end-to-end。我要测试的功能很简单，点击下载客户端和用户提交消息两个功能。站在用户和测试的角度，他们并不关心前端的使用什么框架什么逻辑写的，只想知道浏览器上的交互效果，ui展示效果是不是正确的，功能使用上是不是正确的，按这种思路测试，也叫E2E测试。</p>
<p>除了业务场景适用之外，我选择它最主要还是因为它基于node js，对前端开发者来说上手快。</p>
<h2 data-id="heading-2">使用</h2>
<h3 data-id="heading-3">安装</h3>
<p>进入到需要接入Cypress的项目目录下</p>
<pre><code class="copyable">cd /your/project/path 
<span class="copy-code-btn">复制代码</span></code></pre>
<p>安装cypress，我这里是使用npm下载依赖，版本号是8.1.0</p>
<pre><code class="copyable">npm install cypress --save-dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>vs code终端执行cypress open，开启cypress</p>
<pre><code class="copyable">./node_modules/.bin/cypress open
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">cypress文件夹</h3>
<p>open命令执行成功后，就会弹出一个小窗口。"1-getting-started"和"2-advanced-examples"目录下的是自带的测试用例。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1f8f66aa31d44069befba12d1ed12512~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>同时项目中会多出cypress的文件夹：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f759c4c79f9b4f82831e796abfe755bf~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>fixtures：存放测试数据的地方，可以理解为放接口mock数据的地方</li>
<li>integration： 一般测试用例会写在integration下面，自带官方示例测试用例文件。</li>
</ul>

<ul>
<li>plugins：存放插件，插件可以是自己编写的，也可以是第三方，插件是在项目加载之前、浏览器启动之前和测试执行期间在Node中执行用的。</li>
<li>support：cypress/support/index.js文件在每个规范文件之前运行，比如有些动作是适用于全局的，那么就可以放在这里。比如说，在cypress/support/index.js里增加如下代码：</li>
</ul>
<pre><code class="copyable">beforeEach(() => &#123;
  cy.log('在每个测试执行前都会运行')
&#125;)

// 运行后，会看到每个测试用例都会有个log输出。
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以 cypress run 方式运行测试时，当测试发生错误时，Cypress 会自动截图/录屏，并默认保存cypress/screenshots 文件夹下，而录屏会保存在 cypress/video 文件夹下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/66e04a05b5b54d41964c5ce932334284~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">编写测试案例</h3>
<p>思考测试和用户操作点击下载的过程：</p>
<ol>
<li>打开下载页</li>
<li>点击下载按钮</li>
</ol>

<ol start="3">
<li>等待客户端下载完成</li>
</ol>
<p>剩下的步骤，有bug也不是前端同学的锅了。</p>
<pre><code class="copyable">// cypress/integration/download.js

const path = require("path");

describe('The Home Page', () => &#123;
  it('successfully visit', () => &#123;
    cy.visit('http://localhost:3001')
  &#125;)

  it('successfully download', () => &#123;
    // 执行下载操作
    cy.contains('点我下载')
    .click()
    
    // 执行测试后，cypress文件夹下会多出downloads目录，存放测试过程中下载的文件
    const downloadsFolder = Cypress.config("downloadsFolder");
    const downloadedFilename = path.join(downloadsFolder, "下载文件.exe");
    // 读取文件
    cy.readFile(downloadedFilename).then(data => &#123;
    // 执行断言
    &#125;);
  &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>保存测试文件后，cypress的小窗会多出你的测试js文件，点击即可开启测试</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91ee506fc44a4aa396049fc4db22c9fa~tplv-k3u1fbpfcp-watermark.image" alt="企业微信截图_0d4a8a87-1874-4f7e-a025-90e9a5314b65.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如下图所示，访问下载页和下载客户端测试成功，界面左边是测试日志，中间是展示下载页，右边是浏览器控制台：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c8de71b41d54395bf6d53e7d0199a82~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是这里有个问题，想通过检测用户点击下载到下载是否成功，可能需要耗时很久。我并不想测试执行那么长的时间，所以采用另一种方法：将页面获取下载链接的接口代理到本地mock，获取a标签的链接和mock数据对比。</p>
<pre><code class="copyable">describe('The Home Page', () => &#123;
  before(() => &#123;
    // 拦截请求并传入mock数据
    cy.intercept('GET', '/Download.php', &#123; fixture: 'download.json' &#125;)
  &#125;)

  it('successfully loads', () => &#123;
    cy.visit('http://localhost:3001')
  &#125;)

  it('successfully request download api', () => &#123;
    // 获取mock数据
    cy.fixture('downloadv2.json').then((&#123; data = [] &#125;) => &#123;
      // cypress获取节点 a标签带上data-lbl属性
      cy.get(`[data-lbl=下载]`)
      .should('have.attr', 'href')
      .then(href=>&#123;
        expect(href).to.eq(config.FUrl)
      &#125;)
    &#125;)
  &#125;)
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">cypress的API</h3>
<p>下面是我接触到测试案例时遇到的一些常见的API，虽然官网有指导但是，但是刚开始接触不了解基本概念，还是有点一头雾水。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.cypress.io%2Fapi%2Ftable-of-contents" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.cypress.io/api/table-of-contents" ref="nofollow noopener noreferrer">Cypress官网API文档传送门</a></p>
<h4 data-id="heading-7">测试套件和用例</h4>
<p>对于一条可执行的测试用例来说，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.cypress.io%2Fguides%2Freferences%2Fbundled-tools%23Mocha" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.cypress.io/guides/references/bundled-tools#Mocha" ref="nofollow noopener noreferrer">describe()</a>和<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.cypress.io%2Fguides%2Freferences%2Fbundled-tools%23Mocha" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.cypress.io/guides/references/bundled-tools#Mocha" ref="nofollow noopener noreferrer">it()</a>是两个必要的组成部分</p>
<ul>
<li>describe: 代表测试套件，里面可以设定 ，一个测试套件可以不包括任何钩子函数（Hook），但必须包含至少一条测试用例 it() ，能嵌套子测试套件</li>
<li>it: 代表一条测试用例</li>
</ul>
<p>context: 是 describe() 的别名，其行为方式是一致的，可以直接用 context() 代替 describe()</p>
<h4 data-id="heading-8">钩子函数</h4>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.cypress.io%2Fapi%2Fplugins%2Fbefore-run-api" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.cypress.io/api/plugins/before-run-api" ref="nofollow noopener noreferrer">before</a>() : 运行 cypress via cypress open时，打开项目时将触发该事件。每次cypress run执行时都会触发该事件。如上我的测试案例中，在测试之前将接口代理到mock数据，这样visit()接口打开页面时，节点上渲染的是mock数据。</li>
</ul>
<p>before会在第一个用例之前运行，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.cypress.io%2Fapi%2Fplugins%2Fafter-run-api" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.cypress.io/api/plugins/after-run-api" ref="nofollow noopener noreferrer">afeter</a>会在跑完所有的用例之后运行。<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.cypress.io%2Fguides%2Freferences%2Fbundled-tools%23Mocha" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.cypress.io/guides/references/bundled-tools#Mocha" ref="nofollow noopener noreferrer">beforeEach</a>会在每一个用例前运行，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.cypress.io%2Fguides%2Freferences%2Fbundled-tools%23Mocha" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.cypress.io/guides/references/bundled-tools#Mocha" ref="nofollow noopener noreferrer">afterEach</a>会在每一个用例结束后运行。</p>
<h4 data-id="heading-9">查找，操作dom节点</h4>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.cypress.io%2Fapi%2Fcommands%2Fget" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.cypress.io/api/commands/get" ref="nofollow noopener noreferrer">get()</a>: 用来在 DOM 树中查找 DOM 元素，get方法可以像jquery一样通过selector查找到对应的dom。</li>
</ul>
<p>还有其他查找方法如：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.cypress.io%2Fapi%2Fcommands%2Fchildren" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.cypress.io/api/commands/children" ref="nofollow noopener noreferrer">children</a>获取一组 DOM 元素中每个 DOM 元素的子元素, <a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.cypress.io%2Fapi%2Fcommands%2Fparent" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.cypress.io/api/commands/parent" ref="nofollow noopener noreferrer">parent</a>获取一组 DOM 元素的父 DOM 元素，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.cypress.io%2Fapi%2Fcommands%2Fsiblings" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.cypress.io/api/commands/siblings" ref="nofollow noopener noreferrer">siblings</a>获取兄弟 DOM 元素等。</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.cypress.io%2Fapi%2Fcommands%2Ftrigger%23Syntax" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.cypress.io/api/commands/trigger#Syntax" ref="nofollow noopener noreferrer">trigger()</a>: 在 DOM 元素上触发事件。如：</li>
</ul>
<pre><code class="copyable">// 触发dom的mouseover事件
dom.trigger('mouseover')

// 语法使用示例
// eventName（string）event 在DOM元素上要触发的的名称。
.trigger(eventName)

// position（string）
// 应该触发事件的位置。该center位置是默认位置。
// 有效的位置topLeft，top，topRight，left，center，right，bottomLeft，bottom，和bottomRight。
.trigger(eventName, position)

// options: 传递选项对象以更改的默认行为
.trigger(eventName, options)

// x（number）: 从元素左侧到触发事件的距离（单位px）。
// y（number）: 从元素顶部到触发事件的距离（单位px）。
.trigger(eventName, x, y)

.trigger(eventName, position, options)
.trigger(eventName, x, y, options)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-10">网络接口</h4>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.cypress.io%2Fapi%2Fcommands%2Fintercept%23Syntax" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.cypress.io/api/commands/intercept#Syntax" ref="nofollow noopener noreferrer">intercept</a>: 在网络层管理 HTTP 请求的行为</li>
</ul>
<p>如上我的测试案例中，就利用这个借口拦截请求，代理到我本地的mock数据</p>
<pre><code class="copyable">cy.intercept(url, staticResponse)
cy.intercept(method, url, staticResponse)
cy.intercept(routeMatcher, staticResponse)
cy.intercept(url, routeMatcher, staticResponse)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">Actions行为事件</h4>
<p>ui自动化操作页面上的元素，常用的方法输入如文本，点击元素，清空文本，点击按钮。还有一些特殊的checkbox,radio,滚动条等。cypress都可以api操作</p>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.cypress.io%2Fapi%2Fcommands%2Ftype" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.cypress.io/api/commands/type" ref="nofollow noopener noreferrer">type()</a>: 往输入框输入文本元素。<br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.cypress.io%2Fapi%2Fcommands%2Ffocus" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.cypress.io/api/commands/focus" ref="nofollow noopener noreferrer">focus()</a>: 聚焦DOM元素。<br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.cypress.io%2Fapi%2Fcommands%2Fclear" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.cypress.io/api/commands/clear" ref="nofollow noopener noreferrer">clear()</a>: 清空DOM元素。<br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.cypress.io%2Fapi%2Fcommands%2Frightclick" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.cypress.io/api/commands/rightclick" ref="nofollow noopener noreferrer">rightclick()</a>: 右击 DOM 元素<br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fdocs.cypress.io%2Fapi%2Fcommands%2Fselect%23Syntax" target="_blank" rel="nofollow noopener noreferrer" title="https://docs.cypress.io/api/commands/select#Syntax" ref="nofollow noopener noreferrer">select()</a>: select 选项框</li>
</ul>
<h3 data-id="heading-12">如何自动化</h3>
<p>这里有两个思路，一是把测试提前放到本地，在测试分支合并代码commit阶段触发自动测试，这样可以把问题抛出的步骤提前。第二个是接入到ci/cd上，解放部署，不用等待测试。我先尝试了在commit阶段触发。</p>
<h4 data-id="heading-13">添加 npm 脚本</h4>
<p>这里是指定了要执行的测试案例，不指定的话，默认所有的测试都会执行。</p>
<pre><code class="copyable">// package.json
"scripts": &#123;
    "test": "cypress run --spec cypress/integration/download.js",
    "pretest": "在这里执行打包，并运行服务的程序",
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">添加git钩子</h4>
<p>这里我是利用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fhusky" target="_blank" rel="nofollow noopener noreferrer" title="https://www.npmjs.com/package/husky" ref="nofollow noopener noreferrer">husky</a>创建git commit的钩子</p>
<p>下载husky, 我当前使用的版本是7.0.1：</p>
<pre><code class="copyable">npm install husky --save-dev
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在packgae.json中添加prepare脚本，prepare脚本会在npm install（不带参数）之后自动执行。也就是说当我们执行npm install安装完项目依赖后会执行 husky install命令，该命令会创建.husky/目录并指定该目录为git hooks所在的目录:</p>
<pre><code class="copyable">npm set-script prepare "husky install"
npm run prepare
<span class="copy-code-btn">复制代码</span></code></pre>
<p>添加commit的钩子：</p>
<pre><code class="copyable">npx husky add .husky/pre-commit "npm test"
git add .husky/pre-commit
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这样就实现了，在每次git commit阶段都会执行测试用例。</p>
<h2 data-id="heading-15">存在的问题</h2>
<ol>
<li>在vs code终端提交代码可以顺利进行测试，但是使用vs code的源代码管理工具则会报错。husky类似的<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ftypicode%2Fhusky%2Fissues%2F673" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/typicode/husky/issues/673" ref="nofollow noopener noreferrer">issue</a>还是开放的。据说可以通过降版本解决。</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a18cb211d32e4dfca8f3b6dc2ac96a10~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="2">
<li>在commit阶段触发会增加开发的等待时间，所以后续会尝试把测试接入到流水线上，和打包部署这些操作一样异步进行。</li>
</ol>
<p>后续新的尝试有进度我会继续更新，欢迎指正。</p></div>  
</div>
            