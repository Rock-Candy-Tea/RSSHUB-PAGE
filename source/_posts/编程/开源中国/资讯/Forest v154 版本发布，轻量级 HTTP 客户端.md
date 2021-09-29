
---
title: 'Forest v1.5.4 版本发布，轻量级 HTTP 客户端'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4143'
author: 开源中国
comments: false
date: Wed, 29 Sep 2021 18:08:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4143'
---

<div>   
<div class="content">
                                                                    
                                                        <p style="color:#333333; margin-left:0; margin-right:0; text-align:left"><strong>Forest v1.5.4</strong> 发布。</p> 
<p style="color:#333333; margin-left:0; margin-right:0; text-align:left">此版本主要解决一些遗留问题，此外补充一些接口</p> 
<h2 style="margin-left:0; margin-right:0; text-align:left">URL查询参数相关接口</h2> 
<ol style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>添加 Map 作为URL查询参数</li> 
</ol> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code>// 将Map中的每个键值对作为Query参数加到请求中
Map<String, Object> map = new LinkedHashMap<>();
map.put("a", 1);
map.put("b", 2);
map.put("c", 3);

Forest.get("/")
     // 添加 Map 到 Query参数
    .addQuery(map)
     // 执行请求
    .execute();
// query参数为 a=1&b=2&c=3
</code></pre> 
<ol start="2" style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>添加数组和列表到URL查询参数中</li> 
</ol> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code>// 添加列表到Query参数
Forest.get("/")
     .addQuery("a", Arrays.asList(1, 2, 3))
     .execute();
// query参数为 a=1&a=2&a=3

// 添加数组到Query参数
Forest.get("/")
     .addQuery("a", new Object[] &#123;1, 2, 3&#125;)
     .execute();
// query参数为 a=1&a=2&a=3

</code></pre> 
<ol start="3" style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>添加数组和列表到URL数组查询参数(带[]的参数名)中</li> 
</ol> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code>// 添加列表到Query数组参数
Forest.get("/")
     .addArrayQuery("a", Arrays.asList(1, 2, 3))
     .execute();
// query参数为 a[]=1&a[]=2&a[]=3

// 添加数组到Query数组参数
Forest.get("/")
     .addArrayQuery("a", new Object[] &#123;1, 2, 3&#125;)
     .execute();
// query参数为 a[]=1&a[]=2&a[]=3
</code></pre> 
<ol start="4" style="list-style-type:decimal; margin-left:0; margin-right:0"> 
 <li>添加JSON数据到URL查询参数中</li> 
</ol> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code>// 添加列表到Query数组参数
Forest.get("/")
     .addJSONQuery("a", Arrays.asList(1, 2, 3))
     .execute();
// query参数为 a=[1,2,3]
// 注意：这里的JSON数据最终会被 URLEncode
// 所以最终请求的参数为 a=%5B1%2C2%2C3%5D
</code></pre> 
<h2 style="margin-left:0; margin-right:0; text-align:left">Fix的Bug</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>fix: 依赖Guava包 (#I4CC9B)</li> 
 <li>fix:<span> </span><code>@Query</code>注解修饰Map参数时，Map中的列表属性无法正常序列化 (#I4C8UC)</li> 
 <li>fix: 多线程下的并发问题</li> 
</ul> 
<h2 style="margin-left:0; margin-right:0; text-align:left">代码改动</h2> 
<ul style="list-style-type:disc; margin-left:0; margin-right:0"> 
 <li>update: 去掉多余的DEBUG日志</li> 
 <li>add: ForestLogHandler.logContent(String content) 方法</li> 
 <li>add: ForestRequest.addQuery(String name, Collection collection) 方法</li> 
 <li>add: ForestRequest.addQuery(String name, Object... array) 方法</li> 
 <li>add: ForestRequest.addArrayQuery(String name, Collection collection) 方法</li> 
 <li>add: ForestRequest.addArrayQuery(String name, Object... array) 方法</li> 
</ul> 
<h2><strong>官网地址</strong></h2> 
<p><a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fforest.dtflyx.com" target="_blank">http://forest.dtflyx.com</a></p>
                                        </div>
                                      
</div>
            