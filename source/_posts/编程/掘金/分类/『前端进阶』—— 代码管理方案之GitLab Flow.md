
---
title: '『前端进阶』—— 代码管理方案之GitLab Flow'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff670e54f7904a21bc964ea650d60b87~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 30 Jun 2021 05:45:59 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff670e54f7904a21bc964ea650d60b87~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.8;font-weight:400;font-size:16px;word-spacing:2px;letter-spacing:2px;overflow-x:hidden;color:#3e3e3e;background-image:linear-gradient(90deg,rgba(50,0,0,.05) 3%,transparent 0),linear-gradient(1turn,rgba(50,0,0,.05) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:1.2em;border-bottom:2px solid #ef7060;word-spacing:0!important;letter-spacing:0!important;font-size:inherit;line-height:inherit;display:block;font-weight:400;background:#ef7060;color:#fff;padding:10px;border-top-right-radius:3px;border-top-left-radius:3px;margin-right:3px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>当你往高级前端进阶的过程中，避免不了要带领团队负责一个项目，此时你必定会遇到一个头疼的问题，代码如何进行管理。一般我们都使用Git来管理代码，业界中提供了几种Git工作流，每一种Git工作流就是一种代码管理方案，在对这几种Git工作流的流程熟悉后，才能给团队提供一种合适的代码管理方案。</p>
<p>本文将详细介绍其中一种Git工作流——GitLab Flow，希望对你有帮助，也欢迎在评论中讨论。</p>
<h2 data-id="heading-1">一、流程概念图</h2>
<p>先上一张流程概念图，按图给你介绍GitLab Flow。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ff670e54f7904a21bc964ea650d60b87~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">二、开发流程</h2>
<p>GitLab Flow 的最大原则叫做"上游优先"（upsteam first），即只存在一个主分支master，它是所有其他分支的"上游"。只有上游分支采纳的代码变化，才能应用到其他分支。</p>
<p>故开发新功能前，要用分支master创建一个开发新功能的分支，分支的名称可以用功能名称来命名，这里先给这个分支命名为feature。</p>
<p>当功能开发完成后，用分支master去合并分支feature，合并完成后将分支feature删除。</p>
<h2 data-id="heading-3">三、测试流程</h2>
<p>将分支master的代码部署到测试环境，测试出BUG，直接在分支master上修复，修复完成后部署到测试环境进行测试。</p>
<h2 data-id="heading-4">四、预发布流程</h2>
<p>分支master的代码测试通过后，用分支master创建出一个分支，命名为pre-production。分支pre-production就是<strong>预发布分支</strong>，将其部署到预发布环境。</p>
<h2 data-id="heading-5">五、修复预发布环境BUG流程</h2>
<p>预发布的代码出现BUG时，由于要遵循“上游优先”，不能直接在分支pre-production上修复BUG，得用分支pre-production创建出一个修复BUG的分支，分支的名字可以用BUG名称来命名，这里先给这个分支命名为fixbug。</p>
<p>将BUG修复后，用分支master合并分支fixbug，将分支master的代码部署到测试环境进行测试。</p>
<p>若没有通过测试，继续在分支fixbug上修复BUG，修复后再用分支master合并分支fixbug，再把分支master的代码部署到测试环境进行测试，直到BUG被修复。</p>
<p>BUG被修复后，用分支pre-production合并分支fixbug，然后将分支pre-production的代码部署到预发布环境进行测试，若测试通过则BUG修复完毕，删除分支fixbug，若测试不通过重复以上步骤。</p>
<h2 data-id="heading-6">六、正式环境发布流程</h2>
<p>遵循“上游优先”原则，要用预发布分支pre-production创建出一个分支，命名为production。分支production就是正式分支，将其部署到正式环境，即完成正式环境发布流程。</p>
<h2 data-id="heading-7">七、修复正式环境BUG流程</h2>
<p>遵循“上游优先”原则，得用分支production创建出一个修复BUG分支，分支的名字可以用BUG名称来命名，这里先给这个分支命名为fixbug。</p>
<p>在BUG修复后，在本地测试通过后，用分支master合并分支fixbug，将分支master的代码部署到测试环境进行测试。</p>
<p>若没有通过测试，继续在分支fixbug上修复BUG，再用分支master合并分支fixbug，将分支master的代码部署到测试环境进行测试，直到BUG被修复。</p>
<p>BUG修复后，要遵循“上游优先”原则，故要先把代码发到预发布环境进行测试，测试通过后才能发布到正式环境。</p>
<p>那么用分支pre-production合并分支fixbug。然后将分支pre-production的代码部署到预发布环境进行测试。</p>
<p>若测试通过，用分支production合并分支fixbug，然后部署到正式环境，删除分支fixbug。</p>
<p>若测试失败，重新回到分支fixbug修复BUG，继续走上面的流程，直到Bug被修复。</p>
<h2 data-id="heading-8">八、版本发布流程</h2>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9f8bd4e12974f0e848c9db29c621442~tplv-k3u1fbpfcp-watermark.image" alt="GitHub Flow概念图2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>在GitLab Flow 中版本发布不是采用打tag的形式。而是要用分支master创建一个分支，分支的名字可以如上图那样命名，比如2-3-stable、2-4-stable等等，要注意此时的分支master上的代码是稳定。</p>
<p>若版本分支的代码出现BUG，还是要在分支master上修复BUG，BUG被修复且通过测试后，在版本分支上执行命令<code>git cherry-pick commitId</code>，其中commitId是分支master上BUG修复的提交commitId，将修复BUG的代码合并到版本分支上，再将代码部署到对应的环境。</p></div>  
</div>
            