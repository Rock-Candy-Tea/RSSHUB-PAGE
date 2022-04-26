
---
title: 'MineAdmin v0.7.0 发布，权限管理后台框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6173'
author: 开源中国
comments: false
date: Tue, 26 Apr 2022 08:59:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6173'
---

<div>   
<div class="content">
                                                                                            <p style="color:#40485b; margin-left:0em; margin-right:0em; text-align:start">此版本主要为增强和重构部分代码生成器功能，因代码生成器改动过大，不兼容之前的版本。请谨慎更新</p> 
<h2 style="margin-left:0; margin-right:0; text-align:start">代码生成器更新列表</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">代码生成器重构了大部分功能与生成逻辑，由拼代码生成改为文件模板生成。</p> 
<ul> 
 <li> 
  <ol style="list-style-type:lower-roman"> 
   <li>新增关联配置，支持一对一、一对多、一对多（反向）、多对多配置</li> 
  </ol> </li> 
 <li> 
  <ol start="2" style="list-style-type:lower-roman"> 
   <li>新增菜单配置，支持菜单自由搭配生成。</li> 
  </ol> </li> 
 <li> 
  <ol start="3" style="list-style-type:lower-roman"> 
   <li>字段新增角色权限配置，可指定角色查看某字段</li> 
  </ol> </li> 
 <li> 
  <ol start="4" style="list-style-type:lower-roman"> 
   <li>新增与修改组件可设置模态框或抽屉方式</li> 
  </ol> </li> 
 <li> 
  <ol start="5" style="list-style-type:lower-roman"> 
   <li>新增是否构建菜单选项，选择的话，在生成代码时自动导入菜单SQL</li> 
  </ol> </li> 
 <li> 
  <ol start="6" style="list-style-type:lower-roman"> 
   <li>所属菜单改为非必填，可直接为顶级菜单。</li> 
  </ol> </li> 
 <li> 
  <ol start="7" style="list-style-type:lower-roman"> 
   <li>新增 Switch开关 组件，支持列表回显，同时支持列表支持修改</li> 
  </ol> </li> 
 <li> 
  <ol start="8" style="list-style-type:lower-roman"> 
   <li>新增 计数器 组件，支持列表回显，同时支持列表直接修改</li> 
  </ol> </li> 
 <li> 
  <ol start="9" style="list-style-type:lower-roman"> 
   <li>新增 省市区 组件，可设置级联或者下拉联动方式以及设置保存code或者name</li> 
  </ol> </li> 
 <li> 
  <ol start="10" style="list-style-type:lower-roman"> 
   <li>新增 滑块 组件。</li> 
  </ol> </li> 
 <li> 
  <ol start="11" style="list-style-type:lower-roman"> 
   <li>新增 时间选择器 组件</li> 
  </ol> </li> 
 <li> 
  <ol start="12" style="list-style-type:lower-roman"> 
   <li>增强 日期选择器 组件，可设置组件类型：日期、日期范围、时间、时间范围、年、月、周</li> 
  </ol> </li> 
 <li> 
  <ol start="13" style="list-style-type:lower-roman"> 
   <li>新增 用户选择器 组件</li> 
  </ol> </li> 
 <li> 
  <ol start="14" style="list-style-type:lower-roman"> 
   <li>新增 用户信息 组件，可设置保存 用户id、用户名、昵称、部门id 等信息</li> 
  </ol> </li> 
 <li> 
  <ol start="15" style="list-style-type:lower-roman"> 
   <li>新增 颜色选择器 组件</li> 
  </ol> </li> 
 <li> 
  <ol start="16" style="list-style-type:lower-roman"> 
   <li>新增 评分器 组件</li> 
  </ol> </li> 
 <li> 
  <ol start="17" style="list-style-type:lower-roman"> 
   <li>增强 下拉选择、单选、复选 组件，在支持数据字典同时，也支持自定义项</li> 
  </ol> </li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:start">常规修复更新</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">[增强] 启动信息加入显示当前系统用户<br> [增强] Auth注解添加验证场景功能</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">[修复] 手机端下操作按钮和搜索错位问题<br> [修复] 检查模块中间件问题<br> [修复] 接口简易模式验证bug<br> [修复] 消息接收人列表SQL缺少表前缀问题<br> [修复] 导入驱动phpOfficec依赖更新后导致获取值为空的问题</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">提示：更新到0.7.0版本方法</p> 
<p style="color:#40485b; margin-left:0em; margin-right:0em; text-align:start">更新hyperf框架，执行 composer install 命令<br> 后端执行升级SQL命令：php bin/hyperf.php mine:update</p>
                                        </div>
                                      
</div>
            