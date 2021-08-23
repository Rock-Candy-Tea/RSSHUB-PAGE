
---
title: 'vue2 双向数据绑定和数据响应式'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8264'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 00:06:28 GMT
thumbnail: 'https://picsum.photos/400/300?random=8264'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第2天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h2 data-id="heading-0">前言:</h2>
<p>对于 vue 的双向数据绑定和数据响应式本人最近花了一些时间去深究，自认为算是理清了它们之间的关系和主要的实现原理</p>
<h2 data-id="heading-1">双向数据绑定和数据响应式</h2>
<p>双向数据绑定就是视图层或者数据层中的一方发生变化，相对应的另一层也会发生变化。数据响应式就是拦截数据的访问与更新，在其发生这些操作的时候可以让我们知晓。所以，数据响应式是用来服务双向数据绑定的。</p>
<h2 data-id="heading-2">数据响应式的思想基本原理</h2>
<h3 data-id="heading-3">思想</h3>
<p>我们都知道 vue2 通过 Object.defineProperty 来实现数据拦截，具体是实现方法就是在这个方法基础上在添加亿点点细节。
为了便于功能区分，先定义两个方法(observe、defineReactive)和一个类(Observer)。它们的功能分别是 observe 为最外层响应式方法，用于对要进行响应式的数据做简单过滤，对于基础类型的数据直接返回原值，对于引用类型的数据(如对象和数组)将其变为 Observer 实例；Observe 实例中通过定义对应处理对象和数组的方法，来管理数据的响应式进程；defineReactive 方法是最终进行数据拦截的地方，对传入的数据也进行响应式处理即调用 observe 方法，这样就形成了一个递归操作，但是这个递归不会死循环，应该在 observe 方法中对于基础类型的数据会直接返回原值。在这里进行拦截数据时，get 中就直接返回该值的数据，set 中就将传入的新值赋值给该数据项，当然此处做一下数据判断，看新值是否和原值一样，如果一样的话就不进行赋值操作。</p>
<h3 data-id="heading-4">对象和数组处理的差异</h3>
<p>以上的流程对于对象数据是完全OK的，但是对于数组的话就会有问题，因为对于对象数据，其数据变化主要为值的变化，基本上都是通过赋值操作完成，但是对于数组，其除了通过赋值操作实现数组项的数据变化外，还可以通过方法实现对数组数据的变化，故需要对数组做一些特定的操作即来拦截数组的这些方法。此时就需要一个管理这些数组操作方法的单一文件 array.js 和一个定义一个对象属性的方法 def。在 array.js 中主要拦截的数组方法为 push、pop、shift、unshift、splice、reverse、sort，对于这些方法不需要完全重写，只用在使用它们的时候走一边我们自定义的操作实现数据拦截后在让它们按原来的操作继续即可。具体实现如下，先获取 Array.prototype，再通过 def 方法修改原型上的这些方法，对于push、unshift、splice因为能插入新项，故通过 observe 方法劫持(侦测)这些数据(插入新项)。最后在 Observer 类中通过  Object.setPrototypeOf 让数组的原型变为 array.js 中重写的数组原型即可。</p>
<h2 data-id="heading-5">数据双向绑定</h2>
<p>在 Vue 中通过 Dep 和 Watcher 实现依赖收集和更新通知。故此时需创建两个类 Dep 和 Watcher，Dep类专门帮助我们管理依赖，可以收集依赖，删除依赖，向依赖发送通知等；Watcher是一个中间的角色，数据发生变化时通知它，然后它再通知其他地方。核心思想为<strong>数据使用时收集依赖，数据更新时，通知更新</strong>。</p>
<h2 data-id="heading-6">参考</h2>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.bilibili.com%2Fvideo%2FBV1G54y1s7xV" target="_blank" rel="nofollow noopener noreferrer" title="https://www.bilibili.com/video/BV1G54y1s7xV" ref="nofollow noopener noreferrer">【尚硅谷】Vue源码解析之数据响应式原理</a><br>
<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmy.oschina.net%2Fu%2F4386652%2Fblog%2F4281447" target="_blank" rel="nofollow noopener noreferrer" title="https://my.oschina.net/u/4386652/blog/4281447" ref="nofollow noopener noreferrer">通俗易懂了解Vue双向绑定原理及实现</a></p>
<h2 data-id="heading-7">个人优化</h2>
<p>尚硅谷课程中，存在一定问题:<br>1,就是添加 watcher 时，会触发多次依赖收集，但并未做重复依赖处理，故我在 Dep 的 depend 方法上加上是否存在的判断，条件判断 Dep.target ---> Dep.target && !this.subs.includes(Dep.target);<br>2,我不理解为什么要单独对子元素进行额外依赖收集，我个人认为在对子元素进行响应式处理后就会为其进行依赖收集。<br>以上就是我整理的代码中会与尚硅谷课程有出入的地方，若有什么建议和意见，望提出！</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fbp12322%2Fvue2.0_observe_write" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/bp12322/vue2.0_observe_write" ref="nofollow noopener noreferrer">代码在这里</a>(注，my_data_reactive 这个文件夹中就是尚硅谷课程中的代码，该代码是他人整理，<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Fykang2020%2Fvue_learn%255D" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/ykang2020/vue_learn%5D" ref="nofollow noopener noreferrer">本代码的原仓库在这里</a>)</p></div>  
</div>
            