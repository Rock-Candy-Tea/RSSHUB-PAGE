
---
title: 'pacebox-springboot 2020.0.3.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4251'
author: 开源中国
comments: false
date: Fri, 11 Jun 2021 11:09:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4251'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="text-align:left">pacebox-springboot 融合封装已发布，旨在提供快速开发脚手架、打造更好的开源生态环境。</p> 
<p style="text-align:left">希望有志同道合的朋友一起维护该软件、打造一款快速应用开发级生态框架。</p> 
<pre style="text-align:left">此版本对应<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">spring</span></span></span></span></span></span> <span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">cloud</span></span></span></span></span></span> 2020<span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">.0</span></span></span></span></span></span><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1"><span style="color:#6f42c1">.0</span></span></span></span></span></span>版本,命名与<span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">spring</span></span></span></span></span></span> <span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49"><span style="color:#d73a49">cloud</span></span></span></span></span></span>对应最后位为当时做的集成版</pre> 
<ul> 
</ul> 
<p style="text-align:left"><strong>案例</strong></p> 
<ul> 
 <li>inter-boot-demo  boot版demo</li> 
 <li>inter-micro-demo  cloud版demo（nacos+sentinel体系+权限管理+elasticsearch日志+数据加解密+分布式追踪（基于opentracing））</li> 
 <li>inter-boot-generator        代码在线生成平台</li> 
 <li>inter-boot-fastdfs             FastDFS权限文件管理（后续改名attachment、支持所有文件种类）</li> 
</ul> 
<p style="text-align:left">inter-boot-demo 主要提供权限管理（菜单、角色、用户），elasticsearch入参出参日志，数据加解密，分布式追踪（基于opentracing），</p> 
<p style="text-align:left">文件存储一包集成（支持阿里云OSS,百度云BOS，腾讯COS支持、本地存储）、</p> 
<p style="text-align:left">短信存储一键集成（支持阿里、百度、腾讯短信云）合并接入等方式</p> 
<p style="text-align:left"><strong>问题修复</strong></p> 
<pre>1：修复苹果电脑使用雪花算法生成id的问题    
2：修复使用restTemplate判断不一致问题  
</pre> 
<p style="text-align:left"><strong>组件更新</strong></p> 
<pre>1：pacebox-core 1.0.13升级到1.0.14  
2：springboot 2.4.5升级到2.5.1  
3：springcloud 2020.0.2升级到2020.0.3  </pre> 
<p style="text-align:left">注：2020.0.2.1后新增了bean唯一校验。若使用2020.0.2.1版后的请调整配置bean的方式。具体可参照boot-demo,主要为了方便直接通过注解方式进行bean获取操作。不用在使用Framework来调用使用！</p>
                                        </div>
                                      
</div>
            