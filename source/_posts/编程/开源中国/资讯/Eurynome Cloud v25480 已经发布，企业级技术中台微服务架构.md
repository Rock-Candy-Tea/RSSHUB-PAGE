
---
title: 'Eurynome Cloud v2.5.4.80 已经发布，企业级技术中台微服务架构'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2105'
author: 开源中国
comments: false
date: Thu, 26 Aug 2021 20:13:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2105'
---

<div>   
<div class="content">
                                                                                            <p>Eurynome Cloud v2.5.4.80 已经发布，企业级技术中台微服务架构</p> 
<p>此版本更新内容包括：</p> 
<p>⬆️v2.5.4.80</p> 
<ol> 
 <li>合并eurynome-cloud-curd包和eurynome-cloud-rest包，减少包数量，提升代码维护便捷度。</li> 
 <li>增加接口幂等处理机制，防止重复提交。增加接口防刷限制机制，防止接口恶意频繁刷新。</li> 
 <li>接口幂等和防刷机制，均支持全局配置控制，同时提供@Idempotent和@AccessLimited注解进行灵活的、个性化的配置。</li> 
 <li>接口幂等和防刷机制，缓存标记采用分布式多级缓存进行存储，将低单一访问Redis带来的访问压力，同时支持多实例数据多级缓存本地数据同步。</li> 
 <li>接口幂等和防刷机制，所涉及标记缓存时间配置全部统一支持Duration时间格式，简化配置参数，提升配置便捷度。同时，优化平台错误响应体系，返回更加友好的错误信息提示。</li> 
 <li>定义Stamp签章体系，采用统一体系，对SMS短信验证码、JustAuth State、环信Token以及接口幂等和防刷等需临时存储标记相关应用进行统一实现。同时，采用分布式多级缓存进行数据存储，降低单一访问Redis压力。</li> 
</ol> 
<p>详情查看：<a href="https://gitee.com/herodotus/eurynome-cloud/releases/v2.5.4.80">https://gitee.com/herodotus/eurynome-cloud/releases/v2.5.4.80</a></p>
                                        </div>
                                      
</div>
            