
---
title: 'Vue 中插槽slot的用法和应用场景'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/692ecedc80604d4ea8921e84bf0baf19~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 06 Jun 2021 02:15:23 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/692ecedc80604d4ea8921e84bf0baf19~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">什么是插槽？</h2>
<p>我们知道在Vue中 Child 组件的标签 的中间是不可以包着什么的 。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/692ecedc80604d4ea8921e84bf0baf19~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可是往往在很多时候我们在使用组件的时候总想在组件间外面自定义一些标签，vue新增了一种插槽机制，叫做作用域插槽。要求的版本是2.1.0+；</p>
<p>插槽，其实就相当于占位符。它在组件中给你的HTML模板占了一个位置，让你来传入一些东西。插槽又分为 匿名插槽、具名插槽、作用域插槽。</p>
<p>在 2.6.0 中，我们为具名插槽和作用域插槽引入了一个新的统一的语法 (即 <code>v-slot</code> 指令)。它取代了 <code>slot</code> 和 <code>slot-scope</code></p>
<h2 data-id="heading-1">匿名插槽</h2>
<p>匿名插槽，我们也可以叫它单个插槽或者默认插槽。和具名插槽相对，它是不需要设置 name 属性的，它隐藏的name属性为default。</p>
<p>father.vue</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b5551cd66a641a0b820a19b64843bd4~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>child.vue</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/86bfb664e726408795fea99b1b31f94c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>匿名插槽，name的属性对应的是 default 也可以不写就是默认的意思啦；</p>
<p>在使用的时候还有一个问题要注意的 如果是有2个以上的匿名插槽是会child标签里面的内容全部都替换到每个slot；</p>
<h2 data-id="heading-2">具名插槽 （vue2.6.0+被废弃的slot='name'）</h2>
<p>顾名思义就是slot 是带有name的 ，定义：  或者使用简单缩写的定义 #header 使用：要用一个 template标签包裹</p>
<p>father.vue</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6b958f0c39ba49199f1ca07a40acfab0~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>child.vue</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6f9351d528ba46fab189c25c72ec4d2e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这里说一下多个具名插槽的使用 多个具名插槽，插槽的位置不是使用插槽的位置而定的，是在定义的时候的位置来替换的</p>
<p>father.vue</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3170af0fc9734742ba7e267bd8dc5a7d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>child.vue</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87ea2bab1e924d7cb07d930ea84d8237~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">作用域插槽</h2>
<p>就是用来传递数据的插槽</p>
<p>当你想在一个插槽中使用数据时，要注意一个问题作用域的问题，Vue 官方文档中说了父级模板里的所有内容都是在父级作用域中编译的；子模板里的所有内容都是在子作用域中编译的;</p>
<p>为了让 子组件中的数据 在父级的插槽 内容中可用我们可以将 数据 作为 元素的一个特性绑定上去： v-bind:text="text"</p>
<p>注意：</p>
<p>匿名的作用域插槽和具名的作用域插槽 区别在v-slot:defult="接受的名称"(defult(匿名的可以不写，具名的相反要写的是对应的name))</p>
<p>v-solt可以解构接收 解构接收的字段要和传的字段一样才可以 例如 :one 对应 v-slot="&#123;one&#125;"</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/673251ec449244c9b117815e942def8d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>效果图</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/91f07516db4a4831b28a019275172349~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            