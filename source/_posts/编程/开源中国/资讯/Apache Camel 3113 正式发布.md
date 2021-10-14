
---
title: 'Apache Camel 3.11.3 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1513'
author: 开源中国
comments: false
date: Thu, 14 Oct 2021 07:20:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1513'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Apache Camel 3.11.3 现已发布。Apache Camel 是一个开源的面向消息的中间件框架，它有一个基于规则的路由和调解引擎，提供了一个基于 Java 对象的企业集成模式的实现，使用应用编程接口来配置路由和调解规则。在面向服务的架构项目中，Camel 经常与 Apache ServiceMix、Apache ActiveMQ 和 Apache CXF 一起使用。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>主要更新内容</strong></p> 
<ul> 
 <li style="text-align:left">bug 修复 
  <ul> 
   <li style="text-align:left">camel-rest-openapi - 端点查询参数未转发到底层组件端点</li> 
   <li style="text-align:left">Camel-AWS2-S3：当 includeBody 为 false 时，不应设置消息 Body</li> 
   <li style="text-align:left">Camel-Github：StartingSha 应该是一个 URI 参数而不是一个 URI 路径</li> 
   <li style="text-align:left">camel-metrics - 由于混合 jackson JAR，不能开箱即用</li> 
   <li style="text-align:left">camel-servlet - Camel 更新后 REST 服务出现问题 - 自定义 servletName 不起作用</li> 
   <li style="text-align:left">camel-ssh - 生产者不应该是单子的</li> 
   <li style="text-align:left">okStatusCodeRange 不允许单个状态代码</li> 
   <li style="text-align:left">camel-aws2-lambda：GetAlias 不工作</li> 
   <li style="text-align:left">camel-servlet - 将正文读入流缓存时不应关闭 HttpServletInputStream</li> 
   <li style="text-align:left">camel-core - 流缓存检查引起的异常可能导致转换器问题</li> 
   <li style="text-align:left">NettyHttpHelper 在 CamelHttpPath 为空的情况下将斜杠附加到 URI</li> 
   <li style="text-align:left">camel-aws2-s3：未设置 CONTENT-MD5 标头，这会用对象锁破坏 putObject</li> 
   <li style="text-align:left">升级到 Camel 3.11.0 后。使用聚合器时无法写入 HttpServletResponse。</li> 
   <li style="text-align:left">使用camel-ftp进行并行处理的camel拆分true会消耗大量堆空间</li> 
   <li style="text-align:left">Camel-InfluxDB：每次执行生产者操作时不要检查数据库是否存在</li> 
   <li style="text-align:left">camel-salesforce：事务内的任何 salesforce 操作超时</li> 
   <li style="text-align:left">支持从骆驼上下文中禁用骆驼 servlet 中的流缓存</li> 
  </ul> </li> 
 <li style="text-align:left">改进 
  <ul> 
   <li style="text-align:left">性能/分析：避免在 EventHelper 中进行布尔分配</li> 
   <li style="text-align:left">camel-ftp - 断开连接应该忽略任何类型的异常</li> 
   <li style="text-align:left">不再捆绑 Atlasmap DFDL 模块</li> 
   <li style="text-align:left">camel-mina - MinaProducer 不会在超时时断开连接</li> 
   <li style="text-align:left">camel-restdsl 插件没有为 xml 和 yaml 实现所有记录的参数</li> 
  </ul> </li> 
</ul> 
<p style="color:#333333; margin-left:0px; margin-right:0px; text-align:left">详情请查看<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmail-archives.apache.org%2Fmod_mbox%2Fwww-announce%2F202110.mbox%2F%253CCADL1oAp5ztkiPLotzyCRqBw13ZwXqt%3D%3D94YhcW1kuF22WX%2BAyw%40mail.gmail.com%253E" target="_blank">更新公告</a>。</p> 
<p> </p>
                                        </div>
                                      
</div>
            