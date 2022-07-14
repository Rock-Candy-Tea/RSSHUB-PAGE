
---
title: '.NET 7 Preview 6 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=925'
author: 开源中国
comments: false
date: Thu, 14 Jul 2022 07:17:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=925'
---

<div>   
<div class="content">
                                                                    
                                                        <p>.NET 7 发布了第 6 个预览版。</p> 
<p>主要变化包括：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>引入新的类型转换器</li> 
 <li>更新 System.Formats.Tar API</li> 
 <li>改进 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fdotnet-7-generic-math%2F" target="_blank">Generic Math</a>，方便 API 作者的使用</li> 
 <li>为 <span style="background-color:#ffffff; color:#333333">ML.NET </span>引入新的 <span style="background-color:#ffffff; color:#333333">Text Classification API，</span>增加了最先进的深度学习技术对于自然语言处理</li> 
 <li>对源代码生成器的多项改进</li> 
 <li>用于 RegexGenerator 的新 Roslyn 分析器和修复器，以及在 CodeGen、可观察性、JSON 序列化 / 反序列化和使用流方面的多项性能改进</li> 
</ul> 
<hr> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>类型转换器</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">新增用于新添加的原始类型<code><span>DateOnly</span></code>、<code><span>TimeOnly</span></code>、<code><span>Int128</span></code>、<code><span>UInt128</span></code>和<code><span>Half</span></code>的公开类型转换器。</p> 
<pre><code>namespace System.ComponentModel
&#123;
    public class DateOnlyConverter : System.ComponentModel.TypeConverter
    &#123;
        public DateOnlyConverter() &#123; &#125;
    &#125;

    public class TimeOnlyConverter : System.ComponentModel.TypeConverter
    &#123;
        public TimeOnlyConverter() &#123; &#125;
    &#125;

    public class Int128Converter : System.ComponentModel.BaseNumberConverter
    &#123;
        public Int128Converter() &#123; &#125;
    &#125;

    public class UInt128Converter : System.ComponentModel.BaseNumberConverter
    &#123;
        public UInt128Converter() &#123; &#125;
    &#125;

    public class HalfConverter : System.ComponentModel.BaseNumberConverter
    &#123;
        public HalfConverter() &#123; &#125;
    &#125;
&#125;</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">使用示例</p> 
<pre><code>TypeConverter dateOnlyConverter = TypeDescriptor.GetConverter(typeof(DateOnly));
// produce DateOnly value of DateOnly(1940, 10, 9)
DateOnly? date = dateOnlyConverter.ConvertFromString("1940-10-09") as DateOnly?;

TypeConverter timeOnlyConverter = TypeDescriptor.GetConverter(typeof(TimeOnly));
// produce TimeOnly value of TimeOnly(20, 30, 50)
TimeOnly? time = timeOnlyConverter.ConvertFromString("20:30:50") as TimeOnly?;

TypeConverter halfConverter = TypeDescriptor.GetConverter(typeof(Half));
// produce Half value of -1.2
Half? half = halfConverter.ConvertFromString(((Half)(-1.2)).ToString()) as Half?;

TypeConverter Int128Converter = TypeDescriptor.GetConverter(typeof(Int128));
// produce Int128 value of Int128.MaxValue which equal 170141183460469231731687303715884105727
Int128? int128 = Int128Converter.ConvertFromString("170141183460469231731687303715884105727") as Int128?;

TypeConverter UInt128Converter = TypeDescriptor.GetConverter(typeof(UInt128));
// produce UInt128 value of UInt128.MaxValue which equal 340282366920938463463374607431768211455
UInt128? uint128 = UInt128Converter.ConvertFromString("340282366920938463463374607431768211455") as UInt128?;</code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>对源代码生成器的多项改进</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>添加了对</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><code><span>IAsyncEnumerable</span><span><</span><span>T</span><span>></span></code><span style="background-color:#ffffff; color:#333333"><span> </span>(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fissues%2F59268" target="_blank">#59268</a><span style="background-color:#ffffff; color:#333333">),<span> </span></span><code><span>JsonDocument</span></code><span style="background-color:#ffffff; color:#333333">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fissues%2F59954" target="_blank">#59954</a><span style="background-color:#ffffff; color:#333333">),</span><code><span>DateOnly</span></code><span style="background-color:#ffffff; color:#333333">/</span><code><span>TimeOnly</span></code><span style="background-color:#ffffff; color:#333333">(</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fdotnet%2Fruntime%2Fissues%2F53539" target="_blank">#53539</a><span style="background-color:#ffffff; color:#333333">)<span> </span></span><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff">类型的源代码生成支持</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>。例如：</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-cpp">[<span style="color:#6a737d">JsonSerializable(typeof(typeof(MyPoco))</span>]
<span style="color:#d73a49">public</span> <span style="color:#d73a49">class</span> <span style="color:#6f42c1">MyContext</span> : <span style="color:#6f42c1">JsonSerializerContext</span> &#123;&#125;

<span style="color:#d73a49">public</span> <span style="color:#d73a49">class</span> <span style="color:#6f42c1">MyPoco</span>
&#123;
    <span style="color:#6a737d">// Use of IAsyncEnumerable that previously resulted </span>
    <span style="color:#6a737d">// in JsonSerializer.Serialize() throwing NotSupportedException </span>
    <span style="color:#d73a49">public</span> IAsyncEnumerable<<span style="color:#d73a49">int</span>> Data &#123; <span style="color:#d73a49">get</span>; <span style="color:#d73a49">set</span>; &#125; 
&#125;

<span style="color:#6a737d">// It now works and no longer throws NotSupportedException</span>
JsonSerializer.Serialize(<span style="color:#d73a49">new</span> MyPoco &#123; Data = ... &#125;, MyContext.MyPoco); </code></pre> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>改进 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fdotnet-7-generic-math%2F" target="_blank">Generic Math</a></strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>.NET 6 发布了预览版的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fpreview-features-in-net-6-generic-math%2F" target="_blank">Generic Math</a>，此特性允许 .NET 开发者在通用代码中利用静态 API，包括运算符。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span>Generic Math 极大地方便了 API 作者<span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>，因为他们使用的 API 将开始支持更多类型，而不需要每个数字类型都获得显式支持。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span><span><span><span><span style="color:#333333"><span><span><span><span><span><span><span><span><span><span><span><span style="background-color:#ffffff"><span><span><span>在 .NET 7 中，开发团队对实现进行了改进并响应了社区的反馈。有关更改和可用 API 的更多信息，<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fdotnet-7-generic-math%2F" target="_blank">点此查看</a>。</span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></span></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdevblogs.microsoft.com%2Fdotnet%2Fannouncing-dotnet-7-preview-6%2F" target="_blank">详情查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            