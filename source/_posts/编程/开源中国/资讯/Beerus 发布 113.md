
---
title: 'Beerus 发布 1.1.3'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=5505'
author: 开源中国
comments: false
date: Mon, 20 Dec 2021 09:27:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=5505'
---

<div>   
<div class="content">
                                                                                            <p>本来应该多积累一些东西才发布新版的，但是我觉得这两个功能，有和没有的差距还是有一点点大的，会在一定程度上影响开发效率，所以就选择了赶紧发出来。</p> 
<h3>http请求支持同名多参数</h3> 
<p>以前 如果一个请求中包含了 同名的多个参数，那么beerus只会获取一个，现在对这个功能进行了升级，可以一次性把所有同名参数都获取到。</p> 
<p><strong>1. 传统方式</strong></p> 
<p>支持 urlencode 和 get请求</p> 
<pre><code class="language-go">req.FormValues("name")</code></pre> 
<p><strong>2. 实体接收</strong></p> 
<p>支持 urlencode，JSON 和 get请求</p> 
<pre><code>type DemoParam struct &#123;

TestReception []string
&#125;</code></pre> 
<h3>DB的条件构造器支持多参数</h3> 
<p><strong>比如有这么一个条件</strong></p> 
<p>where id > 10 and (name = 'bee' or age > 18)</p> 
<p>以前的条件构造器是不支持的，现在支持了，只需要这么写即可</p> 
<pre><code class="language-go">conditions := make([]*entity.Condition,0)
conditions = append(conditions, entity.GetCondition("id > ?", 10))
conditions = append(conditions, entity.GetCondition("and (name = ? or age > ?)", "bee", 18))

resultMap, err := operation.GetDBTemplate("Data source name").Select("table name", conditions)</code></pre> 
<p>感兴趣的伙伴们可以访问官网，了解更多：https://beeruscc.com</p>
                                        </div>
                                      
</div>
            