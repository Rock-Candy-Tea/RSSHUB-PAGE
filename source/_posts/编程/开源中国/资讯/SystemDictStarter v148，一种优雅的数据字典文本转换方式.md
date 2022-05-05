
---
title: 'SystemDictStarter v1.4.8，一种优雅的数据字典文本转换方式'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9324'
author: 开源中国
comments: false
date: Wed, 04 May 2022 16:42:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9324'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; text-align:start"><span>在日常项目开发中，不免都会用到一些数据字典的信息，以及前端展示的时候通常也需要把这些数据字典值转换成具体字典文本信息。遇到这种场景通常都是后端把字典的文本转换好一起返回给前端，前端只需要直接展示即可。</span></p> 
<p style="color:#000000; text-align:start"><span>一般情况下后端可能需要单独给返回对象创建一个字段来存储对应的字典文本值，然后进行手动的处理，这种方式通常比较繁琐，在字段多的时候会增加更多的工作量。</span></p> 
<p style="color:#000000; text-align:start"><span>本项目基于 Jackson 的自定义注解功能实现了这一自动转换过程，不需要在对象中定义存放字典文本的字段，只需要在字段上使用</span><span style="background-color:#ffffff; color:#333333"><span> </span>@DictText 注解</span><span>，Jackson序列化的时候即可自动把字典值转换成字典文本。</span></p> 
<p style="color:#000000; text-align:start"><strong>本项目只适用使用 Jackson 做 JSON 序列化，在 fastjson 下失效</strong></p> 
<p style="color:#000000; text-align:start"> </p> 
<p style="color:#000000; text-align:start"><strong style="color:#000000"><code>v1.4.8</code><span> </span>版本已在<span> </span><code>JDK8</code><span> </span><code>JDK11</code><span> </span><code>JDK17</code><span> </span>环境下跑通所有单元测试样例</strong></p> 
<p><strong>更新日志</strong></p> 
<ul> 
 <li>fix: 修复 JDK17 下运行失败问题</li> 
 <li>feat: 重构使用字节码生成 Converter 转换器，增加 ASM 字节码支持</li> 
 <li>feat: 增加配置支持切换字节码工具：ASM/JAVASSIST</li> 
 <li>feat: 增加 DictText#dictTypeHandler 字典类型代码处理器支持，可以动态设置字段的字典类型代码</li> 
 <li>feat: 支持自定义缓存键前缀</li> 
 <li>feat: 增加树结构数据访问深度限制，防止陷入死循环</li> 
 <li>feat: DictType 注解可重复使用，支持把多个枚举字典合并到一个字典中</li> 
 <li>fix: 修复字段值为 null 时被序列化成 "null" 字符串的问题</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>项目地址</strong></p> 
<ul style="list-style-type:disc; margin-left:20px; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span><a href="https://gitee.com/houkunlin/system-dict-starter">https://gitee.com/houkunlin/system-dict-starter</a></span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhoukunlin-starter%2Fsystem-dict-starter" target="_blank">https://github.com/houkunlin-starter/system-dict-starter</a></span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">从数据库读取字典数据为注解提供数据支撑使用示例代码：<a href="https://gitee.com/houkunlin/system-dict-starter/tree/main/system-dict-examples/examples-provider">system-dict-examples/examples-provider</a> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">刷新字典使用示例代码：<a href="https://gitee.com/houkunlin/system-dict-starter/tree/main/system-dict-examples/examples-refresh-dict">system-dict-examples/examples-refresh-dict</a> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><span>树形结构数据转换使用示例代码：</span><a href="https://gitee.com/houkunlin/system-dict-starter/tree/main/system-dict-examples/examples-tree-dict">system-dict-examples/examples-tree-dict</a> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>简单使用文档</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/houkunlin/system-dict-starter/blob/main/usage.md">https://gitee.com/houkunlin/system-dict-starter/blob/main/usage.md</a></p> 
<div style="text-align:start"> 
 <div> 
  <div style="text-align:left"> 
   <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong style="color:#333333">注解简单使用示例</strong></p> 
   <pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-java"><span style="color:#6a737d"><span style="color:#6a737d">// 注解的简单使用</span></span>
<span style="color:#032f62"><span style="color:#032f62">@Data</span></span>
<span style="color:#032f62"><span style="color:#032f62">@AllArgsConstructor</span></span>
class Bean &#123;
    <span style="color:#6a737d"><span style="color:#6a737d">// &#123;"userType":"1","userTypeText":"普通用户"&#125;</span></span>
    <span style="color:#032f62"><span style="color:#032f62">@DictText</span></span>(<span style="color:#032f62"><span style="color:#032f62">"PeopleType"</span></span>)
    private String userType = <span style="color:#032f62"><span style="color:#032f62">"1"</span></span>;
&#125;

<span style="color:#6a737d"><span style="color:#6a737d">// 自定义字典文本输出字段</span></span>
<span style="color:#032f62"><span style="color:#032f62">@Data</span></span>
<span style="color:#032f62"><span style="color:#032f62">@AllArgsConstructor</span></span>
class Bean &#123;
    <span style="color:#6a737d"><span style="color:#6a737d">// &#123;"userType":"1","typeText":"普通用户"&#125;</span></span>
    <span style="color:#032f62"><span style="color:#032f62">@DictText</span></span>(value = <span style="color:#032f62"><span style="color:#032f62">"PeopleType"</span></span>, fieldName = <span style="color:#032f62"><span style="color:#032f62">"typeText"</span></span>)
    private String userType = <span style="color:#032f62"><span style="color:#032f62">"1"</span></span>;
&#125;

<span style="color:#6a737d"><span style="color:#6a737d">// 使用分隔符来存储多个字典值</span></span>
<span style="color:#032f62"><span style="color:#032f62">@Data</span></span>
<span style="color:#032f62"><span style="color:#032f62">@AllArgsConstructor</span></span>
class Bean &#123;
    <span style="color:#6a737d"><span style="color:#6a737d">// &#123;"userType":"0,1","userTypeText":"系统管理、普通用户"&#125;</span></span>
    <span style="color:#032f62"><span style="color:#032f62">@DictText</span></span>(value = <span style="color:#032f62"><span style="color:#032f62">"PeopleType"</span></span>, array = <span style="color:#032f62"><span style="color:#032f62">@Array</span></span>(split = <span style="color:#032f62"><span style="color:#032f62">","</span></span>))
    private String userType = <span style="color:#032f62"><span style="color:#032f62">"0,1"</span></span>;
&#125;

<span style="color:#6a737d"><span style="color:#6a737d">// 使用集合来存储多个字典值</span></span>
<span style="color:#032f62"><span style="color:#032f62">@Data</span></span>
<span style="color:#032f62"><span style="color:#032f62">@AllArgsConstructor</span></span>
class Bean &#123;
     <span style="color:#6a737d"><span style="color:#6a737d">// &#123;"userType":["0","1"],"userTypeText":"系统管理、普通用户"&#125;</span></span>
    <span style="color:#032f62"><span style="color:#032f62">@DictText</span></span>(<span style="color:#032f62"><span style="color:#032f62">"PeopleType"</span></span>)
    private List<String> userType = Arrays.asList(<span style="color:#032f62"><span style="color:#032f62">"0"</span></span>, <span style="color:#032f62"><span style="color:#032f62">"1"</span></span>);
&#125;

<span style="color:#6a737d"><span style="color:#6a737d">// 把集合的字典文本转换成数组形式</span></span>
<span style="color:#032f62"><span style="color:#032f62">@Data</span></span>
<span style="color:#032f62"><span style="color:#032f62">@AllArgsConstructor</span></span>
class Bean &#123;
    <span style="color:#6a737d"><span style="color:#6a737d">// &#123;"userType":["0","1"],"userTypeText":["系统管理","普通用户"]&#125;</span></span>
    <span style="color:#032f62"><span style="color:#032f62">@DictText</span></span>(value = <span style="color:#032f62"><span style="color:#032f62">"PeopleType"</span></span>, array = <span style="color:#032f62"><span style="color:#032f62">@Array</span></span>(toText = false))
    private List<String> userType = Arrays.asList(<span style="color:#032f62"><span style="color:#032f62">"0"</span></span>, <span style="color:#032f62"><span style="color:#032f62">"1"</span></span>);
&#125;

<span style="color:#6a737d"><span style="color:#6a737d">// 转换成 Map 形式在原字段上输出</span></span>
<span style="color:#032f62"><span style="color:#032f62">@Data</span></span>
<span style="color:#032f62"><span style="color:#032f62">@AllArgsConstructor</span></span>
class Bean &#123;
    <span style="color:#6a737d"><span style="color:#6a737d">// &#123;"userType":&#123;"text":"普通用户","value":"1"&#125;&#125;</span></span>
    <span style="color:#032f62"><span style="color:#032f62">@DictText</span></span>(value = <span style="color:#032f62"><span style="color:#032f62">"PeopleType"</span></span>, mapValue = DictText.Type.YES, replace = DictText.Type.YES)
    private String userType;
&#125;</code></pre> 
  </div> 
 </div> 
</div>
                                        </div>
                                      
</div>
            