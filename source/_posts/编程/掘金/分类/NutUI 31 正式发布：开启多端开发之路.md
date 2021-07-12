
---
title: 'NutUI 3.1 正式发布：开启多端开发之路'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3df4c120ad7948019f931733da41a8eb~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 11 Jul 2021 15:17:25 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3df4c120ad7948019f931733da41a8eb~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>作为一款具有京东风格的组件库，我们一直致力于用心打造更符合开发者体验的组件库。NutUI 3.0 上线后我们研发团队也在不断的优化、测试、使用、迭代 Vue3 的相关组件，但是在跨端小程序的开发过程中，发现没有合适的组件库可以支持多端开发。为了填补这一空白，同时为了优化开发者体验，让 NutUI 能够为更多的开发者带来便利，我们决定在 NutUI 中增加小程序多端适配的能力。</p>
<h2 data-id="heading-0">NutUI 开启多端之旅</h2>
<p>当前业务环境下,研发面临的当前的业务场景越来越复杂,产品发布的渠道越来越多，业务在拥有自己 APP 的同时出现了很多小程序渠道，以前研发只需要关注到业务的 APP 和 H5 就好，自从微信产出了微信小程序后，业界各大互联网公司都研发出自己的小程序平台，而且以后可能会愈来愈多，每个小程序平台都有自己的框架语言，如果业务多发布一个渠道，研发就要多写一套代码，在业务的渠道变多而研发资源匮乏的情况下，写一套代码可以快速复用到各个小程序是研发当前的首要痛点。</p>
<p>为了给开发者提供更高效便捷的开发方式，NutUI 和 Taro 合力，现已可以用 NutUI 开发小程序了，NutUI 提供了30+ 组件涵盖了日常业务开发使用的大部分组件。</p>
<p>二者的结合，不仅可以让开发者一处代码，多端运行，畅快自如地开发小程序。更可以在开发过程中，使用到更美观、更便捷、组件更丰富的组件库。我们将 NutUI 和 Taro 更完美地接合到一起，Taro 官方将 NutUI 作为 Vue技术栈的推荐组件库。现在开发者将可以使用 NutUI 无缝开发 H5 和多端小程序。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3df4c120ad7948019f931733da41a8eb~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-1">NutUI 3.0 全新架构升级</h4>
<p>NutUI 3.0 升级以来，我们对框架进行了一些变更，下面是 NutUI 3.0 的基本框架结构，相比 2.0 我们做出了以下升级：</p>
<ul>
<li>Webpack 升级为 Vite ，开发效率大幅提升</li>
<li>全面拥抱 TypeScript</li>
<li>Vue3支持</li>
<li>支持小程序开发</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/abac0eaca8cd4ffcb062bf761c3d7c20~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">视觉体验全面升级</h2>
<h4 data-id="heading-3">官网焕然一新</h4>
<p>NutUI 从 2.0 到 3.0 不仅是技术上的全新升级，组件库产品形象也焕然一新，NutUI 3.0 从官网到文档再到 Demo 等我们都进行了改版。改版后的首页，从多维度展示 NutUI 组件库的平台特点和知识沉淀，对于新用户可以更好且系统性的了解 NutUI 。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b6cbfaad62bf45aaafd30c7a006ca297~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">组件文档变化</h4>
<p>在用户时间注意力稀缺的时代，作为一个工具型的平台，更需要便捷高效的帮助用户实现目标。我们在文档页右上角加上了切换文档的 Tab，这样开发者可以更高效率的找到自己想要的相关文档，我们现在已经支持小程序预览 Demo 了，扫描右侧二维码可以直接查看 NutUI 3.X 组件库的小程序 Demo。
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fnutui.jd.com%2F3x%2F%23%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://nutui.jd.com/3x/#/" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6d83639baacf4f15a031800ac4397bc4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></a></p>
<h2 data-id="heading-5">快速上手小程序开发</h2>
<h4 data-id="heading-6">安装</h4>
<ul>
<li>通过 Npm 或 Yarn 安装</li>
</ul>
<h4 data-id="heading-7">安装 Taro 脚手架</h4>
<pre><code class="hljs language-bash copyable" lang="bash"><span class="hljs-comment"># 使用 npm 安装 CLI</span>
npm install -g @tarojs/cli

<span class="hljs-comment"># OR 使用 yarn 安装 CLI</span>
yarn global add @tarojs/cli

<span class="hljs-comment"># OR 安装了 cnpm，使用 cnpm 安装 CLI</span>
cnpm install -g @tarojs/cli
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>!!! 值得一提的是，如果安装过程出现sass相关的安装错误，请在安装 mirror-config-china 后重试。</p>
</blockquote>
<pre><code class="hljs language-bash copyable" lang="bash">npm install -g mirror-config-china
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">检查是否安装成功</h4>
<pre><code class="hljs language-bash copyable" lang="bash">taro -v
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-9">项目初始化</h4>
<p>使用命令创建模板：</p>
<pre><code class="hljs language-bash copyable" lang="bash">taro init myApp
<span class="copy-code-btn">复制代码</span></code></pre>
<p>按照下方图片依次选择，选择 Vue3 + NutUI 模板
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d55f24e1e3e84cee8658697fc3d599ac~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>选择vue3-NutUI的模板时，内置了按需加载的使用方式，开发者可根据自己的使用场景选择全局使用。</p>
<h4 data-id="heading-10">按需加载使用示例（推荐使用方式）</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">"./App.vue"</span>;
<span class="hljs-keyword">import</span> &#123; Button, Cell, Icon &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"@nutui/nutui-taro"</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">"@nutui/nutui-taro/dist/style.css"</span>;
createApp(App).use(Button).use(Cell).use(Icon);
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">全局使用示例</h4>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; createApp &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">import</span> App <span class="hljs-keyword">from</span> <span class="hljs-string">"./App.vue"</span>;
<span class="hljs-keyword">import</span> NutUI <span class="hljs-keyword">from</span> <span class="hljs-string">"@nutui/nutui-taro"</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">"@nutui/nutui-taro/dist/style.css"</span>;
createApp(App).use(NutUI);
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>注意：这种方式将会导入所有组件</p>
</blockquote>
<p>通过以上方式，即可快速开发小程序场景。 NutUI 团队会持续迭代多端功能，让开发者可以拥有更友好的多端开发体验。</p>
<h2 data-id="heading-12">未来展望</h2>
<p>随着 NutUI 的用户群体越来越多，React 版本的呼声越来越高，我们接下来会将部分的精力投入到 React 技术栈开发中，NutUI-React 将会在 Q4 与大家见面；我们会对 NutUI 的产品体验进行不断优化和迭代，在 Vue 的版本上 NutUI 团队将会持续不断的丰富组件；为了满足大部分开发者在使用组件时需要给上游设计师提供组件规范，我们正在进行 NutUI 设计规范的输出和整理，不久就会在官网上线 Sketch 资源包，尽情期待~
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e180eaaf750f41779f1ac3892e5fdeff~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-13">问卷调研</h2>
<p>为了给您提供更好的服务，希望您能抽出几分钟时间，将您的感受和建议告诉我们，我们会对您的填答信息严格保密。本次调研为有奖调查，完整填答问卷的用户可抽取<strong>京东joy周边礼品</strong>。</p>
<p>问卷链接：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fget.jd.com%2F%23%2Fsurvey%2Findex%3Fid%3D60280" target="_blank" rel="nofollow noopener noreferrer" title="https://get.jd.com/#/survey/index?id=60280" ref="nofollow noopener noreferrer">get.jd.com/#/survey/in…</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fget.jd.com%2F%23%2Fsurvey%2Findex%3Fid%3D60280" target="_blank" rel="nofollow noopener noreferrer" title="https://get.jd.com/#/survey/index?id=60280" ref="nofollow noopener noreferrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5283436a7ad94639bef4dfd0172ab9a9~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></a></p>
<h2 data-id="heading-14">链接</h2>
<ul>
<li>仓库地址: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjdf2e%2Fnutui" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/jdf2e/nutui" ref="nofollow noopener noreferrer">github.com/jdf2e/nutui</a></li>
<li>官网地址: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fnutui.jd.com%2F3x%2F%23%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://nutui.jd.com/3x/#/" ref="nofollow noopener noreferrer">nutui.jd.com/3x/#/</a></li>
<li>加入我们: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fnutui.jd.com%2F%23%2Fjoinus" target="_blank" rel="nofollow noopener noreferrer" title="https://nutui.jd.com/#/joinus" ref="nofollow noopener noreferrer">nutui.jd.com/#/joinus</a></li>
<li>反馈我们：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjdf2e%2Fnutui%2Fissues" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/jdf2e/nutui/issues" ref="nofollow noopener noreferrer">github.com/jdf2e/nutui…</a></li>
</ul></div>  
</div>
            