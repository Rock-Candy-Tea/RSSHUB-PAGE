
---
title: '『前端进阶』—— 代码管理方案之Aone Flow'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff896d6229c6425da1d7ad9f768a6073~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 07:13:17 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff896d6229c6425da1d7ad9f768a6073~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.8;font-weight:400;font-size:16px;word-spacing:2px;letter-spacing:2px;overflow-x:hidden;color:#3e3e3e;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.2em;border-bottom:2px solid #ef7060;word-spacing:0!important;letter-spacing:0!important;font-size:inherit;line-height:inherit;display:block;font-weight:400;background:#ef7060;color:#fff;padding:10px;border-top-right-radius:3px;border-top-left-radius:3px;margin-right:3px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>当你往高级前端进阶的过程中，避免不了要带领团队负责一个项目，此时你必定会遇到一个头疼的问题，代码如何进行管理。一般我们都使用Git来管理代码，业界中提供了几种Git工作流，每一种Git工作流就是一种代码管理方案，在对这几种Git工作流的流程熟悉后，才能给团队提供一种合适的代码管理方案。</p>
<p>本文将详细介绍其中一种Git工作流——Aone Flow，希望对你有帮助，也欢迎在评论中讨论。</p>
<h2 data-id="heading-1">一、开发流程</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff896d6229c6425da1d7ad9f768a6073~tplv-k3u1fbpfcp-watermark.image" alt="Aone-flow.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在Aone Flow中只有三种分支，正式分支master，预发布分支release，功能分支(特性分支)feature。</p>
<p>当开发新功能时，从分支master创建feature分支，分支的命名通常以“feature/功能名称”来命名，每个feature分支可以是一个人完成，或是多个人协作完成。</p>
<p>切记不能用分支master去合并feature分支，也不能在分支master上提交任何修改。</p>
<h2 data-id="heading-2">二、预发布流程</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9de589c955874cfeb1b68df69f67af49~tplv-k3u1fbpfcp-watermark.image" alt="Aone-flow1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在Aone Flow中使用release分支作为预发布分支，先用分支master创建一个release分支，分支的名称通常以release/环境名称，然后将要预发布的功能对应的feature分支合并到release分支。最后将release分支的代码部署到对应的预发布环境进行测试，若出现BUG，直接在release分支上修复，修复完成后再部署到对应的预发布环境测试。</p>
<h2 data-id="heading-3">三、正式发布流程</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2609aae1778e4599a1b329cdca19da80~tplv-k3u1fbpfcp-watermark.image" alt="Aone-flow2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>当release分支的代码在对应的预发布环境测试通过后，用分支master合并release分支，合并完成后打出一个tag，其tag的名称可以用版本号来命名，然后将tag上的代码部署到正式环境，正式发布流程完成，同时删除release分支和相关联的feature分支。</p>
<h2 data-id="heading-4">四、修复正式环境的BUG流程</h2>
<p>若正式环境出现BUG，那么要找到对应版本的tag，用tag创建出一个release分支，此时的release分支相当fixbug分支，在release分支上修复BUG后，将代码部署到对应的预发布环境进行测试。</p>
<p>若测试通过后，在release分支打一个tag，其tag的名字用该版本号后面加个小版本号来命名，如修复v1.1版本的BUG，则tag的名称为v1.1.1，然后将该tag的代码部署在正式环境，最后再用分支master合并release分支，合并完成后将release分支删除。</p>
<p>若测试未通过，继续在release分支修复BUG，再将代码部署到对应的预发布环境进行测试。</p></div>  
</div>
            