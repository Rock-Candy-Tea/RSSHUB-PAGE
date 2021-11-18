
---
title: 'JeeSite V4.3.1 快速开发平台发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4046'
author: 开源中国
comments: false
date: Thu, 18 Nov 2021 15:21:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4046'
---

<div>   
<div class="content">
                                                                    
                                                        <h2 style="text-align:start">升级内容</h2> 
<ul> 
 <li>spring boot 2.5.6、mybatis 3.5.7、druid 1.2.8、jackson 2.13</li> 
 <li>浏览器升级提示信息的页面更新优化，过低版本浏览器引导页面</li> 
 <li>菜单权限接口：用户菜单权限查询 SQL 全版本优化（性能提升）</li> 
 <li>访问日志：增加访问日志类型快捷操作选项卡界面</li> 
 <li>内置功能：公司管理、菜单管理、行政区划增加左树右表界面</li> 
 <li>组织机构：公司和部门树 treeData 接口增加返回 viewCode 数据</li> 
 <li>组织机构：新增导入导出，并优化 ExcelField 注解写到构造上，方便管理</li> 
 <li>代码生成：新增表单（1列、2列、3列）布局选项的快速选择，相比列设置栅格，更便于操作和理解</li> 
 <li>代码生成：是不是数据表都都生成 findPage 方法，方便调用</li> 
 <li>代码生成：模块优化，如果是 PK 则必须生成到表单</li> 
 <li>代码生成：增加子表的表单验证类生成</li> 
 <li>用户列表选择组件的机构和角色列表增加 isAll 参数</li> 
 <li>防止只升级版本号同步Core代码时，造成的未执行升级脚本问题</li> 
 <li>注解名更新 @Length 改为 @Size 规范名称（两注解功能一致）</li> 
 <li>DataGrid：新增分组表和冻结列的合并单元格支持</li> 
 <li>form 组件：新增不使用 path 属性，使用 name 的时候 defaultValue 仍然有效</li> 
 <li>form 组件：如果没有返回 labelValue，则获取 value 显示</li> 
 <li>BPM：待办已办增加返回上一个处理人参数 extendMap[prevAssignee]=true</li> 
 <li>BPM：新增 BpmUtils.updateStatus 支持 Class 类型 serviceBeanName 参数</li> 
 <li>可视化大屏版本升级 2021-11-15 新增诸多功能</li> 
 <li>作业调度：接口增加创建者查询条件</li> 
 <li>菜单管理：增加停用启用功能</li> 
 <li>新增 SAP HANA 数据库的支持</li> 
</ul> 
<h3 style="text-align:start">问题改进</h3> 
<ul> 
 <li>优化防止 form:hidden 的 type 属性与 model 属性冲突</li> 
 <li>增加参数 max-http-form-post-size: 20MB 提交的包大小限制</li> 
 <li>BPM: 请假流程管理，bpm:button 审核状态时显示提交按钮的问题</li> 
 <li>修正 shardingsphere jdbc 因表名大小写不对应报错的问题</li> 
 <li>修正当不设置 ctrlDataParentCodesAttrName 参数的时候报空问题</li> 
 <li>修正 DataGrid 只开启右侧锁定列的时候排序报错</li> 
 <li>修正代码生成多选字段验证时的问题</li> 
 <li>修正删除用户的提示信息</li> 
</ul> 
<h3 style="text-align:start">升级方法</h3> 
<ul> 
 <li>修改<span> </span><code>pom.xml</code><span> </span>文件中的<span> </span><code>jeesite-parent</code><span> </span>版本号为<span> </span><code>4.3.1-SNAPSHOT</code></li> 
 <li>如果你导入了<span> </span><code>jeesite-common</code><span> </span>源码项目，请与<span> </span><code>git</code><span> </span>上的代码进行同步</li> 
 <li>如果你导入了<span> </span><code>jeesite-module-core</code><span> </span>源码项目，请与<span> </span><code>git</code><span> </span>上的代码进行同步</li> 
 <li>如果你是跨版本升级，请注意每一个版本的升级方法，业务上有调整的地方进行修改</li> 
 <li>执行<span> </span><code>root/package.bat(sh)</code><span> </span>打包脚本，强制更新依赖即可。</li> 
</ul> 
<h3><strong>进一步了解</strong></h3> 
<ul> 
 <li>JeeSite 官网地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fjeesite.com%2F" target="_blank">http://jeesite.com</a></li> 
 <li>JeeSite 在线文档：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdocs.jeesite.com%2F" target="_blank">http://docs.jeesite.com</a></li> 
 <li>JeeSite 演示地址：<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fdemo.jeesite.com%2F" target="_blank">http://demo.jeesite.com</a></li> 
 <li>JeeSite 源码下载：<a href="https://gitee.com/thinkgem/jeesite4" target="_blank">https://gitee.com/thinkgem/jeesite4</a></li> 
</ul> 
<p> </p> 
<p> </p> 
<p> </p>
                                        </div>
                                      
</div>
            