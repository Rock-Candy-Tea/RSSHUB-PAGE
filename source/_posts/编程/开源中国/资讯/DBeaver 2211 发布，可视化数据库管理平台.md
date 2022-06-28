
---
title: 'DBeaver 22.1.1 发布，可视化数据库管理平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5531'
author: 开源中国
comments: false
date: Tue, 28 Jun 2022 07:04:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5531'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:0">DBeaver 是一个免费开源的通用数据库工具，适用于开发人员和数据库管理员。</p> 
<p style="margin-left:0">DBeaver 22.1.1 现已发布，更新内容如下：</p> 
<ul> 
 <li>Data viewer： 
  <ul> 
   <li>添加了数组和多行数据类型可视化（beta 版）</li> 
   <li>为内联编辑器添加了类似 Excel 的行为（向下移动行，可配置）</li> 
   <li>分组面板中的错误已修复（“duplicates only”选项）</li> 
   <li>修复了日历编辑控件中 NULL 值表示的不一致问题</li> 
   <li>修复了通过双击激活内联编辑器的错误 (gtk)</li> 
   <li>修复了通过单击禁用内联编辑器的错误 (macos)</li> 
  </ul> </li> 
 <li>Data transfer： 
  <ul> 
   <li>修复了“selected columns only”导出（错误的列映射）</li> 
   <li>目标 DDL 生成器现在检查现有的 non-table 对象</li> 
   <li>以 SQL INSERT 格式导出现在对复杂的自定义表使用正确的表名</li> 
   <li>添加了 CSV 和 TXT 格式的 Header configuration</li> 
   <li>修复了超长 CSV 文件导入的问题（行号可视化）</li> 
  </ul> </li> 
 <li>SQL editor： 
  <ul> 
   <li>添加了从结果集生成 DDL 命令</li> 
   <li>支持从执行日志重新执行查询</li> 
   <li>为不支持 schema change 的数据库（Sybase、SQL Server）修复了 schema selector</li> 
  </ul> </li> 
 <li>Tasks： 
  <ul> 
   <li>添加了嵌套任务文件夹支持</li> 
   <li>添加了文件夹重命名支持</li> 
   <li>SQL 脚本执行任务已修复（NullPointer 错误）</li> 
  </ul> </li> 
 <li>Connections：现在可以自定义新的连接名称模式</li> 
 <li>SSH 配置页面现在在小型显示器上有滚动条</li> 
 <li>Database full text search：改进了页面 UI，增加了长列表分页</li> 
 <li>Metadata editor：列自动大小命令已添加到上下文菜单中</li> 
 <li>General UI：添加了项目配置加载可视化</li> 
 <li>Clickhouse：添加了枚举数据类型支持</li> 
 <li>Derby：默认驱动程序版本设置为 10.15（避免 Java 版本问题）</li> 
 <li>Netezza： 
  <ul> 
   <li>默认目录选择已修复</li> 
   <li>添加了旧驱动程序支持</li> 
  </ul> </li> 
 <li>PostgreSQL： 
  <ul> 
   <li>添加了约束信息预读选项</li> 
   <li>枚举列编辑支持已修复</li> 
   <li>修复了具有 NULL 元素的数组的表示</li> 
  </ul> </li> 
 <li>SQLite：添加了 view text edit 支持</li> 
 <li>SQL Server： 
  <ul> 
   <li>nchar 和 nvarchar 列的 DDL 已修复（长度不正确）</li> 
   <li>现在可以编辑具有别名的列</li> 
  </ul> </li> 
 <li>Trino：添加了多行插入支持</li> 
</ul> 
<p><span style="color:#000000">详情可查看：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdbeaver.io%2F2022%2F06%2F26%2Fdbeaver-22-1-1%2F" target="_blank">https://dbeaver.io/2022/06/26/dbeaver-22-1-1/</a></p>
                                        </div>
                                      
</div>
            