
---
title: 'Rocket-API 2.4.4 发布，API 开发的低代码平台，基于 Spring Boot'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://images.gitee.com/uploads/images/2020/1119/195027_6ae6ae9d_5139840.png'
author: 开源中国
comments: false
date: Mon, 24 Jan 2022 10:41:00 GMT
thumbnail: 'https://images.gitee.com/uploads/images/2020/1119/195027_6ae6ae9d_5139840.png'
---

<div>   
<div class="content">
                                                                                            <p># 版本迭代</p> 
<p><span style="background-color:#ffffff; color:#40485b">1.调整jdbcTemplate为NamedParameterJdbcTemplate来执行sql</span><br> <span style="background-color:#ffffff; color:#40485b">2.新增命名参数式入参,如"select * from user where name=:name"</span><br> <span style="background-color:#ffffff; color:#40485b">3.新增参数类型指定，如:#&#123;str,CLOB&#125;,支持的数据类型查看：java.sql.Types</span><br> <span style="background-color:#ffffff; color:#40485b">4.优化代码结构</span><br> <span style="background-color:#ffffff; color:#40485b">5.新增分页为配置项，通过配置项设置分页变量名，默认值，偏移量属性</span><br> <span style="background-color:#ffffff; color:#40485b">6.添加手动获取分页方法函数db.getPageNo(),db.getOffset(),db.getPageSize()</span><br> <span style="background-color:#ffffff; color:#40485b">7.删除mongo查询返回大小写转换，默认原样输出</span><br> <span style="background-color:#ffffff; color:#40485b">8.修改https下path路径获取不准确的问题</span><br> <span style="background-color:#ffffff; color:#40485b">9.修改事务为非强制条件</span><br> <span style="background-color:#ffffff; color:#40485b">10.自动分页下?&#123;&#125;语法不工作问题处理</span><br> <span style="background-color:#ffffff; color:#40485b">11.添加Presto数据库类型支持，感谢</span><a href="https://gitee.com/ruanxingping">@阮<span> </span></a><span style="background-color:#ffffff; color:#40485b">提供的驱动代码</span><br> <span style="background-color:#ffffff; color:#40485b">12.添加关系性数据库批量操作,db.batchUpdate(sql,params) 支持批量新增和指更新</span><br> <span style="background-color:#ffffff; color:#40485b">13.修改Sql log为参数格式化输出，将参数封装到SQL上，输出日志</span><br> <span style="background-color:#ffffff; color:#40485b">14.添加Utils.val(varName,defaultValue)方法，为空返回默认值,感谢</span><a href="https://gitee.com/chaozwn">@zhao_wei_nan<span> </span></a><span style="background-color:#ffffff; color:#40485b">提供的支持</span><br> <span style="background-color:#ffffff; color:#40485b">15.添加数据源注入，修复动态编辑数据源后，历史数据源不能够释放问题</span><br> <span style="background-color:#ffffff; color:#40485b">16.修改变量作用域标识，添加以下划线 _ 为前缀表示</span><br> <span style="background-color:#ffffff; color:#40485b">17.修改文档访问地址,迁移到语雀<span> </span></span><a href="https://gitee.com/link?target=https%3A%2F%2Fwww.yuque.com%2Falenfive%2Frocket-api" target="_blank">https://www.yuque.com/alenfive/rocket-api</a><br> <span style="background-color:#ffffff; color:#40485b">18.修改支持搜索 全路径匹配</span><br> <span style="background-color:#ffffff; color:#40485b">19.升级到springboot2.6.x版本</span><br> <span style="background-color:#ffffff; color:#40485b">20.添加源代码的启动日志 - 本项目只是单纯用来编译生成 rocket-api-boot-starter</span></p> 
<div style="text-align:start"> 
 <div> 
  <div style="text-align:left"> 
   <p style="margin-left:0; margin-right:0; text-align:left"><img alt="输入图片说明" height="200" src="https://images.gitee.com/uploads/images/2020/1119/195027_6ae6ae9d_5139840.png" width="244" referrerpolicy="no-referrer"></p> 
   <h3 style="margin-left:0; margin-right:0; text-align:left">定位</h3> 
   <p style="margin-left:0; margin-right:0; text-align:left">拒绝CRUD。用尽可能简单的方式，完成尽可能多的需求。通过约定的方式 实现统一的标准。告别加班，拒绝重复劳动，远离搬砖</p> 
   <h3 style="margin-left:0; margin-right:0; text-align:left">概述</h3> 
   <p style="margin-left:0; margin-right:0; text-align:left">"Rocket-API" 基于spring boot 的API敏捷开发框架，服务端50%以上的功能只需要写SQL或者 mongodb原始执行脚本就能完成开发，另外30%也在不停的完善公共组件，比如文件上传，下载，导出，预览，分页等等通过一二行代码也能完成开发，剩下的20%也能依赖于动态编译技术生成class的形式，不需要发布部署，不需要重启来实现研发团队的快速编码，提测以及回归。<br> 实现了服务端研发效率300%-500%的提升，人力成本减少了3倍</p> 
   <h3 style="margin-left:0; margin-right:0; text-align:left">特性</h3> 
   <p style="margin-left:0; margin-right:0; text-align:left"><span style="background-color:#ffffff; color:#333333">用于快速开发API接口。不再定义 </span><code>Controller</code><span style="background-color:#ffffff; color:#333333">, </span><code>Service</code><span style="background-color:#ffffff; color:#333333">, </span><code>Dao</code><span style="background-color:#ffffff; color:#333333">, </span><code>Mybatis</code><span style="background-color:#ffffff; color:#333333">, </span><code>xml</code><span style="background-color:#ffffff; color:#333333">, </span><code>Entity</code><span style="background-color:#ffffff; color:#333333">, </span><code>VO</code><span style="background-color:#ffffff; color:#333333">等对象和方法. 可视化界面，将入参自动封装到可执行的脚本上，支持所有关系性数据库SQL执行语句，非关系型 </span><code>MONGODB</code><span style="background-color:#ffffff; color:#333333">查询语句. 完全基于springboot2.x 作为springboot项目的stater方式集成,无侵入性，新老项目都能快速集成 只需编写一行代码即可完成大部分的业务需求开发，使用难度级别（测试 or 运维）也可参与开发 在线动态编译，无需重启，即时生效，多数据源操作 版本控制,历史记录比对，回滚等功能 远程一键发布到线上环境 线上POSTMAN调试,保存POSTMAN信息或三方文档的自动生成，历史调用记录存储，回塑 代码提示，SQL提示，语法提示 用户管理控制，安全性控制，以及历史行为记录 动态数据源管理，2.3.0.RELEASE 新增功能</span></p> 
   <h3 style="margin-left:0; margin-right:0; text-align:left">工作原理</h3> 
   <p style="margin-left:0; margin-right:0; text-align:left">1.将API信息，请求方式，请求PATH，处理逻辑存储于数据库中，调用springboot提供的RequestMappingHandlerMapping.registerMapping/unregisterMapping 实现动态管理RequestMapping。<br> 2.依赖于java1.8提供的ScriptEngineManager方法，调用Groovy引擎，赋于数据处理能力以及使代码逻辑能够实现动态编译，发布，而不用重启<br> 3.以springboot starter形式，集成在业务项目中</p> 
   <h3 style="margin-left:0; margin-right:0; text-align:left">资源地址</h3> 
   <blockquote> 
    <p style="margin-left:0; margin-right:0">在线演示：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2F39.98.181.90%3A8081%2Finterface-ui" target="_blank">http://39.98.181.90:8081/interface-ui</a></p> 
   </blockquote> 
   <blockquote> 
    <p style="margin-left:0; margin-right:0">代码仓库：<a href="https://gitee.com/alenfive/rocket-api">https://gitee.com/alenfive/rocket-api</a></p> 
   </blockquote> 
   <blockquote> 
    <p style="margin-left:0; margin-right:0">文档地址: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falenfive.gitbook.io%2Frocket-api%2F" target="_blank">https://alenfive.gitbook.io/rocket-api/</a></p> 
   </blockquote> 
   <blockquote> 
    <p style="margin-left:0; margin-right:0">一分钟系列: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.csdn.net%2Fmaple_son%2Farticle%2Fdetails%2F108196584" target="_blank">https://blog.csdn.net/maple_son/article/details/108196584</a></p> 
   </blockquote> 
   <h3 style="margin-left:0; margin-right:0; text-align:left">项目预览</h3> 
   <p style="margin-left:0; margin-right:0; text-align:left"><img height="353" src="https://oscimg.oschina.net/oscnet/up-2e56b257423fca6ed9a31f2a5f29e10ee46.png" width="700" referrerpolicy="no-referrer"></p> 
   <p style="margin-left:0; margin-right:0; text-align:left"><img height="353" src="https://oscimg.oschina.net/oscnet/up-a6cf521da5c1e5f726ab451fc8394081beb.png" width="700" referrerpolicy="no-referrer"></p> 
   <ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
    <li>经过多次项目验证，传统业务型开发，服务端效率能够提升3-5倍，前后端联调提升效率1倍，测试效率2倍提升</li> 
   </ul> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            