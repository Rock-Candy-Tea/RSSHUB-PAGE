
---
title: 'Eurynome Cloud v2.5.4.10 已经发布，企业级技术中台微服务架构'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://images.gitee.com/uploads/images/2021/0805/182800_e8bdf46f_751495.jpeg'
author: 开源中国
comments: false
date: Thu, 05 Aug 2021 18:28:00 GMT
thumbnail: 'https://images.gitee.com/uploads/images/2021/0805/182800_e8bdf46f_751495.jpeg'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Eurynome Cloud v2.5.4.10 已经发布，企业级技术中台微服务架构</p> 
<p>此版本更新内容包括：</p> 
<p>✨ v2.5.4.10</p> 
<ol> 
 <li>全网首个实现Spring Security 动态URL权限与注解表达式权限有机整合，并且可以动态配置的微服务框架。</li> 
 <li>全面支持方法级权限控制，Security OAuth2 permitAll等方法权限以及@PreAuthorize注解权限，均支持动态配置。目前支持以下权限的动态配置： · hasRole · hasAnyRole · hasAuthority · hasAnyAuthority · hasIpAddress · #oauth2.clientHasRole · #oauth2.clientHasAnyRole · #oauth2.hasScope · #oauth2.hasAnyScope · #oauth2.hasScopeMatching · #oauth2.hasAnyScopeMatching · #oauth2.denyOAuthClient · #oauth2.isOAuth · #oauth2.isUser · #oauth2.isClient</li> 
 <li>彻底解决使用withObjectPostProcessor方式，会覆盖外部匹配规则问题。</li> 
 <li>真正实现Scope权限与URL权限的关联与管控，拓展OAuth2默认只进行Scope简单对比的实现逻辑。</li> 
 <li>实现动态权限配置的多服务同步。</li> 
 <li>暂时去除JetCache，全面使用自研支持Hibernate二级缓存的多级缓存。</li> 
 <li>修改配置文件配置</li> 
 <li>删除无用代码</li> 
</ol> 
<p><img alt="输入图片说明" src="https://images.gitee.com/uploads/images/2021/0805/182800_e8bdf46f_751495.jpeg" referrerpolicy="no-referrer"></p> 
<p>详情查看：<a href="https://gitee.com/herodotus/eurynome-cloud/releases/v2.5.4.10">https://gitee.com/herodotus/eurynome-cloud/releases/v2.5.4.10</a></p>
                                        </div>
                                      
</div>
            