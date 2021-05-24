
---
title: 'Nacos 2.0.1 发布，微服务的注册中心和配置中心将更加健壮'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-1e40f51a564c888d59cae46516cc94a63b8.png'
author: 开源中国
comments: false
date: Mon, 24 May 2021 11:04:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-1e40f51a564c888d59cae46516cc94a63b8.png'
---

<div>   
<div class="content">
                                                                    
                                                        <h2>一、前言</h2> 
<p>自nacos2.0.0于2021年3月发布正式版以来，发现nacos2的版本，带上了性能和速度上的明显提升，至项目的启动速度也明显变快。如果你还没有升级的话，那么2.0.1的小版本更新或者让你在多个场景使用得更加顺畅。特别是K8S上的一些BUG的解决。</p> 
<h2>二、发行说明</h2> 
<p>该版本主要修复了k8s环境中Jraft领导者选择的稳定性，并修复了<code>Server is Down</code>频繁抛出错误的问题。<br> 此外，nacos-istio插件和模块中的2.0.1支持XDS协议的MCP。</p> 
<p><span style="background-color:#ffffff; color:#24292e">详细信息请参见以下内容：</span></p> 
<h3>2.1 <span style="color:#24292e"><span style="background-color:#ffffff">特征</span></span></h3> 
<ul> 
 <li>支持ldap登录。</li> 
 <li>在xds上支持mcp。</li> 
 <li>支持服务列表添加视图订户。</li> 
 <li>支持nacos 2.0的客户端加密插件。</li> 
</ul> 
<h3>2.2 <span style="color:#24292e">增强功能</span></h3> 
<ul> 
 <li>推送支持配置一些参数</li> 
 <li>解决<code>Server is Down</code>了k8s环境中的问题。</li> 
 <li>使用GRPC协议注册实例时检查isUseGrpcFeatures</li> 
</ul> 
<h3>2.3 <span style="color:#24292e"><span style="background-color:#ffffff">重构和代码质量</span></span></h3> 
<ul> 
 <li><span style="background-color:#ffffff; color:#24292e">将Distro Config重构为单例并替换GlobalConfig。</span></li> 
</ul> 
<h3>2.4 <span style="color:#24292e">错误修复</span></h3> 
<ul> 
 <li>修复实例节拍仅由负责的服务器运行。</li> 
 <li>修复publishConfig丢失的类型。</li> 
 <li>修复初始化服务器列表失败时的NPE。</li> 
 <li>修复了服务连接到nacos时在ConfigController中引发NoSuchFieldException的问题。</li> 
 <li>修复pageNo大于服务编号时的查询错误。</li> 
 <li>修复未知的订阅者应用程序</li> 
 <li>修复ThreadPool使用问题，并添加了一些发行版监视器。</li> 
 <li>修复了无法关闭NacosConfigService的问题。</li> 
 <li>修复客户端1.X的udp频繁推送。</li> 
 <li>修复Nacos 2.0客户端身份验证可能对非公共名称空间无效。</li> 
 <li>从旧版本服务器接收到状态后，将状态更改为UP。</li> 
</ul> 
<p><img height="259" src="https://oscimg.oschina.net/oscnet/up-1e40f51a564c888d59cae46516cc94a63b8.png" width="600" referrerpolicy="no-referrer"></p> 
<p>项目地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Falibaba%2Fnacos" target="_blank">https://github.com/alibaba/nacos</a></p> 
<p>文档地址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fnacos.io%2Fzh-cn%2F" target="_blank">https://nacos.io/zh-cn/</a></p> 
<h2>三、应用案例</h2> 
<p>MateCloud已经同步升级至该版本，欢迎体验。</p>
                                        </div>
                                      
</div>
            