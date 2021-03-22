
---
title: """""""""""'chroe_ Docker build 缩小 image size 更新github action'"""""""""""
categories: 
    - 编程
    - GitHub - 仓库 Pull Requests
author: GitHub - 仓库 Pull Requests
comments: false
date: Sun, 14 Mar 2021 12:39:18 GMT
thumbnail: 'https://user-images.githubusercontent.com/16515468/111068763-16df5d80-8505-11eb-82fd-61190641ee7d.png'
---

<div>   
<h2>该 PR 相关 Issue / Involved issue</h2>
<p>Close #</p>
<h2>完整路由地址 / Example for the proposed route(s)</h2>
<!--
为方便测试，请附上完整路由地址（可以真正访问的地址），否则将导致 PR 被关闭
请按照如下格式填写`routes`区域: 我们将会根据你的参数展开自动测试. 一行一个路由
如果路由包含在文档中列出可以完全穷举的参数（例如分类），请依次全部列出
To simplify the testing workflow, please include COMPLETE route URL, with all required and optional parameters, otherwise your pull request will be closed.
Please fill the `routes` block follow the format below, as we will perform automatic test based on this information. one route per line.

```
/some/route
/some/other/route
```

如果与路由无关, 请写`NOROUTE`
请不要删除代码块`routes`标识 
If it is not related to route, use `NOROUTE` to bypass CI
FILL BELOW and keep `routes` keyword
-->
<pre><code class="language-routes">NOROUTE
</code></pre>
<h2>新RSS检查列表 / New RSS Script Checklist</h2>
<!-- 
Please go over the checklist below before PR: this improve your PR pass rate.
Reference: https://docs.rsshub.app/en/joinus/
请在提交PR前检查以下事项: 这可以大大提升通过率
这些就是我们在审核时主要关注的事项, 敬请留意
参考: https://docs.rsshub.app/joinus
-->
<ul>
<li>[ ] 这个PR中包含了新的路由吗? Does this PR add new route?
<ul>
<li>如果有, 请完成检查列表. If yes, please finish the check list</li>
<li><strong>如果你的PR符合下方某个事项, 也请注明. If any of the checklist item meets your PR, please fill it out.</strong></li>
<li>[x] <- 这样打勾</li>
</ul>
</li>
<li>[ ] 是否提供了文档? Documentation provided?
<ul>
<li>[ ] 是否提供了英文文档? EN Documentation provided?</li>
</ul>
</li>
<li>[ ] 是否支持全文获取? Is this RSS Script support fulltext?
<ul>
<li>[ ] 如果全文获取中需要访问文章链接, 是否使用了缓存? If fulltext requires to fetch detail pages, is cache used in the process?</li>
<li><a href="https://docs.rsshub.app/joinus/#ti-jiao-xin-de-rsshub-gui-ze-bian-xie-jiao-ben-shi-yong-huan-cun">缓存说明</a> | <a href="https://docs.rsshub.app/joinus/#ti-jiao-xin-de-rsshub-gui-ze-bian-xie-jiao-ben-shi-yong-huan-cun">How to use cache</a></li>
</ul>
</li>
<li>[ ] 目标是否有明显的反爬/频率限制? Is there any sign of anti-bot or rate limit?
<ul>
<li>[ ] 如果有, 是否有对应的措施? (延长缓存时间, 写文档说明, etc.) If yes, do your code reflect this sign? (e.g. write documentations, use long cache time)</li>
</ul>
</li>
<li>[x] 是否引入的新的包? Any new package introduced?
<ul>
<li>如果有, 请说明原因. If yes, please state your reason</li>
</ul>
</li>
<li>[ ] 是否使用了<code>Puppeteer</code>? Make use of <code>Puppeteer</code>?
<ul>
<li>如果有, 请说明原因. If yes, please state your reason</li>
</ul>
</li>
</ul>
<h2>说明 / Note</h2>
<!-- 
Please state your reason/note here 
请在这里描述你的原因或留下其他相关的说明
-->
<ol>
<li>使用<a href="https://www.npmjs.com/package/@vercel/nft">@vercel/nft</a>删除用不到的JS文件。Vercel 在它的Function中就是使用这个东西去删除无用文件的。所以应该vercel能跑起来的，删完之后docker也能跑起来。</li>
<li>使用multi-stage build, 缩小image 体积。避免编译的依赖进入最终docker image。 把长命令分开成一个个RUN,可以更好的利用docker的layer缓存</li>
<li>更新github action 为 <a href="https://github.com/docker/build-push-action">https://github.com/docker/build-push-action</a> 其实就是现在用的这个action的v2</li>
</ol>
<p>Question: 是否可以考虑统一Dockerfile里的npm,yarn。并在容器内提供lock file使用<code>yarn</code>或者<code>npm ci</code>这样安装依赖起来会快些。 （我觉得用选npm好些，yarn1 “frozen” 了</p>
<p>可能拆分几个pr更好, 但是测试action和docker build的时间着实久。。。所以不分了</p>
<p><img src="https://user-images.githubusercontent.com/16515468/111068763-16df5d80-8505-11eb-82fd-61190641ee7d.png" alt="docker-images" referrerpolicy="no-referrer"></p>
  
</div>
            