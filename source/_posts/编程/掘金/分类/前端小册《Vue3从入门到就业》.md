
---
title: '前端小册《Vue3从入门到就业》'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8008'
author: 掘金
comments: false
date: Thu, 08 Sep 2022 20:04:25 GMT
thumbnail: 'https://picsum.photos/400/300?random=8008'
---

<div>   
<div class="markdown-body cache"><style>@charset "UTF-8";.markdown-body&#123;position:relative;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;color:#282d36&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px;color:#2f845e&#125;.markdown-body h2&#123;font-size:22px;display:inline-block;font-weight:700;background:#2f845e;color:#fff;padding:6px 8px 0 0;border-top-right-radius:6px;margin-right:2px;box-shadow:6px 3px 0 0 rgba(47,132,194,.2)&#125;.markdown-body h2:before&#123;content:" ";display:inline-block;width:8px&#125;.markdown-body h2:after&#123;content:" ";position:absolute;display:block;width:calc(100% - 32px);border-bottom:3px solid #2f845e&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%;box-shadow:6px 6px 6px #888&#125;.markdown-body hr&#123;border:none;border-top:1px solid rgba(66,185,131,.15);margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#262626;border:1px solid #2f845e;border-top:8px solid #2f845e;background:linear-gradient(180deg,rgba(66,185,131,.1),transparent)!important&#125;.markdown-body pre>code.language-awesome_error&#123;border:1px solid #ff4d4f;border-left-width:8px;font-size:14px;font-weight:700;padding:15px 10px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#ff4d4f;background:linear-gradient(90deg,#fff2f0,transparent)!important&#125;.markdown-body pre>code.language-awesome_error:before&#123;content:"!";position:absolute;top:50%;left:-9px;transform:translateY(-14px);background:#ff4d4f;color:#fff;border:2px solid #fff;display:flex;align-items:center;justify-content:center;width:22px;height:22px;border-radius:100%;font-weight:700;font-family:Dosis,Source Sans Pro,Helvetica Neue,Arial,sans-serif;font-size:16px&#125;.markdown-body pre>code.language-awesome_warn&#123;border:1px solid #ffc46f;border-left-width:8px;font-size:14px;font-weight:700;padding:15px 10px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#ffc46f;background:linear-gradient(90deg,#fffbe6,transparent)!important&#125;.markdown-body pre>code.language-awesome_warn:before&#123;content:"☂";position:absolute;top:50%;left:-9px;transform:translateY(-14px);background:#ffc46f;color:#fff;border:2px solid #fff;display:flex;align-items:center;justify-content:center;width:22px;height:22px;border-radius:100%;font-weight:700;font-family:Dosis,Source Sans Pro,Helvetica Neue,Arial,sans-serif;font-size:16px&#125;.markdown-body pre>code.language-awesome_success&#123;border:1px solid #52c41a;border-left-width:8px;font-size:14px;font-weight:700;padding:15px 10px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#52c41a;background:linear-gradient(90deg,#f6ffed,transparent)!important&#125;.markdown-body pre>code.language-awesome_success:before&#123;content:"★";position:absolute;top:50%;left:-9px;transform:translateY(-14px);background:#52c41a;color:#fff;border:2px solid #fff;display:flex;align-items:center;justify-content:center;width:22px;height:22px;border-radius:100%;font-weight:700;font-family:Dosis,Source Sans Pro,Helvetica Neue,Arial,sans-serif;font-size:16px&#125;.markdown-body pre>code.language-awesome_info&#123;border:1px solid #1890ff;border-left-width:8px;font-size:14px;font-weight:700;padding:15px 10px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#1890ff;background:linear-gradient(90deg,#e6f7ff,transparent)!important&#125;.markdown-body pre>code.language-awesome_info:before&#123;content:"i";position:absolute;top:50%;left:-9px;transform:translateY(-14px);background:#1890ff;color:#fff;border:2px solid #fff;display:flex;align-items:center;justify-content:center;width:22px;height:22px;border-radius:100%;font-weight:700;font-family:Dosis,Source Sans Pro,Helvetica Neue,Arial,sans-serif;font-size:16px&#125;.markdown-body strong&#123;background-color:inherit;color:#2f845e&#125;.markdown-body em&#123;background-color:inherit;color:#949415&#125;.markdown-body a&#123;text-decoration:none;color:#2f8e54;border-bottom:1px solid #3f9e64&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#3f9e64&#125;.markdown-body a[class^=footnote]&#123;margin-left:4px&#125;.markdown-body a:before&#123;content:"➤ "&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:100%;max-width:100%;overflow:auto;border:2px solid #2f8e54&#125;.markdown-body thead&#123;background:#2f8e54;color:#fff;text-align:left;font-weight:700&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(153,255,188,.1)&#125;.markdown-body td,.markdown-body th&#123;width:100%;padding:12px 7px;line-height:22px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;padding:1px 22px;margin:22px 0;border-left:6px solid #2f845e;background-color:rgba(66,185,131,.1);border-radius:2px&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li::marker,.markdown-body ul li::marker&#123;color:#2f845e&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px;color:#282d36&#125;.markdown-body del&#123;color:#2f845e&#125;.markdown-body input[type=checkbox]:checked:before&#123;content:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAA/klEQVQ4T72TMU7DQBBF318XdFR06egQEnAXRINEGlqgowoIR8AF4AZOZ4JEGq5AC5EixBU4A55BNrEVHAcSBTHlaubt37/zxZKlcn7n6mDPXJvz8IJ89HzWu8t7C8D2dfsY52ae4apHnLx0ktsCsHXZjiUuFgG40x2eJ/H/AhztB+zDUTpLwWj8jGkzxSHiHaMPrDQC8sMoilKzLAUqiKQjmb+ZuAdW80tmelCHODoNgSfP7AFprTTaRTzsJN1GEyuIZ7uW6TEEHwCtyV/6EVBKJHhfzgC0Xv/iXwEFBF4FG0378bd7sPQq5xK/hSnk6sdlX3mZrKkwLZKBeu8n9XuWEUE7X+YAAAAASUVORK5CYII=);position:relative;top:-1px;left:-1px&#125;.markdown-body .math .katex&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:22px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">一.  作者简介</h1>
<blockquote>
<p>👨‍💻 姓名：黄勇超</p>
<p>💻 职位： 现任国内某独角兽公司前端开发工程师，曾任「 前端开发组组长 」以及「 技术部门主管 」</p>
<p>💼 身份： 「 Panda Development Team 」 创始人，「 广州某某科技有限公司 」合伙人</p>
<p>📜 宣言：所有框架都有可能会过时，但是框架沉淀下来的思想会继续指导着我们的前端开发</p>
<blockquote>
</blockquote>
<p>擅长前端所有主流框架，拥有工业、教育、电商、信息、门户等多端多系统项目交付经验</p>
</blockquote>
<p>🔸  从接触前端开始，每一步都举步维艰，每一行代码都在寻找最优的标准写法</p>
<p>🔹  从接触前端以后，你就应该懂得，<strong>学习就应该是一辈子的事情</strong> 📝</p>
<hr>
<h1 data-id="heading-1">二.  为什么要写小册</h1>
<h3 data-id="heading-2">🕰️ 时代潮流</h3>
<p>🕛 从 <strong>Web 1.0</strong> 时代的静态页面</p>
<p>🕜 到随着 <strong>Web 2.0</strong> 概念的普及和 <strong>W3C</strong> 组织的推广，各网站开始重构</p>
<p>🕒 再到 设计模式 | 前端工程化 | 各种编译原理</p>
<p>🕥 对开发者提出的要求越来越高，要全面地拥抱计算机知识体系</p>
<br>
<p>为了防止你的顿悟仅仅相当于别人的基础水平，我们需要体系化和系统化地探索前端开发</p>
<p>这就意味着，我们学习的不仅仅是表面的增删改查，而是底层的工程化、框架，还有海底的计算机知识体系</p>
<hr>
<h3 data-id="heading-3">📝 编写初衷</h3>
<br>
对于大部分开发者而言，需要学习一门新框架新语言，简直过于痛楚
<p>为什么？  以官网、菜鸟教程等学习网站为例</p>
<p>设计者总是迫不及待地想把所有概念一下子传输给用户，对于一个刚入门的开发者而言显然是非常不友好的⚠️</p>
<p><strong>💬 圈起来，这里要考！！！所有的开发者皆要本着为服务用户，传达便捷的理念去进行开发产品</strong></p>
<br>
<p>而对于长时间不断学习且走过许多弯路的我来说，阶段目标就是在不断提升自我的同时，也希望把所总结出来的开发经验和把一些开发语法和逻辑通过 “大白话” 的形式分享出来，去帮助更多实习生，入门者，行业人士去快速高效地学习一门新的技术</p>
<p><strong>💬 因为分享能够自我精进，将有用的知识分享给他人，别人也会因为你的分享而成长，同时埋下分享的种子</strong></p>
<p>只有技术经验的分享与交流，才能使行业进步以及个人进步</p>
<blockquote>
<p>「 涓涓细流汇成海，点点纤尘积就山 」</p>
</blockquote>
<hr>
<h3 data-id="heading-4">👾 为什么要使用 Vue3</h3>
<br>

























<table><thead><tr><th>例子</th><th>框架名称</th></tr></thead><tbody><tr><td>注重数据不可变以及虚拟 DOM</td><td>React</td></tr><tr><td>运行都非常轻量级，侧重在于编译时的优化</td><td>Svelte</td></tr><tr><td>在抽象这个维度又走向一个极致，生来就是为了复杂项目</td><td>Angular</td></tr><tr><td>在每个维度之间，做了非常好的权衡和取舍，兼顾响应式、虚拟 DOM和编译优化</td><td>Vue</td></tr></tbody></table>
<p>目前前端流行的框架中，对开发者的要求各有不同 ； 而相比之下，<strong>Vue</strong> 对于开发者提出的要求就很少</p>
<p>而 <strong>Vue3</strong> 作为 <strong>Vue</strong> 框架最新的版本，也带来了很多优秀的设计</p>
<p>比如 <code>Composition 组合 API</code>  、 基于 <code>Proxy</code> 的响应式系统、自定义渲染器等</p>
<p>这些设计可以让我们以很轻松的方式，从最熟悉的框架逐渐深入底层</p>
<hr>
<h3 data-id="heading-5">📡 核心内容</h3>
<p>🚌 本小册的学习路线：</p>
<p><strong>语法介绍</strong></p>
<p>✏️ 课程会通过⼀个实例开发，讲解核⼼内容和 API 实现，为后面的实战和后续实际场景开发打下基础</p>
<p><strong>项目搭建</strong></p>
<p>✏️ 一步步搭建一个完整的 Vue 3 项目系统，讲解标准化目录的使用</p>
<p><strong>全家桶实战</strong></p>
<p>✏️ 包括 <code>Vue-cli</code>、<code>Vite</code>、<code>Vuex</code>、<code>Vue-router</code>、<code>Devtools</code> 等生态库，以及实战开发中需要的库</p>
<p><strong>进阶开发</strong></p>
<p>✏️  将会讲解如何动态控制页面路由、如何做性能优化、如何开发复杂性的节点渲染页面等</p>
<p><strong>项目组件化</strong></p>
<p>✏️ 将会讲解如何设计一个通用的组件库，包括插槽，如何发布打包等；帮你实现和发布一个自己的组件库</p>
<p><strong>提升开发质量</strong></p>
<p>✏️ 单元测试，提高你的开发质量，减少 BUG 的产生</p>
<p><strong>原理分析</strong></p>
<p>✏️ 为了避免把源码做成⼋股⽂，首先会带你回顾 Vue 的发展历程，让你了解为什么 Vue 是现在这个样⼦，中间还会参考 React 和 Svelte 的设计和及其原理</p>
<p>了解完设计思想和思路后，我们逐个拆分 Vue 的源码包，最终实现⼀个 mini 版的 Vue</p>
<hr>
<h1 data-id="heading-6">三.  拟定小册目录</h1>
<ol>
<li>【课程前言】<em> </em> 关于这门课你需要知道的</li>
<li>【初识框架】<em> </em> Vue3新特性详解</li>
<li>【了解类型】<em> </em>  TypeScript 类型的世界</li>
<li>【项目启动】<em> </em> 项目搭建</li>
<li>【吃全家桶】<em> </em> Vue3全家桶</li>
<li>【学习实战】<em> </em> Vue3全家桶实战</li>
<li>【组件实现】<em> </em> 实现组件库</li>
<li>【组件上传】<em> </em> 组件上传</li>
<li>【难度升级】<em> </em> 难度渲染实现</li>
<li>【表格开发】<em> </em> UI框架通用表格详解</li>
<li>【表单开发】<em> </em> UI框架通用表单详解</li>
<li>【提升质量】<em> </em> 单元测试</li>
<li>【扩展视野】<em> </em> 设计主题系统</li>
<li>【开源社区】<em> </em> 开源项目发布流程</li>
<li>【生态源码】<em> </em> 探讨框架运行原理</li>
<li>【课程总结】<em> </em> 实际开发场景中你要怎么快速融入</li>
</ol></div>  
</div>
            