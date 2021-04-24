
---
title: '【得物技术】前端项目使用Sentry错误监控实践'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1ecb17bd3c74f0a871731091aa4c551~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 23 Apr 2021 02:48:29 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1ecb17bd3c74f0a871731091aa4c551~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>鉴于前端正在向多元化方向发展，场景愈加复杂，生产环境也经常会出现一些本地环境和测试环境无法复现的问题。而且，用户的具体行为和操作我们也不可预期，后端错误监控又只能监测到发起请求后的错误日志，那么错误发生时我们就只能靠用户反馈。但是这种反馈不是实时的，往往也只有截图或者文字描述，无法提供我们需要的其他关键信息，加上生产环境的静态资源文件一般都是经过混淆压缩，我们拿到的报错堆栈信息也没有太大含义。</p>
<p>因此，前端项目更加需要一套成熟的错误监控系统，能够帮助我们实时的监控项目运行状态，提供丰富的详细的错误信息，甚至能够提供场景还原能力。让开发人员能够及时对报错进行跟进解决。</p>
<p>本文着重讲解一下前端项目接入Sentry的步骤和规则设置以及其他Sentry后台使用。</p>
<h1 data-id="heading-1">为何选择Sentry</h1>
<ol>
<li>市场已有的成熟的监控平台</li>
</ol>
<ul>
<li><a href="https://www.fundebug.com/" target="_blank" rel="nofollow noopener noreferrer">Fundebug</a></li>
<li><a href="https://www.bugsnag.com/" target="_blank" rel="nofollow noopener noreferrer">Bugsnag</a></li>
<li>Badjs</li>
<li><a href="https://sentry.io/welcome/" target="_blank" rel="nofollow noopener noreferrer">Sentry</a></li>
</ul>
<ol start="2">
<li>Sentry的优势</li>
</ol>
<ul>
<li>开源，有免费版</li>
<li>可以部署自己的服务器，安全</li>
<li>错误信息及告警机制完善</li>
<li>简单易上手，开发成本低</li>
<li>错误追踪及状态流转及时，方便</li>
<li>丰富的SDK</li>
<li>社区活跃</li>
</ul>
<p>综合对比，Sentry的这些优势既能及时抓取生产环境的前端报错发出通知，又能够提供丰富的错误信息及路径方便开发人员定位解决，满足了前端项目错误监控的基本需求；又是开源免费的，可以搭建自己的服务器，不用担心数据及敏感信息泄露等风险，同时支持各种开发语言及框架。所以，最终选择了Sentry做为得物前端平台的错误监控方案。</p>
<h1 data-id="heading-2">简介</h1>
<blockquote>
<p>Sentry is a service that helps you monitor and fix crashes in realtime. The server is in Python, but it contains a full API for sending events from any language, in any application.</p>
</blockquote>
<p>Sentry是一项可帮助您实时监控和修复错误的服务。该服务器使用Python，但是它包含用于在任何应用程序中从任何语言发送事件的完整API。</p>
<ul>
<li>官网：<a href="https://sentry.io/" target="_blank" rel="nofollow noopener noreferrer">sentry.io</a></li>
<li>社区：<a href="https://forum.sentry.io/" target="_blank" rel="nofollow noopener noreferrer">forum.sentry.io</a></li>
</ul>
<h1 data-id="heading-3">概念</h1>
<ul>
<li>Event：事件。</li>
</ul>
<p>每次产生的日志记录，每个event有很多元信息，包括事件级别，项目信息，环境等。可通过点击具体事件对应的“JSON”数据进行查看</p>
<ul>
<li>Issue：问题。</li>
</ul>
<p>相同的地方产生的一个异常称为一个Issue（是同一类问题的聚合）。假如在同一个位置发生了两次报错，那么会产生两个Event事件，但是只有一个Issue。</p>
<ul>
<li>DSN：客户端（具体项目）密钥。</li>
</ul>
<p>DSN是一个url，包含相关密钥信息，客户端与服务端（sentry服务器）就是通过这个DSN进行通信，上报错误信息的。</p>
<ul>
<li>Auth Token：授权令牌。</li>
</ul>
<p>授权令牌允许基于你的账户使用Sentry API，我们主要用到使用@sentry/cli进行上传sourceMap文件等操作时，sentry/cli会基于Auth Token进行调用相应API方法。</p>
<ul>
<li>Org：组织名称。</li>
</ul>
<p>对应公司部署的sentry服务器上的组织名称。</p>
<ul>
<li>
<p>Release：版本号。</p>
</li>
<li>
<p>Project：客户端名称。（接入sentry的具体项目名）</p>
</li>
<li>
<p>Tag：标签。</p>
</li>
</ul>
<h1 data-id="heading-4">部署</h1>
<blockquote>
<p>虽然Sentry官方提供了免费版本，但是从安全角度和功能限制上我们还是建议自己搭建一个Sentry服务。官方提供了两种安装方式：通过Python安装或通过Docker安装。官方推荐使用Docker进行部署，由于官方文档介绍非常详细，这里不进行阐述，需要注意的是根据实际需求修改相应配置文件。</p>
</blockquote>
<ul>
<li>安装Docker-Compose</li>
<li>拉取Sentry仓库</li>
<li>修改对应配置文件</li>
<li>域名映射</li>
<li>创建管理员密码和用户</li>
</ul>
<h1 data-id="heading-5">接入</h1>
<h2 data-id="heading-6">1. 创建项目</h2>
<ul>
<li>Sentry服务器上创建一个新的项目：ProjectName（项目名），选择Team。</li>
<li>选择对应开发语言模板，这里选择Vue。</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e1ecb17bd3c74f0a871731091aa4c551~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-04-23 下午6.19.27.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-7">2. 工程接入Sentry</h2>
<ul>
<li>创建项目后，会弹出配置详细步骤文档，按照文档配置即可。</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f21492db17e749a38147d892e2a64ff3~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-04-23 下午6.20.02.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>安装依赖</li>
</ul>
<pre><code class="copyable">$ yarn add @sentry/browser -D
$ yarn add @sentry/integrations -D
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>入口文件处生成Sentry实例</li>
</ul>
<pre><code class="copyable">import Vue from 'vue'
import * as Sentry from '@sentry/browser'
import * as Integrations from '@sentry/integrations'
Sentry.init(&#123;
    dsn: 'https://xxx.sentry域名/项目id',
    integrations: [new Integrations.Vue(&#123;Vue, attachProps: true&#125;)],
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><em>P.S. 这里的dsn为刚刚创建项目对应的客户端密钥，在项目->设置->客户端密钥（DSN）出查看。</em></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf98928d079f49f0b21a6f145aea5a1b~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-04-23 下午6.21.33.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">3. 上传SourceMap</h2>
<blockquote>
<p>上述步骤完成以后，手动添加一个错误，启动项目就可以在Sentry服务器对应项目下看到对应的错误了。但是这里我们只能看到错误信息的描述，无法看到具体是哪个文件的哪一行报错，以及具体的错误信息。因为生产环境我们的资源文件都是经过混淆压缩的，接下来我们开始上传sourceMap到服务器，方便还原错误信息。</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2087be3de2a941658a4ca3d6e9334c6d~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-04-23 下午6.22.08.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Sentry官方提供了两种上传sourceMap的方式：使用Sentry-cli命令行和webpack插件。由于命令行方式太过繁琐，且与前端工程化概念脱离。因此采用webpack插件方式进行上传sourceMap文件。</p>
<ul>
<li>安装webpack插件</li>
</ul>
<pre><code class="copyable">yarn add @sentry/webpack-plugin -D
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>项目根目录下添加Sentry配置文件：.sentryclirc</li>
</ul>
<p><em>@sentry/cli上传sourcemap文件时会自动检查该配置文件下的信息，并使用</em></p>
<pre><code class="copyable">[defaults]
url=https://xxxxxx       //  - sentry服务器地址
org=xxx                  //  - 组织名称
project=projectname      //  - 项目名称
[auth]
token=xxx                //  - auth token
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/143622695a8846d98c2e31b436967f96~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-04-23 下午6.23.32.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>P.S. 注意，这里申请的Auth Token要选择project:read和project:releases权限。</strong></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/630905ceb16d495ea714a79e9af8315a~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-04-23 下午6.24.17.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>webpack配置文件添加插件</li>
</ul>
<pre><code class="copyable">const SentryCliPlugin = require('@sentry/webpack-plugin')
const version = '' // 版本号
config.devtool('source-map')
config.plugin('SentryCliPlugin').use(SentryCliPlugin, [&#123;
  release: version,
  // 打包后的代码目录 根据项目实际调整
  include: './dist',
  // url路径访问到的js资源前缀 根据项目实际调整 默认不用动
  // urlPrefix: "~/static/js/",
  ignore: ['node_modules'],
  setCommits: &#123;
    // ==================== 需要改成对应项目的git地址=============
    repo: 'https://xxx.xx.xx',
    // ==================== 需要改成对应项目的git地址=============
    auto: true,
  &#125;,
&#125;]
)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里有几个点需要注意：</p>
<ul>
<li>上传的SourceMap格式需要为"source-map"</li>
<li>版本号version可以根据实际情况及公司编码规范进行设置，且需要在入口处也填写这个版本号（保持一致）</li>
<li>urlPrefix设置需要跟实际资源路径一致（后面会具体讲解）</li>
</ul>
<h2 data-id="heading-9">4. 上传到sentry后删除SourceMap</h2>
<blockquote>
<p>因为@sentry/cli插件上传完sourcemap文件到sentry服务器后不会自动删除对应map文件，为保证站点代码安全性，需要上传后将map文件删除。</p>
</blockquote>
<ul>
<li>使用<a href="https://www.npmjs.com/package/clean-webpack-plugin" target="_blank" rel="nofollow noopener noreferrer">clean-webpack-plugin</a>插件</li>
</ul>
<pre><code class="copyable">config.plugins.push(
  new CleanWebpackPlugin(&#123;
    cleanAfterEveryBuildPatterns: ["./dist/js/*.js.map"]
  &#125;)
)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>使用rimraf，在postbuild脚本中执行删除</li>
</ul>
<pre><code class="copyable">"postbuild:prod": "rimraf ./dist/js/*.js.map"
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>在打包完成后上传文件到服务器时，排除map文件</li>
</ul>
<h2 data-id="heading-10">5. 区分环境</h2>
<blockquote>
<p>为避免项目无用告警信息过多，可以通过代码设置区分一下环境，针对不同环境做不同操作。这里是根据BUILD_ENV环境变量进行区分（脚本命令中注入）。下面几个地方需要做对应修改：（加粗部分为新增修改代码）</p>
</blockquote>
<ul>
<li>package.json脚本命令</li>
</ul>
<pre><code class="copyable">"build:test": "cross-env BUILD_ENV=test vue-cli-service build",
"build:prod": "cross-env BUILD_ENV=production vue-cli-service build",
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>入口文件生成实例处</li>
</ul>
<pre><code class="copyable">import Vue from 'vue'
import * as Sentry from '@sentry/browser'
import * as Integrations from '@sentry/integrations'
const isProd = process.env.BUILD_ENV === 'production'
isProd && Sentry.init(&#123;
    dsn: 'https://xxx.sentry域名/项目id',
    integrations: [new Integrations.Vue(&#123;Vue, attachProps: true&#125;)],
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>webpack配置文件处</li>
</ul>
<pre><code class="copyable">const SentryCliPlugin = require('@sentry/webpack-plugin')
const version = '' // 版本号
const isProd = process.env.BUILD_ENV === 'production'
config.when(isProd, config => &#123;
  config.devtool('source-map')
  config.plugin('SentryCliPlugin').use(SentryCliPlugin, [
    &#123;
      release: version,
      // 打包后的代码目录 根据项目实际调整
      include: './dist',
      // url路径访问到的js资源前缀 根据项目实际调整 默认不用动
      // urlPrefix: "~/static/js/",
      ignore: ['node_modules'],
      setCommits: &#123;
        // ==================== 需要改成对应项目的git地址=============
        repo: 'https://xxx.xx.xx',
        // ==================== 需要改成对应项目的git地址=============
        auto: true,
      &#125;,
    &#125;,
  ])
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>最后，也可以选择性修改Sentry异常上报方法</li>
</ul>
<pre><code class="copyable">import * as Sentry from '@sentry/browser'
const isProd = process.env.BUILD_ENV === 'production'
function ResetCaptureout(Sentry: any) &#123;
  if (isProd) return Sentry
  Sentry.captureException = function() &#123;
    const args = Array.prototype.slice.call(arguments).join(' ')
    return console.log('%csentry：', 'color:red;', args)
  &#125;
  Sentry.captureMessage = function() &#123;
    const args = Array.prototype.slice.call(arguments).join(' ')
    return console.log('%csentry：', 'color:green;', args)
  &#125;
  return Sentry
&#125;
Sentry = ResetCaptureout(Sentry)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-11">6. 完成上述步骤，重新部署以后可以到Sentry服务器上进行验证</h2>
<ul>
<li>查看是否生成对应版本：<strong>项目 -> 版本</strong></li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6fe29c50b89423abee272654179fb42~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-04-23 下午6.29.19.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>查看SourceMap文件是否上传成功：<strong>点击进入某一个版本 -> 工件（artifacts）</strong></li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b07777560a584bbfab7e81a9d62b98fb~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-04-23 下午6.30.09.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-12">7. 看到版本以及对应的工件上传成功就表示已经接入完成，这时再发生报错我们就能看到具体源码信息了。</h2>
<h1 data-id="heading-13">扩展</h1>
<ul>
<li>WebHook关联</li>
</ul>
<p>Sentry提供很多插件集成，除了邮件通知功能还可以接入飞书或者钉钉等其他企业办公软件进行有效快速的通知。</p>
<ul>
<li>路径：项目 -> 设置 -> Legacy Integrations -> 选择Webhook -> 打开开关 -> Configure plugin</li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d1f7059ddbaf4f6e97ddead3ed101bd2~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-04-23 下午6.31.07.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/00841df45db5492480d217cd4a8f8391~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-04-23 下午6.32.00.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>GitLab仓库集成</li>
</ul>
<blockquote>
<p>通过集成Gitlab仓库，我们可以将版本部署、提交记录，sentry issue等进行关联。</p>
</blockquote>
<ul>
<li>路径：Sentry -> 设置 -> 集成 -> GitLab -> Add</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f47f4992eda24a0ca33e4ba55bf1913d~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-04-23 下午6.32.40.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>点击Add Another以后会弹出详细操作说明</li>
<li>安装完以后可以选择Group下面对应的仓库进行添加</li>
<li>Issue关联</li>
</ul>
<blockquote>
<p>当Sentry上有新的报错产生时，可以选择将该报错信息作为一个issue关联到代码仓库上，比较简单，就不赘述了。效果如下图</p>
</blockquote>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83f2433a575f47dfaff987ecd49d86ca~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-04-23 下午6.33.20.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-14">告警设置</h1>
<blockquote>
<p>Sentry本身提供了组合项，可以根据具体业务及错误信息等实际情况进行选择设置。共有三种常见方式：告警规则设置、错误入站过滤器和Issue Owners指定。下面分别对这三种方式进行简单阐述说明。</p>
</blockquote>
<h2 data-id="heading-15">告警规则</h2>
<ol>
<li>设置路径</li>
</ol>
<p><strong>Sentry -> 项目 -> 设置 -> 警报 -> 编辑/新增</strong></p>
<ol start="2">
<li>可选项说明</li>
</ol>
<ul>
<li>An event is seen：当一个事件发生时</li>
<li>An issue is first seen：错误第一次出现</li>
<li>An issue changes state from resolved to unresolved：针对已修复问题复现场景</li>
<li>An issue changes state from ignored to unresolved：当xx条件下“忽略”的问题重新触发时进行提醒</li>
<li>An issue is seen more than xx times in xx time：对于一些已知的低级别，不影响使用的问题可以设置超过多少次以后再进行告警</li>
<li>An event's tags match xx equal to/does not equal xxx：根据事件标签值进行相应决策</li>
<li>An event's level is equal/does not equal xxx：选择事件级别（致命的/错误/警告/日志）</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0320eeadcf394f178f0c5bb4e340b4d2~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-04-23 下午6.34.37.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ol start="3">
<li>触发动作</li>
</ol>
<p>当产生的event符合告警规则时，触发的提醒动作。可以选Email或者其他集成。由于公司内部使用飞书作为日常办公IM，故这里设置为触发飞书WebHook。效果如下图：</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d4955d1ef87240d7b92ade8c9b0e2e46~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-04-23 下午6.34.58.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-16">入站过滤器</h2>
<p>通过入站过滤器可以针对某些版本、某些IP地址用户或者针对指定版本浏览器原因造成的问题进行过滤处理。最重要的是我们可以通过入站过滤器进行自定义过滤规则对一些已知可忽视问题进行设置，比如针对一些请求超时、没有权限，登录态失效等非代码健壮性问题。</p>
<ol start="4">
<li>设置路径</li>
</ol>
<p><strong>Sentry -> 项目 -> 设置 -> 入站过滤器</strong></p>
<ol start="5">
<li>查看过滤错误情况</li>
</ol>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c2b4219675d4fc2a9461a2b9603125e~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-04-23 下午6.35.35.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc34548b25654cbd8b733a970baeed09~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-04-23 下午6.35.49.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-17">Issue Owners</h2>
<p>通过Issue Owners选项我们可以在Issue发生时自动建立Issue与责任人关联关系，与此同时直接发送邮件或者飞书通知给对应负责的小伙伴。一共有两种设置方式，<strong>都是根据正则表达式进行匹配</strong>。</p>
<ol start="6">
<li>
<p>路径(path)：通过指定源文件所在目录及owners</p>
</li>
<li>
<p>页面路由(url)：通过指定具体页面路由及owners</p>
</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/865e1362011f470daaacd4bdbd5c20e2~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-04-23 下午6.46.06.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-18">错误解决方案</h1>
<ul>
<li>Resolve
<ul>
<li><strong>当前版本解决</strong>：发完版本以后，修改issue状态</li>
<li><strong>下个版本解决</strong>：issue发现后马上解决，代码跟随下个版本上线</li>
<li><strong>其他版本</strong>：一般不使用该选项</li>
</ul>
</li>
<li>Ignore
<ul>
<li><strong>时间维度</strong>：xx时间之前忽略（可自定义时间）</li>
<li><strong>数量维度</strong>：再出现xx次之前忽略</li>
<li><strong>用户维度</strong>：再有xx个用户复现这个错误之前忽略</li>
</ul>
</li>
</ul>
<h1 data-id="heading-19">原理</h1>
<h2 data-id="heading-20">前端错误类型</h2>
<ul>
<li>即时运行错误：代码错误</li>
<li>资源加载错误</li>
<li>图片加载错误</li>
</ul>
<h2 data-id="heading-21">上报错误的方法</h2>
<ul>
<li>利用网络请求进行上报</li>
<li>利用图片方式上报</li>
</ul>
<h2 data-id="heading-22">Sentry实现原理</h2>
<ol start="8">
<li>Init初始化，配置release和项目dsn等信息，然后将sentry对象挂载到全局对象上。</li>
<li>重写window.onerror方法。</li>
</ol>
<p>当代码在运行时发生错误时，js会抛出一个Error对象，这个error对象可以通过window.onerror方法获取。Sentry利用TraceKit对window.onerror方法进行了重写，对不同的浏览器差异性进行了统一封装处理。</p>
<ol start="10">
<li>重写window.onunhandledrejection方法。</li>
</ol>
<p>因为window.onerror事件无法获取promise未处理的异常，这时需要通过利用window.onunhandledrejection方法进行捕获异常进行上报。在这个方法里根据接收到的错误对象类型进行不同方式的处理。</p>
<ol>
<li>如果接收到的是一个ErrorEvent对象，那么直接取出它的error属性即可，这就是对应的error对象。</li>
<li>如果接收到的是一个DOMError或者DOMException，那么直接解析出name和message即可，因为这类错误通常是使用了已经废弃的DOMAPI导致的，并不会附带上错误堆栈信息。</li>
<li>如果接收到的是一个标准的错误对象，不做处理</li>
<li>如果接收到的是一个普通的JavaScript对象</li>
<li>使用Ajax上传</li>
</ol>
<p>当前端发生异常时，最终会调用Fetch请求上报到对应的Sentry服务器上，这里需要用到在初始化Sentry时传入的DSN。</p>
<h1 data-id="heading-23">踩坑记录</h1>
<ul>
<li>urlPrefix</li>
</ul>
<blockquote>
<p>在上传sourceMap文件时，不同项目打包后以及最终上传的静态资源文件路径可能有所区别。因此需要配置这个urlPrefix选项。该选项的意思是指项目上线后生产环境下对应的资源文件的完整路径。其中~表示网站根目录，下面举例说明：</p>
</blockquote>
<p>站点域名：<a href="https://www.demo.com/" target="_blank" rel="nofollow noopener noreferrer">www.demo.com</a></p>
<p>静态资源路径：</p>
<p><a href="https://www.demo.com/assets/js/1.js" target="_blank" rel="nofollow noopener noreferrer">www.demo.com/assets/js/1…</a></p>
<p><a href="https://www.demo.com/assets/js/1.js.map" target="_blank" rel="nofollow noopener noreferrer">www.demo.com/assets/js/1…</a></p>
<p>那么这里：~ = <a href="https://www.demo.com/" target="_blank" rel="nofollow noopener noreferrer">www.demo.com</a></p>
<p>urlPrefix选项应该配置为：~/assets/js/</p>
<p><strong>P.S. 默认为~/static/js/</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2482392255e4416f8522c1ba73c65cd8~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-04-23 下午6.48.59.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上面这张图为例：</p>
<p>Sentry拉取资源的时候路径为：域名/js/chunk-xxxx.js</p>
<ul>
<li>sourceMap需要为“source-map”类型，否则无法还原错误。</li>
<li>DSN配置为HTTPS协议头，因此需要处理跨域问题。</li>
<li>sentry报错可以通过控制台Network选项进行查看。</li>
<li><em>遇到问题多跑跑sentry社区，或者扒一下之前的issue记录，能解决80%的问题。</em></li>
</ul>
<h1 data-id="heading-24">总结</h1>
<p>前端项目业务场景日益复杂，经常会出现一些诡异的Bug，测试也很难覆盖到100%场景。某些小的代码问题很有可能造成一些意想不到的后果。与其等待用户发现问题反馈时背锅，不如通过监控系统及早发现，趁带来实际损失之前将其夭折。</p>
<h1 data-id="heading-25">参考文献</h1>
<p><a href="https://www.feishu.cn/hc/zh-CN/articles/360044955173" target="_blank" rel="nofollow noopener noreferrer">www.feishu.cn/hc/zh-CN/ar…</a>
<a href="https://zhuanlan.zhihu.com/p/75385179" target="_blank" rel="nofollow noopener noreferrer">zhuanlan.zhihu.com/p/75385179</a>
<a href="https://juejin.cn/post/6844904114028019719" target="_blank">juejin.cn/post/684490…</a>
<a href="https://zhuanlan.zhihu.com/p/75577689" target="_blank" rel="nofollow noopener noreferrer">zhuanlan.zhihu.com/p/75577689</a>
<a href="https://zhuanlan.zhihu.com/p/89539449" target="_blank" rel="nofollow noopener noreferrer">zhuanlan.zhihu.com/p/89539449</a></p>
<p>文｜Evan</p>
<p>关注得物技术，携手走向技术的云端</p></div>  
</div>
            