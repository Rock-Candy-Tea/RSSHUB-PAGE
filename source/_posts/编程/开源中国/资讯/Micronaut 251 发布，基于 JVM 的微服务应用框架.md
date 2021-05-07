
---
title: 'Micronaut 2.5.1 发布，基于 JVM 的微服务应用框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7745'
author: 开源中国
comments: false
date: Fri, 07 May 2021 07:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7745'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Micronaut 是 Grails 框架作者打造的开源项目，也是新一代基于 JVM 的全栈微服务框架，用于构建模块化的、易于测试的微服务应用。有关 Micronaut 的特性介绍<a href="https://www.oschina.net/news/96381/micronaut-open-sourced">点此查看</a>。</p> 
<p>近日，Micronaut 2.5.1 正式发布，本次更新内容如下：</p> 
<ul> 
 <li>将 micronaut-jms 升级至 1.0.0.M2 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5385" target="_blank">#5385</a>)</li> 
 <li>小幅性能优化 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5384" target="_blank">#5384</a>)</li> 
 <li>改善 Bean context 的启动性能 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5352" target="_blank">#5352</a>)</li> 
 <li>将 micronaut-gcp 升级至 3.5.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5380" target="_blank">#5380</a>)</li> 
 <li>将 micronaut-cache 升级至 2.4.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5355" target="_blank">#5355</a>)</li> 
 <li>确保可重复父类的成员被添加到注释元数据中 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5362" target="_blank">#5362</a>)</li> 
 <li>修复 map 键的列表值没有被添加到目录中 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5363" target="_blank">#5363</a>)</li> 
 <li>如果没有状态路由存在，则在 Stream body 中进行错误响应 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5365" target="_blank">#5365</a>)</li> 
 <li>修复包中带有大写字母的 Beans (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5367" target="_blank">#5367</a>)</li> 
 <li>更正 micronaut-validation native-image 配置的位置 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5377" target="_blank">#5377</a>)</li> 
 <li>将 micronaut-data 升级至 2.4.2 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5373" target="_blank">#5373</a>)</li> 
 <li>将 micronaut-kafka 升级至 3.3.1 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5372" target="_blank">#5372</a>)</li> 
 <li>升级至 Gradle 7.0 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5364" target="_blank">#5364</a>)</li> 
 <li>修正了拦截器的误导性文档 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5358" target="_blank">#5358</a>)</li> 
 <li>Bean introspection: 在一个字段中存储构造函数参数，而不是重新创建数组 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5335" target="_blank">#5335</a>)</li> 
 <li>重构 reactive routing（反应式路由） (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5329" target="_blank">#5329</a>)</li> 
 <li>创建 Netty socket 实例而不是使用 reflection 来创建 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5354" target="_blank">#5354</a>)</li> 
 <li>减少 <code>stream</code> 使用 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5333" target="_blank">#5333</a>)</li> 
 <li>将 micronaut-coherence 升级至 1.0.0.M2 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Fpull%2F5347" target="_blank">#5347</a>)</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fmicronaut-projects%2Fmicronaut-core%2Freleases%2Ftag%2Fv2.5.1" target="_blank">https://github.com/micronaut-projects/micronaut-core/releases/tag/v2.5.1</a></p>
                                        </div>
                                      
</div>
            