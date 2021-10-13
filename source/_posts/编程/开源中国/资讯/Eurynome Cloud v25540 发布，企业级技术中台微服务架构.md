
---
title: 'Eurynome Cloud v2.5.5.40 发布，企业级技术中台微服务架构'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9883'
author: 开源中国
comments: false
date: Wed, 13 Oct 2021 00:28:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9883'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Eurynome Cloud v2.5.5.40 已经发布，企业级技术中台微服务架构。</p> 
<p>此版本更新内容包括：</p> 
<ol> 
 <li>简化 OAuth2 资源服务器 ResourceServerConfigure 配置，代码更简洁规范。</li> 
 <li>进一步融合 OAuth2 错误体系，解决 OAuth2 部分错误提示与系统自定义错误体系不一致、不融合的问题。</li> 
 <li>解决包含路径参数的接口，可以跳过鉴权机制直接访问问题</li> 
 <li>解决人员与用户 <a href="https://www.oschina.net/onetoone">@lingting@ </a> 映射，由Jackson 反序列化实体导致 JPA 保存或修改失败问题。</li> 
 <li>优化接口统一信息反馈类别，新增空数据信息结果反馈，让信息反馈内容更加友好</li> 
 <li>补充常用正则表达式库</li> 
 <li>优化人员管理、角色管理关键信息异步校验功能，解决人员管理，使用枚举作为数据类型类型导致的修改数据错误问题。</li> 
 <li>新增为组织机构人员分配默认用户功能。</li> 
 <li>新增系统默认角色配置功能。支持机构人员、手机验证码、微信小程序、QQ、微博、百度、微信开放平台、微信公众号、企业微信二维码、企业微信网页、钉钉、钉钉账号、阿里云、淘宝、支付宝、Teambition、华为、飞书、京东、抖音、今日头条、小米、人人、美团、饿了么、酷家乐、喜马拉雅、码云、开源中国、Github、Gitlab、Stackoverflow、Coding、谷歌、微软、脸书、领英、推特、亚马逊、Slack、Line、Okta、Pinterest等多种途径或第三方登录默认角色的配置。</li> 
</ol> 
<p>BREAKING CHANGE: 新增了默认角色配置功能，需要补充导入数据，才可以运行。在<code>$&#123;project_home&#125;/services/eurynome-cloud-upms-ability/resources/sqls/update/v2.5.5.40</code>目录下，新增了补充数据脚本。导入更新数据后，再进行使用。</p> 
<p>详情查看：<a href="https://gitee.com/herodotus/eurynome-cloud/releases/v2.5.5.40">https://gitee.com/herodotus/eurynome-cloud/releases/v2.5.5.40</a></p>
                                        </div>
                                      
</div>
            