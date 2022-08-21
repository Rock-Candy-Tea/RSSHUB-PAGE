
---
title: 'EasyDomain v1.4 已经发布，领域驱动开发实用库'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8366'
author: 开源中国
comments: false
date: Sun, 21 Aug 2022 00:28:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8366'
---

<div>   
<div class="content">
                                                                                            <p>EasyDomain v1.4 已经发布，领域驱动开发实用库</p> 
<p>此版本更新内容包括：</p> 
<p>经过复杂项目的锤炼，DDD领域驱动设计库v1.4版本增强了EntityBase和EntityRule的能力。并进一步强化了领域模型在系统设计中的核心地位。</p> 
<p><strong>EntityBase实体基类增强</strong></p> 
<p>EntityBase增加了领域事件收集器(eventCollector)和业务操作收集器组件(actionCollector)，以充血模型为基础，模型本身维护一组数据，模型上的业务操作方法，对模型数据进行修改，进而产生相应的领域事件并放入事件收集器中，最终通过应用服务层事件管理器将事件发布。</p> 
<p>实体 = 模型 + 行为 + 事件</p> 
<p><strong>EntityRule实体规则增强</strong></p> 
<p>EntityRule主要增加了对业务规则的管理能力，以应对各种复杂场景下规则变化。EntityRule 增加了append、replace、remove以及reset等规则操作方法，可以灵活动态的对领域规则进行追加、替换、移除、以及重置等操作，满足多租户、多场景下的规则校验逻辑组合。</p> 
<p>详情查看：<a href="https://gitee.com/lixiaojing/easy-domain/releases/v1.4">https://gitee.com/lixiaojing/easy-domain/releases/v1.4</a></p>
                                        </div>
                                      
</div>
            