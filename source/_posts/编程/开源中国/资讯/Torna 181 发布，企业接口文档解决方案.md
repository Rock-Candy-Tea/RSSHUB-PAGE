
---
title: 'Torna 1.8.1 发布，企业接口文档解决方案'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-acc4130f0d6d58f9de80875be52d9ebe385.png'
author: 开源中国
comments: false
date: Thu, 03 Jun 2021 09:07:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-acc4130f0d6d58f9de80875be52d9ebe385.png'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Torna 1.8.1 发布，本次更新内容如下：</p> 
<ul> 
 <li>【增强】支持定义数组body/数组返回</li> 
 <li>【增强】接口描述支持html标签</li> 
 <li>【增强】调试环境新增是否公开属性</li> 
 <li>【增强】调试页参数可勾选（CheckBox）</li> 
 <li>【优化】优化接口描述字段显示 <a href="https://gitee.com/durcframework/torna/pulls/9" target="_blank">pr</a></li> 
</ul> 
<p>1.8.1开始可以定义数组参数，假设接口接收的是一个json数组，如下代码：</p> 
<pre><code class="language-java">@PostMapping("postArr")
public Result postArr(@RequestBody OrderDTO[] orderDTOS) &#123;
    return null;
&#125;</code></pre> 
<p>通过定义后，文档页面展示如下：</p> 
<p><img alt height="852" src="https://oscimg.oschina.net/oscnet/up-acc4130f0d6d58f9de80875be52d9ebe385.png" width="1746" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><strong>关于Torna</strong></p> 
<p style="text-align:left">企业接口文档解决方案，目标是让文档管理变得更加方便、快捷。Torna采用团队协作的方式管理和维护项目API文档，将不同形式的文档纳入进来，形成一个统一的维护方式。</p> 
<p style="text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-bcbac54f3adc71fa0829b757f9a71e8543b.png" referrerpolicy="no-referrer"></p> 
<p style="text-align:left"><strong>特性介绍</strong></p> 
<ul> 
 <li style="text-align:left">支持接口文档增删改查</li> 
 <li style="text-align:left">支持导入外部接口（支持导入swagger、postman）</li> 
 <li style="text-align:left">支持分享文档（匿名访问、密码访问）</li> 
 <li style="text-align:left">支持OpenAPI管理接口</li> 
 <li style="text-align:left">支持字典管理</li> 
 <li style="text-align:left">支持导出为markdown格式、html格式</li> 
 <li style="text-align:left">支持文档聚合，将不同模块中的文档聚合展示</li> 
 <li style="text-align:left">支持多环境接口调试</li> 
 <li style="text-align:left">支持Mock数据</li> 
 <li style="text-align:left">支持文档权限管理，访客、开发者、管理员对应不同权限</li> 
 <li style="text-align:left">支持第三方登录接入/OAuth认证登录</li> 
 <li style="text-align:left">支持钉钉免密登录</li> 
 <li style="text-align:left">支持设置全局请求头/请求参数/响应参数</li> 
 <li style="text-align:left">支持中英文切换(i18n)</li> 
 <li style="text-align:left">支持docker运行</li> 
 <li style="text-align:left">提供swagger插件，快速导入swagger文档</li> 
 <li style="text-align:left">提供`管理模式`和`浏览模式`双模式，管理模式用来编辑文档内容，浏览模式纯粹查阅文档，界面无其它元素干扰</li> 
 <li style="text-align:left">部署简单，直接运行脚本启动程序</li> 
</ul> 
<p style="text-align:left"><strong>推荐组合</strong></p> 
<p style="text-align:left"><strong>smart-doc + Torna实现文档全流程自动化</strong></p> 
<p style="text-align:left">如果您使用Java语言，推荐使用<code>smart-doc + Torna</code></p> 
<p style="text-align:left"><a href="https://gitee.com/smart-doc-team/smart-doc">smart-doc</a> + Torna 组成行业领先的文档生成和管理解决方案，使用smart-doc无侵入完成Java源代码和注释提取生成API文档，自动将文档推送到Torna企业级接口文档管理平台。</p> 
<p style="text-align:left">通过这套组合您可以实现：只需要写完Java注释就能把接口信息推送到Torna平台，从而实现接口预览、接口调试。</p> 
<p style="text-align:left">推送的内容有：<code>接口名称/author/Path参数/Header/请求参数/返回参数/字典列表/公共错误码</code></p> 
<p style="text-align:left">如果您是非Java语言，可以使用表单页面编辑以上内容，完成后同样可以进行接口预览、调试。</p>
                                        </div>
                                      
</div>
            