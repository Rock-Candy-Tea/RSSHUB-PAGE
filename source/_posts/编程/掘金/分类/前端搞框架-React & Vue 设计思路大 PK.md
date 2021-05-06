
---
title: '前端搞框架-React & Vue 设计思路大 PK'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d3418bae55c4989be05826772085d97~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 05 May 2021 23:22:27 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d3418bae55c4989be05826772085d97~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>前端早早聊大会，成长的新起点，与掘金联合举办。 加微信 codingdreamer 进大会技术群，赢在新的起跑线。</p>
<hr>
<p>第二十五届|前端述职专场，晋升/述职/汇报/年终总结 - 前端每年都要过的关，5-9 全天直播，7 位讲师(蚂蚁/有赞/字节/创业公司等等)，<a href="https://www.huodongxing.com/go/tl25" target="_blank" rel="nofollow noopener noreferrer">点我上车👉 (报名地址)：</a></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0d3418bae55c4989be05826772085d97~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>关键词有：</p>
<ul>
<li>前端述职需要如何包装自己？</li>
<li>前端晋升为何拿不到好的结果？</li>
<li>前端晋升在工作中需要注重哪些产出？</li>
<li>前端有没有比较好的工作汇报方法论</li>
</ul>
<p><strong>所有往期都有全程录播，可以购买<a href="https://www.huodongxing.com/go/2021" target="_blank" rel="nofollow noopener noreferrer">年票</a>一次性解锁全部</strong></p>
<p><a href="https://zaotalk.huodongxing.com/" target="_blank" rel="nofollow noopener noreferrer">👉更多活动 </a></p>
<hr>
<h2 data-id="heading-0">正文如下</h2>
<blockquote>
<p>本文是第十七届 - 前端早早聊框架专场，也是早早聊第 122 场，来自开课吧 - 大圣 的分享的图文讲稿</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3f5815c42a634ccb8d6894fec0010de3~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">关于我</h2>
<p>大家好我是花果山的大圣，今天很荣幸，有机会跟大家分享一下很多年轻人感兴趣的话题《 Vue 和 React 设计思想 PK》,个人水平有限，如果有理解不到位的请倾盆，大家看完后并且再去 Vue 和 React 源码里探索一番，一定会有所收获， 如果没时间的话，还可以跟我一起早起学习</p>
<ol>
<li><a href="https://github.com/shengxinjing" target="_blank" rel="nofollow noopener noreferrer">Github </a></li>
<li><a href="https://space.bilibili.com/26995758" target="_blank" rel="nofollow noopener noreferrer">B站 </a></li>
<li><a href="https://juejin.cn/user/1556564194370270" target="_blank">掘金</a></li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c4574cd37928403eb63a0e0b87f97758~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d137d871a0c84c188352c2ede254a24e~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">框架总览</h2>
<p>前端框架繁多，在学习的时候也会陷入困惑，我们应该抓住最主流的内容 Vue/React，深入底层，尝试揣摩框架作者的设计思路，开阔自己的视野，大家也不要把自己限制在框架之中，认为工作中用到 Vue，就觉得 React 学起来没用，有些时候我们学习竞品的框架，是为了更好的认识自己在用的框架，废话不多说，由于 Vue 本身是个中庸的框架，再揪出设计思路理念比较极致的 Angular 和 Svelte，我们先从视图层最火的四大框架看一下</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/12a3b8d66a814d1fb6f5627b11fcd38d~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-3">下载量</h4>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a63c52d892b64aee919ed8855e602363~tplv-k3u1fbpfcp-zoom-1.image" alt="大圣-Vue和React设计理念.008.jpeg" loading="lazy" referrerpolicy="no-referrer"><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff1bb6223ed2434faf3adfe34bd77ce9~tplv-k3u1fbpfcp-zoom-1.image" alt="大圣-Vue和React设计理念.009.jpeg" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-4">对比维度</h4>
<p>我们从多个维度去对比前端的框架，就能看清楚现在各个框架的现状，我们学习每个框架的设计范式，并且尝试打破局限，就像猪八戒一样，出了高老庄，一路好风光</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d810ec257234ab5aae1e39271d0e8eb~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d395886d4ad54b629b4396ad3577393d~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-5">框架发展</h2>
<h4 data-id="heading-6">字符串模板</h4>
<p>想看清现在视图层的现状，要简单的看下之前框架的发展路线，JQuery 时代的渲染层，大部分都是基于字符串的模板，典型的框架就是 Underscore，baiduTemplate。大致的原理就是把 template 解析成一个函数，缺点也很明显，就是每次数据变化，模板内部要全部重新渲染</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2db08ddb2532418a81925113cf54b1e7~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a5c3382c8cb94c10883eed3913a4e81e~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后刚才我说的四个框架占领了现在的 Web 领域，核心的目标都是一样的，为了做出性能更好的 Web 应用，为此各路大神八仙过海，各显神通有这么几个宏观的维度</p>
<h4 data-id="heading-7">原生 VS 抽象</h4>
<p>原生的就是 JavaScript 本身，比如 JQuery 基本没有太多的抽象，一个 $ 打天下，React 抽象程度稍微复杂一些，需要理解 Component， State， Hooks， JSX 等概念就可以上手了，抽象比较多的就是 Angular，上手就需要了解十几个概念，学习曲线很陡峭， Vue 就处在 React 和 Angular 中间，了解完 data，methods，单文件组建后就可以上手了</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/32a617e973714b16b21cc4b0f3a7cd63~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-8">运行时 VS 预编译</h4>
<p>另外一个维度就是运行时和预编译这个维度，所谓运行时，在浏览器内存里进行的任务，React 的 Runtime 比较重一些，数据发生变化后，并没有直接去操作 dom，而是生成一个新的虚拟 dom，并且通过 diff 算法得出最小的操作行为，全部都是在运行时来做的</p>
<p>这个维度的另外一个极端，也就是重编译的框架，在上线之前经过通过工程化的方式做了预处理，典型代表就是Svelte，基本上是一个 Compiler Framework，写的是模板和数据，经过处理后，基本解析成了原生的 dom 操作，Svelte 的性能也是最接近原生 js 的</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/325799ddf0f14af29e56c0965818b2e9~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/522bd952967d4b14963bb520be13e3e9~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>Vue 依然处于比较中庸的地位，在运行时和预编译取了一个很好地权衡，保留了虚拟 dom，通过响应式控制虚拟 dom 的颗粒度，在预编译里又做了足够多的性能优化，做到了按需更新，这个一会再细聊</p>
<h2 data-id="heading-9">框架设计的维度</h2>
<h4 data-id="heading-10">Vue 和 React</h4>
<p>然后我们揪出来 Vue 和 React，有一些更细化维度
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1e454f5f0f3e4756846bd4b074bf105e~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-11">可变数据 VS 不可变数据</h4>
<p>Vue1 就是把响应式数据玩出了花，通过拦截操作，修改一个数据的同时收集依赖，然后数据修改的时候去通知更新 dom，体验很是舒爽，我们修改了一个 JavaScript 的对象，视图层就修改好了， 这是 Vue 的黑魔法，React 的虚拟 Dom 创建之日期，就是通过计算新老数据的 diff，去决定操作那些 dom，所以每次修改数据，需要生成一份新的数据，说不上优劣之分，只不过路线不同</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/813a14e102dd4e16adc933331f16c8b7~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>这大概就是 Vue 和 React 修改数据的代码对比</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9afb139654ad47dcb371af90a59bbe1d~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a369c80a96b04c2482d4231671c8a6c1~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3dff159950e042169730d35bcf33a8ec~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-12">权衡</h4>
<p>随着应用越来越复杂，React15 架构中，dom diff 的时间超过 16.6ms，就可能会让页面卡顿，Vue1 中的监听器过多，也会让性能雪崩，为了解决这个问题，Vue 选择了权衡，以组件作为颗粒度，组件层面用响应式通知，组件内部通过 dom diff 计算 ，既控制了应用内部 Watcher 的数量，也控制了 dom diff 的量级。看到这段实现的时候，不仅高呼，真是妙啊</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a0b15ba44154aee92fc90df3993f4eb~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  registerComponentHook(componentId, <span class="hljs-string">'lifecycle'</span>, <span class="hljs-string">'attach'</span>, <span class="hljs-function">() =></span> &#123;
    callHook(vm, <span class="hljs-string">'beforeMount'</span>)

    <span class="hljs-keyword">const</span> updateComponent = <span class="hljs-function">() =></span> &#123;
      vm._update(vm._vnode, <span class="hljs-literal">false</span>)
    &#125;
    <span class="hljs-keyword">new</span> Watcher(vm, updateComponent, noop, <span class="hljs-literal">null</span>, <span class="hljs-literal">true</span>)

    vm._isMounted = <span class="hljs-literal">true</span>
    callHook(vm, <span class="hljs-string">'mounted'</span>)
  &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-13">预编译和运行时</h4>
<p>相关概念刚才已经科普了，在 Vue 和 React 中的体现，主要体现在 JSX 和 template 的区别上，React 是完全的 JSX，可以 JSX 在里面写 JavaScipt，所以特点就是足够的动态，与之对应的就是 Vue 的 template，template 的特点是语法受限，可以执行的语法技术 <code>v-if</code> <code>v-for</code> 等指定的语法，虽然不够动态，但是由于语法是可便利的，所以可以再预编译层面做更多的预判，让 Vue 在运行时有更好的性能</p>
<p>顺便放两张尤大的 ppt 的图，Vue3 通过在预编译阶阶段做静态标记的优化，做到了按需更新</p>
<ol>
<li>纯静态的元素标记，直接越过 diff 阶段  比如 <code><p>hello</p></code> </li>
<li>静态的属性也会标记，在 diff 的时候越过这个属性的判断</li>
<li>事件函数传递的时候回加上缓存</li>
<li><code>v-if</code> 和 <code>v-for</code> 内部通过 block+ 数组的方式维护动态元素</li>
</ol>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/88dc332ce9b943f4ad63b85bb6e2fba3~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2fd9643bae64dad8aa9e85260d06318~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5930e293b4f34055957a4311c1b80cc1~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3e8b56965b74ad5847670f162104228~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c31ebe3f09aa4c0eb4d537cbd73d1a53~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/839392de105e499f8bd0c17a55330cdf~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-14">时间切片</h4>
<p>Vue3 通过静态标记 + 响应式 + 虚拟 dom 的方式，控制了 diff 的颗粒度，让 diff 的时间不会超过 16ms，但是 React 自上而下的 diff 过程，项目大了之后，一旦 diff 的时间超过 16.6ms，就会造成卡顿，对此 React 交出的解决方案就是时间切片</p>
<p>简单的来说就是把 diff 的任务按照元素拆开，利用浏览器的空闲时间去算 diff，React 把各种优化的策略都留给了开发者，Vue 则是帮开发者做了很多优化的工作</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/16b7afa3595b492fba7600894dfdd63f~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/26da3d0e15fe40f6956fcd2e6d5bd630~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7d34db220fde460da5a0585912be0fc4~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f275a6a160b740b99ba6f1b2a1ea4d62~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-15">设计思想演进</h2>
<h4 data-id="heading-16">组合优于集成</h4>
<p>这个思想设计模式里面就有定论，也是现在 hooks 和 composition 大行其道的原因，代码写出来也会更加易于维护，这个图可以很好地体现出可维护性上的变化
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99cf81cacdd547149758273c783dbaa3~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-17">跨端</h4>
<p>刚才我们讲了 Svelte 可以做到直接编译成 JavaScript，性能接近原生，这么优秀的思想，为什么 Vue 还要保留虚拟 dom 这个额外的 runtime 损耗呢，我觉得比较重要的一个答案就是跨端</p>
<p>虚拟 dom 除了可以用来计算最小的 diff 之外，另外一个重要的功能就是可以用 JavaScript 的对象来去描述一个 dom，这就是一个普通的对象，在跨端领域意义重大，视图层返回的是一个对象，渲染层可以调用不同平台的渲染 api 去绘制即可</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/22b6b1889c1f41cbaba0354ebb8d2305~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-18">复习</h2>
<p>如上所述，请认真学习框架，并不只是为了面试，而是框架里的优秀思想和设计模式，汇集了顶尖开发者团队最优秀的思想， 多学习别人优秀的代码，开阔自己的视野， 闭门造车你会发现，很多自己的顿悟只是别人的基础</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ae7d809b5bc2460189b530805b452910~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/178cba8e45a74859b54297b7f0996043~tplv-k3u1fbpfcp-zoom-1.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-19">推荐书</h2>
<p>最后推荐一本对我涨薪帮助最大的书《算法》第四版</p>
<p>算法和数据结构一直都是前端工程师进阶的拦路虎之一，这块内容比较成体系，JavaScript 相关的算法书过于简单，只能入门，不能帮你学会算法， 教材《算法导论》从数学的角度去推导算法，又太难，所以我推荐这本《算法》第四版，内容详实有插画，帮助系统的构架算法知识体系，书里用的是 Java，学习的时候正好用 JavaScript 实现一遍书里的例子，学完绝对是一个新的段位</p>
<p>当然，我最大的爱好除了王者，就是看书了，其实有很多书可以推荐，比如</p>
<ol>
<li>JavaScript 进阶的红黄绿三套书</li>
<li>怎么和 HR 谈钱的《谈判是什么》和《优势谈判》</li>
<li>和产品经理吹牛逼必备坛子 《浪潮之巅》《硅谷之谜》</li>
<li>《软技能2》</li>
<li>。。。。</li>
</ol>
<p>以后有机会再给大家推荐，感谢大家的支持 ，我是大圣， 下期再见</p>
<hr>
<p>别忘了给文章点赞</p></div>  
</div>
            