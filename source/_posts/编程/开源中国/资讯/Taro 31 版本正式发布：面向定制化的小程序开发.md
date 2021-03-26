
---
title: 'Taro 3.1 版本正式发布：面向定制化的小程序开发'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8583'
author: 开源中国
comments: false
date: Fri, 26 Mar 2021 10:22:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8583'
---

<div>   
<div class="content">
                                                                                            <div> 
 <div style="text-align:var(--ifm-avatar-intro-alignment)"> 
  <p style="text-align:justify">自 Taro 3.1 体验版推出后，我们不断地根据社区的反馈意见对 3.1 版本进行打磨。主要改进了<strong>开放式架构</strong>、引入了 <code>CustomWrapper</code> 组件以解决性能问题、提出了原生小程序<strong>渐进式混合使用 Taro</strong> 的解决方案。</p> 
  <p style="text-align:justify">经历了 12 个 beta 版本后，终于迎来了 3.1 正式版🎉</p> 
  <h2 style="text-align:center">一、Highlights</h2> 
  <h3 style="text-align:justify">1. 开放式架构</h3> 
  <p style="text-align:justify">近年来业界推出的小程序平台越来越多，但 Taro 核心维护的平台只有 6 个，因此常常有同学提出能不能支持某某平台的 Feature Request。</p> 
  <p style="text-align:justify">基于目前的架构，支持一个新的平台开发复杂度高，同时社区也难以参与贡献。</p> 
  <p style="text-align:justify">为此我们把 Taro 打造成为一个开放式框架，<strong>通过端平台插件能支持任意小程序平台</strong>：</p> 
  <ul> 
   <li> <p><strong>插件开发者</strong>无需修改 Taro 项目源码，即可<strong>编写出一个端平台插件</strong>[1]。</p> </li> 
   <li> <p><strong>插件使用者</strong>只需<strong>安装、配置端平台插件</strong>[2]，即可把代码编译到指定平台。</p> </li> 
  </ul> 
  <p style="text-align:justify">基于开放式架构，我们新增了一些有趣的插件，也十分期待大家利用它施展创意。</p> 
  <h4 style="text-align:justify">新增的插件：</h4> 
  <table cellspacing="0" style="width:753.7142944335938px"> 
   <thead> 
    <tr> 
     <th style="background-color:#f0f0f0; text-align:left">插件</th> 
     <th style="background-color:#f0f0f0; text-align:left">功能</th> 
    </tr> 
   </thead> 
   <tbody> 
    <tr> 
     <td style="border-color:#cccccc"><strong>@tarojs/plugin-platform-weapp-qy</strong>[3]</td> 
     <td style="border-color:#cccccc">编译企业微信小程序</td> 
    </tr> 
    <tr> 
     <td style="border-color:#cccccc"><strong>@tarojs/plugin-platform-alipay-dd</strong>[4]</td> 
     <td style="border-color:#cccccc">编译钉钉小程序</td> 
    </tr> 
    <tr> 
     <td style="border-color:#cccccc"><strong>@tarojs/plugin-platform-alipay-iot</strong>[5]</td> 
     <td style="border-color:#cccccc">编译支付宝 IOT 小程序</td> 
    </tr> 
    <tr> 
     <td style="border-color:#cccccc"><strong>@tarojs/plugin-inject</strong>[6]</td> 
     <td style="border-color:#cccccc">为所有小程序平台快速新增 <strong>API</strong>、<strong>组件</strong>，<strong>调整组件属性</strong>等</td> 
    </tr> 
   </tbody> 
  </table> 
  <h3 style="text-align:justify">2. 新增小程序性能优化组件 CustomWrapper</h3> 
  <p style="text-align:justify">Taro3 使用 <code><template></code> 进行渲染，所有的 <code>setData</code> 都由页面对象调用。如果页面结构比较复杂，应用更新的性能就会下降。</p> 
  <p style="text-align:justify">为此我们引入了一个基础组件 <code>CustomWrapper</code>，它的作用是创建一个原生自定义组件。对后代节点的 <code>setData</code> 将由此自定义组件进行调用，<strong>达到局部更新的效果</strong>，从而提升更新性能。</p> 
  <p style="text-align:justify">开发者可以使用  <code>CustomWrapper</code> 去包裹遇到更新性能问题的组件：</p> 
  <pre style="text-align:justify"><code><CustomWrapper>
  <<span style="color:#e45649">GoodsList</span>>
    <<span style="color:#e45649">Item</span> />
    <<span style="color:#e45649">Item</span> />
    // ...
  </<span style="color:#e45649">GoodsList</span>>
<<span style="color:#50a14f">/CustomWrapper>
</span></code></pre> 
  <blockquote> 
   <p>更详细的性能优化原理请见<strong>《Taro 助力京喜拼拼项目性能体验优化》</strong>[7]</p> 
  </blockquote> 
  <h3 style="text-align:justify">3. 原生小程序渐进式混合使用 Taro 开发</h3> 
  <p style="text-align:justify">过去我们对在 Taro 项目中混合使用原生的支持度较高。相反地，对在原生项目中混合使用 Taro 却没有太重视。但是市面上有着存量的原生开发小程序，他们接入 Taro 开发的改造成本往往非常大，最后只得放弃混合开发的想法。</p> 
  <p style="text-align:justify"><strong>经过与京喜拼拼项目的合作</strong>[8]，也驱使了我们更加关注这部分需求。Taro 推出了一套完整的原生项目混合使用 Taro 的方案。</p> 
  <p style="text-align:justify"><strong>方案</strong>[9]主要支持了三种场景：</p> 
  <ul> 
   <li> <p>在原生项目中使用 Taro 开发的页面。</p> </li> 
   <li> <p>在原生项目的分包中运行完整的 Taro 项目。</p> </li> 
   <li> <p>在原生项目中使用 Taro 开发的自定义组件。</p> </li> 
  </ul> 
  <p style="text-align:justify">希望以上方案能满足打算逐步接入 Taro 开发的同学。更多意见也欢迎在 <strong>Github</strong>[10] 上给我们留言。</p> 
  <h3 style="text-align:justify">4. 拥抱 React 17、TypeScript 4</h3> 
  <h4 style="text-align:justify">4.1. 使用方法</h4> 
  <p>新项目：</p> 
  <p style="text-align:justify">模板默认依赖 React 17、TypeScript 4，可以直接使用。</p> 
  <p>旧项目：</p> 
  <p style="text-align:justify">手动升级项目依赖：</p> 
  <ul> 
   <li> <p><code>react: ^17.0.0</code></p> </li> 
   <li> <p><code>react-dom: ^17.0.0</code></p> </li> 
   <li> <p><code>typescript: ^4.1.0</code></p> </li> 
   <li> <p><code>@typescript-eslint/parser: ^4.15.1</code></p> </li> 
   <li> <p><code>@typescript-eslint/eslint-plugin: ^4.15.1</code></p> </li> 
  </ul> 
  <p style="text-align:justify">设置 ESLint 配置：</p> 
  <pre style="text-align:justify"><code><em>// .eslintrc</em>
<span style="color:#c18401">module</span>.exports = &#123;
  <span style="color:#50a14f">"extends"</span>: [<span style="color:#50a14f">"taro/react"</span>],
  <span style="color:#50a14f">"rules"</span>: &#123;
    <span style="color:#50a14f">"react/jsx-uses-react"</span>: <span style="color:#50a14f">"off"</span>,
    <span style="color:#50a14f">"react/react-in-jsx-scope"</span>: <span style="color:#50a14f">"off"</span>
  &#125;
&#125;
</code></pre> 
  <h4 style="text-align:justify">4.2. React 默认支持 <span style="color:#0e88eb">New JSX Transform</span>[11]</h4> 
  <p style="text-align:justify">New JSX Transform 让开发者<strong>不再需要在书写 JSX 前先引入 React</strong>。</p> 
  <p style="text-align:justify">如果不希望打开此功能，可以修改 Babel 配置的 <code>reactJsxRuntime</code> 选项为 <code>classes</code>：</p> 
  <pre style="text-align:justify"><code><em>// babel.config.js</em>
<span style="color:#c18401">module</span>.exports = &#123;
  <span style="color:#986801">presets</span>: [
    [<span style="color:#50a14f">'taro'</span>, &#123;
      <span style="color:#986801">framework</span>: <span style="color:#50a14f">'react'</span>,
      <span style="color:#986801">ts</span>: <span style="color:#0184bb">true</span>,
      <span style="color:#986801">reactJsxRuntime</span>: <span style="color:#50a14f">'classes'</span>
    &#125;]
  ]
&#125;
</code></pre> 
  <h4 style="text-align:justify">4.3. React H5 端默认开启 <span style="color:#0e88eb">fast-refresh</span>[12]</h4> 
  <p style="text-align:justify">如果不希望打开此功能，可以修改 Taro 配置和 Babel 配置：</p> 
  <pre style="text-align:justify"><code><em>// config/index.js</em>
<span style="color:#a626a4">const</span> config = &#123;
  <span style="color:#986801">h5</span>: &#123;
    <span style="color:#986801">devServer</span>: &#123;
      <span style="color:#986801">hot</span>: <span style="color:#0184bb">false</span>
    &#125;
  &#125;
&#125;

<em>// babel.config.js</em>
<span style="color:#c18401">module</span>.exports = &#123;
  <span style="color:#986801">presets</span>: [
    [<span style="color:#50a14f">'taro'</span>, &#123;
      <span style="color:#986801">framework</span>: <span style="color:#50a14f">'react'</span>,
      <span style="color:#986801">ts</span>: <span style="color:#0184bb">true</span>,
      <span style="color:#986801">hot</span>: <span style="color:#0184bb">false</span>
    &#125;]
  ]
&#125;
</code></pre> 
  <h2 style="text-align:center">二、Breakings</h2> 
  <h3 style="text-align:justify">1. React</h3> 
  <p style="text-align:justify">项目的 React 版本必须 <strong>>= 16.14.0</strong>，或使用 <strong>17.0.0+</strong></p> 
  <h3 style="text-align:justify">2. Vue2</h3> 
  <blockquote> 
   <p>修复 Vue2 入口组件生命周期多次触发的问题，#7179</p> 
  </blockquote> 
  <p style="text-align:justify">用户编写的入口组件需要修改如下：</p> 
  <pre style="text-align:justify"><code><em>// app.js</em>

<em>// 3.0 中需要创建 Vue 对象</em>
<span style="color:#a626a4">const</span> App = <span style="color:#a626a4">new</span> Vue(&#123;&#125;)

<em>// 3.1 中只需要返回对象字面量</em>
<span style="color:#a626a4">const</span> App = &#123;&#125;
</code></pre> 
  <h3 style="text-align:justify">3. Linaria</h3> 
  <p style="text-align:justify">使用 <code>Linaria</code> 时，需要修改 <code>linaria.config.js</code> 的内容。</p> 
  <pre style="text-align:justify"><code><span style="color:#c18401">module</span>.exports = &#123;
  <span style="color:#986801">rules</span>: [
    &#123;
      <span style="color:#986801">action</span>: <span style="color:#c18401">require</span>(<span style="color:#50a14f">"linaria/evaluators"</span>).shaker,
    &#125;,
    &#123;
      <em>// 此处的正则有改变</em>
      <span style="color:#986801">test</span>: <span style="color:#50a14f">/node_modules[\/\\](?!@tarojs "\/\\")/</span>,
      <span style="color:#986801">action</span>: <span style="color:#50a14f">"ignore"</span>
    &#125;
  ]
&#125;
</code></pre> 
  <h2 style="text-align:center">三、特性</h2> 
  <ul> 
   <li> <p>组件 <code>View</code> 增加 <code>catchMove</code> 属性，解决<strong>滚动穿透</strong>[13]问题。</p> </li> 
   <li> <p>同步所有内置小程序官方最新的 API、组件能力。</p> </li> 
  </ul> 
  <h2 style="text-align:center">四、问题修复</h2> 
  <h3 style="text-align:justify">1. 重要</h3> 
  <ul> 
   <li> <p>修复百度小程序渲染问题，#7293。</p> </li> 
   <li> <p>修复、增强微信小程序转换为 Taro 的能力。</p> </li> 
   <li> <p>优化打包体积。</p> </li> 
   <li> <p>支付宝小程序支持引用自定义组件。</p> </li> 
   <li> <p>修复小程序分享 API 在使用 redux 时无法生效的问题，#7232。</p> </li> 
  </ul> 
  <h3 style="text-align:justify">2. 小程序</h3> 
  <ul> 
   <li> <p>修复多端文件没按照 Webpack <code>extension</code> 配置解析的问题，#6786，#7265 。</p> </li> 
   <li> <p>修复 style 属性设置失败的问题，#8678。</p> </li> 
  </ul> 
  <h3 style="text-align:justify">3. H5</h3> 
  <ul> 
   <li> <p>修复 H5 端 HMR 失效的问题。</p> </li> 
   <li> <p>支持路由 <strong>404</strong> 时触发 <code>App.onPageNotFound</code>，#7474。</p> </li> 
   <li> <p>修复表单组件 <code>slot</code> 兼容问题，#7363。</p> </li> 
   <li> <p>修复 <code>View</code> 和 <code>Text</code> 组件多行截断样式失败问题，#7472 #6741。</p> </li> 
   <li> <p>组件的 <code>style</code> 属性支持设置 CSS 变量，#7452。</p> </li> 
  </ul> 
  <h2 style="text-align:center">五、升级指南</h2> 
  <blockquote> 
   <p>从 v2.x 升级的同学需要先按 <strong>迁移指南</strong>[14] 进行操作。</p> 
  </blockquote> 
  <p style="text-align:justify">从 v3.x 升级的同学，首先需要安装 v3.1 的 CLI 工具：</p> 
  <pre style="text-align:justify"><code>npm i -g @tarojs/cli
</code></pre> 
  <p style="text-align:justify">然后进入项目，删除 <strong>node_modules</strong>、<strong>yarn.lock</strong>、<strong>package-lock.json</strong>。</p> 
  <p style="text-align:justify">最后把 <code>package.json</code> 文件中 Taro 相关依赖的版本修改为 <code>^3.1.0</code>，再重新安装依赖。至此升级结束。</p> 
  <h2 style="text-align:center">六、未来规划</h2> 
  <p style="text-align:justify">得益于 <strong>58 技术团队</strong>[15] 的全力支持，Taro 3 即将支持 <strong>React Native</strong>，现已推出 3.2.0 的 Beta 版本，3.2.0 正式版将于本月底推出。欢迎抢先体验：<strong>《增加 React Native 支持的 Taro 3.2.0 版本测试通告》</strong>[16]</p> 
  <h2 style="text-align:center">七、感谢</h2> 
  <p style="text-align:justify">开源不易，贵在坚持。Taro 团队衷心感谢各位参与过本项目开源建设的朋友，无论是为 Taro 提交过代码、建设周边生态，还是反馈过问题，甚至只是茶余饭后讨论、吐槽 Taro 的各位。</p> 
  <p style="text-align:justify">现诚挚邀请您与 Taro 官方团队交流您的使用情况，有你相伴，Taro更加精彩！<strong>问卷地址</strong>[17]</p> 
  <p style="text-align:justify">最后，特别感谢为 Taro 从 v3.0 走到 v3.1 贡献过代码的各位同学，不分先后：</p> 
  <ul> 
   <li> <p>@wuchangming</p> </li> 
   <li> <p>@SyMind</p> </li> 
   <li> <p>@zhuxianguo</p> </li> 
   <li> <p>@Songkeys</p> </li> 
   <li> <p>@vdfor</p> </li> 
   <li> <p>@ZeroTo0ne</p> </li> 
   <li> <p>@zhaoguoweiLLHC</p> </li> 
   <li> <p>@Spencer17x</p> </li> 
   <li> <p>@wingsico</p> </li> 
   <li> <p>@w91</p> </li> 
   <li> <p>@fjc0k</p> </li> 
   <li> <p>@Leechael</p> </li> 
   <li> <p>@southorange1228</p> </li> 
   <li> <p>@alexlees</p> </li> 
   <li> <p>@cncolder</p> </li> 
   <li> <p>@rottenpen</p> </li> 
   <li> <p>@gcxfd</p> </li> 
   <li> <p>@twocucao</p> </li> 
   <li> <p>@pengtikui</p> </li> 
   <li> <p>@kala888</p> </li> 
   <li> <p>@LengYXin</p> </li> 
   <li> <p>@iugo</p> </li> 
   <li> <p>@jin-yufeng</p> </li> 
   <li> <p>@xuchengzone</p> </li> 
   <li> <p>@csolin</p> </li> 
   <li> <p>@xiaoyao96</p> </li> 
   <li> <p>@baranwang</p> </li> 
   <li> <p>@fred8617</p> </li> 
   <li> <p>@huanz</p> </li> 
   <li> <p>@Cslove</p> </li> 
   <li> <p>@002huiguo</p> </li> 
   <li> <p>@jazzqi</p> </li> 
   <li> <p>@Jetsly</p> </li> 
   <li> <p>@yuezk</p> </li> 
   <li> <p>@lukezhange001</p> </li> 
   <li> <p>@k55k32</p> </li> 
   <li> <p>@Soul-Stone</p> </li> 
   <li> <p>@hisanshao</p> </li> 
   <li> <p>@gjc9620</p> </li> 
   <li> <p>@younthu</p> </li> 
   <li> <p>@digiaries</p> </li> 
   <li> <p>@GoodbyeNJN</p> </li> 
   <li> <p>@Swordword</p> </li> 
   <li> <p>@helsonxiao</p> </li> 
   <li> <p>@Ininit</p> </li> 
   <li> <p>@atzcl</p> </li> 
   <li> <p>@taoqf</p> </li> 
   <li> <p>@Aysnine</p> </li> 
   <li> <p>@cjz9032</p> </li> 
   <li> <p>@z3rog</p> </li> 
   <li> <p>@doublethinkio</p> </li> 
   <li> <p>@Jackyzm</p> </li> 
   <li> <p>@ywzou</p> </li> 
   <li> <p>@koalaink</p> </li> 
   <li> <p>@mosqlee</p> </li> 
   <li> <p>@wangjuerong</p> </li> 
   <li> <p>@kdxcxs</p> </li> 
   <li> <p>@LiHDong</p> </li> 
   <li> <p>@ryougifujino</p> </li> 
   <li> <p>@GitaiQAQ</p> </li> 
   <li> <p>@logix-o</p> </li> 
   <li> <p>@CallMeXYZ</p> </li> 
  </ul> 
  <h3 style="text-align:justify"><span style="color:#333333">参考资料</span></h3> 
  <p><span style="color:#666666">[1]</span></p> 
  <p>编写出一个端平台插件: <em>https://taro-docs.jd.com/taro/docs/next/platform-plugin-how</em></p> 
  <p><span style="color:#666666">[2]</span></p> 
  <p>安装、配置端平台插件: <em>https://taro-docs.jd.com/taro/docs/next/platform-plugin#%E7%AB%AF%E5%B9%B3%E5%8F%B0%E6%8F%92%E4%BB%B6%E4%BD%BF%E7%94%A8%E6%96%B9%E6%B3%95%EF%BC%9A</em></p> 
  <p><span style="color:#666666">[3]</span></p> 
  <p>@tarojs/plugin-platform-weapp-qy: <em>https://github.com/NervJS/taro-plugin-platform-weapp-qy</em></p> 
  <p><span style="color:#666666">[4]</span></p> 
  <p>@tarojs/plugin-platform-alipay-dd: <em>https://github.com/NervJS/taro-plugin-platform-alipay-dd</em></p> 
  <p><span style="color:#666666">[5]</span></p> 
  <p>@tarojs/plugin-platform-alipay-iot: <em>https://github.com/NervJS/taro-plugin-platform-alipay-iot</em></p> 
  <p><span style="color:#666666">[6]</span></p> 
  <p>@tarojs/plugin-inject: <em>https://github.com/NervJS/taro-plugin-inject</em></p> 
  <p><span style="color:#666666">[7]</span></p> 
  <p>《Taro 助力京喜拼拼项目性能体验优化》: <em>https://docs.taro.zone/blog/2021-02-08-taro-jxpp#2-%E6%B8%B2%E6%9F%93%E6%80%A7%E8%83%BD%E4%BC%98%E5%8C%96</em></p> 
  <p><span style="color:#666666">[8]</span></p> 
  <p>经过与京喜拼拼项目的合作: <em>https://docs.taro.zone/blog/2021-02-08-taro-jxpp</em></p> 
  <p><span style="color:#666666">[9]</span></p> 
  <p>方案: <em>https://docs.taro.zone/docs/taro-in-miniapp</em></p> 
  <p><span style="color:#666666">[10]</span></p> 
  <p>Github: <em>https://github.com/NervJS/taro</em></p> 
  <p><span style="color:#666666">[11]</span></p> 
  <p>New JSX Transform: <em>https://reactjs.org/blog/2020/09/22/introducing-the-new-jsx-transform.html</em></p> 
  <p><span style="color:#666666">[12]</span></p> 
  <p>fast-refresh: <em>https://github.com/facebook/react/issues/16604#issuecomment-528663101</em></p> 
  <p><span style="color:#666666">[13]</span></p> 
  <p>滚动穿透: <em>https://docs.taro.zone/docs/next/react#%E9%98%BB%E6%AD%A2%E6%BB%9A%E5%8A%A8%E7%A9%BF%E9%80%8F</em></p> 
  <p><span style="color:#666666">[14]</span></p> 
  <p>迁移指南: <em>https://taro-docs.jd.com/taro/docs/next/migration</em></p> 
  <p><span style="color:#666666">[15]</span></p> 
  <p>58 技术团队: <em>https://github.com/wuba</em></p> 
  <p><span style="color:#666666">[16]</span></p> 
  <p>《增加 React Native 支持的 Taro 3.2.0 版本测试通告》: <em>https://taro-docs.jd.com/taro/blog/2020-12-02-taro-3-2-0-cannary-1</em></p> 
  <p><span style="color:#666666">[17]</span></p> 
  <p>问卷地址: <em>https://wj.qq.com/s2/6494361/09cf</em></p> 
 </div> 
</div>
                                        </div>
                                      
</div>
            