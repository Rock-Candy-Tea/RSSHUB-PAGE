
---
title: '了解vue的computed  ｜  8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/feec3ce3281240128ad9914008cdbe85~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 01 Aug 2021 01:34:57 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/feec3ce3281240128ad9914008cdbe85~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">1.了解vue的计算属性computed</h1>
<h2 data-id="heading-1">1.为什么需要设计出计算属性computed</h2>
<p><strong>对于复杂的逻辑，如果直接写在模版内会使模版过重并且难以维护，</strong></p>
<p>下面有一个简单的例子，模版的渲染是根据数据a,b进行判断的</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/feec3ce3281240128ad9914008cdbe85~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-01 下午4.08.17.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>按钮点击前：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/54743356e9aa417f8387f213975d49c3~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-01 下午4.09.37.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>对比点击按钮使a = 0 不显示div</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46175e636d43428d9528794cbb99600a~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-01 下午4.09.44.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以看到使用计算属性和直接在模版内计算的结果是一样的，但是如果在初始化时直接求出结果则不会发生变化，说明计算属性会跟踪依赖的数据变化，从而重新计算。</p>
<h2 data-id="heading-2">2.computed是在哪一个生命周期内创建的</h2>
<p>computed的初始化都是在beforeCreated和created生命周期之间完成的</p>
<h2 data-id="heading-3">3.计算属性是基于响应式依赖进行缓存的，只有当依赖属性发生变化时才重新计算</h2>
<p>有人觉得使用methods和computed是一样的，而我们确实也可以使用methods达到同样的效果，那为什么还需要使用计算属性呢，我们来看下面的例子</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90e2a71e48c54138b7be6a154d054ea4~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-01 下午4.38.31.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>触发方法的结果：我们可以看到每一次执行方法时都会重新计算（这个例子举的不是很恰当，我们可以将自加看做或假设是一种复杂的算法）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a38510d3b6a24744a9465477fc0a9826~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-01 下午4.38.51.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>计算属性的结果：每一次返回都是不变的，说明了computed具有计算属性，我们也可以看成类似于记忆函数</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5455d1fbcd4452f9a05815d75a2633c~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-01 下午4.39.13.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">4.computed不支持异步，当computed中存在异步操作时无法监听数据的变化</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8ed8442f8f8947aab6fec0e623ec9581~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-01 下午5.04.20.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们可以看到即使3秒结束后也没有返回结果</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/62e7d32c1c2040e485ec3d17d228514d~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-01 下午5.04.29.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">5.computed属性中有get和set方法，如果属性的值是一个函数，则默认走get方法。若数据发生变化时，则执行set方法，此时使用对象定义computed</h2>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/394ed218904d4679a0c0454de1d0c836~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-01 下午5.12.02.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-6">3.computed的应用场景</h1>
<p>1.当需要多个值重新计算生成一个新值时使用计算属性，多对一的关系
2.当需要进行复杂运算并希望可以通过缓存减少运算次数，达到提高性能目的时可以使用计算属性</p>
<h1 data-id="heading-7">4.vue3 中当数组的长度没有发生变化时也可以监听数组了，不需要使用$set</h1>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5e7fc0e087ec4b019596ac558c2389c0~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-01 下午5.26.07.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b8ac284dd1b4a528d7ae37e1a393661~tplv-k3u1fbpfcp-watermark.image" alt="截屏2021-08-01 下午5.26.30.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            