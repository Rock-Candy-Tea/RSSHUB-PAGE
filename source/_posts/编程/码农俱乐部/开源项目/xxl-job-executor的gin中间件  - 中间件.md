
---
title: 'xxl-job-executor的gin中间件  - 中间件'
categories: 
 - 编程
 - 码农俱乐部
 - 开源项目
headimg: 'https://picsum.photos/400/300?random=4412'
author: 码农俱乐部
comments: false
date: 2021-11-09 08:09:39
thumbnail: 'https://picsum.photos/400/300?random=4412'
---

<div>   
xxl-job-executor 的 Gin 中间件
背景
xxl-job-executor-go 是 xxl-job 的 golang 执行器，可以独立运行，有时候我们要与项目或者框架（如：gin 框架）集成起来合并为一个服务，本项目因此而生。
执行器项目地址
https://github.com/xxl-job/xxl-job-executor-go
与 Gin 集成示例
package main

import (
"github.com/gin-gonic/gin"
"github.com/gi...
          
</div>
            