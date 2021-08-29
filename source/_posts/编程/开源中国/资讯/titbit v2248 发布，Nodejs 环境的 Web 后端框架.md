
---
title: 'titbit v22.4.8 发布，Node.js 环境的 Web 后端框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=4754'
author: 开源中国
comments: false
date: Sat, 28 Aug 2021 08:26:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=4754'
---

<div>   
<div class="content">
                                                                                            <p>titbit v22.4.8 已经发布，Node.js 环境的 Web 后端框架。</p> 
<p>此版本更新内容包括：</p> 
<ul> 
 <li> <p>titbit.js 调整monitorTimeSlice为500毫秒，此数值不宜太低，实测建议在300毫秒以上，否则容易出现实际进程数量比autoWorker设置的最大值多一个的情况，这和设备性能有关，因为灵敏度太高，此时创建worker等一系列操作还没有完成就会出现继续创建的情况。</p> </li> 
 <li> <p>http2.js 去掉了早期代码判断stream.session.destroyed属性的情况，只需要stream.writable或stream.closed或stream.destroyed即可。</p> </li> 
</ul> 
<p>详情查看：<a href="https://gitee.com/daoio/titbit/releases/v22.4.8">https://gitee.com/daoio/titbit/releases/v22.4.8</a></p>
                                        </div>
                                      
</div>
            