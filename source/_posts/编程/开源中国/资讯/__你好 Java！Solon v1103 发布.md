
---
title: '__你好 Java！Solon v1.10.3 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6187'
author: 开源中国
comments: false
date: Thu, 22 Sep 2022 00:43:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6187'
---

<div>   
<div class="content">
                                                                                            <h4 style="text-align:start">相对于 Spring Boot 和 Spring Cloud 的项目：</h4> 
<ul> 
 <li>启动快 5 ～ 10 倍。<span> </span><strong>（更快）</strong></li> 
 <li>qps 高 2～ 3 倍。<span> </span><strong>（更高）</strong></li> 
 <li>运行时内存节省 1/3 ~ 1/2。<span> </span><strong>（更少）</strong></li> 
 <li>打包可以缩小到 1/2 ~ 1/10；比如，90Mb 的变成了 9Mb。<span> </span><strong>（更小）</strong></li> 
 <li>基于服务 name 进行注册发现 与 k8s svc 相互对应</li> 
 <li>支持 Service Mesh 架构部署方案</li> 
 <li>支持 jdk8, jdk11, jdk17</li> 
</ul> 
<h4 style="text-align:start">本次更新：</h4> 
<ul> 
 <li>新增 forest-solon-plugin 插件</li> 
 <li>插件 solon.serialization.fastjson2 升级 fastjson2 为：2.0.13</li> 
 <li>插件 qiniu-kodo-solon-plugin 升级 qiniu-java-sdk 为 7.11.0</li> 
 <li>插件 beetlsql-solon-plugin 增加 beetlsql.db1 配置方式构建 SQLManagerBuilder；并增加三个快捷配置</li> 
 <li>插件 solon.cache.jedis 添加 CloudLockServiceJedisImpl 类</li> 
 <li>插件 solon.data 添加 CacheTagsService 接口，提供手动缓存控制便利性</li> 
 <li>插件 qiniu-kodo-solon-plugin 增加 regionId 配置项支持</li> 
 <li>插件 nami 支持接口自己是 Filter，并增加非字符串类型的 pathVar 支持</li> 
 <li>添加 Solon.context() ，Aop 开始标为弃用</li> 
 <li>添加 @Rollback 注解，用于测试时回滚</li> 
 <li>添加 SolonJUnit4ClassRunner 运行的单测，支持动态代理</li> 
 <li>调整 Context.outputAsFile() 自动输出文件长度</li> 
 <li>调整 标注 @Bean::attrs 属性为弃用</li> 
 <li>调整 标注 @Component::attrs 属性为弃用</li> 
 <li>调整 @Init 循环依赖的处理逻辑</li> 
</ul> 
<h4 style="text-align:start">进一步了解 Solon：</h4> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fsolon.noear.org%2Farticle%2Fidea" target="_blank">《想法与架构笔记》</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fsolon.noear.org%2Farticle%2Ffamily-preview" target="_blank">《生态预览》</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fsolon.noear.org%2Farticle%2Fcompare-springboot" target="_blank">《与 Spring Boot 的区别？》</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fsolon.noear.org%2Farticle%2Fcompare-springcloud" target="_blank">《与 Spring Cloud 的区别？》</a></li> 
</ul> 
<h4 style="text-align:start">项目仓库：</h4> 
<ul> 
 <li>gitee：<a href="https://gitee.com/noear/solon">https://gitee.com/noear/solon</a></li> 
 <li>github：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fnoear%2Fsolon" target="_blank">https://github.com/noear/solon</a></li> 
</ul>
                                        </div>
                                      
</div>
            