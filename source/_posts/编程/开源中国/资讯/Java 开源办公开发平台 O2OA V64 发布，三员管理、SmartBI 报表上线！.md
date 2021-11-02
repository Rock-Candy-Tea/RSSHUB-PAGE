
---
title: 'Java 开源办公开发平台 O2OA V6.4 发布，三员管理、SmartBI 报表上线！'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-4c5af10cb59171f6cf0e1998a71860684c3.png'
author: 开源中国
comments: false
date: Tue, 02 Nov 2021 09:53:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-4c5af10cb59171f6cf0e1998a71860684c3.png'
---

<div>   
<div class="content">
                                                                                            <p style="margin-left:.0001pt; margin-right:0; text-align:justify"><span><span>        O2OA V6.4<span>版本新增</span><span>了内置应用「三员管理」。该应用支持以系统管理员，安全管理员，安全审计员三员分责分权的方式进行系统安全管理。启动三员管理后会解除</span>xadmin<span>用户及权限同时启用系统的审计日志记录。</span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:justify"><span><span><span>日志界面如下：</span></span></span></p> 
<p style="text-align:center"><img alt height="709" src="https://oscimg.oschina.net/oscnet/up-4c5af10cb59171f6cf0e1998a71860684c3.png" width="1251" referrerpolicy="no-referrer"></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:justify"><span><span><span>点击具体的条目可以查看详情，如下图：</span></span></span></p> 
<p style="text-align:center"><br> <img alt height="719" src="https://oscimg.oschina.net/oscnet/up-a8dfab9c0272da7815ca94849ce693574d7.png" width="1258" referrerpolicy="no-referrer"></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:justify"><span><span><span>        除此之外，还新增了</span>SmartBI<span>报表系统集成功能，可以在流程，内容管理以及门户页面中展示报表。</span></span></span><span><span><span>该功能旨在帮助企业快速搭建企业报表平台，将营销、财务、人力等企业内部流转的数据进行整合加工，构造出不同部门的业务模型，帮助快速生成业务报表等数据报告。</span></span></span></p> 
<p style="margin-left:0.0001pt; margin-right:0px; text-align:center"><span><span><span><img alt height="933" src="https://oscimg.oschina.net/oscnet/up-eff73e17b7b60d296523a198d824e5758da.png" width="1215" referrerpolicy="no-referrer"></span></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:justify"><span><span><span>        另外，目前庆双节活动正在火热进行中（</span>2021.10.24~2021.11.11<span>），兰德网络免费送</span>O2OA<span>技术培训！报名另赠超值</span>8<span>折技术支持服务优惠券，购买技术支持还赠送原价</span>12500<span>元的超值应用开发服务，详情可以移步官网</span><span>查看：</span><u>https://www.o2oa.net/</u></span></span></p> 
<p style="margin-left:.0001pt; margin-right:0; text-align:justify"><span><span>O2OA V6.4</span></span><span><span>还包含其他的功能更新和问题修正，让平台更稳定，用户操作更方便：</span></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">功能新增<br> [流程表单]新增了新HTML编辑器组件：TinyMCE</p> 
<p>[流程表单]新增了从本地拖动图片、从word复制图片、从html片段中复制图片到CKEditor并上传到服务器的功能</p> 
<p>[流程表单]新增了手写板组件，并修改了移动端手写板的界面</p> 
<p>[内容管理]栏目设置中增加了默认阅读表单和默认编辑表单的设置</p> 
<p>[内容管理]分类设置中增加了文档字段映射的功能</p> 
<p>[数据中心]新增了数据中心应用的界面导航配置功能</p> 
<p>[用户认证]新增了安全注销功能</p> 
<p>[用户认证]新增了基于LDAP认证功能</p> 
<p>[平台]新增了三员管理功能</p> 
<p>[平台架构]新增了支持vue3进行前端component进行二次开发的支持</p> 
<p>[门户管理]新增了Element前端组件支持</p> 
<p>功能优化</p> 
<p>[流程表单]优化了数字组件允许使用空字符串作为默认值</p> 
<p>[流程表单]表单模板中的数据网格组件替换为数据表格</p> 
<p>[会议管理]优化了会议申请邀请人选择功能，从只能选择人员变更为可以选择身份、人员、组织和群组。</p> 
<p>[会议管理]会议申请保存后可以修改邀请人了。</p> 
<p>[人员选择]选人范围优先使用id改为优先使用distinguishedName，避免设计元素迁移造成选人出错的问题。</p> 
<p>[平台]禁用api访问的时候同时禁用源代码访问</p> 
<p>[系统认证]未登录或权限不足返回特定httpstatus</p> 
<p>[消息中心]登录后返回的ws消息改为最新10条</p> 
<p>[云文件]file模块增加根据url上传文件</p> 
<p>[人员组织]优化了职务查询慢的问题</p> 
<p>[系统登录]优化了图片验证码，升级为googlecode插件</p> 
<p>[平台架构]HttpConnection类增加超时处理</p> 
<p>问题修复</p> 
<p>[数据中心]修复了设计端列表界面自建表和查询语句的黏贴可能不成功的问题</p> 
<p>[数据中心]修复了导入模型excel导入时超过26个英文字母的问题</p> 
<p>[流程表单]修复了数据表格和数据模板在拆分情况下的问题</p> 
<p>[流程表单]修复了数据表格通用样式优先于单元格样式的问题</p> 
<p>[流程表单]修复了数据表格导入时日期列下标不对的问题 </p> 
<p>[流程表单]修复了数据网格、数据表格、数据模板，queryLoad、load和postLoad会执行两次的问题</p> 
<p>[考勤管理]修复了考勤申诉设置报错的问题</p> 
<p>[用户认证]记录request请求中擦除密码的记录</p> 
<p>[统一搜索]修复了搜索切词报错升级tika到1.27</p> 
<p>[流程平台]修复了导入同版本流程被重命名的问题</p> 
<p>[流程平台]修复了催办提醒10分钟内可以无限提醒问题</p> 
<p>[内容管理]修复了文档查看权限校验错误的问题</p> 
<p>[内容管理]修复了栏目icon获取图片主色调内存溢出问题</p> 
<p>[流程平台]修复了办公中心待阅筛选条件未去重的问题</p> 
<p>[流程平台]修复了待办已办根据标题查询未过滤权限的问题</p> 
<p>[流程平台]修复了公文编辑器word转换时，在IE中版记显示页码错误的问题</p> 
<p>[门户管理]修复了门户页面设计dom列表无法滚动的问题</p>
                                        </div>
                                      
</div>
            