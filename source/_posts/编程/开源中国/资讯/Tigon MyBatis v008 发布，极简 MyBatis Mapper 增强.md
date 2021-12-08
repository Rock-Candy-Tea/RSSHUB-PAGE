
---
title: 'Tigon MyBatis v0.0.8 发布，极简 MyBatis Mapper 增强'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1270'
author: 开源中国
comments: false
date: Wed, 08 Dec 2021 16:26:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1270'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left">Tigon MyBatis v0.0.8 已经发布，为 MyBatis Mapper 提供增强，设计精巧，代码量很少，代码洁癖工程师的朋友</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">此版本更新内容包括：</p> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>优化插入生成Key逻辑，之前通过拦截器方式实现，在高并发环境下存在Bug</li> 
 <li>删除了100多行代码，今天又变强了</li> 
</ul> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">详情查看：<a href="https://gitee.com/chyxion/tigon-mybatis/releases/v0.0.8">https://gitee.com/chyxion/tigon-mybatis/releases/v0.0.8</a></p> 
<h1 style="margin-left:0px; margin-right:0px; text-align:left">Tigon MyBatis</h1> 
<h2 style="margin-left:0; margin-right:0; text-align:left">简介</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">Tigon MyBatis为Spring工程中MyBatis的Mapper提供增强，主要有以下特点</p> 
<ul> 
 <li>代码又少又壮，绝不做多余的事情</li> 
 <li>仅需Mapper继承接口，实现<code>增</code><span> </span><code>删</code><span> </span><code>改</code><span> </span><code>查</code>，无额外配置，爽到没女朋友</li> 
 <li>用完即走，毫不留恋</li> 
</ul> 
<h3 style="margin-left:0; margin-right:0; text-align:left">开始使用</h3> 
<ul> 
 <li>引入Maven依赖</li> 
</ul> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span style="color:#000080"><dependency></span></span>
<span>  <span style="color:#000080"><groupId></span>me.chyxion.tigon<span style="color:#000080"></groupId></span></span>
<span>  <span style="color:#000080"><artifactId></span>tigon-mybatis<span style="color:#000080"></artifactId></span></span>
<span>  <span style="color:#000080"><version></span>0.0.8<span style="color:#000080"></version></span></span>
<span><span style="color:#000080"></dependency></span></span>
</pre> 
 </div> 
</div> 
<h3 style="margin-left:0; margin-right:0; text-align:left">使用示例</h3> 
<p>定义Entity</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><strong>package</strong> <strong style="color:#000055">me.chyxion.tigon.mybatis.entity</strong><span>;</span></span>

<span><strong>import</strong> <strong style="color:#000055">lombok.Getter</strong><span>;</span></span>
<span><strong>import</strong> <strong style="color:#000055">lombok.Setter</strong><span>;</span></span>
<span><strong>import</strong> <strong style="color:#000055">java.util.Date</strong><span>;</span></span>
<span><strong>import</strong> <strong style="color:#000055">lombok.ToString</strong><span>;</span></span>
<span><strong>import</strong> <strong style="color:#000055">java.io.Serializable</strong><span>;</span></span>
<span><strong>import</strong> <strong style="color:#000055">me.chyxion.tigon.mybatis.Table</strong><span>;</span></span>
<span><strong>import</strong> <strong style="color:#000055">me.chyxion.tigon.mybatis.NotUpdate</strong><span>;</span></span>
<span><strong>import</strong> <strong style="color:#000055">me.chyxion.tigon.mybatis.NotUpdateWhenNull</strong><span>;</span></span>

<span><span>@Getter</span></span>
<span><span>@Setter</span></span>
<span><span>@ToString</span></span>
<span><span>@Table</span><span>(</span><span style="color:#dd2200">"tb_user"</span><span>)</span></span>
<span><strong>public</strong> <strong>class</strong> <strong style="color:#445588">User</strong> <strong>implements</strong> <strong style="color:#445588">Serializable</strong> <span>&#123;</span></span>
<span>    <strong>private</strong> <strong>static</strong> <strong>final</strong> <strong style="color:#445588">long</strong> <span>serialVersionUID</span> <span>=</span> <span style="color:#009999">1L</span><span>;</span></span>

<span>    <strong>private</strong> <strong style="color:#445588">Integer</strong> <span>id</span><span>;</span></span>
<span>    <span style="color:#888888">// 标记账户不被更新</span></span>
<span>    <span>@NotUpdate</span></span>
<span>    <strong>private</strong> <strong style="color:#445588">String</strong> <span>account</span><span>;</span></span>
<span>    <span style="color:#888888">// 当手机号为null不被更新</span></span>
<span>    <span>@NotUpdateWhenNull</span></span>
<span>    <strong>private</strong> <strong style="color:#445588">String</strong> <span>mobile</span><span>;</span></span>
<span>    <strong>private</strong> <strong style="color:#445588">String</strong> <span>name</span><span>;</span></span>
<span>    <strong>private</strong> <strong style="color:#445588">Gender</strong> <span>gender</span><span>;</span></span>
<span>    <strong>private</strong> <strong style="color:#445588">String</strong> <span>password</span><span>;</span></span>
<span>    <strong>private</strong> <strong style="color:#445588">Date</strong> <span>birthDate</span><span>;</span></span>
<span>    <strong>private</strong> <strong style="color:#445588">String</strong> <span>city</span><span>;</span></span>
<span>    <strong>private</strong> <strong style="color:#445588">String</strong> <span>avatar</span><span>;</span></span>

<span>    <strong>private</strong> <strong style="color:#445588">Boolean</strong> <span>active</span><span>;</span></span>
<span>    <strong>private</strong> <strong style="color:#445588">String</strong> <span>remark</span><span>;</span></span>
<span>    <strong>private</strong> <strong style="color:#445588">String</strong> <span>createdBy</span><span>;</span></span>
<span>    <strong>private</strong> <strong style="color:#445588">Date</strong> <span>createdAt</span><span>;</span></span>
<span>    <strong>private</strong> <strong style="color:#445588">String</strong> <span>updatedBy</span><span>;</span></span>
<span>    <strong>private</strong> <strong style="color:#445588">Date</strong> <span>updatedAt</span><span>;</span></span>

<span>    <strong>public</strong> <strong>enum</strong> <strong style="color:#445588">Gender</strong> <span>&#123;</span></span>
<span>        <span style="color:#008080">MALE</span><span>,</span></span>
<span>        <span style="color:#008080">FEMALE</span></span>
<span>    <span>&#125;</span></span>
<span><span>&#125;</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p>定义Mapper</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><strong>package</strong> <strong style="color:#000055">me.chyxion.tigon.mybatis.mapper</strong><span>;</span></span>

<span><strong>import</strong> <strong style="color:#000055">java.util.List</strong><span>;</span></span>
<span><strong>import</strong> <strong style="color:#000055">me.chyxion.tigon.mybatis.BaseMapper</strong><span>;</span></span>
<span><strong>import</strong> <strong style="color:#000055">org.apache.ibatis.annotations.Mapper</strong><span>;</span></span>
<span><strong>import</strong> <strong style="color:#000055">me.chyxion.tigon.mybatis.entity.User</strong><span>;</span></span>

<span><span>@Mapper</span></span>
<span><strong>public</strong> <strong>interface</strong> <strong style="color:#445588">UserMapper</strong> <strong>extends</strong> <strong style="color:#445588">BaseMapper</strong><span><</span><strong style="color:#445588">Integer</strong><span>,</span> <strong style="color:#445588">User</strong><span>></span> <span>&#123;</span></span>
<span><span>&#125;</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p>注入Mapper对象</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span>@Autowired</span></span>
<span><strong>private</strong> <strong style="color:#445588">UserMapper</strong> <span>mapper</span><span>;</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p>I. 插入</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span>val</span> <span>user</span> <span>=</span> <strong style="color:#000000">new</strong> <strong style="color:#445588">User</strong><span>();</span></span>
<span><span>user</span><span>.</span><span style="color:#008080">setName</span><span>(</span><span style="color:#dd2200">"Donghuang"</span><span>);</span></span>
<span><span>user</span><span>.</span><span style="color:#008080">setAccount</span><span>(</span><span style="color:#dd2200">"donghuang"</span><span>);</span></span>
<span><span>user</span><span>.</span><span style="color:#008080">setMobile</span><span>(</span><span style="color:#dd2200">"137647788xx"</span><span>);</span></span>
<span><span>user</span><span>.</span><span style="color:#008080">setPassword</span><span>(</span><strong style="color:#445588">RandomStringUtils</strong><span>.</span><span style="color:#008080">randomAlphanumeric</span><span>(</span><span style="color:#009999">16</span><span>));</span></span>
<span><span>user</span><span>.</span><span style="color:#008080">setGender</span><span>(</span><strong style="color:#445588">User</strong><span>.</span><span style="color:#008080">Gender</span><span>.</span><span style="color:#008080">MALE</span><span>);</span></span>
<span><span>user</span><span>.</span><span style="color:#008080">setBirthDate</span><span>(</span><strong style="color:#445588">DateUtils</strong><span>.</span><span style="color:#008080">parseDate</span><span>(</span><span style="color:#dd2200">"1994-04-04"</span><span>));</span></span>
<span><span>user</span><span>.</span><span style="color:#008080">setCity</span><span>(</span><span style="color:#dd2200">"Shanghai"</span><span>);</span></span>
<span><span>user</span><span>.</span><span style="color:#008080">setActive</span><span>(</span><strong>true</strong><span>);</span></span>
<span><span>user</span><span>.</span><span style="color:#008080">setRemark</span><span>(</span><span style="color:#dd2200">"Uncle Donghuang"</span><span>);</span></span>
<span><span>user</span><span>.</span><span style="color:#008080">setCreatedBy</span><span>(</span><span style="color:#dd2200">"donghuang"</span><span>);</span></span>
<span><span>user</span><span>.</span><span style="color:#008080">setCreatedAt</span><span>(</span><strong style="color:#000000">new</strong> <strong style="color:#445588">Date</strong><span>());</span></span>

<span><span style="color:#888888">// 插入单条记录</span></span>
<span><span>mapper</span><span>.</span><span style="color:#008080">insert</span><span>(</span><span>user</span><span>);</span></span>

<span><span>val</span> <span>user1</span> <span>=</span> <strong style="color:#000000">new</strong> <strong style="color:#445588">User</strong><span>();</span></span>
<span><span>user1</span><span>.</span><span style="color:#008080">setName</span><span>(</span><span style="color:#dd2200">"Gemily"</span><span>);</span></span>
<span><span>user1</span><span>.</span><span style="color:#008080">setAccount</span><span>(</span><span style="color:#dd2200">"gemily"</span><span>);</span></span>
<span><span>user1</span><span>.</span><span style="color:#008080">setMobile</span><span>(</span><span style="color:#dd2200">"15770780xxx"</span><span>);</span></span>
<span><span>user1</span><span>.</span><span style="color:#008080">setPassword</span><span>(</span><strong style="color:#445588">RandomStringUtils</strong><span>.</span><span style="color:#008080">randomAlphanumeric</span><span>(</span><span style="color:#009999">16</span><span>));</span></span>
<span><span>user1</span><span>.</span><span style="color:#008080">setGender</span><span>(</span><strong style="color:#445588">User</strong><span>.</span><span style="color:#008080">Gender</span><span>.</span><span style="color:#008080">FEMALE</span><span>);</span></span>
<span><span>user1</span><span>.</span><span style="color:#008080">setBirthDate</span><span>(</span><strong style="color:#445588">DateUtils</strong><span>.</span><span style="color:#008080">parseDate</span><span>(</span><span style="color:#dd2200">"1990-06-06"</span><span>));</span></span>
<span><span>user1</span><span>.</span><span style="color:#008080">setCity</span><span>(</span><span style="color:#dd2200">"Hangzhou"</span><span>);</span></span>
<span><span>user1</span><span>.</span><span style="color:#008080">setActive</span><span>(</span><strong>true</strong><span>);</span></span>
<span><span>user1</span><span>.</span><span style="color:#008080">setCreatedBy</span><span>(</span><span style="color:#dd2200">"donghuang"</span><span>);</span></span>
<span><span>user1</span><span>.</span><span style="color:#008080">setCreatedAt</span><span>(</span><strong style="color:#000000">new</strong> <strong style="color:#445588">Date</strong><span>());</span></span>

<span><span>val</span> <span>user2</span> <span>=</span> <strong style="color:#000000">new</strong> <strong style="color:#445588">User</strong><span>();</span></span>
<span><span>user2</span><span>.</span><span style="color:#008080">setName</span><span>(</span><span style="color:#dd2200">"Luffy"</span><span>);</span></span>
<span><span>user2</span><span>.</span><span style="color:#008080">setAccount</span><span>(</span><span style="color:#dd2200">"luffy"</span><span>);</span></span>
<span><span>user2</span><span>.</span><span style="color:#008080">setMobile</span><span>(</span><span style="color:#dd2200">"137647799xx"</span><span>);</span></span>
<span><span>user2</span><span>.</span><span style="color:#008080">setPassword</span><span>(</span><strong style="color:#445588">RandomStringUtils</strong><span>.</span><span style="color:#008080">randomAlphanumeric</span><span>(</span><span style="color:#009999">16</span><span>));</span></span>
<span><span>user2</span><span>.</span><span style="color:#008080">setGender</span><span>(</span><strong style="color:#445588">User</strong><span>.</span><span style="color:#008080">Gender</span><span>.</span><span style="color:#008080">MALE</span><span>);</span></span>
<span><span>user2</span><span>.</span><span style="color:#008080">setBirthDate</span><span>(</span><strong style="color:#445588">DateUtils</strong><span>.</span><span style="color:#008080">parseDate</span><span>(</span><span style="color:#dd2200">"1997-07-07"</span><span>));</span></span>
<span><span>user2</span><span>.</span><span style="color:#008080">setCity</span><span>(</span><span style="color:#dd2200">"East sea"</span><span>);</span></span>
<span><span>user2</span><span>.</span><span style="color:#008080">setActive</span><span>(</span><strong>true</strong><span>);</span></span>
<span><span>user2</span><span>.</span><span style="color:#008080">setRemark</span><span>(</span><span style="color:#dd2200">"Luffy"</span><span>);</span></span>
<span><span>user2</span><span>.</span><span style="color:#008080">setCreatedBy</span><span>(</span><span style="color:#dd2200">"donghuang"</span><span>);</span></span>
<span><span>user2</span><span>.</span><span style="color:#008080">setCreatedAt</span><span>(</span><strong style="color:#000000">new</strong> <strong style="color:#445588">Date</strong><span>());</span></span>

<span><span style="color:#888888">// 批量插入记录</span></span>
<span><span>mapper</span><span>.</span><span style="color:#008080">insert</span><span>(</span><strong style="color:#445588">Arrays</strong><span>.</span><span style="color:#008080">asList</span><span>(</span><span>user1</span><span>,</span> <span>user2</span><span>));</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p>II. 查询</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">根据<code>ID</code>查询单个对象</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span>val</span> <span>id</span> <span>=</span> <span style="color:#009999">1154</span><span>;</span></span>
<span><span style="color:#888888">// 根据主键查询单条记录</span></span>
<span><span>val</span> <span>user</span> <span>=</span> <span>mapper</span><span>.</span><span style="color:#008080">find</span><span>(</span><span>id</span><span>);</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">根据属性查询单个对象</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span style="color:#888888">// 根据属性account, mobile查询单个对象</span></span>
<span><span>val</span> <span>user</span> <span>=</span> <span>mapper</span><span>.</span><span style="color:#008080">find</span><span>(</span></span>
<span>    <strong style="color:#000000">new</strong> <strong style="color:#990000">Search</strong><span>(</span><span style="color:#dd2200">"account"</span><span>,</span> <span style="color:#dd2200">"donghuang"</span><span>)</span></span>
<span>        <span>.</span><span style="color:#008080">eq</span><span>(</span><span style="color:#dd2200">"mobile"</span><span>,</span> <span style="color:#dd2200">"137647788xx"</span><span>));</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">根据属性查询列表</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span style="color:#888888">// 根据属性birthDate, gender查询数据列表</span></span>
<span><span style="color:#888888">// 查询结果根据属性birthDate升序排序</span></span>
<span><span style="color:#888888">// 返回数据限制42条</span></span>
<span><span>val</span> <span>users</span> <span>=</span> <span>mapper</span><span>.</span><span style="color:#008080">list</span><span>(</span><strong style="color:#000000">new</strong> <strong style="color:#445588">Search</strong><span>()</span></span>
<span>    <span>.</span><span style="color:#008080">between</span><span>(</span><span style="color:#dd2200">"birthDate"</span><span>,</span></span>
<span>        <strong style="color:#445588">DateUtils</strong><span>.</span><span style="color:#008080">parseDate</span><span>(</span><span style="color:#dd2200">"1982-04-04"</span><span>),</span></span>
<span>        <strong style="color:#445588">DateUtils</strong><span>.</span><span style="color:#008080">parseDate</span><span>(</span><span style="color:#dd2200">"1994-04-04"</span><span>)</span></span>
<span>    <span>)</span></span>
<span>    <span>.</span><span style="color:#008080">eq</span><span>(</span><span style="color:#dd2200">"gender"</span><span>,</span> <strong style="color:#445588">User</strong><span>.</span><span style="color:#008080">Gender</span><span>.</span><span style="color:#008080">MALE</span><span>)</span></span>
<span>    <span>.</span><span style="color:#008080">asc</span><span>(</span><span style="color:#dd2200">"birthDate"</span><span>)</span></span>
<span>    <span>.</span><span style="color:#008080">limit</span><span>(</span><span style="color:#009999">42</span><span>));</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><code>Search</code>对象支持的<code>API</code></p> 
<ul> 
 <li><code>asc</code><span> </span>Order ASC 列升序排序</li> 
 <li><code>desc</code><span> </span>Order DSC 列降序排序</li> 
 <li><code>orderBy</code><span> </span>Order by 列属性排序</li> 
 <li><code>between</code><span> </span>Between two values 属性列属于2个值之间</li> 
 <li><code>build</code><span> </span>Build query criterion 自定义构建一个属性列查询条件</li> 
 <li><code>startsWith</code><span> </span>Value starts with string 属性列以字符串开头，等同于<code>col like 'val%'</code></li> 
 <li><code>endsWith</code><span> </span>Value ends with string 属性列以字符串结尾，等同于<code>col like '%val'</code></li> 
 <li><code>contains</code><span> </span>Value contains string 属性列包含字符串，等同于<code>col like '%val%'</code></li> 
 <li><code>like</code><span> </span>Value like 属性列与字符串相似</li> 
 <li><code>eq</code><span> </span>Equals 属性列等于</li> 
 <li><code>ne</code><span> </span>Not equals 属性列小于或等于</li> 
 <li><code>gt</code><span> </span>Greater than 属性列大于</li> 
 <li><code>gte</code><span> </span>Equals or greater than 属性列大于或等于</li> 
 <li><code>lt</code><span> </span>Less than 属性列小于</li> 
 <li><code>lte</code><span> </span>Equals or less than 属性列小于</li> 
 <li><code>in</code><span> </span>In values 属性列属于集合</li> 
 <li><code>notIn</code><span> </span>Not in values 属性列不属于集合</li> 
 <li><code>isNull</code><span> </span>Value is null 属性列为null</li> 
 <li><code>notNull</code><span> </span>Value is not null 属性列不为null</li> 
 <li><code>isTrue</code><span> </span>Value is true 属性列为true</li> 
 <li><code>isFalse</code><span> </span>Value is false 属性列为false</li> 
 <li><code>limit</code><span> </span>Return rows limit 查询/更新结果行数限制</li> 
 <li><code>offset</code><span> </span>Return rows offset 查询结果偏移行数</li> 
 <li><code>and</code><span> </span>And another<span> </span><code>Search</code><span> </span>且另外一个Search对象</li> 
 <li><code>or</code><span> </span>Or another<span> </span><code>Search</code><span> </span>或另外一个Search对象</li> 
</ul> 
<p>III. 更新</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">通过<code>Entity</code>根据<code>ID</code>更新</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span style="color:#888888">// 根据主键查询记录</span></span>
<span><span>val</span> <span>user</span> <span>=</span> <span>mapper</span><span>.</span><span style="color:#008080">find</span><span>(</span><span style="color:#009999">1</span><span>);</span></span>

<span><span>user</span><span>.</span><span style="color:#008080">setName</span><span>(</span><span style="color:#dd2200">"东皇大叔"</span><span>);</span></span>
<span><span>user</span><span>.</span><span style="color:#008080">setUpdatedBy</span><span>(</span><span style="color:#dd2200">"SYS"</span><span>);</span></span>
<span><span>user</span><span>.</span><span style="color:#008080">setUpdatedAt</span><span>(</span><strong style="color:#000000">new</strong> <strong style="color:#445588">Date</strong><span>());</span></span>
<span><span style="color:#888888">// 更新单个实体对象</span></span>
<span><span>mapper</span><span>.</span><span style="color:#008080">update</span><span>(</span><span>user</span><span>);</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">通过<code>Map<String, Object></code>更新</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span>val</span> <span>update</span> <span>=</span> <strong style="color:#000000">new</strong> <strong style="color:#445588">HashMap</strong><span><</span><strong style="color:#445588">String</strong><span>,</span> <strong style="color:#445588">Object</strong><span>>(</span><span style="color:#009999">6</span><span>);</span></span>
<span><span>update</span><span>.</span><span style="color:#008080">put</span><span>(</span><span style="color:#dd2200">"name"</span><span>,</span> <span style="color:#dd2200">"东皇大叔"</span><span>);</span></span>
<span><span>update</span><span>.</span><span style="color:#008080">put</span><span>(</span><span style="color:#dd2200">"updatedBy"</span><span>,</span> <span style="color:#dd2200">"SYS"</span><span>);</span></span>
<span><span>update</span><span>.</span><span style="color:#008080">put</span><span>(</span><span style="color:#dd2200">"updatedAt"</span><span>,</span> <strong style="color:#000000">new</strong> <strong style="color:#445588">Date</strong><span>());</span></span>
<span><span style="color:#888888">// 通过Map更新ID为1的记录</span></span>
<span><span>mapper</span><span>.</span><span style="color:#008080">update</span><span>(</span><span>update</span><span>,</span> <span style="color:#009999">1</span><span>);</span></span>
<span><span style="color:#888888">// 效果同上</span></span>
<span><span style="color:#888888">// mapper.update(update, new Search("id", 1));</span></span>
<span><span style="color:#888888">// mapper.update(update, new Search(1));</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">更新列为<code>NULL</code></p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span style="color:#888888">// 更新id为274229记录的属性列remark为null</span></span>
<span><span>mapper</span><span>.</span><span style="color:#008080">setNull</span><span>(</span><span style="color:#dd2200">"remark"</span><span>,</span> <span style="color:#009999">274229</span><span>);</span></span>
<span><span style="color:#888888">// 更新id为1154记录的属性列remark为null</span></span>
<span><span>mapper</span><span>.</span><span style="color:#008080">setNull</span><span>(</span><span style="color:#dd2200">"remark"</span><span>,</span> <strong style="color:#000000">new</strong> <strong style="color:#445588">Search</strong><span>(</span><span style="color:#dd2200">"id"</span><span>,</span> <span style="color:#009999">1154</span><span>));</span></span>
<span><span style="color:#888888">// 更新全表的属性列remark为null，小心操作！！！</span></span>
<span><span>mapper</span><span>.</span><span style="color:#008080">setNull</span><span>(</span><span style="color:#dd2200">"remark"</span><span>,</span> <strong style="color:#000000">new</strong> <strong style="color:#445588">Search</strong><span>());</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p>IV. 删除</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">通过<code>ID</code>删除数据</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span style="color:#888888">// 根据主键删除记录</span></span>
<span><span>mapper</span><span>.</span><span style="color:#008080">delete</span><span>(</span><span style="color:#009999">1</span><span>);</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">通过<code>Search</code>对象删除数据</p> 
<div style="text-align:left"> 
 <div> 
  <pre><span><span style="color:#888888">// 根据属性ID删除记录</span></span>
<span><span>mapper</span><span>.</span><span style="color:#008080">delete</span><span>(</span><strong style="color:#000000">new</strong> <strong style="color:#445588">Search</strong><span>(</span><span style="color:#dd2200">"id"</span><span>,</span> <span style="color:#009999">1</span><span>));</span></span>
<span><span style="color:#888888">// 等同于 mapper.delete(1);</span></span></pre> 
  <div style="text-align:center">
    
  </div> 
 </div> 
</div> 
<p>V. 杂项</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">除了上面说到的一些基础增删改查操作，还有一些实用功能，如<code>@Transient</code><span> </span><code>@UseGeneratedKeys</code><span> </span><code>@NoPrimaryKey</code><span> </span><code>@NotUpdateWhenNull</code><span> </span><code>@RawValue</code>等注解，插入、更新前回调，以及支持扩展自定义的方法等。</p> 
<h3 style="margin-left:0; margin-right:0; text-align:left">配置说明</h3> 
<ul> 
 <li>SpringBoot项目，无需其他操作，引入依赖即可</li> 
 <li>Spring项目，注册Bean<span> </span><em>me.chyxion.tigon.mybatis.TigonMyBatisConfiguration</em></li> 
 <li>业务Mapper继承<em>me.chyxion.tigon.mybatis.BaseMapper</em>或相关衍生Mapper，<em>Base(Query, Insert, Update, Delete)Mapper</em></li> 
</ul>
                                        </div>
                                      
</div>
            