
---
title: 'Torna 1.12.0 发布，企业接口文档解决方案'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-0efde0858af65f8fad3849d1f6170009c30.png'
author: 开源中国
comments: false
date: Wed, 12 Jan 2022 08:48:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-0efde0858af65f8fad3849d1f6170009c30.png'
---

<div>   
<div class="content">
                                                                                            <p>Torna 1.12.0 发布，本次更新内容如下：</p> 
<ul> 
 <li>【优化】调试环境改造</li> 
 <li>【优化】调试显示图片</li> 
 <li>【优化】文档预览页树菜单显示接口数量</li> 
 <li>【优化】优化参数描述内容过长显示</li> 
 <li>【优化】优化国际化显示</li> 
 <li>【优化】优化LDAP登录，登录后同步邮箱</li> 
 <li>【修复】修复接口调试\n问题<span> </span><a href="https://gitee.com/durcframework/torna/issues/I4KODO">#I4KODO:接口调试\n问题</a></li> 
 <li>【升级】fastmybatis升级到1.10.11</li> 
 <li>【新增】文档表格页可以新增分类</li> 
</ul> 
<p><strong>调试环境改造</strong></p> 
<p>从1.12.0版本起调试功能变得更加灵活，可以复制当前配置，也可以从其它项目中导入调试配置。考虑到大部分的项目的项目它的公共请求头都是一样的，这样就不用每次新建调试环境，直接从其它环境中导入即可。</p> 
<p>此外，还可以根据不同的调试环境设置不同的请求头，从而实现环境隔离，如测试和生产的token是不一样的。</p> 
<p><strong>调试显示图片</strong></p> 
<p>如果服务端返回的是一个图片流，调试返回结果将直接显示图片</p> 
<p><strong>文档预览页树菜单显示接口数量</strong></p> 
<p>文档菜单树右侧显示接口数量，可以查看每个项目中的接口数量</p> 
<p><img height="468" src="https://oscimg.oschina.net/oscnet/up-0efde0858af65f8fad3849d1f6170009c30.png" width="435" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>关于Torna</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">企业接口文档解决方案，目标是让文档管理变得更加方便、快捷。Torna采用团队协作的方式管理和维护项目API文档，将不同形式的文档纳入进来，形成一个统一的维护方式。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Torna弥补了传统文档生成工具（如swagger）的不如之处，在保持原有功能的前提下丰富并增强了一些实用的功能。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><img alt src="https://oscimg.oschina.net/oscnet/up-47d91305f6b4e40f648ded1c23a50e3515c.png" referrerpolicy="no-referrer"></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>推荐组合</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>smart-doc + Torna实现文档全流程自动化</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">如果您使用Java语言，推荐使用<code>smart-doc + Torna</code></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/smart-doc-team/smart-doc">smart-doc</a> + Torna 组成行业领先的文档生成和管理解决方案，使用smart-doc无侵入完成Java源代码和注释提取生成API文档，自动将文档推送到Torna企业级接口文档管理平台。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">通过这套组合您可以实现：只需要写完Java注释就能把接口信息推送到Torna平台，从而实现接口预览、接口调试。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">推送的内容有：<code>接口名称/author/Path参数/Header/请求参数/返回参数/字典列表/公共错误码</code></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">如果您是非Java语言，可以使用表单页面编辑以上内容，完成后同样可以进行接口预览、调试。</p>
                                        </div>
                                      
</div>
            