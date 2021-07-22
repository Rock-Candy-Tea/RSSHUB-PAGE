
---
title: '京东开源组件库 NutUI 3.1 正式发布：支持 Taro，开启多端开发之路'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://storage.360buyimg.com/imgtools/efcc42168f-68defa60-dee6-11eb-b377-57572a0b6c4d.png'
author: 开源中国
comments: false
date: Thu, 22 Jul 2021 14:00:00 GMT
thumbnail: 'https://storage.360buyimg.com/imgtools/efcc42168f-68defa60-dee6-11eb-b377-57572a0b6c4d.png'
---

<div>   
<div class="content">
                                                                                            <div style="text-align:start"> 
 <div>
  作为一款具有京东风格的组件库，我们一直致力于用心打造更符合开发者体验的组件库。NutUI 3.0 上线后我们研发团队也在不断的优化、测试、使用、迭代 Vue3 的相关组件，但是在跨端小程序的开发过程中，发现没有合适的组件库可以支持多端开发。为了填补这一空白，同时为了优化开发者体验，让 NutUI 能够为更多的开发者带来便利，我们决定在 NutUI 中增加小程序多端适配的能力。
 </div> 
 <div> 
  <div> 
   <h2>NutUI 开启多端之旅</h2> 
   <p>当前业务环境下,研发面临的当前的业务场景越来越复杂,产品发布的渠道越来越多，业务在拥有自己 APP 的同时出现了很多小程序渠道，以前研发只需要关注到业务的 APP 和 H5 就好，自从微信产出了微信小程序后，业界各大互联网公司都研发出自己的小程序平台，而且以后可能会愈来愈多，每个小程序平台都有自己的框架语言，如果业务多发布一个渠道，研发就要多写一套代码，在业务的渠道变多而研发资源匮乏的情况下，写一套代码可以快速复用到各个小程序是研发当前的首要痛点。</p> 
   <p>为了给开发者提供更高效便捷的开发方式，NutUI 和 Taro 合力，现已可以用 NutUI 开发小程序了，NutUI 提供了30+ 组件涵盖了日常业务开发使用的大部分组件。</p> 
   <p>二者的结合，不仅可以让开发者一处代码，多端运行，畅快自如地开发小程序。更可以在开发过程中，使用到更美观、更便捷、组件更丰富的组件库。我们将 NutUI 和 Taro 更完美地接合到一起，Taro 官方将 NutUI 作为 Vue技术栈的推荐组件库。现在开发者将可以使用 NutUI 无缝开发 H5 和多端小程序。</p> 
   <p> </p> 
   <div>
    <img alt src="https://storage.360buyimg.com/imgtools/efcc42168f-68defa60-dee6-11eb-b377-57572a0b6c4d.png" style="margin-bottom:30px; margin-top:30px" referrerpolicy="no-referrer">
   </div> 
   <p> </p> 
   <h4>NutUI 3.0 全新架构升级</h4> 
   <p>NutUI 3.0 升级以来，我们对框架进行了一些变更，下面是 NutUI 3.0 的基本框架结构，相比 2.0 我们做出了以下升级：</p> 
   <ul> 
    <li>Webpack 升级为 Vite ，开发效率大幅提升</li> 
    <li>全面拥抱 TypeScript</li> 
    <li>Vue3支持</li> 
    <li>支持小程序开发 
     <div>
      <img alt src="https://storage.360buyimg.com/imgtools/b960625b9e-d216b9a0-df04-11eb-bdd5-2b6f1d99ffde.png" style="margin-bottom:30px" referrerpolicy="no-referrer">
     </div> </li> 
   </ul> 
   <h2>视觉体验全面升级</h2> 
   <h4>官网焕然一新</h4> 
   <p>NutUI 从 2.0 到 3.0 不仅是技术上的全新升级，组件库产品形象也焕然一新，NutUI 3.0 从官网到文档再到 Demo 等我们都进行了改版。改版后的首页，从多维度展示 NutUI 组件库的平台特点和知识沉淀，对于新用户可以更好且系统性的了解 NutUI 。</p> 
   <p> </p> 
   <div>
    <img alt src="https://storage.360buyimg.com/imgtools/88aeaa705e-7c146530-def4-11eb-9acc-b79eb377d415.jpeg" style="margin-bottom:30px; margin-top:30px" referrerpolicy="no-referrer">
   </div> 
   <p> </p> 
   <h4>组件文档变化</h4> 
   <p>在用户时间注意力稀缺的时代，作为一个工具型的平台，更需要便捷高效的帮助用户实现目标。我们在文档页右上角加上了切换文档的 Tab，这样开发者可以更高效率的找到自己想要的相关文档，我们现在已经支持小程序预览 Demo 了，扫描右侧二维码可以直接查看 NutUI 3.X 组件库的小程序 Demo。 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnutui.jd.com%2F3x%2F%23%2F" target="_blank"><img alt src="https://storage.360buyimg.com/imgtools/88deabf02c-92a80fd0-defa-11eb-b377-57572a0b6c4d.jpeg" style="margin-bottom:30px; margin-top:30px" referrerpolicy="no-referrer"></a></p> 
   <h2>快速上手小程序开发</h2> 
   <h4>安装</h4> 
   <ul> 
    <li>通过 Npm 或 Yarn 安装</li> 
   </ul> 
   <h4>安装 Taro 脚手架</h4> 
   <pre><code># 使用 npm 安装 CLI
npm install -g @tarojs/cli

# OR 使用 yarn 安装 CLI
yarn <span style="color:#de935f">global</span> add @tarojs/cli

# OR 安装了 cnpm，使用 cnpm 安装 CLI
cnpm install -g @tarojs/cli</code></pre> 
   <blockquote> 
    <p>!!! 值得一提的是，如果安装过程出现sass相关的安装错误，请在安装 mirror-config-china 后重试。</p> 
   </blockquote> 
   <pre><code><span style="color:#f0c674">npm</span> install -g mirror-config-china</code></pre> 
   <h4>检查是否安装成功</h4> 
   <pre><code><span style="color:#f0c674">taro</span> -v</code></pre> 
   <h4>项目初始化</h4> 
   <p>使用命令创建模板：</p> 
   <pre><code>taro <span style="color:#b294bb">init</span> myApp</code></pre> 
   <p>按照下方图片依次选择，选择 Vue3 + NutUI 模板</p> 
   <div>
    <img alt src="https://storage.360buyimg.com/jdc-article/7E0DDB75DF63D552A1EA01CDAEED659A.jpg" style="margin-bottom:30px; margin-top:30px" referrerpolicy="no-referrer">
   </div> 
   <p> </p> 
   <h4>NPM 使用示例</h4> 
   <pre><code><span style="color:#b294bb">import</span> &#123; createApp &#125; <span style="color:#b294bb">from</span> <span style="color:#b5bd68">"vue"</span>;
<span style="color:#b294bb">import</span> App <span style="color:#b294bb">from</span> <span style="color:#b5bd68">"./App.vue"</span>;
<span style="color:#b294bb">import</span> NutUI <span style="color:#b294bb">from</span> <span style="color:#b5bd68">"@nutui/nutui-taro"</span>;
<span style="color:#b294bb">import</span> <span style="color:#b5bd68">"@nutui/nutui-taro/dist/style.css"</span>;
createApp(App).use(NutUI).mount(<span style="color:#b5bd68">"#app"</span>);</code></pre> 
   <blockquote> 
    <p>注意：这种方式将会导入所有组件</p> 
   </blockquote> 
   <h4>推荐使用按需加载</h4> 
   <pre><code><span style="color:#b294bb">import</span> &#123; createApp &#125; <span style="color:#b294bb">from</span> <span style="color:#b5bd68">"vue"</span>;
<span style="color:#b294bb">import</span> App <span style="color:#b294bb">from</span> <span style="color:#b5bd68">"./App.vue"</span>;
<span style="color:#b294bb">import</span> &#123; Button, Cell, Icon &#125; <span style="color:#b294bb">from</span> <span style="color:#b5bd68">"@nutui/nutui-taro"</span>;
<span style="color:#b294bb">import</span> <span style="color:#b5bd68">"@nutui/nutui-taro/dist/style.css"</span>;
createApp(App).use(Button).use(Cell).use(Icon).mount(<span style="color:#b5bd68">"#app"</span>);</code></pre> 
   <h2>未来展望</h2> 
   <p>随着 NutUI 的用户群体越来越多，React 版本的呼声越来越高，我们接下来会将部分的精力投入到 React 技术栈开发中，NutUI-React 将会在 Q4 与大家见面；我们会对 NutUI 的产品体验进行不断优化和迭代，在 Vue 的版本上 NutUI 团队将会持续不断的丰富组件；为了满足大部分开发者在使用组件时需要给上游设计师提供组件规范，我们正在进行 NutUI 设计规范的输出和整理，不久就会在官网上线 Sketch 资源包，尽情期待~</p> 
   <div>
    <img alt src="http://storage.360buyimg.com/jdc-article/%E8%A7%86%E8%A7%89%E8%A7%84%E8%8C%83-jelly.jpg" style="margin-bottom:30px; margin-top:30px" referrerpolicy="no-referrer">
   </div> 
   <p> </p> 
   <h2>问卷调研</h2> 
   <p>为了给您提供更好的服务，希望您能抽出几分钟时间，将您的感受和建议告诉我们，我们会对您的填答信息严格保密。本次调研为有奖调查，完整填答问卷的用户可抽取<strong>京东joy周边礼品</strong>。</p> 
   <h2>问卷链接： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fget.jd.com%2F%23%2Fsurvey%2Findex%3Fid%3D60280" target="_blank">https://get.jd.com/#/survey/index?id=60280 </a><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fget.jd.com%2F%23%2Fsurvey%2Findex%3Fid%3D60280" target="_blank"><img alt src="https://storage.360buyimg.com/imgtools/c2c4a09af5-7af6c890-dee6-11eb-b377-57572a0b6c4d.jpeg" style="margin-bottom:30px; margin-top:30px" referrerpolicy="no-referrer"></a></h2> 
   <h2>链接</h2> 
   <ul> 
    <li>仓库地址: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjdf2e%2Fnutui" target="_blank">https://github.com/jdf2e/nutui</a></li> 
    <li>官网地址: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnutui.jd.com%2F3x%2F%23%2F" target="_blank">https://nutui.jd.com/3x/#/</a></li> 
    <li>加入我们: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnutui.jd.com%2F%23%2Fjoinus" target="_blank">https://nutui.jd.com/#/joinus</a></li> 
    <li>反馈我们： <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fjdf2e%2Fnutui%2Fissues" target="_blank">https://github.com/jdf2e/nutui/issues</a></li> 
   </ul> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            