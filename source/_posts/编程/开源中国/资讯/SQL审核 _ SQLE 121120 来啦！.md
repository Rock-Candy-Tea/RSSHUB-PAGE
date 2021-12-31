
---
title: 'SQL审核 _ SQLE 1.2112.0 来啦！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6340'
author: 开源中国
comments: false
date: Fri, 31 Dec 2021 17:52:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6340'
---

<div>   
<div class="content">
                                                                                            <p><span style="background-color:#ffffff; color:#333333">SQL审核工具 SQLE 1.2112.0 于今天发布。</span></p> 
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
 <li> <p style="margin-left:0; margin-right:0; text-align:left"><span>[#55] 新增索引优化功能，目前支持三星索引、多表关联查询索引建议、模糊查询、函数查询的索引优化，详细介绍：</span><span>https://actiontech.github.io/sqle-docs-cn/3.modules/3.5_auditworkflow/index_optimization.html</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>[#157] 新增工单定时上线功能，可以设置、取消、修改定时时间</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>[#123] 审核规则支持多配置，提高单个规则的定制灵活性度</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>[#121] 增加规则配置项，提高规则的适用范围</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>[#129] SQL输入支持输入联想，补全关键字，提高录入效率</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>[#171] 数据源支持域名，支持录入并审核云数据库</span></p> </li> 
</ul> 
<p style="color:#010101; margin-left:0; margin-right:0"><strong style="color:#000000"><u>优化</u></strong></p> 
<ul style="list-style-type:square; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>[#49] 工单状态优化，提供更多的状态流转信息</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>[#157] 优化上线信息展示，在工单详情页可以查看上线开始和结束时间，以及当前上线状态</span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span>规则模板编辑页面优化，布局调整去除非必要字段，新增字段类型校验 actiontech/sqle-ui#16</span></p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0"><u><strong>缺陷修复</strong></u></p> 
<ul style="list-style-type:square; margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span>[#130] 修复审核规则 "改表时，表空间超过指定大小(MB)审核时输出osc改写建议" 触发时导致程序崩溃的问题</span></p> </li> 
</ul>
                                        </div>
                                      
</div>
            