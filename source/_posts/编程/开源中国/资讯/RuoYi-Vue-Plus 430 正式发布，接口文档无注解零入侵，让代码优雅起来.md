
---
title: 'RuoYi-Vue-Plus 4.3.0 正式发布，接口文档无注解零入侵，让代码优雅起来'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2172'
author: 开源中国
comments: false
date: Wed, 14 Sep 2022 09:38:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2172'
---

<div>   
<div class="content">
                                                                    
                                                        <h1><span>更新日志</span></h1> 
<h3><span>重大更新</span></h3> 
<ul style="list-style-type:disc"> 
 <li> <p>[重大更新] 整合 springdoc 基于 javadoc 实现无注解零入侵生成接口文档</p> </li> 
 <li> <p>[重大更新] 重写 spring-cache 实现 更人性化的操作 支持注解指定ttl等一些参数</p> </li> 
 <li> <p>[不兼容更新] 移除 swagger 所属所有功能 建议使用 springdoc</p> </li> 
 <li> <p>[重大更新] 移除maven docker插件 过于老旧功能缺陷大 使用idea自带的docker插件替代</p> </li> 
</ul> 
<h3><span>依赖升级</span></h3> 
<ul style="list-style-type:disc"> 
 <li> <p>update springboot 2.6.9 => 2.7.3</p> </li> 
 <li> <p>update springboot-admin 2.7.2 => 2.7.4</p> </li> 
 <li> <p>update redisson 3.17.4 => 3.17.6</p> </li> 
 <li> <p>update hutool 5.8.3 => 5.8.6</p> </li> 
 <li> <p>update okhttp 4.9.1 => 4.10.0</p> </li> 
 <li> <p>update lock4j 2.2.1 => 2.2.2</p> </li> 
 <li> <p>update aws-java-sdk-s3 1.12.248 => 1.12.300 修复依赖安全漏洞</p> </li> 
 <li> <p>update aliyun.sms 2.0.9 => 2.0.18</p> </li> 
 <li> <p>update tencent.sms 3.1.537 => 3.1.591</p> </li> 
 <li> <p>update guava 30.0-jre => 31.1-jre</p> </li> 
 <li> <p>update springdoc 1.6.9 => 1.6.11</p> </li> 
 <li> <p>update druid 1.2.11 => 1.2.12</p> </li> 
 <li> <p>update dynamic-ds 3.5.1 => 3.5.2</p> </li> 
</ul> 
<h3><span>功能更新</span></h3> 
<ul style="list-style-type:disc"> 
 <li> <p>update 优化 短信接口实现类 <code>@Override</code> 注解</p> </li> 
 <li> <p>update 优化 登出方法代码逻辑</p> </li> 
 <li> <p>update 优化 代码中的一些魔法值</p> </li> 
 <li> <p>update 优化 使用 StreamUtils 简化业务流操纵</p> </li> 
 <li> <p>update 修改 oss 客户端自定义域名 统一使用https开关控制协议头</p> </li> 
 <li> <p>update 更新 监控过时配置 WebSecurityConfigurerAdapter 改为 bean 注入</p> </li> 
 <li> <p>update 修改 生成错误注释</p> </li> 
 <li> <p>update 优化 docker 部署方式 使用 host 模式简化部署流程 降低使用成本</p> </li> 
 <li> <p>update 修改 验证码开关变量名</p> </li> 
 <li> <p>update 优化 DateColumn 支持单模板多key场景</p> </li> 
 <li> <p>update 优化 redission 处理增加前缀</p> </li> 
 <li> <p>update 优化 缓存监控 相关代码</p> </li> 
 <li> <p>update 优化 部署脚本 防止出现权限问题</p> </li> 
 <li> <p>update 优化 多个相同角色数据导致权限SQL重复问题</p> </li> 
 <li> <p>update 优化 字典数据使用store存取</p> </li> 
 <li> <p>update 优化 布局设置使用el-drawer抽屉显示</p> </li> 
 <li> <p>update 更新框架文档 专栏与视频 链接地址</p> </li> 
 <li> <p>update 优化 OSS文件上传 主动设置文件公共读 适配天翼云OSS</p> </li> 
 <li> <p>update 优化 表格上右侧工具条（搜索按钮显隐&右侧样式凸出）</p> </li> 
 <li> <p>update 优化 前后端多环境部署保持一致 删除无用环境文件</p> </li> 
 <li> <p>update 优化 错误登录锁定与新增解锁功能</p> </li> 
 <li> <p>update 优化 getLoginId 增加必要参数空校验</p> </li> 
 <li> <p>update 使用 SpringCache注解 优化参数管理、字典管理、在线用户等业务缓存</p> </li> 
 <li> <p>update 优化 多角色数据权限匹配规则</p> </li> 
 <li> <p>update 优化 页面内嵌iframe切换tab不刷新数据</p> </li> 
 <li> <p>update 优化 调整 oss表key 与 ossconfig的service 字段长度不匹配</p> </li> 
 <li> <p>update 优化 操作日志密码脱敏</p> </li> 
 <li> <p>update 重构 QueueUtils 抽取通用方法 统一使用 适配优先队列新用法</p> </li> 
</ul> 
<h3><span>新功能</span></h3> 
<ul style="list-style-type:disc"> 
 <li> <p>add 增加 StreamUtils 流工具 简化 stream 流操纵</p> </li> 
 <li> <p>add 新增 缓存列表菜单功能</p> </li> 
 <li> <p>add 新增 获取oss对象元数据方法</p> </li> 
 <li> <p>add 增加 QueueUtils 操作普通队列的方法</p> </li> 
</ul> 
<h3><span>问题修复</span></h3> 
<ul style="list-style-type:disc"> 
 <li> <p>fix 修复 mysql sys_notice 与 sys_config 表主键类型长度不够问题</p> </li> 
 <li> <p>fix 修复 获取 SensitiveService 空问题 增加空兼容</p> </li> 
 <li> <p>fix 修复 代码生成首字母大写问题</p> </li> 
 <li> <p>fix 修复 minio 上传自定义域名回显路径错误问题</p> </li> 
 <li> <p>fix 修复 短信功能返回实体 SysSms 序列化问题</p> </li> 
 <li> <p>fix 修复 sqlserver 更新sql错误提交</p> </li> 
 <li> <p>fix 修复 RedisUtils 并发 set ttl 错误问题</p> </li> 
 <li> <p>fix 修复 防止主键字段名与'row'或'ids'一致导致报错的问题</p> </li> 
 <li> <p>fix 修复 幂等组件 逻辑问题导致线程变量未清除</p> </li> 
 <li> <p>fix 修复 脱敏没有实现类导致返回数据异常问题</p> </li> 
 <li> <p>fix 修复 用户导出字典使用错误</p> </li> 
 <li> <p>fix 修复 用户登录与短信登录 国际化格式不一致</p> </li> 
 <li> <p>fix 修复 BaseMapperPlus 方法命令不一致问题</p> </li> 
 <li> <p>fix 修复 短信功能是否启用判断不生效BUG</p> </li> 
 <li> <p>fix 修复 xxljob prod 环境配置文件 数据库ip漏改</p> </li> 
 <li> <p>fix 修复 部署脚本 cp 命令缺少参数问题</p> </li> 
 <li> <p>fix 修复 菜单管理的一些操作问题</p> </li> 
 <li> <p>fix 修复 国际化文件提交为特殊编码问题</p> </li> 
 <li> <p>fix 修复 minio配置https遇到的问题</p> </li> 
 <li> <p>fix 修复 点击删除后点击取消控制台报错问题</p> </li> 
 <li> <p>fix 修复 文件/图片上传组件 第一次上传报错导致后续上传无限loading问题</p> </li> 
 <li> <p>fix 修复 postgresql 时间查询类型转换报错问题</p> </li> 
 <li> <p>fix 修复 部门与角色 状态导出字典使用错误</p> </li> 
 <li> <p>fix 修复 openapi结构体 因springdoc缓存导致多次拼接接口路径问题</p> </li> 
 <li> <p>fix 修复 没有权限的用户编辑部门缺少数据</p> </li> 
 <li> <p>fix 修复 oss配置删除内部数据id匹配类型问题</p> </li> 
 <li> <p>fix 修复 用户导入存在则更新不生效</p> </li> 
 <li> <p>fix 修复 日志转换非json数据导致报错</p> </li> 
</ul> 
<h2><span>平台简介</span></h2> 
<blockquote> 
 <p style="color:black; margin-left:0; margin-right:0">RuoYi-Vue-Plus 是重写 RuoYi-Vue 针对 <code>分布式集群</code> 场景全方位升级(不兼容原框架)</p> 
</blockquote> 
<blockquote> 
 <p style="color:black; margin-left:0; margin-right:0">项目代码、文档 均开源免费可商用 遵循开源协议在项目中保留开源协议文件即可<br> 活到老写到老 为兴趣而开源 为学习而开源 为让大家真正可以学到技术而开源</p> 
</blockquote> 
<table style="display:table; text-align:left"> 
 <thead> 
  <tr> 
   <th style="background-color:#f0f0f0; text-align:left">功能介绍</th> 
   <th style="background-color:#f0f0f0; text-align:left">使用技术</th> 
   <th style="background-color:#f0f0f0; text-align:left">特性注意事项</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">当前框架</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">RuoYi-Vue-Plus</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">重写RuoYi-Vue全方位升级(不兼容原框架)</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">微服务分支</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">RuoYi-Cloud-Plus</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">重写RuoYi-Cloud全方位升级(不兼容原框架)</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">单体分支</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">RuoYi-Vue-Plus-fast</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">单体应用结构</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Vue3分支</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">RuoYi-Vue-Plus-UI</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">由于组件还未完善 仅供学习</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">原框架</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">RuoYi-Vue</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">定期同步需要的功能</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">前端开发框架</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Vue、Element UI</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">后端开发框架</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">SpringBoot</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left"> </td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">容器框架</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Undertow</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">基于 XNIO 的高性能容器</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">权限认证框架</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Sa-Token、Jwt</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">强解耦、强扩展</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">关系数据库</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">MySQL</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">适配 8.X 最低 5.7</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">关系数据库</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Oracle</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">适配 11g 12c</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">关系数据库</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">PostgreSQL</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">适配 13 14</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">关系数据库</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">SQLServer</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">适配 2017 2019</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">缓存数据库</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Redis</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">适配 6.X 最低 4.X</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">数据库框架</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Mybatis-Plus</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">快速 CRUD 增加开发效率</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">数据库框架</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">p6spy</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">更强劲的 SQL 分析</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">多数据源框架</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">dynamic-datasource</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">支持主从与多种类数据库异构</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">序列化框架</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Jackson</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">统一使用 jackson 高效可靠</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Redis客户端</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Redisson</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">支持单机、集群配置</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">分布式限流</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Redisson</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">全局、请求IP、集群ID 多种限流</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">分布式队列</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Redisson</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">普通队列、延迟队列、优先队列 等</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">分布式锁</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Lock4j</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">注解锁、工具锁 多种多样</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">分布式幂等</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Redisson</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">拦截重复提交</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">分布式日志</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">TLog</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">支持跟踪链路日志记录、性能分析、链路排查</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">分布式任务调度</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Xxl-Job</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">高性能 高可靠 易扩展</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">文件存储</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Minio</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">本地存储</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">文件存储</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">七牛、阿里、腾讯</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">云存储</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">短信模块</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">阿里、腾讯</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">短信发送</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">监控框架</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">SpringBoot-Admin</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">全方位服务监控</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">校验框架</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Validation</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">增强接口安全性、严谨性 支持国际化</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Excel框架</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Alibaba EasyExcel</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">性能优异 扩展性强</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">文档框架</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">SpringDoc、javadoc</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">无注解零入侵基于java注释</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">工具类框架</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Hutool、Lombok</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">减少代码冗余 增加安全性</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">代码生成器</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">适配MP、Knife4j规范化代码</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">一键生成前后端代码</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">部署方式</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Docker</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">容器编排 一键部署业务集群</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">国际化</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">SpringMessage</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">Spring标准国际化方案</td> 
  </tr> 
 </tbody> 
</table> 
<h2><span>参考文档</span></h2> 
<p style="color:black; margin-left:0; margin-right:0">使用框架前请仔细阅读文档重点注意事项</p> 
<blockquote> 
 <p style="color:black; margin-left:0; margin-right:0"><a href="https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/pages?sort_id=4164117&doc_id=1469725">初始化项目 必看</a></p> 
 <blockquote> 
  <p style="color:black; margin-left:0; margin-right:0"><a href="https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/pages?sort_id=4164117&doc_id=1469725">https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/pages?sort_id=4164117&doc_id=1469725</a></p> 
 </blockquote> 
 <p style="color:black; margin-left:0; margin-right:0"><a href="https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/pages?sort_id=5473272&doc_id=1469725">专栏与视频 入门必看</a></p> 
 <blockquote> 
  <p style="color:black; margin-left:0; margin-right:0"><a href="https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/pages?sort_id=5473272&doc_id=1469725">https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/pages?sort_id=5473272&doc_id=1469725</a></p> 
 </blockquote> 
 <p style="color:black; margin-left:0; margin-right:0"><a href="https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/pages?sort_id=4219382&doc_id=1469725">部署项目 必看</a></p> 
 <blockquote> 
  <p style="color:black; margin-left:0; margin-right:0"><a href="https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/pages?sort_id=4219382&doc_id=1469725">https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/pages?sort_id=4219382&doc_id=1469725</a></p> 
 </blockquote> 
 <p style="color:black; margin-left:0; margin-right:0"><a href="https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/pages">参考文档 Wiki</a></p> 
 <blockquote> 
  <p style="color:black; margin-left:0; margin-right:0"><a href="https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/pages">https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/pages</a></p> 
 </blockquote> 
</blockquote> 
<h2><span>业务功能</span></h2> 
<table style="display:table; text-align:left"> 
 <thead> 
  <tr> 
   <th style="background-color:#f0f0f0; text-align:left">功能</th> 
   <th style="background-color:#f0f0f0; text-align:left">介绍</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">用户管理</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">用户是系统操作者，该功能主要完成系统用户配置。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">部门管理</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">配置系统组织机构（公司、部门、小组），树结构展现支持数据权限。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">岗位管理</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">配置系统用户所属担任职务。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">菜单管理</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">配置系统菜单，操作权限，按钮权限标识等。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">角色管理</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">角色菜单权限分配、设置角色按机构进行数据范围权限划分。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">字典管理</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">对系统中经常使用的一些较为固定的数据进行维护。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">参数管理</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">对系统动态配置常用参数。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">通知公告</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">系统通知公告信息发布维护。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">操作日志</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">系统正常操作日志记录和查询；系统异常信息日志记录和查询。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">登录日志</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">系统登录日志记录查询包含登录异常。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">文件管理</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">系统文件上传、下载等管理。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">定时任务</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">在线（添加、修改、删除)任务调度包含执行结果日志。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">代码生成</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">前后端代码的生成（java、html、xml、sql）支持CRUD下载 。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">系统接口</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">根据业务代码自动生成相关的api接口文档。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">服务监控</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">监视集群系统CPU、内存、磁盘、堆栈、在线日志、Spring相关配置等。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">缓存监控</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">对系统的缓存信息查询，命令统计等。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">在线构建器</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">拖动表单元素生成相应的HTML代码。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">连接池监视</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">监视当前系统数据库连接池状态，可进行分析SQL找出系统性能瓶颈。</td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">使用案例</td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px; text-align:left">系统的一些功能案例</td> 
  </tr> 
 </tbody> 
</table>
                                        </div>
                                      
</div>
            