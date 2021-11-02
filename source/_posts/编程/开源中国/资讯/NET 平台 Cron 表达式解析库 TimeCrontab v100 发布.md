
---
title: '.NET 平台 Cron 表达式解析库 TimeCrontab v1.0.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://img.shields.io/badge/license-MulanPSL--2.0-orange?cacheSeconds=10800'
author: 开源中国
comments: false
date: Tue, 02 Nov 2021 06:14:00 GMT
thumbnail: 'https://img.shields.io/badge/license-MulanPSL--2.0-orange?cacheSeconds=10800'
---

<div>   
<div class="content">
                                                                                            <h1 style="margin-left:0px; margin-right:0px; text-align:left">TimeCrontab</h1> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/dotnetchina/TimeCrontab/blob/master/LICENSE"><img alt="license" src="https://img.shields.io/badge/license-MulanPSL--2.0-orange?cacheSeconds=10800" referrerpolicy="no-referrer"></a><span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FTimeCrontab" target="_blank"><img alt="nuget" src="https://img.shields.io/nuget/v/TimeCrontab.svg?cacheSeconds=10800" referrerpolicy="no-referrer"></a><span> </span><a href="https://gitee.com/dotnetchina"><img alt="dotNET China" src="https://img.shields.io/badge/organization-dotNET%20China-yellow?cacheSeconds=10800" referrerpolicy="no-referrer"></a></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">.NET 平台 Cron 表达式解析库，支持 Cron 完整特性。</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><img alt="TimeCrontab.drawio" src="https://gitee.com/dotnetchina/TimeCrontab/raw/master/drawio/TimeCrontab.drawio.png" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">特性</h2> 
<ul> 
 <li>支持 Cron 完整特性</li> 
 <li>超高性能</li> 
 <li>易拓展</li> 
 <li>很小，仅<span> </span><code>4KB</code></li> 
 <li>无第三方依赖</li> 
 <li>跨平台</li> 
 <li>高质量代码和良好单元测试</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">安装</h2> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FTimeCrontab" target="_blank">Package Manager</a></li> 
</ul> 
<div style="text-align:left"> 
 <pre><span><span>Install-Package</span><span style="color:#bbbbbb"> </span><span>TimeCrontab</span></span></pre> 
 <ul> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FTimeCrontab" target="_blank">.NET CLI</a></li> 
 </ul> 
 <div style="text-align:left"> 
  <pre><span><span>dotnet</span><span style="color:#bbbbbb"> </span><span>add</span><span style="color:#bbbbbb"> </span><span>package</span><span style="color:#bbbbbb"> </span><span>TimeCrontab</span></span></pre> 
  <h2 style="margin-left:0; margin-right:0; text-align:left">快速入门</h2> 
  <p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">我们在<a href="https://gitee.com/dotnetchina/TimeCrontab/blob/master/samples">主页</a>上有不少例子，这是让您入门的第一个：</p> 
  <p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>常规格式</strong>：分 时 天 月 周</p> 
  <div style="text-align:left"> 
   <pre><span><strong style="color:#445588">var</strong> <span>crontab</span> <span>=</span> <span>Crontab</span><span>.</span><strong style="color:#990000">Parse</strong><span>(</span><span style="color:#dd2200">"* * * * *"</span><span>);</span></span>
<span><strong style="color:#445588">var</strong> <span>nextOccurrence</span> <span>=</span> <span>crontab</span><span>.</span><strong style="color:#990000">GetNextOccurrence</strong><span>(</span><span>DateTime</span><span>.</span><span>Now</span><span>);</span></span></pre> 
   <p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>支持年份</strong>：分 时 天 月 周 年</p> 
   <div style="text-align:left"> 
    <pre><span><strong style="color:#445588">var</strong> <span>crontab</span> <span>=</span> <span>Crontab</span><span>.</span><strong style="color:#990000">Parse</strong><span>(</span><span style="color:#dd2200">"* * * * * *"</span><span>,</span> <span>CronStringFormat</span><span>.</span><span>WithYears</span><span>);</span></span>
<span><strong style="color:#445588">var</strong> <span>nextOccurrence</span> <span>=</span> <span>crontab</span><span>.</span><strong style="color:#990000">GetNextOccurrence</strong><span>(</span><span>DateTime</span><span>.</span><span>Now</span><span>);</span></span></pre> 
    <p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>支持秒数</strong>：秒 分 时 天 月 周</p> 
    <div style="text-align:left"> 
     <pre><span><strong style="color:#445588">var</strong> <span>crontab</span> <span>=</span> <span>Crontab</span><span>.</span><strong style="color:#990000">Parse</strong><span>(</span><span style="color:#dd2200">"* * * * * *"</span><span>,</span> <span>CronStringFormat</span><span>.</span><span>WithSeconds</span><span>);</span></span>
<span><strong style="color:#445588">var</strong> <span>nextOccurrence</span> <span>=</span> <span>crontab</span><span>.</span><strong style="color:#990000">GetNextOccurrence</strong><span>(</span><span>DateTime</span><span>.</span><span>Now</span><span>);</span></span></pre> 
     <p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>支持秒和年</strong>：秒 分 时 天 月 周 年</p> 
     <div style="text-align:left"> 
      <pre><span><strong style="color:#445588">var</strong> <span>crontab</span> <span>=</span> <span>Crontab</span><span>.</span><strong style="color:#990000">Parse</strong><span>(</span><span style="color:#dd2200">"* * * * * * *"</span><span>,</span> <span>CronStringFormat</span><span>.</span><span>WithSecondsAndYears</span><span>);</span></span>
<span><strong style="color:#445588">var</strong> <span>nextOccurrence</span> <span>=</span> <span>crontab</span><span>.</span><strong style="color:#990000">GetNextOccurrence</strong><span>(</span><span>DateTime</span><span>.</span><span>Now</span><span>);</span></span></pre> 
      <p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>Macro 标识符</strong></p> 
      <div style="text-align:left"> 
       <pre><span><strong style="color:#445588">var</strong> <span>secondly</span> <span>=</span> <span>Crontab</span><span>.</span><span>Secondly</span><span>;</span>    <span style="color:#888888">// 每秒</span></span>
<span><strong style="color:#445588">var</strong> <span>minutely</span> <span>=</span> <span>Crontab</span><span>.</span><span>Minutely</span><span>;</span>    <span style="color:#888888">// 每分钟</span></span>
<span><strong style="color:#445588">var</strong> <span>hourly</span> <span>=</span> <span>Crontab</span><span>.</span><span>Hourly</span><span>;</span>    <span style="color:#888888">// 每小时</span></span>
<span><strong style="color:#445588">var</strong> <span>daily</span> <span>=</span> <span>Crontab</span><span>.</span><span>Daily</span><span>;</span>  <span style="color:#888888">// 每天 00:00:00</span></span>
<span><strong style="color:#445588">var</strong> <span>monthly</span> <span>=</span> <span>Crontab</span><span>.</span><span>Monthly</span><span>;</span>  <span style="color:#888888">// 每月 1 号 00:00:00</span></span>
<span><strong style="color:#445588">var</strong> <span>weekly</span> <span>=</span> <span>Crontab</span><span>.</span><span>Weekly</span><span>;</span>    <span style="color:#888888">// 每周日 00：00：00</span></span>
<span><strong style="color:#445588">var</strong> <span>yearly</span> <span>=</span> <span>Crontab</span><span>.</span><span>Yearly</span><span>;</span>    <span style="color:#888888">// 每年 1 月 1 号 00:00:00</span></span></pre> 
       <p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/dotnetchina/TimeCrontab/blob/master/docs">更多文档</a></p> 
       <h2 style="margin-left:0; margin-right:0; text-align:left">文档</h2> 
       <p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">您可以在<a href="https://gitee.com/dotnetchina/TimeCrontab/blob/master/docs">主页</a>找到 TimeCrontab 文档。</p> 
       <h2 style="margin-left:0; margin-right:0; text-align:left">贡献</h2> 
       <p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">该存储库的主要目的是继续发展 TimeCrontab 核心，使其更快、更易于使用。TimeCrontab 的开发在<span> </span><a href="https://gitee.com/dotnetchina/TimeCrontab">Gitee</a><span> </span>上公开进行，我们感谢社区贡献错误修复和改进。</p> 
       <h2 style="margin-left:0; margin-right:0; text-align:left">许可证</h2> 
       <p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">TimeCrontab 采用<span> </span><a href="https://gitee.com/dotnetchina/TimeCrontab/blob/master/LICENSE">MulanPSL-2.0</a><span> </span>开源许可证。</p> 
       <div style="text-align:left"> 
        <pre><span>Copyright (c) 2020-2021 百小僧, Baiqian Co.,Ltd.</span>
<span>TimeCrontab is licensed under Mulan PSL v2.</span>
<span>You can use this software according to the terms andconditions of the Mulan PSL v2.</span>
<span>You may obtain a copy of Mulan PSL v2 at:</span>
<span>            https://gitee.com/dotnetchina/TimeCrontab/blob/master/LICENSE</span>
<span>THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUTWARRANTIES OF ANY KIND, EITHER EXPRESS OR IMPLIED,INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.</span>
<span>See the Mulan PSL v2 for more details.</span></pre> 
       </div> 
      </div> 
     </div> 
    </div> 
   </div> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            