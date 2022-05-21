
---
title: 'W3A SOC v1.0.10 更新，上资产采集，摸清家底'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=79'
author: 开源中国
comments: false
date: Sat, 21 May 2022 14:52:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=79'
---

<div>   
<div class="content">
                                                                                            <p style="color:#24292f; text-align:start">主要更新：</p> 
<ul> 
 <li>修复ES的BUG。</li> 
 <li>完成数据隔离的优化。</li> 
 <li>更新底层数据隔离逻辑，将工具上报的隔离完善。</li> 
 <li>修复站点重复创建的问题。</li> 
 <li>优化大盘里的Web攻击类型占比图数据，用实际站点攻击的数据做统计。</li> 
 <li>增加云上秘钥管理，支持腾讯云、阿里云秘钥托管。</li> 
 <li>增加K8S配置管理托管。</li> 
 <li>增加资产抓取配置管理。</li> 
 <li>增加云上资产快速抓取，摸清清家底。（第一版先上腾讯云）（基于元豚DevOPS的已有能力） 
  <ul> 
   <li>云服务器</li> 
   <li>DNS（域名资产）</li> 
  </ul> </li> 
 <li>工具部分增加能力： 
  <ul> 
   <li>资产快速抓取清洗上报能力</li> 
   <li>跟云原生SDK打通</li> 
  </ul> </li> 
</ul> 
<p style="color:#24292f; text-align:start">本次上架接口共计：30个，变更旧接口14个，增加新服务1个(资产采集服务)。</p> 
<p style="color:#24292f; text-align:start">重要：</p> 
<ul> 
 <li>这个版本和之前的版本不太兼容，主要在站点管理这块有点变化，</li> 
 <li>整体数据隔离有变化，如生产环境使用，请直接联系我。</li> 
</ul> 
<p style="color:#24292f; text-align:start">主要镜像：</p> 
<ul> 
 <li>registry.cn-beijing.aliyuncs.com/aidolphins_com/w3a-workapi:v1.0.10 √</li> 
 <li>registry.cn-beijing.aliyuncs.com/aidolphins_com/w3a-dashboard:v1.0.10 √</li> 
 <li>registry.cn-beijing.aliyuncs.com/aidolphins_com/w3a-openapi:v1.0.10 √</li> 
 <li>registry.cn-beijing.aliyuncs.com/aidolphins_com/w3a-agent:v1.0.10 √</li> 
 <li>registry.cn-beijing.aliyuncs.com/aidolphins_com/w3a-frontend:v1.0.10 √</li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            