
---
title: 'W3A SOC v1.0.11 更新，上 Web 漏洞扫描，闭环漏洞管理'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9686'
author: 开源中国
comments: false
date: Tue, 24 May 2022 13:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9686'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#24292f; text-align:start">主要更新：</p> 
<ul> 
 <li>新增Web开源扫描的联动，可以直接联动云上的域名资产进行送检。</li> 
 <li>工具端新增漏洞扫描的联动功能，跟镜像捆绑。</li> 
 <li>平台侧新增Web漏洞扫描配置的配置控制，在「元豚控制台」入口处进入了解，可以在线修改扫描插件。（默认非专业安全人员无需了解，部署完成后天然就具备Web漏扫能力，抓取资产后，天然闭环）</li> 
 <li>Web漏洞扫描完成后，跟漏洞管理打通，目前已实现。</li> 
 <li>Web漏洞扫描增加跟腾讯云翻译的打通，漏洞详情译文，目前只对高级用户开放。</li> 
 <li>增加M1/X86_64的docker-compose区分支持。</li> 
 <li>修复部分BUG(13个)</li> 
</ul> 
<p style="color:#24292f; text-align:start">待办：</p> 
<ul> 
 <li>全流程贯穿测试。</li> 
 <li>完善文档，最佳实践部分的文件。</li> 
</ul> 
<p style="color:#24292f; text-align:start">下一步：（优先级）</p> 
<ul> 
 <li>插一个「紧急任务」，马上要护网了，完成SOC端启明星辰-cSplus系列的日志SysLog纳管，争取在护网时让老铁们能用上，联动分析。</li> 
 <li>云上全资产采集，如K8S的数据资产采集、入库。</li> 
 <li>站点管理增加资产关联匹配的能力，能够将采集到的资产通过自动化的方式匹配，也可以手动方式匹配。</li> 
 <li>SOC增加API画像，分析请求的API，绘制站点API资产地图，用于后续代码组成分析用，SCA相关。</li> 
 <li>系统漏洞扫描，漏洞直接丢漏洞管理中。</li> 
 <li>把之前元豚自动化构建K8S集群的能力融合到W3A SOC中。</li> 
</ul> 
<p style="color:#24292f; text-align:start">CentOS - x86-64:<br> registry.cn-beijing.aliyuncs.com/aidolphins_com/w3a-workapi:v1.0.11 √<br> registry.cn-beijing.aliyuncs.com/aidolphins_com/w3a-dashboard:v1.0.11 √<br> registry.cn-beijing.aliyuncs.com/aidolphins_com/w3a-openapi:v1.0.11 √<br> registry.cn-beijing.aliyuncs.com/aidolphins_com/w3a-agent:v1.0.11 √<br> registry.cn-beijing.aliyuncs.com/aidolphins_com/w3a-frontend:v1.0.11 √<br> registry.cn-beijing.aliyuncs.com/aidolphins_com/w3a-arachni:v1.0.11 √</p> 
<p style="color:#24292f; text-align:start">Mac Osx - m1<br> registry.cn-beijing.aliyuncs.com/aidolphins_com/w3a-agent:v1.0.11-m1 √<br> registry.cn-beijing.aliyuncs.com/aidolphins_com/w3a-frontend:v1.0.11-m1 √<br> registry.cn-beijing.aliyuncs.com/aidolphins_com/w3a-workapi:v1.0.11-m1 √<br> registry.cn-beijing.aliyuncs.com/aidolphins_com/w3a-dashboard:v1.0.11-m1 √<br> registry.cn-beijing.aliyuncs.com/aidolphins_com/w3a-openapi:v1.0.11-m1 √<br> registry.cn-beijing.aliyuncs.com/aidolphins_com/w3a-arachni:v1.0.11-m1 x -- Web漏洞扫描不支持在M1下运转</p> 
<p> </p>
                                        </div>
                                      
</div>
            