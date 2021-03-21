
---
title: Martian 3.2.18 发布，弃用 FastJson
categories: 
    - 编程
    - 开源中国 - 资讯
author: 开源中国 - 资讯
comments: false
date: Fri, 19 Mar 2021 18:18:00 GMT
thumbnail: 
---

<div>   
<div class="content">
                                                                                            <h3>本次更新如下</h3> 
<ol> 
 <li>开放JWT秘钥配置权限</li> 
 <li>丢弃FastJson改用Jackson</li> 
</ol> 
<h3>JWT秘钥配置权限</h3> 
<p>在配置类重写此方法即可</p> 
<pre><code class="language-java">@Override
public JWTConfig jwtConfig() {
     JWTConfig jwtConfig = new JWTConfig();
     // token失效时间单位，默认: 秒
     jwtConfig.setCalendarField(Calendar.SECOND);
     // token失效时间，默认: 86400秒
     jwtConfig.setCalendarInterval(86400);
     // 秘钥，默认: 一个UUID
     jwtConfig.setSecret(UUID.randomUUID().toString());
     return jwtConfig;
}</code></pre> 
<h3>改用Jackson后有哪些影响</h3> 
<p>除了实体类映射有影响之外，其他地方均不受影响</p> 
<p style="text-align:start"><strong>一、实体类的字段映射</strong></p> 
<p style="text-align:start">开发中经常出现这种情况，实体类的命名规范是驼峰，而数据库字段是下划线分割，所以会出现对不上的情况，这个时候我们可以用这个注解来解决：</p> 
<pre style="text-align:start"><code class="language-java">com.fasterxml.jackson.annotation.JsonProperty
</code></pre> 
<p style="text-align:start">在实体类的字段上加上这个注解，设置name属性为数据库字段名</p> 
<pre><code class="language-java">public class TestPO{

    @JsonProperty(value = "数据库里的name字段名")
    private String name;
    @JsonProperty(value = "数据库里的age字段名")
    private String age;
    @JsonProperty(value = "数据库里的id字段名")
    private int id;

}</code></pre> 
<p style="text-align:start"><strong>二、避免字段不一致而报错</strong></p> 
<ul> 
 <li>有时候，我们查询出来的结果集里面的字段，在实体类里面会找不到</li> 
 <li>比如，实体类的字段是 a, b 但是结果集里面的字段是 a, b, c，这个c在实体类里不存在</li> 
 <li>这种情况下会出现异常，所以为了避免这个异常的出现，可以用到这个注解：</li> 
</ul> 
<pre><code class="language-java">com.fasterxml.jackson.annotation.JsonIgnoreProperties</code></pre> 
<p style="text-align:start">在实体类上加上这个注解即可</p> 
<pre><code class="language-java">@JsonIgnoreProperties(ignoreUnknown = true)
public class TestPO{


}</code></pre> 
<p style="text-align:start"><strong>三、指定日期格式</strong></p> 
<p style="text-align:start">当实体类里面出现了Date类型，在执行数据库操作的时候会出异常，所以需要指定一个日期格式， 指定格式可以用这个注解：</p> 
<pre style="text-align:start"><code class="language-java">com.fasterxml.jackson.annotation.JsonFormat
</code></pre> 
<p style="text-align:start">在实体类上加上这个注解即可</p> 
<pre><code class="language-java">@JsonIgnoreProperties(ignoreUnknown = true)
public class TestPO{

    @JsonProperty("create_time")
    @JsonFormat(pattern = "yyyy-MM-dd HH🇲🇲ss")
    private Date createTime;

}</code></pre> 
<p style="text-align:start"><strong>实体类需要写get/set方法，或者用lombok注解</strong></p> 
<h3 style="text-align:start"><strong>更多信息可以前往官网查看</strong></h3> 
<p style="text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fmars-framework.com%2F" target="_blank">http://mars-framework.com/</a></p>
                                        </div>
                                      
</div>
            