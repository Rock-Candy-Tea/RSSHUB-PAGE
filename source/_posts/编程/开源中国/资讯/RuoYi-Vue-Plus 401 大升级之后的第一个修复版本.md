
---
title: 'RuoYi-Vue-Plus 4.0.1 大升级之后的第一个修复版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://images.gitee.com/uploads/images/2021/1112/202137_673ac5d2_1766278.png'
author: 开源中国
comments: false
date: Tue, 01 Mar 2022 10:20:00 GMT
thumbnail: 'https://images.gitee.com/uploads/images/2021/1112/202137_673ac5d2_1766278.png'
---

<div>   
<div class="content">
                                                                                            <h1>更新说明</h1> 
<h3>依赖升级</h3> 
<ul> 
 <li>update springboot 2.6.3 => 2.6.4</li> 
 <li>update hutool 5.7.20 => 5.7.21</li> 
 <li>update qiniu 7.9.2 => 7.9.3</li> 
 <li>update minio 8.3.5 => 8.3.7</li> 
</ul> 
<h3>功能更新</h3> 
<ul> 
 <li>update 图片上传 文件上传 支持并发上传</li> 
 <li>update 组件ImageUpload支持多图同时选择上传</li> 
 <li>udpate 组件fileUpload支持多文件同时选择上传</li> 
 <li>update 优化 R 默认返回 msg</li> 
 <li>update 增加 用户注册 用户类型默认值</li> 
 <li>update 增加用户登出日志</li> 
 <li>update 更新 多用户多设备的注释说明</li> 
 <li>update 优化 是否为管理员的判断</li> 
 <li>update 优化 页面若未匹配到字典标签则返回原字典值</li> 
 <li>update 调整用户登录 将日志调整到最后 防止获取不到用户警告</li> 
 <li>update 优化随机数生成方式 避免容易生成两个相同随机数的问题</li> 
</ul> 
<h3>问题修复</h3> 
<ul> 
 <li>fix 修复代码生成 基于路径生成 路径为空问题</li> 
 <li>fix 恢复误删 @Async 注解线程池配置类</li> 
 <li>fix 修复 minio 适配 https 导致的问题</li> 
 <li>fix 修复分页组件请求两次问题</li> 
</ul> 
<h1 style="margin-left:0; margin-right:0; text-align:start"><span>软件介绍</span></h1> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><span>RuoYi-Vue-Plus 是重写 RuoYi-Vue 针对<span> </span></span><span><code>分布式集群</code></span><span><span> </span>场景全方位升级(不兼容原框架)</span></p> 
</blockquote> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><span>系统演示:<span> </span></span><span><a href="https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/%E7%B3%BB%E7%BB%9F%E6%BC%94%E7%A4%BA?sort_id=4836388"><span>传送门</span></a></span></p> 
</blockquote> 
<table cellspacing="0" class="md-table" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; border:none; box-sizing:border-box; break-inside:auto; color:#444444; cursor:text; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px !important; max-width:100%; orphans:2; overflow:auto; padding:0px; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:pre-wrap; widows:2; width:800px; word-break:initial; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th><span><span>功能介绍</span></span></th> 
   <th><span><span>使用技术</span></span></th> 
   <th><span><span>文档地址</span></span></th> 
   <th><span><span>特性注意事项</span></span></th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>当前框架</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>RuoYi-Vue-Plus</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span><a href="https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/pages"><span>RuoYi-Vue-Plus文档</span></a></span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>重写RuoYi-Vue全方位升级(不兼容原框架)</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>微服务分支</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>RuoYi-Cloud-Plus</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span><a href="https://gitee.com/JavaLionLi/RuoYi-Cloud-Plus"><span>微服务分支地址</span></a></span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>重写RuoYi-Cloud全方位升级(不兼容原框架)</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>单体分支</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>RuoYi-Vue-Plus-fast</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span><a href="https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/tree/fast/"><span>fast分支地址</span></a></span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>单体应用结构</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>Vue3分支</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>RuoYi-Vue-Plus-UI</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span><a href="https://gitee.com/JavaLionLi/RuoYi-Vue-Plus-UI"><span>UI地址</span></a></span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>由于组件还未完善 仅供学习</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>原框架</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>RuoYi-Vue</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fruoyi.vip%2F" target="_blank"><span>RuoYi-Vue官网</span></a></span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>定期同步需要的功能</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>前端开发框架</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>Vue、Element UI</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Felement.eleme.cn%2F%23%2Fzh-CN" target="_blank"><span>Element UI官网</span></a></span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>后端开发框架</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>SpringBoot</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fspring.io%2Fprojects%2Fspring-boot%2F%23learn" target="_blank"><span>SpringBoot官网</span></a></span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>容器框架</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>Undertow</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fundertow.io%2F" target="_blank"><span>Undertow官网</span></a></span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>基于 XNIO 的高性能容器</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>权限认证框架</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>Sa-Token、Jwt</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsa-token.dev33.cn%2F" target="_blank"><span>Sa-Token官网</span></a></span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>强解耦、强扩展</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>关系数据库</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>MySQL</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdev.mysql.com%2F" target="_blank"><span>MySQL官网</span></a></span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>适配 8.X 最低 5.7</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>缓存数据库</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>Redis</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fredis.io%2F" target="_blank"><span>Redis官网</span></a></span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>适配 6.X 最低 4.X</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>数据库框架</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>Mybatis-Plus</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fbaomidou.com%2Fguide%2F" target="_blank"><span>Mybatis-Plus文档</span></a></span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>快速 CRUD 增加开发效率</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>数据库框架</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>p6spy</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fp6spy.readthedocs.io%2F" target="_blank"><span>p6spy官网</span></a></span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>更强劲的 SQL 分析</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>多数据源框架</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>dynamic-datasource</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.kancloud.cn%2Ftracy5546%2Fdynamic-datasource%2Fcontent" target="_blank"><span>dynamic-ds文档</span></a></span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>支持主从与多种类数据库异构</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>序列化框架</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>Jackson</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FFasterXML%2Fjackson" target="_blank"><span>Jackson官网</span></a></span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>统一使用 jackson 高效可靠</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>Redis客户端</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>Redisson</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredisson%2Fredisson%2Fwiki%2F%25E7%259B%25AE%25E5%25BD%2595" target="_blank"><span>Redisson文档</span></a></span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>支持单机、集群配置</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>分布式限流</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>Redisson</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredisson%2Fredisson%2Fwiki%2F%25E7%259B%25AE%25E5%25BD%2595" target="_blank"><span>Redisson文档</span></a></span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>全局、请求IP、集群ID 多种限流</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>分布式队列</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>Redisson</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fredisson%2Fredisson%2Fwiki%2F%25E7%259B%25AE%25E5%25BD%2595" target="_blank"><span>Redisson文档</span></a></span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>普通队列、延迟队列、优先队列 等</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>分布式锁</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>Lock4j</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span><a href="https://gitee.com/baomidou/lock4j"><span>Lock4j官网</span></a></span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>注解锁、工具锁 多种多样</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>分布式幂等</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>Redisson</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span><a href="https://gitee.com/baomidou/lock4j"><span>Lock4j文档</span></a></span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>拦截重复提交</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>分布式日志</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>TLog</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fyomahub.com%2Ftlog%2Fdocs" target="_blank"><span>TLog文档</span></a></span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>支持跟踪链路日志记录、性能分析、链路排查</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>分布式任务调度</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>Xxl-Job</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.xuxueli.com%2Fxxl-job%2F" target="_blank"><span>Xxl-Job官网</span></a></span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>高性能 高可靠 易扩展</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>文件存储</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>Minio</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.min.io%2F" target="_blank"><span>Minio文档</span></a></span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>本地存储</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>文件存储</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>七牛、阿里、腾讯</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span><a href="https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/pages?sort_id=4359146&doc_id=1469725"><span>OSS使用文档</span></a></span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>云存储</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>监控框架</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>SpringBoot-Admin</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fcodecentric.github.io%2Fspring-boot-admin%2Fcurrent%2F" target="_blank"><span>SpringBoot-Admin文档</span></a></span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>全方位服务监控</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>校验框架</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>Validation</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.jboss.org%2Fhibernate%2Fstable%2Fvalidator%2Freference%2Fen-US%2Fhtml_single%2F" target="_blank"><span>Validation文档</span></a></span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>增强接口安全性、严谨性 支持国际化</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>Excel框架</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>Alibaba EasyExcel</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.yuque.com%2Feasyexcel%2Fdoc%2Feasyexcel" target="_blank"><span>EasyExcel文档</span></a></span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>性能优异 扩展性强</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>文档框架</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>Knife4j</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdoc.xiaominfo.com%2Fknife4j%2Fdocumentation%2F" target="_blank"><span>Knife4j文档</span></a></span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>美化接口文档</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>工具类框架</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>Hutool、Lombok</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.hutool.cn%2Fdocs%2F" target="_blank"><span>Hutool文档</span></a></span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>减少代码冗余 增加安全性</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>代码生成器</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>适配MP、Knife4j规范化代码</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.hutool.cn%2Fdocs%2F" target="_blank"><span>Hutool文档</span></a></span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>一键生成前后端代码</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>部署方式</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>Docker</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.docker.com%2F" target="_blank"><span>Docker文档</span></a></span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>容器编排 一键部署业务集群</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>国际化</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>SpringMessage</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdocs.spring.io%2Fspring-framework%2Fdocs%2Fcurrent%2Freference%2Fhtml%2Fweb.html%23mvc" target="_blank"><span>SpringMVC文档</span></a></span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>Spring标准国际化方案</span></span></td> 
  </tr> 
 </tbody> 
</table> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span>参考文档</span></h2> 
<p style="color:#333333; margin-left:20px; margin-right:0; text-align:start"><span>使用框架前请仔细阅读文档重点注意事项</span></p> 
<blockquote> 
 <p><span><a href="https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/%E5%85%B3%E4%BA%8E%E5%88%9D%E5%A7%8B%E5%8C%96%E9%A1%B9%E7%9B%AE?sort_id=4164117"><span>初始化项目 必看</span></a></span></p> 
 <blockquote> 
  <p style="margin-left:0; margin-right:0"><span><a href="https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/%E5%85%B3%E4%BA%8E%E5%88%9D%E5%A7%8B%E5%8C%96%E9%A1%B9%E7%9B%AE?sort_id=4164117"><span>https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/关于初始化项目?sort_id=4164117</span></a></span></p> 
 </blockquote> 
 <p style="margin-left:20px; margin-right:0"><span><a href="https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/%E5%85%B3%E4%BA%8E%E5%BA%94%E7%94%A8%E9%83%A8%E7%BD%B2?sort_id=4219382"><span>部署项目 必看</span></a></span></p> 
 <blockquote> 
  <p style="margin-left:0; margin-right:0"><span><a href="https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/%E5%85%B3%E4%BA%8E%E5%BA%94%E7%94%A8%E9%83%A8%E7%BD%B2?sort_id=4219382"><span>https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/关于应用部署?sort_id=4219382</span></a></span></p> 
 </blockquote> 
 <p style="margin-left:20px; margin-right:0"><span><a href="https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/pages"><span>参考文档 Wiki</span></a></span></p> 
 <blockquote> 
  <p style="margin-left:0; margin-right:0"><span><a href="https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/pages"><span>https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/pages</span></a></span></p> 
 </blockquote> 
</blockquote> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span>软件架构图</span></h2> 
<p style="color:#333333; margin-left:20px; margin-right:0; text-align:start"><span><img alt="Plus部署架构图" src="https://images.gitee.com/uploads/images/2021/1112/202137_673ac5d2_1766278.png" referrerpolicy="no-referrer"></span></p> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span>贡献代码</span></h2> 
<p style="color:#333333; margin-left:20px; margin-right:0; text-align:start"><span>欢迎各路英雄豪杰<span> </span></span><span><code>PR</code></span><span><span> </span>代码 请提交到<span> </span></span><span><code>dev</code></span><span><span> </span>开发分支 统一测试发版</span></p> 
<p style="color:#333333; margin-left:20px; margin-right:0; text-align:start"><span>框架定位为<span> </span></span><span><code>通用后台管理系统(分布式集群强化)</code></span><span><span> </span>原则上不接受业务<span> </span></span><span><code>PR</code></span></p> 
<h3 style="margin-left:0; margin-right:0; text-align:start"><span>其他</span></h3> 
<ul style="list-style-type:disc; margin-left:20px; margin-right:0"> 
 <li> <p><span>同步升级 RuoYi-Vue</span></p> </li> 
 <li> <p><span>GitHub 地址<span> </span></span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJavaLionLi%2FRuoYi-Vue-Plus" target="_blank"><span>RuoYi-Vue-Plus-github</span></a></span></p> </li> 
 <li> <p><span>单模块 分支<span> </span></span><span><a href="https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/tree/fast/"><span>RuoYi-Vue-Plus-fast</span></a></span></p> </li> 
 <li> <p><span>微服务 分支<span> </span></span><span><a href="https://gitee.com/JavaLionLi/RuoYi-Cloud-Plus"><span>RuoYi-Cloud-Plus</span></a></span></p> </li> 
 <li> <p><span>用户扩展项目<span> </span></span><span><a href="https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/pages?sort_id=4478302&doc_id=1469725"><span>扩展项目列表</span></a></span></p> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:start"><span>业务功能</span></h2> 
<table cellspacing="0" class="md-table" style="-webkit-text-stroke-width:0px; background-color:#ffffff; border-collapse:collapse; border-spacing:0px; border:none; box-sizing:border-box; break-inside:auto; color:#444444; cursor:text; display:block; font-family:-apple-system,BlinkMacSystemFont,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol","Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:14px; font-style:normal; font-variant-caps:normal; font-variant-ligatures:normal; font-weight:400; letter-spacing:normal; line-height:inherit; margin:0px !important; max-width:100%; orphans:2; overflow:auto; padding:0px; text-align:left; text-decoration-color:initial; text-decoration-style:initial; text-decoration-thickness:initial; text-transform:none; white-space:pre-wrap; widows:2; width:800px; word-break:initial; word-spacing:0px"> 
 <thead> 
  <tr> 
   <th><span><span>功能</span></span></th> 
   <th><span><span>介绍</span></span></th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>用户管理</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>用户是系统操作者，该功能主要完成系统用户配置。</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>部门管理</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>配置系统组织机构（公司、部门、小组），树结构展现支持数据权限。</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>岗位管理</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>配置系统用户所属担任职务。</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>菜单管理</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>配置系统菜单，操作权限，按钮权限标识等。</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>角色管理</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>角色菜单权限分配、设置角色按机构进行数据范围权限划分。</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>字典管理</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>对系统中经常使用的一些较为固定的数据进行维护。</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>参数管理</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>对系统动态配置常用参数。</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>通知公告</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>系统通知公告信息发布维护。</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>操作日志</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>系统正常操作日志记录和查询；系统异常信息日志记录和查询。</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>登录日志</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>系统登录日志记录查询包含登录异常。</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>文件管理</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>系统文件上传、下载等管理。</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>定时任务</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>在线（添加、修改、删除)任务调度包含执行结果日志。</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>代码生成</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>前后端代码的生成（java、html、xml、sql）支持CRUD下载 。</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>系统接口</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>根据业务代码自动生成相关的api接口文档。</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>服务监控</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>监视集群系统CPU、内存、磁盘、堆栈、在线日志、Spring相关配置等。</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>缓存监控</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>对系统的缓存信息查询，命令统计等。</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>在线构建器</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>拖动表单元素生成相应的HTML代码。</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>连接池监视</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>监视当前系统数据库连接池状态，可进行分析SQL找出系统性能瓶颈。</span></span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>使用案例</span></span></td> 
   <td style="border-color:#dfe2e5; border-style:solid; border-width:1px"><span><span>系统的一些功能案例</span></span></td> 
  </tr> 
 </tbody> 
</table> 
<p> </p>
                                        </div>
                                      
</div>
            