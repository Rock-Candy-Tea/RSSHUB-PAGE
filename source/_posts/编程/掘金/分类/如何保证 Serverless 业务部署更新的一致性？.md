
---
title: '如何保证 Serverless 业务部署更新的一致性？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/847c642294ab44969e7aa3c82fab6217~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 18:52:29 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/847c642294ab44969e7aa3c82fab6217~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>简介： 代码在其他场景被更新，需要我们在当前得到感知，这个事情其实是非常重要的，和代码的安全发布密不可少。而此时，通过 Serverless Devs 是可以做到的。</p>
<p>作者｜Anycodes</p>
<p>从我做 Serverless 工具开始，就经常会遇到有人问这样一个问题：如何保证 Serverless 业务部署更新的一致性。</p>
<p>所谓的一致性在这里指的是：我们通过工具在本地进行项目部署，此时再有人通过其他途径（例如控制台等），对项目进行过更新等操作，此时我再在本地进行项目部署，是不是会直接覆盖？</p>
<p>例如，当用户 A 在本地更新了业务，因为一些特殊情况，导致出现了一个线上异常情况 “X”，此时用户 B 重新更新，将这个内容修复了，但是 B 没有及时同步给 A 这个事情，A 又更新了新的功能，直接覆盖了 B 的内容，这个时候之前的异常 “X” 又出现了，如果此时在 A 更新的时候，可以感知到线上资源已经变动，那么这种事情就不会再次发生。</p>
<p>目前基于 Serverless Devs 的阿里云函数计算组件，已经支持了线上 “异动” 的感知能力，包括了以下几个情况：</p>
<ul>
<li>本地新建并部署一个线上没有的资源</li>
<li>本地部署完成，线上更新，本地再次部署</li>
<li>本地新建并部署一个线上已经有的资源</li>
</ul>
<h1 data-id="heading-0">实验准备</h1>
<p>通过 s init 创建一个函数（选择 Aibaba Cloud Serverless， 选择 HTTP Function - Python3 Example ）：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/847c642294ab44969e7aa3c82fab6217~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时我们查看一下 s.yaml ：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/67d91ac3d9b240a494b5e21eb4f3e368~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>该项目部署到线上之后的表现就是在 cn-hangzhou 区创建一个 fc-deploy-service 服务，以及 http-trigger-function 函数。</p>
<h1 data-id="heading-1">实验过程</h1>
<p><strong>本地新建并部署一个线上没有的资源</strong></p>
<p>此时，我们确定一下线上并没有对应资源，所以我们部署一下：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c81fb6ca4cc54f8bba55ec8ee6824637~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>部署完成，很顺利：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cf2452a2580141239e1dd240591612bf~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>打开浏览器，查看反馈给我们的自定义地址：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/38af58897a60450a86377563b2681d79~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时，我们可以在本地，更新一下这个函数代码：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a18e963897634d68b325d70275e23e21~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>保存部署：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94390fae3e69404db91aba45ade76f2c~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>完成之后，再查看线上资源：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb8850675c6045b6a73d5f398fb41f5e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>整个过程，还是比较贴近传统的基本流程，也没有触发线上异动，算是中规中矩的理想过程。</p>
<h1 data-id="heading-2">本地部署完成，线上更新，本地再次部署</h1>
<p>此时，我们对线上资源进行变更，首先在控制台找到函数：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/61fff83c047f4d168db18a387dfa6692~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>修改代码，并部署。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3c01d91f4ca4d30b433e618ac5da48e~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>部署完成之后，我们刷新一下刚才的地址：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/46004a07830c404dbd91b7ff5360803d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到已经更新。此时，我们再从本地进行部署：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bb9aef67b4804accb831741ad36bd960~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>可以看到，系统已经感知到我们的代码变化，此时，我们选择yes，完成之后在查看线上资源：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ea84be9b3a854020b75be88152a40aea~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>此处需要额外说明的是，只要是函数计算的服务，函数，触发器发生变化，此处都可以进行感知，不管是配置还是代码。</p>
<h1 data-id="heading-3">本地新建并部署一个线上已经有的资源</h1>
<p>此时，我们再进行最后的实验，我们将本地项目删除，重新建设。然后执行部署，由于刚刚实验过的原因，我们已经在线上存在了这些资源，所以此时算是部署一个线上的资源。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/426269da6d0343f6bbd90226ad8e069d~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时可以看到，系统感知到这个资源本地没部署过，线上并且已经存在，所以此时需要确定是否覆盖。</p>
<h1 data-id="heading-4">总结</h1>
<p>代码在其他场景被更新，需要我们在当前得到感知，这个事情其实是非常重要的，和代码的安全发布密不可少。而此时，通过 Serverless Devs 是可以做到的。</p>
<p>那么问题来了，如果我已经有了一个项目，我想集成到cd流程，我不想出现交互式操作，应该如何处理呢？</p>
<p>此时我们提供一个 --ues-local 参数，用来强行覆盖线上配置，通过这样的指令就可以实现无交互的，本地优先。</p>
<p>每一个工具的诞生，都要有一个成长的过程，Serverless Devs 正在不断的成长。期待更多更好的功能出现。</p>
<p><a href="https://link.juejin.cn/?target=http%3A%2F%2Fclick.aliyun.com%2Fm%2F1000285452%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://click.aliyun.com/m/1000285452/" ref="nofollow noopener noreferrer">原文链接</a></p>
<p>本文为阿里云原创内容，未经允许不得转载。</p></div>  
</div>
            