
---
title: 'Zinc v0.2.9 发布，轻量级全文索引引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=238'
author: 开源中国
comments: false
date: Mon, 22 Aug 2022 07:36:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=238'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0">Zinc 是一个进行全文索引的搜索引擎，是 Elasticsearch 的轻量级替代品，运行在不到 100 MB 的 RAM 中。它使用 bluge 作为底层索引库。与 elasticsearch 不同，它非常简单且易于操作。</p> 
<p style="margin-left:0">目前 Zinc v0.2.9 发布了，此版本带来如下改动：</p> 
<h2>Changelog</h2> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fcommit%2F9873bb951e4c5c1afa935bc3aee7fd927ec45af7" target="_blank">9873bb9</a> 将 github.com/aws/aws-sdk-go-v2/config 从 1.15.15 升级到 1.17.1 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fpull%2F438" target="_blank">#438</a>)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fcommit%2F0dbd6f4f35d67edfeba2937286c28bf2841c4997" target="_blank">0dbd6f4</a> 将 github.com/aws/aws-sdk-go-v2/service/s3 从 1.27.2 升级到 1.27.5 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fpull%2F429" target="_blank">#429</a>)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fcommit%2F79bd60410222756979192235151d7959c7336e1a" target="_blank">79bd604</a> 将 github.com/prometheus/client_golang 从 1.11.1 升级到 1.13.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fpull%2F411" target="_blank">#411</a>)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fcommit%2Fb77c92a47b61b6d0248a240d488e0fa1d9f81f3c" target="_blank">b77c92a</a> 将 github.com/swaggo/gin-swagger 从 1.5.1 升级到 1.5.2 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fpull%2F416" target="_blank">#416</a>)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fcommit%2F22b44578670c37d3294cd1dd25f2fddb60492ca6" target="_blank">22b4457</a> 将 nodata 文本的“正在加载...”修复为“无可用数据”(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fpull%2F400" target="_blank">#400</a>)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fcommit%2Fd6834bef10bbab3ed7fd6aa8f15bbce75aef15cb" target="_blank">d6834be</a> <span style="color:#24292f">访问时刷新索引页面</span> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fpull%2F433" target="_blank">#433</a>)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fcommit%2F30a083bf27fdab97d1e884178da61cd32ca6964f" target="_blank">30a083b</a> 功能：<span style="color:#24292f">为 prometheus 插件添加更多指标</span> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fpull%2F407" target="_blank">#407</a>)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fcommit%2Fda83d470c482ecd4aff7373ff6231d25fda813a1" target="_blank">da83d47</a> fix 错别字 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fpull%2F431" target="_blank">#431</a>)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fcommit%2F14ea0671ee931e1c75679df4a8ca04a06c6da134" target="_blank">14ea067</a> fix: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fissues%2F439" target="_blank">#439</a> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fpull%2F440" target="_blank">#440</a>)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fcommit%2Fa85dea03a48b60ee7610d2fb7710c1bc2be89dec" target="_blank">a85dea0</a> fix：使用模板创建索引 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fpull%2F442" target="_blank">#442</a>)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fcommit%2F197486c3a48c9906e0fe69aae3118594ac5ff7d9" target="_blank">197486c</a> fix: <span style="color:#24292f">不返回空错误</span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fpull%2F418" target="_blank">#418</a>)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fcommit%2F6c66ceec7600ff8660374d33ca692a015780c7f5" target="_blank">6c66cee</a> fix: <span style="color:#24292f">模板不适用于设置</span> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fpull%2F446" target="_blank">#446</a>)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fcommit%2F3b295d877727c3c8f586abc013f7d5dcffb450e2" target="_blank">3b295d8</a> <span style="color:#24292f">实现 es 别名 api </span> (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fpull%2F409" target="_blank">#409</a>)</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fcommit%2Fb493a71d8a6c07a9d31eeea60a714184191dfbde" target="_blank">b493a71</a> <span style="color:#24292f">使最大文档大小可配置。</span>(<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Fpull%2F426" target="_blank">#426</a>)</li> 
</ul> 
<p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fzinclabs%2Fzinc%2Freleases%2Ftag%2Fv0.2.9" target="_blank">https://github.com/zinclabs/zinc/releases/tag/v0.2.9</a></p>
                                        </div>
                                      
</div>
            