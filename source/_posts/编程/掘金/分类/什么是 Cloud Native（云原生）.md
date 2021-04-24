
---
title: '什么是 Cloud Native（云原生）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c13f55e668e48caaca8e27c52d51071~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 23 Apr 2021 21:49:52 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c13f55e668e48caaca8e27c52d51071~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>最近群里有两三个人都提到了云原生，我就趁着周末的时间看看什么是云原生。</p>
<p>此文翻译自<a href="https://docs.microsoft.com/en-us/dotnet/architecture/cloud-native/definition" target="_blank" rel="nofollow noopener noreferrer">微软的文档</a>，但是翻着翻着我就不得不吐槽了。</p>
<p>译文开始</p>
<hr>
<p>你去问十个工程师，什么是云原生，很有可能会得到十个不同的答案。</p>
<p>云原生将颠覆你过去关于如何搭建一个核心商业系统的思维模式。</p>
<p>云原生的系统可以很好地应对极速变化、快速扩展和弹性伸缩（rapid change, large scale, and resilience）（译注：所有新技术都这么说）。</p>
<p>云原生计算基金会对云原生的官方定义如下：</p>
<blockquote>
<p>云原生技术可以给团队赋能（译注：有阿里味儿），以保证团队能够在公共云、私有云以及混合云等各种动态的环境中运行大规模的应用，使用到的技术包括但不限于容器化、服务网格、微服务、不可变基础设施（Immutable Infrastructure）、声明式 API 等</p>
</blockquote>
<blockquote>
<p>这些技术可以打造可伸缩、可管理、可监控的松耦合系统。基于强健的自动化基础，这些被联合起，来的技术，可以让工程师很轻松地对系统进行重大的改造。</p>
</blockquote>
<p>随着用户需求的增长（译注：我看是产品经理的不靠谱系数增长），应用变得越来越复杂了。但用户期待更快速地反应、更新颖的功能，还有零宕机时间。性能问题、不停出现的报错、难以维护的系统使得用户的期待很难得到满足，用户就会跑到你的竞争对手那里去（译注：制造焦虑）。</p>
<p>而云原生可以为你提供速度和灵活度。</p>
<p>以下是已经实现了这些技术的公司（译注：这些公司实现了这些技术，不代表这些公司使用了云原生），想一想这些公司有多牛 X（译注：跟你云原生有什么关系呢）：</p>





















<table><thead><tr><th>公司</th><th>体验</th></tr></thead><tbody><tr><td>网飞 Netflix</td><td>拥有 600 多个服务，每天部署一百次以上</td></tr><tr><td>优步 Uber</td><td>拥有 1000 多个服务，每天部署几千次</td></tr><tr><td>微信 WeChat</td><td>拥有 3000 多个服务，每天部署一千次以上</td></tr></tbody></table>
<p>这些公司的系统就是有上百个独立的微服务组成的。这种架构方式让它们能快速响应市场需求，它们能第一时间更新自己的复杂应用里面的小服务，也能按需求量将小服务快速扩张。</p>
<p>译注：我翻译不下去了，也没有必要继续翻译了。</p>
<hr>
<p>下文讲了容器化、自动化、后台服务、Serverless、微服务、多项目仓库、持续集成、持续部署、日志系统、权限管理等等……都属于云原生。</p>
<p>然后我就懂了：只要我们把所有服务都搬到阿里云/腾讯云/微软云/亚马逊云上，就一定是云原生了，因为云原生的关键技术在这些平台上都有售。</p>
<p>你要是自己买几台服务器来跑应用，那绝对不能算作云原生。</p>
<p>而且你还得在设计系统的第一天起就默认已经购买了这些服务，不然就不够「原生」了。</p>
<p>合着「云原生」就是「云计算厂商」提供的套餐呗，买就对了。</p>
<p>最后我认为「云原生」还是不如 low-code，因为 low-code 连代码都不用写了。</p>
<p>快点出 low-code 套餐吧，我下次一定买。</p>
<p>手动狗头。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9c13f55e668e48caaca8e27c52d51071~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            