
---
title: '用 Java？试试国产轻量的 Solon v1.10.1'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7633'
author: 开源中国
comments: false
date: Wed, 24 Aug 2022 09:17:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7633'
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
 <li>插件 sqltoy-solon-plugin 升级 sqltoy 为 5.2.9</li> 
 <li>插件 beetlsql-solon-plugin 升级 beetlsql 为 3.18.0</li> 
 <li>插件 solon.auth 增加多账号体系验证支持</li> 
 <li>插件 solon-test 增加 @SolonTest::args 启动参数支持</li> 
 <li>插件 mybatis-solon-plugin 增加数据源 plugins 配置节支持</li> 
 <li>插件 solon.web.staticfiles 增加 WEB-INF/static/ 做为静态文件目录支持（与 static/ 并存，二选一）</li> 
 <li>增加 BeanContainer::subBean 订阅 bean</li> 
 <li>增加 BeanContainer::subWrap 订阅 beanwrap</li> 
 <li>增加 Props::getBean(keyStarts), keyStarts 为空支持</li> 
 <li>增加 NvMap::getBean(clz) 接口支持</li> 
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
            