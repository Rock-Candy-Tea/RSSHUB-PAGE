
---
title: '5分钟入门Scrum _ Python 主题月'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://picsum.photos/400/300?random=1517'
author: 掘金
comments: false
date: Thu, 22 Jul 2021 19:02:13 GMT
thumbnail: 'https://picsum.photos/400/300?random=1517'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><blockquote>
<p>本文正在参加「Python主题月」，详情查看 <a href="https://juejin.cn/post/6979532761954533390/" target="_blank" title="https://juejin.cn/post/6979532761954533390/">活动链接</a></p>
</blockquote>
<h1 data-id="heading-0">什么是 scrum</h1>
<p><code>scrum</code> 顾名思义就是工作并列进行。在软件项目中，<code>scrum</code> 是敏捷项目管理的一种方式。有人说 <code>scrum</code> 是一种思想，有人说 <code>scrum</code> 是一种框架，其实都不重要，重要的是其核心：<code>加速产品交付&提升用户满意度</code>。</p>
<h1 data-id="heading-1">3355 原则</h1>
<p><code>scrum</code> 中有一个 <code>3355</code> 原则是我们需要了解的。</p>
<h3 data-id="heading-2">3 种角色</h3>
<ol>
<li><code>Product Owner（OP）</code></li>
<li><code>Scrum Master（SM）</code></li>
<li><code>Develop Team（DT）</code></li>
</ol>
<p><strong>其中:</strong></p>
<ul>
<li><code>OP</code> 负责产品创意和设计等；</li>
<li><code>SM</code> 是整个团队的服务式 <code>Leader</code>，帮助团队解决问题，组织日常会议等；</li>
<li><code>DT</code> 包含结构，开发，测试，运维等，整个团队互相协助，完成约定的 <code>Sprint</code> 内的任务。</li>
</ul>
<h3 data-id="heading-3">3 中工件（输出）</h3>
<ol>
<li><code>Product Backlog（PB）</code></li>
<li><code>Sprint Backlog（SB）</code></li>
<li><code>Product NewPart（SNP）</code></li>
</ol>
<p><strong>其中:</strong></p>
<ul>
<li><code>PB</code> 为产品代办事项，你可以理解其为原始需求；</li>
<li><code>SB</code> 为迭代待办事项，即 <code>Scrum Master</code> 从 <code>PB</code> 中挑选的当前 <code>Sprint</code> 需要完成的任务列表；</li>
<li><code>SNP</code> 为产品增量，即当前 <code>Sprint</code> 完成后新增的功能，且 SNP 必须达到可发布的状态，当前 <code>Sprint</code> 才算完成。</li>
</ul>
<h3 data-id="heading-4">5 个活动</h3>
<ol>
<li><code>Sprint Lifecicle（SL）</code></li>
<li><code>Sprint Plan Meeting（SPM）</code></li>
<li><code>Sprint Day Meeting（SDM）</code></li>
<li><code>Sprint Check Meeting（SCM）</code></li>
<li><code>Sprint Replay Meeting（SRM）</code></li>
</ol>
<p><strong>其中:</strong></p>
<ul>
<li><code>SL</code> 是 <code>Sprint</code> 生命周期，一般为 <code>1</code> 到 <code>4</code> 周，建议 <code>2</code> 周；</li>
<li><code>SPM</code> 为迭代计划会议，即迭代内容沟通确认和启动；</li>
<li><code>SDM</code> 为迭代每日会议，目的在反馈每日进度和风险；</li>
<li><code>SCM</code> 为迭代评审会议，即在迭代开发中对技术方案，测试用例等进行评审；</li>
<li><code>SRM</code> 为迭代回顾会议，在迭代晚期（含结束）对整个迭代的内容进行回顾和复盘，以实现持续优化的目的。</li>
</ul>
<h3 data-id="heading-5">5 种价值观</h3>
<ol>
<li>承诺</li>
<li>勇气</li>
<li>专注</li>
<li>开放</li>
<li>尊重</li>
</ol>
<p>以上价值观不再赘述，旨在培养团队协作，勇于承担，互相帮助，共创辉煌。</p>
<blockquote>
<p>整个 <code>Scrum</code> 流程贯穿在 <code>5</code> 个活动中，其他的都是促成 <code>Scrum</code> 目标达成的规则和催化剂。</p>
</blockquote>
<h1 data-id="heading-6">总结</h1>
<p><code>Scrum</code> 的迭代内要进行变更等操作，要求非常严格；承诺迭代内的交付量必须完成；考核标准是一个迭代内完成的任务数；交付周期为一个迭代；交付目标是“满足客户的期望”。</p>
<p>总体来说，<code>Scrum</code> 适合成熟的中大型团队，小型团队采用 <code>Scrum</code> 管理会造成不必要的资源耗费。在项目管理中我会建议根据团队和项目的自身情况选择合适的项目管理方式，没有必要盲目随流。</p>
<blockquote>
<p>以上就是今天的全部内容了，感谢您的阅读，我们下节再会。</p>
</blockquote></div>  
</div>
            