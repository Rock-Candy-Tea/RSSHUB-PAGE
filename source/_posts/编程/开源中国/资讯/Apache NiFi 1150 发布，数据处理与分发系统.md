
---
title: 'Apache NiFi 1.15.0 发布，数据处理与分发系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=362'
author: 开源中国
comments: false
date: Tue, 09 Nov 2021 06:42:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=362'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">Apache NiFi 1.15.0 现已发布。Apache NiFi 是一个易于使用、功能强大而且可靠的数据处理和分发系统。它为数据流设计，支持高度可配置的指示图的数据路由、转换和系统中介逻辑。</span></p> 
<p><span style="background-color:#ffffff; color:#333333"><strong>主要更新内容</strong></span></p> 
<ul> 
 <li><span style="background-color:#ffffff; color:#333333">参数上下文现在支持继承。这使得管理跨多个流使用的通用属性集变得更加容易，并且仅根据给定实例的需要调整特定参数。对于运行相同流程或流程版本的多个实例的 NiFi 用户来说，这种模式非常有价值。</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">NiFi 的 API 现在允许组件提供验证机制，专注于与外部服务对话并通过 REST API 和 NiFi UI 将其返回。</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">无状态 NiFi 非常强大，并且正在出现更多执行它的引擎。并且现在支持在传统的 NiFi 部署中运行无状态 NiFi 流。</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">脚本记录处理器支持高度可定制的路由和分区。</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">实现加密存储库共享配置</span></li> 
 <li><span style="background-color:#ffffff; color:#333333"> 在 UI 的参数上下文视图中添加继承的参数上下文选项卡</span></li> 
 <li><span style="background-color:#ffffff; color:#333333"> 将 KerberosUserService 与 HDFS 处理器集成</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">AttributesToJSON "空值" 描述与实现不匹配</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">MockProcessSession remove() 不报告 "DROP" 出处事件</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">在 InvokeScriptedProcessor 的敏感属性中使用敏感参数会导致 Jetty 在 NiFi 重启时关闭</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">PutElasticsearchRecord 会从文档中删除 ID</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">SFTP KeepAlive 不工作</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">添加新的敏感属性提供程序</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">添加 SignContentPGP 和 VerifyContentPGP 处理器</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">如果完整（多行）消息不可用，则允许 TailFile 推迟摄取文本行</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">向 Confluent Schema Registry 请求添加动态 HTTP 标头</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">UI - 提供 UX 以支持验证配置</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">为 NiFi Toolkit 添加 RPM 配置文件</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">在 PutBigQueryBatch 的属性中添加作业 ID</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">PutElasticsearch/RecordHttp 处理器应该支持 Elasticsearch 数据流</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">Elasticsearch REST 处理器应该允许动态属性作为查询字符串参数</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">使用 REST API 创建新的 Elasticsearch 滚动/分页查询处理器</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">创建 Elasticsearch update_by_query 处理器</span></li> 
 <li><span style="background-color:#ffffff; color:#333333">PutSNS 处理器中的 Amazon SNS FIFO 支持</span></li> 
</ul> 
<p><span style="background-color:#ffffff; color:#333333">详情请查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcwiki.apache.org%2Fconfluence%2Fdisplay%2FNIFI%2FRelease%2BNotes%23ReleaseNotes-Version1.15.0" target="_blank">更新公告</a></span></p>
                                        </div>
                                      
</div>
            