
---
title: 'PublicCMS V4.0.202204 发布，基于 Java 的开源 CMS 系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://gitee.com/sanluan/PublicCMS/raw/master/doc/structure.png'
author: 开源中国
comments: false
date: Wed, 20 Apr 2022 14:32:00 GMT
thumbnail: 'https://gitee.com/sanluan/PublicCMS/raw/master/doc/structure.png'
---

<div>   
<div class="content">
                                                                                            <h2 style="margin-left:0; margin-right:0; text-align:left">简介</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">PublicCMS是采用2022年主流技术开发的开源JAVACMS系统。由天津黑核科技有限公司开发，架构科学，轻松支持上千万数据、千万PV；支持全站静态化，SSI，动态页面局部静态化等为您快速建站，建设大规模站点提供强大驱动，也是企业级项目产品原型的良好选择。</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">快速编译与运行</h2> 
<ul> 
 <li>编译运行</li> 
</ul> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">保证操作系统中有jdk1.8及以上</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span>cd publiccms-parent</span>
<span>mvnw clean package</span>
<span>cd publiccms/target</span>
<span>java -jar publiccms.war</span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">访问程序页面http://localhost:8080/<span> </span>,根据页面提示配置并初始化数据库 管理后台访问相对路径为http://localhost:8080/admin/<span> </span>,数据脚本内置管理员账号/密码:admin/admin</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">Public CMS架构图</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt src="https://gitee.com/sanluan/PublicCMS/raw/master/doc/structure.png" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">Public CMS管理后台 - 中文</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt src="https://gitee.com/sanluan/PublicCMS/raw/master/doc/management.png" referrerpolicy="no-referrer">程序功能修改</p> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>增加word、excel文档导入功能</li> 
 <li>增加数据源管理</li> 
 <li>增加问卷调查、试题功能</li> 
 <li>增加百度编辑器一键排版图片尺寸清理、图片统一宽度、行高、段前距、段后距、字体、字号、清除空格设置</li> 
 <li>增加封面图尺寸自定义</li> 
 <li>增加文件预览</li> 
 <li>增加图片截取功能</li> 
 <li>增加允许上传的文件类型自定义</li> 
 <li>增加团队协作资源锁定、账号登录次数，IP登录次数、注册次数锁定功能</li> 
 <li>数据字典增加子级</li> 
 <li>数据字典增加级联排除其他数据字典值规则</li> 
 <li>增加1688个新图标及图标筛选功能</li> 
 <li>增加esc关闭弹窗、ctrl+s保存、按住ctrl打开新窗口功能</li> 
 <li>增加用户头像、个人资料修改</li> 
 <li>增加重建分类childIds功能</li> 
 <li>增加重建内容全文索引字段功能(用于修复修改扩展字段是否可搜索设置)</li> 
 <li>增加内容复制分发</li> 
 <li>增加百度编辑器图片转存webp转jpg(防止从微信复制的文章ie不能浏览)</li> 
 <li>部门增加编码</li> 
 <li>用户管理页面增加部门树、部门选择页面改为异步树，取消用户昵称唯一约束</li> 
 <li>增加部门扩展字段类型</li> 
 <li>增加UI框架异常信息输出</li> 
 <li>增加后台模板自定义功能</li> 
 <li>评分改回csrf验证</li> 
 <li>增加评论审核开关、评论后重新生成内容静态页面开关</li> 
 <li>增加附件商品搜索</li> 
 <li>增加接口同域名站群支持</li> 
 <li>增加进程停止未结束任务计划恢复</li> 
 <li>增加订单导出功能</li> 
 <li>增加内容导出的自定义列</li> 
 <li>增加页面片段数据导出的自定义列</li> 
 <li>网站访问统计增加域名设置</li> 
</ol> 
<h3 style="margin-left:0; margin-right:0; text-align:left">BUG与缺陷修复</h3> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>这里是列表文本内容批量静态化不这里是列表文本再因为某一条失败而终止</li> 
 <li>自定义词库排除分词功能bug修改</li> 
 <li>搜索指令多个分类id、模型id，分类包含子分类导致无结果bug修改</li> 
 <li>推荐信息删除不生效</li> 
 <li>重定向漏洞修复</li> 
 <li>CK编辑器保存按钮跳出ui框架bug修复</li> 
 <li>内容预览页面标签类型ID对比错误修改</li> 
 <li>任务计划手动触发标记传递bug修复</li> 
 <li>添加搜索词bug修复</li> 
 <li>这里是列表文本页面片段投稿表单逻辑错误修改</li> 
</ol> 
<p><a href="https://gitee.com/sanluan/PublicCMS/blob/master/Update%20History.md">完整更新日志</a></p>
                                        </div>
                                      
</div>
            