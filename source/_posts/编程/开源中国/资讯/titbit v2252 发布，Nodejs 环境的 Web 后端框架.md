
---
title: 'titbit v22.5.2 发布，Node.js 环境的 Web 后端框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9996'
author: 开源中国
comments: false
date: Thu, 09 Sep 2021 22:52:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9996'
---

<div>   
<div class="content">
                                                                                            <p>titbit v22.5.2 已经发布，Node.js 环境的 Web 后端框架。</p> 
<p>此版本更新内容包括：</p> 
<p><strong>所有更改都不影响原有代码，只是对之前代码的规范化整理。</strong></p> 
<ul> 
 <li> <p>middleware函数运行后返回一个真实的中间件，把middleware名字改成了mid，符合midcore的加载规范。</p> </li> 
 <li> <p>monitor中获取系统平均进程数的格式化数值，去掉了模板字符串处理，微乎其微的提高了性能。</p> </li> 
</ul> 
<blockquote> 
 <p>midcore从v22.2.1开始，支持加载具有mid属性或者middleware属性作为中间件，要求：</p> 
 <ul> 
  <li>mid是一个普通函数，运行此函数要返回一个真正的中间件函数。</li> 
  <li>middleware则应该是一个完整的中间件函数，会自动进行this绑定（箭头函数无法绑定this）。</li> 
 </ul> 
</blockquote> 
<p>详情查看：<a blank="_target" href="https://gitee.com/daoio/titbit/releases/v22.5.2">https://gitee.com/daoio/titbit/releases/v22.5.2</a></p>
                                        </div>
                                      
</div>
            