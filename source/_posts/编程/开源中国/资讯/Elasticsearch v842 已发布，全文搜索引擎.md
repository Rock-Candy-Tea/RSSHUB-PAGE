
---
title: 'Elasticsearch v8.4.2 已发布，全文搜索引擎'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3664'
author: 开源中国
comments: false
date: Thu, 22 Sep 2022 07:06:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3664'
---

<div>   
<div class="content">
                                                                                            <div> 
 <div> 
  <div> 
   <p style="margin-left:0px">Elasticsearch 是一个基于 Lucene 库的搜索引擎。它提供了一个分布式、支持多租户的全文搜索引擎，具有 HTTP Web 接口和无模式 JSON 文档。Elasticsearch 基于 Java 开发，并在 SSPL + Elastic License 双重授权许可下作为开源软件发布。</p> 
   <p>Elasticsearch 8.4.2 现已发布，该版本更新内容如下：</p> 
   <h3 style="margin-left:0px"><strong>Bug修复</strong></h3> 
   <p><strong>分配</strong></p> 
   <ul> 
    <li>修复 <code>MaxRetryAllocationDecider</code> 中的调试模式<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F89973" target="_blank">#89973</a></li> 
   </ul> 
   <p><strong>验证</strong></p> 
   <ul> 
    <li>修复 <code>TransportOpenIdConnectPrepareAuthenticationAction</code> 中重复发送响应的问题<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F89930" target="_blank">#89930</a></li> 
   </ul> 
   <p><strong>自动缩放</strong></p> 
   <ul> 
    <li>修复克隆或拆分后自动缩放的问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F89768" target="_blank">#89768</a>（问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F89758" target="_blank">#89758</a>）</li> 
   </ul> 
   <p><span style="color:#212529"><strong>Health</strong></span></p> 
   <ul> 
    <li>修复获取远程 master 历史记录的条件 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F89472" target="_blank">#89472</a>（issue : <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F89431" target="_blank">#89431</a>）</li> 
   </ul> 
   <p><span style="color:#212529"><strong>ILM+SLM</strong></span></p> 
   <ul> 
    <li>在 ILM 别名交换期间复制 <code>isHidden</code> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F89650" target="_blank">#89650</a>（问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F89604" target="_blank">#89604</a>）</li> 
   </ul> 
   <p><strong>基础设施/核心</strong></p> 
   <ul> 
    <li>将日期舍入逻辑扩展为有条件 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F89693" target="_blank">#89693</a>（问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F89096" target="_blank">#89096</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F58986" target="_blank">#58986</a>）</li> 
    <li>修复 <code>FileSettingsService</code> 挂起错误更新<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F89630" target="_blank"> #89630</a></li> 
    <li>实施修复以终止文件观察程序线程，以避免死锁问题 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F89934" target="_blank">#89934</a></li> 
   </ul> 
   <p><strong>机器学习</strong></p> 
   <ul> 
    <li>修复 <code>TransportDeleteExpiredDataAction</code> 中的内存泄漏  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F89935" target="_blank">#89935</a></li> 
    <li>现有类别匹配时不保留分类标记<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Fml-cpp%2Fpull%2F2398" target="_blank">#2398</a></li> 
   </ul> 
   <p><strong>网络</strong></p> 
   <ul> 
    <li>修复双重调用时的内存泄漏<code>RestChannel.sendResponse</code> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F89873" target="_blank">#89873</a></li> 
   </ul> 
   <p><span style="color:#212529"><strong>Ranking</strong></span></p> 
   <ul> 
    <li>避免使用 <code>cross_fields</code> 类型的负分<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F89016" target="_blank">#89016</a>（问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F44700" target="_blank">#44700</a>）</li> 
   </ul> 
   <p><span style="color:#212529"><strong>Rollup</strong></span></p> 
   <ul> 
    <li>分叉 <code>TransportRollupCapsAction</code> 到管理池<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F89803" target="_blank">#89803</a></li> 
   </ul> 
   <p><strong>搜索</strong></p> 
   <ul> 
    <li>空区间需要从位置 -1 开始 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F89962" target="_blank">#89962</a>（问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F89789" target="_blank">#89789</a>）</li> 
   </ul> 
   <p><strong>转换</strong></p> 
   <ul> 
    <li>调度程序并发修复 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F89716" target="_blank">#89716</a>（问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F88991" target="_blank">#88991</a>）</li> 
   </ul> 
   <h3 style="margin-left:0px"><strong>增强功能</strong></h3> 
   <p><strong>分配</strong></p> 
   <ul> 
    <li>记录从 Web 身份令牌获取凭据的失败尝试 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F88241" target="_blank">#88241</a></li> 
   </ul> 
   <p><strong>健康</strong></p> 
   <ul> 
    <li>将延迟分配诊断案例添加到分片可用性指标 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F89056" target="_blank">#89056</a></li> 
   </ul> 
   <h3 style="margin-left:0px"><strong>升级</strong></h3> 
   <p><strong>打包</strong></p> 
   <ul> 
    <li>将 OpenJDK 更新到 18.0.2.1 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F89535" target="_blank">#89535</a>（问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F89531" target="_blank">#89531</a>）</li> 
   </ul> 
   <p>更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.elastic.co%2Fguide%2Fen%2Felasticsearch%2Freference%2F8.4%2Frelease-notes-8.4.2.html" target="_blank">https://www.elastic.co/guide/en/elasticsearch/reference/8.4/release-notes-8.4.2.html</a></p> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            