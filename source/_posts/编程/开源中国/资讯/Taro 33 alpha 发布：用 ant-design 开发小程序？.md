
---
title: 'Taro 3.3 alpha 发布：用 ant-design 开发小程序？'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2785'
author: 开源中国
comments: false
date: Mon, 26 Apr 2021 10:47:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2785'
---

<div>   
<div class="content">
                                                                    
                                                        <div> 
 <p>小程序的设计并没有完全遵循 Web 规范，导致小程序生态和传统 Web 开发生态之间的割裂，海量优秀的 Web 物料并不能直接用于小程序开发。因而 Taro 在相当一段时间内生态都相对薄弱，UI 框架选择不多的问题更是深深困扰着开发者。</p> 
 <p>另一方面，业界有着存量的 H5 应用，中短期内 H5 应用适配到小程序端的需要还会存在。我们希望能减少 H5 应用迁移到小程序端的成本，甚至能够直接运行在小程序端。</p> 
 <p>Taro 团队一直在思考如何最大限度地在小程序环境中复用 Web 生态，直到 Taro 3.0 诞生后，这种想法有了落地的可能。下文将介绍基于 Taro 3.0 实现 H5 同构的思路与问题，以及我们尝试适配了三大移动端 UI 框架 <strong>WEUI</strong>、<strong>Ant Design Mobile</strong>、<strong>VantUI</strong> 的实验结果。</p> 
 <h2>一、实现思路</h2> 
 <p>Taro 3.0 是一款重运行时的跨端框架，它通过模拟实现浏览器的 BOM 和 DOM API 实现了对 React、Vue 等 Web 开发框架的兼容。</p> 
 <p>既然已经有了浏览器环境的 BOM 和 DOM API，Taro 应用和 Web 应用之间的鸿沟在于小程序组件和 HTML 标签之间的差异。</p> 
 <!--truncate--> 
 <h3>支持渲染 H5 标签</h3> 
 <p>Taro3 的渲染数据流如下：</p> 
 <p><strong>前端框架 -> Taro DOM -> 小程序 data</strong></p> 
 <p>HTML 标签和小程序组件的标签名、属性、事件是有差异的，而前端框架无需感知这些差异。</p> 
 <p>因此前端框架适配层、Taro DOM 层不需要改动，只要在 <strong>Taro DOM 序列化为小程序 data</strong> 这一步作映射即可。</p> 
 <h4>1. 标签名映射</h4> 
 <p>HTML 标签相对小程序组件封装程度更低、功能更简单，可以看作是小程序组件的子集。因此可以按一定的规则，把 HTML 标签映射为小程序组件，如：</p> 
 <pre><code class="language-js">// Taro DOM 的序列化数据
&#123;
  nn: 'img'
&#125;
// 映射结果
&#123;
  nn: 'image'
&#125;</code></pre> 
 <p>完整的标签名映射规则请看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro-rfcs%2Fblob%2Fhtml-support%2Frfcs%2F0004-rendering-html.md%23%25E4%25B8%2580%25E6%25A0%2587%25E7%25AD%25BE%25E5%2590%258D%25E5%25BD%25B1%25E5%25B0%2584" target="_blank">RFC 附录一</a></p> 
 <h4>2. 属性映射</h4> 
 <p>如果 HTML 标签的属性能在对应小程序组件的属性上找到对应，则进行映射，如：</p> 
 <pre><code class="language-js">// Taro DOM 的序列化数据
&#123;
  nn: 'a',
  href: 'xxx'
  target: '_blank'
&#125;
// 映射结果
&#123;
  nn: 'navigator',
  url: 'xxx',
  openType: 'navigate'
&#125;</code></pre> 
 <p>完整的属性名映射规则请看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro-rfcs%2Fblob%2Fhtml-support%2Frfcs%2F0004-rendering-html.md%23%25E4%25BA%258C%25E5%25B1%259E%25E6%2580%25A7%25E5%2590%258D%25E5%25BD%25B1%25E5%25B0%2584" target="_blank">RFC 附录二</a></p> 
 <h4>3. 事件映射</h4> 
 <p>把 HTML 特有的事件在小程序端找到相似的事件进行映射，如：</p> 
 <table> 
  <thead> 
   <tr> 
    <th>HTML 事件</th> 
    <th>小程序组件事件</th> 
   </tr> 
  </thead> 
  <tbody> 
   <tr> 
    <td>click</td> 
    <td>tap</td> 
   </tr> 
  </tbody> 
 </table> 
 <p>完整的事件映射规则请看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro-rfcs%2Fblob%2Fhtml-support%2Frfcs%2F0004-rendering-html.md%23%25E4%25B8%2589%25E4%25BA%258B%25E4%25BB%25B6%25E5%25BD%25B1%25E5%25B0%2584" target="_blank">RFC 附录三</a></p> 
 <h3>样式</h3> 
 <h4>1. 标签选择器</h4> 
 <p>前文介绍了我们会把 HTML 标签映射为小程序组件，但是 H5 应用中使用到的 CSS 标签选择器就会失效。</p> 
 <p>因此 Taro 使用了类名去进行模拟：</p> 
 <p>1) 为所有 H5 标签都加上类名： <code>h5-$&#123;tagName&#125;</code>。</p> 
 <pre><code class="language-js">// 源代码
<div />
// 渲染结果
<view class="h5-div" /></code></pre> 
 <p>2) 使用 postcss 插件处理标签名选择器：</p> 
 <pre><code class="language-scss">// 标签名选择器
div &#123;&#125;
// 经 postcss 插件处理后变为类名选择器
.h5-div &#123;&#125;</code></pre> 
 <h4>2. 浏览器默认样式</h4> 
 <p>Taro 提供两种内置的浏览器默认样式，可以直接引入生效：</p> 
 <ul> 
  <li><code>@tarojs/taro/html.css</code>: W3C HTML4 的内置样式。只有 HTML4 标签样式，体积较小，兼容性强，能适应大多数情况。</li> 
  <li><code>@tarojs/taro/html5.css</code>: Chrome(Blink) HTML5 的内置样式。内置样式丰富，包括了大多数 HTML5 标签，体积较大，不一定支持所有小程序容器。</li> 
 </ul> 
 <h3>限制</h3> 
 <p>理想很美好，但现实却略显骨感。即使 Taro 能实现 BOM、DOM API，支持使用 HTML 标签等，同构方案还是存在着一些框架层面抹平不了的差异。以下列举出若干主要限制：</p> 
 <h4>1. 获取元素尺寸</h4> 
 <p>在 H5 中我们可以调用 DOM API 同步获取元素的尺寸：</p> 
 <pre><code class="language-js">// h5
const el = document.getElementById('#inner')
const res = el.getBoundingClientRect()
console.log(res)</code></pre> 
 <p>但是在小程序中，获取元素尺寸的 API 是异步的：</p> 
 <pre><code class="language-js">// 小程序
const query = Taro.createSelectorQuery()
query.select('#inner')
  .boundingClientRect()
  .exec(res => &#123;
    console.log(res)
  &#125;)</code></pre> 
 <p>因此不能兼容那些使用了同步 DOM API 去获取元素尺寸的组件。</p> 
 <h4>2. DOM API 差异</h4> 
 <p><code><canvas></code>、<code><video></code>、<code><audio></code> 等标签在 H5 端可以直接调用 <code>HTMLElement</code> 上的方法：</p> 
 <pre><code class="language-js">// h5
const el = document.getElementById('myVideo')
el.play()</code></pre> 
 <p>但是在 Taro 中，要调用组件上的原生方法，必须先创建对应的 <code>Context</code>：</p> 
 <pre><code class="language-js">// 小程序
const ctx = Taro.createVideoContext('myVideo')
ctx.play()</code></pre> 
 <h4>3. 样式限制</h4> 
 <p>部分样式或 CSS 选择器在小程序中不支持，如：</p> 
 <ul> 
  <li>通配符 *</li> 
  <li>媒体查询</li> 
  <li>属性选择器，当属性不是对应小程序组件的内置属性时</li> 
 </ul> 
 <h2>二、使用方法</h2> 
 <h3>升级 3.3.0-alpha 版本</h3> 
 <p>首先需要安装 v3.3 的 CLI 工具：</p> 
 <pre><code class="language-bash">npm i -g @tarojs/cli@alpha</code></pre> 
 <p>然后进入项目，把 <code>package.json</code> 文件中 taro 相关依赖的版本修改为 <code>^3.3.0-alpha.2</code>，再重新安装依赖（建议先把 <strong>node_modules</strong> 文件夹删除）。</p> 
 <h3>安装同构插件</h3> 
 <p>为了节省项目空间，同构功能是可选的，以 Taro 插件的形式提供。</p> 
 <p>首先开发者需要安装插件 <code>@tarojs/plugin-html</code>：</p> 
 <pre><code class="language-bash">npm i @tarojs/plugin-html</code></pre> 
 <p>然后配置使用此插件：</p> 
 <pre><code class="language-js">// config/index.js
const config = &#123;
  // ...
  plugins: [
    '@tarojs/plugin-html'
  ]
&#125;</code></pre> 
 <h2>三、示例项目</h2> 
 <p>为了验证同构功能的可用性和效果，我们对 CSS 样式库 <strong>WEUI</strong>、React 组件库 <strong>Antd Design Mobile</strong>、Vue2 组件库 <strong>VantUI</strong> 的所有组件进行了测试。</p> 
 <p>测试效果比较理想，甚至稍微超出我们的预期，配合各组件库自身的按需加载能力，能以小巧的体积使用丰富的组件，相信各位开发者会喜欢这个功能。</p> 
 <h3>WEUI</h3> 
 <p>仓库地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro-weui" target="_blank">taro-weui</a></p> 
 <p>WEUI 是一个 CSS 的样式库，与框架无关，兼容性比较高，大部分组件能直接使用。</p> 
 <h3>Antd Mobile Design</h3> 
 <p>仓库地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro-antd-mobile" target="_blank">taro-antd-mobile</a></p> 
 <blockquote> 
  <p>Antd Mobile Design 官方已经相当久没有维护，此适配项目属于实验性质。</p> 
 </blockquote> 
 <p>能直接兼容使用的组件大概为 80%，主要问题在于：</p> 
 <ol> 
  <li>组件库里广泛使用了 SVG，目前并不支持。</li> 
  <li>不能使用需要同步获取元素尺寸的部分组件。</li> 
 </ol> 
 <h3>VantUI</h3> 
 <p>仓库地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro-vant" target="_blank">taro-vant</a></p> 
 <p>VantUI 的组件十分丰富，能直接兼容使用的组件大概为 70%。部分开发者会在 Taro 中配合使用 Vant Weapp，但 Vant Weapp 只能运行在微信小程序，因此对 VantUI 的直接适配是一个很好的补充。</p> 
 <p>适配过程主要遇到的问题有：</p> 
 <ol> 
  <li>少量组件内置的 SVG ICON 不能显示。</li> 
  <li>不能使用需要同步获取元素尺寸的部分组件。</li> 
  <li>Vue <code><transition></code> 组件需要额外适配。</li> 
 </ol> 
 <h2>四、共建倡议</h2> 
 <p>同构方案还在持续优化中，部分实现还没有最终定稿。欢迎各位开发者到我们的论坛下留言，提出您的宝贵意见～：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FNervJS%2Ftaro%2Fdiscussions%2F9029" target="_blank">同构方案 RFC</a>。</p> 
 <p>另外，上述三款 Web UI 框架很多目前没能兼容的组件，只要针对小程序环境做一点兼容工作，是可以进行使用的。一款框架的生态需要官方和社区共同努力建设，单靠 Taro 团队及300多位贡献者的人力没办法撑起整个社区的生态。我们希望这三个兼容性示例项目能起到抛砖引玉的作用，吸引广大开发者进行共建，一起完善上述组件库，甚至不断地引入更多的 Web 端生态库，让跨端开发变得更轻松。十分期待您的参与～</p> 
</div>
                                        </div>
                                      
</div>
            