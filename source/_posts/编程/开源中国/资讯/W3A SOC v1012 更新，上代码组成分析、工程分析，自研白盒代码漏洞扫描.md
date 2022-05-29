
---
title: 'W3A SOC v1.0.12 更新，上代码组成分析、工程分析，自研白盒代码漏洞扫描'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8405'
author: 开源中国
comments: false
date: Sat, 28 May 2022 15:07:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8405'
---

<div>   
<div class="content">
                                                                                            <p style="color:#24292f; text-align:start">主要更新：</p> 
<ul> 
 <li>修复数据库事务的问题。</li> 
 <li>更换整体的图表插件，全部换成最新的echarts5.</li> 
 <li>修复前端跳转的BUG。</li> 
 <li>增加Git代码资产关联能力，在「元豚控制台」进行git的配置绑定，即可关联Git的仓库，可关联多个。</li> 
 <li>增加Gitee/GitHub资产手动录入,关联授权配置能力，可以用于拉取分析。</li> 
 <li>在站点中，可以设置关联的仓库，首次关联后，即可将对应的检测数据渲染，后台将自动通过Git配置获取代码工程进行分析，主要实现：（Java端免费，其它端后续请用商业版定制，目前后端和工具上了，前端还没有联动）</li> 
</ul> 
<ul> 
 <li>自动识别代码仓库语言，更新到资产中</li> 
 <li>自动识别代码归属哪个分类配置，全自动化匹配更新</li> 
 <li>工程的API分析，实现全部API的分析抓取，呈现投射结构。</li> 
 <li>工程的所用组件抓取，包括：组件的名称、版本、调用次数等，全方位展示。</li> 
 <li>工程的代码统计，包括代码行数的统计，全规模探测组成。</li> 
 <li>基于Golang自研开发静态白盒代码漏洞扫描能力，少量规则上架。</li> 
</ul> 
<ul> 
 <li>修复旧的CVM资产问题</li> 
 <li>修复Dns数据比对的问题</li> 
 <li>增加底层工具抓取Gitlab数据能力，并上报WorkAPI。</li> 
 <li>新增云资产删除接口，面向workAPI</li> 
 <li>新增Git仓库15个撮合接口，面向WorkAPI</li> 
 <li>对接联调站点应用里的「工程管理」渲染API，其中「质量&安全水位」、「安全风险占比」的接口还有点问题，下个版本加上，安全风险占比主要跟工具端自研代码漏洞扫描结合，得调下。</li> 
</ul> 
<p style="color:#24292f; text-align:start">PS:</p> 
<ul> 
 <li>会紧跟一个版本，最近两天，把前端部分也上了，现在工程分析只上了后端和工具部分。</li> 
</ul>
                                        </div>
                                      
</div>
            