
---
title: 'Appsmith v1.6.12 发布，应用快速构建框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=6457'
author: 开源中国
comments: false
date: Fri, 25 Feb 2022 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=6457'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">Appsmith 是一个用于构建管理面板、CRUD 应用程序和工作流的框架，它允许拖放组件来构建仪表板、使用 JavaScript 对象编写逻辑并连接到任何 API、数据库或 GraphQL 源。</span></p> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">目前 Appsmith 发布了 1.6.12 版本，带来如下改动：</span></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>新特性</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>应用程序列表页面的响应式移动 UI<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fappsmithorg%2Fappsmith%2Fpull%2F10255" target="_blank">#10255</a></li> 
 <li>S3 插件：添加一次删除多个文件的命令<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fappsmithorg%2Fappsmith%2Fpull%2F11119" target="_blank">#11119</a></li> 
 <li>能够通过富文本编辑器的工具栏插入媒体和更多格式<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fappsmithorg%2Fappsmith%2Fpull%2F11052" target="_blank">#11052</a></li> 
 <li>支持使用自签名证书运行的 REST API  <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fappsmithorg%2Fappsmith%2Fpull%2F11043" target="_blank">#11043</a></li> 
 <li>禁用通过管理设置页面配置的表单登录<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fappsmithorg%2Fappsmith%2Fpull%2F11234" target="_blank">#11234</a></li> 
 <li>支持 GET 请求中的请求正文<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fappsmithorg%2Fappsmith%2Fpull%2F7127" target="_blank">#7127</a></li> 
 <li>添加对处理逗号分隔的浮点值的支持<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fappsmithorg%2Fappsmith%2Fpull%2F11207" target="_blank">#11207</a></li> 
 <li>相机小部件中的多项增强功能<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fappsmithorg%2Fappsmith%2Fpull%2F10943" target="_blank">#10943</a></li> 
 <li>Ansible 支持在 Amazon Linux 上部署<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fappsmithorg%2Fappsmith%2Fpull%2F10466" target="_blank">#10466</a></li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>Bug修复</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复复选框表单控件的顶部边距问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fappsmithorg%2Fappsmith%2Fpull%2F10930" target="_blank">#10930</a></li> 
 <li>修复 Firestore where 子句不获取数字<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fappsmithorg%2Fappsmith%2Fpull%2F10775" target="_blank">#10775</a></li> 
 <li>修复启用多选时表格小部件中的“全选和取消全选”问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fappsmithorg%2Fappsmith%2Fpull%2F10838" target="_blank">#10838</a></li> 
 <li>修复位置更改并打开居中选项时地图图钉不居中的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fappsmithorg%2Fappsmith%2Fpull%2F10296" target="_blank">#10296</a></li> 
 <li>修复 Phone Input 和 Input 小部件在提交问题时未重置的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fappsmithorg%2Fappsmith%2Fpull%2F10860" target="_blank">#10860</a></li> 
 <li>修复文本小部件中的标题标签样式不正确的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fappsmithorg%2Fappsmith%2Fpull%2F10949" target="_blank">#10949</a></li> 
 <li>实体资源管理器中的条目现在会自动排序<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fappsmithorg%2Fappsmith%2Fpull%2F10777" target="_blank">#10777</a></li> 
 <li>修复查询中数字占位符的顺序问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fappsmithorg%2Fappsmith%2Fpull%2F11005" target="_blank">#11005</a></li> 
 <li>修复 API URL 编辑器，以垂直扩展长 URL<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fappsmithorg%2Fappsmith%2Fpull%2F10663" target="_blank">#10663</a></li> 
 <li>修复评论图标隐藏在选项卡小部件的选项卡后面的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fappsmithorg%2Fappsmith%2Fpull%2F11019" target="_blank">#11019</a></li> 
 <li>修复 Google 表格因混合数据类型而合并失败的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fappsmithorg%2Fappsmith%2Fpull%2F11089" target="_blank">#11089</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fappsmithorg%2Fappsmith%2Freleases%2Ftag%2Fv1.6.12" target="_blank">https://github.com/appsmithorg/appsmith/releases/tag/v1.6.12</a></p>
                                        </div>
                                      
</div>
            