
---
title: 'Fes.js for Vue3，简洁却不简单'
categories: 
 - 编程
 - segmentfault
 - 频道
headimg: 'https://segmentfault.com/img/remote/1460000039688153'
author: segmentfault
comments: false
date: 2021-03-23 20:17:33
thumbnail: 'https://segmentfault.com/img/remote/1460000039688153'
---

<div>   
<p>Fes.js 是一套优秀的中后台前端解决方案。提供初始项目，开发调试，模拟接口，编译打包的命令行工具。内置布局，权限，数据字典，状态管理，存储，API 等多个模块。以约定，配置化，组件化的设计思想，让用户只需关心使用组件构造页面内容。基于 Vue.js，上手简单。经过多个项目中打磨，趋于稳定。</p><p>1.0 上线后收到了社区小伙伴们的良好建议，在此谢谢支持 Fes.js 的你们，希望本次升级给大家带来更多的帮助，期待未来共同创造更多功能。</p><p>我们需要开发的大部分前端应用的业务比较类似，比如中后台应用大多都是工作台、增删改查、权限、图表等。所以在开发一个前端应用之前，除了环境准备工作，还需要处理这些基础的业务逻辑。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039688153" alt="图片" title="图片" referrerpolicy="no-referrer"></span></p><p>如果没有统一的规范或者框架，技术选型也要看开发人员的喜好，每个项目的准备工作都手动处理一遍，非常耗费时间。久而久之，当团队会出现多种技术栈，历史项目将越来越难维护。所以我们需要一套完整的解决方案，管理开发到部署整个流程，在问题发生前将其解决。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039688154" alt="图片" title="图片" referrerpolicy="no-referrer"></span></p><p><strong>Fes.js 2.0 做了哪些改进</strong></p><p>对于 1.0  本只支持 PC 应用、不易扩展等不足，我们在 2.0 版本重新设计了以插件机制为基础的可扩展架构。</p><p>重写了 90% 代码，Fes.js 2.0 以 <strong>Vue 3.0</strong> 和路由为基础，同时支持配置式路由和约定式路由，并以此进行功能扩展。匹配了覆盖编译时和运行时生命周期完善的插件体系，支持各种功能扩展和业务需求。 </p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039688155" alt="图片" title="图片" referrerpolicy="no-referrer"></span></p><p>Fes.js 架构</p><p>Fes.js 把大家常用的技术栈封装成一个个插件进行整理，收敛到一起，让大家只用 Fes.js 就可以完成 80% 的日常工作。</p><p>支持插件和插件集，通过这张图应该很好理解到他们的关系，通过插件集我们把插件收敛依赖然后支持不同的业务类型。</p><p><span class="img-wrap"><img class="lazy" src="https://segmentfault.com/img/remote/1460000039688156" alt="图片" title="图片" referrerpolicy="no-referrer"></span></p><p>插件和插件集</p><p><strong>Fes.js 2.0 的特点</strong></p><p>======================</p><ul><li><p><strong>快速 Fast</strong></p><hr></li></ul><p>内置了路由、开发、构建等，并且提供测试、布局、权限、国际化、状态管理、API 请求、数据字典、SvgIcon 等插件，可以满足大部分日常开发需求。</p><ul><li><p><strong>简单 Easy</strong></p></li></ul><p>基于 Vue.js 3.0，上手简单。贯彻“约定优于配置”思想，设计插件上尽可能用约定替代配置，同时提供统一的插件配置入口，简单简洁又不失灵活。提供一致性的 API 入口，一致化的体验，学习起来更轻松。</p><ul><li><p><strong>健壮 Strong</strong></p></li></ul><p>只需要关心页面内容，减少写 BUG 的机会！提供单元测试、覆盖测试能力保障项目质量。</p><ul><li><p><strong>可扩展</strong></p></li></ul><p>借鉴 Umi 实现了完整的生命周期和插件化机制，插件可以管理项目的编译时和运行时，能力均可以通过插件封装进来，在 Fes.js 中协调有序的运行。</p><ul><li><p><strong>面向未来</strong></p></li></ul><p>在满足需求的同时，我们也不会停止对新技术的探索。已使用 Vue3.0 来提升应用性能，已使用 webpack 5 提升构建性能和实现微服务，未来会探索vite等新技术。</p><ul><li><p><strong>令人愉悦</strong></p></li></ul><p>我们的主要重点是开发人员体验。我们喜欢 Fes.js，并且会不断改进框架，所以您也喜欢它！期待有吸引力的解决方案，描述性的错误消息，强大的默认值和详细的文档。如果有问题或疑问，我们有用的社区将为您提供帮助。</p><p><strong>快速上手</strong></p><p>基础配置：要有 10.13 或以上版本的 Node.js， 管理 npm 依赖推荐使用 yarn。</p><p>使用 yarn：</p><pre><code># 创建模板
yarn create 
# @fesjs/fes-app myapp``
# 安装依赖
yarn 
# 运行
yarn de </code></pre><p>使用 npm：</p><pre><code>#创建模板
npx @fesjs/create-fes-app myapp
# 安装依赖
npm install 
# 运行
npm run dev</code></pre><p><a href="https://mp.weixin.qq.com/s?__biz=MjM5NDk2OTEzOA==&mid=2247484215&idx=1&sn=80afe48939a0a7812fc8a25beba7da24&chksm=a6fee06a9189697c0f42edaf612fb3a98ee7f773224fb704020407d9eba4f8f6762bb151e3c5&mpshare=1&scene=1&srcid=03225dF8jbkQVOX0gwFUSFIa&sharer_sharetime=1616388830932&sharer_shareid=967fd85e1954a2fdc667dd2f3ac3fe9c&version=3.1.2.2211&platform=win#rd" rel="nofollow">演示操作文章视频</a></p><p><strong>写在最后</strong></p><p>============</p><p>使用过程中，如果遇到困难，可到文档下查看解决方案；同时社区鼓励所有同学通过 Github 交流反馈，第一时间提交 issue。Fes.js 正在迅速发展中， 期待大家来一起玩耍！</p><ul><li>Github Issue<p><a href="https://github.com/WeBankFinTech/fes.js/issues" rel="nofollow">https://github.com/WeBankFinT...</a></p></li><li>Github repo<p><a href="https://github.com/WeBankFinTech/fes.js/tree/vue3" rel="nofollow">https://github.com/WeBankFinT...</a></p></li><li>使用文档<p><a href="https://winixt.gitee.io/fesjs/zh/" rel="nofollow">https://winixt.gitee.io/fesjs...</a></p></li><li>共建指南<p><a href="https://winixt.gitee.io/fesjs/zh/guide/contributing.html" rel="nofollow">https://winixt.gitee.io/fesjs...</a></p></li><li>项目联络<p>geniusWanc</p></li></ul>  
</div>
            