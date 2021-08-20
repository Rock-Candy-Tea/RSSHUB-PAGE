
---
title: 'Micronaut 3.0.0 正式发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7658'
author: 开源中国
comments: false
date: Fri, 20 Aug 2021 06:21:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7658'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Micronaut 是 Grails 框架作者打造的开源项目，也是新一代基于 JVM 的全栈微服务框架，用于构建模块化的、易于测试的微服务应用。有关 Micronaut 的特性介绍<a href="https://www.oschina.net/news/96381/micronaut-open-sourced">点此查看</a>。</p> 
<p>Micronaut 3.0.0 正式版在 3.0.0 RC 1 版本的基础上升级了众多内容，具体更新内容如下：</p> 
<p>Micronaut 3.0.0 RC1 的更新内容可以<a href="https://www.oschina.net/news/155168/micronaut-3-0-0-rc1-released">点击此处查看</a></p> 
<h3>变化：</h3> 
<ul> 
 <li>不要使用已经取消的 emitter (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5987" target="_blank">#5987</a>)</li> 
 <li>升级 Netty 至 4.1.67 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5994" target="_blank">#5994</a>)</li> 
 <li>Pr 5993 rebase (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6004" target="_blank">#6004</a>)</li> 
 <li>当备份数据在磁盘上时，允许对 CompletedFileUpload 返回的输入流进行多次调用关闭 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5982" target="_blank">#5982</a>)</li> 
 <li>build: 将 micronaut-reactor-http-client 添加到 bom (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5976" target="_blank">#5976</a>)</li> 
 <li>build: 将 micronaut-rxjava3-http-client 添加到 bom (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5977" target="_blank">#5977</a>)</li> 
 <li>将 micronaut-kubernetes 升至 3.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6038" target="_blank">#6038</a>)</li> 
 <li>将 micronaut-aws 升至 3.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6037" target="_blank">#6037</a>)</li> 
 <li>将 micronaut-kafka 升至 4.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6036" target="_blank">#6036</a>)</li> 
 <li>将 micronaut-gcp 升至 4.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6035" target="_blank">#6035</a>)</li> 
 <li>将 micronaut-azure 升至 3.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6034" target="_blank">#6034</a>)</li> 
 <li>将 micronaut-oracle-cloud 升至 2.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6033" target="_blank">#6033</a>)</li> 
 <li>将 micronaut-micrometer 升至 4.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6031" target="_blank">#6031</a>)</li> 
 <li>将 micronaut-spring 升至 4.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6032" target="_blank">#6032</a>)</li> 
 <li>将 micronaut-r2dbc 升至 2.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6029" target="_blank">#6029</a>)</li> 
 <li>将 micronaut-sql 升至 4.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6030" target="_blank">#6030</a>)</li> 
 <li>将 micronaut-mongodb 升至 4.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6028" target="_blank">#6028</a>)</li> 
 <li>将 micronaut-reactor 升至 2.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6027" target="_blank">#6027</a>)</li> 
 <li>将 micronaut-rxjava3 升至 2.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6026" target="_blank">#6026</a>)</li> 
 <li>将 micronaut-grpc 升至 3.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6025" target="_blank">#6025</a>)</li> 
 <li>将 micronaut-security 升至 3.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6024" target="_blank">#6024</a>)</li> 
 <li>将 micronaut-redis 升至 5.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6023" target="_blank">#6023</a>)</li> 
 <li>将 micronaut-rxjava2 升至 1.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6022" target="_blank">#6022</a>)</li> 
 <li>将 micronaut-neo4j 升至 5.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6021" target="_blank">#6021</a>)</li> 
 <li>将 micronaut-discovery-client 升至 3.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6020" target="_blank">#6020</a>)</li> 
 <li>将 micronaut-views 升至 3.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6019" target="_blank">#6019</a>)</li> 
 <li>将 micronaut-jmx 升至 3.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6018" target="_blank">#6018</a>)</li> 
 <li>将 micronaut-nats 升至 3.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6017" target="_blank">#6017</a>)</li> 
 <li>将 micronaut-multitenancy 升至 4.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6016" target="_blank">#6016</a>)</li> 
 <li>将 micronaut-servlet 升至 3.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6015" target="_blank">#6015</a>)</li> 
 <li>将 micronaut-test 升至 3.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6014" target="_blank">#6014</a>)</li> 
 <li>将 micronaut-picocli 升至 4.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6013" target="_blank">#6013</a>)</li> 
 <li>将 micronaut-rabbitmq 升至 3.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6012" target="_blank">#6012</a>)</li> 
 <li>将 micronaut-graphql 升至 3.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6010" target="_blank">#6010</a>)</li> 
 <li>将 micronaut-rss 升至 3.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6009" target="_blank">#6009</a>)</li> 
 <li>将 micronaut-elasticsearch 升至 3.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6008" target="_blank">#6008</a>)</li> 
 <li>将 micronaut-mqtt 升至 2.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6007" target="_blank">#6007</a>)</li> 
 <li>将 micronaut-problem-json 升至 2.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6006" target="_blank">#6006</a>)</li> 
 <li>将 micronaut-jaxrs 升至 3.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6005" target="_blank">#6005</a>)</li> 
 <li>将 micronaut-data 升至 3.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6003" target="_blank">#6003</a>)</li> 
 <li>将 micronaut-cache 升至 3.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6002" target="_blank">#6002</a>)</li> 
 <li>将 micronaut-kotlin 升至 3.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6001" target="_blank">#6001</a>)</li> 
 <li>将 micronaut-jackson-xml 升至 3.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F6000" target="_blank">#6000</a>)</li> 
 <li>将 micronaut-acme 升至 3.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5999" target="_blank">#5999</a>)</li> 
 <li>将 micronaut-aws 升至 2.6.2 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5996" target="_blank">#5996</a>)</li> 
 <li>将 micronaut-groovy 升至 3.0.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5983" target="_blank">#5983</a>)</li> 
 <li>将 micronaut-openapi 升至 3.0.1 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5990" target="_blank">#5990</a>)</li> 
 <li>将 micronaut-openapi 升至 2.6.2 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5989" target="_blank">#5989</a>)</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Freleases%2Ftag%2Fv3.0.0" target="_blank">https://github.com/micronaut-projects/micronaut-core/releases/tag/v3.0.0</a></p>
                                        </div>
                                      
</div>
            