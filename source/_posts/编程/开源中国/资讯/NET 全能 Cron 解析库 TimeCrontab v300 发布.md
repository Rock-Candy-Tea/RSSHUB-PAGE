
---
title: '.NET 全能 Cron 解析库 TimeCrontab v3.0.0 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://img.shields.io/badge/license-MIT-orange?cacheSeconds=10800'
author: 开源中国
comments: false
date: Thu, 11 Aug 2022 14:03:00 GMT
thumbnail: 'https://img.shields.io/badge/license-MIT-orange?cacheSeconds=10800'
---

<div>   
<div class="content">
                                                                                            <h2>序言</h2> 
<p>在重构 Furion 的定时任务模块时发现 Hangfire 开源的 Cron 解析工具类不够强大：<u>不支持星期，不支持完整的 Cron 表达式解析</u>。<strong>翻遍了 Github 和 Nuget 没找到一个完完整整支持 Cron 的 .NET 库</strong>。</p> 
<p><span style="color:#3498db">所以，机会来了</span>。😊</p> 
<hr> 
<h1 style="margin-left:0px; margin-right:0px">TimeCrontab</h1> 
<p style="color:#40485b; margin-left:0px; margin-right:0px"><a href="https://gitee.com/dotnetchina/TimeCrontab/blob/master/LICENSE"><img alt="license" src="https://img.shields.io/badge/license-MIT-orange?cacheSeconds=10800" referrerpolicy="no-referrer"></a><span style="background-color:#ffffff; color:#40485b"><span> </span></span><a href="https://gitee.com/link?target=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FTimeCrontab"><img alt="nuget" src="https://img.shields.io/nuget/v/TimeCrontab.svg?cacheSeconds=10800" referrerpolicy="no-referrer"></a><span style="background-color:#ffffff; color:#40485b"><span> </span></span><a href="https://gitee.com/dotnetchina"><img alt="dotNET China" src="https://img.shields.io/badge/organization-dotNET%20China-yellow?cacheSeconds=10800" referrerpolicy="no-referrer"></a></p> 
<p style="color:#40485b; margin-left:0px; margin-right:0px"> </p> 
<p style="color:#40485b; margin-left:0px; margin-right:0px">.NET 全能 Cron 表达式解析库，支持 Cron 完整特性。</p> 
<p style="color:#40485b; margin-left:0px; margin-right:0px"><img alt="TimeCrontab.drawio" src="https://gitee.com/dotnetchina/TimeCrontab/raw/master/drawio/TimeCrontab.drawio.png" referrerpolicy="no-referrer"></p> 
<h2 style="margin-left:0px; margin-right:0px">特性</h2> 
<ul> 
 <li>支持 Cron 完整特性</li> 
 <li>超高性能</li> 
 <li>易拓展</li> 
 <li>很小，仅<span> </span><code>4KB</code></li> 
 <li>无第三方依赖</li> 
 <li>跨平台</li> 
 <li>高质量代码和良好单元测试</li> 
 <li>支持<span> </span><code>.NET Framework 3.5+</code><span> </span>及后续版本</li> 
</ul> 
<h2 style="margin-left:0px; margin-right:0px">安装</h2> 
<ul> 
 <li><a href="https://gitee.com/link?target=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FTimeCrontab">Package Manager</a></li> 
</ul> 
<div style="text-align:left"> 
 <pre><span><span>Install-Package</span><span style="color:#bbbbbb"> </span><span>TimeCrontab</span></span></pre> 
 <div style="text-align:left"> 
  <ul> 
   <li style="text-align:left"><a href="https://gitee.com/link?target=https%3A%2F%2Fwww.nuget.org%2Fpackages%2FTimeCrontab">.NET CLI</a></li> 
  </ul> 
  <div style="text-align:left"> 
   <pre><span><span>dotnet</span><span style="color:#bbbbbb"> </span><span>add</span><span style="color:#bbbbbb"> </span><span>package</span><span style="color:#bbbbbb"> </span><span>TimeCrontab</span></span></pre> 
   <div style="text-align:left"> 
    <h2 style="margin-left:0px; margin-right:0px; text-align:left">快速入门</h2> 
    <p style="color:#40485b; margin-left:0px; margin-right:0px; text-align:left">我们在<a href="https://gitee.com/dotnetchina/TimeCrontab/blob/net6/samples">主页</a>上有不少例子，这是让您入门的第一个：</p> 
    <p style="color:#40485b; margin-left:0px; margin-right:0px; text-align:left"><strong>常规格式</strong>：分 时 天 月 周</p> 
    <div style="text-align:left"> 
     <pre><span><strong style="color:#445588">var</strong> <span>crontab</span> <span>=</span> <span>Crontab</span><span>.</span><strong style="color:#990000">Parse</strong><span>(</span><span style="color:#dd2200">"* * * * *"</span><span>);</span></span>
<span><strong style="color:#445588">var</strong> <span>nextOccurrence</span> <span>=</span> <span>crontab</span><span>.</span><strong style="color:#990000">GetNextOccurrence</strong><span>(</span><span>DateTime</span><span>.</span><span>Now</span><span>);</span></span></pre> 
     <div style="text-align:left"> 
      <p style="color:#40485b; margin-left:0px; margin-right:0px; text-align:left"><strong>支持年份</strong>：分 时 天 月 周 年</p> 
      <div style="text-align:left"> 
       <pre><span><strong style="color:#445588">var</strong> <span>crontab</span> <span>=</span> <span>Crontab</span><span>.</span><strong style="color:#990000">Parse</strong><span>(</span><span style="color:#dd2200">"* * * * * *"</span><span>,</span> <span>CronStringFormat</span><span>.</span><span>WithYears</span><span>);</span></span>
<span><strong style="color:#445588">var</strong> <span>nextOccurrence</span> <span>=</span> <span>crontab</span><span>.</span><strong style="color:#990000">GetNextOccurrence</strong><span>(</span><span>DateTime</span><span>.</span><span>Now</span><span>);</span></span></pre> 
       <div style="text-align:left"> 
        <p style="color:#40485b; margin-left:0px; margin-right:0px; text-align:left"><strong>支持秒数</strong>：秒 分 时 天 月 周</p> 
        <div style="text-align:left"> 
         <pre><span><strong style="color:#445588">var</strong> <span>crontab</span> <span>=</span> <span>Crontab</span><span>.</span><strong style="color:#990000">Parse</strong><span>(</span><span style="color:#dd2200">"* * * * * *"</span><span>,</span> <span>CronStringFormat</span><span>.</span><span>WithSeconds</span><span>);</span></span>
<span><strong style="color:#445588">var</strong> <span>nextOccurrence</span> <span>=</span> <span>crontab</span><span>.</span><strong style="color:#990000">GetNextOccurrence</strong><span>(</span><span>DateTime</span><span>.</span><span>Now</span><span>);</span></span></pre> 
         <div style="text-align:left"> 
          <p style="color:#40485b; margin-left:0px; margin-right:0px; text-align:left"><strong>支持秒和年</strong>：秒 分 时 天 月 周 年</p> 
          <div style="text-align:left"> 
           <pre><span><strong style="color:#445588">var</strong> <span>crontab</span> <span>=</span> <span>Crontab</span><span>.</span><strong style="color:#990000">Parse</strong><span>(</span><span style="color:#dd2200">"* * * * * * *"</span><span>,</span> <span>CronStringFormat</span><span>.</span><span>WithSecondsAndYears</span><span>);</span></span>
<span><strong style="color:#445588">var</strong> <span>nextOccurrence</span> <span>=</span> <span>crontab</span><span>.</span><strong style="color:#990000">GetNextOccurrence</strong><span>(</span><span>DateTime</span><span>.</span><span>Now</span><span>);</span></span></pre> 
           <div style="text-align:left"> 
            <p style="color:#40485b; margin-left:0px; margin-right:0px; text-align:left"><strong>Macro 标识符</strong></p> 
            <div style="text-align:left"> 
             <pre><span><strong style="color:#445588">var</strong> <span>secondly</span> <span>=</span> <span>Crontab</span><span>.</span><span>Secondly</span><span>;</span>    <span style="color:#888888">// 每秒</span></span>
<span><strong style="color:#445588">var</strong> <span>minutely</span> <span>=</span> <span>Crontab</span><span>.</span><span>Minutely</span><span>;</span>    <span style="color:#888888">// 每分钟</span></span>
<span><strong style="color:#445588">var</strong> <span>hourly</span> <span>=</span> <span>Crontab</span><span>.</span><span>Hourly</span><span>;</span>    <span style="color:#888888">// 每小时</span></span>
<span><strong style="color:#445588">var</strong> <span>daily</span> <span>=</span> <span>Crontab</span><span>.</span><span>Daily</span><span>;</span>  <span style="color:#888888">// 每天 00:00:00</span></span>
<span><strong style="color:#445588">var</strong> <span>monthly</span> <span>=</span> <span>Crontab</span><span>.</span><span>Monthly</span><span>;</span>  <span style="color:#888888">// 每月 1 号 00:00:00</span></span>
<span><strong style="color:#445588">var</strong> <span>weekly</span> <span>=</span> <span>Crontab</span><span>.</span><span>Weekly</span><span>;</span>    <span style="color:#888888">// 每周日 00：00：00</span></span>
<span><strong style="color:#445588">var</strong> <span>yearly</span> <span>=</span> <span>Crontab</span><span>.</span><span>Yearly</span><span>;</span>    <span style="color:#888888">// 每年 1 月 1 号 00:00:00</span></span></pre> 
             <div style="text-align:left"> 
              <p style="color:#40485b; margin-left:0px; margin-right:0px; text-align:left"><a href="https://gitee.com/dotnetchina/TimeCrontab/blob/net6/docs">更多文档</a></p> 
              <h2 style="margin-left:0px; margin-right:0px; text-align:left">文档</h2> 
              <p style="color:#40485b; margin-left:0px; margin-right:0px; text-align:left">您可以在<a href="https://gitee.com/dotnetchina/TimeCrontab/blob/net6/docs">主页</a>找到 TimeCrontab 文档。</p> 
              <h2 style="margin-left:0px; margin-right:0px; text-align:left">贡献</h2> 
              <p style="color:#40485b; margin-left:0px; margin-right:0px; text-align:left">该存储库的主要目的是继续发展 TimeCrontab 核心，使其更快、更易于使用。TimeCrontab 的开发在<span> </span><a href="https://gitee.com/dotnetchina/TimeCrontab">Gitee</a><span> </span>上公开进行，我们感谢社区贡献错误修复和改进。</p> 
              <h2 style="text-align:left">测试</h2> 
              <p style="text-align:left">支持 .NET Framework 3.5+ 及后续版本（含 .NET Core +，.NET 5+）</p> 
              <pre><code class="language-cs">using System;
using Xunit;

namespace TimeCrontab.UnitTests;

public class TimeCrontabUnitTests
&#123;
    [Theory]
    [InlineData("* * * * *", "* * * * *", CronStringFormat.Default)]
    [InlineData("0 0 31W * *", "0 0 31W * *", CronStringFormat.Default)]
    [InlineData("0 23 ? * MON-FRI", "0 23 ? * 1-5", CronStringFormat.Default)]
    [InlineData("*/5 * * * *", "*/5 * * * *", CronStringFormat.Default)]
    [InlineData("30 11 * * 1-5", "30 11 * * 1-5", CronStringFormat.Default)]
    [InlineData("23 12 * JAN *", "23 12 * 1 *", CronStringFormat.Default)]
    [InlineData("* * * * MON#3", "* * * * 1#3", CronStringFormat.Default)]
    [InlineData("*/5 * L JAN *", "*/5 * L 1 *", CronStringFormat.Default)]
    [InlineData("0 0 ? 1 MON#1", "0 0 ? 1 1#1", CronStringFormat.Default)]
    [InlineData("0 0 LW * *", "0 0 LW * *", CronStringFormat.Default)]
    [InlineData("0 30 10-13 ? * WED,FRI", "0 30 10-13 ? * 3,5", CronStringFormat.WithSeconds)]
    [InlineData("0 */5 * * * *", "0 */5 * * * *", CronStringFormat.WithSeconds)]
    [InlineData("0 0/1 * * * ?", "0 */1 * * * ?", CronStringFormat.WithSeconds)]
    [InlineData("5-10 30-35 10-12 * * *", "5-10 30-35 10-12 * * *", CronStringFormat.WithSeconds)]
    public void TestParse(string expression, string outputString, CronStringFormat format)
    &#123;
        var output = Crontab.Parse(expression, format).ToString();
        Assert.Equal(outputString, output);
    &#125;

    [Theory]
    [InlineData("* * * * *", "2021-01-01 00:01:00", CronStringFormat.Default)]
    [InlineData("0 0 31W * *", "2021-01-29 00:00:00", CronStringFormat.Default)]
    [InlineData("0 23 ? * MON-FRI", "2021-01-01 23:00:00", CronStringFormat.Default)]
    [InlineData("*/5 * * * *", "2021-01-01 00:05:00", CronStringFormat.Default)]
    [InlineData("30 11 * * 1-5", "2021-01-01 11:30:00", CronStringFormat.Default)]
    [InlineData("23 12 * JAN *", "2021-01-01 12:23:00", CronStringFormat.Default)]
    [InlineData("* * * * MON#3", "2021-01-18 00:00:00", CronStringFormat.Default)]
    [InlineData("*/5 * L JAN *", "2021-01-31 00:00:00", CronStringFormat.Default)]
    [InlineData("0 0 ? 1 MON#1", "2021-01-04 00:00:00", CronStringFormat.Default)]
    [InlineData("0 0 LW * *", "2021-01-29 00:00:00", CronStringFormat.Default)]
    [InlineData("0 30 10-13 ? * WED,FRI", "2021-01-01 10:30:00", CronStringFormat.WithSeconds)]
    [InlineData("0 */5 * * * *", "2021-01-01 00:05:00", CronStringFormat.WithSeconds)]
    [InlineData("0 0/1 * * * ?", "2021-01-01 00:01:00", CronStringFormat.WithSeconds)]
    [InlineData("5-10 30-35 10-12 * * *", "2021-01-01 10:30:05", CronStringFormat.WithSeconds)]
    public void TestGetNextOccurence(string expression, string nextOccurenceString, CronStringFormat format)
    &#123;
        var beginTime = new DateTime(2021, 1, 1, 0, 0, 0);
        var crontab = Crontab.Parse(expression, format);
        var nextOccurence = crontab.GetNextOccurrence(beginTime);
        Assert.Equal(nextOccurenceString, nextOccurence.ToString("yyyy-MM-dd HH🇲🇲ss"));
    &#125;
&#125;
</code></pre> 
              <span>​</span> 
              <p><img height="768" src="https://oscimg.oschina.net/oscnet/up-0222a4994bf5648f7850a612e7ded824411.png" width="1037" referrerpolicy="no-referrer"></p> 
              <h2 style="margin-left:0px; margin-right:0px; text-align:left">许可证</h2> 
              <p style="color:#40485b; margin-left:0px; margin-right:0px; text-align:left">TimeCrontab 采用<span> </span><a href="https://gitee.com/dotnetchina/TimeCrontab/blob/net6/LICENSE">MIT</a><span> </span>开源许可证。</p> 
              <div style="text-align:left"> 
               <pre><span>MIT License</span>

<span>Copyright (c) 2020-2022 百小僧, Baiqian Co.,Ltd.</span>

<span>Permission is hereby granted, free of charge, to any person obtaining a copy</span>
<span>of this software and associated documentation files (the "Software"), to deal</span>
<span>in the Software without restriction, including without limitation the rights</span>
<span>to use, copy, modify, merge, publish, distribute, sublicense, and/or sell</span>
<span>copies of the Software, and to permit persons to whom the Software is</span>
<span>furnished to do so, subject to the following conditions:</span>

<span>The above copyright notice and this permission notice shall be included in all</span>
<span>copies or substantial portions of the Software.</span>

<span>THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR</span>
<span>IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,</span>
<span>FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE</span>
<span>AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER</span>
<span>LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,</span>
<span>OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE</span>
<span>SOFTWARE.</span></pre> 
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
    </div> 
   </div> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            