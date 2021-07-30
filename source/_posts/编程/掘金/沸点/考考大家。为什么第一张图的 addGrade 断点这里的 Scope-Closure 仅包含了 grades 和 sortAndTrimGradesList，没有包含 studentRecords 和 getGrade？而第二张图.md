
---
title: '考考大家。为什么第一张图的 addGrade 断点这里的 Scope-Closure 仅包含了 grades 和 sortAndTrimGradesList，没有包含 studentRecords 和 getGrade？而第二张图...'
categories: 
 - 编程
 - 掘金
 - 沸点
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/075d9a0a6b704da0a4558bc1023fbcf4~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 29 Jul 2021 16:20:11 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/075d9a0a6b704da0a4558bc1023fbcf4~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
考考大家。为什么第一张图的 addGrade 断点这里的 Scope-Closure 仅包含了 grades 和 sortAndTrimGradesList，没有包含 studentRecords 和 getGrade？而第二张图 getInfo 断点这里的 Scope-Closure 包含了入参的 grade、id、name 三个～ 闭包相关知识<br>
            
          <img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/075d9a0a6b704da0a4558bc1023fbcf4~tplv-k3u1fbpfcp-watermark.image" referrerpolicy="no-referrer"><br>
        
          <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d590def2c89844f68831e51f1e7dc313~tplv-k3u1fbpfcp-watermark.image" referrerpolicy="no-referrer"><br>
        <br>
          
</div>
            