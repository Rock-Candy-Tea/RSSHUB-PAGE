
---
title: 'MyBatis JPA Extra v2.7 GA 发布'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=8291'
author: 开源中国
comments: false
date: Tue, 28 Dec 2021 12:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=8291'
---

<div>   
<div class="content">
                                                                                            <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>MyBatis JPA Extra</strong><span style="background-color:#ffffff; color:#24292e">对MyBatis进行了JPA扩展，旨在基于JPA 2.1的注释简化对单表CUID操作，根据JPA注释动态生成SQL语句；使用Interceptor实现数据库SELECT分页查询，适配多种数据库；另外提供mybatis-jpa-extra-spring-boot-starter简化SpringBoot集成。</span></p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left"><strong>MyBatis JPA Extra</strong>对MyBatis扩展JPA功能</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">1.基于JPA 2.1的注释<strong>简化CUID操作</strong>;</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">2.用Interceptor实现数据库<strong>SELECT分页查询</strong>;</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">3.提供mybatis-jpa-extra-spring-boot-starter,<strong>简化SpringBoot集成</strong>;</p> 
<h2>1、JavaBean注释简单</h2> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">仅有6个注释</p> 
<blockquote> 
 <ul> 
  <li><a href="https://my.oschina.net/u/1260961" target="_blank">@Entity</a></li> 
  <li><a href="https://my.oschina.net/u/2493882" target="_blank">@Table</a></li> 
  <li><a href="https://my.oschina.net/u/1218" target="_blank">@Column</a></li> 
  <li><a href="https://my.oschina.net/u/3451001" target="_blank">@Id</a></li> 
  <li>@GeneratedValue</li> 
  <li>@Transient</li> 
 </ul> 
</blockquote> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:left">@GeneratedValue有4中策略</p> 
<ol> 
 <li> <p style="margin-left:0; margin-right:0"><strong>AUTO</strong></p> <p style="margin-left:0; margin-right:0">snowflakeid</p> <p style="margin-left:0; margin-right:0">uuid</p> <p style="margin-left:0; margin-right:0">uuid.hex</p> <p style="margin-left:0; margin-right:0">serial</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>SEQUENCE</strong></p> <p style="margin-left:0; margin-right:0">generator值为数据库序列名</p> </li> 
 <li> <p style="margin-left:0; margin-right:0"><strong>IDENTITY</strong></p> <p style="margin-left:0; margin-right:0">generator无，根据数据库自动生成方式</p> </li> 
</ol> 
<div> 
 <div> 
  <pre><span><strong>package</strong> <strong>org.apache.mybatis.jpa.test.entity</strong><span>;</span></span>
<span><strong>import</strong> <strong>java.io.Serializable</strong><span>;</span></span>
<span><strong>import</strong> <strong>javax.persistence.Column</strong><span>;</span></span>
<span><strong>import</strong> <strong>javax.persistence.Entity</strong><span>;</span></span>
<span><strong>import</strong> <strong>javax.persistence.GeneratedValue</strong><span>;</span></span>
<span><strong>import</strong> <strong>javax.persistence.GenerationType</strong><span>;</span></span>
<span><strong>import</strong> <strong>javax.persistence.Id</strong><span>;</span></span>
<span><strong>import</strong> <strong>javax.persistence.Table</strong><span>;</span></span>
<span><strong>import</strong> <strong>org.apache.mybatis.jpa.persistence.JpaBaseEntity</strong><span>;</span></span>

<span><span>@Entity</span></span>
<span><span>@Table</span><span>(</span><span>name</span> <span>=</span> <span style="color:#dd2200">"STUDENTS"</span><span>)</span>  </span>
<span><strong>public</strong> <strong>class</strong> <strong>Students</strong> <strong>extends</strong> <strong>JpaBaseEntity</strong> <strong>implements</strong> <strong>Serializable</strong><span>&#123;</span></span>
<span><strong>private</strong> <strong>static</strong> <strong>final</strong> <strong>long</strong> <span>serialVersionUID</span> <span>=</span> <span>-</span><span style="color:#009999">6928570405840778151L</span><span>;</span></span>
<span></span>
<span><span>@Id</span></span>
<span><span>@Column</span></span>
<span><span>@GeneratedValue</span><span>(</span><span>strategy</span><span>=</span><strong>GenerationType</strong><span>.</span><span style="color:#008080">AUTO</span><span>,</span><span>generator</span><span>=</span><span style="color:#dd2200">"snowflakeid"</span><span>)</span></span>
<span><span style="color:#888888">//@GeneratedValue(strategy=GenerationType.SEQUENCE,generator="SEQ_MYBATIS_STUD")</span></span>
<span><span style="color:#888888">//@GeneratedValue(strategy=GenerationType.IDENTITY,generator="SEQ_MYBATIS_STUD")</span></span>
<span><strong>private</strong> <strong>String</strong> <span>id</span><span>;</span></span>
<span></span>
<span><span>@Column</span></span>
<span><strong>private</strong> <strong>String</strong> <span>stdNo</span><span>;</span></span>
<span></span>
<span><span>@Column</span></span>
<span><strong>private</strong> <strong>String</strong> <span>stdName</span><span>;</span></span>
<span></span>
<span><span>@Column</span></span>
<span><strong>private</strong> <strong>String</strong> <span>stdGender</span><span>;</span></span>
<span></span>
<span><span>@Column</span></span>
<span><strong>private</strong> <strong>int</strong> <span>stdAge</span><span>;</span></span>
<span></span>
<span><span>@Column</span></span>
<span><strong>private</strong> <strong>String</strong> <span>stdMajor</span><span>;</span></span>
<span></span>
<span><span>@Column</span></span>
<span><strong>private</strong> <strong>String</strong> <span>stdClass</span><span>;</span></span>
<span></span>
<span><span>@Column</span></span>
<span><strong>private</strong> <strong>byte</strong><span>[]</span> <span>images</span><span>;</span></span>
<span></span>
<span><strong>public</strong> <strong>Students</strong><span>()</span> <span>&#123;</span></span>
<span><strong>super</strong><span>();</span></span>
<span><span>&#125;</span></span>

<span><strong>public</strong> <strong>get</strong><span>()&#123;&#125;;</span></span>
<span><strong>public</strong> <strong>void</strong> <strong>set</strong><span>()&#123;&#125;;</span></span>
<span><span style="color:#888888">//...</span></span>
<span><span>&#125;</span></span></pre> 
  <div>
    
  </div> 
 </div> 
</div> 
<h2>2、单表新增、修改、删除、查询、分页查询</h2> 
<div> 
 <div> 
  <pre><span><strong>package</strong> <strong>org.apache.mybatis.jpa.test</strong><span>;</span></span>
<span><strong>import</strong> <strong>java.sql.Types</strong><span>;</span></span>
<span><strong>import</strong> <strong>java.text.SimpleDateFormat</strong><span>;</span></span>
<span><strong>import</strong> <strong>java.util.ArrayList</strong><span>;</span></span>
<span><strong>import</strong> <strong>java.util.Date</strong><span>;</span></span>
<span><strong>import</strong> <strong>java.util.List</strong><span>;</span></span>
<span><strong>import</strong> <strong>org.apache.mybatis.jpa.test.dao.service.StudentsService</strong><span>;</span></span>
<span><strong>import</strong> <strong>org.apache.mybatis.jpa.test.entity.Students</strong><span>;</span></span>
<span><strong>import</strong> <strong>org.apache.mybatis.jpa.util.WebContext</strong><span>;</span></span>
<span><strong>import</strong> <strong>org.junit.Before</strong><span>;</span></span>
<span><strong>import</strong> <strong>org.junit.Test</strong><span>;</span></span>
<span><strong>import</strong> <strong>org.slf4j.Logger</strong><span>;</span></span>
<span><strong>import</strong> <strong>org.slf4j.LoggerFactory</strong><span>;</span></span>
<span><strong>import</strong> <strong>org.springframework.context.ApplicationContext</strong><span>;</span></span>
<span><strong>import</strong> <strong>org.springframework.context.support.ClassPathXmlApplicationContext</strong><span>;</span></span>

<span><strong>public</strong> <strong>class</strong> <strong>MyBatisTestRunner</strong> <span>&#123;</span></span>
<span><strong>private</strong> <strong>static</strong> <strong>final</strong> <strong>Logger</strong> <span>_logger</span> <span>=</span> <strong>LoggerFactory</strong><span>.</span><span style="color:#008080">getLogger</span><span>(</span><strong>MyBatisTestRunner</strong><span>.</span><span style="color:#008080">class</span><span>);</span></span>
<span><strong>public</strong> <strong>static</strong> <strong>ApplicationContext</strong> <span>context</span><span>;</span></span>
<span><strong>public</strong> <strong>static</strong> <strong>StudentsService</strong> <span>service</span><span>;</span></span>
<span></span>
<span><span>@Test</span></span>
<span><strong>public</strong> <strong>void</strong> <strong>insert</strong><span>()</span> <strong>throws</strong> <strong>Exception</strong><span>&#123;</span></span>
<span><span>_logger</span><span>.</span><span style="color:#008080">info</span><span>(</span><span style="color:#dd2200">"insert..."</span><span>);</span></span>
<span><strong>Students</strong> <span>student</span><span>=</span><strong>new</strong> <strong>Students</strong><span>();</span></span>
<span><span style="color:#888888">//student.setId("10024");</span></span>
<span><span>student</span><span>.</span><span style="color:#008080">setStdNo</span><span>(</span><span style="color:#dd2200">"10024"</span><span>);</span></span>
<span><span>student</span><span>.</span><span style="color:#008080">setStdGender</span><span>(</span><span style="color:#dd2200">"M"</span><span>);</span></span>
<span><span>student</span><span>.</span><span style="color:#008080">setStdName</span><span>(</span><span style="color:#dd2200">"司马昭"</span><span>);</span></span>
<span><span>student</span><span>.</span><span style="color:#008080">setStdAge</span><span>(</span><span style="color:#009999">20</span><span>);</span></span>
<span><span>student</span><span>.</span><span style="color:#008080">setStdMajor</span><span>(</span><span style="color:#dd2200">"政治"</span><span>);</span></span>
<span><span>student</span><span>.</span><span style="color:#008080">setStdClass</span><span>(</span><span style="color:#dd2200">"4"</span><span>);</span></span>
<span><span>service</span><span>.</span><span style="color:#008080">insert</span><span>(</span><span>student</span><span>);</span></span>
<span></span>
<span><strong>Thread</strong><span>.</span><span style="color:#008080">sleep</span><span>(</span><span style="color:#009999">1000</span><span>);</span></span>
<span><span>_logger</span><span>.</span><span style="color:#008080">info</span><span>(</span><span style="color:#dd2200">"insert id "</span> <span>+</span> <span>student</span><span>.</span><span style="color:#008080">getId</span><span>());</span></span>
<span><span style="color:#888888">//service.remove(student.getId());</span></span>
<span><span>&#125;</span></span>
<span></span>
<span><span>@Test</span></span>
<span><strong>public</strong> <strong>void</strong> <strong>merge</strong><span>()</span> <strong>throws</strong> <strong>Exception</strong><span>&#123;</span></span>
<span><span>_logger</span><span>.</span><span style="color:#008080">info</span><span>(</span><span style="color:#dd2200">"merge..."</span><span>);</span></span>
<span><strong>Students</strong> <span>student</span><span>=</span><strong>new</strong> <strong>Students</strong><span>();</span></span>
<span><span style="color:#888888">//student.setId("10024");</span></span>
<span><span>student</span><span>.</span><span style="color:#008080">setStdNo</span><span>(</span><span style="color:#dd2200">"10024"</span><span>);</span></span>
<span><span>student</span><span>.</span><span style="color:#008080">setStdGender</span><span>(</span><span style="color:#dd2200">"M"</span><span>);</span></span>
<span><span>student</span><span>.</span><span style="color:#008080">setStdName</span><span>(</span><span style="color:#dd2200">"司马昭"</span><span>);</span></span>
<span><span>student</span><span>.</span><span style="color:#008080">setStdAge</span><span>(</span><span style="color:#009999">20</span><span>);</span></span>
<span><span>student</span><span>.</span><span style="color:#008080">setStdMajor</span><span>(</span><span style="color:#dd2200">"政治"</span><span>);</span></span>
<span><span>student</span><span>.</span><span style="color:#008080">setStdClass</span><span>(</span><span style="color:#dd2200">"4"</span><span>);</span></span>
<span><span>service</span><span>.</span><span style="color:#008080">merge</span><span>(</span><span>student</span><span>);</span></span>
<span></span>
<span><strong>Thread</strong><span>.</span><span style="color:#008080">sleep</span><span>(</span><span style="color:#009999">1000</span><span>);</span></span>
<span><span>_logger</span><span>.</span><span style="color:#008080">info</span><span>(</span><span style="color:#dd2200">"insert id "</span> <span>+</span> <span>student</span><span>.</span><span style="color:#008080">getId</span><span>());</span></span>
<span><span>&#125;</span></span>
<span></span>
<span><span>@Test</span></span>
<span><strong>public</strong> <strong>void</strong> <strong>find</strong><span>()</span> <strong>throws</strong> <strong>Exception</strong><span>&#123;</span></span>
<span><span>_logger</span><span>.</span><span style="color:#008080">info</span><span>(</span><span style="color:#dd2200">"find..."</span><span>);</span></span>
<span><span>_logger</span><span>.</span><span style="color:#008080">info</span><span>(</span><span style="color:#dd2200">"find by filter  "</span> </span>
<span><span>+</span> <span>service</span><span>.</span><span style="color:#008080">find</span><span>(</span><span style="color:#dd2200">" StdNo = '10024' or StdNo = '10004'"</span><span>)</span></span>
<span><span>);</span></span>

<span><span>_logger</span><span>.</span><span style="color:#008080">info</span><span>(</span><span style="color:#dd2200">"find by filter with args "</span> </span>
<span><span>+</span> <span>service</span><span>.</span><span style="color:#008080">find</span><span>(</span></span>
<span><span style="color:#dd2200">" StdNo = ? or StdNo = ?  "</span><span>,</span></span>
<span><strong>new</strong> <strong>Object</strong><span>[]&#123;</span><span style="color:#dd2200">"10024"</span><span>,</span><span style="color:#dd2200">"10004"</span><span>&#125;,</span></span>
<span><strong>new</strong> <strong>int</strong><span>[]&#123;</span><strong>Types</strong><span>.</span><span style="color:#008080">VARCHAR</span><span>,</span><strong>Types</strong><span>.</span><span style="color:#008080">INTEGER</span><span>&#125;</span></span>
<span><span>)</span></span>
<span><span>);</span></span>
<span><span>&#125;</span></span>
<span></span>
<span><span>@Test</span></span>
<span><strong>public</strong> <strong>void</strong> <strong>get</strong><span>()</span> <strong>throws</strong> <strong>Exception</strong><span>&#123;</span></span>
<span><span>_logger</span><span>.</span><span style="color:#008080">info</span><span>(</span><span style="color:#dd2200">"get..."</span><span>);</span></span>
<span><strong>Students</strong> <span>student</span><span>=</span><span>service</span><span>.</span><span style="color:#008080">get</span><span>(</span><span style="color:#dd2200">"317d5eda-927c-4871-a916-472a8062df23"</span><span>);</span></span>
<span><strong>System</strong><span>.</span><span style="color:#008080">out</span><span>.</span><span style="color:#008080">println</span><span>(</span><span style="color:#dd2200">"Students "</span><span>+</span><span>student</span><span>);</span></span>
<span> <span>_logger</span><span>.</span><span style="color:#008080">info</span><span>(</span><span style="color:#dd2200">"Students "</span><span>+</span><span>student</span><span>);</span></span>
<span><span>&#125;</span></span>
<span></span>
<span><span>@Test</span></span>
<span><strong>public</strong> <strong>void</strong> <strong>update</strong><span>()</span> <strong>throws</strong> <strong>Exception</strong><span>&#123;</span></span>
<span><span>_logger</span><span>.</span><span style="color:#008080">info</span><span>(</span><span style="color:#dd2200">"get..."</span><span>);</span></span>
<span><strong>Students</strong> <span>student</span><span>=</span><span>service</span><span>.</span><span style="color:#008080">get</span><span>(</span><span style="color:#dd2200">"317d5eda-927c-4871-a916-472a8062df23"</span><span>);</span></span>
<span><strong>System</strong><span>.</span><span style="color:#008080">out</span><span>.</span><span style="color:#008080">println</span><span>(</span><span style="color:#dd2200">"Students "</span><span>+</span><span>student</span><span>);</span></span>
<span> <span>_logger</span><span>.</span><span style="color:#008080">info</span><span>(</span><span style="color:#dd2200">"Students "</span><span>+</span><span>student</span><span>);</span></span>
<span> <span>_logger</span><span>.</span><span style="color:#008080">info</span><span>(</span><span style="color:#dd2200">"update..."</span><span>);</span></span>
<span> <span>student</span><span>.</span><span style="color:#008080">setImages</span><span>(</span><strong>null</strong><span>);</span></span>
<span> <span>service</span><span>.</span><span style="color:#008080">update</span><span>(</span><span>student</span><span>);</span></span>
<span> <span>_logger</span><span>.</span><span style="color:#008080">info</span><span>(</span><span style="color:#dd2200">"updateed."</span><span>);</span></span>
<span> </span>
<span> <span>student</span><span>.</span><span style="color:#008080">setImages</span><span>(</span><span style="color:#dd2200">"ssss"</span><span>.</span><span style="color:#008080">getBytes</span><span>());</span></span>
<span> <span>service</span><span>.</span><span style="color:#008080">update</span><span>(</span><span>student</span><span>);</span></span>
<span> <span>_logger</span><span>.</span><span style="color:#008080">info</span><span>(</span><span style="color:#dd2200">"updateed2."</span><span>);</span></span>
<span><span>&#125;</span></span>
<span></span>
<span><span>@Test</span></span>
<span><strong>public</strong> <strong>void</strong> <strong>remove</strong><span>()</span> <strong>throws</strong> <strong>Exception</strong><span>&#123;</span></span>
<span><span>_logger</span><span>.</span><span style="color:#008080">info</span><span>(</span><span style="color:#dd2200">"remove..."</span><span>);</span></span>
<span><strong>Students</strong> <span>student</span><span>=</span><strong>new</strong> <strong>Students</strong><span>();</span></span>
<span><span>student</span><span>.</span><span style="color:#008080">setId</span><span>(</span><span style="color:#dd2200">"921d3377-937a-4578-b1e2-92fb23b5e512"</span><span>);</span></span>
<span><span>service</span><span>.</span><span style="color:#008080">remove</span><span>(</span><span>student</span><span>.</span><span style="color:#008080">getId</span><span>());</span></span>
<span><span>&#125;</span></span>
<span></span>
<span><span>@Test</span></span>
<span><strong>public</strong> <strong>void</strong> <strong>batchDelete</strong><span>()</span> <strong>throws</strong> <strong>Exception</strong><span>&#123;</span></span>
<span><span>_logger</span><span>.</span><span style="color:#008080">info</span><span>(</span><span style="color:#dd2200">"batchDelete..."</span><span>);</span></span>
<span><strong>List</strong><span><</span><strong>String</strong><span>></span> <span>idList</span><span>=</span><strong>new</strong> <strong>ArrayList</strong><span><</span><strong>String</strong><span>>();</span></span>
<span><span>idList</span><span>.</span><span style="color:#008080">add</span><span>(</span><span style="color:#dd2200">"8584804d-b5ac-45d2-9f91-4dd8e7a090a7"</span><span>);</span></span>
<span><span>idList</span><span>.</span><span style="color:#008080">add</span><span>(</span><span style="color:#dd2200">"ab7422e9-a91a-4840-9e59-9d911257c918"</span><span>);</span></span>
<span><span>idList</span><span>.</span><span style="color:#008080">add</span><span>(</span><span style="color:#dd2200">"12b6ceb8-573b-4f01-ad85-cfb24cfa007c"</span><span>);</span></span>
<span><span>idList</span><span>.</span><span style="color:#008080">add</span><span>(</span><span style="color:#dd2200">"dafd5ba4-d2e3-4656-bd42-178841e610fe"</span><span>);</span></span>
<span><span>service</span><span>.</span><span style="color:#008080">deleteBatch</span><span>(</span><span>idList</span><span>);</span></span>
<span><span>&#125;</span></span>
<span></span>
<span><span>@Test</span></span>
<span><strong>public</strong> <strong>void</strong> <strong>logicDelete</strong><span>()</span> <strong>throws</strong> <strong>Exception</strong><span>&#123;</span></span>
<span><span>_logger</span><span>.</span><span style="color:#008080">info</span><span>(</span><span style="color:#dd2200">"logicDelete..."</span><span>);</span></span>
<span><strong>List</strong><span><</span><strong>String</strong><span>></span> <span>idList</span><span>=</span><strong>new</strong> <strong>ArrayList</strong><span><</span><strong>String</strong><span>>();</span></span>
<span><span>idList</span><span>.</span><span style="color:#008080">add</span><span>(</span><span style="color:#dd2200">"8584804d-b5ac-45d2-9f91-4dd8e7a090a7"</span><span>);</span></span>
<span><span>idList</span><span>.</span><span style="color:#008080">add</span><span>(</span><span style="color:#dd2200">"ab7422e9-a91a-4840-9e59-9d911257c918"</span><span>);</span></span>
<span><span>idList</span><span>.</span><span style="color:#008080">add</span><span>(</span><span style="color:#dd2200">"12b6ceb8-573b-4f01-ad85-cfb24cfa007c"</span><span>);</span></span>
<span><span>idList</span><span>.</span><span style="color:#008080">add</span><span>(</span><span style="color:#dd2200">"dafd5ba4-d2e3-4656-bd42-178841e610fe"</span><span>);</span></span>
<span><span>service</span><span>.</span><span style="color:#008080">logicDelete</span><span>(</span><span>idList</span><span>);</span></span>
<span><span>&#125;</span></span>
<span></span>
<span><span>@Test</span></span>
<span><strong>public</strong> <strong>void</strong> <strong>batchDeleteByIds</strong><span>()</span> <strong>throws</strong> <strong>Exception</strong><span>&#123;</span></span>
<span><span>_logger</span><span>.</span><span style="color:#008080">info</span><span>(</span><span style="color:#dd2200">"batchDeleteByIds..."</span><span>);</span></span>
<span><span>service</span><span>.</span><span style="color:#008080">deleteBatch</span><span>(</span><span style="color:#dd2200">"2"</span><span>);</span></span>
<span><span>service</span><span>.</span><span style="color:#008080">deleteBatch</span><span>(</span><span style="color:#dd2200">"2,639178432667713536"</span><span>);</span></span>
<span><span>&#125;</span></span>

<span><span>@Test</span></span>
<span><strong>public</strong> <strong>void</strong> <strong>queryPageResults</strong><span>()</span> <strong>throws</strong> <strong>Exception</strong><span>&#123;</span></span>
<span><span>_logger</span><span>.</span><span style="color:#008080">info</span><span>(</span><span style="color:#dd2200">"queryPageResults..."</span><span>);</span></span>
<span> <strong>Students</strong> <span>student</span><span>=</span><strong>new</strong> <strong>Students</strong><span>();</span></span>
<span> <span style="color:#888888">//student.setId("af04d610-6092-481e-9558-30bd63ef783c");</span></span>
<span> <span style="color:#888888">//student.setStdGender("M");</span></span>
<span> <span style="color:#888888">//student.setStdMajor(政治");</span></span>
<span> <span>student</span><span>.</span><span style="color:#008080">setPageSize</span><span>(</span><span style="color:#009999">10</span><span>);</span></span>
<span> <span style="color:#888888">//student.setPageNumber(2);</span></span>
<span> <span>student</span><span>.</span><span style="color:#008080">calculate</span><span>(</span><span style="color:#009999">21</span><span>);</span></span>
<span> <strong>List</strong><span><</span><strong>Students</strong><span>></span> <span>allListStudents</span> <span>=</span> </span>
<span> <span>service</span><span>.</span><span style="color:#008080">queryPageResults</span><span>(</span><span>student</span><span>).</span><span style="color:#008080">getRows</span><span>();</span></span>
<span> <strong>for</strong> <span>(</span><strong>Students</strong> <span>s</span> <span>:</span> <span>allListStudents</span><span>)</span> <span>&#123;</span></span>
<span> <span>_logger</span><span>.</span><span style="color:#008080">info</span><span>(</span><span style="color:#dd2200">"Students "</span><span>+</span><span>s</span><span>);</span></span>
<span> <span>&#125;</span></span>
<span><span>&#125;</span></span>
<span></span>
<span><span>@Test</span></span>
<span><strong>public</strong> <strong>void</strong> <strong>queryPageResultsByMapperId</strong><span>()</span> <strong>throws</strong> <strong>Exception</strong><span>&#123;</span></span>
<span><span>_logger</span><span>.</span><span style="color:#008080">info</span><span>(</span><span style="color:#dd2200">"queryPageResults by mapperId..."</span><span>);</span></span>
<span> <strong>Students</strong> <span>student</span><span>=</span><strong>new</strong> <strong>Students</strong><span>();</span></span>
<span> <span>student</span><span>.</span><span style="color:#008080">setStdGender</span><span>(</span><span style="color:#dd2200">"M"</span><span>);</span></span>
<span> <span style="color:#888888">//student.setStdMajor(政治");</span></span>
<span> <span>student</span><span>.</span><span style="color:#008080">setPageSize</span><span>(</span><span style="color:#009999">10</span><span>);</span></span>
<span> <span>student</span><span>.</span><span style="color:#008080">setPageNumber</span><span>(</span><span style="color:#009999">2</span><span>);</span></span>
<span> <strong>List</strong><span><</span><strong>Students</strong><span>></span> <span>allListStudents</span> <span>=</span> </span>
<span> <span>service</span><span>.</span><span style="color:#008080">queryPageResults</span><span>(</span><span style="color:#dd2200">"queryPageResults1"</span><span>,</span><span>student</span><span>).</span><span style="color:#008080">getRows</span><span>();</span></span>
<span> <strong>for</strong> <span>(</span><strong>Students</strong> <span>s</span> <span>:</span> <span>allListStudents</span><span>)</span> <span>&#123;</span></span>
<span> <span>_logger</span><span>.</span><span style="color:#008080">info</span><span>(</span><span style="color:#dd2200">"Students "</span><span>+</span><span>s</span><span>);</span></span>
<span> <span>&#125;</span></span>
<span><span>&#125;</span></span>
<span></span>
<span><span>@Test</span></span>
<span><strong>public</strong> <strong>void</strong> <strong>query</strong><span>()</span> <strong>throws</strong> <strong>Exception</strong><span>&#123;</span></span>
<span><span>_logger</span><span>.</span><span style="color:#008080">info</span><span>(</span><span style="color:#dd2200">"findAll..."</span><span>);</span></span>
<span><strong>List</strong><span><</span><strong>Students</strong><span>></span> <span>allListStudents</span> <span>=</span><span>service</span><span>.</span><span style="color:#008080">query</span><span>(</span><strong>null</strong><span>);</span></span>
<span> <strong>for</strong> <span>(</span><strong>Students</strong> <span>s</span> <span>:</span> <span>allListStudents</span><span>)</span> <span>&#123;</span></span>
<span> <span>_logger</span><span>.</span><span style="color:#008080">info</span><span>(</span><span style="color:#dd2200">"Students "</span><span>+</span><span>s</span><span>);</span></span>
<span> <span>&#125;</span></span>
<span><span>&#125;</span></span>
<span></span>
<span><span>@Test</span></span>
<span><strong>public</strong> <strong>void</strong> <strong>findAll</strong><span>()</span> <strong>throws</strong> <strong>Exception</strong><span>&#123;</span></span>
<span><span>_logger</span><span>.</span><span style="color:#008080">info</span><span>(</span><span style="color:#dd2200">"findAll..."</span><span>);</span></span>
<span><strong>List</strong><span><</span><strong>Students</strong><span>></span> <span>allListStudents</span> <span>=</span><span>service</span><span>.</span><span style="color:#008080">findAll</span><span>();</span></span>
<span> <strong>for</strong> <span>(</span><strong>Students</strong> <span>s</span> <span>:</span> <span>allListStudents</span><span>)</span> <span>&#123;</span></span>
<span> <span>_logger</span><span>.</span><span style="color:#008080">info</span><span>(</span><span style="color:#dd2200">"Students "</span><span>+</span><span>s</span><span>);</span></span>
<span> <span>&#125;</span></span>
<span><span>&#125;</span></span>
<span></span>
<span><span>@Before</span></span>
<span><strong>public</strong> <strong>void</strong> <strong>initSpringContext</strong><span>()&#123;</span></span>
<span><strong>if</strong><span>(</span><span>context</span><span>!=</span><strong>null</strong><span>)</span> <strong>return</strong><span>;</span></span>
<span><span>_logger</span><span>.</span><span style="color:#008080">info</span><span>(</span><span style="color:#dd2200">"init Spring Context..."</span><span>);</span></span>
<span><strong>SimpleDateFormat</strong> <span>sdf_ymdhms</span> <span>=</span><strong>new</strong> <strong>SimpleDateFormat</strong><span>(</span><span style="color:#dd2200">"yyyy-MM-dd HH🇲🇲ss"</span><span>);</span></span>
<span><strong>String</strong> <span>startTime</span><span>=</span><span>sdf_ymdhms</span><span>.</span><span style="color:#008080">format</span><span>(</span><strong>new</strong> <strong>Date</strong><span>());</span></span>
<span><strong>try</strong><span>&#123;</span></span>
<span><strong>MyBatisTestRunner</strong> <span>runner</span><span>=</span><strong>new</strong> <strong>MyBatisTestRunner</strong><span>();</span></span>
<span><span>runner</span><span>.</span><span style="color:#008080">init</span><span>();</span></span>
<span><span>&#125;</span><strong>catch</strong><span>(</span><strong>Exception</strong> <span>e</span><span>)&#123;</span></span>
<span><span>e</span><span>.</span><span style="color:#008080">printStackTrace</span><span>();</span></span>
<span><span>&#125;</span></span>
<span><span>_logger</span><span>.</span><span style="color:#008080">info</span><span>(</span><span style="color:#dd2200">"-- --Init Start at "</span> <span>+</span> <span>startTime</span><span>+</span><span style="color:#dd2200">" , End at  "</span><span>+</span><span>sdf_ymdhms</span><span>.</span><span style="color:#008080">format</span><span>(</span><strong>new</strong> <strong>Date</strong><span>()));</span></span>
<span><span>&#125;</span></span>
<span></span>
<span><span style="color:#888888">//Initialization ApplicationContext for Project</span></span>
<span><strong>public</strong> <strong>void</strong> <strong>init</strong><span>()&#123;</span></span>
<span><span>_logger</span><span>.</span><span style="color:#008080">info</span><span>(</span><span style="color:#dd2200">"Application dir "</span><span>+</span><strong>System</strong><span>.</span><span style="color:#008080">getProperty</span><span>(</span><span style="color:#dd2200">"user.dir"</span><span>));</span></span>
<span><span>context</span> <span>=</span> <strong>new</strong> <strong>ClassPathXmlApplicationContext</strong><span>(</span><strong>new</strong> <strong>String</strong><span>[]</span> <span>&#123;</span><span style="color:#dd2200">"spring/applicationContext.xml"</span><span>&#125;);</span></span>
<span><strong>WebContext</strong><span>.</span><span style="color:#008080">applicationContext</span><span>=</span><span>context</span><span>;</span></span>
<span><span>service</span> <span>=(</span><strong>StudentsService</strong><span>)</span><strong>WebContext</strong><span>.</span><span style="color:#008080">getBean</span><span>(</span><span style="color:#dd2200">"studentsService"</span><span>);</span></span>
<span><span>&#125;</span></span>
<span><span>&#125;</span></span></pre> 
 </div> 
</div> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">版本更新</p> 
<p style="color:#40485b; margin-left:0em; margin-right:0em; text-align:start">代码优化</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">新增find方法，根据过滤器查询数据</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">新增insertBatch方法</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">新增deleteBatch方法</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">删除batchInsert方法</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">删除batchDelete方法</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">日志功能优化</p> 
<p style="color:#40485b; margin-left:0; margin-right:0; text-align:start">缓存调整为caffeine</p> 
<p style="color:#40485b; margin-left:0em; margin-right:0em; text-align:start">升级log4j2 2.17.0</p>
                                        </div>
                                      
</div>
            