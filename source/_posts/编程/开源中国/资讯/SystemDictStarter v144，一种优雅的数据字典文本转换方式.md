
---
title: 'SystemDictStarter v1.4.4，一种优雅的数据字典文本转换方式'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9320'
author: 开源中国
comments: false
date: Fri, 29 Oct 2021 00:05:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9320'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">在日常项目开发中，不免都会用到一些数据字典的信息，遇到这种场景通常都是后端把字典的文本转换好一起返回给前端，前端只需要直接展示即可。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">一般情况下后端可能需要单独给返回对象创建一个字段来存储对应的字典文本值，然后进行手动的处理，这种方式通常比较繁琐，在字段多的时候会增加更多的工作量。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">本项目基于 Jackson 的自定义注解功能实现了这一自动转换过程，不需要在对象中定义存放字典文本的字段，只需要在字段上使用 @DictText 注解，Jackson序列化的时候即可自动把字典值转换成字典文本。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>更新日志</strong></p> 
<p style="color:#24292f; text-align:start">功能代码变更</p> 
<ul> 
 <li>feat: 增加一个<span> </span><code>RefreshDictValueEvent</code><span> </span>事件可以刷新单个字典文本信息</li> 
 <li>feat: 增加一个刷新字典的端点：<code>dictRefresh</code></li> 
 <li>feat: 增加使用 Redis 的发布/订阅 功能来处理字典刷新事件通知配置（需要设定配置文件来启用）</li> 
 <li>refactor: 修改系统字典端点ID<span> </span><code>dictSystem</code><span> </span>解决系统字典端点控制台日志警告问题</li> 
 <li>refactor: MQ通知其他协同系统刷新字典默认未启用</li> 
</ul> 
<p style="color:#24292f; text-align:start">配置文件变更：</p> 
<ul> 
 <li>移除<span> </span><code>system.dict.mq-header-source-key</code><span> </span>配置项</li> 
 <li>增加<span> </span><code>system.dict.mq-type</code><span> 配置项</span>选择性启用 RefreshDictEvent 事件通知其他系统刷新字典 
  <ul> 
   <li>可选值：<code>none</code><span> </span>不启用（默认），<code>amqp</code><span> </span>使用 RabbitMQ，<span> </span><code>redis</code><span> </span>使用 Redis 的发布/订阅功能</li> 
  </ul> </li> 
 <li>更改<span> </span><code>system.dict.refresh-dict-interval</code><span> </span>属性类型为<span> </span><code>Duration</code><span> </span>类型，默认值未改变</li> 
</ul> 
<p style="color:#24292f; text-align:start">涵盖 1.4.3.X 变更</p> 
<ul> 
 <li>fix: 修复因 Redis 客户端不同导致项目启动报错问题 <a href="https://gitee.com/houkunlin/system-dict-starter/issues/I4EBUT">#I4EBUT</a></li> 
 <li>fix: 修复 Java 8 环境下 SpringBoot 打包后使用 java -jar 启动异常问题 <a href="https://gitee.com/houkunlin/system-dict-starter/issues/I4EUF1">#I4EUF1</a></li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>项目地址</strong></p> 
<ul style="list-style-type:disc; margin-left:20px; margin-right:0"> 
 <li> <p style="margin-left:0; margin-right:0"><span><a href="https://gitee.com/houkunlin/system-dict-starter">https://gitee.com/houkunlin/system-dict-starter</a></span></p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fhoukunlin-starter%2Fsystem-dict-starter" target="_blank">https://github.com/houkunlin-starter/system-dict-starter</a></span></p> </li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>详细使用文档</strong></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><a href="https://gitee.com/houkunlin/system-dict-starter/blob/main/usage.md">https://gitee.com/houkunlin/system-dict-starter/blob/main/usage.md</a></p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>注解简单使用示例</strong></p> 
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

<span style="color:#6a737d">// 转换成 Map 形式输出</span>
<span style="color:#032f62">@Data</span>
<span style="color:#032f62">@AllArgsConstructor</span>
class Bean &#123;
    <span style="color:#6a737d">// &#123;"userType":&#123;"text":"普通用户","value":"1"&#125;&#125;</span>
    <span style="color:#032f62">@DictText</span>(value = <span style="color:#032f62">"PeopleType"</span>, mapValue = DictText.Type.YES)
    private String userType;
&#125;</code></pre>
                                        </div>
                                      
</div>
            