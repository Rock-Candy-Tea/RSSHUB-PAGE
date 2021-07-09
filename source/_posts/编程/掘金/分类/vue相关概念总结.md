
---
title: 'vue相关概念总结'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f5f71e2406d41f7a2ae5e74decdb8cc~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 08 Jul 2021 23:26:29 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f5f71e2406d41f7a2ae5e74decdb8cc~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h4 data-id="heading-0">vue & react 概念</h4>
<ul>
<li><code>Vue</code>是一套用于构建用户界面的渐进式框架。</li>
<li><code>React</code>用于构建用户界面的 <code>JavaScript</code> 库。</li>
</ul>
<h4 data-id="heading-1">vue 概念深入 -- 渐进式框架的理解</h4>
<blockquote>
<p>Vue是一套用于构建用户界面的渐进式框架，Vue 被设计为可以自底向上逐层应用，Vue的核心是只关注视图层，不仅易于上手，还便于与第三方库或既有项目整合。</p>
</blockquote>
<p><strong>渐进式框架: 提供足够的选择，并且没有很多强制性的要求</strong></p>
<p>渐进也可以理解为一步一步的意思，大概意思就是使用Vue的时候，并不需要把整个框架的所有东西都用上，可以根据实际情况选择你需要的部分。如下图：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f5f71e2406d41f7a2ae5e74decdb8cc~tplv-k3u1fbpfcp-watermark.image" alt="Pasted Graphic 1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>声明式渲染和组件系统是Vue的核心库所包含内容，</li>
<li>而客户端路由、状态管理、构建工具都有专门解决方案。</li>
<li>这些解决方案相互独立，你可以在核心的基础上任意选用其他的部件，不一定要全部整合在一起。</li>
<li>Vue的使用没有很多强制性的要求,不像Angular那样，要使用Angular，还必须得使用它的模块机制、必须使用它的依赖注入、 必须使用它的特殊形式定义组件（这一点每个视图框架都有，Vue也难以避免）</li>
</ul>
<p><strong>自底向上逐层应用</strong></p>
<ul>
<li>由基层开始做起，把基础的东西写好，再逐层往上添加效果和功能。</li>
</ul>
<h4 data-id="heading-2">vue 概念深入 -- 命令式 & 声明式</h4>
<ul>
<li>命令式：一步一步告诉程序如何去做，能否达成结果取决于开发者的设计。</li>
<li>声明式：只告诉程序想要什么结果，如何达成由程序保证，开发者不用关心。</li>
</ul>
<h4 data-id="heading-3">vue3.0新特性</h4>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0f1e1cad0204814b868e6f5edfae906~tplv-k3u1fbpfcp-watermark.image" alt="vue3.0新特性.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">升级vue3.0的好处</h4>
<ul>
<li>vue2.x:一个功能反复跳转问题</li>
<li>vue2.x解决方案Mixin:
<ul>
<li>命名冲突问题</li>
<li>不清楚暴露出来的变量的作用</li>
<li>逻辑重用到其他 component 经常遇到问题</li>
</ul>
</li>
<li>vue3.x-<code>Composition API</code>:按照逻辑分割，增加代码可读性和可维护性</li>
</ul>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2911413852314078b52b80d00eec6f6d~tplv-k3u1fbpfcp-watermark.image" alt="vue3.x-compositionAPI.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-5">vue3.x-<code>Composition API</code></h4>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/182501b26cc04737ba6399419e6e66d1~tplv-k3u1fbpfcp-watermark.image" alt="vue3.x-compositionAPI2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-6">vue3.x-<code>setup</code></h4>
<ul>
<li>在 <code>beforeCreate</code> 之前执行.</li>
<li><code>setup(props, context)</code>:
<ul>
<li><code>props</code>: 组件传入的属性</li>
<li><code>context</code>: <code>&#123;attrs,slot,emit&#125;</code></li>
</ul>
</li>
</ul>
<h4 data-id="heading-7">Vue3.x - 生命周期图示</h4>
<ul>
<li>新增了用于调试的钩子函数<code>onRenderTriggered</code>和<code>onRenderTricked</code>
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f702432a2a04ad681a208d4cd8ce637~tplv-k3u1fbpfcp-watermark.image" alt="lifecycle.png" loading="lazy" referrerpolicy="no-referrer"></li>
</ul>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/004b4f8734ad48b78740207ade138a07~tplv-k3u1fbpfcp-watermark.image" alt="life.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            