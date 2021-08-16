
---
title: 'J2eeFAST 2.5.0 版本发布，Java EE 企业级快速开发平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://images.gitee.com/uploads/images/2020/0908/084001_75d40312_1816537.png'
author: 开源中国
comments: false
date: Mon, 16 Aug 2021 09:25:00 GMT
thumbnail: 'https://images.gitee.com/uploads/images/2020/0908/084001_75d40312_1816537.png'
---

<div>   
<div class="content">
                                                                                            <div> 
 <div> 
  <h4>版本更新</h4> 
  <ul> 
   <li>本次更新 
    <ul> 
     <li><code>2021-08-15 v2.5.0</code></li> 
    </ul> 
    <ul> 
     <li>升级mybatisplus到最新版本3.4.3</li> 
     <li>升级Flowable 工作流引擎到最新版本6.6.0</li> 
     <li>升级hutool到 5.7.6</li> 
     <li>升级swagger到 3.0.0</li> 
     <li>升级fastjson到最新版1.2.76</li> 
     <li>fix: issues #I3BOFQ sql注入问题</li> 
     <li>修复添加SQLServer数据库源问题</li> 
     <li>修复富文本最大化显示问题</li> 
     <li>登录滑动验提示图片新增可配置路径</li> 
     <li>新增初始化数据库、打war包脚本</li> 
     <li>修改字典表格链接样式</li> 
     <li>增加ftp依赖</li> 
     <li>新增首页图标统计样例</li> 
     <li>新增公司部门编码字段</li> 
     <li>新增复杂表格、多表联动等演示案例</li> 
     <li>优化树、表组件</li> 
     <li>fix: shiro 共享session会话到redis逻辑问题导致切换用户异常情况</li> 
     <li>优化访问更新redis频率</li> 
     <li>升级echarts 图表统计到最新版本</li> 
     <li>新增评论插件</li> 
     <li>新增系统内部消息评论</li> 
     <li>调整样式两个登录页面新增多租户选择、优化页面样式、新增主题样式</li> 
     <li>新引入ace 代码编辑器插件</li> 
     <li>系统新增多租户模式(SAAS)</li> 
     <li>整合ureport2 报表插件</li> 
     <li>新增复杂表格设置问题</li> 
     <li>修复冻结表格窗体变化导致样式错位问题</li> 
     <li>优化表格样式</li> 
     <li>改进启动多次加载系统参数问题</li> 
     <li>修复用户在线情况不准确问题</li> 
     <li>新增通过配置实现不同角色展示不同首页</li> 
     <li>改进系统自动脚本升级</li> 
     <li>新增日志记录访问代理信息</li> 
     <li>新增动态表名、数据量大的时候可以做分表处理</li> 
     <li>修复日志不记录异常情况，耗时统计错误问题、新增记录代理信息字段</li> 
     <li>整合工作流到系统支持多租户功能</li> 
     <li>优化查询页面查询条件过多显示问题</li> 
     <li>优化其他细节</li> 
    </ul> </li> 
  </ul> 
  <hr> 
  <p>J2eeFAST 是一个 Java EE 企业级快速开发平台， <strong>致力于打造中小企业最好用的开源免费的后台框架平台</strong> 。 系统基于（Spring Boot、Spring MVC、Apache Shiro、MyBatis-Plus、Freemarker、Bootstrap、AdminLTE）经典技术开发， 系统内置核心模块包含众多常用基础功能(在线代码生成功能、组织机构、角色用户、菜单及按钮授权、数据权限、系统参数、license认证、BPM工作流、多租户、在线报表等)， <strong>让你用最低的成本、最高的效率，开发项目，她也适合新手朋友练手</strong> 。同时具备， <strong>界面简洁美观、高效、安全、源码可控、版本迭代快、免费技术交流群</strong> 等特点。她适用于所有Web应用，她会成为你快速开发项目的好帮手。</p> 
  <h4>软件架构</h4> 
  <ol> 
   <li><em>核心框架：Spring Boot 2.X</em></li> 
   <li><em>安全框架：Apache Shiro 1.X</em></li> 
   <li><em>模板引擎：Freemarker</em></li> 
   <li><em>前端：AdminLTE 2.3.8, Bootstrap 3.3.7, Bootstrap-Table 1.11.0, JQuery 3.3.1</em></li> 
   <li><em>持久层框架：MyBatis-Plus 3.X</em></li> 
   <li><em>定时任务: Quartz</em></li> 
   <li><em>数据库连接池：Druid 1.10.1</em></li> 
   <li><em>数据库: Mysql5.7</em></li> 
   <li><em>分布式缓存数据库: Redis 4.0.9</em></li> 
   <li><em>工具类：Hutool 4.5.8</em></li> 
   <li><em>工作流引擎:flowable 6.6.0</em></li> 
  </ol> 
  <h4>演示地址</h4> 
  <ol> 
   <li>演示地址： <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.j2eefast.com" target="_blank">http://www.j2eefast.com</a><br> 账号 ：admin 密码：admin</li> 
   <li>功能还在陆续更新中......</li> 
  </ol> 
  <h4>项目演示</h4> 
  <p><img alt="输入图片说明" src="https://images.gitee.com/uploads/images/2020/0908/084001_75d40312_1816537.png" referrerpolicy="no-referrer"> <img alt="输入图片说明" src="https://images.gitee.com/uploads/images/2020/0908/084020_e10905d8_1816537.png" referrerpolicy="no-referrer"> <img alt="输入图片说明" src="https://images.gitee.com/uploads/images/2020/0908/084104_5497a596_1816537.png" referrerpolicy="no-referrer"> <img alt="输入图片说明" src="https://images.gitee.com/uploads/images/2020/0908/084221_70975dcf_1816537.png" referrerpolicy="no-referrer"> <img alt="输入图片说明" src="https://images.gitee.com/uploads/images/2020/0810/142932_30f1f459_1816537.png" referrerpolicy="no-referrer"> <img alt="输入图片说明" src="https://images.gitee.com/uploads/images/2020/0810/143020_d4583af2_1816537.png" referrerpolicy="no-referrer"> <img alt="输入图片说明" src="https://images.gitee.com/uploads/images/2020/0810/143057_462c279f_1816537.png" referrerpolicy="no-referrer"> <img alt="输入图片说明" src="https://images.gitee.com/uploads/images/2020/0810/143152_b0ff9fd0_1816537.png" referrerpolicy="no-referrer"> <img alt="输入图片说明" src="https://images.gitee.com/uploads/images/2020/0908/084132_00c4292f_1816537.png" referrerpolicy="no-referrer"> <img alt="输入图片说明" src="https://images.gitee.com/uploads/images/2020/0908/084145_791f453f_1816537.png" referrerpolicy="no-referrer"></p> 
 </div> 
</div>
                                        </div>
                                      
</div>
            