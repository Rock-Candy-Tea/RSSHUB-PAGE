
---
title: 'W3A SOC v1.0.9 更新，增加开放平台 OpenAPI、完善文档建设'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8523'
author: 开源中国
comments: false
date: Thu, 19 May 2022 15:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8523'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#24292f; text-align:start">主要更新：</p> 
<ul> 
 <li>文档已更新到最新的内容，完善了容器化部署和非容器化部署的方式参考，在「部署管理」里,<a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fw3asoc.aidolphins.com%2F" target="_blank">http://w3asoc.aidolphins.com/</a></li> 
 <li>开放平台API文档已托管到apifox，地址在：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.apifox.cn%2Fapidoc%2Fproject-1000880" target="_blank">https://www.apifox.cn/apidoc/project-1000880</a></li> 
 <li>增加OpenAPI端，增加鉴权，该端可以直接部署到网内的边界，用于跟第三方合作输入数据内部闭环转化。（感谢debNull 的建议）</li> 
 <li>增加OpenAPI端，漏洞投喂API，第三方可以通过apifox上的文档进行自行对接。</li> 
 <li>历史的OpenAPI迁入workAPI里，workAPi对内使用，不对外，openAPi带鉴权，用于外部对接。</li> 
 <li>增加平台端授权管理，分发OpenAPI的鉴权秘钥，用于跟第三方生态交互。</li> 
 <li>增加登录后的说明文档跳转入口。</li> 
 <li>将原有的用户管理切换到右上角的控制台入口里，不再放到站点中管理。</li> 
 <li>修改了docker-compose,增加了workapi。</li> 
 <li>更改初始化的SQL文件。</li> 
</ul> 
<p style="color:#24292f; text-align:start">主要镜像：</p> 
<ul> 
 <li>registry.cn-beijing.aliyuncs.com/aidolphins_com/w3a-workapi:v1.0.9 √</li> 
 <li>registry.cn-beijing.aliyuncs.com/aidolphins_com/w3a-dashboard:v1.0.9 √</li> 
 <li>registry.cn-beijing.aliyuncs.com/aidolphins_com/w3a-openapi:v1.0.9 √</li> 
 <li>registry.cn-beijing.aliyuncs.com/aidolphins_com/w3a-agent:v1.0.9 √</li> 
 <li>registry.cn-beijing.aliyuncs.com/aidolphins_com/w3a-frontend:v1.0.9 √</li> 
</ul> 
<p> </p>
                                        </div>
                                      
</div>
            