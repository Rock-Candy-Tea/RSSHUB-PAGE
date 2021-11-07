
---
title: 'SystemDictStarter v1.4.5 一种优雅的数据字典文本转换方式'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4400'
author: 开源中国
comments: false
date: Sun, 07 Nov 2021 11:36:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4400'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在日常项目开发中，不免都会用到一些数据字典的信息，遇到这种场景通常都是后端把字典的文本转换好一起返回给前端，前端只需要直接展示即可。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">一般情况下后端可能需要单独给返回对象创建一个字段来存储对应的字典文本值，然后进行手动的处理，这种方式通常比较繁琐，在字段多的时候会增加更多的工作量。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">本项目基于 Jackson 的自定义注解功能实现了这一自动转换过程，不需要在对象中定义存放字典文本的字段，只需要在字段上使用 @DictText 注解，Jackson序列化的时候即可自动把字典值转换成字典文本。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>更新日志</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">功能代码变更</p> 
<ul> 
 <li>feat: 增加一个 DictText#replace 配置字段，标记是否用字典文本值替换字典值（在原字段上输出字典文本值）<a href="https://gitee.com/houkunlin/system-dict-starter/issues/I4GT0N">#I4GT0N:希望增加字典替换功能</a></li> 
 <li>feat: 增加一个 RefreshDictTypeEvent 事件刷新一个完整的字典类型信息<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhoukunlin-starter%2Fsystem-dict-starter%2Fissues%2F2%23issuecomment-960424924" target="_blank">github#2</a></li> 
 <li>fix: 修复刷新单个字典值文本信息时文本信息未同步到字典类型对象里面的问题<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhoukunlin-starter%2Fsystem-dict-starter%2Fissues%2F2%23issuecomment-960423263" target="_blank">github#2</a></li> 
 <li>feat: RefreshDictValueEvent 事件增加 updateDictType 字段决定在更新单个字典文本值时是否维护对应字典类型对象的字典值列表信息</li> 
</ul> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">涵盖 1.4.4.X 变更</p> 
<ul> 
 <li>feat: 在刷新字典时当 DictValueVo.title == null 被视为删除相应的字典文本信息</li> 
 <li>fix: 修复 SpringBoot 2.4.0 以下版本无法启动问题</li> 
</ul> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">配置文件变更：</p> 
<ul> 
 <li>增加一个<span> </span><code>system.dict.replace-value</code><span> </span>配置项（在原字典值字段上把字典值替换成字典文本输出）</li> 
</ul> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start"><strong>由于引入了 DictText#replace 配置，会影响使用 DictText#mapValue=YES 和 system.dict.map-value=true 的配置，有使用上诉配置的请增加如下配置：</strong></p> 
<ol> 
 <li><strong>使用注解 DictText#mapValue=YES 配置的请增加 DictText#replace=YES 配置</strong></li> 
 <li><strong>使用全局 system.dict.map-value=true 配置的请增加 system.dict.replace-value=true 配置</strong></li> 
</ol> 
<p> </p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>项目地址</strong></p> 
<ul style="list-style-type:disc; margin-left:20px; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span><a href="https://gitee.com/houkunlin/system-dict-starter">https://gitee.com/houkunlin/system-dict-starter</a></span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhoukunlin-starter%2Fsystem-dict-starter" target="_blank">https://github.com/houkunlin-starter/system-dict-starter</a></span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>详细使用文档</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/houkunlin/system-dict-starter/blob/main/usage.md">https://gitee.com/houkunlin/system-dict-starter/blob/main/usage.md</a></p> 
<p><strong style="color:#333333">注解简单使用示例</strong></p> 
<pre><code class="language-java">// 注解的简单使用
@Data
@AllArgsConstructor
class Bean &#123;
    // &#123;"userType":"1","userTypeText":"普通用户"&#125;
    @DictText("PeopleType")
    private String userType = "1";
&#125;

// 自定义字典文本输出字段
@Data
@AllArgsConstructor
class Bean &#123;
    // &#123;"userType":"1","typeText":"普通用户"&#125;
    @DictText(value = "PeopleType", fieldName = "typeText")
    private String userType = "1";
&#125;

// 使用分隔符来存储多个字典值
@Data
@AllArgsConstructor
class Bean &#123;
    // &#123;"userType":"0,1","userTypeText":"系统管理、普通用户"&#125;
    @DictText(value = "PeopleType", array = @Array(split = ","))
    private String userType = "0,1";
&#125;

// 使用集合来存储多个字典值
@Data
@AllArgsConstructor
class Bean &#123;
     // &#123;"userType":["0","1"],"userTypeText":"系统管理、普通用户"&#125;
    @DictText("PeopleType")
    private List<String> userType = Arrays.asList("0", "1");
&#125;

// 把集合的字典文本转换成数组形式
@Data
@AllArgsConstructor
class Bean &#123;
    // &#123;"userType":["0","1"],"userTypeText":["系统管理","普通用户"]&#125;
    @DictText(value = "PeopleType", array = @Array(toText = false))
    private List<String> userType = Arrays.asList("0", "1");
&#125;

// 转换成 Map 形式在原字段上输出
@Data
@AllArgsConstructor
class Bean &#123;
    // &#123;"userType":&#123;"text":"普通用户","value":"1"&#125;&#125;
    @DictText(value = "PeopleType", mapValue = DictText.Type.YES, replace = DictText.Type.YES)
    private String userType;
&#125;</code></pre>
                                        </div>
                                      
</div>
            