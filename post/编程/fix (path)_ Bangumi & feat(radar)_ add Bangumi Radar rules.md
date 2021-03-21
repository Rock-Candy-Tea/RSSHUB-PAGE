
---
title: fix (path)_ Bangumi & feat(radar)_ add Bangumi Radar rules
categories: 
    - 编程
    - GitHub - 仓库 Pull Requests
author: GitHub - 仓库 Pull Requests
comments: false
date: Wed, 10 Mar 2021 15:51:06 GMT
thumbnail: 
---

<div>   
<h2>该 PR 相关 Issue / Involved issue</h2>
<p>Close #</p>
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
<pre><code class="language-routes">/bangumi/subject/315069
/bangumi/topic/361913
/bangumi/subject/214265/blogs
/saraba1st/thread/1842868
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
<li>[ ] <- 这样打勾</li>
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

-->添加了 Bangumi 的 RSSHub Radar 支持。修改了文档中 Bangumi RSS 的一处错误。上述两项修改均已亲自测试。
<p>下面有两个问题</p>
<ul>
<li><s>发现疑似失效路由两个，我不确定是否需要移除</s>
<ul>
<li><s>/bangumi/subject/:id/blogs 文档： <a href="https://docs.rsshub.app/anime.html#bangumi-tiao-mu-di-ping-lun">https://docs.rsshub.app/anime.html#bangumi-tiao-mu-di-ping-lun</a></s></li>
<li><s>/bangumi/topic/:id 文档： <a href="https://docs.rsshub.app/anime.html#bangumi-xiao-zu-hua-ti-de-xin-hui-fu">https://docs.rsshub.app/anime.html#bangumi-xiao-zu-hua-ti-de-xin-hui-fu</a></s></li>
</ul>
</li>
<li>Bangumi 是多个网址，我不知道该如何都匹配上，难道要重复三遍仅修改网址吗？貌似不太优雅，还请指教或者帮忙修改。
<ul>
<li>网址分别是 <a href="https://bgm.tv/">https://bgm.tv</a> ,<a href="https://bangumi.tv/">https://bangumi.tv</a> ,<a href="https://chii.in/">https://chii.in</a></li>
</ul>
</li>
</ul>
<p>以上，感谢开发者帮忙查看。</p>
  
</div>
            