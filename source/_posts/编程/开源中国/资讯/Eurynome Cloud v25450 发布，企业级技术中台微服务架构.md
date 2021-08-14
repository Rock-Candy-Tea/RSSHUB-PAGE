
---
title: 'Eurynome Cloud v2.5.4.50 发布，企业级技术中台微服务架构'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1535'
author: 开源中国
comments: false
date: Sat, 14 Aug 2021 07:46:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1535'
---

<div>   
<div class="content">
                                                                                            <p>Eurynome Cloud v2.5.4.50 已经发布，企业级技术中台微服务架构</p> 
<p>此版本更新内容包括：</p> 
<p>v2.5.4.50</p> 
<ol> 
 <li>优化服务本地权限存储逻辑，解决权限属性数据重复存储，不会替换问题。</li> 
 <li>重新梳理Spring Security OAuth2 方法级表达式动态权限鉴权逻辑，摒弃无用的权限验证Voter逻辑，使用统一逻辑实现@PreAuthorize注解权限的全面动态可配置化。统一平台接口白名单，IP地址白名单，以及Scope绑定URL的管理。</li> 
 <li>重构UserDetails用户信息组织逻辑，使用Spring Security标准代码，替换自定义逻辑代码，降低代码冗余，与自研方法级动态权限完美融合。</li> 
 <li>优化平台权限从Controller扫描、汇总存储至服务器以及动态修改后最终回传同步至服务的整理逻辑以及事件流。完美支持单体式架构、UPMS自身应用需求、分布式架构以及分布式各服务多实例等各种应用场景。</li> 
 <li>修复部分已知BUG，将部分代码中日志由@Slf4j改回传统日志编写方式，一方面提高编译效率，另一方面解决源代码包查看时Idea提醒代码不一致问题。</li> 
 <li>清理系统无用代码。</li> 
 <li>增加方法级动态权限演示动图，更新Readme</li> 
</ol> 
<p>详情查看：<a href="https://gitee.com/herodotus/eurynome-cloud/releases/v2.5.4.50">https://gitee.com/herodotus/eurynome-cloud/releases/v2.5.4.50</a></p>
                                        </div>
                                      
</div>
            