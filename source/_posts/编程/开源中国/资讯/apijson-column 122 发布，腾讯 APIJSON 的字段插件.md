
---
title: 'apijson-column 1.2.2 发布，腾讯 APIJSON 的字段插件'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://user-images.githubusercontent.com/5738175/113572899-ab903380-964b-11eb-9f3c-69f3437d8a54.png'
author: 开源中国
comments: false
date: Fri, 08 Jul 2022 10:06:00 GMT
thumbnail: 'https://user-images.githubusercontent.com/5738175/113572899-ab903380-964b-11eb-9f3c-69f3437d8a54.png'
---

<div>   
<div class="content">
                                                                                            <p><img alt="image" src="https://user-images.githubusercontent.com/5738175/113572899-ab903380-964b-11eb-9f3c-69f3437d8a54.png" referrerpolicy="no-referrer"></p> 
<p><img alt="image" src="https://user-images.githubusercontent.com/5738175/113572926-b77bf580-964b-11eb-8a17-10917669c2aa.png" referrerpolicy="no-referrer"></p> 
<p><strong>apijson-column 1.0.0-1.2.2 更新内容</strong></p> 
<ul> 
 <li> <p style="color:#24292f; text-align:start"><span style="background-color:#ffffff; color:#24292f">支持 字段名映射 和 !key 反选字段；</span></p> </li> 
 <li> <p style="color:#24292f; text-align:start"><span style="background-color:#ffffff; color:#24292f">完善文档；</span></p> </li> 
 <li> <p style="color:#24292f; text-align:start"> </p> <p style="color:#24292f; text-align:start">升级自身, APIJSON 版本分别为 1.2.2, 5.1.0；</p> </li> 
</ul> 
<p>具体见 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2FAPIJSON%2Fapijson-column%2Freleases" target="_blank">Release 发布版本</a>。</p> 
<h1> </h1> 
<h1>apijson-column<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fjitpack.io%2F%23APIJSON%2Fapijson-column" target="_blank"><img alt src="https://camo.githubusercontent.com/8dac7121e8d02ac614953deab241d41f47d3db73ea8c42191d8f1d5e12b679be/68747470733a2f2f6a69747061636b2e696f2f762f4150494a534f4e2f6170696a736f6e2d636f6c756d6e2e737667" referrerpolicy="no-referrer"></a></h1> 
<p style="color:#24292f; text-align:start">腾讯<span> </span><a href="https://gitee.com/Tencent/APIJSON">APIJSON</a><span> </span>4.6.6+ 的字段插件，支持 !key 反选字段 和 字段名映射，可通过 Maven, Gradle 等远程依赖。</p> 
<p style="color:#24292f; text-align:start"> </p> 
<h3>1.反选字段</h3> 
<p style="color:#24292f; text-align:start">"@column": "!columnKey" // 返回排除 columnKey 后的全部其它字段</p> 
<div> 
 <pre><span>&#123;</span>
    <span style="color:var(--color-prettylights-syntax-string)">"User"</span>: <span>&#123;</span>  <span style="color:var(--color-prettylights-syntax-comment)">// id,sex,name,tag,head,contactIdList,pictureList,date</span>
        <span style="color:var(--color-prettylights-syntax-string)">"id"</span>: <span style="color:var(--color-prettylights-syntax-constant)">82001</span><span>,</span>
        <span style="color:var(--color-prettylights-syntax-string)">"@column"</span>: <span style="color:var(--color-prettylights-syntax-string)">"!contactIdList"</span>  <span style="color:var(--color-prettylights-syntax-comment)">// -> id,sex,name,tag,head,pictureList,date</span>
    <span>&#125;</span>
<span>&#125;</span></pre> 
</div> 
<p style="color:#24292f; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F5738175%2F113572899-ab903380-964b-11eb-9f3c-69f3437d8a54.png" target="_blank"><img alt="image" src="https://user-images.githubusercontent.com/5738175/113572899-ab903380-964b-11eb-9f3c-69f3437d8a54.png" referrerpolicy="no-referrer"></a></p> 
<h3>2.字段名映射</h3> 
<p style="color:#24292f; text-align:start">"@column": "showKey" // 隐藏了数据库的对应真实字段名</p> 
<div> 
 <pre><span>&#123;</span>
    <span style="color:var(--color-prettylights-syntax-string)">"User"</span>: <span>&#123;</span>  <span style="color:var(--color-prettylights-syntax-comment)">// id,sex,name,tag,head,contactIdList,pictureList,date</span>
        <span style="color:var(--color-prettylights-syntax-string)">"id"</span>: <span style="color:var(--color-prettylights-syntax-constant)">82001</span><span>,</span>
        <span style="color:var(--color-prettylights-syntax-string)">"@column"</span>: <span style="color:var(--color-prettylights-syntax-string)">"gender"</span>  <span style="color:var(--color-prettylights-syntax-comment)">// -> sex </span>
    <span>&#125;</span>
<span>&#125;</span></pre> 
</div> 
<p style="color:#24292f; text-align:start"><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fuser-images.githubusercontent.com%2F5738175%2F113572926-b77bf580-964b-11eb-8a17-10917669c2aa.png" target="_blank"><img alt="image" src="https://user-images.githubusercontent.com/5738175/113572926-b77bf580-964b-11eb-8a17-10917669c2aa.png" referrerpolicy="no-referrer"></a></p> 
<p> </p> 
<p><a href="https://gitee.com/APIJSON/apijson-column">https://gitee.com/APIJSON/apijson-column</a></p> 
<p>创作不易，右上角点 ⭐Star 支持下吧 ^_^</p> 
<p> </p>
                                        </div>
                                      
</div>
            