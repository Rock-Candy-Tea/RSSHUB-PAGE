
---
title: 'Rocket-API 2.4.3 发布，API 开发的低代码平台，基于 Spring Boot'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://images.gitee.com/uploads/images/2020/1119/195027_6ae6ae9d_5139840.png'
author: 开源中国
comments: false
date: Mon, 09 Aug 2021 09:41:00 GMT
thumbnail: 'https://images.gitee.com/uploads/images/2020/1119/195027_6ae6ae9d_5139840.png'
---

<div>   
<div class="content">
                                                                                            <div style="text-align:left"> 
 <div> 
  <h2 style="text-align: left;">功能新增</h2> 
  <ol> 
   <li>修改搜索框，支持树形结构搜索，展示相关联的上下级，正则搜索</li> 
   <li>新增'''sql '''单引号支持sql提示</li> 
   <li>添加纯SQL模式，自动识别增删改查分页，计数等数据库操作，并附带sql语法和代码提示 ,文档见：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falenfive.gitbook.io%2Frocket-api%2Fshu-ju-ku-cao-zuo%2Fchun-sql-mo-shi" target="_blank">https://alenfive.gitbook.io/rocket-api/shu-ju-ku-cao-zuo/chun-sql-mo-shi</a></li> 
   <li>添加动态数据源默认的事务管理，所有的数据库操作都会带上可重复读级别事务管控，Exception级别异常事务回滚</li> 
  </ol> 
  <h2 style="text-align: left;">功能修改</h2> 
  <p style="text-align:left">1.默认组path默认修改默认值为 ""<br> 2.修改符在单引号环境下，不加引号，原样封装到sql中如‴sqlselect∗from符在单引号环境下，不加引号，原样封装到sql中如‴sqlselect∗from&#123;table&#125;''' -> "select * from user"</p> 
  <p style="text-align:left"> </p> 
 </div> 
</div> 
<div style="text-align:left"> 
 <div> 
  <div> 
   <div>
     
   </div> 
  </div> 
 </div> 
</div> 
<p style="text-align:left"><img alt="输入图片说明" height="200" src="https://images.gitee.com/uploads/images/2020/1119/195027_6ae6ae9d_5139840.png" width="244" referrerpolicy="no-referrer"></p> 
<h3 style="text-align:left">定位</h3> 
<p style="text-align:left">拒绝CRUD。用尽可能简单的方式，完成尽可能多的需求。通过约定的方式 实现统一的标准。告别加班，拒绝重复劳动，远离搬砖</p> 
<h3 style="text-align:left">概述</h3> 
<p style="text-align:left">"Rocket-API" 基于spring boot 的API敏捷开发框架，服务端50%以上的功能只需要写SQL或者 mongodb原始执行脚本就能完成开发，另外30%也在不停的完善公共组件，比如文件上传，下载，导出，预览，分页等等通过一二行代码也能完成开发，剩下的20%也能依赖于动态编译技术生成class的形式，不需要发布部署，不需要重启来实现研发团队的快速编码，提测以及回归。<br> 实现了服务端研发效率300%-500%的提升，人力成本减少了3倍</p> 
<h3 style="text-align:left">特性</h3> 
<p style="text-align:left"><span style="background-color:#ffffff; color:#333333">用于快速开发API接口。不再定义 </span><code>Controller</code><span style="background-color:#ffffff; color:#333333">, </span><code>Service</code><span style="background-color:#ffffff; color:#333333">, </span><code>Dao</code><span style="background-color:#ffffff; color:#333333">, </span><code>Mybatis</code><span style="background-color:#ffffff; color:#333333">, </span><code>xml</code><span style="background-color:#ffffff; color:#333333">, </span><code>Entity</code><span style="background-color:#ffffff; color:#333333">, </span><code>VO</code><span style="background-color:#ffffff; color:#333333">等对象和方法. 可视化界面，将入参自动封装到可执行的脚本上，支持所有关系性数据库SQL执行语句，非关系型 </span><code>MONGODB</code><span style="background-color:#ffffff; color:#333333">查询语句. 完全基于springboot2.x 作为springboot项目的stater方式集成,无侵入性，新老项目都能快速集成 只需编写一行代码即可完成大部分的业务需求开发，使用难度级别（测试 or 运维）也可参与开发 在线动态编译，无需重启，即时生效，多数据源操作 版本控制,历史记录比对，回滚等功能 远程一键发布到线上环境 线上POSTMAN调试,保存POSTMAN信息或三方文档的自动生成，历史调用记录存储，回塑 代码提示，SQL提示，语法提示 用户管理控制，安全性控制，以及历史行为记录 动态数据源管理，2.3.0.RELEASE 新增功能</span></p> 
<h3 style="text-align:left">工作原理</h3> 
<p style="text-align:left">1.将API信息，请求方式，请求PATH，处理逻辑存储于数据库中，调用springboot提供的RequestMappingHandlerMapping.registerMapping/unregisterMapping 实现动态管理RequestMapping。<br> 2.依赖于java1.8提供的ScriptEngineManager方法，调用Groovy引擎，赋于数据处理能力以及使代码逻辑能够实现动态编译，发布，而不用重启<br> 3.以springboot starter形式，集成在业务项目中</p> 
<h3 style="text-align:left">资源地址</h3> 
<blockquote> 
 <p>在线演示：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2F39.98.181.90%3A8081%2Finterface-ui" target="_blank">http://39.98.181.90:8081/interface-ui</a></p> 
</blockquote> 
<blockquote> 
 <p>代码仓库：<a href="https://gitee.com/alenfive/rocket-api">https://gitee.com/alenfive/rocket-api</a></p> 
</blockquote> 
<blockquote> 
 <p>文档地址: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Falenfive.gitbook.io%2Frocket-api%2F" target="_blank">https://alenfive.gitbook.io/rocket-api/</a></p> 
</blockquote> 
<blockquote> 
 <p>一分钟系列: <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.csdn.net%2Fmaple_son%2Farticle%2Fdetails%2F108196584" target="_blank">https://blog.csdn.net/maple_son/article/details/108196584</a></p> 
</blockquote> 
<h3 style="text-align:left">项目预览</h3> 
<p style="text-align:left"><img height="353" src="https://oscimg.oschina.net/oscnet/up-2e56b257423fca6ed9a31f2a5f29e10ee46.png" width="700" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><img height="353" src="https://oscimg.oschina.net/oscnet/up-a6cf521da5c1e5f726ab451fc8394081beb.png" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>经过多次项目验证，传统业务型开发，服务端效率能够提升3-5倍，前后端联调提升效率1倍，测试效率2倍提升</li> 
</ul>
                                        </div>
                                      
</div>
            