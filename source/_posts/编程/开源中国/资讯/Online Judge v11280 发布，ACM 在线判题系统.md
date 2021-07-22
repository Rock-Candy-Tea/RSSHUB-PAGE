
---
title: 'Online Judge v1.1.280 发布，ACM 在线判题系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=3209'
author: 开源中国
comments: false
date: Wed, 21 Jul 2021 19:58:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=3209'
---

<div>   
<div class="content">
                                                                                            <p>Online Judge v1.1.280 已经发布，ACM在线判题系统</p> 
<p>此版本更新内容包括：</p> 
<p>1、扩展web与judger通信消息长度支持8字节。 <strong>（升级需要注意）</strong></p> 
<pre><code>如：长度由0x0150变为0x00000150
abcddcba000200000150&#123;"language_id":"4","time":"","session_id":"EB804425B5B92A2F433ED26CF1738BF4","problem_id":"1000","input":"1 2","verdict":"","code":"#include <stdio.h>\r\nint main(void)\r\n&#123;\r\n    int a,b;\r\n    while(scanf(\"69277786928600\", &a,&b) != EOF)\r\n        printf(\"0\\n\",a+b+1);\r\n    return 0;\r\n&#125;","output":"","compile_error":"","memory":""&#125;
</code></pre> 
<p>2、web端题目和提交界面合并，可伸缩</p> 
<p>详情查看：<a href="https://gitee.com/jungle/online-judge/releases/v1.1.280">https://gitee.com/jungle/online-judge/releases/v1.1.280</a></p>
                                        </div>
                                      
</div>
            