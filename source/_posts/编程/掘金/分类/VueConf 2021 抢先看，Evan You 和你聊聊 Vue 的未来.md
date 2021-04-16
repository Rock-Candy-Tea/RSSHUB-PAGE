
---
title: 'VueConf 2021 抢先看，Evan You 和你聊聊 Vue 的未来'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30c1f90d4e47486fbc1f3fd009be56f2~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 15 Apr 2021 17:16:57 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30c1f90d4e47486fbc1f3fd009be56f2~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30c1f90d4e47486fbc1f3fd009be56f2~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">近况</h2>
<p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad45fbd1984c4ac9b32c080b6976f38c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><strong>158 万</strong>周活跃用户（通过 devtools 插件来统计），<strong>940 万</strong>的月下载量。</p>
<h2 data-id="heading-1">对比去年</h2>
<p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b29de515665c4bd7bbc7c4ef6244588c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>Devtools：110 万 -> 158 万（+43.6%）
NPM：620 万 -> 940 万（+51.6%）</p>
<h2 data-id="heading-2">Vue 3.0 One Piece</h2>
<p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fd121c5a6ea342909dfe7a2b91cfd734~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ab6662ba5e6465cbf7552b32f31e581~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>自那之后，Vue3 逐渐趋于稳定，继续探索用户体验。</p>
<h2 data-id="heading-3">Vue Router 4.0</h2>
<p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ba7a923f7214641a71f1e3a9293e4b1~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>已经稳定。</p>
<h2 data-id="heading-4">Vuex 4.0</h2>
<p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f5b2417d35d496a831e710a1dfc5b87~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>已经稳定。</p>
<h2 data-id="heading-5">生态</h2>
<p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d7c0e4ebe7348de825a6854b95ec0eb~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>慢慢赶上了！</p>
<ul>
<li>Nuxt 3</li>
<li>Vuetify</li>
<li>Quasar</li>
<li>Element Plus</li>
<li>Ant Design Vue</li>
</ul>
<h2 data-id="heading-6">用户体验</h2>
<p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3cbb6916f0c54efd97bbbd4e80445fa9~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>持续探索中：</p>
<ul>
<li>新的构建工具</li>
<li>更棒的语法</li>
<li>IDE/TS 支持</li>
</ul>
<h2 data-id="heading-7">构建工具</h2>
<p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c4c03cae64a4c1c9000f916faaa7f3f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>Vite，不用说了，今年的明星项目。</p>
<ul>
<li>和 Vue-CLI 更加相似的体验</li>
<li>基于 ESM 的 HMR 热更新</li>
<li>ESBuild 提供依赖预构建</li>
<li>Rollup 兼容的插件接口</li>
<li>内置 SSR 支持</li>
<li>更多更多……</li>
</ul>
<p>可以扩展阅读笔者之前写的<a href="https://juejin.cn/post/6932367804108800007" target="_blank">浅谈 Vite 2.0 原理，依赖预编译，插件机制是如何兼容 Rollup 的？</a></p>
<p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cb4ccadb609c4e288260e2d421f2fcf3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>Vite 还是 Vue-CLI？</p>
<ul>
<li>短期内会共存</li>
<li>长期会融合：Vite 的速度 + Vue-CLI 的全面度支持</li>
</ul>
<h2 data-id="heading-8">测试</h2>
<p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f05fcb549ef34c548972d9a81b7f8994~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>Cypress 新版组件测试</li>
<li>@web/test-runner</li>
<li>Jest 集成进行中</li>
</ul>
<p>看了下 <code>@web/test-runner</code> 的简介，非常全面的测试解决方案：</p>
<p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/521594eacb984baca4b27805595f9692~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">VitePress</h2>
<p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ff0a0f18014463594239786a3e70e5f~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>基于 Vue3 + Vite 的静态站点生成器。</p>
<p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9b275e536fd04e8f9e46eb976614e350~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>它的独特之处在于：</p>
<ul>
<li>利用 SPA 的开发体验来定制用户主题</li>
<li>在 Markdown 里自由加入动态组件</li>
<li>自动消除静态内容的“双重负载”</li>
</ul>
<p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73e1db85ef5947069163c7da7f8280d1~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>利用 VitePress 这个平台，探索未来 SSR/SSG 优化（Eat Your Own Dog Food）</p>
<ul>
<li>更积极的消除静态内容（甚至是主题组件）</li>
<li>更高效的构建</li>
<li>按需构建 + 边缘缓存</li>
</ul>
<h2 data-id="heading-10">新的开发体验</h2>
<p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff8bb38d4e484dbb82bffcac488f6eeb~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>利用编译器做更多事情：</p>
<ul>
<li><code>script setup</code></li>
<li><code>style</code> CSS 变量注入</li>
</ul>
<h3 data-id="heading-11">script setup</h3>
<p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d7fb69c5713c4220a902af73796b05be~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e78ea9ba4db42778eb072ef4ccbbcf4~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://github.com/vuejs/rfcs/blob/script-setup-2/active-rfcs/0000-script-setup.md" target="_blank" rel="nofollow noopener noreferrer">RFC 地址</a></li>
<li>在单文件组建中提供更符合用户体验的 Composition API</li>
<li>提高运行时性能</li>
</ul>
<h3 data-id="heading-12">style 变量注入</h3>
<p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/dde0f14148584e75932a5cf731c0ec61~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li><a href="https://github.com/vuejs/rfcs/blob/style-vars-2/active-rfcs/0000-sfc-style-variables.md" target="_blank" rel="nofollow noopener noreferrer">RFC 地址</a></li>
<li>利用 <code>v-bind()</code> 在单文件组件的 <code>style</code> 中注入 JS 状态驱动的 CSS 变量</li>
<li>CSS-in-JS 的好处尽享，但避免了它的心智负担。</li>
</ul>
<h2 data-id="heading-13">更好的 IDE/TS 支持</h2>
<p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b36a809a5a5f468f868d5357a06ccba8~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>多个探索中的项目</p>
<ul>
<li>Vetur</li>
<li>VueDX</li>
<li>Volar</li>
</ul>
<p>获得了：</p>
<ul>
<li>类型检查，语法提示和 SFC templates 的自动重构</li>
</ul>
<p>接下来：</p>
<ul>
<li><strong>把这些努力整合成更推荐的链路</strong></li>
<li>提供 CLI 工具来利用 TS 校验 SFC</li>
</ul>
<p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bc0663a52eff44ef8d2b79604b7eef3c~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>计划：</p>
<ul>
<li>基于 Volar 的<strong>新的官方 VSCode 插件</strong>，从 Vetur 和 VueDX 上汲取很多灵感。</li>
<li>通过内部设计来支持其他编辑器，通过 LSP（Language Service Protocol）</li>
</ul>
<h2 data-id="heading-14">未来</h2>
<p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5b7f71d0cd29444f8e5877761ea46e9e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>我们在 Vue3 中放弃了 IE11。</p>
<ul>
<li><a href="https://github.com/vuejs/rfcs/blob/ie11/active-rfcs/0000-vue3-ie11-support.md" target="_blank" rel="nofollow noopener noreferrer">RFC</a></li>
<li><a href="https://github.com/vuejs/rfcs/discussions/296" target="_blank" rel="nofollow noopener noreferrer">讨论</a></li>
</ul>
<p>笔者对这个 RFC 也进行了翻译：</p>
<p><a href="https://mp.weixin.qq.com/s?__biz=MzI3NTM5NDgzOA==&mid=2247495151&idx=1&sn=981920c2345fb3a70097b2a8dfa5ba66&chksm=eb07d596dc705c80b9db1bf62b0cc614b4f4012087e994ad178d5d91cfc3b9ad16f5c5ae72f0&token=1932513687&lang=zh_CN#rd" target="_blank" rel="nofollow noopener noreferrer">Vue3 考虑彻底放弃 IE 浏览器</a></p>
<p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6266282de18b49b6b15c51338d09d9cf~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>Vue 2.7 会成为坚持留守 IE11 人群的选择，它会提供更多的 Vue3 特性和 TS 支持。（估计在 2021 第三季度）</p>
<p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/83c03673c6be4aa2b61338241b0f0714~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>Vue3 的集成构建也要来了！</p>
<ul>
<li>估计在<strong>四月末</strong></li>
<li>可单独配置来兼容 v2</li>
</ul>
<p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be6b3288db154640abff09e637983eb3~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/05f1a7b9388f42f0bcdc0329f902e995~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>Vue3 会在 2021 二季度末尾，变成新的默认版本！</p>
<ul>
<li>npm 的 lastest tag 会默认安装 Vue3</li>
<li>vuejs.org 官网会指向 Vue3 的文档</li>
</ul>
<p><img alt title="屏幕截图.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a7ce14e35eb46159b3326452721b2a5~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>感谢大家！</p>
<h2 data-id="heading-15">原推地址</h2>
<p><a href="https://twitter.com/youyuxi/status/1382373548317147147" target="_blank" rel="nofollow noopener noreferrer">twitter.com/youyuxi/sta…</a></p>
<h2 data-id="heading-16">感谢大家</h2>
<p>我是 ssh，目前就职于<a href="https://webinfra.org/bytedance/web-infra" target="_blank" rel="nofollow noopener noreferrer">字节跳动的 Web Infra 团队</a>，目前团队在北上广深杭都还缺人（尤其是北京）。</p>
<p>我组建了一个<a href="https://github.com/sl1673495/bytedance-apm-group/blob/main/README.md" target="_blank" rel="nofollow noopener noreferrer">氛围特别好的招聘社群</a>，大家在里面尽情的讨论面试相关的想法和问题，也欢迎你加入，随时投递简历给我，交朋友也欢迎。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            