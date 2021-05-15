
---
title: 'Vue源码笔记——全局API'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4636'
author: 掘金
comments: false
date: Fri, 14 May 2021 22:59:26 GMT
thumbnail: 'https://picsum.photos/400/300?random=4636'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">vue.use(options)</h2>
<ol>
<li>vue.use(options)注册一个第三方插件,option为对象则调用函数的install方法，为函数则直接执行该函数。</li>
<li>进行插件缓存，保证只注册一次</li>
<li>vue.use使用splice把Vue放到了参数数组第一位。install(Vue,...args)&#123;&#125;</li>
</ol>
<h2 data-id="heading-1">vue.mixin(options)</h2>
<ol>
<li>在Vue的全局配置上合并options配置，（组件在生成VNode时会将该全局配置合并到自身配置上）</li>
</ol>
<ul>
<li>标准化options对象上的props、inject、derective选项格式</li>
<li>合并options上的extends和mixin到全局配置</li>
<li>合并options和全局配置</li>
</ul>
<h2 data-id="heading-2">vue.component(name,cmpt)</h2>
<ol>
<li>注册全局组件，本质是将组件配置注册到全局配置的components属性上（组件生成VNode时将全局的components合并到组件配置）</li>
</ol>
<h2 data-id="heading-3">vue.derective('my-derective',function)</h2>
<p>原理同vue.component(filter等类似)</p>
<h2 data-id="heading-4">vue.extend(options)</h2>
<p>通过Vue的构造器创建一个子类，options作为该子类默认全局配置（一大用处是内置公共配置，mixin也可以实现）</p>
<h2 data-id="heading-5">vue.nextTick(cb)</h2>
<ol>
<li>数据变更触发依赖通知更新，将负责更新的watcher放入watcher队列</li>
<li>将watcher放入callbacks数组</li>
<li>浏览器异步任务队列放入放入舒心callBacks数组的函数</li>
<li>Vue.nextTick后push到callBacks后</li>
<li>执行顺序flushCallback——》watcher.run——》更新dom——》nextTick的cb</li>
</ol></div>  
</div>
            