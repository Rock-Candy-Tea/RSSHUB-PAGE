
---
title: 'JeeSite Vue 5.0.3 发布，Spring Boot 快速开发平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-b6a11e6130872416da8d7df0883fc1ba13a.png'
author: 开源中国
comments: false
date: Mon, 16 May 2022 10:27:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-b6a11e6130872416da8d7df0883fc1ba13a.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h3 style="margin-left:0; margin-right:0; text-align:start">升级内容</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 在线用户列表界面、3分钟内活动的用户、游客用户、强踢</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 访问日志界面功能、异常日志、修正前后数据对比</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 菜单管理子系统管理、右上角用户切换子系统</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 多租户切换功能、页面缓存接口优化</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 左树右表可拖拽调整大小 by Oliver</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 BasicTable 表格列拖拽调整列宽功能</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 BasicTable 树表的本地数据，展开折叠</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 BasicTable 组件，字典类型，显示字典默认值属性 defaultValue</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 BasicForm 表单 None 空组件，用于占位</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 useDict 字典工具新增 initGetDictList 方法，便捷获取字典信息</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">新增 DictLabel 组件支持这种写法 tag red badge bg-red 多重写法</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 内置功能体验，状态下拉框，切换后立即查询，不用点击查询按钮</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 BasicTable 树表展开节点，异步加载性能优化</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 BasicTable 避免 selection-change 重复调用，有数据时再调用</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 BasicTable 单元格编辑的自动取消功能，支持除了 Input 组件外的所有组件自动取消</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 BasicTable 单元格编辑，增加 editAutoCancel 参数，默认为不自动取消</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 BasicForm 调整 onChange 的执行顺序，放到设置表单 Model 后</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 BasicForm 允许表单标签 label 为空，省去设置，为空的时候不显示标签</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 Drawer 和 Modal 当不显示确定的时候，取消按钮默认为关闭字样</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 Dropdown 组件，保留字问题 key 修改为 value</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 Dropdown 组件，未设置图标的时候不显示空图标</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 缩短登录的连接超时时间，增加连接服务器超时和网络问题提示信息</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">优化 Vue ErrorHandle 全局错误句柄的页面布局及细节</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">修正 Tree 的 setCheckedKeys 方法，如果设置了空值，就报空的问题</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">修正 DictLabel 组件 列表上停用启用没有及时更新的问题</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">修正 BasicTable 编辑表格不显示数值或布尔类型的数据问题</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">无用户数限制，无在线人数限制</p> </li> 
 <li> <p style="margin-left:.3rem; margin-right:.3rem">其它细节更多优化改进</p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">升级方法</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">请与 <code>jeesite-vue</code> 代码仓库源码进行同步，合并代码，手动解决冲突代码。</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">后端请更新 LoginController 和 CorpAdminController java 类</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">前端与后端版本不同，匹配后端版本为 <code>JeeSite v5.0.1</code></p> </li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:start">了解更多</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0">JeeSite 官网地址：http://jeesite.com</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">JeeSite 在线文档：http://docs.jeesite.com</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">JeeSite 演示地址：http://demo.jeesite.com</p> </li> 
 <li> <p style="margin-left:0; margin-right:0">JeeSite <span>Vue</span> 演示地址：http://vue.jeesite.com</p> <p style="margin-left:0; margin-right:0"> </p> </li> 
</ul> 
<p><img height="901" src="https://oscimg.oschina.net/oscnet/up-b6a11e6130872416da8d7df0883fc1ba13a.png" width="1919" referrerpolicy="no-referrer"></p> 
<p> </p>
                                        </div>
                                      
</div>
            