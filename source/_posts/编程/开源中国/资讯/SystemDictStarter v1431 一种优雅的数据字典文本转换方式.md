
---
title: 'SystemDictStarter v1.4.3.1 一种优雅的数据字典文本转换方式'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3772'
author: 开源中国
comments: false
date: Mon, 18 Oct 2021 11:31:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3772'
---

<div>   
<div class="content">
                                                                    
                                                        <p>在日常项目开发中，不免都会用到一些数据字典的信息，遇到这种场景通常都是后端把字典的文本转换好一起返回给前端，前端只需要直接展示即可。一般情况下后端可能需要单独给返回对象创建一个字段来存储对应的字典文本值，然后进行手动的处理，这种方式通常比较繁琐，在字段多的时候会增加更多的工作量。</p> 
<p>本项目基于 Jackson 的自定义注解功能实现了这一自动转换过程，不需要在对象中定义存放字典文本的字段，只需要在字段上使用 @DictText 注解，Jackson序列化的时候即可自动把字典值转换成字典文本。</p> 
<p> </p> 
<p><strong>更新日志</strong></p> 
<p>v1.4.3.1 版本无新功能引入</p> 
<ul> 
 <li>优化 @DictText 注解对数组类型字段序列化处理方式</li> 
 <li>优化 @DictText 注解使用枚举配置时的序列化处理方式</li> 
 <li>优化字段为 null 值时的处理方式</li> 
 <li>修改序列化器的变量名称，明确变量名具体意义</li> 
</ul> 
<p> </p> 
<p><strong>项目地址</strong></p> 
<ul style="list-style-type:disc; margin-left:20px; margin-right:0"> 
 <li> <p><span><a href="https://gitee.com/houkunlin/system-dict-starter">https://gitee.com/houkunlin/system-dict-starter</a></span></p> </li> 
 <li> <p><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhoukunlin-starter%2Fsystem-dict-starter" target="_blank">https://github.com/houkunlin-starter/system-dict-starter</a></span></p> </li> 
</ul> 
<p><strong>详细使用文档</strong></p> 
<p><a href="https://gitee.com/houkunlin/system-dict-starter/blob/main/usage.md">https://gitee.com/houkunlin/system-dict-starter/blob/main/usage.md</a></p> 
<p> </p> 
<p><strong>注解简单使用示例</strong></p> 
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

// 转换成 Map 形式输出
@Data
@AllArgsConstructor
class Bean &#123;
    // &#123;"userType":&#123;"text":"普通用户","value":"1"&#125;&#125;
    @DictText(value = "PeopleType", mapValue = DictText.Type.YES)
    private String userType;
&#125;</code></pre> 
<p> </p>
                                        </div>
                                      
</div>
            