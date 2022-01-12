
---
title: 'NutUI 新增 React 版支持'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://img30.360buyimg.com/ling/jfs/t1/212181/9/9982/7437/61d40d5bEff7ed7be/b907817bd309d599.png'
author: 开源中国
comments: false
date: Tue, 11 Jan 2022 21:30:00 GMT
thumbnail: 'https://img30.360buyimg.com/ling/jfs/t1/212181/9/9982/7437/61d40d5bEff7ed7be/b907817bd309d599.png'
---

<div>   
<div class="content">
                                                                                            <h2 style="margin-left:0; margin-right:10px; text-align:left"><span style="color:#0e88eb">NutUI React 版如约而来</span></h2> 
<p style="color:black; margin-left:10px; margin-right:10px">京东零售开源项目 NutUI 是一套京东风格的轻量级移动端组件库，开发和服务于移动 Web 界面的企业级产品。随着 NutUI 的用户越来越多，社区交流群里对 React 版本的呼声也越来越高。我们响应社区的呼声，2021 年 6 月开始规划并启动 React 版的开发。经过长时间的研发与打磨，React 版终于要和大家见面了！</p> 
<p style="color:black; margin-left:10px; margin-right:10px">NutUI 是一款京东风格的多端统一开发组件库，之前只有 Vue 语言版。它也支持使用 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnutui.jd.com%2F%23%2Fstarttaro" target="_blank">Vue3</a> 来编写可以同时在小程序和 H5 平台上运行的应用，帮助开发者提升效率，改善开发体验，降低多端开发成本。</p> 
<p style="color:black; margin-left:10px; margin-right:10px">2018 年开源以来，NutUI 逐渐受到业界关注。其打造开发体验佳的初心及持续的打磨升级受到内外开发者的广泛认可，对于我们来说无疑是一件备受鼓舞的事情。随着用户的增多，社区交流群里对 React 版本的呼声也越来越高。我们积极响应社区的呼声，2021 年 6 月开始规划并启动 React 版的开发，经过长时间的开发与打磨，NutUI-React 终于要和大家见面了！</p> 
<p style="color:black; margin-left:10px; margin-right:10px">NutUI-React 在技术和视觉方面都做出了较大改进，让组件看起来更绚丽，开发者用起来更舒服。</p> 
<blockquote>
 <strong style="color:#0e88eb">★ </strong> 
 <p style="color:#0e88eb; margin-left:0; margin-right:0">源码抢先看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjdf2e%2Fnutui-react" target="_blank">https://github.com/jdf2e/nutui-react</a></p> 
 <span style="color:#0e88eb">”</span>
</blockquote> 
<p style="color:black; margin-left:10px; margin-right:10px">手机扫码体验</p> 
<p><img alt="NutUI 体验二维码" src="https://img30.360buyimg.com/ling/jfs/t1/212181/9/9982/7437/61d40d5bEff7ed7be/b907817bd309d599.png" referrerpolicy="no-referrer"></p> 
<p>NutUI 体验二维码</p> 
<h2 style="margin-left:0; margin-right:10px; text-align:left"><span style="color:#0e88eb">组件概览</span></h2> 
<p style="color:black; margin-left:10px; margin-right:10px">本期共计 45 个组件，包含五大通用类别：<strong style="color:#0e88eb">基础</strong>、<strong style="color:#0e88eb">布局</strong>、<strong style="color:#0e88eb">导航</strong>、<strong style="color:#0e88eb">操作反馈</strong>、<strong style="color:#0e88eb">数据录入</strong>及若干京东特色组件，满足大多数业务场景的需求。</p> 
<p style="color:black; margin-left:10px; margin-right:10px">结合项目中的应用，重点关注「数据交互」和「行为交互」类组件，如 Toast、Dialog 提示类的组件，PopUp、Picker 等选择面板类的组件，InputNumber、Rate、Address 等电商风格鲜明的组件，经常搭配用来处理移动端分页和回到顶部的 Infinite 和 BackTop 等。</p> 
<p><img alt="img" src="https://img14.360buyimg.com/ling/jfs/t1/176177/26/25273/732296/61d570d1Eb1e1ca0d/074c5b83ea50e7e9.jpg" referrerpolicy="no-referrer"></p> 
<p>img</p> 
<h2 style="margin-left:0; margin-right:10px; text-align:left"><span style="color:#0e88eb">技术看点</span></h2> 
<h3><span style="color:#0e88eb">1、基于稳定的 React 17</span></h3> 
<p style="color:black; margin-left:10px; margin-right:10px">React 17 的定位是让 React 自身升级变得更加容易，较之前版本的修改较为平和，重大改动不多。2021 年 11 月 15 日 React 18 进入了 Beta 阶段，在面向未来的 React 组件库中采用 React 17 将有利于组件库对 React 18 或未来的 React 版本进行，对于您当前的项目升级到 17 来说成本较低，这也方便您引入 NutUI-React 组件库。</p> 
<h3><span style="color:#0e88eb">2、按需加载</span></h3> 
<p style="color:black; margin-left:10px; margin-right:10px">NutUI-React 的 JavaScript 代码默认支持基于 ES Modules 的 Tree Shaking，并提供了详细的文档支持，简化的配置选项。这一点也是使用者非常关注的一项技术点，对于我们项目中打包代码体积有很好的帮助。</p> 
<h3><span style="color:#0e88eb">3、支持主题定制</span></h3> 
<p style="color:black; margin-left:10px; margin-right:10px">目前 NutUI-React 提供京东风格的出厂主题，同时也提供了完整的 Sass 文件，支持通过 Sass additionalData 定义<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnutui.jd.com%2Freact%2F%23%2Ftheme-react" target="_blank">个性化</a>主题。</p> 
<h3><span style="color:#0e88eb">4、全面使用 TypeScript</span></h3> 
<p style="color:black; margin-left:10px; margin-right:10px">NutUI-React 引入 TypeScript 4，加强了在 TypeScript 上的严格的类型校验，和 Demo 输出的严谨性。我们采用常用代码规范如 react/recommended、react-hooks/recommended、@typescript-eslint/recommended、prettier/recommended，以此加强了 StyleLint 和 ESLint （含 TSLint 功能）的校验，使组件库在交付质量上更进一步，让您用着放心。</p> 
<h3><span style="color:#0e88eb">5、基于 Vite 构建工具</span></h3> 
<p style="color:black; margin-left:10px; margin-right:10px">组件库工程基于 Vite 构建工具，使用 Rollup 的 Vite 大大提升了开发者在开发阶段的热更新效率，同时配置开箱即用。</p> 
<h2 style="margin-left:0; margin-right:10px; text-align:left"><span style="color:#0e88eb">视觉体验</span></h2> 
<p style="color:black; margin-left:10px; margin-right:10px">沿用 Vue 3 版本的视觉规范，使用 JD APP 10.0 设计语言，结合京东站内众多应用场景对已有组件进行了梳理优化，为站内页面开发提供了视觉规范依据，进一步完善标准化的设计语义的定义。</p> 
<p><img alt="img" src="https://img14.360buyimg.com/ling/jfs/t1/125377/15/21145/963945/61d5715bE30a8efa8/00aa6572d0ddbc88.png" referrerpolicy="no-referrer"></p> 
<p>img</p> 
<h2 style="margin-left:0; margin-right:10px; text-align:left"><span style="color:#0e88eb">文档呈现</span></h2> 
<p style="color:black; margin-left:10px; margin-right:10px">延续 Vue 版本上的风格和习惯，方便老用户使用。在实现上做了较大改动，本次将整个文档中心从组件库源码中进行了拆分，并适配多语言多版本的文档展示。从开发者的角度上，当前版本需要关注 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjdf2e%2Fnutui-docs" target="_blank">NUTUI-Docs</a> 代码库。作为使用者，我们留有一个小彩蛋，部分组件集成了“代码的在线编辑器”，您可以通过在线编辑，所见即所得您想要的效果，期待您找到这些小彩蛋，此功能计划春节后将全部开放。</p> 
<h2 style="margin-left:0; margin-right:10px; text-align:left"><span style="color:#0e88eb">快速上手</span></h2> 
<p style="color:black; margin-left:10px; margin-right:10px">至此，相信您已经对 React 组件库元旦版已经有了大概的了解，它像市面上所有的组件库一样，希望给你带来高效、友好的开发体验。同时，也希望给你带来更严谨的代码体验和更丰富的代码示例。希望 TA 像一本书，供你茶余饭后，品读玩味。更希望 TA 像一个伙伴，在你工作时间，共创解惑。</p> 
<h3><span style="color:#0e88eb">安装</span></h3> 
<pre><code>npm i @nutui/nutui-react
</code></pre> 
<p style="color:black; margin-left:10px; margin-right:10px">项目里使用 NutUI-React</p> 
<pre><code><span style="color:#c678dd">import</span> * <span style="color:#c678dd">as</span> React <span style="color:#c678dd">from</span> <span style="color:#98c379">"react"</span>;
<span style="color:#c678dd">import</span> * <span style="color:#c678dd">as</span> ReactDOM <span style="color:#c678dd">from</span> <span style="color:#98c379">"react-dom"</span>;
<span style="color:#c678dd">import</span> <span style="color:#98c379">'@nutui/nutui-react/dist/style.css'</span>
<span style="color:#c678dd">import</span> &#123; Icon &#125; <span style="color:#c678dd">from</span> <span style="color:#98c379">'@nutui/nutui-react'</span>;


ReactDOM.render(
  <span><span><<span style="color:#e06c75">div</span> <span style="color:#d19a66">className</span>=<span style="color:#98c379">"App"</span>></span>
    <span><<span style="color:#e06c75">Icon</span> <span style="color:#d19a66">name</span>=<span style="color:#98c379">"dongdong"</span>></span><span></<span style="color:#e06c75">Icon</span>></span>
  <span></<span style="color:#e06c75">div</span>></span></span>,
  <span style="color:#e6c07b">document</span>.getElementById(<span style="color:#98c379">"app"</span>)
)
</code></pre> 
<h3><span style="color:#0e88eb">按需加载，有两种方式</span></h3> 
<h4><span>方式一、安装 vite 插件</span></h4> 
<pre><code>npm install vite-plugin-style-<span style="color:#c678dd">import</span> --save-dev
</code></pre> 
<p style="color:black; margin-left:10px; margin-right:10px">在 vite config 中修改配置</p> 
<pre><code><span style="color:#c678dd">import</span> &#123; defineConfig &#125; <span style="color:#c678dd">from</span> <span style="color:#98c379">"vite"</span>;
<span style="color:#c678dd">import</span> react <span style="color:#c678dd">from</span> <span style="color:#98c379">"@vitejs/plugin-react"</span>;
<span style="color:#c678dd">import</span> styleImport <span style="color:#c678dd">from</span> <span style="color:#98c379">"vite-plugin-style-import"</span>;
<em>// https://vitejs.dev/config/</em>
<span style="color:#c678dd">export</span> <span style="color:#c678dd">default</span> defineConfig(&#123;
  <span style="color:#d19a66">css</span>: &#123;
    <span style="color:#d19a66">preprocessorOptions</span>: &#123;
      <span style="color:#d19a66">scss</span>: &#123;
        <em>// 配置 nutui 全局 scss 变量</em>
        <span style="color:#d19a66">additionalData</span>: <span style="color:#98c379">`@import "@nutui/nutui-react/dist/styles/variables.scss";`</span>,
      &#125;,
    &#125;,
  &#125;,
  <span style="color:#d19a66">plugins</span>: [
    react(),
    styleImport(&#123;
      <span style="color:#d19a66">libs</span>: [
        &#123;
          <span style="color:#d19a66">libraryName</span>: <span style="color:#98c379">"@nutui/nutui-react"</span>,
          <span style="color:#d19a66">libraryNameChangeCase</span>: <span style="color:#98c379">"pascalCase"</span>,
          <span style="color:#d19a66">resolveStyle</span>: <span>(<span>name</span>) =></span> &#123;
            <span style="color:#c678dd">return</span> <span style="color:#98c379">`@nutui/nutui-react/dist/packages/<span style="color:#e06c75">$&#123;name.toLowerCase()&#125;</span>/<span style="color:#e06c75">$&#123;name.toLowerCase()&#125;</span>.scss`</span>;
          &#125;,
        &#125;,
      ],
    &#125;),
  ],
&#125;);
</code></pre> 
<h4><span>方式二、使用 webpack 插件</span></h4> 
<pre><code>npm install babel-plugin-<span style="color:#c678dd">import</span> --save-dev
</code></pre> 
<p style="color:black; margin-left:10px; margin-right:10px">在 babel.confi.js 里添加配置</p> 
<pre><code>&#123;
  <em>// ...</em>
  <span style="color:#d19a66">plugins</span>: [
    [
      <span style="color:#98c379">"import"</span>,
      &#123;
        <span style="color:#98c379">"libraryName"</span>: <span style="color:#98c379">"@nutui/nutui-react"</span>,
        <span style="color:#98c379">"libraryDirectory"</span>: <span style="color:#98c379">"dist/esm"</span>,
        <span style="color:#98c379">"style"</span>: <span style="color:#56b6c2">true</span>,
        <span style="color:#98c379">"camel2DashComponentName"</span>: <span style="color:#56b6c2">false</span>
      &#125;,
      <span style="color:#98c379">'nutui-react'</span>
    ]
  ]
&#125;
</code></pre> 
<p style="color:black; margin-left:10px; margin-right:10px">以上，即对组件的按需加载。同时，我们还提供 webpack 的方法，可移步文档中心查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnutui.jd.com%2Freact%2F%23%2Fstart-react" target="_blank">实践</a>。</p> 
<h2 style="margin-left:0; margin-right:10px; text-align:left"><span style="color:#0e88eb">发版计划</span></h2> 
<p style="color:black; margin-left:10px; margin-right:10px">我们将按照 SemVer 版本控制规范进行发版。目前在 2022Q1 阶段对已有组件进行项目验证，和代码优化。在此期间，您可以加入到我们的共建计划中，在 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjdf2e%2Fnutui-react%2Fissues" target="_blank">Github </a>上提出您的宝贵建议，以及在使用时遇到的一切问题，我们也会对此每周进行一次小版本的迭代。您也可以在这里给我们精神支持，点上一颗 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjdf2e%2Fnutui-react" target="_blank">Star</a>。</p> 
<h2 style="margin-left:0; margin-right:10px; text-align:left"><span style="color:#0e88eb">联系我们</span></h2> 
<ul style="list-style-type:disc"> 
 <li> <p>Github 地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjdf2e%2Fnutui-react" target="_blank">https://github.com/jdf2e/nutui-react</a></p> </li> 
 <li> <p>NPM 地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.npmjs.com%2Fpackage%2F%40nutui%2Fnutui-react" target="_blank">https://www.npmjs.com/package/@nutui/nutui-react</a></p> </li> 
</ul>
                                        </div>
                                      
</div>
            