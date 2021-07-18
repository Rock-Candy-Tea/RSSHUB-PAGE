
---
title: 'Taro3.x 快速开发微信小程序以及 minidebug 小程序调试工具使用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8bd7cf545fe44e6193996c469030acbc~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 04 Jul 2021 02:02:22 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8bd7cf545fe44e6193996c469030acbc~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>「本文已参与好文召集令活动，点击查看:<a href="https://juejin.cn/post/6978685539985653767" target="_blank" title="https://juejin.cn/post/6978685539985653767">后端、大前端双赛道投稿，2万元奖池等你挑战！</a></p>
</blockquote>
<h2 data-id="heading-0">前言</h2>
<blockquote>
<p>最近公司准备开发一款扫码开票类型的微信小程序，时间紧，任务急。第一反应就是打开小程序开放平台查看开发文档，哦豁，官方的组件也太少了吧，难道要自己手写吗 ？ 经过多方调研，了解目前市面上比较流行的小程序开发框架有 <strong>Uniapp</strong>、<strong>Taro</strong> 。因为目前公司技术栈完全使用的 react hooks + ts 开发，所以在框架选择上自然就选择了 Taro 。</p>
</blockquote>
<h2 data-id="heading-1">Taro 简介</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8bd7cf545fe44e6193996c469030acbc~tplv-k3u1fbpfcp-zoom-1.image" alt="Taro 多端统一开发解决方案" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Taro 是一个开放式跨端跨框架解决方案，支持使用 React/Vue/Nerv 等框架来开发 微信 / 京东 / 百度 / 支付宝 / 字节跳动 / QQ 小程序 / H5 / RN 等应用。
现如今市面上端的形态多种多样，Web、React Native、微信小程序等各种端大行其道。当业务要求同时在不同的端都要求有所表现的时候，针对不同的端去编写多套代码的成本显然非常高，这时候只编写一套代码就能够适配到多端的能力就显得极为需要。</p>
<h2 data-id="heading-2">安装及使用</h2>
<p>Taro 项目基于 node，请确保已具备较新的 <strong>node 环境（>=12.0.0）</strong>，推荐使用 node 版本管理工具 nvm 来管理 node，这样不仅可以很方便地切换 node 版本，而且全局安装时候也不用加 sudo 了。</p>
<h2 data-id="heading-3">CLI 工具安装</h2>
<p>首先，你需要使用 npm 或者 yarn 全局安装 @tarojs/cli，或者直接使用 npx:</p>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 使用 npm 安装 CLI</span>
npm install -g @tarojs/cli

<span class="hljs-comment"># OR 使用 yarn 安装 CLI</span>
yarn global add @tarojs/cli

<span class="hljs-comment"># OR 安装了 cnpm，使用 cnpm 安装 CLI</span>
cnpm install -g @tarojs/cli
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>npm 5.2+ 也可在不全局安装的情况下使用 npx 创建模板项目：</p>
</blockquote>
<pre><code class="hljs language-bash copyable" lang="bash"> npx @tarojs/cli init taro_init_template
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>这里为了方便快捷，建议直接使用 <strong>npx</strong> 创建模板项目哈</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26bf716185364f62b9a933a50bc76055~tplv-k3u1fbpfcp-zoom-1.image" alt="模板创建：react + ts + sass + taro ui " loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">运行&启动项目</h2>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># yarn</span>
 yarn dev:weapp
 yarn build:weapp

<span class="hljs-comment"># npm script</span>
 npm run dev:weapp
 npm run build:weapp

<span class="hljs-comment"># 仅限全局安装</span>
 taro build --<span class="hljs-built_in">type</span> weapp --watch
 taro build --<span class="hljs-built_in">type</span> weapp

<span class="hljs-comment"># npx 用户也可以使用</span>
 npx taro build --<span class="hljs-built_in">type</span> weapp --watch
 npx taro build --<span class="hljs-built_in">type</span> weapp

<span class="hljs-comment"># watch 同时开启压缩</span>
$ <span class="hljs-built_in">set</span> NODE_ENV=production && taro build --<span class="hljs-built_in">type</span> weapp --watch <span class="hljs-comment"># Windows</span>
$ NODE_ENV=production taro build --<span class="hljs-built_in">type</span> weapp --watch <span class="hljs-comment"># Mac</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以上是微信小程序的编译命令，其它小程序编译可以查看项目文件夹下的 package.json 文件夹</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/610d1289990049219a445cc446caf08f~tplv-k3u1fbpfcp-zoom-1.image" alt="编译命令" loading="lazy" referrerpolicy="no-referrer"></p>
<p>运行小程序，你会发现在项目目录下多出了一个 dist 文件夹，打开微信开发者工具，用自己微信号登录，点击小程序界面的 <strong>+</strong> ，导入项目，项目名称自己定义，目录选择刚刚创建模板项目下的 <strong>dist</strong> 文件夹，<strong>AppId</strong> 可以暂时使用测试号哦，后期可以自己注册一个用于开发使用。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf3b420b4f8f40c49941efb9ef352c76~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3fbce8b8970840f49c28b26289ad9b79~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>[sitemap 索引情况提示] 根据 sitemap 的规则[0]，当前页面 [pages/index/index] 将被索引</p>
</blockquote>
<p><strong>遇到上述警告，可以设置 project.config.json => setting => checkSiteMap</strong></p>
<pre><code class="hljs language-json copyable" lang="json">&#123;
<span class="hljs-attr">"miniprogramRoot"</span>: <span class="hljs-string">"dist/"</span>,
<span class="hljs-attr">"projectname"</span>: <span class="hljs-string">"taro_template"</span>,
<span class="hljs-attr">"description"</span>: <span class="hljs-string">"taro_template"</span>,
<span class="hljs-attr">"appid"</span>: <span class="hljs-string">"touristappid"</span>,
<span class="hljs-attr">"setting"</span>: &#123;
<span class="hljs-attr">"urlCheck"</span>: <span class="hljs-literal">true</span>,
<span class="hljs-attr">"es6"</span>: <span class="hljs-literal">false</span>,
<span class="hljs-attr">"postcss"</span>: <span class="hljs-literal">false</span>,
<span class="hljs-attr">"preloadBackgroundData"</span>: <span class="hljs-literal">false</span>,
<span class="hljs-attr">"minified"</span>: <span class="hljs-literal">false</span>,
<span class="hljs-attr">"newFeature"</span>: <span class="hljs-literal">true</span>,
<span class="hljs-attr">"autoAudits"</span>: <span class="hljs-literal">false</span>,
<span class="hljs-attr">"coverView"</span>: <span class="hljs-literal">true</span>,
<span class="hljs-attr">"showShadowRootInWxmlPanel"</span>: <span class="hljs-literal">false</span>,
<span class="hljs-attr">"scopeDataCheck"</span>: <span class="hljs-literal">false</span>,
<span class="hljs-attr">"useCompilerModule"</span>: <span class="hljs-literal">false</span>,
    <span class="hljs-comment">// 这里添加哦</span>
<span class="hljs-attr">"checkSiteMap"</span>:<span class="hljs-literal">false</span>
&#125;,
<span class="hljs-attr">"compileType"</span>: <span class="hljs-string">"miniprogram"</span>,
<span class="hljs-attr">"simulatorType"</span>: <span class="hljs-string">"wechat"</span>,
<span class="hljs-attr">"simulatorPluginLibVersion"</span>: &#123;&#125;,
<span class="hljs-attr">"condition"</span>: &#123;&#125;
&#125;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">快速创建新页面 & 增加 TabBar</h2>
<blockquote>
<p><strong>Taro create --name [页面名称]</strong> 能够在当前项目的<strong>pages</strong>目录下快速生成新的页面文件，并填充基础代码，是一个提高开发效率的利器。
新增页面并且配置 <strong>app.config.ts</strong></p>
</blockquote>
<h4 data-id="heading-6">app.config.ts 完整配置</h4>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-attr">pages</span>: [
    <span class="hljs-string">"pages/index/index"</span>,
    <span class="hljs-string">"pages/setting/setting"</span>,
    <span class="hljs-comment">// "pages/login/login"</span>
  ],
  <span class="hljs-attr">subpackages</span>: [
    &#123;
      <span class="hljs-attr">root</span>: <span class="hljs-string">"pages/login/"</span>,
      <span class="hljs-attr">pages</span>: [
        <span class="hljs-string">"login"</span>
      ]
    &#125;
  ],
  <span class="hljs-attr">window</span>: &#123;
    <span class="hljs-attr">backgroundTextStyle</span>: <span class="hljs-string">"light"</span>,
    <span class="hljs-attr">navigationBarBackgroundColor</span>: <span class="hljs-string">"#fff"</span>,
    <span class="hljs-attr">navigationBarTitleText</span>: <span class="hljs-string">"WeChat"</span>,
    <span class="hljs-attr">navigationBarTextStyle</span>: <span class="hljs-string">"black"</span>
  &#125;,
  <span class="hljs-attr">tabBar</span>: &#123;
    <span class="hljs-attr">list</span>: [
      &#123;
        <span class="hljs-attr">pagePath</span>: <span class="hljs-string">"pages/index/index"</span>,
        <span class="hljs-attr">text</span>: <span class="hljs-string">"首页"</span>,
        <span class="hljs-attr">iconPath</span>: <span class="hljs-string">"assets/images/tab_index.png"</span>,
        <span class="hljs-attr">selectedIconPath</span>: <span class="hljs-string">"assets/images/tab_index_active.png"</span>
      &#125;,
      &#123;
        <span class="hljs-attr">pagePath</span>: <span class="hljs-string">"pages/setting/setting"</span>,
        <span class="hljs-attr">text</span>: <span class="hljs-string">"个人中心"</span>,
        <span class="hljs-attr">iconPath</span>: <span class="hljs-string">"assets/images/tab_setting.png"</span>,
        <span class="hljs-attr">selectedIconPath</span>: <span class="hljs-string">"assets/images/tab_setting_active.png"</span>
      &#125;
    ],
    <span class="hljs-attr">color</span>: <span class="hljs-string">"#BFBFBF"</span>,
    <span class="hljs-attr">selectedColor</span>: <span class="hljs-string">"#1296DB"</span>,
    <span class="hljs-attr">backgroundColor</span>: <span class="hljs-string">"#fff"</span>,
    <span class="hljs-attr">borderStyle</span>: <span class="hljs-string">"white"</span>
  &#125;
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>细心的同学可能会发现，app.config.ts 文件中增加了 subpackages 配置，下面来详细讲下这个配置的作用</p>
</blockquote>
<h2 data-id="heading-7">subpackages 分包</h2>
<blockquote>
<p>在小程序启动时，默认会下载主包并启动主包内页面，当用户进入分包内某个页面时，客户端会把对应分包下载下来，下载完成后再进行展示。</p>
</blockquote>
<p>目前小程序分包大小有以下限制：</p>
<ul>
<li>整个小程序所有分包大小不超过 <strong>20M</strong></li>
<li>单个分包/主包大小不能超过 <strong>2M</strong></li>
</ul>
<blockquote>
<p>注意：作为 tabbar 页面不能使用分包，可以使用分包的页面添加到 subpackages，且在 pages 中移除</p>
</blockquote>
<h2 data-id="heading-8">路由</h2>
<h5 data-id="heading-9">Taro.switchTab(option)</h5>
<blockquote>
<p>跳转到 tabBar 页面，并关闭其他所有非 tabBar 页面</p>
</blockquote>
<h5 data-id="heading-10">Taro.reLaunch(option)</h5>
<blockquote>
<p>关闭所有页面，打开到应用内的某个页面</p>
</blockquote>
<h5 data-id="heading-11">Taro.redirectTo(option)</h5>
<blockquote>
<p>关闭当前页面，跳转到应用内的某个页面。但是不允许跳转到 tabbar 页面。</p>
</blockquote>
<h5 data-id="heading-12">Taro.navigateTo(option)</h5>
<blockquote>
<p>保留当前页面，跳转到应用内的某个页面。但是不能跳到 tabbar 页面。使用 Taro.navigateBack 可以返回到原页面。小程序中页面栈最多十层。</p>
</blockquote>
<h5 data-id="heading-13">Taro.navigateBack(option)</h5>
<blockquote>
<p>关闭当前页面，返回上一页面或多级页面。可通过 getCurrentPages 获取当前的页面栈，决定需要返回几层。</p>
</blockquote>
<p>路由不做过多介绍，详细使用方法请参考官方文档。</p>
<h2 data-id="heading-14">请求封装 Taro.request</h2>
<h5 data-id="heading-15">定义统一状态</h5>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> HTTP_STATUS = &#123;
    <span class="hljs-attr">SUCCESS</span>: <span class="hljs-number">200</span>,
    <span class="hljs-attr">CREATED</span>: <span class="hljs-number">201</span>,
    <span class="hljs-attr">ACCEPTED</span>: <span class="hljs-number">202</span>,
    <span class="hljs-attr">CLIENT_ERROR</span>: <span class="hljs-number">400</span>,
    <span class="hljs-attr">AUTHENTICATE</span>: <span class="hljs-number">301</span>,
    <span class="hljs-attr">FORBIDDEN</span>: <span class="hljs-number">403</span>,
    <span class="hljs-attr">NOT_FOUND</span>: <span class="hljs-number">404</span>,
    <span class="hljs-attr">SERVER_ERROR</span>: <span class="hljs-number">500</span>,
    <span class="hljs-attr">BAD_GATEWAY</span>: <span class="hljs-number">502</span>,
    <span class="hljs-attr">SERVICE_UNAVAILABLE</span>: <span class="hljs-number">503</span>,
    <span class="hljs-attr">GATEWAY_TIMEOUT</span>: <span class="hljs-number">504</span>
  &#125;

  <span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> REFRESH_STATUS = &#123;
    <span class="hljs-attr">NORMAL</span>: <span class="hljs-number">0</span>,
    <span class="hljs-attr">REFRESHING</span>: <span class="hljs-number">1</span>,
    <span class="hljs-attr">NO_MORE_DATA</span>: <span class="hljs-number">2</span>
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-16">定义错误统一输出方法</h5>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> &#123; formatTime &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"../utils/common"</span>
<span class="hljs-comment">/**
 *
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> </span>name 错误名字
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> </span>action 错误动作描述
 * <span class="hljs-doctag">@param <span class="hljs-type">&#123;string&#125;</span> </span>info 错误信息，通常是 fail 返回的
 */</span>
<span class="hljs-comment">// eslint-disable-next-line</span>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> logError = <span class="hljs-function">(<span class="hljs-params">name: <span class="hljs-built_in">string</span>, action: <span class="hljs-built_in">string</span>, info?: <span class="hljs-built_in">string</span> | <span class="hljs-built_in">object</span> </span>) =></span> &#123;
  <span class="hljs-keyword">if</span> (!info) &#123;
    info = <span class="hljs-string">'empty'</span>
  &#125;
  <span class="hljs-keyword">let</span> time = formatTime(<span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>())
  <span class="hljs-built_in">console</span>.error(time, name, action, info)
  <span class="hljs-keyword">if</span> (<span class="hljs-keyword">typeof</span> info === <span class="hljs-string">'object'</span>) &#123;
    info = <span class="hljs-built_in">JSON</span>.stringify(info)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-17">定义 request.ts</h5>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> Taro <span class="hljs-keyword">from</span> <span class="hljs-string">'@tarojs/taro'</span>
<span class="hljs-keyword">import</span> &#123; HTTP_STATUS &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./status'</span>
<span class="hljs-keyword">import</span> &#123; logError &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./error'</span>
<span class="hljs-keyword">import</span> &#123; baseUrl &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'./baseUrl'</span>
<span class="hljs-keyword">import</span> &#123; checkLogin &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./auth"</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  <span class="hljs-function"><span class="hljs-title">baseOptions</span>(<span class="hljs-params">params, method = <span class="hljs-string">'GET'</span></span>)</span> &#123;
    <span class="hljs-keyword">let</span> &#123; url, data &#125; = params
    <span class="hljs-keyword">let</span> contentType = <span class="hljs-string">'application/json'</span>
    contentType = params.contentType || contentType
    <span class="hljs-keyword">type</span> OptionType = &#123;
      <span class="hljs-attr">url</span>: <span class="hljs-built_in">string</span>,
      data?: <span class="hljs-built_in">object</span> | <span class="hljs-built_in">string</span>,
      method?: <span class="hljs-built_in">any</span>,
      <span class="hljs-attr">header</span>: <span class="hljs-built_in">object</span>,
      <span class="hljs-comment">// mode: string,</span>
      <span class="hljs-attr">success</span>: <span class="hljs-built_in">any</span>,
      <span class="hljs-attr">error</span>: <span class="hljs-built_in">any</span>,
      <span class="hljs-attr">xhrFields</span>: <span class="hljs-built_in">object</span>,
    &#125;
    <span class="hljs-keyword">const</span> setCookie = <span class="hljs-function">(<span class="hljs-params">res: &#123;
      cookies: <span class="hljs-built_in">Array</span><&#123;
        name: <span class="hljs-built_in">string</span>,
        value: <span class="hljs-built_in">string</span>,
        expires: <span class="hljs-built_in">string</span>,
        path: <span class="hljs-built_in">string</span>
      &#125;>,
      header: &#123;
        <span class="hljs-string">'Set-Cookie'</span>: <span class="hljs-built_in">string</span>
      &#125;
    &#125;</span>) =></span> &#123;
      <span class="hljs-keyword">if</span> (res.cookies && res.cookies.length > <span class="hljs-number">0</span>) &#123;
        <span class="hljs-keyword">let</span> cookies = Taro.getStorageSync(<span class="hljs-string">'cookies'</span>) || <span class="hljs-string">''</span>;
        res.cookies.forEach(<span class="hljs-function">(<span class="hljs-params">cookie, index</span>) =></span> &#123;
          <span class="hljs-comment">// windows的微信开发者工具返回的是cookie格式是有name和value的,在mac上是只是字符串的</span>
          <span class="hljs-keyword">if</span> (cookie.name && cookie.value) &#123;
            cookies += index === res.cookies.length - <span class="hljs-number">1</span> ? <span class="hljs-string">`<span class="hljs-subst">$&#123;cookie.name&#125;</span>=<span class="hljs-subst">$&#123;cookie.value&#125;</span>;expires=<span class="hljs-subst">$&#123;cookie.expires&#125;</span>;path=<span class="hljs-subst">$&#123;cookie.path&#125;</span>`</span> : <span class="hljs-string">`<span class="hljs-subst">$&#123;cookie.name&#125;</span>=<span class="hljs-subst">$&#123;cookie.value&#125;</span>;`</span>
          &#125; <span class="hljs-keyword">else</span> &#123;
            cookies += <span class="hljs-string">`<span class="hljs-subst">$&#123;cookie&#125;</span>;`</span>
          &#125;
        &#125;);
        Taro.setStorageSync(<span class="hljs-string">'cookies'</span>, cookies)
      &#125;
      <span class="hljs-comment">// if (res.header && res.header['Set-Cookie']) &#123;</span>
      <span class="hljs-comment">//   Taro.setStorageSync('cookies', res.header['Set-Cookie'])</span>
      <span class="hljs-comment">// &#125;</span>
    &#125;
    <span class="hljs-keyword">const</span> option: OptionType = &#123;
      <span class="hljs-attr">url</span>: url.indexOf(<span class="hljs-string">'http'</span>) !== -<span class="hljs-number">1</span> ? url : baseUrl + url,
      <span class="hljs-attr">data</span>: data,
      <span class="hljs-attr">method</span>: method,
      <span class="hljs-attr">header</span>: &#123;
        <span class="hljs-string">'content-type'</span>: contentType,
        <span class="hljs-comment">// 增加请求头</span>
        <span class="hljs-attr">cookie</span>: Taro.getStorageSync(<span class="hljs-string">'cookies'</span>)
      &#125;,
      <span class="hljs-comment">// mode: 'cors',</span>
      <span class="hljs-attr">xhrFields</span>: &#123; <span class="hljs-attr">withCredentials</span>: <span class="hljs-literal">true</span> &#125;,
      <span class="hljs-function"><span class="hljs-title">success</span>(<span class="hljs-params">res</span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'res'</span>, res)
        setCookie(res)
        <span class="hljs-keyword">if</span> (res.statusCode === HTTP_STATUS.NOT_FOUND) &#123;
          <span class="hljs-keyword">return</span> logError(<span class="hljs-string">'api'</span>, <span class="hljs-string">'请求资源不存在'</span>)
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (res.statusCode === HTTP_STATUS.BAD_GATEWAY) &#123;
          <span class="hljs-keyword">return</span> logError(<span class="hljs-string">'api'</span>, <span class="hljs-string">'服务端出现了问题'</span>)
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (res.statusCode === HTTP_STATUS.FORBIDDEN) &#123;
          <span class="hljs-keyword">return</span> logError(<span class="hljs-string">'api'</span>, <span class="hljs-string">'没有权限访问'</span>)
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (res.statusCode === HTTP_STATUS.AUTHENTICATE) &#123;
          Taro.clearStorage()
          <span class="hljs-comment">//跳转到登录页面</span>
          checkLogin()
          <span class="hljs-keyword">return</span> logError(<span class="hljs-string">'api'</span>, <span class="hljs-string">'请先登录'</span>)
        &#125; <span class="hljs-keyword">else</span> <span class="hljs-keyword">if</span> (res.statusCode === HTTP_STATUS.SUCCESS) &#123;
          <span class="hljs-keyword">return</span> res.data
        &#125;
      &#125;,
      <span class="hljs-function"><span class="hljs-title">error</span>(<span class="hljs-params">e</span>)</span> &#123;
        logError(<span class="hljs-string">'api'</span>, <span class="hljs-string">'请求接口出现问题'</span>, e)
      &#125;
    &#125;
    <span class="hljs-comment">// eslint-disable-next-line</span>
    <span class="hljs-keyword">return</span> Taro.request(option)
  &#125;,
  <span class="hljs-function"><span class="hljs-title">get</span>(<span class="hljs-params">url, data?: <span class="hljs-built_in">object</span></span>)</span> &#123;
    <span class="hljs-keyword">let</span> option = &#123; url, data &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.baseOptions(option)
  &#125;,
  <span class="hljs-attr">post</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">url, data?: <span class="hljs-built_in">object</span>, contentType?: <span class="hljs-built_in">string</span></span>) </span>&#123;
    <span class="hljs-keyword">let</span> params = &#123; url, data, contentType &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.baseOptions(params, <span class="hljs-string">'POST'</span>)
  &#125;,
  <span class="hljs-function"><span class="hljs-title">put</span>(<span class="hljs-params">url, data?: <span class="hljs-built_in">object</span></span>)</span> &#123;
    <span class="hljs-keyword">let</span> option = &#123; url, data &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.baseOptions(option, <span class="hljs-string">'PUT'</span>)
  &#125;,
  <span class="hljs-function"><span class="hljs-title">delete</span>(<span class="hljs-params">url, data?: <span class="hljs-built_in">object</span></span>)</span> &#123;
    <span class="hljs-keyword">let</span> option = &#123; url, data &#125;
    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.baseOptions(option, <span class="hljs-string">'DELETE'</span>)
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-18">定义 baseUrl.ts</h5>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> baseUrl = <span class="hljs-string">'http://172.36.0.26:3000'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-19">定义 api.ts</h5>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> request <span class="hljs-keyword">from</span> <span class="hljs-string">"./request"</span>

<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> getDetail = (params):<span class="hljs-built_in">Promise</span><<span class="hljs-built_in">any</span>>=>&#123;
    <span class="hljs-keyword">return</span> request.get(<span class="hljs-string">'/url'</span>, params)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-20">组件中使用</h5>
<pre><code class="hljs language-typescript copyable" lang="typescript">  <span class="hljs-keyword">const</span> getDetail = <span class="hljs-function">()=></span>&#123;
    api.getDetail(&#123;
      <span class="hljs-attr">data</span>: <span class="hljs-number">1232</span>
    &#125;).then(<span class="hljs-function">(<span class="hljs-params">res</span>)=></span>&#123;
      <span class="hljs-built_in">console</span>.log(res)
    &#125;)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-21">Dva 集成使用</h2>
<blockquote>
<p>react 状态状态管理库： Redux，<strong>Dva</strong>，Mobx ... 本次搭建采用 Dva 来搭建，终于为什么选用 <strong>Dva</strong> ，完全就是为了尝鲜，因为以前项目中一直使用的 redux,redux 的繁琐想必大家也是知道的。大家也可以去尝试下使用 Mobx 。Mobx 可以称得上是这几个库中最简洁的库了。</p>
</blockquote>
<blockquote>
<p>当然了，hooks 中的 <strong>useContext()</strong> 也是组件之间共享状态的一种方案。</p>
</blockquote>
<h5 data-id="heading-22">安装</h5>
<pre><code class="hljs language-bash copyable" lang="bash">npm install --save dva-core dva-loading
npm install --save redux react-redux redux-thunk redux-logger
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-23">新增 src/utils/dva.ts</h4>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-comment">// src/utils/dva.ts</span>
<span class="hljs-keyword">import</span> &#123;create &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'dva-core'</span>;
<span class="hljs-comment">// import &#123;createLogger &#125; from 'redux-logger';</span>
<span class="hljs-keyword">import</span> createLoading <span class="hljs-keyword">from</span> <span class="hljs-string">'dva-loading'</span>;

<span class="hljs-keyword">let</span> app: &#123;<span class="hljs-attr">use</span>: <span class="hljs-function">(<span class="hljs-params">arg0: <span class="hljs-built_in">any</span></span>) =></span> <span class="hljs-built_in">void</span>; model: <span class="hljs-function">(<span class="hljs-params">arg0: <span class="hljs-built_in">any</span></span>) =></span> <span class="hljs-built_in">any</span>; start: <span class="hljs-function">() =></span> <span class="hljs-built_in">void</span>; _store: <span class="hljs-built_in">any</span>; getStore: <span class="hljs-function">() =></span> <span class="hljs-built_in">any</span>; dispatch: <span class="hljs-built_in">any</span>&#125;;
<span class="hljs-keyword">let</span> store: &#123;<span class="hljs-attr">dispatch</span>: <span class="hljs-built_in">any</span>&#125;;
<span class="hljs-keyword">let</span> dispatch: <span class="hljs-built_in">any</span>;
<span class="hljs-keyword">let</span> registered: <span class="hljs-built_in">boolean</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">createApp</span>(<span class="hljs-params">opt: &#123;models: <span class="hljs-built_in">any</span>[]; initialState: <span class="hljs-built_in">any</span> &#125;</span>) </span>&#123;

  <span class="hljs-comment">// redux日志, 引用redux-logger</span>
  <span class="hljs-comment">// opt.onAction = [createLogger()];</span>
  app = create(opt);
  app.use(createLoading(&#123;&#125;));


  <span class="hljs-keyword">if</span> (!registered) opt.models.forEach(<span class="hljs-function">(<span class="hljs-params">model: <span class="hljs-built_in">any</span></span>) =></span> app.model(model));
  registered = <span class="hljs-literal">true</span>;
  app.start();

  store = app._store;
  app.getStore = <span class="hljs-function">() =></span> store;

  dispatch = store.dispatch;

  app.dispatch = dispatch;
  <span class="hljs-keyword">return</span> app;
&#125;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
  createApp,
  <span class="hljs-function"><span class="hljs-title">getDispatch</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> app.dispatch;
  &#125;,
  <span class="hljs-function"><span class="hljs-title">getStore</span>(<span class="hljs-params"></span>)</span> &#123; <span class="hljs-comment">// 这个是在非组件的文件中获取Store的方法, 不需要可以不暴露</span>
    <span class="hljs-keyword">return</span> app.getStore();
  &#125;,
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-24">新增 models 文件夹</h5>
<blockquote>
<p>models 下专门用来统一管理自己的数据</p>
</blockquote>
<p>models/index.ts</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">
<span class="hljs-keyword">import</span> &#123; GlobalModelState &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"./setting/types"</span>
<span class="hljs-keyword">import</span> setting <span class="hljs-keyword">from</span> <span class="hljs-string">"./setting/index"</span>


<span class="hljs-keyword">const</span> models:<span class="hljs-built_in">Array</span><GlobalModelState> = [
    setting
]

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> models
<span class="copy-code-btn">复制代码</span></code></pre>
<p>models/setting/index.ts</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> * <span class="hljs-keyword">as</span> types <span class="hljs-keyword">from</span> <span class="hljs-string">"./types"</span>;

<span class="hljs-keyword">const</span> setting: types.GlobalModelState = &#123;
  <span class="hljs-attr">namespace</span>: <span class="hljs-string">"setting"</span>,
  <span class="hljs-attr">state</span>: &#123;
    <span class="hljs-attr">userInfo</span>: &#123;&#125;
  &#125;,

  <span class="hljs-comment">// 修改 state 中的数据</span>
  <span class="hljs-attr">reducers</span>: &#123;
    <span class="hljs-function"><span class="hljs-title">setUserInfo</span>(<span class="hljs-params">state, &#123; data &#125;</span>)</span> &#123;
      <span class="hljs-built_in">console</span>.log(data);
      <span class="hljs-keyword">return</span> &#123;
        ...state,
        <span class="hljs-attr">userInfo</span>: data.userInfo
      &#125;;
    &#125;
  &#125;

  <span class="hljs-comment">// 异步操作后修改 state 中的数据</span>
  <span class="hljs-comment">// effects: &#123;</span>
  <span class="hljs-comment">//   *changeName(&#123; payload &#125;, &#123; put, call &#125;) &#123;</span>
  <span class="hljs-comment">//     // call 触发异步</span>
  <span class="hljs-comment">//     // let data = yield call("/api", payload);</span>

  <span class="hljs-comment">//     // put 触发 action</span>
  <span class="hljs-comment">//     yield put(&#123;</span>
  <span class="hljs-comment">//       type: "saveName",</span>
  <span class="hljs-comment">//       data: &#123;</span>
  <span class="hljs-comment">//         name: "异步修改的",</span>
  <span class="hljs-comment">//       &#125;,</span>
  <span class="hljs-comment">//     &#125;);</span>
  <span class="hljs-comment">//     yield console.log("run");</span>
  <span class="hljs-comment">//   &#125;,</span>
  <span class="hljs-comment">// &#125;,</span>
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> setting;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-25">入口集成</h5>
<blockquote>
<p>将入口文件 app.ts 修改成 app.tsx，引入 Provider、dva、models。</p>
</blockquote>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> &#123; Component, useEffect &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> &#123; View, Text &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@tarojs/components"</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">"./app.scss"</span>;

<span class="hljs-comment">// 此处必须使用 react-redux 否则报错</span>
<span class="hljs-keyword">import</span> &#123; Provider &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react-redux"</span>;

<span class="hljs-keyword">import</span> dva <span class="hljs-keyword">from</span> <span class="hljs-string">"./utils/dva"</span>;

<span class="hljs-keyword">import</span> models <span class="hljs-keyword">from</span> <span class="hljs-string">"./models"</span>;

<span class="hljs-comment">// 集成 dva</span>
<span class="hljs-keyword">const</span> dvaApp = dva.createApp(&#123;
  <span class="hljs-attr">initialState</span>: &#123;&#125;,
  models,
  <span class="hljs-attr">enableLog</span>: <span class="hljs-literal">false</span>
&#125;);
<span class="hljs-keyword">const</span> store = dvaApp.getStore();

<span class="hljs-keyword">const</span> App: React.FC = (&#123; children &#125;): JSX.Element => &#123;

  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Provider</span> <span class="hljs-attr">store</span>=<span class="hljs-string">&#123;store&#125;</span>></span>&#123;children&#125;<span class="hljs-tag"></<span class="hljs-name">Provider</span>></span></span>;
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> App;


<span class="copy-code-btn">复制代码</span></code></pre>
<p>获取 store 中的数据 (useSelector)</p>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">const</span> userInfo = useSelector(<span class="hljs-function"><span class="hljs-params">state</span> =></span> state.setting.userInfo).nickName
<span class="copy-code-btn">复制代码</span></code></pre>
<p>修改 store 中的数据 (useDispatch)</p>
<pre><code class="hljs language-typescript copyable" lang="typescript">  dispatch(&#123;
    <span class="hljs-attr">type</span>:<span class="hljs-string">"setting/setUserInfo"</span>,
    <span class="hljs-attr">data</span>:&#123;
      userInfo
    &#125;
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-26">页面适配问题</h2>
<blockquote>
<p>Taro 默认按照<strong>designWidth：750</strong>的尺寸来进行自动转换，如果 UI 给的设计稿是 375 的宽度，可以修改 <strong>config</strong> => **index.js **</p>
</blockquote>
<pre><code class="hljs language-javascript copyable" lang="javascript">designWidth: <span class="hljs-number">750</span>,
  <span class="hljs-attr">deviceRatio</span>: &#123;
    <span class="hljs-number">640</span>: <span class="hljs-number">2.34</span> / <span class="hljs-number">2</span>,
    <span class="hljs-number">750</span>: <span class="hljs-number">1</span>,
    <span class="hljs-number">828</span>: <span class="hljs-number">1.81</span> / <span class="hljs-number">2</span>,
    <span class="hljs-number">375</span>: <span class="hljs-number">2</span>
  &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>当然了，只是修改上面部分还远远不够，这个时候运行项目，你会发现 taro-ui 组件样式变得好大，what ？ 组件被放大了两倍 ？ 不要慌，按照如下配置即可</p>
</blockquote>
<pre><code class="hljs language-bash copyable" lang="bash">yarn add postcss-px-scale
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">const</span> config = &#123;
  <span class="hljs-attr">projectName</span>: <span class="hljs-string">"taro_template"</span>,
  <span class="hljs-attr">date</span>: <span class="hljs-string">"2021-6-23"</span>,
  <span class="hljs-attr">designWidth</span>: <span class="hljs-number">750</span>,
  <span class="hljs-attr">deviceRatio</span>: &#123;
    <span class="hljs-number">640</span>: <span class="hljs-number">2.34</span> / <span class="hljs-number">2</span>,
    <span class="hljs-number">750</span>: <span class="hljs-number">1</span>,
    <span class="hljs-number">828</span>: <span class="hljs-number">1.81</span> / <span class="hljs-number">2</span>,
    <span class="hljs-number">375</span>: <span class="hljs-number">2</span>
  &#125;,
  <span class="hljs-attr">sourceRoot</span>: <span class="hljs-string">"src"</span>,
  <span class="hljs-attr">outputRoot</span>: <span class="hljs-string">"dist"</span>,
  <span class="hljs-attr">plugins</span>: [],
  <span class="hljs-attr">defineConstants</span>: &#123;&#125;,
  <span class="hljs-attr">copy</span>: &#123;
    <span class="hljs-attr">patterns</span>: [],
    <span class="hljs-attr">options</span>: &#123;&#125;
  &#125;,
  <span class="hljs-attr">framework</span>: <span class="hljs-string">"react"</span>,
  <span class="hljs-attr">mini</span>: &#123;
    <span class="hljs-attr">postcss</span>: &#123;
      <span class="hljs-attr">pxtransform</span>: &#123;
        <span class="hljs-attr">enable</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">config</span>: &#123;&#125;
      &#125;,
      <span class="hljs-attr">url</span>: &#123;
        <span class="hljs-attr">enable</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">config</span>: &#123;
          <span class="hljs-attr">limit</span>: <span class="hljs-number">1024</span> <span class="hljs-comment">// 设定转换尺寸上限</span>
        &#125;
      &#125;,
      <span class="hljs-attr">cssModules</span>: &#123;
        <span class="hljs-attr">enable</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 默认为 false，如需使用 css modules 功能，则设为 true</span>
        <span class="hljs-attr">config</span>: &#123;
          <span class="hljs-attr">namingPattern</span>: <span class="hljs-string">"module"</span>, <span class="hljs-comment">// 转换模式，取值为 global/module</span>
          <span class="hljs-attr">generateScopedName</span>: <span class="hljs-string">"[name]__[local]___[hash:base64:5]"</span>
        &#125;
      &#125;,
      <span class="hljs-comment">// 这里增加配置</span>
      <span class="hljs-string">"postcss-px-scale"</span>: &#123;
        <span class="hljs-attr">enable</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">config</span>: &#123; <span class="hljs-attr">scale</span>: <span class="hljs-number">0.5</span>, <span class="hljs-attr">units</span>: <span class="hljs-string">"rpx"</span>, <span class="hljs-attr">includes</span>: [<span class="hljs-string">"taro-ui"</span>] &#125;
      &#125;,
    &#125;,
  &#125;,
  <span class="hljs-attr">h5</span>: &#123;
    <span class="hljs-attr">publicPath</span>: <span class="hljs-string">"/"</span>,
    <span class="hljs-attr">staticDirectory</span>: <span class="hljs-string">"static"</span>,
    <span class="hljs-attr">esnextModules</span>:[<span class="hljs-string">'taro-ui'</span>],
    <span class="hljs-attr">postcss</span>: &#123;
      <span class="hljs-attr">autoprefixer</span>: &#123;
        <span class="hljs-attr">enable</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">config</span>: &#123;&#125;
      &#125;,
      <span class="hljs-attr">cssModules</span>: &#123;
        <span class="hljs-attr">enable</span>: <span class="hljs-literal">false</span>, <span class="hljs-comment">// 默认为 false，如需使用 css modules 功能，则设为 true</span>
        <span class="hljs-attr">config</span>: &#123;
          <span class="hljs-attr">namingPattern</span>: <span class="hljs-string">"module"</span>, <span class="hljs-comment">// 转换模式，取值为 global/module</span>
          <span class="hljs-attr">generateScopedName</span>: <span class="hljs-string">"[name]__[local]___[hash:base64:5]"</span>
        &#125;
      &#125;,
      <span class="hljs-comment">// 这里增加配置</span>
      <span class="hljs-string">"postcss-px-scale"</span>: &#123;
        <span class="hljs-attr">enable</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">config</span>: &#123; <span class="hljs-attr">scale</span>: <span class="hljs-number">0.5</span>, <span class="hljs-attr">units</span>: <span class="hljs-string">"rem"</span>, <span class="hljs-attr">includes</span>: [<span class="hljs-string">"taro-ui"</span>] &#125;
      &#125;,
    &#125;,
  &#125;
&#125;;

<span class="hljs-built_in">module</span>.exports = <span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">merge</span>) </span>&#123;
  <span class="hljs-keyword">if</span> (process.env.NODE_ENV === <span class="hljs-string">"development"</span>) &#123;
    <span class="hljs-keyword">return</span> merge(&#123;&#125;, config, <span class="hljs-built_in">require</span>(<span class="hljs-string">"./dev"</span>));
  &#125;
  <span class="hljs-keyword">return</span> merge(&#123;&#125;, config, <span class="hljs-built_in">require</span>(<span class="hljs-string">"./prod"</span>));
&#125;;

<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-27">扫二维码功能</h2>
<blockquote>
<p>扫码功能就很简单了，可以直接调用官方提供的方法</p>
</blockquote>
<pre><code class="hljs language-typescript copyable" lang="typescript">Taro.scanCode(&#123;
    <span class="hljs-attr">success</span>: <span class="hljs-function"><span class="hljs-params">result</span> =></span> &#123;
      <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"扫码成功的回调"</span>, result);
    &#125;
  &#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>更多用法自己查看官方文档吧，这里就不做一一介绍了。</p>
<h2 data-id="heading-28">调试技巧 - minidebug</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1c74990fd36d4559a00669edb544bb02~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-29">功能介绍</h5>
<blockquote>
<p>主要功能包括环境切换、身份Mock、应用信息获取、位置模拟、缓存管理、扫一扫、H5跳转、更新版本等。</p>
</blockquote>
<h5 data-id="heading-30">安装</h5>
<pre><code class="hljs language-bash copyable" lang="bash">yarn add @jdlfe/minidebug-next

<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-31">新建空页面 debug</h5>
<blockquote>
<p>活学活用，使用 cli 快速创建页面</p>
</blockquote>
<pre><code class="hljs language-bash copyable" lang="bash">Taro create -- debug
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>引入组件 Debug</p>
</blockquote>
<pre><code class="hljs language-typescript copyable" lang="typescript"><span class="hljs-keyword">import</span> &#123; View &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@tarojs/components'</span>
<span class="hljs-keyword">import</span> &#123; Debug &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'@jdlfe/minidebug-next'</span>

<span class="hljs-keyword">import</span> <span class="hljs-string">'./debug.scss'</span>

<span class="hljs-keyword">const</span> Bug: React.FC = <span class="hljs-function">() =></span> &#123;

  <span class="hljs-keyword">return</span> (
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">View</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">Debug</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">View</span>></span></span>
  );
&#125;;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> Bug;

<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>增加页面配置入口，用于打开页面，页面最好配置到 subpackages 中，不然会造成主包比较大。</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b8b418a4cec8403a98e2ff2abf1b267a~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9e4c4e0deeb14a50ba640e5270a05396~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>更多用法参考 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjdlfe%2Fminidebug" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/jdlfe/minidebug" ref="nofollow noopener noreferrer">github.com/jdlfe/minid…</a></p>
</blockquote>
<h2 data-id="heading-32">源码地址</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fxushanpei%2Ftaro_init_template" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/xushanpei/taro_init_template" ref="nofollow noopener noreferrer">Github 仓库地址</a></p>
<h2 data-id="heading-33">最后来个自我介绍吧</h2>
<blockquote>
<p>大家好，我是 前端小菜鸡之菜鸡互啄 ，某不知名小公司的一名前端开发搬砖员。这是我在掘金上发表的第一篇文章，不得不说，写文章真的挺累的，比起写代码要累的多，希望大家能够多多支持。后期会不断输出一些新的文章。</p>
</blockquote>
<p>也可以关注我的公众号： <strong>前端开发爱好者</strong> 每天会收集一些大佬的文章和创作一些原创的文章，欢迎大家关注我。</p></div>  
</div>
            