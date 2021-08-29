
---
title: 'vue入门-第四章'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca55f0636b7d4f3abb03c4538a15d8db~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 28 Aug 2021 20:36:02 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca55f0636b7d4f3abb03c4538a15d8db~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><strong>这是我参与8月更文挑战的第29天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h1 data-id="heading-0">vue入门-第四章</h1>
<blockquote>
<p>下文主要记录vue的一些基础常用特性。</p>
</blockquote>
<h3 data-id="heading-1">1.指令</h3>
<blockquote>
<p>与jQuery手动操作dom的方式不同，vue采用指令进行双向数据绑定的方式，数据更新则dom更新</p>
</blockquote>
<blockquote>
</blockquote>
<p>常用指令入如下：</p>
<h4 data-id="heading-2">1.v-bind</h4>
<p>给dom元素属性赋值，可以是自定义属性或者原生属性 (<code>v-bind:属性=""</code> 可直接缩写成 <code>属性=""</code>)),例如：</p>
<p><code><div data="&#123;&#123;data&#125;&#125;"></div></code></p>
<h4 data-id="heading-3">2.v-on</h4>
<p>用于自定义原生事件；例如给button添加一个click事件（<code>v-on:事件名="表达式" 可缩写为 @事件名=“表达式”</code>）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca55f0636b7d4f3abb03c4538a15d8db~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0828e1661fca4aaf8b47e08342eac86d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">3.v-model</h4>
<p>双向数据绑定。使用频率最高的指令了。例如input</p>
<p><code><input v-model="inputVal"/></code></p>
<h4 data-id="heading-5">4.v-for</h4>
<p>循环指令。常用于页面数组数据的循环展示。</p>
<p>语法 v-for="item in list" （list 可以是对象或者数组）</p>
<h4 data-id="heading-6">5.v-if/v-else</h4>
<p>判断指令。与代码中的if/else类似，后跟可转换为布尔类型的表达式。用于显示或者隐藏dom。（else会自动匹配上一个if，多个判断时可采用v-else-if）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5a1b5af5181465b97b9c75b0803f419~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c448e8c582e34b16838fe3b48e898c27~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-7">6.v-show</h4>
<p>作用效果与v-if/else 类似。都是控制dom的展示与否。区别是v-if/else 表达式为false是不加载该部分dom，而v-show则是做css的display:block/none。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c160647fbdac400c9df20fce3259a433~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-8">2.生命周期</h3>
<blockquote>
<p>每一个vue的实例对象在被创建、初始化、编译、挂载、渲染-更新、卸载时的一系列过程叫做生命周期。具体如下：</p>
</blockquote>
<h5 data-id="heading-9">1.（创建前）</h5>

















































<table><thead><tr><th>生命周期</th><th>描述</th></tr></thead><tbody><tr><td>beforeCreate</td><td>创建前，在实例化之后，数据观测和事件配置之前</td></tr><tr><td>created</td><td>创建后，此时实例已创建完成但未挂载；数据观测和事件配置已完成，$el不可见</td></tr><tr><td>beforeMount</td><td>在挂载开始前调用</td></tr><tr><td>mounted</td><td>挂载完成。dom渲染成功</td></tr><tr><td>beforeUpdate</td><td>数据更新前调用</td></tr><tr><td>updated</td><td>数据更新，dom重新渲染</td></tr><tr><td>activated</td><td>keep-live组件激活时调用</td></tr><tr><td>deactivated</td><td>keep-live组件停用时调用</td></tr><tr><td>beforeDestroy</td><td>实例销毁前调用。此时实例仍然可用</td></tr><tr><td>destoryed</td><td>实例销毁后调用。vue所有指令、事件全部解绑、销毁</td></tr></tbody></table>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cc3c768bad2c404e8c974c82f16e8c76~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-10">3.监听器</h3>
<blockquote>
<p>通常我们会使用watch来监听data中的数据变化，然后触发事件进行处理。</p>
</blockquote>
<pre><code class="copyable">
watch:&#123;

//监听数组

dataList:function(newV,oldV)&#123;

console.log('newV:',newV,','oldV:',oldV)

&#125;

//监听对象

objInfo:&#123;

immediate:true,//是否立即触发回调

deep:true,//是否监听对象内部某一属性值的变化

handler(newV,oldV)&#123;

console.log('newV:',newV,','oldV:',oldV)

&#125;

&#125;

//如只监听对象中单一属性（键路径）

'objInfo.status':&#123;

handler(newV,oldV)&#123;

console.log('newV:',newV,','oldV:',oldV)

&#125;

&#125;

&#125;

<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            