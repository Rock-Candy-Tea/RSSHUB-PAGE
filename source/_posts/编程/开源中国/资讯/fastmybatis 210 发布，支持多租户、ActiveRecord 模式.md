
---
title: 'fastmybatis 2.1.0 发布，支持多租户、ActiveRecord 模式'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4822'
author: 开源中国
comments: false
date: Thu, 24 Mar 2022 02:01:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4822'
---

<div>   
<div class="content">
                                                                                            <p>fastmybatis 2.1.0 发布，本次更新内容如下：</p> 
<ul> 
 <li>支持多租户</li> 
 <li>新增ActiveRecord模式</li> 
</ul> 
<p><strong>多租户</strong></p> 
<p>fastmybatis支持两种方式实现多租户：通过字段隔离，通过表名隔离</p> 
<p>具体实现方式参考文档：<a href="https://durcframework.gitee.io/fastmybatis/#/files/10027_%E5%A4%9A%E7%A7%9F%E6%88%B7?t=1647433191044" target="_blank">多租户</a></p> 
<p><strong>ActiveRecord模式</strong></p> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">实体类实现<code>com.gitee.fastmybatis.core.support.Record</code>接口即可拥有ActiveRecord模式</p> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">实体类：</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code><span style="color:#8e908c">/**
 * Active Record
 * 表名：user_info
 * 备注：用户信息表
 */</span>
<span style="color:#525252">@Table</span><span style="color:#525252">(</span>name <span>=</span> <span style="color:var(--theme-color,#42b983)">"user_info"</span><span style="color:#525252">)</span>
<span style="color:#e96900">public</span> <span style="color:#e96900">class</span> <span>UserInfoRecord</span> <span style="color:#e96900">implements</span> <span>Record</span> <span style="color:#525252">&#123;</span>
    <span style="color:#525252">.</span><span style="color:#525252">.</span><span style="color:#525252">.</span>
<span style="color:#525252">&#125;</span></code></pre> 
<p style="color:#34495e; margin-left:0; margin-right:0; text-align:start">测试用例：</p> 
<pre style="margin-left:0; margin-right:0; text-align:start"><code>    <span style="color:#8e908c">// 保存全部字段</span>
    <span style="color:#525252">@Test</span>
    <span style="color:#e96900">public</span> <span style="color:#e96900">void</span> <span style="color:#e96900">save</span><span style="color:#525252">(</span><span style="color:#525252">)</span> <span style="color:#525252">&#123;</span>
        <span>UserInfoRecord</span> userInfoRecord <span>=</span> <span style="color:#e96900">new</span> <span>UserInfoRecord</span><span style="color:#525252">(</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
        userInfoRecord<span style="color:#525252">.</span><span style="color:#e96900">setUserId</span><span style="color:#525252">(</span><span style="color:#c76b29">11</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
        userInfoRecord<span style="color:#525252">.</span><span style="color:#e96900">setCity</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"杭州"</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
        userInfoRecord<span style="color:#525252">.</span><span style="color:#e96900">setAddress</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"西湖"</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
        <span style="color:#e96900">boolean</span> success <span>=</span> userInfoRecord<span style="color:#525252">.</span><span style="color:#e96900">save</span><span style="color:#525252">(</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
        <span>Assert</span><span style="color:#525252">.</span><span style="color:#e96900">assertTrue</span><span style="color:#525252">(</span>success<span style="color:#525252">)</span><span style="color:#525252">;</span>
    <span style="color:#525252">&#125;</span>

    <span style="color:#8e908c">// 保存不为null的字段</span>
    <span style="color:#525252">@Test</span>
    <span style="color:#e96900">public</span> <span style="color:#e96900">void</span> <span style="color:#e96900">saveIgnoreNull</span><span style="color:#525252">(</span><span style="color:#525252">)</span> <span style="color:#525252">&#123;</span>
        <span>UserInfoRecord</span> userInfoRecord <span>=</span> <span style="color:#e96900">new</span> <span>UserInfoRecord</span><span style="color:#525252">(</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
        userInfoRecord<span style="color:#525252">.</span><span style="color:#e96900">setUserId</span><span style="color:#525252">(</span><span style="color:#c76b29">11</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
        userInfoRecord<span style="color:#525252">.</span><span style="color:#e96900">setCity</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"杭州"</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
        userInfoRecord<span style="color:#525252">.</span><span style="color:#e96900">setAddress</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"西湖"</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
        <span style="color:#e96900">boolean</span> success <span>=</span> userInfoRecord<span style="color:#525252">.</span><span style="color:#e96900">saveIgnoreNull</span><span style="color:#525252">(</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
        <span>Assert</span><span style="color:#525252">.</span><span style="color:#e96900">assertTrue</span><span style="color:#525252">(</span>success<span style="color:#525252">)</span><span style="color:#525252">;</span>
    <span style="color:#525252">&#125;</span>

    <span style="color:#8e908c">// 修改全部字段</span>
    <span style="color:#525252">@Test</span>
    <span style="color:#e96900">public</span> <span style="color:#e96900">void</span> <span style="color:#e96900">update</span><span style="color:#525252">(</span><span style="color:#525252">)</span> <span style="color:#525252">&#123;</span>
        <span>UserInfoRecord</span> userInfoRecord <span>=</span> <span style="color:#e96900">new</span> <span>UserInfoRecord</span><span style="color:#525252">(</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
        userInfoRecord<span style="color:#525252">.</span><span style="color:#e96900">setId</span><span style="color:#525252">(</span><span style="color:#c76b29">4</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
        userInfoRecord<span style="color:#525252">.</span><span style="color:#e96900">setUserId</span><span style="color:#525252">(</span><span style="color:#c76b29">11</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
        userInfoRecord<span style="color:#525252">.</span><span style="color:#e96900">setCity</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"杭州"</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
        userInfoRecord<span style="color:#525252">.</span><span style="color:#e96900">setAddress</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"西湖"</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
        <span style="color:#e96900">boolean</span> success <span>=</span> userInfoRecord<span style="color:#525252">.</span><span style="color:#e96900">update</span><span style="color:#525252">(</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
        <span>Assert</span><span style="color:#525252">.</span><span style="color:#e96900">assertTrue</span><span style="color:#525252">(</span>success<span style="color:#525252">)</span><span style="color:#525252">;</span>
    <span style="color:#525252">&#125;</span>

    <span style="color:#8e908c">// 修改不为null的字段</span>
    <span style="color:#525252">@Test</span>
    <span style="color:#e96900">public</span> <span style="color:#e96900">void</span> <span style="color:#e96900">updateIgnoreNull</span><span style="color:#525252">(</span><span style="color:#525252">)</span> <span style="color:#525252">&#123;</span>
        <span>UserInfoRecord</span> userInfoRecord <span>=</span> <span style="color:#e96900">new</span> <span>UserInfoRecord</span><span style="color:#525252">(</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
        userInfoRecord<span style="color:#525252">.</span><span style="color:#e96900">setId</span><span style="color:#525252">(</span><span style="color:#c76b29">5</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
        userInfoRecord<span style="color:#525252">.</span><span style="color:#e96900">setUserId</span><span style="color:#525252">(</span><span style="color:#c76b29">11</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
        userInfoRecord<span style="color:#525252">.</span><span style="color:#e96900">setCity</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"杭州"</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
        userInfoRecord<span style="color:#525252">.</span><span style="color:#e96900">setAddress</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"西湖"</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
        <span style="color:#e96900">boolean</span> success <span>=</span> userInfoRecord<span style="color:#525252">.</span><span style="color:#e96900">updateIgnoreNull</span><span style="color:#525252">(</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
        <span>Assert</span><span style="color:#525252">.</span><span style="color:#e96900">assertTrue</span><span style="color:#525252">(</span>success<span style="color:#525252">)</span><span style="color:#525252">;</span>
    <span style="color:#525252">&#125;</span>

    <span style="color:#8e908c">// 保存或修改不为null的字段</span>
    <span style="color:#525252">@Test</span>
    <span style="color:#e96900">public</span> <span style="color:#e96900">void</span> <span style="color:#e96900">saveOrUpdateIgnoreNull</span><span style="color:#525252">(</span><span style="color:#525252">)</span> <span style="color:#525252">&#123;</span>
        <span>UserInfoRecord</span> userInfoRecord <span>=</span> <span style="color:#e96900">new</span> <span>UserInfoRecord</span><span style="color:#525252">(</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
        userInfoRecord<span style="color:#525252">.</span><span style="color:#e96900">setUserId</span><span style="color:#525252">(</span><span style="color:#c76b29">11</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
        userInfoRecord<span style="color:#525252">.</span><span style="color:#e96900">setCity</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"杭州"</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
        userInfoRecord<span style="color:#525252">.</span><span style="color:#e96900">setAddress</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"西湖"</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
        <span style="color:#e96900">boolean</span> success <span>=</span> userInfoRecord<span style="color:#525252">.</span><span style="color:#e96900">saveOrUpdateIgnoreNull</span><span style="color:#525252">(</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
        <span>Assert</span><span style="color:#525252">.</span><span style="color:#e96900">assertTrue</span><span style="color:#525252">(</span>success<span style="color:#525252">)</span><span style="color:#525252">;</span>
        <span>System</span><span style="color:#525252">.</span>out<span style="color:#525252">.</span><span style="color:#e96900">println</span><span style="color:#525252">(</span><span style="color:var(--theme-color,#42b983)">"id:"</span> <span>+</span> userInfoRecord<span style="color:#525252">.</span><span style="color:#e96900">getId</span><span style="color:#525252">(</span><span style="color:#525252">)</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
    <span style="color:#525252">&#125;</span>


    <span style="color:#8e908c">// 删除记录</span>
    <span style="color:#525252">@Test</span>
    <span style="color:#e96900">public</span> <span style="color:#e96900">void</span> <span style="color:#e96900">delete</span><span style="color:#525252">(</span><span style="color:#525252">)</span> <span style="color:#525252">&#123;</span>
        <span>UserInfoRecord</span> userInfoRecord <span>=</span> <span style="color:#e96900">new</span> <span>UserInfoRecord</span><span style="color:#525252">(</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
        userInfoRecord<span style="color:#525252">.</span><span style="color:#e96900">setId</span><span style="color:#525252">(</span><span style="color:#c76b29">8</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
        <span style="color:#e96900">boolean</span> success <span>=</span> userInfoRecord<span style="color:#525252">.</span><span style="color:#e96900">delete</span><span style="color:#525252">(</span><span style="color:#525252">)</span><span style="color:#525252">;</span>
        <span>Assert</span><span style="color:#525252">.</span><span style="color:#e96900">assertTrue</span><span style="color:#525252">(</span>success<span style="color:#525252">)</span><span style="color:#525252">;</span>
    <span style="color:#525252">&#125;</span></code></pre> 
<p> </p> 
<p><strong>关于fastmybatis</strong></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">fastmybatis是一个mybatis开发框架，其宗旨为：简单、快速、有效。</p> 
<ul> 
 <li>零配置快速上手</li> 
 <li>无需编写xml文件即可完成CRUD操作</li> 
 <li>支持mysql、sqlserver、oracle、postgresql、sqlite</li> 
 <li>支持自定义sql，对于基本的增删改查不需要写SQL，对于其它特殊SQL（如统计SQL）可写在xml中</li> 
 <li>支持与spring-boot集成，依赖starter即可</li> 
 <li>支持插件编写</li> 
 <li>支持ActiveRecord模式</li> 
 <li>支持多租户</li> 
 <li>提供通用Service</li> 
 <li>轻量级，无侵入性，是官方mybatis的一种扩展</li> 
</ul>
                                        </div>
                                      
</div>
            