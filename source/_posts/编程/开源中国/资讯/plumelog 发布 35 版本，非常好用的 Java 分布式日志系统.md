
---
title: 'plumelog 发布 3.5 版本，非常好用的 Java 分布式日志系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-47109a705cdbcb88937e8444fddb7a9686a.png'
author: 开源中国
comments: false
date: Fri, 12 Nov 2021 01:35:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-47109a705cdbcb88937e8444fddb7a9686a.png'
---

<div>   
<div class="content">
                                                                                            <div style="text-align:left"> 
 <div> 
  <div> 
   <h3 style="margin-left:0; margin-right:0">3.5版本更新内容如下</h3> 
   <ul> 
    <li>增加lite启动模式，此时不需要配置redis和es，lite模式下，扩展字段，错误统计，错误报警都不能使用，适合小规模项目使用</li> 
    <li>增加了plumelog-lite模块，plumelog-lite作为plumelog依赖包的形式存在，直接引用直接使用，无需部署，嵌入到项目中</li> 
    <li>增加日志控制台，查看实时输出情况，在部署和测试时候堪称神器，打开控制台的时候会影响性能，注意使用时机</li> 
    <li>修复了链路追踪，有可能最外层不能显示的bug</li> 
    <li>增加自动检测ES版本，不需要再配置</li> 
    <li>增加自动配置ES最大分片数量，不需要去手动设置</li> 
    <li>优化了界面，优化报警界面出界保存按钮显示一半的bug</li> 
    <li>优化redis模式下配置，如果所有应用只用一个队列redis，管理用redis可以不用配置，会自动启用队列的redis作为管理redis</li> 
    <li>修复已经已知的bug,其他优化</li> 
    <li>老用户升级直接替换plumelog-server-3.5.jar，重启即可</li> 
    <li>lite模式，需要升级客户端到3.5</li> 
    <li>内嵌springboot-admin，方便管理springboot项目，可以利用springbootadmin,动态调整日志输出级别</li> 
   </ul> 
   <p>plumelog是一个轻量级java专业的分布式日志系统，部署简单，吞吐量大，使用方便，包含链路追踪，扩展字段，错误统计，日志错误报警，控制台实时日志等功能，可分布式部署，可单机部署，可嵌入式不是，满足各种项目的使用需求，非java项目也可以通过调用API的方式接入，堪称日志管理神器，使得线上变得透明，查询问题变得更加快捷</p> 
   <p>功能演示视频地址 https://v.qq.com/x/page/g3308uxlcnw.html</p> 
   <p><img height="1694" src="https://oscimg.oschina.net/oscnet/up-47109a705cdbcb88937e8444fddb7a9686a.png" width="3356" referrerpolicy="no-referrer"></p> 
   <p><img height="1544" src="https://oscimg.oschina.net/oscnet/up-3f96c27668a774096e77321fc40138d21d8.png" width="3334" referrerpolicy="no-referrer"></p> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            