
---
title: 'Apache Pulsar 生态项目 Kafka-on-Pulsar 发布 2.8.1 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8825'
author: 开源中国
comments: false
date: Mon, 13 Sep 2021 13:54:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8825'
---

<div>   
<div class="content">
                                                                                            <div> 
 <p><strong>关于 Apache Pulsar</strong></p> 
 <p>Apache Pulsar 是 Apache 软件基金会顶级项目，是下一代云原生分布式消息流平台，集消息、存储、轻量化函数式计算为一体，采用计算与存储分离架构设计，支持多租户、持久化存储、多机房跨区域数据复制，具有强一致性、高吞吐以及低延时的高可扩展流数据存储特性。</p> 
 <p><strong>关于 KoP</strong></p> 
 <p>“KoP“（Kafka on Pulsar）由 StreamNative 和 OVHcloud 共同开源，主要满足想要从 Kafka 应用程序切换到 Pulsar 的用户的强烈需求。</p> 
 <p>KoP 将 Kafka 协议处理插件引入 Pulsar broker，从而实现 Apache Pulsar 对原生 Apache Kafka 协议的支持。将 KoP 协议处理插件添加到现有 Pulsar 集群后，<strong>用户不用修改代码就可以将现有的 Kafka 应用程序和服务迁移到 Pulsar，从而使用 Pulsar 的强大功能</strong>，例如：</p> 
</div> 
<div>
 •利用企业级多租户特性简化运营；
 <br> •避免数据搬迁，简化操作；
 <br> •利用 Apache BookKeeper 和分层存储持久保留事件流；
 <br> •利用 Pulsar Functions 进行无服务器化事件处理。
</div> 
<div>
  
</div> 
<div>
 KoP 2.8.1 版本 KoP 2.8.1 发布了，主要有三个方面的更新：
</div> 
<ul> 
 <li>支持 Kafka 0.10 客户端</li> 
 <li>支持 Authorization</li> 
 <li>支持 entryFormat 为 Kafka 的情况下 Pulsar producer 和 Kafka consumer 的交互（反向的交互正在 Pulsar 端进行修改）</li> 
</ul> 
<p>bug 修复与其它 feature 请参考<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fstreamnative%2Fkop%2Freleases%2Ftag%2Fv2.8.1.0" target="_blank"> release note</a> 。大力感谢开发者的支持。</p>
                                        </div>
                                      
</div>
            