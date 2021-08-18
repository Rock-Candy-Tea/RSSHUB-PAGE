
---
title: 'vue2响应式原理之dep和watcher直接的关系'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c858df65689a499281ed08d18b37979a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 17 Aug 2021 01:30:18 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c858df65689a499281ed08d18b37979a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">因为本人学习前端时间有限，仅有一年多时间，如果存在理解问题，请各位大佬不吝啬赐教</h2>
<h3 data-id="heading-1">关于defineReactive等使用细节需要自行了解</h3>
<h3 data-id="heading-2">一些关键知识点</h3>
<ul>
<li>
<p>$mount时 会 new Watcher 把组件的 updateComponent 方法传给watcher 作为getter</p>
</li>
<li>
<p>在watcher的get中通过pushTarget 把当前watcher赋值给Dep.target</p>
</li>
<li>
<p>Dep的作用是调度中心/订阅器，在defineReactive 为每一个属性都实例话了一个Dep, 对用到该属性的Watcher进行管理（getter中收集，setter中通知）</p>
</li>
<li>
<p>Watcher是订阅者/观察者</p>
</li>
<li>
<p>数据的Dep的subs数组存放这个数据所绑定的观察者对象，观察者对象的deps数组中存放着与这个观察者有关的数据Dep。所以数据的Dep与Watcher其实是多对多关系</p>
</li>
<li>
<p>$watch和computed观察者是在created生命钩子函数前就创建完毕并且绑定的，而render观察者是在mounted之前创建并绑定的，所以同一个组件中，render观察者的id会大于其他观察者（id是在后面执行队列里面升序排序的时候的依据）。 换句话说，在同一个组件的观察者中，当数据发生改变的时候，渲染函数观察者一定是最后执行的。 这个很好理解，其他观察者中难免会对数据进行修改，如果渲染函数观察者先执行了，然后其他观察者对数据进行改变的话，那么没办法将数据准确呈现在页面上，导致数据不一致性。</p>
</li>
<li>
<p>defineReactive --》 const dep = new Dep() --> getter中 --> dep.append() --> Dep.target.addDep(this) 这个this 就是当前dep实例 --> Dep.target是一个watcher watcher.addDep 会把当前watcher加入到 dep实例中。</p>
</li>
</ul>
<h3 data-id="heading-3">流程图</h3>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c858df65689a499281ed08d18b37979a~tplv-k3u1fbpfcp-watermark.image" alt="render时 dep和watcher的关系.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            