
---
title: 'Apache Pulsar 2.7.1 发布，云原生分布式消息流平台'
categories: 
 - 编程
 - 开源中国
 - — 资讯
headimg: ''
author: 开源中国
comments: false
date: Tue, 23 Mar 2021 09:10:00 GMT
thumbnail: ''
---

<div>   
<div class="content">
                                                                                            <p><span style="color:null"><span style="background-color:null">Apache Pulsar 是 Apache 软件基金会顶级项目，是下一代云原生分布式消息流平台，集消息、存储、轻量化函数式计算为一体，采用计算与存储分离架构设计，支持多租户、持久化存储、多机房跨区域数据复制，具有强一致性、高吞吐、低延时及高可扩展性等流数据存储特性。</span></span><br> <span style="color:#505050"><span style="background-color:null">GitHub 地址：</span></span><span style="color:#0080ff"><span style="background-color:null">http://github.com/apache/pulsar/</span></span></p> 
<h1><span style="color:null">新版本特性</span></h1> 
<h2><span style="color:null">Broker</span></h2> 
<ul> 
 <li><span style="color:null">修复获取主题策略时未检查主题所有权的问题；</span></li> 
 <li> <p>修复一旦达到 maxSubscriptionsPerTopic 的限制，则无法为较旧的订阅创建 consumer 的问题；</p> </li> 
 <li> <p>Schema 比较逻辑更改；</p> </li> 
</ul> 
<p>等等。</p> 
<h2>Proxy</h2> 
<ul> 
 <li>修复proxy 配置 bindAddress 不适用于 servicePort 的问题；</li> 
 <li>从 proxy 返回正确的身份验证和身份验证错误到客户端；</li> 
 <li>修复元数据设置兼容性问题；</li> 
</ul> 
<p>等等。</p> 
<h2>Pulsar Admin</h2> 
<ul> 
 <li>验证卸载参数；</li> 
 <li>未执行过期消息请求时通知用户；</li> 
 <li>按位置过期消息；</li> 
</ul> 
<p>等等。</p> 
<h2>Client</h2> 
<ul> 
 <li>[Java] 将消息发布到死信 topic 时添加原始信息；</li> 
 <li>[Java] 修复空 topic 的hasMessageAvailable();</li> 
 <li>[Java] 将 BouncyCastleProvider 添加为安全提供程序以防止 NPE;</li> 
 <li>[C ++] 在 commands.newproducer() 中添加“加密”选项;</li> 
 <li>[C ++] 删除 MultiTopicsConsumerImpl 的 namespace 检查;</li> 
 <li>[C ++] 将损坏的复制消息修复到特定群集;</li> 
 <li>[Python] 支持 python 端到端加密;</li> 
 <li>[Websocket] 修复初始序列 ID 错误;</li> 
</ul> 
<p>等等。</p>
                                        </div>
                                      
</div>
            