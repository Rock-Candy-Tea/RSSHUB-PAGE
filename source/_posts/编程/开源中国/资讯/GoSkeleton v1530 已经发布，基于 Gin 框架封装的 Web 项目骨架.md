
---
title: 'GoSkeleton v1.5.30 已经发布，基于 Gin 框架封装的 Web 项目骨架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=912'
author: 开源中国
comments: false
date: Sun, 28 Nov 2021 21:38:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=912'
---

<div>   
<div class="content">
                                                                                            <p>GoSkeleton v1.5.30 已经发布，基于 Gin 框架封装的 Web 项目骨架</p> 
<p>此版本更新内容包括：</p> 
<h4>V 1.5.30 2021-11-28</h4> 
<ul> 
 <li>新增<br> 1.引入表单参数验证器全局自动翻译器,简化代码书写,提升开发效率.</li> 
 <li>更新<br> 1.按照gin官方提示,当程序切换到生产模式时,对gin的路由进行二次封装、异常恢复中间件自定义重写,release模式经过并发测试可以获得5%的性能提升.<br> 1.1 当配置文件(config/config.yml)中的键 <code>AppDebug</code> 设置为 <code>false</code> 时,gin 路由默认启用 <code>release</code> 模式，并且不会记录接口访问日志,生产环境请使用 <code>nginx</code> 代理，也方便实现负载均衡.<br> 2.其他更新主要是一些细节：文档、程序注释方面.</li> 
</ul> 
<p>详情查看：<a href="https://gitee.com/daitougege/GinSkeleton/releases/v1.5.30">https://gitee.com/daitougege/GinSkeleton/releases/v1.5.30</a></p>
                                        </div>
                                      
</div>
            