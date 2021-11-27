
---
title: 'SQL审核 _ SQLE 1.2111.0 来啦！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7714'
author: 开源中国
comments: false
date: Fri, 26 Nov 2021 17:59:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7714'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#ffffff; color:#333333">SQL审核工具 SQLE 1.2111.0 于今天发布。</span></p> 
<p style="margin-left:0; margin-right:0"><strong>一、SQLE 项目介绍</strong></p> 
<p>爱可生开源社区的 SQLE <span style="background-color:#ffffff">是一款面向数据库使用者和管理者，</span>支持多场景审核，支持标准化上线流程，原生支持 MySQL 审核且数据库类型可扩展的 SQL 审核工具。</p> 
<p><strong style="color:#407600">SQLE 获取</strong></p> 
<table cellspacing="0" style="border-collapse:collapse; box-sizing:border-box !important; display:table; margin:0px 0px 10px; max-width:100%; outline:0px; overflow-wrap:break-word !important; padding:0px; width:677px"> 
 <thead> 
  <tr> 
   <th style="text-align:left"><span>类型</span></th> 
   <th style="text-align:left"><span>地址</span></th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px"><span>版本库</span></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px"><span>https://github.com/actiontech/sqle</span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px"><span>文档</span></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px"><span>https://actiontech.github.io/sqle-docs-cn/</span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px"><span>发布信息</span></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px"><span>https://github.com/actiontech/sqle/releases</span></td> 
  </tr> 
  <tr> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px"><span>数据审核插件开发文档</span></td> 
   <td style="border-color:#cccccc; border-style:solid; border-width:1px"><span>https://actiontech.github.io/sqle-docs-cn/3.modules/3.7_auditplugin/auditplugin_development.html</span></td> 
  </tr> 
 </tbody> 
</table> 
<p style="margin-left:0; margin-right:0"><strong><strong>二、更新列表</strong></strong></p> 
<p style="margin-left:0; margin-right:0"><strong><span style="color:#3da742">Release Notes</span></strong></p> 
<p><strong><u>特性</u></strong></p> 
<ul style="list-style-type:square; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>工单上线支持 Online DDL #38</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>支持 LDAP 登录 #44</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>支持自定义数据库，并</span></p> </li> 
</ul> 
<ul style="list-style-type:circle; margin-left:32px; margin-right:32px"> 
 <li> <p style="margin-left:0; margin-right:0"><span>支持 PostgreSQL 数据库审核插件 </span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>支持 Oracle 数据库审核插件 </span></p> </li> 
</ul> 
<p><strong><u>优化</u></strong></p> 
<ul style="list-style-type:square; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>优化白名单页面展示框 #39</span></p> </li> 
 <li> <p><span>优化添加审核计划时的提示信息 #41</span></p> </li> 
 <li> <p><span>调整插件层 API #59</span></p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0"><u><strong>缺陷修复</strong></u></p> 
<ul style="list-style-type:square; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复回滚语句不能正常生成 #42</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复系统配置（邮箱配置，LDAP配置）密码无法修改的问题 #78</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复 release 分支无法触发 CI 流程问题 #66</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复 MyBatis XML 解析器解析空文件 panic 问题 #61</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复数据库审核插件审核规则定义不生效的问题 #57 #107</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复角色删除后，该角色绑定的用户还能访问绑定的数据源的问题 #77</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复命令行参数启动SQLE时 panic 的问题 #65</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>修复使用 Mybatis Scanner 扫描的 XML 内SQL长度支持太小的问题 #60</span></p> </li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            