
---
title: '用Vue3+Vite+Typescript及全家桶最近版本搭建一个多人在线聊天室'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6afbfc3382b847e5a9936b094d5847ff~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 02:37:13 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6afbfc3382b847e5a9936b094d5847ff~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>先整个在线体验链接，瞅瞅效果：</p>
<p><a href="http://www.hgqweb.cn/vue3-h5/chat-room/index.html#/login" target="_blank" rel="nofollow noopener noreferrer">芒果皮儿聊天室在线Demo</a></p>
<p>一直想体验一下Vue3及周边技术栈的最新版本，于是最近几天忙活了一下，整了个在线聊天室的Demo版本吧，使用Vite搭建的，模板采用的vue-ts，整合了vuex，vue-router，ant-design-vue，axios的最新版本，感觉还挺爽，也踩了一些坑，但是对于大佬们来说必然不算啥，所以完全是小白的姿势尝鲜新技术，算是练练手吧。</p>
<p>服务端这边使用的是被称为Node版Spring的NestJs，用起来个人感觉还是很nice的，刚接触还在学习中，整合了JWT身份验证、日志系统、数据库操作等（代码最初也是参考大佬的教程做的），实现了登录注册及SocketIO收发消息。</p>
<p>话不多说先放几张效果图：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6afbfc3382b847e5a9936b094d5847ff~tplv-k3u1fbpfcp-watermark.image" alt="e5b42f6534250522b5e5428d2a72c30.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>还有一个平平无奇毫无美感的登录页，作为前端的耻辱（狗头）：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3a15151670b5480084822296fe44d3f6~tplv-k3u1fbpfcp-watermark.image" alt="429c02066c116b016f9c99c2a0fa680.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>整体代码比较简单，GitHub地址为 <a href="https://hub.fastgit.org/guoguoqiqi/chat-room-client" target="_blank" rel="nofollow noopener noreferrer">聊天室前端代码Vue3+Vite+Typescript</a>，求几个星星</p>
<p>服务端代码也在我的GitHub上</p>
<p>目前刚开始做，只完成了登录注册及收发消息，还在不断完善更新，欢迎交流或者一起练手完善</p></div>  
</div>
            