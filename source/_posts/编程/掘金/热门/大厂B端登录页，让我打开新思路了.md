
---
title: '大厂B端登录页，让我打开新思路了'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4dc4fad4847144d6a0d0d6bc753b902b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
author: 掘金
comments: false
date: Thu, 01 Sep 2022 20:18:56 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4dc4fad4847144d6a0d0d6bc753b902b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:16px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:24px;margin-bottom:5px&#125;.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;font-size:20px&#125;.markdown-body h2&#123;padding-bottom:12px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>登录页这个东西，因为感觉很简单，所以经常不被重视。</p>
<p>但是登录页作为一个产品的门面，直接影响用户第一印象，又是非常重要的存在。</p>
<p>最近研究了一下我电脑上那一堆桌面端的登录页，还真发现了一些之前没想清楚的门道来。</p>
<p>目录：</p>
<p>0. 不登录</p>
<p>1. 填写项目</p>
<p>2. 二维码</p>
<p>3. 登录方式</p>
<p>4. 注册和忘记密码</p>
<p>5. 勾选项</p>
<p>6. 登录按钮</p>
<p>7. 设置项</p>
<p>8. Logo</p>
<p>0. 不登录</p>
<p>很多产品会提供部分功能给未登录账号使用。</p>
<p>比较谨慎的，Zoom 会给一个直接加入会议的按钮：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4dc4fad4847144d6a0d0d6bc753b902b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>极端一些的，会像 WPS 这样打开后直接进入，不需要登录页：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/68e5e7c3bbce45bba1c2ca25bc02e4c1~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>给未登录用户太多功能会影响注册用户占比，强制登录又会把使用门槛拉得太高，这个主要看产品定位吧。</p>
<p>接下来，咱们主要针对必须登录的情况来讲吧。</p>
<p>1. 填写项</p>
<p>这有什么好说的，登录填写项不就是用户名/邮箱/手机号+密码吗？</p>
<p>没错，最典型的却是如此。例如百度网盘和钉钉：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10cfc3abad364878a3f3e2b70a56074d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bdb7cb9f12534a72818e5c3fa3edd483~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是我发现，有的产品会故意分两步让你填，这样就可以把注册和登录合并到一个步骤了（输入后看看注册过没，没有就走注册流程，有就走登录流程）。例如飞书和 Google：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/591ee589d7904691a2966cbf81702011~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/28c2708427aa4a86945e0eb7fd915f27~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>还有的，甚至不把填写项放出来，非要你点击入口才行。例如微云和 CCtalk：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/90eae20be3284ff7845f2a7a2afb5607~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e74b97939fd24bf6b55c64f322ba4e47~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>我个人是比较喜欢一打开就是填写项，一次填完的，不知道大家怎么看？</p>
<p>2. 二维码</p>
<p>我发现把二维码放到右上角的方式蛮常见的。</p>
<p>例如钉钉就做得很好看：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/396a69d85a8946948e010dfd9210d8b9~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>飞书用高亮色做有点生硬，但也还行：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f602fe5b754540e58b436c5bc2349f02~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>微云这个感觉中间突然被切了一角，有点奇怪：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c989ce023a7d4672b777005b547d1559~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>3. 登录方式</p>
<p>如果登录方式只有 2 种，tab 是最常用的切换方式。例如微云：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/81badc2e7e104463ae66b49d82da8fac~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果比较多，用图标在底部列出来是最常用的方式。例如腾讯会议和 Zoom：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/75f80da33add4b8396aa9ed08460fcc9~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3d19b8d8e12843eb9f3daf49e855d520~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>但也有一些产品，可能比较纠结，两种方式混合一下。比如飞书：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/be8e2d28164a427f9d5df4161c8cdaaa~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是记住一定要在图标下加文字说明，否则就会像 CCtalk 一样看不懂第一个图标是什么（悬停提示也没有）：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b7e49eded81f49019df2a126d5d8bd1d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>4. 注册与忘记密码</p>
<p>这两个按钮几乎所有登录页都需要，但又不是特别重要的信息。</p>
<p>一般两种布局最常见，一是将这两个按钮都放在输入框下面。例如微云和钉钉：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a350dd0f489f473f8ef55d7db589412c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/638020c82eb64c9989f7d6369bb6f143~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>二是把忘记密码放在密码框里面，然后注册就放在右下角某个地方。例如 Zoom、腾讯会议：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3766dcbe7afa4e0d94d43813f1e734b6~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7a3b23305d084697acc17b696a036f54~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>也如果把输入邮箱/手机号和密码分成两步，就可以省略一个这两个入口，不过登录就得多一步操作了。例如飞书：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/878a2d037d53462ca04dd94a884a0124~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>5. 勾选项</p>
<p>登录页一般有两个勾选项，一个是自动登录、一个是同意协议条款的，大多默认不勾选。</p>
<p>一般都放到登录按钮的下面，虽然不符合操作顺序（先勾选了才能确定），但是排版好看些。例如飞书：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b61315c0d7f84f05bd46000ecede3168~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>其实像微云这样把勾选项放到登录按钮上其实更加符合操作顺序，因为这是在登录之前要确认的内容：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/898f98354b4b495fa8127daf38443923~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Zoom 在底部写上登录即代表同意政策和条款，就省略一个勾选项了：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/47e7c82d35694967a378ef0acd77c1ef~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>但谁都比不上百度网盘，它们干脆一个勾选项都没有，至今还不是好好的？</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/966daf4f940d4286ba64cddecaedaa12~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>6. 登录按钮</p>
<p>基本上登录页都少不了登录按钮，除非是像钉钉这样登录方式有限的：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/24457da4cbef4a9f9545b09507355711~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>有的产品会让登录按钮置灰，直至用户填写完成为止。例如飞书和 Zoom：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/76b9a3fb1fc140639c5bb195569ce912~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1dc3bac3dce04b308f4a5d417e87b52e~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>7. 设置项</p>
<p>很多产品会在用户登录之前就提供设置项目，主要是网络设置和语言设计。</p>
<p>例如飞书就两个都给了（左下角），做得挺到位的：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f9d95e1d66f4782a7406114ebcbb5a7~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>Zoom 就没有提供，跟着我的系统语言用中文，这个思路页也能理解：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1b7786ba00784ebbbe859328ae77afd0~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a375454f21e24473a71b562ed7ba619c~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>腾讯会议比较实诚，把整个设置面板的入口都放到登录页了，包括语言选项在内：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/894f8e23823e46c8a0cbbea23e816f1b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ee3ea55b8dbf451580a9d4fa1dd1275b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>8. Logo</p>
<p>大部分产品的登录页都会放上 logo，这个感觉是常识。例如腾讯会议、百度网盘：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b8c652b1563496589d4bec108fb256d~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1ef279b90b1c4085a107e5454db78b0b~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>但其实也有不少只写名字不放 logo 的。例如微云、飞书：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94511363c3c7488b95c3aa4df19948af~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fdfe1920f36142de855ad041cbcdca15~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>钉钉就比较奇特，既没有 logo 也没有名字，不去状态栏查看一下都不知道这是什么软件：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f9f9b8c9ec75402ea2e29092c8408826~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>总结一下</p>
<p>登录页表面看上去简单，经常不受重视，但仔细这么对比下来，发现可变因素还真是挺多的。</p>
<p>不知道大家对于这个页面有什么困惑的地方，可以在评论区讨论一下。</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.mockplus.cn%2F%3Fhome%3D1%3Fhmsr%3Dwenjj" target="_blank" rel="nofollow noopener noreferrer" title="https://www.mockplus.cn/?home=1?hmsr=wenjj" ref="nofollow noopener noreferrer"><strong>做设计，用摹客</strong></a>。</p>
<p>以上文章来源于体验进阶，作者 设计师ZoeYZ</p></div>  
</div>
            