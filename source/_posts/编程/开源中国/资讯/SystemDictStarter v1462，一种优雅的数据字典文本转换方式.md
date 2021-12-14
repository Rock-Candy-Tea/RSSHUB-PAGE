
---
title: 'SystemDictStarter v1.4.6.2，一种优雅的数据字典文本转换方式'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9293'
author: 开源中国
comments: false
date: Tue, 14 Dec 2021 01:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9293'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在日常项目开发中，不免都会用到一些数据字典的信息，遇到这种场景通常都是后端把字典的文本转换好一起返回给前端，前端只需要直接展示即可。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">一般情况下后端可能需要单独给返回对象创建一个字段来存储对应的字典文本值，然后进行手动的处理，这种方式通常比较繁琐，在字段多的时候会增加更多的工作量。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>本项目基于 Jackson 的自定义注解功能实现</strong>了这一自动转换过程，不需要在对象中定义存放字典文本的字段，只需要在字段上使用 @DictText 注解，Jackson序列化的时候即可自动把字典值转换成字典文本。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>更新日志</strong></p> 
<ul> 
 <li>fix: 修复字典值使用文本分隔转换数组结果时，字典值无分隔符导致无数据问题</li> 
 <li>fix: 修复在一些多模块项目场景下获取不到 RedisTemplate<String, DictTypeVo> 导致启动失败问题</li> 
 <li>feat: 增加树形结构数据的字典文本转换支持</li> 
 <li>feat(store): 刷新字典时当 DictTypeVo#children = null 时视为删除字典类型对象</li> 
 <li>feat(store): 删除字典类型对象的同时也删除此字典类型下的所有字典值文本信息</li> 
 <li> <p>feat: RefreshDictValueEvent 增加参数设置删除单个字典值文本后字典类型无字典值列表时删除此字典类型信息</p> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>项目地址</strong></p> 
<ul style="list-style-type:disc; margin-left:20px; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span><a href="https://gitee.com/houkunlin/system-dict-starter">https://gitee.com/houkunlin/system-dict-starter</a></span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhoukunlin-starter%2Fsystem-dict-starter" target="_blank">https://github.com/houkunlin-starter/system-dict-starter</a></span></p> </li> 
</ul> 
<p style="margin-left:0; margin-right:0">从数据库读取字典数据为注解提供数据支撑使用示例代码：<a href="https://gitee.com/houkunlin/system-dict-starter/tree/main/system-dict-examples/examples-provider">system-dict-examples/examples-provider</a> </p> 
<p style="margin-left:0; margin-right:0">刷新字典使用示例代码：<a href="https://gitee.com/houkunlin/system-dict-starter/tree/main/system-dict-examples/examples-refresh-dict">system-dict-examples/examples-refresh-dict</a> </p> 
<p style="margin-left:0; margin-right:0"><span>树形结构数据转换使用示例代码：</span><a href="https://gitee.com/houkunlin/system-dict-starter/tree/main/system-dict-examples/examples-tree-dict">system-dict-examples/examples-tree-dict</a> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>简单使用文档</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/houkunlin/system-dict-starter/blob/main/usage.md">https://gitee.com/houkunlin/system-dict-starter/blob/main/usage.md</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong style="color:#333333">注解简单使用示例</strong></p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code class="language-java"><span style="color:#6a737d">// 注解的简单使用</span>
<span style="color:#032f62">@Data</span>
<span style="color:#032f62">@AllArgsConstructor</span>
class Bean &#123;
    <span style="color:#6a737d">// &#123;"userType":"1","userTypeText":"普通用户"&#125;</span>
    <span style="color:#032f62">@DictText</span>(<span style="color:#032f62">"PeopleType"</span>)
    private String userType = <span style="color:#032f62">"1"</span>;
&#125;

<span style="color:#6a737d">// 自定义字典文本输出字段</span>
<span style="color:#032f62">@Data</span>
<span style="color:#032f62">@AllArgsConstructor</span>
class Bean &#123;
    <span style="color:#6a737d">// &#123;"userType":"1","typeText":"普通用户"&#125;</span>
    <span style="color:#032f62">@DictText</span>(value = <span style="color:#032f62">"PeopleType"</span>, fieldName = <span style="color:#032f62">"typeText"</span>)
    private String userType = <span style="color:#032f62">"1"</span>;
&#125;

<span style="color:#6a737d">// 使用分隔符来存储多个字典值</span>
<span style="color:#032f62">@Data</span>
<span style="color:#032f62">@AllArgsConstructor</span>
class Bean &#123;
    <span style="color:#6a737d">// &#123;"userType":"0,1","userTypeText":"系统管理、普通用户"&#125;</span>
    <span style="color:#032f62">@DictText</span>(value = <span style="color:#032f62">"PeopleType"</span>, array = <span style="color:#032f62">@Array</span>(split = <span style="color:#032f62">","</span>))
    private String userType = <span style="color:#032f62">"0,1"</span>;
&#125;

<span style="color:#6a737d">// 使用集合来存储多个字典值</span>
<span style="color:#032f62">@Data</span>
<span style="color:#032f62">@AllArgsConstructor</span>
class Bean &#123;
     <span style="color:#6a737d">// &#123;"userType":["0","1"],"userTypeText":"系统管理、普通用户"&#125;</span>
    <span style="color:#032f62">@DictText</span>(<span style="color:#032f62">"PeopleType"</span>)
    private List<String> userType = Arrays.asList(<span style="color:#032f62">"0"</span>, <span style="color:#032f62">"1"</span>);
&#125;

<span style="color:#6a737d">// 把集合的字典文本转换成数组形式</span>
<span style="color:#032f62">@Data</span>
<span style="color:#032f62">@AllArgsConstructor</span>
class Bean &#123;
    <span style="color:#6a737d">// &#123;"userType":["0","1"],"userTypeText":["系统管理","普通用户"]&#125;</span>
    <span style="color:#032f62">@DictText</span>(value = <span style="color:#032f62">"PeopleType"</span>, array = <span style="color:#032f62">@Array</span>(toText = false))
    private List<String> userType = Arrays.asList(<span style="color:#032f62">"0"</span>, <span style="color:#032f62">"1"</span>);
&#125;

<span style="color:#6a737d">// 转换成 Map 形式在原字段上输出</span>
<span style="color:#032f62">@Data</span>
<span style="color:#032f62">@AllArgsConstructor</span>
class Bean &#123;
    <span style="color:#6a737d">// &#123;"userType":&#123;"text":"普通用户","value":"1"&#125;&#125;</span>
    <span style="color:#032f62">@DictText</span>(value = <span style="color:#032f62">"PeopleType"</span>, mapValue = DictText.Type.YES, replace = DictText.Type.YES)
    private String userType;
&#125;</code></pre>
                                        </div>
                                      
</div>
            