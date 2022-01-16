
---
title: 'Elasticsearch 7.16.3 发布，升级到 log4j 2.17.1'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4999'
author: 开源中国
comments: false
date: Sun, 16 Jan 2022 07:33:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4999'
---

<div>   
<div class="content">
                                                                                            <p><span style="color:#333333">Elasticsearch 是一个基于 Lucene 库的搜索引擎。它提供了一个分布式、支持多租户的全文搜索引擎，具有 HTTP Web 接口和无模式 JSON 文档。Elasticsearch 是用 Java 开发的，并在 Apache 许可证下作为开源软件发布。官方客户端在 Java、.NET（C#）、PHP、Python、Apache Groovy、Ruby 和许多其他语言中都是可用的。</span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Elasticsearch 7.16.3 现已发布，具体更新内容如下：</p> 
<h4><strong>Enhancements</strong></h4> 
<div> 
 <p><strong>Security</strong></p> 
 <p> </p> 
 <div> 
  <div> 
   <ul> 
    <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>为 fleet-server 服务账户添加“maintenance”权限<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F82125" target="_blank">#82125</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   </ul> 
  </div> 
 </div> 
 <h4><strong><span><span><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>Bug 修复</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></h4> 
 <div> 
  <p><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span><strong>Authorization</strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
  <div> 
   <ul> 
    <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>修复 docs 和 role<code>field_security</code>的错误消息 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F81283" target="_blank">#81283</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   </ul> 
  </div> 
  <p><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span><strong>Infra/Scripting</strong></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
  <div> 
   <ul> 
    <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>从 lambdas 内的块中跟踪这个指针的捕获情况 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F82228" target="_blank">#82228</a>（</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><span style="background-color:#ffffff; color:#212529">issue</span><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fissues%2F82224" target="_blank">#82224</a>）</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   </ul> 
  </div> 
 </div> 
 <h4><strong><span><span><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>升级</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></strong></h4> 
 <div> 
  <p><strong>Infra/Logging</strong></p> 
  <div> 
   <ul> 
    <li><span><span><span><span style="color:#212529"><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span><span><span>升级到 log4j 2.17.1 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Felastic%2Felasticsearch%2Fpull%2F82111" target="_blank">#82111</a></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></li> 
   </ul> 
  </div> 
 </div> 
</div> 
<p>更新说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.elastic.co%2Fguide%2Fen%2Felasticsearch%2Freference%2F7.16%2Frelease-notes-7.16.3.html" target="_blank">https://www.elastic.co/guide/en/elasticsearch/reference/7.16/release-notes-7.16.3.html</a> </p>
                                        </div>
                                      
</div>
            