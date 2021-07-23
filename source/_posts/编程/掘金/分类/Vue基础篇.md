
---
title: 'Vue基础篇'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7208359a3c1f41b7810980ac5f7a5163~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 04:38:26 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7208359a3c1f41b7810980ac5f7a5163~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">MVVM模式</h2>
<p>mvvm即Model-View-ViewModel，mvvm的设计原理是基于mvc的，所以说mvvm不算是一种创新，充其量是一种改造，这其中的ViewModel便是一个小小的创新；如下图所示：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7208359a3c1f41b7810980ac5f7a5163~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>以上图中可看出三者之间的关系；可以将ViewMode看作是Model和View的连接桥，View可以通过事件绑定Model，Model可以通过数据绑定View，通过ViewMode可以实现数据和视图的完全分离。</p>
<h2 data-id="heading-1">Vue生命周期</h2>
<p>beforeCreate
Created
beforemount
mounted
beforeUpdate
updated
beforeDestroy
destroyed</p>
<h2 data-id="heading-2">vue中常见的指令及作用</h2>
<p>v-text 只解析文本信息
v-html 可以解析超文本标签
v-if/v-else-if/v-else 与javaScript中的一样，用于判断。
v-show 通过控制元素的display css属性来控制元素的显示与隐藏
v-for 循环
v-on 绑定事件，可以用@符号来代替
v-bind 绑定元素的一个或者多个属性，用于动态更新html上元素的标签内容
v-slot 插槽
v-pre 跳过自己以及子元素的编译过程
v-model 数据的双向绑定
v-clock 解决页面闪烁问题
v-once 只渲染一次</p>
<h2 data-id="heading-3">vue中watch和computed区别</h2>
<p>computed：
1)有缓存机制
2)不能接受参数
3)不能与data中的属性重复
watch：
1)可以接受两个参数
2)监听时触发一个回调，并在回调中做一些处理
3)监听的书信必须存在
4)允许异步</p></div>  
</div>
            