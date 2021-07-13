
---
title: 'DevUI 11.4.0 发布：DatePickerPro 来啦'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-d5cc84aede64a81474133246d9f45c6a50f.png'
author: 开源中国
comments: false
date: Tue, 13 Jul 2021 15:53:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-d5cc84aede64a81474133246d9f45c6a50f.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:start"><img alt src="https://oscimg.oschina.net/oscnet/up-d5cc84aede64a81474133246d9f45c6a50f.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2F" target="_blank">DevUI</a> 是一款面向企业中后台产品的开源前端解决方案，它倡导<code>沉浸</code>、<code>灵活</code>、<code>至简</code>的设计价值观，提倡设计者为真实的需求服务，为多数人的设计，拒绝哗众取宠、取悦眼球的设计。如果你正在开发 <code>ToB</code> 的<code>工具类产品</code>，DevUI 将是一个很不错的选择！</p> 
<h1 style="text-align:start">DatePickerPro</h1> 
<p style="text-align:start"><img alt="1.PNG" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c50d401fc78749d8bdaa06661482b9c4~tplv-k3u1fbpfcp-watermark.image" referrerpolicy="no-referrer"></p> 
<p style="text-align:start">本次版本我们带来了升级版的日期选择器，具体有哪些提升呢？我们一起来看看吧！</p> 
<p style="text-align:start">设计层面：</p> 
<ol> 
 <li>借鉴移动端，利用鼠标滚轮特性及精准点击特性，减少用户操作路径；</li> 
 <li>模块化设计，可以按业务需求拆分重组，搭配快速选择区，提升效率。</li> 
</ol> 
<p style="text-align:start">用户使用层面：</p> 
<ol> 
 <li>组件提供了单选/范围类型，支持日期/周/月份/年份的模式，支持各种自定义模板扩展，充分满足业务复杂场景；</li> 
 <li>通过组件封装的方式可以强管控用户的使用方法及样式，同时保证了组件的易用性和一致性；</li> 
 <li>参数及使用方式大部分继承了之前的组件，减少了用户的迁移成本。</li> 
</ol> 
<p style="text-align:start">大家快来体验吧！除此之外新版本主要有以下新增特性和BUG修复：</p> 
<h1 style="text-align:start">新增特性</h1> 
<ul> 
 <li>新增datepicker-pro组件</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fcomponents%2Fzh-cn%2Fdrawer" target="_blank">drawer</a>支持自定义模板</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fcomponents%2Fzh-cn%2Fsteps-guide" target="_blank">steps-guide</a>新增beforeChange方法，在setcurrentIndex前置执行，控制该步骤是否显示</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fcomponents%2Fzh-cn%2Fpanel" target="_blank">panel</a>支持隐藏左侧填充</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fcomponents%2Fzh-cn%2Ftransfer" target="_blank">transfer</a>增加showOptionTitleAPI来控制鼠标悬浮是否显示title，优化transfer样式</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fcomponents%2Fzh-cn%2Fcategory-search" target="_blank">category-search</a>在toggleEvent新增参数currentSelecttag</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fcomponents%2Fzh-cn%2Falert" target="_blank">alert</a>新增simple类型展示</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fcomponents%2Fzh-cn%2Fgantt" target="_blank">gantt</a>优化按需加载及超出容器自动滚动</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fcomponents%2Fzh-cn%2Fcascader" target="_blank">cascader</a>添加下拉头部自定义模板</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fcomponents%2Fzh-cn%2Ftree" target="_blank">tree</a>的删除节点方法在虚拟滚动模式下支持控制是否立即更新，兼容大数据量删除的场景</li> 
</ul> 
<p style="text-align:start">以下是 DatePickerPro 的动画效果： </p> 
<p style="text-align:start"><img alt="1626014266341.gif" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e0a124e5d901479bae58d41efbcb5162~tplv-k3u1fbpfcp-watermark.image" referrerpolicy="no-referrer"></p> 
<p style="text-align:start">以下是新旧版本日期选择器的对比图： </p> 
<p style="text-align:start"><img alt="datepicker.jpg" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2181e3b290244696b689b2bb0c856ee3~tplv-k3u1fbpfcp-watermark.image" referrerpolicy="no-referrer"></p> 
<h1 style="text-align:start">Bug修复</h1> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fcomponents%2Fzh-cn%2Fcategory-search" target="_blank">category-search</a>修复filterName类型为null时报错,修复部分下拉内容没有title的问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fcomponents%2Fzh-cn%2Fdatatable" target="_blank">datatable</a>修复checked状态更新的部分问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fcomponents%2Fzh-cn%2Ftransfer" target="_blank">transfer</a>修复特定条件下状态显示有误的问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fcomponents%2Fzh-cn%2Fpopover" target="_blank">popover</a>修复初始化弹出位置计算错误的问题</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fcomponents%2Fzh-cn%2Finput-number" target="_blank">input-number</a>修复上下按钮不能触发正则校验</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fcomponents%2Fzh-cn%2Ftime-axis" target="_blank">time-axis</a>水平默认文字居中且末尾无线，type、status表现和之前统一，修复模板data数据不正确，增加API改变时间圈颜色</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fcomponents%2Fzh-cn%2Ftree-select" target="_blank">tree-select</a>修复leafOnly条件下，父节点会显示在输入框的bug</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fcomponents%2Fzh-cn%2Fupload" target="_blank">upload</a>修复oneTimeUpload条件下，上传文件成功却进入onError事件的bug</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fcomponents%2Fzh-cn%2Ftree" target="_blank">tree</a>修复beforeAdd方法无法阻止节点添加的bug</li> 
</ul> 
<p style="text-align:start">欢迎您一起参与DevUI的开源，我们任何形式的贡献！</p> 
<p style="text-align:start">欢迎加DevUI小助手微信：devui-official，一起讨论组件技术和前端技术。</p> 
<p style="text-align:start">欢迎关注我们<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2F" target="_blank">DevUI</a>组件库，点亮我们的小星星🌟：</p> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdevcloudfe%2Fng-devui" target="_blank">https://github.com/devcloudfe/ng-devui</a></p> 
<p style="text-align:start">也欢迎使用DevUI新发布的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevui.design%2Fadmin%2F" target="_blank">DevUI Admin</a>系统，开箱即用，10分钟搭建一个美观大气的后台管理系统！</p> 
<p style="text-align:start">详细的 Release Notes，请参考：</p> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FDevCloudFE%2Fng-devui%2Freleases%2Ftag%2F11.4.0" target="_blank">https://github.com/DevCloudFE/ng-devui/releases/tag/11.4.0</a></p>
                                        </div>
                                      
</div>
            