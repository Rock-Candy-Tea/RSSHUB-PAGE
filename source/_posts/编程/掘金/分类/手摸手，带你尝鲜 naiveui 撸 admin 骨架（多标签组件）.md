
---
title: '手摸手，带你尝鲜 naiveui 撸 admin 骨架（多标签组件）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19f3516bc3624403b197427d93524011~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 14 Aug 2021 01:29:34 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19f3516bc3624403b197427d93524011~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>后台管理通常页面较多，试想一下，如果一个页面跳转另外一个页面，假如你操作的页面，有很多是相同的，只是功能点不同，那么你每次都得从左侧菜单找到他，点击跳转，体验交互不是那么优雅，为了解决这个问题，<strong>多标签页组件</strong>，就显得尤为重要了。</p>
<h1 data-id="heading-1">布局</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19f3516bc3624403b197427d93524011~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-2">解析</h1>
<p>1、实现布局</p>
<p>2、当标签数量超出屏幕的时候，左右需要展示箭头按钮，用于滚动内容</p>
<p>3、右侧固定一个快捷操作按钮</p>
<p>4、每个标签可关闭</p>
<p>5、给标签添加一个拖动效果</p>
<p>6、给标签添加右键展开操作菜单功能</p>
<p>7、自适应宽度，显示操作按钮</p>
<p>8、点击标签，可跳转到路由页面</p>
<p>9、暂列这些吧，其实还有很多可以实现的，一个体验好的组件，需要处理的可多了O(∩_∩)O哈哈~</p>
<h1 data-id="heading-3">实现布局</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c06066baf514da0903fb55cad8df52d~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上只是布局思路，删减了一些动态绑定class代码，如需完整代码，可查看<strong>github</strong>仓库</p>
<h1 data-id="heading-4">超出屏幕</h1>
<p>这里我们用到一个库，<strong>element-resize-detector，</strong> 安装 ****yarn add element-resize-detector</p>
<p><strong>核心代码</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ace0478ab20411ba6e62d9046fabaaa~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-5">固定快捷操作</h1>
<p><strong>模板实现</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be36b5e05eb64871b3138b48bd359f93~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>script代码</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71ca7303d6e34c4f864e08f23ae76a6b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-6">标签右键展开</h1>
<p><strong>模板代码</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f5626e701b0144c0b840409635e78475~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>script代码</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3eb3cd595bb946b389b0ea4f0532c80a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-7">拖动</h1>
<p>这里借助一款插件，<strong>vuedraggable</strong> 安装 ****yarn add vuedraggable</p>
<p><strong>核心代码</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db55ef8d47524c4bb9e1ddf3bd051f0a~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-8">标签跳转</h1>
<p>这里分析一下完整思路，标签是通过从 watch route.fullPath 然后 从route 中，组装一个简易tab结构，保存在vuex中，跳转代码如下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90abf0e4e566440e86df30aa6079de3c~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-9">标签持久化</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f76c2c91246348258cff700b48d5a578~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-10">最终效果</h1>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/49887cea7fec4412b7126c2d609f3fcc~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-11">完整源码</h1>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fjekip%2Fnaive-ui-admin%2Fblob%2Fmain%2Fsrc%2Flayout%2Fcomponents%2FTagsView%2Findex.vue" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/jekip/naive-ui-admin/blob/main/src/layout/components/TagsView/index.vue" ref="nofollow noopener noreferrer">github.com/jekip/naive…</a></p>
<p>顺手点个 <strong>Star</strong> 吧，谢谢~</p></div>  
</div>
            