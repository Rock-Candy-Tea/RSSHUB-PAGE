
---
title: 'vue3前端青铜到黄金王者 - 第8个入门v watch使用'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7866'
author: 掘金
comments: false
date: Sun, 22 Aug 2021 07:36:10 GMT
thumbnail: 'https://picsum.photos/400/300?random=7866'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第21天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h1 data-id="heading-0">什么是Watch</h1>
<p>watch 是 Vue.js 最强大的功能之一。</p>
<p>当关注的某个变量的值变化时，watch监听到并且执行，注册监听该变量的函数（比如更根据变化执行一些数据，消息更新等）</p>
<p>我们直接敲代码吧：</p>
<pre><code class="copyable"><!DOCTYPE html>

<html lang="en">

<head>

    <title>vue3青铜到黄金-丸子酱-vue-0n</title>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <script src="/vue3.1.5_vue.global.js"></script>

</head>

<body>

    <div id="wzApp">

<h3><a v-bind:href="url">点击访问->子酱@CSDN博客</a></h3>

<input  v-model="num1" /><br/>

<input v-model="num2" /><br/>

<div>&#123;&#123;num1 + num2&#125;&#125;</div>

    </div>

</body>

<script>

    const &#123; createApp,ref,watch &#125; = Vue

    const url = 'https://blog.csdn.net/qq_28008615'

    const num1 = ref("Hello")

    const num2 = ref("Vue3") 

    const app = &#123;

        setup() &#123;

            watch(num1, (newVal, oldVal)=>&#123; 

                console.log('change from ' + oldVal + ' to ' + newVal)

            &#125;)

            return &#123;

                url, num1, num2

            &#125;

        &#125;

    &#125;   

    createApp(app).mount('#wzApp')

</script>

</html>
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-1">重点说明</h1>
<h2 data-id="heading-2">监听多个参数执行不同的方法</h2>
<p>不过以上只是一些简单的例子，对于vue3中，watch可以监听多个源，并且执行不同的函数。</p>
<p>在vue3中同理也能实现相同的情景，通过多个watch来实现，但在vue2中，只能存在一个watch。</p>
<p>比如再添加多一个监听</p>
<pre><code class="copyable">
            watch(num2, (newVal, oldVal)=>&#123; 

                console.log('change from ' + oldVal + ' to ' + newVal)

            &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其他更多读者可以试试编写一些watch监听，vue3还是增强了不少。</p>
<h1 data-id="heading-3">总结</h1>
<p>watch 可以监控跟踪到不同变量值的变化来触发其他操作。</p>
<p>比如在做游戏网站装备售卖的时候，可以根据页面的一些状态变化。更换皮肤，提示各种消息。这样比较友好。</p>
<p>当然还能根据一个固定时间来提示活动信息（这个可以用定时器来修改一些变量，watch级联更新）</p>
<p>就写到这里</p>
<blockquote>
<p>我是丸子，每天学会一个小知识。<br>
一个前端开发<br>
希望多多支持鼓励，感谢</p>
</blockquote></div>  
</div>
            