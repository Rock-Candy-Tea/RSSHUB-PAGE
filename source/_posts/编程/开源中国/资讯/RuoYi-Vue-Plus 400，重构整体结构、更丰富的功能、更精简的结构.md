
---
title: 'RuoYi-Vue-Plus 4.0.0，重构整体结构、更丰富的功能、更精简的结构'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://images.gitee.com/uploads/images/2021/1112/202137_673ac5d2_1766278.png'
author: 开源中国
comments: false
date: Fri, 18 Feb 2022 10:42:00 GMT
thumbnail: 'https://images.gitee.com/uploads/images/2021/1112/202137_673ac5d2_1766278.png'
---

<div>   
<div class="content">
                                                                                            <h1 style="text-align:start"><span>更新说明</span></h1> 
<h3 style="text-align:start"><span>重大更新</span></h3> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>[重大更新] 重写项目整体结构 数据处理下沉至Mapper符合MVC规范 减少循环依赖</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>[重磅更新] 主分支与satoken分支合并 权限统一使用 sa-token</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>[重磅更新] 适配升级 SpringBoot 2.6</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>[重磅更新] EasyExcel大版本升级3.X</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>[重磅更新] 移除链式调用注解 因链式调用不符合java规范 导致很多问题</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>[重磅更新] 增加 轻量级 分布式队列 支持</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>[重磅更新] 增加 数据脱敏注解 使用序列化控制脱敏 支持多种表达式</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>[重磅更新] 重构 使用 Spring 简化 oss 模块代码</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>[重磅更新] 重构 调整返回类型为 R 精简 Controller 代码</span></p> </li> 
</ul> 
<h3 style="text-align:start"><span>依赖升级</span></h3> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>update springboot 2.5.8 => 2.6.3</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>update mybatis-plus 3.4.3.4 => 3.5.1</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>update maven-jar-plugin 3.2.0 => 3.2.2</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>update maven-war-plugin 3.2.0 => 3.2.2</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>update maven-compiler-plugin 3.1 => 3.9.0</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>update hutool 5.7.18 => 5.7.20</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>update springboot-admin 2.6.0 => 2.6.2</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>update redisson 3.16.7 => 3.16.8</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>update qiniu 7.9.0 => 7.9.2</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>update aliyun 3.13.1 => 3.14.0</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>update qcloud 5.6.58 => 5.6.68</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>update minio 8.3.4 => 8.3.5</span></p> </li> 
</ul> 
<h3 style="text-align:start"><span>功能更新</span></h3> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>update 用户管理部门查询选择节点后分页参数初始</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>update 防重复提交标识组合（key + url + header）</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>update 接口文档增加 basic 账号密码验证</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>update 用户修改减少一次角色列表关联查询</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>update 优化部门修改缩放后出现的错位问题</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>update 指定 maven 资源过滤为具体文件 防止错误过滤</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>update hutool 引入改为 bom 依赖项引入</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>update 降低开发环境 redis连接池数量</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>update 升级 springboot 2.6.X 解决 springfox 兼容性问题</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>update 优化多用户体系处理 更名 LoginUtils 为 LoginHelper 支持 LoginUser 多级缓存</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>update 优化加载字典缓存数据</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>update 数据库更改 对接多用户体系</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>update 移除掉 StringUtils 语义不明确的api方法 使用特定工具替换</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>update 优化登录、注册在接口通过</span><span><code>@Validated</code></span><span>注解进行数据基础校验</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>update 优化 查询登录用户数据 统一走缓存</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>update 优化 redisson 配置 去除掉不常用的配置 使用默认配置</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>update 用户访问控制时校验数据权限，防止越权</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>update 修改用户注册报未登录警告</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>update 调整oss预览开关 使用前端直接调用更改配置参数</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>update 使用 satoken 自带的 BCrypt 工具 替换 Security 加密工具 减少依赖</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>update 优化 TreeBuildUtils 工具 使用反射自动获取顶级父id</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>update 使用 hutool Dict 优化 JsonUtils 防止类型解析异常</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>update 优化代码生成 使用新 JsonUtils.parseMap 方法</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>update 更新 所有 oss 均支持 https 配置</span></p> </li> 
</ul> 
<h3 style="text-align:start"><span>新功能</span></h3> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>add 增加 RedisUtils 工具 hasKey 检查key存在方法</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>add 增加 监控中心 自定义事件通知</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>add 增加 3.X update 4.0 更新sql</span></p> </li> 
</ul> 
<h3 style="text-align:start"><span>问题修复</span></h3> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>fix 修复登录失效后多次请求提示多次弹窗问题</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>fix 修复 StringUtils 通配符匹配无效</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>fix 修复选项卡点击右键刷新丢失参数问题</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>fix 修复 数据权限 缓存方法名错误问题</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>fix 修复自定义组件</span><span><code>file-upload</code></span><span>无法显示第一个文件，列表显示的文件比实际文件少一个的问题</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>fix 修复因升级 sa-token 导致 doLogin 无法获取 token 问题</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>fix 修复分页组件请求两次问题</span></p> </li> 
</ul> 
<h3 style="text-align:start"><span>移除功能</span></h3> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>remove 移除过期代码 分页工具相关</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>remove 移除过期代码 多数据源切换</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>remove 移除过期代码 数据权限</span></p> </li> 
</ul> 
<h3 style="text-align:start"><span>其他</span></h3> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>3.X 版本进入维护阶段 不进行更新 只修复bug 持续维护到2022年10月 </span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>4.X 版本公测将近一个月 大部分bug已修复 官网主分支更改为 4.X 版本 推荐使用</span></p> </li> 
</ul> 
<h1 style="text-align:start"><span>软件介绍</span></h1> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><span>RuoYi-Vue-Plus 是重写 RuoYi-Vue 针对 </span><span><code>分布式集群</code></span><span> 场景全方位升级(不兼容原框架)</span></p> 
</blockquote> 
<blockquote> 
 <p style="margin-left:0; margin-right:0"><span>系统演示: </span><span><a href="https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/%E7%B3%BB%E7%BB%9F%E6%BC%94%E7%A4%BA?sort_id=4836388"><span>传送门</span></a></span></p> 
</blockquote> 
<table cellspacing="0" class="md-table" style="border-collapse:collapse; border-spacing:0px; box-sizing:border-box; break-inside:auto; cursor:text; margin:0px !important; overflow:auto; padding:0px; text-align:left; white-space:pre-wrap; width:800px; word-break:initial"> 
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
<h2 style="text-align:start"><span>参考文档</span></h2> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>使用框架前请仔细阅读文档重点注意事项</span><span> </span><span style="color:#a7a7a7"> </span></p> 
<blockquote> 
 <p style="margin-left:.8em; margin-right:0"><span><a href="https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/%E5%85%B3%E4%BA%8E%E5%88%9D%E5%A7%8B%E5%8C%96%E9%A1%B9%E7%9B%AE?sort_id=4164117"><span>初始化项目 必看</span></a></span></p> 
 <blockquote> 
  <p style="margin-left:0; margin-right:0"><span><a href="https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/%E5%85%B3%E4%BA%8E%E5%88%9D%E5%A7%8B%E5%8C%96%E9%A1%B9%E7%9B%AE?sort_id=4164117"><span>https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/关于初始化项目?sort_id=4164117</span></a></span></p> 
 </blockquote> 
 <p style="margin-left:.8em; margin-right:.8em"><span><a href="https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/%E5%85%B3%E4%BA%8E%E5%BA%94%E7%94%A8%E9%83%A8%E7%BD%B2?sort_id=4219382"><span>部署项目 必看</span></a></span></p> 
 <blockquote> 
  <p style="margin-left:0; margin-right:0"><span><a href="https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/%E5%85%B3%E4%BA%8E%E5%BA%94%E7%94%A8%E9%83%A8%E7%BD%B2?sort_id=4219382"><span>https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/关于应用部署?sort_id=4219382</span></a></span></p> 
 </blockquote> 
 <p style="margin-left:.8em; margin-right:.8em"><span><a href="https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/pages"><span>参考文档 Wiki</span></a></span></p> 
 <blockquote> 
  <p style="margin-left:0; margin-right:0"><span><a href="https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/pages"><span>https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/pages</span></a></span></p> 
 </blockquote> 
</blockquote> 
<h2 style="text-align:start"><span>软件架构图</span></h2> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span><img alt="Plus部署架构图" src="https://images.gitee.com/uploads/images/2021/1112/202137_673ac5d2_1766278.png" referrerpolicy="no-referrer"></span></p> 
<h2 style="text-align:start"><span>贡献代码</span></h2> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>欢迎各路英雄豪杰 </span><span><code>PR</code></span><span> 代码 请提交到 </span><span><code>dev</code></span><span> 开发分支 统一测试发版</span></p> 
<p style="color:#333333; margin-left:.8em; margin-right:.8em; text-align:start"><span>框架定位为 </span><span><code>通用后台管理系统(分布式集群强化)</code></span><span> 原则上不接受业务 </span><span><code>PR</code></span></p> 
<h3 style="text-align:start"><span>其他</span></h3> 
<ul style="margin-left:.8em; margin-right:.8em"> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>同步升级 RuoYi-Vue</span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>GitHub 地址 </span><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FJavaLionLi%2FRuoYi-Vue-Plus" target="_blank"><span>RuoYi-Vue-Plus-github</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>单模块 分支 </span><span><a href="https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/tree/fast/"><span>RuoYi-Vue-Plus-fast</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>微服务 分支 </span><span><a href="https://gitee.com/JavaLionLi/RuoYi-Cloud-Plus"><span>RuoYi-Cloud-Plus</span></a></span></p> </li> 
 <li> <p style="margin-left:.5rem; margin-right:0"><span>用户扩展项目 </span><span><a href="https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/pages?sort_id=4478302&doc_id=1469725"><span>扩展项目列表</span></a></span></p> </li> 
</ul> 
<h2 style="text-align:start"><span>加群与捐献</span></h2> 
<blockquote> 
 <p style="margin-left:.8em; margin-right:0"><span><a href="https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/%E5%8A%A0%E7%BE%A4%E4%B8%8E%E6%8D%90%E7%8C%AE?sort_id=4104598"><span>加群与捐献</span></a></span></p> 
 <blockquote> 
  <p style="margin-left:0; margin-right:0"><span><a href="https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/%E5%8A%A0%E7%BE%A4%E4%B8%8E%E6%8D%90%E7%8C%AE?sort_id=4104598"><span>https://gitee.com/JavaLionLi/RuoYi-Vue-Plus/wikis/加群与捐献?sort_id=4104598</span></a></span></p> 
 </blockquote> 
</blockquote> 
<h2 style="text-align:start"><span>业务功能</span></h2> 
<table cellspacing="0" class="md-table" style="border-collapse:collapse; border-spacing:0px; box-sizing:border-box; break-inside:auto; cursor:text; margin:0px !important; overflow:auto; padding:0px; text-align:left; white-space:pre-wrap; width:800px; word-break:initial"> 
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
<p> </p>
                                        </div>
                                      
</div>
            