
---
title: 'feat_ add dbaplus社群'
categories: 
    - 编程
    - GitHub - 仓库 Pull Requests
author: GitHub - 仓库 Pull Requests
comments: false
date: Wed, 10 Mar 2021 14:29:07 GMT
thumbnail: ''
---

<div>   
<h2>该 PR 相关 Issue / Involved issue</h2>
<p>Close #7144</p>
<h2>完整路由地址 / Example for the proposed route(s)</h2>
<!--
为方便测试，请附上完整路由地址，包括所有必选与可选参数，否则将导致 PR 被关闭。
To simplify the testing workflow, please include the complete route, with all required and optional parameters, otherwise your pull request will be closed.

请按照如下格式填写`routes`区域: 我们将会根据你的参数展开自动测试. 一行一个路由
Please fill the `routes` block follow the format below, as we will perform automatic test based on this information. one route per line.

```
/some/route
/some/other/route
```

如果与路由无关, 请写`NOROUTE`
-->
<!-- 在下方填写, 请不要删除`routes`标识: CI验证需要. FILL BELOW and keep `routes` keyword -->
<pre><code class="language-routes">/dbaplus
/dbaplus/153
/dbaplus/134
/dbaplus/73
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
<li>[x] 这个PR中包含了新的路由吗? Does this PR add new route?
<ul>
<li>如果有, 请完成检查列表. If yes, please finish the check list</li>
<li><strong>如果你的PR符合下方某个事项, 也请注明. If any of the checklist item meets your PR, please fill it out.</strong></li>
<li>[x] <- 这样打勾</li>
</ul>
</li>
<li>[x] 是否提供了文档? Documentation provided?
<ul>
<li>[ ] 是否提供了英文文档? EN Documentation provided?</li>
</ul>
</li>
<li>[x] 是否支持全文获取? Is this RSS Script support fulltext?
<ul>
<li>[x] 如果全文获取中需要访问文章链接, 是否使用了缓存? If fulltext requires to fetch detail pages, is cache used in the process?</li>
<li><a href="https://docs.rsshub.app/joinus/#ti-jiao-xin-de-rsshub-gui-ze-bian-xie-jiao-ben-shi-yong-huan-cun">缓存说明</a> | <a href="https://docs.rsshub.app/joinus/#ti-jiao-xin-de-rsshub-gui-ze-bian-xie-jiao-ben-shi-yong-huan-cun">How to use cache</a></li>
</ul>
</li>
<li>[ ] 目标是否有明显的反爬/频率限制? Is there any sign of anti-bot or rate limit?
<ul>
<li>[ ] 如果有, 是否有对应的措施? (延长缓存时间, 写文档说明, etc.) If yes, do your code reflect this sign? (e.g. write documentations, use long cache time)</li>
</ul>
</li>
<li>[ ] 是否引入的新的包? Any new package introduced?
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
  
</div>
            