
---
title: 'Taro转React-Native的实践总结和分析思考'
categories: 
 - 社交媒体
 - 简书
 - 首页
headimg: 'https://picsum.photos/400/300?random=2775'
author: 简书
comments: false
date: Invalid Date
thumbnail: 'https://picsum.photos/400/300?random=2775'
---

<div>   
<p>本文始发于我的博文<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fzackzheng.info%2F2020%2F06%2F14%2Ftaro-to-react-native%2F" target="_blank">Taro转React-Native的实践总结和分析思考</a>，现转发至此。</p>
<h1>一、前言</h1>
<blockquote>
<p><strong>Taro</strong> 是一套遵循 <a href="https://links.jianshu.com/go?to=https%3A%2F%2Freactjs.org%2F" target="_blank">React</a> 语法规范的 <strong>多端开发</strong> 解决方案。</p>
<p>使用 <strong>Taro</strong>，我们可以只书写一套代码，再通过 <strong>Taro</strong> 的编译工具，将源代码分别编译出可以在不同端（微信/百度/支付宝/字节跳动/QQ/京东小程序、快应用、H5、React-Native 等）运行的代码。</p>
<p>*摘自<a href="https://links.jianshu.com/go?to=https%3A%2F%2Ftaro-docs.jd.com%2Ftaro%2Fdocs%2FREADME" target="_blank">Taro 介绍</a></p>
</blockquote>
<p><code>Taro</code>是一套优秀的多端开发解决方案。我们团队自较早期时(18年底)便开始了深入研究，并投入到丰富的微信小程序开发实践中，同时作者还负责团队<code>Taro</code>转百度/字节跳动/<code>React-Native</code>的项目。</p>
<p>本文将介绍<code>Taro</code>转<code>React-Native</code>的项目框架、<code>Taro</code>转<code>React-Native</code>过程中遇到的问题和解决方案、RN的热更新，以及框架相关的思考。</p>
<p>项目完成于去年(2019年)，最近才抽空重新修改了总结文档放到博客上。因此可能有些转换细节不是最新的，请留意。</p>
<h1>二、项目实践</h1>
<p>Taro 转 React-Native（以下简称RN） 项目，目前应用于将“美梨工坊桌面”项目（Taro）转换成美梨桌面 iOS App（基于 RN 进行封装的 App 壳），是 App 的 RN 内置包系统，主要功能为 RN 所有功能的展现，包括协作项目开发、页面展示、公共 Bundle、热更新、预下载、一键部署等特性。</p>
<p>作用：让客户端/前端团队能支持更灵活的开发协作、节省开发成本、支持及时处理线上问题。</p>
<h2>2.1 整体框架</h2>
<p>包含以下四个方面。</p>
<h3>开发链路</h3>
<ul>
<li>基于 NPM 的 Web 开发体验</li>
<li>基于 Webpack 构建，完整的项目管理</li>
<li>React-Native 二次组件、工具集合类</li>
</ul>
<h3>打包链路</h3>
<ul>
<li>自动打包、随版本生成配置</li>
<li>持续集成、部署、交付</li>
</ul>
<h3>发布链路</h3>
<ul>
<li>git webhook，自动发布</li>
<li>后台 API，OSS 自动上传</li>
<li>发布配置后台，通知提醒</li>
</ul>
<h3>Native 支持</h3>
<ul>
<li>推送功能支持</li>
<li>原生路由至 RN 页面支持</li>
<li>Bundle 文件和资源文件的更新</li>
</ul>
<h2>2.2 RN 准备工作</h2>
<p>目前只在 iOS 平台上做部署，所以只展开 iOS 端的准备工作。</p>
<ul>
<li>安装依赖库</li>
</ul>
<pre><code class="shell">brew install node
brew install watchman
</code></pre>
<ul>
<li>安装 React-Native 命令行工具</li>
</ul>
<pre><code class="shell">npm install -g yarn react-native-cli
</code></pre>
<ul>
<li>安装 Xcode</li>
<li>在 config/index.js 文件中配置：</li>
</ul>
<pre><code class="json">rn: &#123;
  appJson: &#123;
    name: 'MeiliDesktop',
  &#125;,
&#125;
</code></pre>
<p>相关开发链接：</p>
<ul>
<li><a href="https://links.jianshu.com/go?to=https%3A%2F%2Freactnative.cn%2Fdocs%2Fgetting-started%2F" target="_blank">RN开发文档</a></li>
<li><a href="https://links.jianshu.com/go?to=https%3A%2F%2Ftaro-docs.jd.com%2Ftaro%2Fdocs%2Freact-native.html" target="_blank">Taro React-Native 端开发流程</a></li>
</ul>
<h2>2.3 遇到的问题</h2>
<p>主要列举 Taro 转换 React-Native 过程中遇到的问题及处理方法。</p>
<h3>2.3.1 环境/依赖库相关问题</h3>
<ul>
<li>node-sass</li>
</ul>
<p>执行项目 yarn，安装 node-sass 库会失败，根据 <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2Fnode-sass%2Fv%2F4.9.1" target="_blank">node-sass 官网</a>文档，切换源并使用 npm 可以成功：</p>
<pre><code>npm install -g mirror-config-china --registry=http://registry.npm.taobao.org
npm install node-sass
</code></pre>
<ul>
<li>fbjs</li>
</ul>
<p>提示找不到 fbjs，添加该库并执行安装。</p>
<ul>
<li>NervJS/taro-native-shell 壳子应用编译失败</li>
</ul>
<p>文档建议使用 <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro-native-shell" target="_blank">NervJS/taro-native-shell</a> 工程，该工程是 RN 工程中原生的部分。</p>
<p>可能会遇到环境或 Xcode 版本兼容问题，可以自行生成壳子工程。</p>
<pre><code>react-native init AwesomeProject
</code></pre>
<ul>
<li>The UMNativeModulesProxy native module is not exported through NativeModules</li>
</ul>
<p>使用自行生成的壳子工程需要自行安装依赖<code>react-native-unimodules</code>，添加到<code>package.json</code>的<code>dependencies</code>中。</p>
<ul>
<li>selector hasGrantedPermission</li>
</ul>
<p><code>react-native-unimodules</code>使用的是 0.7.0 版本，发现换成 0.6.0 即可解决。</p>
<pre><code>"react-native-unimodules": "0.6.0"
</code></pre>
<h3>2.3.2 组件/样式问题</h3>
<ul>
<li>Invariant Violation: Text strings must be rendered within a  component.</li>
</ul>
<p>文字需要包在 <code>Text</code> 组件里面</p>
<pre><code><View className='page-order-detail__content'>
    &#123;steps && steps.length && (<View></View>)
</View>
</code></pre>
<p>上面的代码也会提示错误，需要改成：</p>
<pre><code><View className='page-order-detail__content'>
    &#123;steps && steps.length > 0 && (<View></View>)
</View>
</code></pre>
<ul>
<li>Input 设置<code>line-height</code>会导致输入内容显示异常</li>
</ul>
<p>内容会显示偏下并被遮挡</p>
<ul>
<li>Text 组件不支持设置圆角等</li>
<li>Input 不支持设置<code>Height</code>
</li>
<li>400,700，normal 或 bold 之外的 font-weight 值在Android上的React-Native中没有效果</li>
<li>不支持<code>100vh</code>设置</li>
<li>其他不支持的样式</li>
</ul>
<p><code>React-Native</code>的样式基于开源的跨平台布局引擎 <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Ffacebook%2Fyoga" target="_blank">Yoga</a> ，样式基本上是实现了 CSS 的一个子集，所以会有些样式不支持，在出错时会给出支持的样式列表。如 RN 不支持针对某一边设置 style，即 border-bottom-style 会报错。</p>
<ul>
<li>必须使用 Flex 布局</li>
<li>文字要包在 <code>Text</code> 组件里面，否则不显示</li>
<li>
<code>position:fixed</code> React-Native 不支持</li>
<li>样式选择器仅支持类选择器，且不支持 <strong>组合器</strong>
</li>
<li>RN 中 View 标签默认主轴方向是 column</li>
</ul>
<p>如果需要兼容各端，最好在布局中显式声明主轴方向。</p>
<h3>2.3.3 其他问题</h3>
<ul>
<li>不支持同步的 Storage 存取</li>
</ul>
<p>即不支持<code>Taro.setStorageSync</code>和<code>Taro.getStorageSync</code>两个同步方法，因此需要对已有代码进行重构，使用<code>async/await</code>和<code>Promise</code>进行处理。</p>
<ul>
<li>找不到方法/函数</li>
</ul>
<p>所有的方法参数传递，需要<code>bind(this)</code></p>
<ul>
<li>this.setState is not a function</li>
</ul>
<p>寻找未添加<code>bind(this)</code>的方法参数传递，添加<code>bind(this)</code></p>
<ul>
<li>
<code>componentWillMount()</code>即将废弃</li>
</ul>
<p>使用<code>componentDidMount()</code>实现</p>
<ul>
<li>没有读取文件并进行 base64 编码</li>
</ul>
<p>使用<code>rn-fetch-blob</code>库解决。</p>
<h3>2.3.4 其他参考</h3>
<p>Taro 官方提供了<a href="https://links.jianshu.com/go?to=https%3A%2F%2Ftaro-docs.jd.com%2Ftaro%2Fdocs%2Fbefore-dev-remind.html" target="_blank">各端开发前注意事项</a>，特别是使用 RN 的样式区别。</p>
<p>Taro 官方提供了<a href="https://links.jianshu.com/go?to=https%3A%2F%2Ftaro-docs.jd.com%2Ftaro%2Fdocs%2Fbest-practice.html" target="_blank">最佳实践</a>，可以参考。</p>
<p>Taro 官方提供了<a href="https://links.jianshu.com/go?to=https%3A%2F%2Ftaro-docs.jd.com%2Ftaro%2Fdocs%2Fcomposition.html" target="_blank">更多资源</a>，可以查看其他团队的文章分享和遇到的问题解决。</p>
<h2>2.4 热更新方案</h2>
<p>目前业界 RN 热更新方案同样分为 全量更新 和 增量更新。原理同 Weex 类似，此处不再赘述。</p>
<p>全量更新分为两部分，即<code>Bundle</code>文件和资源的更新。</p>
<ul>
<li>目前方案</li>
</ul>
<p>当前项目页面较少，整个 Bundle 文件不到 2MB，目前使用全量更新。</p>
<p>资源文件夹先压缩再上传；<code>App</code>端下载后进行<code>md5</code>验证，验证通过则解压到缓存目录。</p>
<p>在下次重新打开 App 才读取缓存的<code>Bundle</code>和 资源。</p>
<p>接口格式可参考以下方案：</p>
<pre><code>&#123;
    "error_code": 0,
    "error_message": "成功",
    "data": &#123;
        "bundle": &#123;
            "version": "190108174500",
            "url": "https://xxx/main.jsbundle",
            "md5": "xxx"
        &#125;,
        "assets": &#123;
            "version": "190108174500",
            "url": "https://xxx/assets.zip",
            "md5": "xxx"
        &#125;
    &#125;
&#125;
</code></pre>
<p>因为该项目的用户是公司内部员工，目前第一版，所以没有对复杂情况进行处理，后续应用后再持续设计。</p>
<p>如支持不同设备或不同<code>App</code>版本使用不同的<code>Bundle</code>等等。</p>
<ul>
<li>Pushy</li>
</ul>
<p>目前官方推荐热更新框架<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fpushy.reactnative.cn" target="_blank">Pushy</a>，可以了解下，原理都是差不多的，实现会更方便。</p>
<h2>2.5 相关命令及其作用</h2>
<ul>
<li>Taro 转 RN</li>
</ul>
<pre><code>taro build --type rn
</code></pre>
<ul>
<li>调试代码</li>
</ul>
<pre><code>taro build --type rn --watch
</code></pre>
<ul>
<li>打包 RN Bundle 和资源</li>
</ul>
<pre><code>cd rn_temp && node ../node_modules/react-native/local-cli/cli.js bundle --entry-file ./rn_temp/index.js --bundle-output ./bundle/main.jsbundle --assets-dest ./bundle --dev false
</code></pre>
<p>执行 Taro 转 RN 命令后，在项目中会生成 rn_temp 文件夹，该文件夹即完整的 RN 代码，打包 RN 需要进入该目录执行。</p>
<p>打包后会生成 Bundle 文件和资源文件夹，用于替换原生保存的 RN 内容。</p>
<h1>三、总结</h1>
<ul>
<li>友好度——转换工作复杂度</li>
</ul>
<p>由于作者是开发<code>iOS</code>客户端的，且于4年前已经在现有项目中集成过<code>React-Native</code>页面，对<code>React-Native</code>的原理和机制有过研究，实践过相关技术栈，所以转换工作相对容易。</p>
<p>对于不是客户端出身，或者不熟悉<code>React-Native</code>/<code>Weex</code>等客户端跨平台框架的机制和技术栈的同学，需要做点其他功课。</p>
<ul>
<li>多端适配以<code>React-Native</code>样式为主</li>
</ul>
<p>如果需要适配多端，需要以 <code>React-Native</code> 的约束来管理样式。</p>
<p>因为样式上<code>H5</code>最为灵活，小程序次之，<code>React-Native</code>最弱（<code>React-Native</code>的样式基于开源的跨平台布局引擎 <a href="https://links.jianshu.com/go?to=https%3A%2F%2Fgithub.com%2Ffacebook%2Fyoga" target="_blank">Yoga</a> ，样式基本上是实现了 CSS 的一个子集），统一多端样式即是对齐短板，也就是要以 <code>React-Native</code> 的约束来管理样式，同时兼顾小程序的限制。</p>
<ul>
<li>
<code>Taro</code>-> <code>React-Native</code> -> <code>iOS/Android</code>链条长</li>
</ul>
<p>通过 <code>Taro</code> 转<code>React-Native</code>，<code>React-Native</code>再转<code>iOS/Android</code>，链条过长，会面临复杂度增加、维护成本较大、组件适配、客户端系统版本和语言升级维护等问题，同时影响一些复杂功能的实现方案的决策和估时。</p>
<p>毫无疑问，这是复杂度非常高的架构设计，对开发人员的能力和各方面经验有较高要求。</p>
<p>为了尽早覆盖跨客户端，<code>Taro</code>官方选择 <code>React-Native</code>无疑是最快速和易行的方案。</p>
<ul>
<li>跨端效果和质量</li>
</ul>
<p>总体而言，在功能不复杂的项目中，进行<code>Taro</code>转换<code>React-Native</code>，虽然修改较多但都不算难处理，虽有几处转换问题需等官方处理，但转换后的效果和质量还算OK。</p>
<p>-END-<br>
欢迎到我的博客交流：<a href="https://links.jianshu.com/go?to=https%3A%2F%2Fzackzheng.info" target="_blank">https://zackzheng.info</a></p>
  
</div>
            