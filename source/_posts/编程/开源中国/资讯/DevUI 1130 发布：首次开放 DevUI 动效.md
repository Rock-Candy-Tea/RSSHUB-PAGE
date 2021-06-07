
---
title: 'DevUI 11.3.0 发布：首次开放 DevUI 动效'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0607/142450_iAMf_2720166.png'
author: 开源中国
comments: false
date: Mon, 07 Jun 2021 06:25:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0607/142450_iAMf_2720166.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p><img src="https://static.oschina.net/uploads/space/2021/0607/142450_iAMf_2720166.png" referrerpolicy="no-referrer"></p> 
<p>DevUI 是一款面向企业中后台产品的开源前端解决方案，它倡导<code>沉浸</code>、<code>灵活</code>、<code>至简</code>的设计价值观，提倡设计者为真实的需求服务，为多数人的设计，拒绝哗众取宠、取悦眼球的设计。如果你正在开发 <code>ToB</code> 的<code>工具类产品</code>，DevUI 将是一个很不错的选择！</p> 
<h1>新增特性</h1> 
<p>新版本主要包含以下特性：</p> 
<ul> 
 <li>开放DevUI动效,参考<code>扩展服务/Animations动效</code></li> 
 <li><code>time-axis</code>组件新增交替排布、设置内容位置、自定义轴点图标、轴线样式等特性</li> 
 <li><code>toggle</code>支持开关内容展示</li> 
 <li><code>category-search</code>分类搜索tree类型支持单选，textInput类型模板支持dValidateRules校验， 分类搜索中保存过滤器名称输入框增加清空按钮</li> 
 <li><code>drawer</code>新增直接关闭方法</li> 
 <li><code>quadrant-diagram</code>象限图适配暗黑模式，象限图增加是否展示工具栏</li> 
 <li><code>pagination</code>新增自动隐藏特性</li> 
</ul> 
<h1>Bug修复</h1> 
<p>修复了以下缺陷，包含社区提的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FDevCloudFE%2Fng-devui%2Fissues" target="_blank">issue</a>和内部发现的问题。</p> 
<ul> 
 <li><code>radio</code>修复传入对象导致id重复报错的问题</li> 
 <li><code>tooltip</code>修复input变化时未刷新问题</li> 
 <li><code>button</code>修复width处理异常,以及异步icon未刷新问题</li> 
 <li><code>category-search</code>修复自定义模板必选为可选，修复cache未初始化导致比较重置时覆盖了value值</li> 
 <li><code>tree</code>修复disableSelect设置后不应触发SelectNode</li> 
 <li><code>treeSelect</code>修复单选模式下的清空所有按钮未触发绑定值的变更</li> 
 <li><code>dataTable</code>修复fixHead下实际高度不对，修复扩展区域初始值问题和demo展示问题，及timePicker报错问题</li> 
 <li><code>datePicker</code>修复分类搜索中年份选择出错问题， 修复最下行日期在选择年月时露出的问题</li> 
 <li><code>nav-sprite</code>修复样式问题和延时设置问题，解决初始化不同步的问题</li> 
 <li><code>timePicker</code>修复输入长度超过2时的报错</li> 
 <li><code>search</code>修复输入文字过长与清除图标显示重叠</li> 
 <li><code>upload</code>修改多文件上传时自动清空文件的问题，修复oneTimeUpload的文件状态显示不正确的问题</li> 
</ul> 
<h1>API变更</h1> 
<p>无</p> 
<hr> 
<p>感谢 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fxiejay97" target="_blank">@xiejay97</a> <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fyangtuantuan" target="_blank">@yangtuantuan</a> 的贡献。</p> 
<p>欢迎您一起参与DevUI的开源，我们任何形式的贡献！</p> 
<p>欢迎加DevUI小助手微信：devui-official，一起讨论组件技术和前端技术。</p> 
<p>欢迎关注我们<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2F" target="_blank">DevUI</a>组件库，点亮我们的小星星：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdevcloudfe%2Fng-devui" target="_blank">https://github.com/devcloudfe/ng-devui</a></p> 
<p>也欢迎使用DevUI新发布的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fadmin%2F" target="_blank">DevUI Admin</a>系统，开箱即用，10分钟搭建一个美观大气的后台管理系统！</p> 
<p>详细的 Release Notes，请参考：</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FDevCloudFE%2Fng-devui%2Freleases%2Ftag%2F11.3.0" target="_blank">https://github.com/DevCloudFE/ng-devui/releases/tag/11.3.0</a></p>
                                        </div>
                                      
</div>
            