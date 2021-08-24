
---
title: 'Diboot 2.3.0 发布，高效易用的低代码开发平台'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2615'
author: 开源中国
comments: false
date: Tue, 24 Aug 2021 15:09:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2615'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:start">Diboot是为开发者所打造的一个低代码开发平台，一个数倍提效的赋能工具。</p> 
<p style="text-align:start">Diboot不但拥有从前端到后端的整个基础架构，帮你更快开展项目。而且还拥有开发过程中的前后端一系列已有组件，助你少造轮子。还具有一套自动化工具，在开发过程中，前后端方面都可以帮您提质增效。</p> 
<p style="text-align:start">Diboot将致力于有效提高软件的代码质量、开发效率、可维护性，同时也对其打造了自动化工具来完成系列重复工作和复杂工作。</p> 
<p style="text-align:start">Diboot将通过系列基础组件化繁为简，又通过高效工具以简驭繁。</p> 
<h3 style="text-align:start">更新内容</h3> 
<p style="text-align:start">在此版本中，我们主要新增了删除撤回功能、devtools支持表的模块化管理与代码生成、搜索功能对回车搜索和下拉选择搜索的优化、核心组件core的系列性能优化和扩展、IAM系列优化及登陆加密的支持、其他系列组件的功能扩展等。</p> 
<h4 style="text-align:start">diboot-core & diboot-core-starter</h4> 
<p style="text-align:start">🎉 新增：</p> 
<ul> 
 <li>支持“删除撤回”的后端接口</li> 
 <li>redis及无状态相关自动配置实现</li> 
 <li>支持含转义关键字的列绑定</li> 
 <li>BindQuery支持配置Strategy空值处理策略</li> 
 <li>升级依赖版本：spring boot 2.5.3, mybatis-plus 3.4.3.1...</li> 
</ul> 
<p style="text-align:start">🍻 优化：</p> 
<ul> 
 <li>关联绑定缓存及资源占用相关优化</li> 
 <li>绑定VO及getViewObjectList等接口仅select必需字段</li> 
 <li>BaseCrudRestController中的泛型定义</li> 
 <li>starter中的配置参数支持输入提示</li> 
 <li>单元测试，添加默认配置文件等</li> 
</ul> 
<p style="text-align:start">🐛 修复：</p> 
<ul> 
 <li>特殊场景下的绑定结果中map为null报错的问题</li> 
</ul> 
<h4 style="text-align:start">diboot-IAM-starter</h4> 
<p style="text-align:start">🎉 新增：</p> 
<ul> 
 <li>新增EncryptCredential加密处理，支持登录加密场景</li> 
 <li>新增redis及无状态相关自动配置实现</li> 
 <li>新增配置参数支持便捷开启无状态</li> 
</ul> 
<p style="text-align:start">🍻 优化：</p> 
<ul> 
 <li>优化starter中的配置参数支持输入提示</li> 
 <li>移除IamUserService中的*SortByOrg接口</li> 
 <li>升级依赖版本</li> 
</ul> 
<p style="text-align:start">🐛 修复：</p> 
<ul> 
 <li>Fix bug: getParentOrgIds接口某种数据场景下报NPE的问题</li> 
</ul> 
<h4 style="text-align:start">diboot-file-starter</h4> 
<p style="text-align:start">🎉 新增：</p> 
<ul> 
 <li>新增@ExcelOption注解，支持导入导出字典字段为excel“下拉选项”形式</li> 
</ul> 
<p style="text-align:start">🍻 优化：</p> 
<ul> 
 <li>优化starter中的配置参数支持输入提示</li> 
 <li>预览时页面显示的总数由分页数量优化为导入的总数量</li> 
 <li>升级依赖版本</li> 
</ul> 
<h4 style="text-align:start">diboot-message-starter</h4> 
<p style="text-align:start">🍻 优化：</p> 
<ul> 
 <li>邮件通道支持发送附件</li> 
 <li>优化starter中的配置参数支持输入提示</li> 
 <li>升级依赖版本</li> 
</ul> 
<h4 style="text-align:start">diboot-scheduler-starter</h4> 
<p style="text-align:start">🍻 优化：</p> 
<ul> 
 <li>优化starter中的配置参数支持输入提示</li> 
 <li>清理过期代码，升级依赖版本</li> 
</ul> 
<h4 style="text-align:start">Devtools</h4> 
<p style="text-align:start">🎉 新增：</p> 
<ul> 
 <li>数据表管理支持表前缀/模块及Entity类名自定义；</li> 
 <li>数据表管理新增索引管理功能；</li> 
 <li>数据表管理支持删除表、重命名表；</li> 
 <li>CRUD列表与表单页面支持树结构的生成；</li> 
 <li>CRUD前端生成配置支持保存快照，恢复快照；</li> 
 <li>前端列表、详情、时间轴、导出等，可选ID字段；</li> 
 <li>前端列表表格可对满足条件的字段进行缩略展示相关配置和生成；</li> 
 <li>支持线上订阅</li> 
</ul> 
<p style="text-align:start">🍻 优化：</p> 
<ul> 
 <li>页面系列样式及交互优化；</li> 
 <li>前端生成的代码格式优化；</li> 
 <li>面板列表倒序排列；</li> 
 <li>优化：生成后端代码后，应用不重启，在设计器中也能够读取到对应的关联字段；</li> 
</ul> 
<p style="text-align:start">🐛 修复：</p> 
<ul> 
 <li>fix：多个面板容器存在时，之前的面板预览样式丢失的问题；</li> 
 <li>fix：偶发的关联显示字段不显示或不能设置的问题；</li> 
 <li>fix：被关联表在ER图中，不显示字典关联的字典数据列表的问题；</li> 
 <li>fix：系列具有列表配置功能的前端组件在读取历史配置信息后不能正确回显的问题；</li> 
</ul> 
<h4 style="text-align:start">前端项目 diboot-antd-admin</h4> 
<p style="text-align:start">🍻 优化：</p> 
<ul> 
 <li>删除操作增加支持撤回</li> 
 <li>优化角色权限选择UI，叶子节点平铺</li> 
 <li>优化文件上传下载组件细节</li> 
 <li>优化全局样式定义</li> 
 <li>优化搜索框支持可清除</li> 
 <li>搜索框支持回车搜索和列表选择后搜索</li> 
 <li>优化退出清空token相关逻辑</li> 
</ul> 
<h4 style="text-align:start">前端项目 diboot-element-admin</h4> 
<p style="text-align:start">🍻 优化：</p> 
<ul> 
 <li>更换富文本编辑器为tinymce</li> 
 <li>删除增加支持撤回操作</li> 
 <li>优化角色权限选择UI，叶子节点平铺</li> 
 <li>优化文件上传下载组件细节</li> 
 <li>优化全局样式定义</li> 
 <li>优化搜索框支持可清除</li> 
 <li>搜索框支持回车搜索和列表选择后搜索</li> 
</ul>
                                        </div>
                                      
</div>
            