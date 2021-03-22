
---
title: 'Fes.js for Vue3，简洁却不简单'
categories: 
    - 编程
    - 开源中国 - 资讯
author: 开源中国 - 资讯
comments: false
date: Mon, 22 Mar 2021 07:28:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-f50bbeb11b5ca84bf436c2955d90e4637dd.png'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#888888">Fes.js 是一套优秀的中后台前端解决方案。</span><span style="color:#888888">提供初始项目，开发调试，模拟接口，编译打包的命令行工具。</span><span style="color:#888888">内置布局，权限，数据字典，状态管理，存储，API 等多个模块。</span><span style="color:#888888">以约定，配置化，组件化的设计思想，让用户只需关心使用组件构造页面内容。</span><span style="color:#888888">基于 Vue.js，上手简单。</span><span style="color:#888888">经过多个项目中打磨，趋于稳定。</span></p> 
<p><span style="color:#888888"><span style="color:#888888">1.0 上线后收到了社区小伙伴们的良好建议，<span style="background-color:#f1f8ff; color:#888888">在此</span><span style="background-color:#f1f8ff; color:#888888">谢谢支持</span><span style="background-color:#f1f8ff; color:#888888"> Fes.js 的你们，</span>希望本次升级给大家带来更多的帮助，期待未来共同创造更多功能。</span></span></p> 
<p>我们需要开发的大部分前端应用的业务比较类似，比如中后台应用大多都是工作台、增删改查、权限、图表等。所以在开发一个前端应用之前，除了环境准备工作，还需要处理这些基础的业务逻辑。</p> 
<p><img alt height="498" src="https://oscimg.oschina.net/oscnet/up-f50bbeb11b5ca84bf436c2955d90e4637dd.png" width="700" referrerpolicy="no-referrer"></p> 
<p>如果没有统一的规范或者框架，技术选型也要看开发人员的喜好，每个项目的准备工作都手动处理一遍，非常耗费时间。久而久之，当团队会出现多种技术栈，历史项目将越来越难维护。所以我们需要一套完整的解决方案，管理开发到部署整个流程，在问题发生前将其解决。</p> 
<p><img alt height="449" src="https://oscimg.oschina.net/oscnet/up-c79dd1d1b6f509bc25097d0ebba350ce185.png" width="700" referrerpolicy="no-referrer"></p> 
<p><span style="color:#021eaa"><strong><span style="color:#021eaa">Fes.js 2.0 做了哪些改进</span></strong></span></p> 
<p>对于 1.0  本只支持 PC 应用、不易扩展等不足，我们在 2.0 版本重新设计了以插件机制为基础的可扩展架构。</p> 
<p>重写了 90% 代码，Fes.js 2.0 以 <strong>Vue 3.0</strong> 和路由为基础，同时支持配置式路由和约定式路由，并以此进行功能扩展。匹配了覆盖编译时和运行时生命周期完善的插件体系，支持各种功能扩展和业务需求。    </p> 
<p><img alt height="357" src="https://oscimg.oschina.net/oscnet/up-0c0dca9cc176e796d1c7edb2c9f175af1c9.png" width="700" referrerpolicy="no-referrer"></p> 
<p><span style="color:#3498db"><strong>Fes.js 架构</strong></span></p> 
<p>Fes.js 把大家常用的技术栈封装成一个个插件进行整理，收敛到一起，让大家只用 Fes.js 就可以完成 80% 的日常工作。</p> 
<p>支持插件和插件集，通过这张图应该很好理解到他们的关系，通过插件集我们把插件收敛依赖然后支持不同的业务类型。</p> 
<p><img alt height="533" src="https://oscimg.oschina.net/oscnet/up-da0801d51e0a69b9b3ebb30d826bc744c2d.png" width="700" referrerpolicy="no-referrer"></p> 
<p><span style="color:#021eaa"><strong><span style="color:#021eaa">Fes.js 2.0 的特点</span></strong></span></p> 
<ul> 
 <li> <h2><strong>快速 Fast</strong></h2> </li> 
</ul> 
<p>内置了路由、开发、构建等，并且提供测试、布局、权限、国际化、状态管理、API 请求、数据字典、SvgIcon 等插件，可以满足大部分日常开发需求。 </p> 
<ul> 
 <li> <h3><strong>简单 Easy</strong></h3> </li> 
</ul> 
<p>基于 Vue.js 3.0，上手简单。贯彻“约定优于配置”思想，设计插件上尽可能用约定替代配置，同时提供统一的插件配置入口，简单简洁又不失灵活。提供一致性的 API 入口，一致化的体验，学习起来更轻松。</p> 
<ul> 
 <li> <h3><strong>健壮 Strong</strong></h3> </li> 
</ul> 
<p>只需要关心页面内容，减少写 BUG 的机会！提供单元测试、覆盖测试能力保障项目质量。</p> 
<ul> 
 <li> <h3><strong>可扩展</strong></h3> </li> 
</ul> 
<p>借鉴 Umi 实现了完整的生命周期和插件化机制，插件可以管理项目的编译时和运行时，能力均可以通过插件封装进来，在 Fes.js 中协调有序的运行。</p> 
<ul> 
 <li> <h3><strong>面向未来</strong></h3> </li> 
</ul> 
<p>在满足需求的同时，我们也不会停止对新技术的探索。已使用 Vue3.0 来提升应用性能，已使用 webpack 5 提升构建性能和实现微服务，未来会探索vite等新技术。</p> 
<ul> 
 <li> <h3><strong>令人愉悦</strong></h3> </li> 
</ul> 
<p>我们的主要重点是开发人员体验。我们喜欢 Fes.js，并且会不断改进框架，所以您也喜欢它！期待有吸引力的解决方案，描述性的错误消息，强大的默认值和详细的文档。如果有问题或疑问，我们有用的社区将为您提供帮助。</p> 
<h1><strong><span style="color:#021eaa">快速上手</span></strong></h1> 
<p>基础配置：要有 10.13 或以上版本的 Node.js， 管理 npm 依赖推荐使用 yarn。</p> 
<p>使用 <span style="background-color:rgba(0, 0, 0, 0.03)">yarn</span>：</p> 
<p><code># 创建模板</code><code>yarn create @fesjs/fes-app myapp</code><br> <code># 安装依赖</code><code>yarn </code><br> <code># 运行</code><code>yarn de</code></p> 
<p>使用 <span style="background-color:rgba(0, 0, 0, 0.03)">npm</span>：</p> 
<pre><code># 创建模板</code><code>npx @fesjs/create-fes-app myapp</code>
<code># 安装依赖</code><code>npm install </code>
<code># 运行</code><code>npm run dev</code></pre> 
<p><strong><span style="color:#021eaa">写在最后</span></strong></p> 
<p>使用过程中，如果遇到困难，可到文档下查看解决方案；同时社区鼓励所有同学通过 Github 交流反馈，第一时间提交 issue。Fes.js 正在迅速发展中， 期待大家来一起玩耍！</p> 
<ul> 
 <li> <p>Github Issue</p> <p>https://github.com/WeBankFinTech/fes.js/issues</p> </li> 
 <li> <p>Github repo</p> <p>https://github.com/WeBankFinTech/fes.js/tree/vue3</p> </li> 
 <li> <p>使用文档</p> <p>https://winixt.gitee.io/fesjs/zh/</p> </li> 
 <li> <p>共建指南</p> <p>https://winixt.gitee.io/fesjs/zh/guide/contributing.html</p> </li> 
 <li> <p>项目助手</p> <p>geniusWanc</p> </li> 
</ul>
                                        </div>
                                      
</div>
            