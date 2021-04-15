
---
title: '开源多云技术平台——Choerodon猪齿鱼发布 0.25 版本'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://uploader.shimo.im/f/9HGBrIJ7QIfaQB77.png!thumbnail'
author: 开源中国
comments: false
date: Thu, 15 Apr 2021 13:55:00 GMT
thumbnail: 'https://uploader.shimo.im/f/9HGBrIJ7QIfaQB77.png!thumbnail'
---

<div>   
<div class="content">
                                                                    
                                                        <p><span style="background-color:#f9eda6">2021年04月15日</span>，Choerodon猪齿鱼发布<strong>0.25</strong>版本，本次更新<strong>敏捷</strong>中的问题项新增跨项目移动、上传并预览UI/UX文件等功能，组织层新增状态机模板及看板模板功能；<strong>流水线</strong>中CI阶段新增镜像安全扫描任务等功能及图表；<strong>测试</strong>中支持导出测试报表等功能；其它功能模块也都进行了不同程度的新增、修改和优化，欢迎各位更新体验。</p> 
<ul> 
 <li style="text-align:left">发布版本：0.25</li> 
 <li style="text-align:left">发布时间：<span style="background-color:#f9eda6">2021年04月15日</span></li> 
 <li style="text-align:left">更新范围：敏捷协作、代码开发、环境部署、测试管理、制品库、基础功能</li> 
</ul> 
<p style="text-align:left">下面就为大家带来详细的模块介绍。</p> 
<h1 style="text-align:left"><span style="color:#2980b9"><strong>敏捷协作</strong></span></h1> 
<h2 style="text-align:left">新增功能</h2> 
<ul> 
 <li><span style="background-color:#f9eda6">所有问题增加列表视图；</span></li> 
 <li><span style="background-color:#f9eda6">问题项详情支持上传并预览UI/UX文件；</span></li> 
</ul> 
<p><img height="auto" src="https://uploader.shimo.im/f/9HGBrIJ7QIfaQB77.png!thumbnail" width="1597" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><span style="background-color:#f9eda6">问题项支持评论及回复；</span></li> 
 <li><span style="background-color:#f9eda6">问题项支持跨项目移动</span>；</li> 
</ul> 
<p><img height="auto" src="https://uploader.shimo.im/f/tXVxCu59lBKgX8It.gif" width="2246" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>项目报告支持项目质量图表；</li> 
 <li><span style="background-color:#f9eda6">支持自定义问题类型；</span></li> 
</ul> 
<p><img height="auto" src="https://uploader.shimo.im/f/IEQ5v0AIpWMQmnDT.png!thumbnail" width="2256" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>支持启停用问题类型；</li> 
 <li>系统预定义字段支持维护默认值；</li> 
 <li>页面配置的自定义字段控件增加人员多选控件；</li> 
 <li>支持导入页面字段配置；</li> 
 <li>模块支持自定义顺序；</li> 
 <li>状态机支持状态自定义顺序；</li> 
 <li><span style="background-color:#f9eda6">组织层增加状态机模板和看板模板；</span></li> 
</ul> 
<p><span style="background-color:#f9eda6">​​​​​​​</span><img height="auto" src="https://uploader.shimo.im/f/Rlp17yG9xU2VaHAd.png!thumbnail" width="1877" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>工作台增加我经手的、我报告的；</li> 
 <li>项目概览增加项目动态；</li> 
 <li>导入导出问题支持保存常用模板；</li> 
 <li>支持问题延期通知；</li> 
 <li>支持冲刺延期通知；</li> 
 <li style="text-align:left">敏捷问题支持移除关联分支的功能；</li> 
</ul> 
<h2> </h2> 
<h2 style="text-align:left">功能优化</h2> 
<ul> 
 <li style="text-align:left"><span style="background-color:#f9eda6">优化富文本编辑器：支持插入表格；</span></li> 
</ul> 
<p style="text-align:left"><span style="background-color:#f9eda6">​​​​​​​</span><img height="auto" src="https://uploader.shimo.im/f/8LqWzCEpSluSEung.png!thumbnail" width="500" referrerpolicy="no-referrer"></p> 
<ul> 
 <li style="text-align:left">上传附件支持分片上传；</li> 
 <li style="text-align:left">所有问题按状态筛选优化可按问题类型级联；</li> 
 <li style="text-align:left">优化导入导出按钮位置；</li> 
 <li style="text-align:left">迭代计划工作台模式融入项目概览；</li> 
 <li style="text-align:left">优化查找用户支持按用户名拼音搜索；</li> 
 <li style="text-align:left">优化创建问题项时切换问题类型，概要、描述清空的问题；</li> 
</ul> 
<h2 style="text-align:left">缺陷修复</h2> 
<ul> 
 <li style="text-align:left">修复导出、发送项目报告因内容过长造成显示不全的问题；</li> 
 <li style="text-align:left">修复看板兼容Safari浏览器问题；</li> 
 <li style="text-align:left">修复待办事项快捷拖动issue数据不一致的问题；</li> 
 <li style="text-align:left">修复状态机初始状态设置自定义流转不生效的问题；</li> 
 <li style="text-align:left">修复导入问题自定义问题类型导入失败的问题；</li> 
 <li style="text-align:left">修复问题详情开发标签页存在两个more-vert按钮；</li> 
</ul> 
<h1 style="text-align:left"><span style="color:#2980b9">代码开发</span></h1> 
<h2 style="text-align:left">新增功能</h2> 
<ul> 
 <li><span style="background-color:#ffff00">应用流水线-CI阶段-构建任务中，新增支持镜像安全扫描的功能</span><span style="background-color:#ffff00">；</span></li> 
</ul> 
<p><span style="background-color:#ffff00">​​​​​​​</span><img height="auto" src="https://uploader.shimo.im/f/AUjrqPRlQkFuIiYJ.gif" width="2246" referrerpolicy="no-referrer"></p> 
<ul> 
 <li>流水线构建结果支持本地下载；</li> 
 <li>流水线构建日志支持本地下载；</li> 
 <li>DevOps报表中新增流水线触发次数图与流水线执行时长图；</li> 
</ul> 
<p>​​​​​​​<img height="auto" src="https://uploader.shimo.im/f/tvtSkA1kzvseco9q.png!thumbnail" width="1772" referrerpolicy="no-referrer"></p> 
<h1 style="text-align:left"><span style="color:#2980b9">环境部署</span></h1> 
<h2 style="text-align:left">新增功能</h2> 
<ul> 
 <li>PV管理中创建PV时新增支持添加Label的功能；</li> 
</ul> 
<h2 style="text-align:left">功能优化</h2> 
<ul> 
 <li style="text-align:left">部署人员变更实例时，默认不再调整其中Pod数量，仅可通过资源-运行详情界面中的Pod控制器调整其数量；</li> 
</ul> 
<h1 style="text-align:left"><span style="color:#2980b9">测试管理</span></h1> 
<h2 style="text-align:left">新增功能</h2> 
<ul> 
 <li style="text-align:left"><span style="background-color:#f9eda6">测试用例增加自定义编号；</span></li> 
</ul> 
<p style="text-align:left"><span style="background-color:#f9eda6">​​​​​​​</span><img height="auto" src="https://uploader.shimo.im/f/EI8g2TIkuW2Xrp5L.png!thumbnail" width="1566" referrerpolicy="no-referrer"></p> 
<ul> 
 <li style="text-align:left"><span style="background-color:#f9eda6">测试计划支持批量删除用例；</span></li> 
 <li style="text-align:left"><span style="background-color:#f9eda6">测试报表支持导出PDF；</span></li> 
 <li style="text-align:left"><span style="background-color:#f9eda6">工作台增加待我执行的用例；</span></li> 
</ul> 
<h2 style="text-align:left">功能优化</h2> 
<ul> 
 <li style="text-align:left">优化测试计划批量指派；</li> 
 <li style="text-align:left">优化测试计划选择用例形式；</li> 
</ul> 
<h2 style="text-align:left">缺陷修复</h2> 
<ul> 
 <li style="text-align:left">修复测试计划中创建缺陷时关联问题选择框错位的问题；</li> 
 <li style="text-align:left">修复测试计划中创建缺陷时经办人显示乱码的问题；</li> 
</ul> 
<h1 style="text-align:left"><span style="color:#2980b9">制品库</span></h1> 
<h2 style="text-align:left">新增功能</h2> 
<ul> 
 <li style="text-align:left">制品库-Docker仓库中新增镜像安全扫描的功能，支持显示出扫描后的结果详情；</li> 
</ul> 
<h2 style="text-align:left">缺陷修复</h2> 
<ul> 
 <li style="text-align:left">修复了制品界面上传jar包较大时，接口超时的问题；</li> 
</ul> 
<h1 style="text-align:left"><span style="color:#2980b9">基础功能</span></h1> 
<h2 style="text-align:left">新增功能</h2> 
<ul> 
 <li>组织层与项目层-导入用户，支持通过Excel批量导入自定义的角色；</li> 
 <li>创建项目支持选择多个项目类型，且支持修改已有项目的项目类型；</li> 
 <li>工作台中加上个人代码提交的记录展示；</li> 
 <li>自定义工作台与项目概览支持一键重置为默认的；</li> 
 <li>项目设置-通用中支持修改项目类型；</li> 
</ul> 
<h2 style="text-align:left">缺陷修复</h2> 
<ul> 
 <li>修复了项目列表-最近使用栏，未将应用服务按照使用的时间进行倒序排序的问题；</li> 
 <li>修复了组织层角色查询，自定义角色和预定义角色查询混淆的问题；</li> 
</ul>
                                        </div>
                                      
</div>
            